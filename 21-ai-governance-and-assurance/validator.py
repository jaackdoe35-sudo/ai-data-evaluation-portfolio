"""CSV structure and reference checks only; no governance effectiveness conclusions."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES = {
    "system-inventory.csv": ("system_id", ["system_id", "system_name", "system_status"]),
    "risk-register.csv": ("risk_id", ["risk_id", "system_id", "risk_domain"]),
    "control-matrix.csv": ("control_id", ["control_id", "control_objective", "implementation_status"]),
    "evidence-register.csv": ("evidence_id", ["evidence_id", "control_or_risk", "evidence_status"]),
    "control-test-plan.csv": ("test_id", ["test_id", "control_id", "test_type", "current_status"]),
}


def validate():
    errors = []
    data = {}
    for name, (key, required) in FILES.items():
        try:
            with (ROOT / name).open(encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames or []
                rows = list(reader)
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"{name}: {exc}")
            continue
        missing = [column for column in required if column not in headers]
        if missing:
            errors.append(f"{name}: missing columns {missing}")
        if not rows:
            errors.append(f"{name}: no rows")
        values = [row.get(key, "").strip() for row in rows]
        if any(not value for value in values):
            errors.append(f"{name}: blank {key}")
        if len(values) != len(set(values)):
            errors.append(f"{name}: duplicate {key}")
        data[name] = rows

    if len(data) != len(FILES):
        return errors

    systems = {row["system_id"] for row in data["system-inventory.csv"]}
    risks = {row["risk_id"] for row in data["risk-register.csv"]}
    controls = {row["control_id"] for row in data["control-matrix.csv"]}

    for row in data["risk-register.csv"]:
        if row["system_id"] not in systems:
            errors.append(f"Unknown system: {row['risk_id']}")
        if row.get("initial_likelihood") != "Not assessed":
            errors.append(f"Risk likelihood must remain Not assessed without evidence: {row['risk_id']}")
        if row.get("residual_rating") != "Not assessed":
            errors.append(f"Residual risk must remain Not assessed: {row['risk_id']}")

    for row in data["control-matrix.csv"]:
        if row["implementation_status"] != "Proposed":
            errors.append(f"Control not Proposed: {row['control_id']}")

    for row in data["evidence-register.csv"]:
        reference = row["control_or_risk"]
        if reference.startswith("C-") and reference not in controls:
            errors.append(f"Unknown control: {reference}")
        if reference.startswith("R-") and reference not in risks:
            errors.append(f"Unknown risk: {reference}")

    for row in data["control-test-plan.csv"]:
        if row["control_id"] not in controls:
            errors.append(f"Unknown control in test plan: {row['test_id']}")
        if row["current_status"] != "not_tested":
            errors.append(f"Control test must remain not_tested until evidence exists: {row['test_id']}")

    return errors


if __name__ == "__main__":
    issues = validate()
    if issues:
        print("\n".join(issues))
        raise SystemExit(1)
    print("Governance CSV structure valid; all controls remain proposed and tests not tested. No effectiveness conclusion implied.")
