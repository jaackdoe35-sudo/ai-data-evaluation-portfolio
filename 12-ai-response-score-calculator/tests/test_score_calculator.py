import unittest
from score_calculator import analyze_rows, DIMENSIONS, render_report

HEADERS = ["id", *DIMENSIONS, "issue_severity"]

def record(rid="R1", **values):
    row = {"id": rid, **{d: "4" for d in DIMENSIONS}, "issue_severity": "None"}
    row.update(values)
    return row

class ScoreCalculatorTests(unittest.TestCase):
    def test_mean_is_recalculated(self):
        result = analyze_rows(HEADERS, [record(factuality="1", instruction_following="3")])
        self.assertEqual(result["R1"]["mean"], 3.2)

    def test_na_is_excluded_from_mean(self):
        result = analyze_rows(HEADERS, [record(factuality="N/A")])
        self.assertEqual(result["R1"]["mean"], 4.0)

    def test_invalid_score_is_rejected(self):
        with self.assertRaises(ValueError):
            analyze_rows(HEADERS, [record(factuality="6")])

    def test_duplicate_ids_are_rejected(self):
        with self.assertRaises(ValueError):
            analyze_rows(HEADERS, [record(), record()])

    def test_report_includes_dimension_summary(self):
        result = analyze_rows(HEADERS, [record()])
        self.assertIn("Mean score by dimension", render_report(result))

if __name__ == "__main__":
    unittest.main()
