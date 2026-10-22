"""Offline tests for the Oracle HCM knowledge ingestion pipeline."""
import importlib.util
import sqlite3
import tempfile
import unittest
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "oracle_hcm_knowledge.py"
SPEC = importlib.util.spec_from_file_location("oracle_hcm_knowledge", SCRIPT)
KNOWLEDGE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(KNOWLEDGE)


class ManifestTests(unittest.TestCase):
    def test_real_recruiting_sources_are_registered(self):
        manifest = KNOWLEDGE.load_manifest(ROOT / ".project/docs/oracle/ORC/source-manifest.json")
        self.assertEqual(manifest["module_code"], "ORC")
        ids = [item["source_id"] for item in manifest["sources"]]
        self.assertEqual(len(ids), len(set(ids)))
        by_id = {item["source_id"]: item for item in manifest["sources"]}
        self.assertEqual(by_id["ORC-IMPL"]["document_id"], "G34431-12")
        self.assertEqual(by_id["ORC-IMPL"]["expected_pdf_pages"], 448)
        self.assertEqual(by_id["ORC-USER"]["document_id"], "G34440-08")
        self.assertEqual(by_id["ORC-USER"]["expected_pdf_pages"], 220)
        self.assertEqual(by_id["ORC-BOOSTER"]["document_id"], "G34425-04")
        self.assertEqual(by_id["ORC-BOOSTER"]["expected_pdf_pages"], 70)
        self.assertEqual(by_id["ORC-26D-WN"]["release"], "26D")

    def test_registered_sources_use_the_allowlisted_oracle_host(self):
        manifest = KNOWLEDGE.load_manifest(ROOT / ".project/docs/oracle/ORC/source-manifest.json")
        for source in manifest["sources"]:
            for key in ("html_url", "pdf_url"):
                if source.get(key):
                    self.assertEqual(urlsplit(source[key]).hostname, "docs.oracle.com")

    def test_official_release_discovery_includes_verified_26d(self):
        manifest = KNOWLEDGE.load_manifest(ROOT / ".project/docs/oracle/ORC/source-manifest.json")
        candidates = KNOWLEDGE.release_candidates(manifest)
        self.assertTrue(any(release == "26D" and url == "https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/recr-26d/" for release, url in candidates))


class IndexPrimitiveTests(unittest.TestCase):
    def test_html_parser_extracts_heading_text_and_links(self):
        parser = KNOWLEDGE.parse_html(b'<html><head><title>Oracle guide</title></head><body><h1>Career Sites</h1><p>Configure a career site.</p><a href="setup.html">Setup</a></body></html>')
        self.assertEqual(parser.title, "Oracle guide")
        self.assertIn("Career Sites", parser.text)
        self.assertIn("Configure a career site.", parser.text)
        self.assertIn("setup.html", parser.links)

    def test_chunks_preserve_searchable_terms_and_bound_size(self):
        original = "Candidate selection process. " * 200
        chunks = KNOWLEDGE.split_chunks(original, size=400, overlap=40)
        self.assertGreater(len(chunks), 1)
        self.assertTrue(all(len(chunk) <= 401 for chunk in chunks))
        self.assertTrue(all("Candidate" in chunk for chunk in chunks))

    def test_local_fts_index_accepts_and_returns_retrievable_chunks(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "index.sqlite3"
            conn = KNOWLEDGE.init_db(path)
            count = KNOWLEDGE.insert_chunks(
                conn,
                "TEST-SOURCE",
                "Local indexing test",
                "https://docs.oracle.com/en/cloud/saas/talent-management/faimh/index.html",
                "rolling",
                "test locator",
                "Career site candidate selection application flow."
            )
            conn.commit()
            rows = conn.execute("SELECT source_id,title,locator,content FROM chunks WHERE chunks MATCH ?", ("candidate",)).fetchall()
            conn.close()
            self.assertGreater(count, 0)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0][0], "TEST-SOURCE")

    def test_fetch_refuses_non_oracle_domains_before_network_access(self):
        with self.assertRaises(ValueError):
            KNOWLEDGE.safe_get("https://example.org/not-an-oracle-document")


if __name__ == "__main__":
    unittest.main()
