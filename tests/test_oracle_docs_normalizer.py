"""Regression tests for the Oracle PDF Markdown normalizer."""
from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "oracle_docs" / "normalize_markdown.py"
SPEC = importlib.util.spec_from_file_location("normalize_markdown", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load normalizer: {MODULE_PATH}")
NORMALIZER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(NORMALIZER)


class NormalizeMarkdownTests(unittest.TestCase):
    def test_bold_numeric_markers_become_ordered_list_steps(self):
        source = "## Example\n\n**1.** Set the site profile option.\n\n**2.** Save and close.\n"
        result, _ = NORMALIZER.normalize(source)
        self.assertIn("1. Set the site profile option.", result)
        self.assertIn("2. Save and close.", result)
        self.assertNotRegex(result, r"\*\*\d+\.\*\*")

    def test_setup_navigation_becomes_nested_bullets(self):
        source = (
            "1. In the Setup and Maintenance work area, go to\n\n-\n\n"
            "Offering: Recruiting and Candidate Experience -\n\n"
            "Functional Area: Workforce Information -\n\n"
            "Task: Manage Person Extensible Flexfield\n"
        )
        result, counts = NORMALIZER.normalize(source)
        self.assertIn("    - Offering: Recruiting and Candidate Experience", result)
        self.assertIn("    - Functional Area: Workforce Information", result)
        self.assertIn("    - Task: Manage Person Extensible Flexfield", result)
        self.assertEqual(counts["setup_navigation_blocks"], 1)

    def test_scheduled_process_sequence_is_a_real_nested_list(self):
        source = (
            "### New Provisioning\n\n"
            "2. Run these scheduled processes one time sequentially: -\n\n"
            "**Load and Index Master Geography Hierarchy** without parameters. -\n\n"
            "**Load and Index Job Requisitions** with Drop and Recreate. -\n"
            "3. Schedule the following processes to run every 15 minutes: -\n\n"
            "**Maintain Candidates and Job Requisitions for Search**-\n\n"
            "**Index Candidate Attachments**-\n\n4. Validate search.\n"
        )
        result, counts = NORMALIZER.normalize(source)
        self.assertIn("    - **Load and Index Master Geography Hierarchy** without parameters.", result)
        self.assertIn("    - **Load and Index Job Requisitions** with Drop and Recreate.", result)
        self.assertIn("    - **Maintain Candidates and Job Requisitions for Search**", result)
        self.assertIn("    - **Index Candidate Attachments**", result)
        self.assertNotRegex(result, r"(?m)^    - \*\*[^\n]+\*\*-$")
        self.assertEqual(counts["scheduled_process_lists"], 2)
        self.assertEqual(counts["scheduled_process_bullets"], 4)

    def test_alphabetic_substeps_do_not_leave_empty_bullets(self):
        source = "Intro text.\n\n-\n\n**a.** In Setup and Maintenance.\n\n-\n\n**b.** Click Save.\n"
        result, _ = NORMALIZER.normalize(source)
        self.assertIn("- a. In Setup and Maintenance.", result)
        self.assertIn("- b. Click Save.", result)
        self.assertNotRegex(result, r"(?m)^-\s*$\n(?:\s*\n)*- [a-z]\. ")

    def test_bold_spans_get_word_boundaries(self):
        source = "A**Important**word and **Go**Now.\n"
        result, _ = NORMALIZER.normalize(source)
        self.assertIn("A **Important** word", result)
        self.assertIn("**Go** Now", result)

    def test_transform_is_idempotent(self):
        source = (
            "1. In Setup and Maintenance, go to\n\n-\n\n"
            "Offering: Recruiting -\n\nFunctional Area: Workforce Information -\n\n"
            "Task: Manage Administrator Profile Values\n\n"
            "2. Run these scheduled processes one time sequentially: -\n\n"
            "**Load and Index Candidates** with Drop and Recreate. -\n"
        )
        once, _ = NORMALIZER.normalize(source)
        twice, _ = NORMALIZER.normalize(once)
        self.assertEqual(once, twice)


if __name__ == "__main__":
    unittest.main(verbosity=2)
