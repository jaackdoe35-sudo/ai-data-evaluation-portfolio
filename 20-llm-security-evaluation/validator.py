"""Structural validator for the AI security evaluation scenario catalogue.

This validates the test specification, not a target model's security behavior.
"""
import json
import sys
from pathlib import Path

REQUIRED_CASE_FIELDS = {
    "id", "category", "risk", "scenario", "test_input",
    "expected_behavior", "failure_indicators", "safe_success_indicators",
}
ALLOWED_RISKS = {"low", "medium", "high"}


def validate_catalogue(data):
    errors = []
    if data.get("status") != "test_specifications_only":
        errors.append("Catalogue status must remain test_specifications_only.")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["cases must be a non-empty list."]
    seen = set()
    for index, case in enumerate(cases, start=1):
        prefix = f"Case {index}"
        if not isinstance(case, dict):
            errors.append(f"{prefix}: must be an object.")
            continue
        missing = REQUIRED_CASE_FIELDS - set(case)
        for field in sorted(missing):
            errors.append(f"{prefix}: missing required field '{field}'.")
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{prefix}: id must be a non-empty string.")
        elif case_id in seen:
            errors.append(f"{prefix}: duplicate id '{case_id}'.")
        else:
            seen.add(case_id)
        if case.get("risk") not in ALLOWED_RISKS:
            errors.append(f"{prefix}: risk must be low, medium, or high.")
        for field in ("category", "scenario", "test_input", "expected_behavior"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                errors.append(f"{prefix}: '{field}' must be a non-empty string.")
        for field in ("failure_indicators", "safe_success_indicators"):
            value = case.get(field)
            if not isinstance(value, list) or not value or not all(
                isinstance(item, str) and item.strip() for item in value
            ):
                errors.append(f"{prefix}: '{field}' must be a non-empty list of strings.")
    return errors


def main(argv=None):
    path = Path(argv[1] if argv and len(argv) > 1 else
                Path(__file__).with_name("security-evaluation-cases.json"))
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"Could not read catalogue: {exc}")
        return 1
    errors = validate_catalogue(data)
    if errors:
        print(f"Catalogue validation found {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Catalogue structure valid: {len(data['cases'])} scenarios; no model execution implied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
