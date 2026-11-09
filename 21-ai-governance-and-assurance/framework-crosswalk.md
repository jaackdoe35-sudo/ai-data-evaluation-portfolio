# Framework Crosswalk — TalentScreen AI Governance Case Study

**Assessment date:** 9 November 2026  
**Case:** GOV-001 TalentScreen, a fictional AI-assisted recruitment-screening workflow  
**Mapping status:** desk-based, evidence-scoped thematic mapping. This is not certification, conformity assessment, legal advice or an independent audit.

## 1. Purpose and mapping method

This crosswalk connects the existing inventory, impact assessment, risk register, control matrix, test plan, evidence register, monitoring plan and assurance workpaper to publicly accessible framework material.

A framework reference is not proof that a requirement is satisfied. Each row therefore distinguishes:
- **Artifact coverage:** whether the portfolio contains a document or proposed procedure addressing the topic.
- **Evidence status:** what the artifact actually proves in this fictional exercise.
- **Next evidence:** what a real organization would need to produce before implementation or effectiveness could be concluded.

The mapping is selective and risk-based. It does not claim that every framework outcome is covered.

## 2. NIST AI Risk Management Framework (AI RMF) 1.0

**Version note:** This mapping uses NIST AI RMF 1.0 (2023). NIST states that AI RMF 1.0 is being updated and a revised version is in progress. Recheck the framework before using this crosswalk for a live engagement. The AI RMF and Playbook are voluntary resources; they are not a certification checklist.

| NIST reference | Relevant outcome (short description) | TalentScreen artifacts | Current evidence judgment | Gap / next evidence |
|---|---|---|---|---|
| GOVERN 1.1 | Understand, manage and document AI-related legal/regulatory requirements | regulatory-mapping.md; impact-assessment.md | Preliminary issue map only; jurisdiction and actor roles unknown | Confirm territorial scope, provider/deployer roles, employment and data-protection law with qualified counsel; maintain a dated obligations register |
| GOVERN 1.4–1.6 | Risk policies, periodic review/roles, AI-system inventory | system-inventory.csv; risk-methodology.md; monitoring-plan.md; decision-log.csv | Inventory and governance process are designed; no approval, named owner or operating review | Approved inventory, accountable owner, risk appetite, review cadence and decommissioning authority |
| GOVERN 2.1–2.3 | Accountability, communication, training and leadership responsibility | connected-case-study.md; human-oversight.md; decision-log.csv | Roles are proposed role descriptions, not appointments; training is not evidenced | Named role holders, RACI/decision rights, training completion and leadership risk decisions |
| GOVERN 3.2 | Define human-AI roles and oversight | human-oversight.md; C-005; TP-005 | Oversight is a design requirement; no live workflow or reviewer test | Workflow walkthrough, reviewer competence evidence, override/escalation logs and observed challenge tests |
| GOVERN 4.2–4.3 | Document impacts; enable testing and incident learning | impact-assessment.md; risk-register.csv; incident-response.md; Project 20 security catalogue | Risks and test plans are documented; no TalentScreen incident or production test | Actual incident process, test records, escalation outcomes and lessons learned |
| GOVERN 5.1–5.2 | Obtain and integrate feedback from affected/external actors | impact-assessment.md; human-oversight.md | Stakeholder groups are identified conceptually; no engagement occurred | Applicant/user consultation, accessible feedback route, adjudication and evidence of design changes |
| GOVERN 6.1–6.2 | Manage third-party AI, software, data and supply-chain risks | system-inventory.csv; risk-register.csv; vendor/change controls in C-001/C-010 | Provider and third-party dependencies are unknown | Vendor inventory, due diligence, contractual controls, change notification and contingency evidence |
| MAP 1.1, 1.5–1.6 | Define intended purpose, context, risk tolerance and system requirements | system-inventory.csv; connected-case-study.md; risk-methodology.md | Intended workflow is described; geography, risk tolerance and technical facts remain unknown | Approved use statement, jurisdiction, non-goals, requirements and risk acceptance criteria |
| MAP 2.1–2.3 | Describe tasks/methods, knowledge limits, oversight and TEVV considerations | system-inventory.csv; impact-assessment.md; control-test-plan.csv | High-level workflow only; no model, architecture, test set or technical limitations | Model/system documentation, capability limits, representative evaluation design and validation evidence |
| MAP 3.2–3.5 | Consider costs, scope, operator proficiency and human oversight | impact-assessment.md; human-oversight.md; control-test-plan.csv | Risks and proposed oversight are documented; no cost/benefit evidence or operator proficiency evidence | Context-specific impact evidence, trained reviewers, documented authority and oversight tests |
| MAP 4.1–4.2 | Map third-party components, legal risks and internal controls | system-inventory.csv; risk-register.csv; C-001/C-009 | Dependency mapping is proposed; components/providers are unknown | Component/data-flow inventory, supplier terms, security and IP review |
| MAP 5.1–5.2 | Characterize impact likelihood/magnitude and engage relevant actors | impact-assessment.md; risk-register.csv | Impact pathways are hypotheses; likelihood and magnitude deliberately not rated | Evidence-backed impact assessment, affected-person engagement and documented rationale |
| MEASURE 1.1–1.3 | Select risk metrics; assess controls; use independent expertise where appropriate | control-test-plan.csv; evidence-register.csv; independent-review-template.csv | Test specifications exist; no real measurements or independent review | Pre-registered metrics/thresholds, actual samples, raw outputs, exception analysis and independent challenge |
| MEASURE 2.1–2.5 | Document test sets/tools; measure performance; establish validity/reliability and limits | TP-006; Project 01 and Project 20 are separate evaluation practice artifacts | No TalentScreen model/test set/results. Other projects are not evidence about this fictional system | Versioned representative test set, ground truth, subgroup analysis, uncertainty, adjudication and deployment-context validation |
| MEASURE 2.6–2.11 | Evaluate safety, security, transparency, privacy, fairness and bias | impact-assessment.md; C-003/C-005/C-006/C-007/C-008/C-009 | Risks and control ideas are documented; no system-specific measurement | Actual privacy/security/fairness evaluations, evidence of notice and oversight, model/system performance and limitations |
| MEASURE 3.1–3.3 | Track emerging risks and enable feedback/appeals | monitoring-plan.md; human-oversight.md; incident-response.md | Monitoring and appeal processes are proposals; no telemetry or appeal records | Baselines, live trend reports, applicant appeal records, risk escalation and follow-up |
| MANAGE 1.1–1.4 | Decide whether to proceed; prioritize/treat risks; document residual risk | risk-register.csv; risk-methodology.md; remediation-tracker.csv; assurance-workpaper.md | No real risk rating, risk acceptance or residual-risk conclusion | Validated likelihood/impact, approved treatment owners, acceptance authority and residual-risk rationale |
| MANAGE 2.3–2.4 | Respond to unknown risks; stop, supersede or deactivate unsafe systems | incident-response.md; monitoring-plan.md; C-010 | Pause/deactivation is proposed, not implemented or exercised | Named stop authority, triggers, tested response and restart criteria |
| MANAGE 3.1–3.2 | Monitor third-party risks and pre-trained models | risk-register.csv; C-001/C-010 | No vendor/model/version evidence | Supplier/model inventory, change monitoring and revalidation |
| MANAGE 4.1–4.3 | Implement monitoring, appeals, incident response, recovery and continual improvement | monitoring-plan.md; incident-response.md; remediation-tracker.csv | Lifecycle plans exist as design artifacts; no operating records | Implemented telemetry, response tickets, recovery tests, closure evidence and periodic review |

### NIST mapping conclusion

The strongest coverage is **documented design** across GOVERN, MAP and planned MANAGE activities. MEASURE is primarily a test plan, not measured TalentScreen performance. No NIST outcome is claimed as implemented or achieved by a real organization. The crosswalk is a navigation and gap-analysis aid, not a conformance score.

## 3. ISO/IEC 42001:2023 — thematic alignment only

ISO describes ISO/IEC 42001:2023 as requirements for establishing, implementing, maintaining and continually improving an AI management system (AIMS). The full standard is a paid, copyrighted publication. This portfolio mapping uses only the public ISO overview and does **not** reproduce the standard, claim clause-level coverage or assert conformity.

| Publicly described AIMS theme | Related TalentScreen artifacts | Current evidence judgment | What would be needed in an organization |
|---|---|---|---|
| Organizational context, interested parties and scope | system-inventory.csv; impact-assessment.md | Fictional context and stakeholders described; no real organizational context or approved scope | Approved AIMS scope, organizational context, interested-party needs and system boundaries |
| Leadership, policy, roles and accountability | decision-log.csv; connected-case-study.md; C-001 | Proposed roles and decisions only | Approved AI policy, leadership sponsorship, named responsibilities and authority |
| AI risk/opportunity planning and treatment | risk-register.csv; risk-methodology.md; remediation-tracker.csv | Risk hypotheses and proposed treatments; no accepted risk assessment | Organization-approved risk criteria, assessment records, treatment plan and risk acceptance |
| Resources, competence and documented information | evidence-register.csv; human-oversight.md; independent-review-template.csv | Evidence expectations and role descriptions exist; no personnel competence or controlled records | Competence records, document control, training and resourcing |
| Operational lifecycle and third-party controls | data-governance-and-lineage.md; monitoring-plan.md; incident-response.md | Proposed procedures only; no real operations or supplier evidence | Implemented lifecycle procedures, supplier controls, change records and operational evidence |
| Performance evaluation, internal review and continual improvement | control-test-plan.csv; assurance-workpaper.md; simulation-report.md; remediation-tracker.csv | Desk-based assessment and synthetic simulation only; no AIMS audit or management review | Actual performance measures, internal audit, management review, corrective action and verified closure |

**ISO conclusion:** The project demonstrates familiarity with several AI management-system themes. It does not establish that an AIMS exists, that ISO/IEC 42001 requirements are met, or that the system or organization is certified. A formal clause-by-clause crosswalk requires lawful access to the current standard text and a defined organizational scope.

## 4. Cross-framework traceability

The practical trace is:

1. **Context and impact:** system inventory and impact assessment.
2. **Risk analysis:** risk register and risk methodology.
3. **Treatment design:** control matrix and remediation tracker.
4. **Measurement plan:** control test plan and evidence register.
5. **Operational governance design:** human oversight, data governance, monitoring and incident response.
6. **Evidence judgment:** assurance workpaper and simulation report.
7. **Improvement:** remediation closure criteria and reassessment triggers.

The same artifact may support more than one framework outcome. This is thematic alignment, not a claim that frameworks are interchangeable.

## 5. Sources and version control

- NIST AI RMF 1.0 and revision status: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF Core (official AIRC): https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- NIST AI RMF Playbook: https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook
- ISO/IEC 42001:2023 official overview: https://www.iso.org/standard/42001
- EU AI Act regulatory issues are treated separately in [regulatory-mapping.md](regulatory-mapping.md).

**Refresh rule:** Recheck NIST revision status, the current ISO edition and any applicable law before using this mapping outside this educational case study. Record the source version and review date in any future update.
