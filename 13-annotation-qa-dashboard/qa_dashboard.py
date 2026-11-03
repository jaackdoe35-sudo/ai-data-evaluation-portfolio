"""Generate a self-contained HTML quality review dashboard for annotation CSV data."""
import argparse
import csv
import html
import sys
from collections import Counter
from pathlib import Path

REQUIRED = ("record_id", "message_text", "primary_intent", "sentiment", "urgency",
            "pii_types", "pii_span_to_redact", "clarification_flag", "annotation_rationale")
SENTIMENTS = {"positive", "neutral", "negative"}
URGENCIES = {"routine", "standard", "elevated", "urgent"}
PII = {"none": "", "phone": "[PHONE]", "email": "[EMAIL]", "card_last4": "[LAST4]"}


def inspect(fieldnames, rows):
    if fieldnames is None:
        raise ValueError("CSV has no header row.")
    missing_columns = sorted(set(REQUIRED) - set(fieldnames))
    if missing_columns:
        raise ValueError("Missing required columns: " + ", ".join(missing_columns))
    rows = list(rows)
    issues, ids = [], Counter()
    for line, row in enumerate(rows, start=2):
        rid = (row.get("record_id") or "").strip()
        if rid:
            ids[rid] += 1
        else:
            issues.append((line, "Missing record ID", "record_id is empty"))
        for field in ("message_text", "primary_intent", "sentiment", "urgency",
                      "pii_types", "clarification_flag", "annotation_rationale"):
            if not (row.get(field) or "").strip():
                issues.append((line, "Missing required value", field))
        if row.get("sentiment") not in SENTIMENTS:
            issues.append((line, "Invalid sentiment", row.get("sentiment", "")))
        if row.get("urgency") not in URGENCIES:
            issues.append((line, "Invalid urgency", row.get("urgency", "")))
        pii_type = (row.get("pii_types") or "").strip()
        token = (row.get("pii_span_to_redact") or "").strip()
        if pii_type not in PII:
            issues.append((line, "Invalid PII type", pii_type))
        elif PII[pii_type] != token:
            issues.append((line, "PII token mismatch", f"{pii_type} / {token or '(blank)'}"))
        if row.get("clarification_flag") not in {"yes", "no"}:
            issues.append((line, "Invalid clarification flag", row.get("clarification_flag", "")))
    for rid, count in ids.items():
        if count > 1:
            issues.append(("—", "Duplicate record ID", f"{rid} appears {count} times"))
    return {"rows": rows, "issues": issues}


def table(counter, title):
    body = "".join(f"<tr><td>{html.escape(str(k))}</td><td>{v}</td></tr>"
                   for k, v in sorted(counter.items()))
    return f"<section><h2>{html.escape(title)}</h2><table><thead><tr><th>Value</th><th>Count</th></tr></thead><tbody>{body or '<tr><td colspan=2>No values</td></tr>'}</tbody></table></section>"


def render_dashboard(result, source_name):
    rows, issues = result["rows"], result["issues"]
    distributions = {
        "Primary intent": Counter((r.get("primary_intent") or "(blank)") for r in rows),
        "Sentiment": Counter((r.get("sentiment") or "(blank)") for r in rows),
        "Urgency": Counter((r.get("urgency") or "(blank)") for r in rows),
        "PII type": Counter((r.get("pii_types") or "(blank)") for r in rows),
        "Clarification required": Counter((r.get("clarification_flag") or "(blank)") for r in rows),
    }
    issue_rows = "".join(
        f"<tr><td>{html.escape(str(line))}</td><td>{html.escape(kind)}</td><td>{html.escape(detail)}</td></tr>"
        for line, kind, detail in issues
    ) or '<tr><td colspan="3">No configured QA issues found.</td></tr>'
    sections = "".join(table(counter, title) for title, counter in distributions.items())
    status = "Review required" if issues else "No configured issues found"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Annotation QA Dashboard</title>
<style>
body{{font:16px system-ui,sans-serif;max-width:1100px;margin:2rem auto;padding:0 1rem;color:#202820;background:#fafaf7}}
h1,h2{{color:#183b2b}}.metrics{{display:flex;gap:1rem;flex-wrap:wrap}}.metric{{border:1px solid #ccd5cc;border-radius:8px;padding:1rem;min-width:150px;background:white}}
.metric strong{{display:block;font-size:1.7rem}}section{{margin:2rem 0}}table{{border-collapse:collapse;width:100%;background:white}}th,td{{border:1px solid #d8ded8;padding:.55rem;text-align:left}}th{{background:#eef2ed}}.status{{font-weight:700}}.note{{color:#4d5b50}}
</style></head><body>
<h1>Annotation QA Dashboard</h1><p class="note">Source file: {html.escape(source_name)} · Rule-based review only</p>
<div class="metrics"><div class="metric"><strong>{len(rows)}</strong>Records</div>
<div class="metric"><strong>{len(issues)}</strong>QA flags</div>
<div class="metric"><strong>{len({(r.get("record_id") or "").strip() for r in rows if (r.get("record_id") or "").strip()})}</strong>Unique non-empty IDs</div></div>
<p class="status">{status}</p>
{sections}
<section><h2>QA findings</h2><table><thead><tr><th>CSV line</th><th>Finding</th><th>Details</th></tr></thead><tbody>{issue_rows}</tbody></table></section>
<p class="note">A flag is a review lead, not proof that an annotation is wrong. This dashboard checks selected structural and categorical rules; it does not assess semantic correctness, annotator agreement, or production readiness. Review the source records and task guidelines before making corrections.</p>
</body></html>"""


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv")
    parser.add_argument("--output", default="annotation_qa_dashboard.html")
    args = parser.parse_args(argv)
    try:
        with Path(args.input_csv).open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            result = inspect(reader.fieldnames, reader)
        Path(args.output).write_text(render_dashboard(result, Path(args.input_csv).name), encoding="utf-8")
        print(f"Reviewed {len(result['rows'])} records; {len(result['issues'])} QA flag(s). Dashboard: {args.output}")
        return 0
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"Dashboard generation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
