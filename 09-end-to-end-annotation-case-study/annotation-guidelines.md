# Annotation Guidelines — End-to-End Support Message Case Study
## Task
Annotate each single customer-support message with one primary intent, optional secondary intent, sentiment, urgency, sensitive-data type, exact synthetic redaction token, clarification flag, and concise evidence-based rationale. Do not infer account state, transaction outcome, policy entitlement, or facts absent from the message.
## Primary-intent taxonomy
| Label | Definition and boundary |
|---|---|
| account_access | Login, lockout, password reset, or access failure; not profile edits |
| account_closure | Explicit request to close an account |
| profile_update | Change account contact/profile details when no card replacement is the main request |
| card_activation | Activate a newly received card |
| card_delivery | Missing, delayed, or tracking a physical card; lost cards use lost_card |
| card_replacement_address | Requests a replacement card and/or its delivery to a new address |
| card_not_working | General physical-card malfunction |
| card_payment_declined | Card payment declined; do not assume the cause |
| contactless_payment_issue | Contactless fails while other card use may work |
| card_payment_dispute | Disputes a card payment for a stated merchant/service issue; unrecognized use is suspected_fraud |
| card_bill_payment_status | Status of a payment toward a credit-card bill |
| card_retained_by_atm | ATM physically retained the card |
| lost_card | Card reported lost or misplaced |
| suspected_fraud | User reports unrecognized/apparently unauthorized activity; do not state fraud is confirmed |
| cash_withdrawal_dispute | ATM debited account but did not dispense cash |
| withdrawal_limit | Asks about current cash withdrawal limit |
| withdrawal_limit_change | Requests a change to withdrawal limit |
| transfer_status | Status/receipt/progress of a specific transfer |
| transfer_information | General question about transfer mechanics or definitions |
| transfer_cancellation | Requests cancellation of a pending/scheduled transfer |
| transfer_reversal_request | Requests reversal/recovery after sending to wrong recipient; do not promise recovery |
| transfer_reference_issue | Wrong/missing transfer reference while destination is stated correct |
| duplicate_transaction | Reports a transaction appearing more than once |
| duplicate_charge | Reports same fee/charge applied more than once |
| fee_information | Asks what a fee is, amount, or calculation; a specific disputed charge may need clarification |
| refund_status | Asks about timing/receipt of an expected refund; do not infer entitlement |
| pin_help | Requests safe PIN guidance; never request the PIN itself |
| intent_unclear | Text lacks enough detail or contains unresolved competing intents |
## Sentiment
- positive: explicit satisfaction, gratitude, or positive evaluation.
- neutral: factual question/request without clear emotional polarity.
- negative: frustration, worry, dissatisfaction, or adverse experience.
Sentiment is independent of urgency; negative does not automatically mean urgent.
## Urgency
- routine: ordinary information or non-time-sensitive request.
- standard: normal service issue with no immediate risk indicated.
- elevated: time-sensitive, disputed funds, unresolved transaction, or significant access issue.
- urgent: lost/retained card, suspected unauthorized activity, or immediate protective action requested.
Urgency is triage priority inferred only from message content; do not infer actual financial loss or account compromise.
## PII detection and redaction
Allowed tags: none, phone, email, card_last4. This dataset uses only synthetic tokens [PHONE], [EMAIL], and [LAST4]. Never invent real identifiers. In production, follow client privacy policy and applicable law. Last-four card digits are treated as sensitive here.
## Clarification flag
Set yes when the message cannot support a reliable narrow intent, contains materially competing interpretations, or lacks essential routing detail. The flag supplements rather than replaces the best available primary label.
## Decision hierarchy
1. Identify the requested outcome, not just keywords.
2. Prefer the narrowest supported intent.
3. Separate reported facts from suspicions or hypotheses.
4. Do not infer causes, policy outcomes, reversibility, or account status.
5. Use intent_unclear when a defensible route is not possible.
6. Assign sentiment and urgency independently.
7. Detect synthetic identifiers and preserve only the placeholder token in the redaction field.
8. Tie the rationale to message evidence.
## Quality-control rules
- One unique record_id per message; exactly one primary intent.
- Secondary intent is blank unless a separate request is explicit.
- Categorical values must belong to the schema.
- pii_types=none requires an empty redaction span; non-none PII requires a token span.
- Every record needs a rationale.
- Flag ambiguity instead of guessing.
- Record any post-review change with original label, revised label, reason, and reviewer status.
## Limitations
This taxonomy is for a small synthetic English-language portfolio exercise. It is not a client taxonomy, financial-services compliance policy, fraud procedure, or substitute for organizational security/privacy rules.