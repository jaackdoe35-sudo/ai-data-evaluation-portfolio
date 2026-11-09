# Project 22 — Structured Annotation Practice Assessment

**Status:** assessment pack prepared; candidate performance not yet measured  
**Dataset:** 30 synthetic support tasks  
**Scoring:** field-level accuracy, exact-match accuracy and elapsed throughput  
**Security:** public honor-system exercise; reference labels are not access-controlled

## Purpose

This assessment is designed to measure a candidate's own instruction-following, intent classification, priority assignment, action-needed judgment, rationale quality and throughput on a fixed 30-item support queue.

## Candidate procedure

1. Use only `tasks.csv` and the blank submission template. Do not inspect `gold-standard.csv` before freezing the submission. The reference file is public, so this relies on candidate integrity rather than technical access control.
2. Work independently. Do not use an LLM to generate labels if the purpose is to measure personal annotation performance.
3. Start a timer immediately before task T001. Record the same ISO-8601 UTC start timestamp on all 30 rows; record one consistent finish timestamp after T030.
4. For each task, enter one allowed intent, priority and action_required value.
5. Add a short rationale tied to the message and mark confidence high/medium/low.
6. Do not invent facts. If a message is ambiguous, choose the closest supported label and explain the uncertainty.
7. Freeze the submission before viewing the answer key. Preserve the original submission and score output.

## Label schema

- intent: billing, delivery, product, returns, account, technical, cancellation, general
- priority: high, normal, low
- action_required: yes or no
- confidence: high, medium or low

Priority and action-required guidance are defined in the task pack and should be applied consistently.

## Scoring and interpretation

The scorer reports field-level accuracy, strict exact-match accuracy, missing/invalid labels, confusion counts and elapsed throughput. It validates all 30 task IDs, allowed labels and consistent timezone-aware timestamps. It does not grade rationale quality or confidence calibration; those require manual review against the rubric.

Suggested internal readiness gates are explicitly practice thresholds, not employer standards. A result below the suggested gate should trigger error analysis and a fresh practice set, not retroactive changes to the key.

Throughput must be interpreted alongside accuracy. A fast submission with poor labeling is not a quality result.

## Files

- `tasks.csv`: task set.
- `candidate-submission-template.csv`: blank submission.
- `gold-standard.csv`: reference labels; do not inspect before freezing.
- `score_submission.py`: scoring and timing validator.
- `second-review-protocol.md`: independent second-rater procedure.

## Current result

No candidate submission has been recorded in the repository. Therefore there is no verified personal accuracy, exact-match score, rationale score, confidence calibration or throughput to report. The assessment is prepared but incomplete as evidence of the candidate's own performance.

## Limitations

This is a small synthetic practice set, not a validated psychometric instrument, real client guideline set, statistically representative benchmark or proof of production experience. The reference key is publicly accessible, so it is not a secure blind assessment.
