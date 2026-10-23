"""Offline tests for separate multi-source Oracle corpus search."""
from __future__ import annotations
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "oracle_docs" / "search_corpus.py"
SPEC = importlib.util.spec_from_file_location("search_corpus", TARGET)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load search tool: {TARGET}")
SEARCH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SEARCH)


class ExternalCorpusSearchTests(unittest.TestCase):
    def test_build_indexes_both_pdf_and_html_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "corpus"
            pdf = root / "DOC-001" / "retrieval-chunks.jsonl"
            html = root / "DOC-002-html" / "retrieval-chunks.jsonl"
            pdf.parent.mkdir(parents=True)
            html.parent.mkdir(parents=True)
            pdf.write_text(json.dumps({
                "chunk_id":"pdf-1","doc_id":"DOC-001","title":"Implementing Recruiting",
                "edition":"G34431-12","source_kind":"pdf","source_pdf_page_start":31,
                "source_pdf_page_end":31,"canonical_url":"https://docs.oracle.com/pdf",
                "text":"candidate search and attachment index"
            })+"\n",encoding="utf-8")
            html.write_text(json.dumps({
                "chunk_id":"html-1","doc_id":"DOC-002","title":"Using Recruiting",
                "edition":"G34440-08","source_kind":"oracle-help-center-html",
                "source_html_sequence_start":3,"source_html_sequence_end":4,
                "source_url_start":"https://docs.oracle.com/guide/requisitions.html",
                "canonical_url":"https://docs.oracle.com/guide/index.html",
                "text":"candidate interview calendar availability"
            })+"\n",encoding="utf-8")
            inputs, rows = SEARCH.collect_rows(root)
            self.assertEqual(len(inputs),2)
            self.assertEqual(len(rows),2)
            db=Path(tmp)/"index.sqlite"
            SEARCH.build(root,db)
            stdout=io.StringIO()
            with contextlib.redirect_stdout(stdout):
                SEARCH.search(db,"candidate interview",8,False)
            rendered=stdout.getvalue()
            self.assertIn("Oracle HTML sequence 3–4",rendered)
            self.assertIn("requisitions.html",rendered)

    def test_empty_corpus_fails_loudly(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(SystemExit):
                SEARCH.build(Path(tmp),Path(tmp)/"index.sqlite")


if __name__ == "__main__":
    unittest.main(verbosity=2)
