#!/usr/bin/env python3
"""Fetch an Oracle Help Center guide by following only same-guide Next links.

This is a PDF-download fallback, not a replacement for the official PDF: HTML page
sequence numbers are not Oracle printed pages or physical PDF page numbers.
Outputs default to .local/oracle-docs/<DOC-ID>-html/ (git-ignored).
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag
from urllib.request import Request, urlopen


SKIP_TAGS = {"script", "style", "nav", "footer", "aside", "noscript", "svg"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


def guide_scope(url: str, index_url: str) -> bool:
    target, root = urlparse(url), urlparse(index_url)
    prefix = root.path.rsplit("/", 1)[0].rstrip("/") + "/"
    return target.scheme == "https" and target.netloc.lower() == root.netloc.lower() and target.path.startswith(prefix) and not target.path.lower().endswith((".pdf", ".zip", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".css", ".js"))


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self.active = [], None

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            a = dict(attrs)
            self.active = {"href": a.get("href", ""), "rel": a.get("rel", ""), "class": a.get("class", ""), "text": []}

    def handle_data(self, data):
        if self.active is not None:
            self.active["text"].append(data)

    def handle_endtag(self, tag):
        if tag.lower() == "a" and self.active is not None:
            link = self.active
            link["text"] = re.sub(r"\s+", " ", "".join(link["text"])).strip()
            self.links.append(link)
            self.active = None


def next_page_url(source: str, current_url: str, index_url: str) -> str | None:
    parser = LinkParser()
    parser.feed(source)
    for link in parser.links:
        label = link["text"].lower().strip(" .›»→")
        rel = set(link["rel"].lower().split())
        classes = set(re.sub(r"[^a-z0-9 -]", " ", link["class"].lower()).split())
        if not ("next" in rel or "next" in classes or label in {"next", "next page", "next topic", "next chapter"}):
            continue
        href = link["href"].strip()
        if not href or href.startswith(("#", "javascript:", "mailto:")):
            continue
        candidate = urldefrag(urljoin(current_url, href))[0]
        if candidate != current_url and guide_scope(candidate, index_url):
            return candidate
    return None


class MarkdownParser(HTMLParser):
    def __init__(self, base_url: str = ""):
        super().__init__(convert_charrefs=True)
        self.parts, self.stack = [], []
        self.base_url = base_url
        self.anchors = []
        self.skip_depth = 0
        self.skip_stack = []
        self.table = None
        self.row = None
        self.cell = None

    def emit(self, text):
        if self.cell is not None:
            self.cell.append(text)
        else:
            self.parts.append(text)

    def newline(self, count=2):
        target = self.cell if self.cell is not None else self.parts
        joined = "".join(target)
        want = "\n" * count
        if joined and not joined.endswith(want):
            target.append("\n" * max(1, count - len(joined) + len(joined.rstrip("\n"))))

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if self.skip_depth:
            if tag not in VOID:
                self.skip_depth += 1
                self.skip_stack.append(tag)
            return
        if tag in SKIP_TAGS:
            if tag not in VOID:
                self.skip_depth, self.skip_stack = 1, [tag]
            return
        if tag == "a":
            href = attr.get("href", "").strip()
            if href and not href.startswith(("javascript:", "mailto:", "#")):
                from urllib.parse import urljoin
                self.anchors.append(urljoin(self.base_url, href) if self.base_url else href)
                self.emit("[")
            else:
                self.anchors.append(None)
        elif tag == "table":
            self.newline(2); self.table, self.row = [], None
        elif tag == "tr" and self.table is not None:
            self.row = []
        elif tag in {"td", "th"} and self.table is not None:
            self.cell = []
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.newline(2); self.emit("#" * int(tag[1]) + " ")
        elif tag == "p" or tag in {"section", "article", "main", "div"}:
            self.newline(2)
        elif tag == "br":
            self.newline(1)
        elif tag == "li":
            self.newline(1); self.emit("- ")
        elif tag == "pre":
            self.newline(2); self.emit("    ")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if self.skip_depth:
            if self.skip_stack and tag == self.skip_stack[-1]:
                self.skip_stack.pop(); self.skip_depth -= 1
            return
        if tag == "a":
            href = self.anchors.pop() if self.anchors else None
            if href:
                self.emit("](" + href + ")")
        elif tag in {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "pre", "section", "article", "div", "main"}:
            self.newline(2 if tag != "li" else 1)
        elif tag in {"td", "th"} and self.cell is not None and self.row is not None:
            self.row.append(re.sub(r"\s+", " ", "".join(self.cell)).strip()); self.cell = None
        elif tag == "tr" and self.table is not None and self.row is not None:
            if self.row:
                self.table.append(self.row)
            self.row = None
        elif tag == "table" and self.table is not None:
            rows = self.table
            if rows:
                width = max(len(r) for r in rows)
                padded = [r + [""] * (width-len(r)) for r in rows]
                self.parts.append("\n" + "| " + " | ".join(padded[0]) + " |\n")
                self.parts.append("| " + " | ".join("---" for _ in range(width)) + " |\n")
                for row in padded[1:]:
                    self.parts.append("| " + " | ".join(row) + " |\n")
                self.parts.append("\n")
            self.table = None

    def handle_data(self, data):
        if not self.skip_depth:
            self.emit(data)

    def markdown(self):
        text = "".join(self.parts).replace("\xa0", " ")
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def fetch(url: str, timeout: int, user_agent: str) -> bytes:
    request = Request(url, headers={"User-Agent": user_agent, "Accept": "text/html,application/xhtml+xml"})
    with urlopen(request, timeout=timeout) as response:
        if "html" not in response.headers.get("Content-Type", "").lower():
            raise RuntimeError(f"Expected HTML at {url}; got {response.headers.get('Content-Type')}")
        return response.read()


def chunks(text: str, doc_id: str, title: str, edition: str, canonical_url: str, pages: list[dict], size: int, overlap: int):
    words = list(re.finditer(r"\S+", text))
    markers = [(m.start(), int(m.group(1)), m.group(2)) for m in re.finditer(r"<!-- source-html-page: (\d+) \| url: (\S+) -->", text)]
    start = 0
    while start < len(words):
        end = min(len(words), start + size)
        first, last = words[start].start(), words[end-1].end()
        start_seq = end_seq = None
        start_url = end_url = None
        for offset, seq, url in markers:
            if offset <= first:
                start_seq, start_url = seq, url
            if offset <= last:
                end_seq, end_url = seq, url
            else:
                break
        body = text[first:last]
        yield {
            "chunk_id": f"{doc_id.lower()}-html-{start+1:07d}",
            "doc_id": doc_id, "title": title, "edition": edition or None,
            "canonical_url": canonical_url, "source_kind": "oracle-help-center-html",
            "source_html_sequence_start": start_seq, "source_html_sequence_end": end_seq,
            "source_url_start": start_url, "source_url_end": end_url,
            "word_start": start, "word_end_exclusive": end, "text": body,
        }
        if end == len(words):
            break
        start = max(start + 1, end - overlap)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index-url", required=True)
    parser.add_argument("--doc-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--edition", default="")
    parser.add_argument("--canonical-url", default="")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--max-pages", type=int, default=300)
    parser.add_argument("--delay-seconds", type=float, default=0.3)
    parser.add_argument("--timeout", type=int, default=15)
    parser.add_argument("--max-words", type=int, default=520)
    parser.add_argument("--overlap", type=int, default=70)
    parser.add_argument("--user-agent", default="OracleHCM-ReferenceIngest/1.0")
    args = parser.parse_args()
    if not args.index_url.startswith("https://") or not guide_scope(args.index_url, args.index_url):
        parser.error("--index-url must be a valid HTTPS Oracle guide index URL")
    if args.max_pages < 1 or args.max_words < 50 or not 0 <= args.overlap < args.max_words:
        parser.error("invalid page/chunk bounds")
    output = args.output_dir.resolve() if args.output_dir else Path.cwd()/".local"/"oracle-docs"/(args.doc_id.lower()+"-html")
    output.mkdir(parents=True, exist_ok=True)
    current, seen, pages, manifest_pages = args.index_url, set(), [], []
    for sequence in range(1, args.max_pages + 1):
        if current in seen:
            raise SystemExit(f"Next-link loop detected at {current}")
        seen.add(current)
        try:
            raw = fetch(current, args.timeout, args.user_agent)
        except Exception as exc:
            raise SystemExit(f"Fetch failed at sequence {sequence} ({current}): {exc}. No complete corpus was claimed.")
        html = raw.decode("utf-8", errors="replace")
        parser_html = MarkdownParser(current); parser_html.feed(html)
        title = args.title if sequence == 1 else args.title
        page_md = f"# {title} — HTML sequence {sequence}\n\n<!-- source-html-page: {sequence} | url: {current} -->\n\nSource: {current}\n\n" + parser_html.markdown()
        pages.append(page_md)
        target = output/"pages"/f"page-{sequence:04d}.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page_md, encoding="utf-8")
        manifest_pages.append({"sequence":sequence,"url":current,"sha256":hashlib.sha256(raw).hexdigest(),"bytes":len(raw),"markdown_chars":len(parser_html.markdown())})
        next_url = next_page_url(html, current, args.index_url)
        if not next_url:
            break
        current = next_url
        time.sleep(args.delay_seconds)
    full_text = "# "+args.title+"\n\n> HTML-derived; page sequence is not Oracle printed pagination or PDF page numbering.\n\n" + "\n\n---\n\n".join(pages)
    (output/"full-text.md").write_text(full_text, encoding="utf-8")
    with (output/"retrieval-chunks.jsonl").open("w", encoding="utf-8") as f:
        count = 0
        for item in chunks(full_text,args.doc_id,args.title,args.edition,args.canonical_url or args.index_url,manifest_pages,args.max_words,args.overlap):
            f.write(json.dumps(item,ensure_ascii=False)+"\n"); count += 1
    manifest = {
        "doc_id":args.doc_id,"title":args.title,"edition":args.edition or None,
        "canonical_url":args.canonical_url or args.index_url,"start_url":args.index_url,
        "source_kind":"oracle-help-center-html","pages_fetched":len(manifest_pages),
        "terminated_by_next_link":len(manifest_pages)<args.max_pages,
        "stopped_at_max_pages":len(manifest_pages)==args.max_pages,
        "pages":manifest_pages,"chunk_count":count,
        "processed_at_utc":datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "warning":"HTML sequence numbers are not Oracle printed/PDF pages; verify guide completeness before use."
    }
    (output/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"output_dir":str(output),"pages_fetched":len(manifest_pages),"chunks":count,"terminated_by_next_link":manifest["terminated_by_next_link"],"stopped_at_max_pages":manifest["stopped_at_max_pages"]},indent=2))


if __name__ == "__main__":
    main()
