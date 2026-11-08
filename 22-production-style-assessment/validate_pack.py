"""Validate the production-style annotation pack without scoring candidate performance."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parent
ALLOWED={
 "intent":{"billing","delivery","product","returns","account","technical","cancellation","general"},
 "priority":{"high","normal","low"},
 "action_required":{"yes","no"},
}
def read(name):
 with (ROOT/name).open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def validate():
 errors=[]
 try:
  tasks=read("tasks.csv"); gold=read("gold-standard.csv"); template=read("candidate-submission-template.csv")
 except (OSError,csv.Error) as exc:return [str(exc)]
 ids=[r.get("task_id","").strip() for r in tasks]
 if len(ids)!=30:errors.append(f"Expected 30 tasks, found {len(ids)}")
 if len(ids)!=len(set(ids)):errors.append("Duplicate task IDs")
 if set(ids)!={f"T{i:03d}" for i in range(1,31)}:errors.append("Task IDs must be T001–T030")
 if {r.get("task_id") for r in gold}!=set(ids):errors.append("Gold key task IDs differ from task set")
 if {r.get("task_id") for r in template}!=set(ids):errors.append("Submission template task IDs differ from task set")
 for row in gold:
  for field,allowed in ALLOWED.items():
   if row.get(field) not in allowed:errors.append(f"{row.get('task_id')}: invalid {field} label")
 for row in template:
  for field in ALLOWED:
   if row.get(field,"").strip():errors.append(f"{row.get('task_id')}: candidate template must be blank in {field}")
 if any(not r.get("message","").strip() for r in tasks):errors.append("Blank task message")
 return errors
if __name__=="__main__":
 issues=validate()
 if issues:print("\n".join(issues));raise SystemExit(1)
 print("Assessment pack structurally valid: 30 tasks, aligned reference key and blank candidate template. Candidate performance not measured.")
