# Methodology — End-to-End Support Message Annotation

## Task and unit

Single-message support-intent annotation with independent sentiment, urgency, and synthetic PII tagging. Each row is one customer message. This demonstrates a structured workflow, not automated banking decisions.

## Dataset construction

- 40 original synthetic English messages authored for this exercise.
- Coverage includes card servicing, payments, transfers, fees, refunds, account access, suspected fraud, cash withdrawals, and unclear requests.
- Three records contain synthetic PII placeholders; these are literal tokens, not personal data.
- Ambiguous examples deliberately test clarification and abstention.
- No train/test split or model-performance claim is made.

## Annotation procedure

1. Define schema and boundary rules before labeling.
2. Read each message as a complete utterance.
3. Select one primary intent based on requested outcome.
4. Add a secondary intent only for a separate explicit request.
5. Assign sentiment and urgency independently.
6. Detect sensitive placeholders and record the token span.
7. Flag ambiguity where a narrow route is not supported.
8. Write a rationale tied to message evidence.
9. Run structural/schema checks.
10. Manually inspect boundary cases.

## QA design

Automated checks cover expected row count, unique IDs, required fields, allowed categorical values, clarification flag values, and PII-span consistency. Manual review focuses on suspected fraud vs merchant dispute, fee information vs duplicate charge, transfer cancellation vs reversal, card delivery vs lost card, and withdrawal-limit inquiry vs limit-change request.

## Limitations

Dataset and annotations were authored in one session by one annotating agent. Self-audit is not independent review. No second annotator, external gold labels, inter-annotator agreement, throughput measurement, or production deployment was involved.
