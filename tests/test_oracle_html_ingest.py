"""Offline tests for the public Oracle HTML ingestion tool."""
from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "oracle_docs" / "ingest_oracle_html.py"
SPEC = importlib.util.spec_from_file_location("ingest_oracle_html", TARGET)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load HTML ingestor: {TARGET}")
INGEST = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INGEST)


class OracleHTMLIngestTests(unittest.TestCase):
    def test_scope_restricted_to_https_and_same_guide_directory(self):
        index = "https://docs.oracle.com/en/cloud/saas/talent-management/faush/index.html"
        self.assertTrue(INGEST.guide_scope(index, index))
        self.assertTrue(INGEST.guide_scope("https://docs.oracle.com/en/cloud/saas/talent-management/faush/job-requisitions.html", index))
        self.assertFalse(INGEST.guide_scope("https://evil.example/faush/other.html", index))
        self.assertFalse(INGEST.guide_scope("http://docs.oracle.com/en/cloud/saas/talent-management/faush/index.html", index))
        self.assertFalse(INGEST.guide_scope("https://docs.oracle.com/en/cloud/saas/talent-management/faarb/index.html", index))
        self.assertFalse(INGEST.guide_scope("https://docs.oracle.com/en/cloud/saas/talent-management/faush/using-recruiting.pdf", index))

    def test_next_page_only_follows_explicit_next_navigation(self):
        index = "https://docs.oracle.com/en/cloud/saas/talent-management/faush/index.html"
        html = '<a href="job-requisitions.html" rel="next">Next</a><a href="security.html">Security</a>'
        self.assertEqual(
            INGEST.next_page_url(html, index, index),
            "https://docs.oracle.com/en/cloud/saas/talent-management/faush/job-requisitions.html",
        )
        self.assertIsNone(INGEST.next_page_url('<a href="security.html">Security</a>', index, index))

    def test_next_link_outside_scope_is_rejected(self):
        index = "https://docs.oracle.com/en/cloud/saas/talent-management/faush/index.html"
        html = '<a href="../faarb/index.html" rel="next">Next</a>'
        self.assertIsNone(INGEST.next_page_url(html, index, index))

    def test_html_to_markdown_keeps_headings_lists_links_and_tables(self):
        html = """
        <html><body><nav><a>Navigation noise</a></nav><main>
        <h1>Job Requisitions</h1><p>Configure the requisition.</p>
        <ul><li>One item</li><li>Two item</li></ul>
        <p><a href="details.html">Detailed setup</a></p>
        <table><tr><th>Setting</th><th>Value</th></tr><tr><td>Enabled</td><td>Yes</td></tr></table>
        </main></body></html>
        """
        parser = INGEST.MarkdownParser()
        parser.feed(html)
        result = parser.markdown()
        self.assertIn("# Job Requisitions", result)
        self.assertIn("- One item", result)
        self.assertIn("[Detailed setup](details.html)", result)
        self.assertIn("| Setting | Value |", result)
        self.assertNotIn("Navigation noise", result)

    def test_manifest_distinguishes_html_sequence_from_pdf_pages(self):
        row = next(INGEST.chunks(
            "# Example\n\n<!-- source-html-page: 1 | url: https://docs.oracle.com/a/index.html -->\n\nBody text",
            "DOC-TEST", "Example", "TEST", "https://docs.oracle.com/a/index.html", [], 50, 5
        ))
        self.assertEqual(row["source_kind"], "oracle-help-center-html")
        self.assertEqual(row["source_html_sequence_start"], 1)
        self.assertIn("source_url_start", row)
        self.assertNotIn("source_pdf_page_start", row)


if __name__ == "__main__":
    unittest.main(verbosity=2)
