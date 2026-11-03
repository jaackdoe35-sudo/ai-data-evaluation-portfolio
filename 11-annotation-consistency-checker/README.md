# Project 11 — Annotation Consistency Checker

## Purpose
A lightweight companion to Project 10. It scans annotated CSV records for selected cross-record and cross-field patterns that deserve human review.

## Review flags
- Identical normalized message text assigned different primary-intent labels.
- `intent_unclear` used without setting the clarification flag to `yes`.
- PII type and redaction token combinations that conflict with the portfolio's documented synthetic schema.

## Run
Requires Python 3 and uses only the standard library.

```bash
python consistency_checker.py sample_annotations.csv
```

The tool writes review flags to the terminal. It does not change labels or claim that flagged records are wrong.

## Files
- `consistency_checker.py`: rule-based checker.
- `sample_annotations.csv`: deliberately constructed examples, including one conflicting duplicate.
- `tests/test_consistency_checker.py`: automated unit tests.

## Interpretation
A flag is a prompt for a human reviewer, not an adjudication. Identical text can legitimately receive different labels under different task contexts, and the checker does not have access to all possible context. It deliberately avoids trying to infer semantic correctness from keywords.

## Limitations
This is a small demonstration against the portfolio's synthetic annotation schema. It does not calculate inter-annotator agreement, replace double annotation, or establish production annotation quality.
