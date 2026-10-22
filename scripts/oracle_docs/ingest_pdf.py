#!/usr/bin/env python3
"""Extract a searchable, source-page-traceable local corpus from an Oracle PDF.

Outputs are local/private by default: .local/oracle-docs/<doc-id>/
Requires PyMuPDF: python -m pip install pymupdf
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PAGE_RE = re.compile(r"<!-- source-pdf-page: (\d+) -->")


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "source"


def make_chunks(text: str, max_words: int, overlap: int):
    words = list(re.finditer(r"\S+", text))
    markers = [(m.start(), int(m.group(1))) for m in PAGE_RE.finditer(text)]
    start = 0
    while start < len(words):
        end = min(len(words), start + max_words)
        if end < len(words):
            cutoff = max(start + 1, start + int(max_words * 0.82))
            for i in range(end - 1, cutoff - 1, -1):
                if "\n\n" in text[words[i].end():words[i + 1].start()]:
                    end = i + 1
                    break
        first, last = words[start].start(), words[end - 1].end()
        page_start = page_end = None
        for offset, page_number in markers:
            if offset <= first:
                page_start = page_number
            if offset <= last:
                page_end = page_number
            else:
                break
        yield text[first:last], start, end, page_start, page_end
        if end >= len(words):
            break
        start = max(start + 1, end - overlap)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Local searchable PDF")
    parser.add_argument("--doc-id", required=True, help="Registered source ID, e.g. DOC-001")
    parser.add_argument("--title", required=True, help="Oracle guide title")
    parser.add_argument("--edition", default="", help="Oracle guide identifier, not tenant release")
    parser.add_argument("--canonical-url", default="", help="Canonical Oracle source URL")
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--max-words", type=int, default=520)
    parser.add_argument("--overlap", type=int, default=70)
    parser.add_argument("--low-text-threshold", type=int, default=100)
    args = parser.parse_args()
    if args.max_words < 50:
        parser.error("--max-words must be at least 50")
    if not 0 <= args.overlap < args.max_words:
        parser.error("--overlap must be between zero and max-words minus one")
    source = args.input.expanduser().resolve()
    if not source.is_file():
        parser.error(f"PDF not found: {source}")
    try:
        import fitz
    except ImportError:
        print("PyMuPDF is required: python -m pip install pymupdf", file=sys.stderr)
        return 2

    output = args.output_dir.expanduser().resolve() if args.output_dir else (
        Path.cwd() / ".local" / "oracle-docs" / slug(args.doc_id)
    ).resolve()
    output.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    doc = fitz.open(source)
    page_parts, low_pages, empty_pages, replacement_pages = [], [], [], []
    total_chars = 0
    pages_dir = output / "pages"
    pages_dir.mkdir(exist_ok=True)

    for number, page in enumerate(doc, 1):
        body = page.get_text("text", sort=True).replace("\x00", "").strip()
        total_chars += len(body)
        if len(body) < args.low_text_threshold:
            low_pages.append({"physical_page": number, "characters": len(body), "preview": body[:100].replace("\n", " ")})
        if not body:
            empty_pages.append(number)
        if "\ufffd" in body:
            replacement_pages.append(number)
        page_parts.append(f"<!-- source-pdf-page: {number} -->\n\n{body}\n")
        (pages_dir / f"page-{number:04d}.md").write_text(
            f"# Physical PDF page {number}\n\n<!-- source-pdf-page: {number} -->\n\n{body}\n",
            encoding="utf-8",
        )

    full_text = (
        f"# {args.title}\n\n> Extracted from {source.name}; SHA-256: {digest}.\n"
        "> Physical page markers are PDF page numbers, not Oracle printed pages.\n"
        "> OCR was not performed; complex table/layout reconstruction is not guaranteed.\n\n"
        + "\n\n---\n\n".join(page_parts)
    )
    (output / "full-text.md").write_text(full_text + "\n", encoding="utf-8")
    chunks_path = output / "retrieval-chunks.jsonl"
    chunk_count = 0
    with chunks_path.open("w", encoding="utf-8") as handle:
        for number, (body, start, end, page_start, page_end) in enumerate(
            make_chunks(full_text, args.max_words, args.overlap), 1
        ):
            row = {
                "chunk_id": f"{slug(args.doc_id)}-{number:05d}",
                "doc_id": args.doc_id,
                "title": args.title,
                "edition": args.edition or None,
                "canonical_url": args.canonical_url or None,
                "source_sha256": digest,
                "source_pdf_page_start": page_start,
                "source_pdf_page_end": page_end,
                "word_start": start,
                "word_end_exclusive": end,
                "text": body,
            }
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            chunk_count += 1

    manifest = {
        "doc_id": args.doc_id,
        "title": args.title,
        "edition": args.edition or None,
        "canonical_url": args.canonical_url or None,
        "source_filename": source.name,
        "local_source_path": str(source),
        "source_sha256": digest,
        "physical_page_count": len(doc),
        "page_text_characters": total_chars,
        "empty_text_pages": empty_pages,
        "low_text_pages": low_pages,
        "pages_with_replacement_character": replacement_pages,
        "processed_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "extractor": "PyMuPDF get_text('text', sort=True)",
        "ocr_performed": False,
        "layout_limit": "Complex tables, columns, diagrams and visual-only details require source-PDF review.",
        "chunking": {"max_words": args.max_words, "overlap_words": args.overlap, "chunks": chunk_count},
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    doc.close()
    print(json.dumps({
        "output_dir": str(output), "doc_id": args.doc_id, "edition": args.edition or None,
        "pages": manifest["physical_page_count"], "characters": total_chars,
        "chunks": chunk_count, "low_text_pages": len(low_pages), "empty_text_pages": len(empty_pages),
        "sha256": digest,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
