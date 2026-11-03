"""Recalculate AI response evaluation scores and summarize results."""
import argparse
import csv
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

DIMENSIONS = ("factuality", "instruction_following", "completeness", "clarity", "safety_judgment")
REQUIRED = {"id", *DIMENSIONS, "issue_severity"}
SEVERITIES = {"Critical", "Major", "Minor", "None"}


def analyze_rows(fieldnames, rows):
    if fieldnames is None:
        raise ValueError("CSV has no header row.")
    missing = sorted(REQUIRED - set(fieldnames))
    if missing:
        raise ValueError("Missing required columns: " + ", ".join(missing))
    records, errors = {}, []
    for line, row in enumerate(rows, start=2):
        rid = (row.get("id") or "").strip()
        if not rid:
            errors.append(f"Row {line}: id is empty.")
            continue
        if rid in records:
            errors.append(f"Row {line}: duplicate id '{rid}'.")
            continue
        scores = {}
        for dim in DIMENSIONS:
            raw = (row.get(dim) or "").strip()
            if raw.upper() == "N/A":
                scores[dim] = None
            else:
                try:
                    score = float(raw)
                except ValueError:
                    errors.append(f"Row {line}: {dim} must be 1–5 or N/A.")
                    continue
                if score < 1 or score > 5 or not score.is_integer():
                    errors.append(f"Row {line}: {dim} must be an integer from 1 to 5 or N/A.")
                else:
                    scores[dim] = score
        severity = (row.get("issue_severity") or "").strip()
        if severity not in SEVERITIES:
            errors.append(f"Row {line}: invalid issue_severity '{severity}'.")
        if len(scores) == len(DIMENSIONS) and severity in SEVERITIES:
            available = [v for v in scores.values() if v is not None]
            if not available:
                errors.append(f"Row {line}: at least one dimension must be scored.")
                continue
            records[rid] = {"scores": scores, "mean": round(statistics.mean(available), 1),
                            "severity": severity}
    if errors:
        raise ValueError("\n".join(errors))
    if not records:
        raise ValueError("No valid evaluation records found.")
    return records


def render_report(records):
    dimension_values = defaultdict(list)
    for record in records.values():
        for dim, score in record["scores"].items():
            if score is not None:
                dimension_values[dim].append(score)
    severity_counts = Counter(r["severity"] for r in records.values())
    means = [r["mean"] for r in records.values()]
    lines = [
        "# AI Response Evaluation Score Summary", "",
        f"- Evaluated responses: {len(records)}",
        f"- Mean overall score: {statistics.mean(means):.2f}/5",
        f"- Lowest overall score: {min(means):.1f}/5",
        f"- Highest overall score: {max(means):.1f}/5", "",
        "## Mean score by dimension", "",
        "| Dimension | Mean | Scored records |", "|---|---:|---:|",
    ]
    for dim in DIMENSIONS:
        vals = dimension_values[dim]
        lines.append(f"| {dim.replace('_', ' ').title()} | {statistics.mean(vals):.2f} | {len(vals)} |" if vals else f"| {dim} | N/A | 0 |")
    lines += ["", "## Issue severity", "", "| Severity | Count |", "|---|---:|"]
    for severity in ("Critical", "Major", "Minor", "None"):
        lines.append(f"| {severity} | {severity_counts[severity]} |")
    lines += ["", "## Recalculated record scores", "", "| ID | Overall mean | Severity |", "|---|---:|---|"]
    for rid, record in sorted(records.items()):
        lines.append(f"| {rid} | {record['mean']:.1f} | {record['severity']} |")
    lines += ["", "## Interpretation limits", "",
              "Scores summarize the supplied dimension ratings; they do not independently establish whether those ratings are correct. Read the original prompt, response and evidence rationale before making a quality decision. N/A dimensions are excluded from that record's mean.", ""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv")
    parser.add_argument("--output", default="evaluation_summary.md")
    args = parser.parse_args(argv)
    try:
        with Path(args.input_csv).open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            records = analyze_rows(reader.fieldnames, reader)
        Path(args.output).write_text(render_report(records), encoding="utf-8")
        print(f"Processed {len(records)} records. Summary written to {args.output}.")
        return 0
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"Evaluation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
