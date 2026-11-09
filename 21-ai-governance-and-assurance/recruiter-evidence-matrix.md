# AI Safety, Governance & Assurance — Recruiter Evidence Matrix

This matrix maps target entry-level roles to portfolio artifacts and states the evidence boundary. It is a navigation aid, not a claim of employment experience or professional certification.

| Role family | Relevant competencies | Portfolio evidence | Current evidence level | Remaining proof required |
|---|---|---|---|---|
| AI Safety Evaluation Assistant | Test-case design, expected behavior, prompt-injection boundaries, authorization, refusal calibration, evidence capture, result classification | [12-case catalogue](../20-llm-security-evaluation/security-evaluation-cases.json), [execution protocol](../20-llm-security-evaluation/execution-protocol.md), [evaluator rubric](../20-llm-security-evaluation/evaluator-rubric.md) | Test design and scoring method documented; live model behavior not tested | Execute on named model/configuration, preserve raw outputs/traces, repeat stochastic cases, obtain independent scoring/adjudication |
| Junior AI Governance Analyst | System inventory, intended-use boundary, affected stakeholders, lifecycle risk identification, documentation and escalation | [Inventory](system-inventory.csv), [impact assessment](impact-assessment.md), [risk register](risk-register.csv), [risk methodology](risk-methodology.md) | Fictional design exercise; risk hypotheses only; likelihood and residual risk not assessed | Apply to a real, authorized case with evidence, accountable owners and jurisdiction-specific facts |
| Junior AI Risk Analyst | Risk statements, causes/events/impacts, likelihood/impact methodology, treatment ownership, monitoring triggers | [Risk register](risk-register.csv), [risk methodology](risk-methodology.md), [monitoring plan](monitoring-plan.md) | Method and proposed risk treatments documented; no empirically rated risk | Validate assumptions with system evidence; document scoring rationale, treatment decisions and acceptance authority |
| Junior AI Assurance / Controls Analyst | Control objectives, design/implementation/operating distinction, evidence requests, test procedures, findings and closure criteria | [Control matrix](control-matrix.csv), [control test plan](control-test-plan.csv), [evidence register](evidence-register.csv), [assurance workpaper](assurance-workpaper.md) | Desk-based self-authored workpaper; no control implementation or operating-effectiveness testing | Perform authorized walkthroughs, inspect primary evidence, select samples, reperform tests, document exceptions and independent review |
| AI Governance / Assurance Research Assistant | Public-source evidence review, provider-claim scrutiny, framework mapping, control traceability, findings and evidence requests | [GPT-6 Astra public-system review](public-system-review-gpt-6-astra.md) | Primary-source desk review; provider disclosures distinguished from independent evidence; no internal access or control-effectiveness verification | Validate findings through authorized internal evidence, independent evaluation, operating samples and qualified legal review where needed |

## Evidence hierarchy used

- **Test design:** a procedure and expected outcome are specified.
- **Executed observation:** a named target was tested and raw evidence retained.
- **Independent validation:** another evaluator reviewed or repeated the work.
- **Implementation evidence:** a control is shown to exist in the actual environment.
- **Operating-effectiveness evidence:** a control operated consistently across a defined period and sample.
- **Assurance conclusion:** an appropriately scoped reviewer evaluates sufficient reliable evidence.

These levels must not be collapsed. A document can prove that a procedure was written; it cannot prove that the procedure was performed or that a control works.

## Honest candidate positioning

The defensible positioning today is **entry-level AI evaluation and governance/risk documentation with a technical evidence orientation**. The work samples demonstrate structured thinking and the ability to produce organized evaluation artifacts. They do not establish paid AI safety work, professional audit experience, regulatory/legal expertise, production control ownership or independent assurance.

## Interview questions this portfolio should withstand

1. What exact target did you test, on what date and configuration?
2. Show the raw evidence for a reported pass or failure.
3. How did you separate model output from your interpretation?
4. How would you handle evaluator disagreement?
5. Why is a control marked proposed rather than implemented?
6. What evidence would establish operating effectiveness?
7. Why have you not assigned residual risk?
8. What would cause you to pause or escalate the system?
9. Which regulatory conclusions are facts and which require legal review?
10. What limitations prevent your conclusion from being generalized?

A strong candidate should be able to answer each question with a repository pointer, direct evidence or an explicit unknown—not improvisation.
