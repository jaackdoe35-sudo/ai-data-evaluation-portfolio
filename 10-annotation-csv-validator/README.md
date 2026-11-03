# Project 10 — Annotation CSV Validator

## Purpose
A small Python command-line utility that checks an annotation CSV against the schema used in the portfolio's end-to-end support-message case study.

## Checks
- Required columns are present.
- Record IDs are non-empty and unique.
- Required text and rationale fields are populated.
- Primary intent, sentiment, urgency, PII and clarification labels belong to the documented allowed values.
- PII tags and synthetic redaction tokens are internally consistent.
- CSV parsing errors are reported.

The validator reports problems; it does not silently repair or relabel records.

## Run
Requires Python 3 and uses only the standard library.

```bash
python validator.py sample_annotations.csv
```

Exit code is 0 when no validation errors are found and 1 when errors are found.

## Files
- `validator.py`: validation utility.
- `sample_annotations.csv`: small illustrative input containing valid and deliberately invalid rows.
- `tests/test_validator.py`: automated tests using Python's built-in unittest framework.

## Evidence and limitations
This is a self-directed practice tool built for the portfolio's documented synthetic schema. It performs structural and categorical checks, not semantic verification of whether an annotation is correct for the message. A clean result means only that the tested rules passed; it does not establish annotation accuracy or production readiness.
