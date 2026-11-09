#!/usr/bin/env python3
"""Score a frozen candidate CSV against the separate synthetic gold standard."""
import csv
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIELDS = ("intent", "priority", "action_required")
ALLOWED = {
    "intent": {"billing", "delivery", "product", "returns", "account", "technical", "cancellation", "general"},
    "priority": {"high", "normal", "low"},
    "action_required": {"yes", "no"},
}


def load(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    ids = [row.get("task_id", "").strip() for row in rows]
    if any(not item for item in ids):
        raise ValueError("Every row must have a task_id")
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate task_id values found")
    return {row["task_id"].strip(): row for row in rows}


def parse_single_timestamp(values, field):
    populated = [value.strip() for value in values if value and value.strip()]
    unique = set(populated)
    if len(unique) != 1:
        return None, f"{field}: expected one consistent timestamp repeated across all rows"
    if len(populated) != len(values):
        return None, f"{field}: timestamp is missing from one or more rows"
    try:
        parsed = datetime.fromisoformat(populated[0].replace("Z", "+00:00"))
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            return None, f"{field}: timestamp must include a timezone"
        return parsed, None
    except ValueError:
        return None, f"{field}: invalid ISO-8601 timestamp"


def score(candidate_path):
    gold = load(ROOT / "gold-standard.csv")
    candidate = load(candidate_path)
    if set(candidate) != set(gold):
        missing = sorted(set(gold) - set(candidate))
        extra = sorted(set(candidate) - set(gold))
        raise ValueError(f"Task ID mismatch; missing={missing}, extra={extra}")

    metrics = {}
    exact = 0
    errors = []
    quality_issues = []
    for task_id, gold_row in gold.items():
        candidate_row = candidate[task_id]
        matches = []
        row_valid = True
        for field in FIELDS:
            observed = candidate_row.get(field, "").strip().lower()
            if not observed:
                quality_issues.append({"task_id": task_id, "field": field, "issue": "missing"})
                row_valid = False
            elif observed not in ALLOWED[field]:
                quality_issues.append({"task_id": task_id, "field": field, "issue": "invalid_label", "observed": observed})
                row_valid = False
            matched = observed == gold_row[field].strip().lower()
            matches.append(matched)
            item = metrics.setdefault(field, {"correct": 0, "total": 0})
            item["total"] += 1
            item["correct"] += int(matched)
            if not matched:
                errors.append({"task_id": task_id, "field": field, "expected": gold_row[field], "observed": candidate_row.get(field, "")})
        if row_valid and all(matches):
            exact += 1

    for item in metrics.values():
        item["accuracy_pct"] = round(100 * item["correct"] / item["total"], 2)

    result = {
        "records": len(gold),
        "exact_match": exact,
        "exact_match_pct": round(100 * exact / len(gold), 2),
        "fields": metrics,
        "label_quality_issues": quality_issues,
        "errors": errors,
    }

    starts, start_error = parse_single_timestamp(
        [row.get("started_at_utc", "") for row in candidate.values()], "started_at_utc"
    )
    ends, end_error = parse_single_timestamp(
        [row.get("completed_at_utc", "") for row in candidate.values()], "completed_at_utc"
    )
    timing_errors = [item for item in (start_error, end_error) if item]
    if not timing_errors and starts and ends:
        minutes = (ends - starts).total_seconds() / 60
        if minutes <= 0:
            timing_errors.append("completed_at_utc must be later than started_at_utc")
        else:
            result["elapsed_minutes"] = round(minutes, 2)
            result["records_per_hour"] = round(len(gold) / (minutes / 60), 2)
    if timing_errors:
        result["timing_errors"] = timing_errors
        result["throughput"] = "not calculated"

    return result


if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "candidate-submission-template.csv"
    print(json.dumps(score(path), indent=2))
