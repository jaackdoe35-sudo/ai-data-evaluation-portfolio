import unittest
from run_assurance_simulation import run


class AssuranceSimulationTests(unittest.TestCase):
    def test_seeded_results_match_expected(self):
        result = run()
        self.assertTrue(result["all_fixture_expectations_match"])

    def test_expected_finding_distribution(self):
        result = run()
        self.assertEqual(result["counts"], {
            "pass": 2, "partial": 4, "fail": 4, "not_tested": 0
        })

    def test_all_ten_controls_are_assessed(self):
        result = run()
        self.assertEqual(len(result["controls"]), 10)

    def test_fixture_is_explicitly_synthetic(self):
        result = run()
        self.assertIn("synthetic", result["notice"].lower())
        self.assertIn("not a real", result["notice"].lower())


if __name__ == "__main__":
    unittest.main()
