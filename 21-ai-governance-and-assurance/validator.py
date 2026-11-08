"""CSV structure and reference checks only; no governance effectiveness conclusions."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parent
FILES={
"system-inventory.csv":("system_id",["system_id","system_name","system_status"]),
"risk-register.csv":("risk_id",["risk_id","system_id","risk_domain"]),
"control-matrix.csv":("control_id",["control_id","control_objective","implementation_status"]),
"evidence-register.csv":("evidence_id",["evidence_id","control_or_risk","evidence_status"]),
}
def validate():
    errors=[]; data={}
    for name,(key,required) in FILES.items():
        try:
            with (ROOT/name).open(encoding="utf-8",newline="") as f:
                reader=csv.DictReader(f); headers=reader.fieldnames or []; rows=list(reader)
        except (OSError,UnicodeError,csv.Error) as exc:
            errors.append(f"{name}: {exc}"); continue
        missing=[x for x in required if x not in headers]
        if missing: errors.append(f"{name}: missing columns {missing}")
        if not rows: errors.append(f"{name}: no rows")
        values=[r.get(key,"").strip() for r in rows]
        if any(not v for v in values): errors.append(f"{name}: blank {key}")
        if len(values)!=len(set(values)): errors.append(f"{name}: duplicate {key}")
        data[name]=rows
    if len(data)!=len(FILES): return errors
    systems={r["system_id"] for r in data["system-inventory.csv"]}
    risks={r["risk_id"] for r in data["risk-register.csv"]}
    controls={r["control_id"] for r in data["control-matrix.csv"]}
    for row in data["risk-register.csv"]:
        if row["system_id"] not in systems: errors.append(f"Unknown system: {row['risk_id']}")
    for row in data["control-matrix.csv"]:
        if row["implementation_status"]!="Proposed": errors.append(f"Control not Proposed: {row['control_id']}")
    for row in data["evidence-register.csv"]:
        ref=row["control_or_risk"]
        if ref.startswith("C-") and ref not in controls: errors.append(f"Unknown control: {ref}")
        if ref.startswith("R-") and ref not in risks: errors.append(f"Unknown risk: {ref}")
    return errors
if __name__=="__main__":
    issues=validate()
    if issues:
        print("\n".join(issues)); raise SystemExit(1)
    print("Governance CSV structure valid; no implementation/compliance conclusion implied.")
