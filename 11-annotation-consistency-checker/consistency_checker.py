"""Flag selected annotation consistency patterns for human review."""
import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

PII_TOKENS = {"phone": "[PHONE]", "email": "[EMAIL]", "card_last4": "[LAST4]"}


def normalize_message(value):
    return " ".join((value or "").casefold().split())


def check_rows(rows):
    flags = []
    by_message = defaultdict(list)
    for line_number, row in enumerate(rows, start=2):
        message_key = normalize_message(row.get("message_text"))
        if message_key:
            by_message[message_key].append((line_number, row))

        if row.get("primary_intent") == "intent_unclear" and row.get("clarification_flag") != "yes":
            flags.append(
                f"Row {line_number}: intent_unclear is paired with clarification_flag "
                "other than 'yes'."
            )

        pii_type = (row.get("pii_types") or "").strip()
        redaction = (row.get("pii_span_to_redact") or "").strip()
        if pii_type == "none" and redaction:
            flags.append(f"Row {line_number}: redaction token exists but pii_types is 'none'.")
        elif pii_type in PII_TOKENS and redaction != PII_TOKENS[pii_type]:
            flags.append(
                f"Row {line_number}: pii_types '{pii_type}' does not match expected "
                f"token {PII_TOKENS[pii_type]}."
            )

    for occurrences in by_message.values():
        labels = {row.get("primary_intent", "") for _, row in occurrences}
        if len(occurrences) > 1 and len(labels) > 1:
            line_list = ", ".join(str(line) for line, _ in occurrences)
            flags.append(
                f"Rows {line_list}: identical message text has conflicting primary-intent labels."
            )
    return flags


def check_file(path):
    try:
        with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                return ["CSV has no header row."]
            required = {"message_text", "primary_intent", "clarification_flag",
                        "pii_types", "pii_span_to_redact"}
            missing = sorted(required - set(reader.fieldnames))
            if missing:
                return [f"Missing required column: {name}" for name in missing]
            return check_rows(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        return [f"Could not read CSV: {exc}"]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", help="Path to the annotation CSV file")
    args = parser.parse_args(argv)
    flags = check_file(args.csv_file)
    if flags:
        print(f"Human review recommended for {len(flags)} item(s):")
        for flag in flags:
            print(f"- {flag}")
        return 1
    print("No configured consistency patterns were flagged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
