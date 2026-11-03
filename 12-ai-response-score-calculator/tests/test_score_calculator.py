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

    def test_empty_dataset_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "No valid evaluation records"):
            analyze_rows(HEADERS, [])

    def test_all_na_dimensions_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "at least one dimension"):
            analyze_rows(HEADERS, [record(**{d: "N/A" for d in DIMENSIONS})])

    def test_fractional_score_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "integer from 1 to 5"):
            analyze_rows(HEADERS, [record(factuality="4.5")])

    def test_non_finite_score_is_rejected(self):
        with self.assertRaises(ValueError):
            analyze_rows(HEADERS, [record(factuality="NaN")])

    def test_invalid_severity_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "invalid issue_severity"):
            analyze_rows(HEADERS, [record(issue_severity="Unknown")])

    def test_missing_header_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "no header row"):
            analyze_rows(None, [])

if __name__ == "__main__":
    unittest.main()
