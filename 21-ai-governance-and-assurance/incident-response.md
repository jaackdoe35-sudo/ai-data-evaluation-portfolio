# AI Incident Response — TalentScreen (fictional)

**Status:** Proposed playbook; no organization, incident system, on-call team or exercise exists.

## Triggers
Applicant-data disclosure; unauthorized access or tampering; malicious document processing; fabricated candidate facts; material ranking regression; credible discrimination/automation-bias signal; unavailable override/complaint path; untracked model or criteria change.

## Response
1. **Detect:** record time, reporter, version, workflow, scope and evidence pointer; avoid broad circulation of personal data.
2. **Triage:** assign incident lead; assess confidentiality, integrity, availability, rights and decision impact; consider pausing processing.
3. **Contain:** suspend affected feature/version/integration; preserve logs; restrict access; prevent further automated prioritisation where needed.
4. **Assess impact:** identify people, records, decisions, jurisdictions, processors and time window; separate confirmed facts from estimates.
5. **Escalate:** notify system owner, privacy/legal, security, HR process owner and vendor under an approved matrix.
6. **Notification assessment:** qualified privacy/legal personnel determine applicable regulator, data-subject, employment and contractual duties/deadlines. No universal deadline is prescribed here.
7. **Recover:** remediate, validate controls, rerun evaluation and approve restart.
8. **Learn:** update risk register, controls, monitoring and training; track corrective actions.

Preserve logs, versions, configuration, input/output references, access and decision records under documented chain-of-custody and retention rules. Proposed tabletop scenarios: data exposure, manipulated application causing unsupported ranking, and model update regression.

No incident or tabletop has occurred. This is not evidence of operational readiness.
