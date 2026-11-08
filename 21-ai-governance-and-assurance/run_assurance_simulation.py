"""Evaluate synthetic TalentScreen control evidence; not a real audit."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/"synthetic-control-evidence.json").read_text(encoding="utf-8"))

def assess(c):
    e=c["evidence"]; cid=c["control_id"]
    if cid=="C-001":
        if not e["inventory_approved"] or not e["owner_assigned"]: return "fail","Inventory approval and accountable owner are absent."
    elif cid=="C-002":
        if not e["impact_assessment_complete"] or not e["affected_groups_mapped"]: return "fail","Impact assessment or affected-group mapping is absent."
        if not e["challenge_route_defined"]: return "partial","Applicant challenge/correction route is not defined."
    elif cid=="C-003":
        if not e["lineage_complete"] or not e["retention_schedule_approved"] or not e["deletion_test_passed"]: return "fail","Lineage, retention approval or deletion test is incomplete."
    elif cid=="C-004":
        if e["risks_with_owner"]<e["material_risks"] or e["treatments_approved"]<e["material_risks"]: return "fail","Not all material risks have owners and approved treatments."
    elif cid=="C-005":
        if e["reviewer_test_cases"]<=0 or e["material_errors_seeded"]<=0: return "not_tested","No usable reviewer test sample."
        if e["material_errors_detected"]<e["material_errors_seeded"] or not e["reviewer_test_passed"]: return "fail","At least one seeded material error was missed."
    elif cid=="C-006":
        if not e["evaluation_run_exists"]: return "not_tested","No evaluation run exists."
        if not e["thresholds_pre_registered"] or not e["subgroup_results_available"] or not e["evaluation_thresholds_met"]: return "fail","No pre-registered thresholds, subgroup results or demonstrated threshold attainment."
    elif cid=="C-007":
        if not all(e[k] for k in ("notice_approved","purpose_described","limitations_described","challenge_route_described")): return "fail","Approved notice is incomplete."
    elif cid=="C-008":
        n=e["sample_size"]
        if n<=0: return "not_tested","No log sample."
        complete=min(e["records_with_actor"],e["records_with_timestamp"],e["records_with_model_version"],e["records_with_source_reference"])
        if complete<n: return "partial",f"{n-complete} of {n} records lack at least one required traceability field."
    elif cid=="C-009":
        if not e["access_test_run"]: return "not_tested","No access test."
        if e["blocked_attempts"]<e["unauthorized_access_attempts"]: return "fail","One or more unauthorized access attempts were not blocked."
        if not e["incident_tabletop_run"]: return "partial","Incident response tabletop has not been performed."
    elif cid=="C-010":
        if not all(e[k] for k in ("metrics_defined","thresholds_approved","alert_test_run","alert_received")): return "fail","Monitoring/alert design or alert test is incomplete."
        if not e["pause_decision_recorded"] or not e["revalidation_completed"]: return "partial","Pause decision or post-alert revalidation is missing."
    else: return "not_tested","No rule for control."
    return "pass","All exercise-specific evidence predicates were met."
def run():
    rows=[]
    for c in DATA["controls"]:
        result,reason=assess(c)
        rows.append({"control_id":c["control_id"],"objective":c["objective"],"expected_result":c["expected_result"],"observed_result":result,"matches_fixture_expectation":result==c["expected_result"],"reason":reason,"evidence":c["evidence"]})
    return {"case_id":DATA["case_id"],"notice":DATA["notice"],"counts":{k:sum(x["observed_result"]==k for x in rows) for k in ("pass","partial","fail","not_tested")},"all_fixture_expectations_match":all(x["matches_fixture_expectation"] for x in rows),"controls":rows}
if __name__=="__main__":
    result=run()
    print(json.dumps(result,indent=2))
    if not result["all_fixture_expectations_match"]: raise SystemExit(1)
