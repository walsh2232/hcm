# Local Oracle PDF intake tooling

These scripts create searchable local research corpora from official Oracle PDFs without committing the source PDF or full extracted text into git.

## Requirements

Python 3.10+ and PyMuPDF:

    python -m pip install pymupdf

## Ingest a PDF

Run from the repository root after downloading the official guide locally:

    python scripts/oracle_docs/ingest_pdf.py --input ./using-recruiting.pdf --doc-id DOC-002 --title "Using Recruiting" --edition G34440-08 --canonical-url https://docs.oracle.com/en/cloud/saas/talent-management/faush/using-recruiting.pdf

By default output goes to .local/oracle-docs/DOC-002/ (git-ignored). Outputs include manifest.json, full-text.md, one Markdown file per physical PDF page, and overlapping retrieval-chunks.jsonl.

## Build and query a local lexical index

The companion search_corpus.py script aggregates all local retrieval-chunks.jsonl files into a SQLite FTS5 database outside the tracked repository:

    python scripts/oracle_docs/search_corpus.py build
    python scripts/oracle_docs/search_corpus.py search "candidate duplicate check"
    python scripts/oracle_docs/search_corpus.py search "IRC_MANAGE_RECRUITING_ADMINISTRATION" --limit 10

## Important limits

- The extractor reads the PDF text layer; it does not run OCR.
- Physical PDF page numbers are explicit; Oracle printed pagination is not guessed.
- Complex tables, diagrams, screenshots, and side-by-side columns require visual review against the original PDF.
- The local corpus may contain substantial copyrighted text; keep it local/private unless the rights holder's terms explicitly permit republication.
- Do not place production HCM data or candidate/employee PII in this pipeline.

## Normalize PDF-derived Markdown

After extraction, if a private corpus uses per-chapter Markdown files beneath a local wiki root, run the repeatable procedure normalizer before rebuilding the master text and search index:

    python scripts/oracle_docs/normalize_markdown.py --root .local/oracle-wiki --check
    python scripts/oracle_docs/normalize_markdown.py --root .local/oracle-wiki --apply

Run the `--check` command again; it should report zero changed files. The normalizer repairs repeated bold/number formatting, Setup and Maintenance navigation triplets, and known Oracle Search scheduled-process lists. It does not validate configuration or fix product behavior. Log source inconsistencies separately rather than normalizing identifier strings.
