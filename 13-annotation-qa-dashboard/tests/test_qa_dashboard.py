import unittest
from qa_dashboard import REQUIRED, inspect, render_dashboard

def row(**overrides):
    data = {"record_id":"A1","message_text":"A support request","primary_intent":"transfer_status",
            "sentiment":"neutral","urgency":"standard","pii_types":"none",
            "pii_span_to_redact":"","clarification_flag":"no",
            "annotation_rationale":"Direct status question."}
    data.update(overrides)
    return data

class DashboardTests(unittest.TestCase):
    def test_valid_record_has_no_flags(self):
        self.assertEqual(inspect(REQUIRED, [row()])["issues"], [])

    def test_duplicate_ids_flagged(self):
        result = inspect(REQUIRED, [row(), row()])
        self.assertTrue(any(issue[1] == "Duplicate record ID" for issue in result["issues"]))

    def test_pii_mismatch_flagged(self):
        result = inspect(REQUIRED, [row(pii_types="email", pii_span_to_redact="[PHONE]")])
        self.assertTrue(any(issue[1] == "PII token mismatch" for issue in result["issues"]))

    def test_invalid_urgency_flagged(self):
        result = inspect(REQUIRED, [row(urgency="immediate")])
        self.assertTrue(any(issue[1] == "Invalid urgency" for issue in result["issues"]))

    def test_dashboard_contains_summary_and_disclaimer(self):
        page = render_dashboard(inspect(REQUIRED, [row()]), "sample.csv")
        self.assertIn("Annotation QA Dashboard", page)
        self.assertIn("does not assess semantic correctness", page)

if __name__ == "__main__":
    unittest.main()
