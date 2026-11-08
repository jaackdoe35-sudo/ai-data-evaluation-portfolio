import unittest
from validator import validate


class GovernanceStructureTests(unittest.TestCase):
    def test_current_artifacts_are_structurally_valid(self):
        self.assertEqual(validate(), [])

    def test_control_test_plan_covers_all_controls(self):
        import csv
        from pathlib import Path
        root = Path(__file__).resolve().parents[1]
        with (root / "control-matrix.csv").open(encoding="utf-8", newline="") as f:
            controls = {row["control_id"] for row in csv.DictReader(f)}
        with (root / "control-test-plan.csv").open(encoding="utf-8", newline="") as f:
            tested = {row["control_id"] for row in csv.DictReader(f)}
        self.assertEqual(controls, tested)

    def test_risk_ratings_are_not_fabricated(self):
        import csv
        from pathlib import Path
        root = Path(__file__).resolve().parents[1]
        with (root / "risk-register.csv").open(encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))
        self.assertTrue(rows)
        for row in rows:
            self.assertEqual(row["initial_likelihood"], "Not assessed")
            self.assertEqual(row["residual_rating"], "Not assessed")

    def test_controls_are_not_claimed_as_implemented(self):
        import csv
        from pathlib import Path
        root = Path(__file__).resolve().parents[1]
        with (root / "control-matrix.csv").open(encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))
        self.assertTrue(rows)
        self.assertTrue(all(row["implementation_status"] == "Proposed" for row in rows))


if __name__ == "__main__":
    unittest.main()
