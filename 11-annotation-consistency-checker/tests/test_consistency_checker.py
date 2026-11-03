import unittest
from consistency_checker import check_rows


class ConsistencyCheckerTests(unittest.TestCase):
    def test_conflicting_duplicate_text_is_flagged(self):
        rows = [
            {"message_text": "Same message", "primary_intent": "transfer_status",
             "clarification_flag": "no", "pii_types": "none", "pii_span_to_redact": ""},
            {"message_text": " same   message ", "primary_intent": "refund_status",
             "clarification_flag": "no", "pii_types": "none", "pii_span_to_redact": ""},
        ]
        flags = check_rows(rows)
        self.assertTrue(any("conflicting primary-intent" in f for f in flags))

    def test_unclear_without_clarification_is_flagged(self):
        rows = [
            {"message_text": "Unclear", "primary_intent": "intent_unclear",
             "clarification_flag": "no", "pii_types": "none", "pii_span_to_redact": ""},
        ]
        flags = check_rows(rows)
        self.assertTrue(any("clarification_flag" in f for f in flags))

    def test_valid_record_is_not_flagged(self):
        rows = [
            {"message_text": "Clear request", "primary_intent": "transfer_status",
             "clarification_flag": "no", "pii_types": "none", "pii_span_to_redact": ""},
        ]
        self.assertEqual(check_rows(rows), [])


if __name__ == "__main__":
    unittest.main()
