import csv
import unittest
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "search_relevance_dataset.csv"
INTENTS = {"informational", "navigational", "transactional", "local"}

class SearchRelevanceDatasetTests(unittest.TestCase):
    def setUp(self):
        with DATA.open(encoding="utf-8", newline="") as f:
            self.rows = list(csv.DictReader(f))

    def test_expected_case_count(self):
        self.assertEqual(len(self.rows), 20)

    def test_ids_are_unique_and_present(self):
        ids = [r["case_id"].strip() for r in self.rows]
        self.assertTrue(all(ids))
        self.assertEqual(len(ids), len(set(ids)))

    def test_grades_and_intents_are_valid(self):
        self.assertTrue(all(r["relevance_grade"] in {"0", "1", "2", "3"} for r in self.rows))
        self.assertTrue(all(r["intent_type"] in INTENTS for r in self.rows))

    def test_required_text_is_present(self):
        fields = ("query", "result_title", "result_snippet", "rationale")
        self.assertTrue(all(all(r[f].strip() for f in fields) for r in self.rows))

    def test_review_flags_are_valid(self):
        self.assertTrue(all(r["review_flag"] in {"yes", "no"} for r in self.rows))

if __name__ == "__main__":
    unittest.main()
