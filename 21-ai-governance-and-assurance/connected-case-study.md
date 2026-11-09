# Project 21 — TalentScreen Connected AI Governance Case Study

**Case type:** fictional, self-directed governance and assurance exercise  
**System:** GOV-001 TalentScreen, an assumed AI-assisted recruitment-screening workflow  
**Status:** design artifacts and deterministic synthetic evidence simulation completed  
**Evidence boundary:** no real organization, applicant data, deployed model, production workflow, control owner or independent audit exists.

## Executive summary

This case study asks how an organization should govern an AI-assisted workflow that extracts candidate information and prioritizes a recruiter review queue without allowing a ranking to become an unreviewed employment decision. It connects system inventory, impact assessment, risk analysis, control design, test planning, evidence tracking, synthetic simulation, remediation and an evidence-bounded assurance conclusion.

The work demonstrates governance documentation and traceability. It does not establish implementation, compliance or operating effectiveness.

## Problem and decision context

The hypothetical organization needs to decide whether the proposed use is sufficiently defined and controlled to proceed to a real assessment. The critical governance distinction is between a tool that supports a human review queue and a system that effectively determines access to employment opportunities. The case therefore treats purpose, affected people, job-related criteria, data provenance, human authority, transparency, security and lifecycle change as linked questions.

## Scope and assumptions

The assumed workflow extracts information from applications, compares it with published role criteria and prioritizes a human review queue. Actual system architecture, provider, model, data, jurisdiction, owners and deployment status are deliberately unknown. Unknowns remain explicit; they are not filled with invented organizational facts.

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

## Decision rights and gates

The proposed roles—business sponsor, AI governance lead, HR process owner, privacy/legal reviewer, security lead, model/system owner and independent assurance reviewer—are design roles only. They are not actual appointments or approvals.

The proposed gate sequence is: define purpose and accountable ownership; assess impact and risk; map controls to risks and tests; inspect implementation evidence before assigning operating credit; block positive readiness conclusions while critical questions remain unresolved; reassess material changes; and obtain independent review before making assurance claims.

## Synthetic simulation and observed outcome

The deterministic simulation evaluates a deliberately seeded evidence fixture against ten exercise-specific control rules. It tests whether the runner classifies the supplied fixture as designed. It does not test TalentScreen, a model, an organization's actual controls or an actual auditor.

The simulation illustrates evidence-to-control reasoning: missing ownership remains a finding; incomplete lineage, retention or deletion evidence does not become a pass; a missed seeded material error is treated as a control failure in the exercise; an access test does not substitute for an incident tabletop; and an alert does not prove a pause decision or revalidation occurred.

## Assurance conclusion

The [assurance report](assurance-report.md) expresses no assurance opinion. The artifacts establish a structured design exercise with deterministic synthetic evidence simulation. They do not establish implementation, legal compliance, model fairness, operational effectiveness, certification or independent assurance. Residual risk is not assessed.

## Evidence required before a real assurance conclusion

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
