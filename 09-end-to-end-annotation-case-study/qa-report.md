# Quality Assurance Report
## Dataset snapshot
- Records: 40
- Unique record IDs: 40
- Duplicate IDs: 0
- Missing message/rationale fields: 0
- PII/span mismatches: 0
- Records flagged for clarification: 6
- Implemented validation issues: 0
## Primary-intent distribution
- suspected_fraud: 4
- fee_information: 3
- intent_unclear: 3
- transfer_status: 3
- account_access: 2
- card_delivery: 2
- refund_status: 2
- account_closure: 1
- card_activation: 1
- card_bill_payment_status: 1
- card_not_working: 1
- card_payment_declined: 1
- card_payment_dispute: 1
- card_replacement_address: 1
- card_retained_by_atm: 1
- cash_withdrawal_dispute: 1
- contactless_payment_issue: 1
- duplicate_charge: 1
- duplicate_transaction: 1
- lost_card: 1
- pin_help: 1
- profile_update: 1
- transfer_cancellation: 1
- transfer_information: 1
- transfer_reference_issue: 1
- transfer_reversal_request: 1
- withdrawal_limit: 1
- withdrawal_limit_change: 1
## Sentiment distribution
- negative: 24
- neutral: 16
## Urgency distribution
- elevated: 9
- routine: 9
- standard: 14
- urgent: 8
## PII distribution
- card_last4: 1
- email: 1
- none: 37
- phone: 1
## Validation result
All implemented structural checks returned zero issues for this dataset snapshot. This demonstrates consistency against the listed checks, not proof that every semantic label is correct.
## Manual boundary review
Reviewed distinctions: unrecognized transaction vs merchant/service dispute; generic fee question vs duplicate charge; scheduled transfer cancellation vs reversal request; missing card vs lost card; asking about a withdrawal limit vs requesting a change; unclear card/statement issue vs a specific route.
## Limitations
The audit was authored by the same annotating agent. It is not independent QA, second-annotator review, or inter-annotator agreement. Production work would require a separate reviewer, adjudication protocol, privacy controls, and taxonomy maintenance.