# TalentScreen — Connected AI Governance Case Study

**Case type:** fictional, self-directed governance and assurance exercise
**System:** GOV-001 TalentScreen, an AI-assisted recruitment-screening workflow
**Evidence boundary:** no real organization, applicant data, deployed model, production workflow, control owner or independent audit exists.

## Executive question
Can the organization justify using an AI-assisted system to extract candidate information and prioritize a recruiter review queue, while preventing the ranking from becoming an unreviewed employment decision?

This is a connected governance programme, not a collection of standalone templates. Each phase produces an artifact used by the next phase.

## Governance lifecycle and artifact traceability

| Phase | Governance question | Primary artifact | Output carried forward |
|---|---|---|---|
| 1. Intake and inventory | What is the system, intended use, boundary and accountable owner? | [System inventory](system-inventory.csv) | GOV-001, intended use, data inputs, decision impact and explicit unknowns |
| 2. Impact assessment | Who may be affected and how could harm occur? | [Impact assessment](impact-assessment.md) | Fairness, validity, privacy, oversight, transparency, security and lifecycle pathways |
| 3. Risk analysis | What can go wrong, why, and what evidence would establish it? | [Risk register](risk-register.csv) and [methodology](risk-methodology.md) | R-001–R-008, evidence requirements and unassessed likelihood/residual risk |
| 4. Control design | What should prevent, detect or correct each risk? | [Control matrix](control-matrix.csv) | C-001–C-010 proposed objectives; no implementation credit |
| 5. Assurance planning | How would each control be tested? | [Control test plan](control-test-plan.csv) | TP-001–TP-010 with procedures, samples and acceptance criteria |
| 6. Evidence collection | What evidence exists, who should own it, and what is missing? | [Evidence register](evidence-register.csv) | E-001–E-010 with evidence status and review procedure |
| 7. Simulated test | What would a test conclude if seeded evidence were supplied? | [Synthetic fixture](synthetic-control-evidence.json), [runner](run_assurance_simulation.py) | Deterministic exercise classifications, not observations of a real system |
| 8. Findings and remediation | What gaps require action, ownership and closure evidence? | [Simulation report](simulation-report.md), [remediation tracker](remediation-tracker.csv) | Exercise findings with proposed corrective actions and closure tests |
| 9. Assurance conclusion | What can be stated without overstating the evidence? | [Assurance workpaper](assurance-workpaper.md) and [report](assurance-report.md) | Design exercise completed; real system assurance not established |

## Decision rights and governance gates
The following are proposed case-study decision rights, not actual appointments or approvals:
- **Business sponsor:** accountable for business purpose and whether the use case proceeds to assessment.
- **AI governance lead:** coordinates inventory, impact assessment, risk treatment and evidence traceability.
- **HR process owner:** defines job-related criteria, reviewer workflow and applicant challenge routes.
- **Privacy/legal reviewer:** determines applicable jurisdictions, legal roles, privacy requirements and regulatory interpretation.
- **Security lead:** reviews data flows, identity/access, integrations, logging and incident response.
- **Model/system owner:** supplies model, data, evaluation, version and change evidence.
- **Independent assurance reviewer:** challenges the evidence and tests; must not be the author of the controls being assessed.

### Gate sequence
1. **Intake:** purpose, system boundary, jurisdiction, provider and accountable owner must be identified or recorded as unresolved.
2. **Impact/risk:** material impacts map to risks, mitigations, owners and evidence requirements. Unknowns remain open.
3. **Design:** each control objective maps to risks and a test procedure.
4. **Implementation:** proposed controls receive no operating-effectiveness credit until implementation evidence is inspected.
5. **Pre-deployment:** unresolved critical legal, privacy, security, fairness or oversight questions prevent a positive readiness conclusion.
6. **Monitoring:** model, data, role criteria, vendor or workflow changes trigger reassessment.
7. **Independent assurance:** the reviewer receives source evidence, samples, test results and prior findings; disagreements and limitations are recorded.

## Risk-to-control traceability

| Risk | Risk pathway | Proposed control(s) | Test(s) | Evidence expected |
|---|---|---|---|---|
| R-001 Fairness | Proxy features or unrepresentative data affect ranking | C-002, C-003, C-006 | TP-002, TP-003, TP-006 | Impact mapping, data lineage, cohort evaluation and adjudicated results |
| R-002 Validity | Extraction errors or unsupported inferences distort candidate summaries | C-006, C-005 | TP-006, TP-005 | Ground-truth protocol, error analysis, source-linked review and overrides |
| R-003 Privacy | Excessive collection, access or retention | C-003, C-008 | TP-003, TP-008 | Data inventory, purpose assessment, access and deletion evidence |
| R-004 Oversight | Recruiters over-rely on ranking | C-005, C-007 | TP-005, TP-007 | Reviewer training, override logs, challenge route and notices |
| R-005 Transparency | Affected people cannot understand or challenge the system | C-007, C-008 | TP-007, TP-008 | Approved notices, explanations, correction and complaint records |
| R-006 Security | Files or integrations manipulate outputs or expose data | C-009, C-008 | TP-009, TP-008 | Threat model, access tests, incident exercise and protected logs |
| R-007 Third-party/lifecycle | Provider changes behavior or terms without reassessment | C-001, C-010 | TP-001, TP-010 | Vendor due diligence, version history and change records |
| R-008 Drift | Population or job criteria changes degrade outcomes | C-006, C-010 | TP-006, TP-010 | Baselines, monitoring trends, thresholds and revalidation records |

## Exercise decision log
The [decision log](decision-log.csv) records governance decisions a real programme would need to make. Every entry is marked as a proposed exercise decision. No board approval, legal determination, owner acceptance or deployment authorization is represented.

## Synthetic control simulation
The deterministic simulation evaluates a deliberately seeded evidence fixture against ten exercise-specific control rules. It tests whether the runner correctly classifies the supplied fixture. It does **not** test TalentScreen, a model, an organization's actual controls or an actual auditor.

The simulation demonstrates evidence-to-control reasoning: missing ownership remains a finding; incomplete lineage, retention or deletion evidence does not become a pass; a missed seeded material error is treated as a control failure in the exercise; an access test does not substitute for an incident tabletop; and an alert does not prove a pause decision or revalidation occurred.

## Required next evidence before any real assurance conclusion
1. Approved system description, named accountable owner, provider and jurisdiction.
2. Actual data inventory, purpose analysis, lineage, retention and deletion configuration.
3. Documented job-related criteria and a representative, legally appropriate evaluation design.
4. Model/version details, raw evaluation outputs, error analysis and independent adjudication.
5. Observed recruiter workflow, training, override and escalation evidence.
6. Approved notices and applicant correction/challenge process.
7. Threat model, access-control tests, logs and incident tabletop records.
8. Vendor terms, change notification, model version history and exit controls.
9. Monitoring baselines, thresholds, alerts, pause decisions and post-change revalidation.
10. Independent reviewer workpapers and evidence-linked closure of findings.

## Conclusion
This connected case study demonstrates how inventory, impact analysis, risk, control design, testing, evidence collection, remediation and assurance conclusions fit together. The current artifacts establish a **structured design exercise with a deterministic synthetic evidence simulation**. They do not establish implementation, legal compliance, model fairness, operational effectiveness, certification or independent assurance.