#!/usr/bin/env python3
"""Source-aware local retrieval for official Oracle HCM module documentation.

Original manuals, fetched HTML text, PDF caches, and the SQLite index stay local
under .cache/oracle-hcm and are excluded from Git.
"""
from __future__ import annotations

import argparse
import hashlib
import html
from html.parser import HTMLParser
import json
import re
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST_PATH = ROOT / ".project/docs/oracle/ORC/source-manifest.json"
MANIFEST_PATH = DEFAULT_MANIFEST_PATH
CACHE_ROOT = ROOT / ".cache/oracle-hcm"
CACHE_DIR = CACHE_ROOT / "orc"
DOCUMENTS_DIR = CACHE_DIR / "documents"
DB_PATH = CACHE_DIR / "index.sqlite3"
STATUS_PATH = MANIFEST_PATH.parent / "source-status.json"
USER_AGENT = "oracle-hcm-knowledge-index/1.0 (official-document metadata and local search)"
DEFAULT_TIMEOUT = 25


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def today() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def load_manifest(path: Path | None = None) -> dict:
    actual_path = path or MANIFEST_PATH
    data = json.loads(actual_path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or not data.get("module_code"):
        raise ValueError(f"Unsupported or incomplete source manifest: {actual_path}")
    for source in data.get("sources", []):
        for key in ("html_url", "pdf_url"):
            url = source.get(key)
            if url and urlsplit(url).hostname not in data["source_policy"]["allowed_hosts"]:
                raise ValueError(f"Disallowed source host in manifest: {url}")
        if source.get("source_type") == "release_discovery_pattern":
            if not source.get("release_url_template") or not source.get("required_title_terms"):
                raise ValueError("Release discovery patterns must define release_url_template and required_title_terms.")
    return data


def configure_paths(manifest_path: Path) -> None:
    """Select a module manifest and isolate its cache, index, and status snapshot."""
    global MANIFEST_PATH, CACHE_DIR, DOCUMENTS_DIR, DB_PATH, STATUS_PATH
    MANIFEST_PATH = manifest_path if manifest_path.is_absolute() else ROOT / manifest_path
    data = load_manifest(MANIFEST_PATH)
    module_key = re.sub(r"[^a-z0-9_-]", "", data["module_code"].lower())
    if not module_key:
        raise ValueError("Manifest module_code must contain letters or digits.")
    CACHE_DIR = CACHE_ROOT / module_key
    DOCUMENTS_DIR = CACHE_DIR / "documents"
    DB_PATH = CACHE_DIR / "index.sqlite3"
    STATUS_PATH = MANIFEST_PATH.parent / "source-status.json"


class PageParser(HTMLParser):
    """Extract visible text, headings and same-page links without JS execution."""

    SKIP = {"script", "style", "noscript", "svg", "template"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.links: list[str] = []
        self.headings: list[str] = []
        self._skip_depth = 0
        self._heading_depth = 0
        self._heading_parts: list[str] = []
        self.title_parts: list[str] = []
        self._in_title = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag in self.SKIP:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if tag == "a" and attrs_dict.get("href"):
            self.links.append(attrs_dict["href"] or "")
        if tag == "title":
            self._in_title += 1
        if tag in {"h1", "h2", "h3", "h4"}:
            self._heading_depth += 1
            self._heading_parts = []
        if tag in {"p", "br", "li", "tr", "div", "section", "article"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in self.SKIP:
            if self._skip_depth:
                self._skip_depth -= 1
            return
        if self._skip_depth:
            return
        if tag == "title" and self._in_title:
            self._in_title -= 1
        if tag in {"h1", "h2", "h3", "h4"} and self._heading_depth:
            heading = clean_text(" ".join(self._heading_parts))
            if heading:
                self.headings.append(heading)
                self.parts.append("\n")
                self.parts.append(heading)
                self.parts.append("\n")
            self._heading_depth -= 1
            self._heading_parts = []
        if tag in {"p", "li", "tr", "div", "section", "article"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        value = data.strip()
        if not value:
            return
        if self._in_title:
            self.title_parts.append(value)
        self.parts.append(value)
        self.parts.append(" ")
        if self._heading_depth:
            self._heading_parts.append(value)

    @property
    def title(self) -> str:
        return clean_text(" ".join(self.title_parts))

    @property
    def text(self) -> str:
        return clean_text(" ".join(self.parts))


def clean_text(value: str) -> str:
    value = html.unescape(value)
    value = value.replace("\u00a0", " ")
    value = re.sub(r"[ \t\r\f\v]+", " ", value)
    value = re.sub(r" *\n+ *", "\n", value)
    return value.strip()


def canonical_url(url: str) -> str:
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, ""))


def fetch(url: str, timeout: int = DEFAULT_TIMEOUT) -> tuple[bytes, dict, int]:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/pdf,*/*"})
    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read()
            return body, dict(response.headers.items()), int(response.status)
    except HTTPError as exc:
        return exc.read(1024 * 64), dict(exc.headers.items()), int(exc.code)
    except (URLError, TimeoutError, OSError) as exc:
        raise RuntimeError(f"Fetch failed for {url}: {exc}") from exc


def parse_html(body: bytes) -> PageParser:
    parser = PageParser()
    parser.feed(body.decode("utf-8", errors="replace"))
    parser.close()
    return parser


def get_status_sources(manifest: dict) -> list[dict]:
    items = []
    for source in manifest["sources"]:
        if source.get("source_type") == "release_discovery_pattern":
            continue
        for key in ("html_url", "pdf_url"):
            if source.get(key):
                items.append({
                    "source_id": source["source_id"],
                    "title": source["title"],
                    "kind": "pdf" if key == "pdf_url" else "html",
                    "url": source[key],
                    "release": source.get("release", source.get("release_binding", "rolling")),
                    "expected_pdf_pages": source.get("expected_pdf_pages")
                })
    return items


def release_candidates(manifest: dict) -> list[tuple[str, str]]:
    pattern = next((s for s in manifest["sources"] if s.get("source_type") == "release_discovery_pattern"), None)
    if not pattern:
        return []
    output = []
    for candidate in pattern.get("release_candidates", []):
        release = candidate.lower()
        output.append((candidate.upper(), pattern["release_url_template"].format(release=release)))
    return output


def discover_latest_release(manifest: dict, timeout: int = 10) -> dict | None:
    pattern = next((s for s in manifest["sources"] if s.get("source_type") == "release_discovery_pattern"), None)
    required_terms = [term.lower() for term in (pattern or {}).get("required_title_terms", [])]
    if not required_terms:
        return None

    # Prefer Oracle's central readiness index over guessing a module-specific path.
    index_links: list[str] = []
    discovery_index = (pattern or {}).get("discovery_index_url")
    slug = (pattern or {}).get("release_slug")
    if discovery_index and slug:
        try:
            index_body, index_headers, index_status = fetch(discovery_index, timeout=timeout)
            if 200 <= index_status < 300:
                index_parser = parse_html(index_body)
                index_links = [
                    canonical_url(urljoin(discovery_index, link))
                    for link in index_parser.links
                    if urlsplit(urljoin(discovery_index, link)).hostname == "docs.oracle.com"
                ]
        except RuntimeError:
            index_links = []

    for release, fallback_url in release_candidates(manifest):
        lower = release.lower()
        candidates = [
            link for link in index_links
            if f"/{lower}/" in urlsplit(link).path.lower()
            and f"/{slug}-{lower}/" in urlsplit(link).path.lower()
        ]
        if not candidates:
            candidates = [fallback_url]
        for url in candidates:
            try:
                body, headers, status = fetch(url, timeout=timeout)
            except RuntimeError:
                continue
            if status < 200 or status >= 300:
                continue
            parser = parse_html(body)
            joined = (parser.title + " " + parser.text[:8000]).lower()
            # Reject Oracle's generic/fallback pages; require module term and release marker.
            if all(term in joined for term in required_terms) and ("what's new" in joined or "whats new" in joined):
                prefix_template = (pattern or {}).get("release_crawl_prefix_template")
                crawl_prefix = prefix_template.format(release=lower, slug=slug) if prefix_template else None
                return {
                    "release": release,
                    "url": url,
                    "crawl_prefix": crawl_prefix,
                    "title": parser.title or f"{manifest['module_name']} {release} What's New",
                    "http_status": status,
                    "sha256": hashlib.sha256(body).hexdigest(),
                    "content_type": headers.get("Content-Type", ""),
                    "content_length": len(body)
                }
            time.sleep(0.08)
    return None


def refresh(timeout: int = DEFAULT_TIMEOUT) -> int:
    manifest = load_manifest()
    old = {}
    if STATUS_PATH.exists():
        try:
            old_data = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
            old = {item.get("source_id") + "|" + item.get("kind", "html"): item
                   for item in old_data.get("sources", [])}
        except (ValueError, TypeError):
            old = {}

    new_items = []
    failures = 0
    for item in get_status_sources(manifest):
        try:
            body, headers, status = fetch(item["url"], timeout=timeout)
            is_pdf = item["kind"] == "pdf" or "pdf" in headers.get("Content-Type", "").lower()
            if not is_pdf:
                parser = parse_html(body)
                observed_title = parser.title or next(iter(parser.headings), item["title"])
                normalized = parser.text.encode("utf-8")
                fingerprint = hashlib.sha256(normalized).hexdigest()
            else:
                observed_title = item["title"]
                fingerprint = hashlib.sha256(body).hexdigest()
            status_record = {
                **item,
                "http_status": status,
                "ok": 200 <= status < 300,
                "observed_title": observed_title,
                "content_type": headers.get("Content-Type", ""),
                "content_length": len(body),
                "sha256": fingerprint
            }
            if not status_record["ok"]:
                failures += 1
                status_record["message"] = "Oracle returned a non-success HTTP status."
        except RuntimeError as exc:
            failures += 1
            status_record = {**item, "ok": False, "http_status": None, "message": str(exc)}
        key = status_record["source_id"] + "|" + status_record["kind"]
        previous = old.get(key, {})
        comparison = ("http_status", "observed_title", "sha256", "ok")
        unchanged = all(previous.get(k) == status_record.get(k) for k in comparison)
        status_record["last_changed_at"] = previous.get("last_changed_at", today()) if unchanged else today()
        new_items.append(status_record)
        time.sleep(0.15)

    latest = discover_latest_release(manifest, timeout=min(timeout, 12))
    discovery_patterns = [s for s in manifest["sources"] if s.get("source_type") == "release_discovery_pattern"]
    release_discovery_required = any(s.get("required", True) for s in discovery_patterns)
    previous_latest = None
    if STATUS_PATH.exists():
        try:
            previous_latest = json.loads(STATUS_PATH.read_text(encoding="utf-8")).get("latest_release")
        except (ValueError, OSError):
            pass
    if latest:
        same_latest = previous_latest and previous_latest.get("release") == latest.get("release") and previous_latest.get("sha256") == latest.get("sha256")
        latest["last_changed_at"] = previous_latest.get("last_changed_at", today()) if same_latest else today()
    status_doc = {
        "schema_version": 1,
        "module_code": manifest["module_code"],
        "generated_by": "scripts/oracle_hcm_knowledge.py refresh",
        "latest_release": latest,
        "release_discovery_required": release_discovery_required,
        "sources": new_items,
        "note": "Metadata and fingerprints only. No guide text or PDF contents are stored in this file."
    }
    STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATUS_PATH.write_text(json.dumps(status_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Checked {len(new_items)} source URLs; {failures} request(s) failed or returned non-2xx.")
    if latest:
        print(f"Latest verified Recruiting readiness page: {latest['release']} — {latest['url']}")
    elif release_discovery_required:
        print("WARNING: no release-readiness page passed the configured title/content check.")
        failures += 1
    else:
        print("No module-specific release page discovered; source URLs and the official catalog were still checked.")
    print(f"Metadata snapshot: {STATUS_PATH.relative_to(ROOT)}")
    return 1 if failures else 0


def init_db(db_path: Path = DB_PATH) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("CREATE TABLE IF NOT EXISTS source_meta (source_id TEXT, title TEXT, url TEXT, kind TEXT, release TEXT, sha256 TEXT, retrieved_at TEXT, PRIMARY KEY(source_id,url))")
    conn.execute("CREATE VIRTUAL TABLE IF NOT EXISTS chunks USING fts5(source_id UNINDEXED, title, url UNINDEXED, release UNINDEXED, locator UNINDEXED, content, tokenize='unicode61')")
    return conn


def split_chunks(text: str, size: int = 1300, overlap: int = 180) -> list[str]:
    text = clean_text(text)
    if not text:
        return []
    paragraphs = [clean_text(p) for p in re.split(r"\n{1,}", text) if clean_text(p)]
    chunks: list[str] = []
    current = ""
    for paragraph in paragraphs:
        if len(paragraph) > size:
            if current:
                chunks.append(current)
                current = ""
            start = 0
            while start < len(paragraph):
                part = paragraph[start:start + size]
                if part:
                    chunks.append(part)
                start += max(1, size - overlap)
            continue
        if current and len(current) + len(paragraph) + 1 > size:
            chunks.append(current)
            current = current[-overlap:] + " " + paragraph if overlap else paragraph
        else:
            current = (current + "\n" + paragraph).strip()
    if current:
        chunks.append(current)
    return chunks


def insert_chunks(conn: sqlite3.Connection, source_id: str, title: str, url: str, release: str, locator: str, text_value: str) -> int:
    chunks = split_chunks(text_value)
    conn.executemany(
        "INSERT INTO chunks(source_id,title,url,release,locator,content) VALUES(?,?,?,?,?,?)",
        [(source_id, title, url, release, locator, item) for item in chunks]
    )
    return len(chunks)


def safe_get(url: str, timeout: int = DEFAULT_TIMEOUT) -> tuple[bytes, dict, int]:
    if urlsplit(url).hostname != "docs.oracle.com":
        raise ValueError(f"Refusing to fetch non-Oracle host: {url}")
    return fetch(url, timeout=timeout)


def crawl_html(conn: sqlite3.Connection, source: dict, seed_url: str, prefix: str, max_pages: int) -> tuple[int, int]:
    queue = [canonical_url(seed_url)]
    seen: set[str] = set()
    pages = chunk_count = 0
    prefix = canonical_url(prefix).rstrip("/") + "/"
    while queue and pages < max_pages:
        url = queue.pop(0)
        if url in seen or not url.startswith(prefix) or urlsplit(url).hostname != "docs.oracle.com":
            continue
        seen.add(url)
        try:
            body, headers, status = safe_get(url)
        except (RuntimeError, ValueError) as exc:
            print(f"WARNING: {exc}", file=sys.stderr)
            continue
        if status < 200 or status >= 300:
            continue
        content_type = headers.get("Content-Type", "").lower()
        if "html" not in content_type and not url.endswith(".html") and not url.endswith("/"):
            continue
        parser = parse_html(body)
        page_title = parser.headings[0] if parser.headings else source["title"]
        display_title = f"{source['title']} — {page_title}" if page_title != source["title"] else source["title"]
        release = source.get("release", "rolling")
        chunk_count += insert_chunks(conn, source["source_id"], display_title, url, release, page_title or url, parser.text)
        pages += 1
        if pages % 40 == 0:
            print(f"  {source['source_id']}: crawled {pages} pages")
        for href in parser.links:
            candidate = canonical_url(urljoin(url, href))
            parts = urlsplit(candidate)
            if parts.scheme == "https" and parts.netloc == "docs.oracle.com" and candidate.startswith(prefix) and parts.path.lower().endswith((".html", ".htm")) and candidate not in seen:
                queue.append(candidate)
        time.sleep(0.08)
    return pages, chunk_count


def ingest(max_pages: int | None = None) -> int:
    manifest = load_manifest()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
    conn = init_db()
    conn.execute("DELETE FROM chunks")
    conn.execute("DELETE FROM source_meta")
    total_chunks = 0
    pages_total = 0
    errors = 0

    for source in manifest["sources"]:
        if source.get("source_type") == "release_discovery_pattern":
            continue
        source_id = source["source_id"]
        title = source["title"]
        release = source.get("release", source.get("release_binding", "rolling"))
        html_url = source.get("html_url")
        pdf_url = source.get("pdf_url")
        if pdf_url:
            try:
                body, headers, status = safe_get(pdf_url, timeout=45)
                if not (200 <= status < 300) or not body.startswith(b"%PDF"):
                    raise RuntimeError(f"PDF download did not return a valid PDF (HTTP {status}): {pdf_url}")
                pdf_path = DOCUMENTS_DIR / (source_id.lower() + ".pdf")
                pdf_path.write_bytes(body)
                digest = hashlib.sha256(body).hexdigest()
                conn.execute("INSERT OR REPLACE INTO source_meta VALUES(?,?,?,?,?,?,?)",
                             (source_id, title, pdf_url, "pdf", release, digest, utc_now()))
                try:
                    import fitz  # PyMuPDF
                except ImportError as exc:
                    raise RuntimeError("PyMuPDF is required. Install requirements-knowledge.txt before ingesting PDFs.") from exc
                pdf = fitz.open(pdf_path)
                actual_pages = len(pdf)
                expected_pages = source.get("expected_pdf_pages")
                if expected_pages and actual_pages != expected_pages:
                    print(f"NOTICE: {source_id} PDF has {actual_pages} pages; manifest previously observed {expected_pages}.")
                for page_index, page in enumerate(pdf):
                    page_text = page.get_text("text")
                    total_chunks += insert_chunks(conn, source_id, title, pdf_url, release, f"PDF page {page_index + 1}", page_text)
                pdf.close()
                print(f"Indexed {source_id}: {actual_pages} PDF pages")
            except Exception as exc:
                errors += 1
                print(f"ERROR indexing {source_id} PDF: {exc}", file=sys.stderr)

        if html_url:
            prefix = source.get("crawl_prefix")
            if prefix:
                try:
                    cap = max_pages or manifest["indexing"].get("max_pages_per_source", 1200)
                    pages, count = crawl_html(conn, source, html_url, prefix, cap)
                    pages_total += pages
                    total_chunks += count
                    print(f"Indexed {source_id}: {pages} HTML pages")
                except Exception as exc:
                    errors += 1
                    print(f"ERROR crawling {source_id}: {exc}", file=sys.stderr)
            else:
                try:
                    body, headers, status = safe_get(html_url)
                    if 200 <= status < 300:
                        parser = parse_html(body)
                        digest = hashlib.sha256(parser.text.encode("utf-8")).hexdigest()
                        conn.execute("INSERT OR REPLACE INTO source_meta VALUES(?,?,?,?,?,?,?)",
                                     (source_id, title, html_url, "html", release, digest, utc_now()))
                        total_chunks += insert_chunks(conn, source_id, title, html_url, release, parser.headings[0] if parser.headings else title, parser.text)
                        pages_total += 1
                        print(f"Indexed {source_id}: 1 HTML page")
                    else:
                        raise RuntimeError(f"HTTP {status}")
                except Exception as exc:
                    errors += 1
                    print(f"ERROR indexing {source_id} HTML: {exc}", file=sys.stderr)

    status_doc = {}
    if STATUS_PATH.exists():
        try:
            status_doc = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            status_doc = {}
    latest = status_doc.get("latest_release")
    if latest and latest.get("url"):
        dynamic_source = {"source_id":f"{manifest['module_code']}-RELEASE-LATEST","title":latest.get("title",f"Latest {manifest['module_name']} What's New"),"release":latest.get("release","unknown")}
        # Readiness page links are crawled within their release-specific namespace only.
        try:
            prefix = latest.get("crawl_prefix") or latest["url"].rstrip("/") + "/"
            pages, count = crawl_html(conn, dynamic_source, latest["url"], prefix, max_pages or 1200)
            pages_total += pages
            total_chunks += count
            print(f"Indexed latest release {dynamic_source['release']}: {pages} HTML pages")
        except Exception as exc:
            errors += 1
            print(f"ERROR indexing latest release: {exc}", file=sys.stderr)

    conn.commit()
    counts = conn.execute("SELECT count(*) FROM chunks").fetchone()[0]
    conn.close()
    print(f"Index complete: {counts} searchable chunks, {pages_total} HTML pages, {errors} source errors.")
    print(f"Local index: {DB_PATH.relative_to(ROOT)}")
    return 1 if errors or counts == 0 else 0


def show_status() -> int:
    manifest = load_manifest()
    print(f"{manifest['module_name']} ({manifest['module_code']})")
    print(f"Manifest: {MANIFEST_PATH.relative_to(ROOT)}")
    print(f"Local index exists: {DB_PATH.exists()}")
    if DB_PATH.exists():
        try:
            conn = sqlite3.connect(DB_PATH)
            count = conn.execute("SELECT count(*) FROM chunks").fetchone()[0]
            sources = conn.execute("SELECT count(*) FROM source_meta").fetchone()[0]
            conn.close()
            print(f"Indexed chunks: {count}; source records: {sources}")
        except sqlite3.Error as exc:
            print(f"Index cannot be read: {exc}")
    if STATUS_PATH.exists():
        data = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
        latest = data.get("latest_release")
        if latest:
            print(f"Latest verified release: {latest.get('release')} — {latest.get('url')}")
        for item in data.get("sources", []):
            state = "OK" if item.get("ok") else "CHECK"
            print(f"{state:5} {item.get('source_id')} [{item.get('kind')}] HTTP={item.get('http_status')} {item.get('url')}")
    else:
        print("No source-status snapshot yet. Run refresh.")
    return 0


def search(query: str, limit: int = 8) -> int:
    if not DB_PATH.exists():
        print("Local index not found. Run: python scripts/oracle_hcm_knowledge.py ingest", file=sys.stderr)
        return 2
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            "SELECT source_id,title,url,release,locator,content,bm25(chunks) AS score FROM chunks WHERE chunks MATCH ? ORDER BY score LIMIT ?",
            (query, limit)
        ).fetchall()
    except sqlite3.OperationalError as exc:
        print(f"Search query could not be parsed: {exc}", file=sys.stderr)
        return 2
    if not rows:
        print("No matching passages. Try fewer or different terms.")
        return 0
    for i, row in enumerate(rows, 1):
        print(f"\n[{i}] {row['title']} — {row['source_id']} — release: {row['release']}")
        print(f"Locator: {row['locator']}")
        print(f"Source: {row['url']}")
        snippet = re.sub(r"\s+", " ", row["content"]).strip()
        if len(snippet) > 1000:
            snippet = snippet[:1000].rsplit(" ", 1)[0] + "…"
        print(snippet)
    conn.close()
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Retrieve official Oracle HCM module documentation locally.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    p_status = subparsers.add_parser("status", help="show manifest, local index, and latest URL status")
    p_status.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH, help="path to a module source-manifest.json")
    p_refresh = subparsers.add_parser("refresh", help="check Oracle sources and update the metadata-only status snapshot")
    p_refresh.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    p_refresh.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH, help="path to a module source-manifest.json")
    p_ingest = subparsers.add_parser("ingest", help="download/extract official sources into the local index")
    p_ingest.add_argument("--max-pages", type=int, default=None, help="per-source HTML crawl cap; lower values are useful for a quick first run")
    p_ingest.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH, help="path to a module source-manifest.json")
    p_search = subparsers.add_parser("search", help="search the local full-text index")
    p_search.add_argument("query", help="SQLite FTS5 query")
    p_search.add_argument("--limit", type=int, default=8)
    p_search.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH, help="path to a module source-manifest.json")
    args = parser.parse_args()
    try:
        configure_paths(args.manifest)
        if args.command == "status":
            return show_status()
        if args.command == "refresh":
            return refresh(timeout=args.timeout)
        if args.command == "ingest":
            return ingest(max_pages=args.max_pages)
        if args.command == "search":
            return search(args.query, limit=args.limit)
    except (ValueError, OSError, sqlite3.Error, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
