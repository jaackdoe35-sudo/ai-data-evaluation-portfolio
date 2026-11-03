# Project 13 — Annotation Data Quality Review Dashboard

## Purpose
A small offline tool that reviews an annotation CSV against selected structural and categorical rules, then generates a self-contained HTML dashboard.

## What it reports
- Number of input records and unique non-empty record IDs.
- Counts by primary intent, sentiment, urgency, PII type and clarification flag.
- Missing required values and duplicate record IDs.
- Invalid primary-intent, sentiment, urgency and clarification labels.
- Mismatches between PII types and their expected synthetic redaction tokens.

## Run
Requires Python 3 and uses only the standard library.

```bash
python qa_dashboard.py sample_annotations.csv --output sample_dashboard.html
python -m unittest discover -s tests -v
```

Open the generated HTML file in a browser. It is a static report and does not upload the CSV or require an online service.

## Sample result
The included seven-record sample deliberately contains three QA flags: one invalid urgency label, one PII-token mismatch and one duplicate ID. See the [sample dashboard](sample_dashboard.html).

## Limitations
This tool checks configured structural and categorical rules only. It does not judge whether an intent label is semantically correct, measure inter-annotator agreement, calculate reviewer accuracy, or establish production readiness. A flag is a prompt for human review, not proof of an annotation error. Review the source message and annotation guidelines before changing a label.
