import unittest
from validator import REQUIRED_COLUMNS, validate_rows


def row(**overrides):
    data = {
        "record_id": "T001", "message_text": "I need help with my card.",
        "primary_intent": "intent_unclear", "secondary_intent": "",
        "sentiment": "neutral", "urgency": "routine", "pii_types": "none",
        "pii_span_to_redact": "", "clarification_flag": "yes",
        "annotation_rationale": "Insufficient detail for a narrow label.",
    }
    data.update(overrides)
    return data


class ValidatorTests(unittest.TestCase):
    def test_valid_row_passes(self):
        self.assertEqual(validate_rows(REQUIRED_COLUMNS, [row()]), [])

    def test_duplicate_id_is_reported(self):
        errors = validate_rows(REQUIRED_COLUMNS, [row(), row()])
        self.assertTrue(any("duplicate record_id" in e for e in errors))

    def test_invalid_label_is_reported(self):
        errors = validate_rows(REQUIRED_COLUMNS, [row(primary_intent="unknown")])
        self.assertTrue(any("invalid primary_intent" in e for e in errors))

    def test_pii_token_mismatch_is_reported(self):
        errors = validate_rows(REQUIRED_COLUMNS, [
            row(pii_types="email", pii_span_to_redact="[PHONE]")
        ])
        self.assertTrue(any("requires redaction token [EMAIL]" in e for e in errors))

    def test_missing_column_is_reported(self):
        errors = validate_rows(REQUIRED_COLUMNS[:-1], [row()])
        self.assertTrue(any("Missing required column" in e for e in errors))

    def test_empty_dataset_is_rejected(self):
        errors = validate_rows(REQUIRED_COLUMNS, [])
        self.assertTrue(any("no data rows" in e for e in errors))

    def test_duplicate_headers_are_rejected(self):
        errors = validate_rows(REQUIRED_COLUMNS + ["record_id"], [row()])
        self.assertTrue(any("duplicate column names" in e for e in errors))

    def test_pii_token_must_appear_in_source_message(self):
        errors = validate_rows(REQUIRED_COLUMNS, [
            row(pii_types="email", pii_span_to_redact="[EMAIL]")
        ])
        self.assertTrue(any("does not appear in message_text" in e for e in errors))

    def test_valid_pii_token_in_source_message_passes(self):
        errors = validate_rows(REQUIRED_COLUMNS, [
            row(message_text="Contact me at [EMAIL].", pii_types="email",
                pii_span_to_redact="[EMAIL]")
        ])
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
