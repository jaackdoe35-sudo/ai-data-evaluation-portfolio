#!/usr/bin/env python3
"""Score a frozen candidate CSV against the separate synthetic gold standard."""
import csv, sys
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parent
FIELDS=("intent","priority","action_required")

def load(path):
    with path.open(encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    return {r["task_id"]:r for r in rows}

def score(candidate_path):
    gold=load(ROOT/"gold-standard.csv")
    candidate=load(candidate_path)
    if set(candidate)!=set(gold):
        missing=sorted(set(gold)-set(candidate)); extra=sorted(set(candidate)-set(gold))
        raise ValueError(f"Task ID mismatch; missing={missing}, extra={extra}")
    metrics={}
    exact=0
    errors=[]
    for task_id,g in gold.items():
        c=candidate[task_id]
        matches=[c.get(field,"").strip().lower()==g[field].strip().lower() for field in FIELDS]
        exact+=all(matches)
        for field,ok in zip(FIELDS,matches):
            item=metrics.setdefault(field,{"correct":0,"total":0})
            item["total"]+=1; item["correct"]+=int(ok)
            if not ok: errors.append({"task_id":task_id,"field":field,"expected":g[field],"observed":c.get(field,"")})
    for item in metrics.values(): item["accuracy_pct"]=round(100*item["correct"]/item["total"],2)
    result={"records":len(gold),"exact_match":exact,"exact_match_pct":round(100*exact/len(gold),2),"fields":metrics,"errors":errors}
    starts=[r.get("started_at_utc","").strip() for r in candidate.values() if r.get("started_at_utc","").strip()]
    ends=[r.get("completed_at_utc","").strip() for r in candidate.values() if r.get("completed_at_utc","").strip()]
    if len(starts)==1 and len(ends)==1:
        try:
            start=datetime.fromisoformat(starts[0].replace("Z","+00:00")); end=datetime.fromisoformat(ends[0].replace("Z","+00:00"))
            minutes=(end-start).total_seconds()/60
            if minutes<=0: raise ValueError("Finish must be after start")
            result["elapsed_minutes"]=round(minutes,2)
            result["records_per_hour"]=round(len(gold)/(minutes/60),2)
        except ValueError as exc: result["timing_error"]=str(exc)
    else: result["throughput"]="not calculated: provide one valid start and finish timestamp"
    return result

if __name__=="__main__":
    path=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/"candidate-submission-template.csv"
    print(__import__("json").dumps(score(path),indent=2))
