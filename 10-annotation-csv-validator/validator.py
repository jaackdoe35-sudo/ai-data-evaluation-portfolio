"""Validate annotation CSV files against the portfolio case-study schema."""
import argparse
import csv
import sys
from pathlib import Path

REQUIRED_COLUMNS = [
    "record_id", "message_text", "primary_intent", "secondary_intent",
    "sentiment", "urgency", "pii_types", "pii_span_to_redact",
    "clarification_flag", "annotation_rationale",
]
PRIMARY_INTENTS = {
    "account_access", "account_closure", "profile_update", "card_activation",
    "card_delivery", "card_replacement_address", "card_not_working",
    "card_payment_declined", "contactless_payment_issue", "card_payment_dispute",
    "card_bill_payment_status", "card_retained_by_atm", "lost_card",
    "suspected_fraud", "cash_withdrawal_dispute", "withdrawal_limit",
    "withdrawal_limit_change", "transfer_status", "transfer_information",
    "transfer_cancellation", "transfer_reversal_request",
    "transfer_reference_issue", "duplicate_transaction", "duplicate_charge",
    "fee_information", "refund_status", "pin_help", "intent_unclear",
}
SENTIMENTS = {"positive", "neutral", "negative"}
URGENCIES = {"routine", "standard", "elevated", "urgent"}
PII_TYPES = {"none", "phone", "email", "card_last4"}
CLARIFICATION_FLAGS = {"yes", "no"}
PII_TOKENS = {"phone": "[PHONE]", "email": "[EMAIL]", "card_last4": "[LAST4]"}


def validate_rows(fieldnames, rows):
    errors = []
    if fieldnames is None:
        return ["CSV has no header row."]
    if len(fieldnames) != len(set(fieldnames)):
        return ["CSV contains duplicate column names."]
    missing = [name for name in REQUIRED_COLUMNS if name not in fieldnames]
    if missing:
        return [f"Missing required column: {name}" for name in missing]

    rows = list(rows)
    if not rows:
        return ["CSV contains a header but no data rows."]
    seen_ids = set()
    for line_number, row in enumerate(rows, start=2):
        record_id = (row.get("record_id") or "").strip()
        if not record_id:
            errors.append(f"Row {line_number}: record_id is empty.")
        elif record_id in seen_ids:
            errors.append(f"Row {line_number}: duplicate record_id '{record_id}'.")
        else:
            seen_ids.add(record_id)

        for column in ("message_text", "primary_intent", "sentiment", "urgency",
                       "pii_types", "clarification_flag", "annotation_rationale"):
            if not (row.get(column) or "").strip():
                errors.append(f"Row {line_number}: required value '{column}' is empty.")

        checks = {
            "primary_intent": PRIMARY_INTENTS,
            "sentiment": SENTIMENTS,
            "urgency": URGENCIES,
            "pii_types": PII_TYPES,
            "clarification_flag": CLARIFICATION_FLAGS,
        }
        for column, allowed in checks.items():
            value = (row.get(column) or "").strip()
            if value and value not in allowed:
                errors.append(f"Row {line_number}: invalid {column} value '{value}'.")

        pii_type = (row.get("pii_types") or "").strip()
        redaction = (row.get("pii_span_to_redact") or "").strip()
        if pii_type == "none" and redaction:
            errors.append(f"Row {line_number}: PII span supplied while pii_types is 'none'.")
        elif pii_type in PII_TOKENS:
            expected_token = PII_TOKENS[pii_type]
            if redaction != expected_token:
                errors.append(
                    f"Row {line_number}: {pii_type} requires redaction token "
                    f"{expected_token}."
                )
            if expected_token not in (row.get("message_text") or ""):
                errors.append(
                    f"Row {line_number}: expected PII token {expected_token} "
                    "does not appear in message_text."
                )
    return errors


def validate_file(path):
    try:
        with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            return validate_rows(reader.fieldnames, reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        return [f"Could not read CSV: {exc}"]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", help="Path to the annotation CSV file")
    args = parser.parse_args(argv)
    errors = validate_file(args.csv_file)
    if errors:
        print(f"Validation found {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Validation passed: no issues found by the configured structural rules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
