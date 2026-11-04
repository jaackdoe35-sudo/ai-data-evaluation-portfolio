import unittest
from validator import validate_catalogue

VALID_CASE = {
    "id": "SEC-T01", "category": "direct_prompt_injection", "risk": "medium",
    "scenario": "A controlled scenario.", "test_input": "A harmless test input.",
    "expected_behavior": "Maintain the instruction boundary.",
    "failure_indicators": ["Follows the injected instruction."],
    "safe_success_indicators": ["Does not follow the injected instruction."],
}


class CatalogueValidatorTests(unittest.TestCase):
    def test_valid_catalogue_passes(self):
        self.assertEqual(validate_catalogue({
            "status": "test_specifications_only", "cases": [VALID_CASE]
        }), [])

    def test_wrong_status_is_rejected(self):
        errors = validate_catalogue({"status": "executed", "cases": [VALID_CASE]})
        self.assertTrue(any("test_specifications_only" in error for error in errors))

    def test_duplicate_ids_are_rejected(self):
        errors = validate_catalogue({
            "status": "test_specifications_only", "cases": [VALID_CASE, VALID_CASE]
        })
        self.assertTrue(any("duplicate id" in error for error in errors))

    def test_missing_expected_behavior_is_rejected(self):
        case = dict(VALID_CASE)
        del case["expected_behavior"]
        errors = validate_catalogue({
            "status": "test_specifications_only", "cases": [case]
        })
        self.assertTrue(any("expected_behavior" in error for error in errors))

    def test_invalid_risk_is_rejected(self):
        case = dict(VALID_CASE, risk="critical")
        errors = validate_catalogue({
            "status": "test_specifications_only", "cases": [case]
        })
        self.assertTrue(any("risk must be" in error for error in errors))

    def test_empty_catalogue_is_rejected(self):
        errors = validate_catalogue({"status": "test_specifications_only", "cases": []})
        self.assertTrue(any("non-empty list" in error for error in errors))

    def test_empty_failure_indicators_are_rejected(self):
        case = dict(VALID_CASE, failure_indicators=[])
        errors = validate_catalogue({
            "status": "test_specifications_only", "cases": [case]
        })
        self.assertTrue(any("failure_indicators" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
