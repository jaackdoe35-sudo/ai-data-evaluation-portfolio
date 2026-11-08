# Production-Style Annotation Assessment

**Status: assessment pack prepared; candidate performance not yet measured.** All messages are synthetic. The answer key is separate from the task file. Do not publish candidate results until a completed submission has been scored.

## Objective
Measure instruction-following, intent classification, priority assignment, action-needed judgment, rationale quality and throughput on a fixed 30-item customer-support queue.

## Rules
1. Use only the task file; do not inspect the answer key before submitting.
2. Work independently. Do not use an LLM to generate labels if the purpose is to measure your own annotation performance.
3. Start a timer immediately before task T001. Record start and finish timestamps in UTC in the submission file.
4. For each task, enter exactly one allowed intent, priority and action_required value.
5. Add a short rationale tied to the message. Mark confidence high/medium/low.
6. Do not invent facts. If the message is ambiguous, record the closest supported label and explain uncertainty.
7. Stop the timer after T030. Do not edit answers after viewing the answer key.
8. Score the submission with the provided script. Preserve the original submission and score output.

## Label schema
- intent: billing, delivery, product, returns, account, technical, cancellation, general
- priority: high, normal, low
- action_required: yes or no
- confidence: high, medium or low

Priority guide:
- high: financial loss, security/account compromise, missing parcel with claimed delivery, imminent cancellation/dispatch, or similarly urgent customer impact.
- normal: a problem requiring support action but without an immediate severe impact.
- low: informational request, positive acknowledgement or no action needed.

Action-required guide:
- yes: the customer asks for help, reports an unresolved problem, requests a change or needs a response.
- no: informational/positive message that does not require a case action based on the supplied text.

## Files
- `tasks.csv`: blind task set.
- `candidate-submission-template.csv`: blank submission with timestamp and rationale fields.
- `gold-standard.csv`: reference labels; keep hidden until submission is frozen.
- `score_submission.py`: computes per-field accuracy, exact-match accuracy, confusion counts and elapsed throughput.
- `second-review-protocol.md`: independent second-rater process.

## Scoring
The script reports field-level accuracy and strict exact-match accuracy. It does not grade rationale quality or confidence calibration. Review those manually against the rubric. Report all denominators and missing labels. No benchmark ranking or industry pass threshold is claimed.

Suggested internal readiness gate (not an employer standard): >=90% intent, >=90% priority, >=95% action_required, >=85% exact match, no critical account-security or financial urgency error, and no missing records. If below the gate, diagnose and repeat with a new blind set rather than changing the answer key.

## Throughput
Elapsed minutes = finish timestamp - start timestamp. Throughput = completed records / elapsed hours. Only compute when both timestamps are valid and all 30 tasks are present. Report speed beside accuracy; speed without accuracy is not a quality result.

## Limitations
This is a small synthetic practice set, not a validated psychometric instrument, real client guideline set, statistically representative benchmark or proof of production experience.
