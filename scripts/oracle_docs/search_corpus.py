#!/usr/bin/env python3
"""Build/search a local SQLite FTS5 index across .local/oracle-docs corpora."""
from __future__ import annotations
import argparse
import json
import sqlite3
from pathlib import Path


def default_root():
    return Path.cwd() / ".local" / "oracle-docs"


def build(root: Path, db_path: Path):
    inputs = sorted(root.rglob("retrieval-chunks.jsonl"))
    if not inputs:
        raise SystemExit(f"No retrieval-chunks.jsonl files under {root}. Run ingest_pdf.py first.")
    rows = []
    for path in inputs:
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            try:
                row = json.loads(line)
            except Exception as exc:
                raise SystemExit(f"Invalid JSON in {path}:{number}: {exc}")
            rows.append((
                row.get("chunk_id"), row.get("doc_id"), row.get("title"), row.get("edition"),
                row.get("source_pdf_page_start"), row.get("source_pdf_page_end"),
                row.get("canonical_url"), str(path), row.get("text", "")
            ))
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    con = sqlite3.connect(db_path)
    con.execute("CREATE VIRTUAL TABLE chunks USING fts5(chunk_id UNINDEXED, doc_id UNINDEXED, title, edition UNINDEXED, page_start UNINDEXED, page_end UNINDEXED, canonical_url UNINDEXED, local_chunk_file UNINDEXED, body, tokenize='unicode61 remove_diacritics 2')")
    con.executemany("INSERT INTO chunks VALUES(?,?,?,?,?,?,?,?,?)", rows)
    con.commit()
    integrity = con.execute("PRAGMA integrity_check").fetchone()[0]
    con.close()
    print(json.dumps({"database": str(db_path), "documents": len(inputs), "chunks": len(rows), "integrity": integrity}, indent=2))


def search(db_path: Path, query: str, limit: int, as_json: bool):
    if not db_path.exists():
        raise SystemExit(f"Index not found: {db_path}. Run the build command first.")
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    try:
        sql = "SELECT chunk_id, doc_id, title, edition, page_start, page_end, canonical_url, snippet(chunks,8,'[',']',' … ',25) AS excerpt, bm25(chunks) AS score FROM chunks WHERE chunks MATCH ? ORDER BY score LIMIT ?"
        try:
            found = con.execute(sql, (query, limit)).fetchall()
        except sqlite3.OperationalError:
            terms = [w.strip('"') for w in query.split() if w.strip('"')]
            fallback = " OR ".join('"' + term.replace('"', '') + '"' for term in terms)
            found = con.execute(sql, (fallback, limit)).fetchall()
        results = [dict(row) for row in found]
    finally:
        con.close()
    if as_json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return
    if not results:
        print("No results. Try fewer or different keywords.")
        return
    for i, row in enumerate(results, 1):
        pages = f"PDF pp. {row['page_start'] or '?'}–{row['page_end'] or '?'}"
        print(f"{i}. {row['title']} ({row['doc_id']}, {row['edition'] or 'edition unknown'}) — {pages}")
        if row["canonical_url"]:
            print(f"   Source: {row['canonical_url']}")
        print(f"   Chunk: {row['chunk_id']} · {row['excerpt']}\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["build", "search"])
    parser.add_argument("query", nargs="?", default="")
    parser.add_argument("--root", type=Path, default=default_root(), help="Local corpus root")
    parser.add_argument("--database", type=Path, default=Path.cwd()/".local"/"oracle-search"/"index.sqlite")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.command == "build":
        build(args.root.resolve(), args.database.resolve())
    else:
        if not args.query.strip():
            parser.error("search requires a query")
        search(args.database.resolve(), args.query, args.limit, args.json)


if __name__ == "__main__":
    main()
