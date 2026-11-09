# Evidence Judgment and Assurance Findings — TalentScreen

**Case:** GOV-001 TalentScreen (fictional)  
**Assessment date:** 9 November 2026  
**Assessment type:** self-authored, desk-based portfolio exercise with a deterministic synthetic-evidence simulation  
**Status:** no independent assurance opinion; no real system was assessed.

## 1. Scope and evidence reviewed

The review considered the system inventory, impact assessment, risk register and methodology, control matrix, control test plan, evidence register, synthetic evidence fixture, simulation runner/report, connected case study, regulatory map, monitoring and incident-response design artifacts.

No organization, deployed model, applicant data, production environment, control owner, approval record, interview, real operating log or independent reviewer was available. The case is fictional. The synthetic fixture is deliberately seeded training data and must not be represented as evidence from a real organization.

## 2. Assurance questions and evidence levels

The assessment distinguishes five separate questions:

| Evidence level | Question | What can support it | Current TalentScreen position |
|---|---|---|---|
| 1. Documentation | Is a policy, process, control or test described? | Authored document, register, procedure or design | Demonstrated for selected governance topics |
| 2. Design adequacy | Would the proposed design address the stated risk if implemented? | Traceable risk-control rationale, criteria, walkthrough and challenge | Partially reasoned in the artifacts; not independently validated |
| 3. Implementation | Does the control exist in the actual system and organization? | Approved configuration, contract, workflow, access record, named owner, direct observation | Not evidenced; fictional system |
| 4. Operating effectiveness | Did the control operate consistently over a defined period and population? | Complete population, sampling rationale, source records, reperformance, exceptions and period | Not tested; no operating population exists |
| 5. Independent assurance | Has a suitably independent reviewer assessed sufficient reliable evidence? | Independent workpapers, reviewer identity/competence, review trail and conclusion | Not performed; blank review template only |

A test plan is not a test result. A synthetic simulation is not an implementation test. A self-authored document can evidence that documentation was produced, but not that an organization approved or followed it.

## 3. Synthetic simulation — separate from real-world assurance

The deterministic runner evaluates a deliberately seeded JSON fixture against ten exercise-specific control predicates. The fixture contains simulated records and pre-seeded expected outcomes.

| Control | Fixture result | What the simulation demonstrates | What it does not demonstrate |
|---|---|---|---|
| C-001 Accountability | Fail | The evaluator flags an unapproved inventory and missing accountable owner in the fixture | No real inventory or owner was inspected |
| C-002 Impact assessment | Partial | The evaluator detects a missing applicant challenge/correction route | No actual applicant process was assessed |
| C-003 Data governance | Pass | The supplied fixture satisfies the exercise's limited data-governance predicate | No actual data flow, lineage or retention configuration was verified |
| C-004 Risk management | Fail | The evaluator detects incomplete risk ownership and treatment approval in the fixture | No actual risk owner or approval was interviewed or verified |
| C-005 Human oversight | Fail | The fixture records a reviewer missing one of four seeded material errors | No real recruiter or deployed interface was tested |
| C-006 Accuracy/robustness | Fail | The fixture's 91% aggregate accuracy, absent pre-registered thresholds and subgroup results, fails the exercise predicate | The 91% value is synthetic; it is not a model result or benchmark |
| C-007 Transparency/documentation | Pass | The fixture satisfies the exercise's limited documentation predicate | No real notice or user-facing behavior was verified |
| C-008 Logging/traceability | Partial | Four of twenty fixture log records omit model version | No production logs or retention controls were inspected |
| C-009 Security/incident response | Partial | The fixture records 5/5 simulated access attempts blocked but no incident tabletop | No live access test or security control was executed |
| C-010 Monitoring/change | Partial | The fixture records an alert but no pause decision or revalidation | No live telemetry, incident or change process was observed |

**Fixture totals:** 2 Pass, 4 Partial, 4 Fail. These are classifications of the seeded training fixture only. The script's reproducibility shows that the evaluator applies its programmed predicates consistently to that fixture; it does not validate the truth of the fixture or the adequacy of the predicates.

## 4. Evidence-quality assessment

Each evidence item should be judged against the following dimensions:

- **Relevance:** directly supports the control assertion or risk decision.
- **Attribution:** source, creator, owner and creation context are identifiable.
- **Completeness:** full record and relevant exceptions are available.
- **Currency:** applies to the correct system version, period and use context.
- **Integrity:** protected against unauthorized alteration; provenance can be checked.
- **Independence:** corroborated or generated independently where the assertion requires it.
- **Population and sampling:** population is defined, sample selection is justified and results can be reperformed.
- **Traceability:** evidence links to the risk, control, test step, finding and closure condition.

For this exercise, self-authored artifacts have attribution to the portfolio author but are not independent. Synthetic fixture records have known exercise provenance but no real-world source. No evidence item supports an assertion that a TalentScreen control is implemented or operating effectively.

## 5. Findings and priorities

Priority labels below are practical workpaper priorities, not formal audit ratings or measured residual-risk scores.

| ID | Category | Evidence-based conclusion | Evidence pointer | Priority | Closure evidence |
|---|---|---|---|---|---|
| F-01 | Scope and accountability | Actual system boundary, provider, model, jurisdiction and accountable owner are unknown by design | system-inventory.csv; evidence-register.csv | Critical blocker | Approved inventory, intended-use statement, provider/model details, jurisdiction and named owner |
| F-02 | Regulatory applicability | The EU AI Act issue map is conditional; territorial scope, provider/deployer roles and material influence are not established | regulatory-mapping.md; system-inventory.csv | High | Fact-specific legal applicability/classification determination and dated obligations register |
| F-03 | Risk assessment | Eight risk hypotheses are documented, but likelihood, impact magnitude and residual risk are not rated | risk-register.csv; risk-methodology.md | High | System-specific evidence, approved risk criteria, scoring rationale and risk-owner decisions |
| F-04 | Control design | Ten proposed control objectives and test specifications exist; design adequacy has not been independently challenged against an actual workflow | control-matrix.csv; control-test-plan.csv | High | Documented design walkthrough, workflow trace and independent challenge |
| F-05 | Implementation | No real implementation evidence exists; all control statuses remain proposed or unavailable | evidence-register.csv | High | Actual configurations, approvals, contracts, access records and direct observation |
| F-06 | Operating effectiveness | No real population, period, sample or reperformance exists | control-test-plan.csv; evidence-register.csv | High | Defined period/population, sampling rationale, source records, reperformance and exception analysis |
| F-07 | Fairness and validity | No TalentScreen model, dataset, ground truth, subgroup result or measured outcome exists | impact-assessment.md; TP-006 | High | Representative and lawful evaluation design, subgroup analysis, uncertainty, adjudication and documented limitations |
| F-08 | Human oversight | Oversight is a design proposal; no actual recruiter workflow, training, override or escalation evidence exists | human-oversight.md; TP-005 | High | Observed workflow, competence/training records, seeded-error tests and sampled override/escalation records |
| F-09 | Monitoring and incident response | Plans exist but there is no real telemetry, incident tabletop, pause decision or recovery record | monitoring-plan.md; incident-response.md | Moderate/High | Approved metrics and thresholds, actual monitoring records, tabletop results, decision authority and closure |
| F-10 | Independent review | No independent review has been completed; the template is blank | independent-review-template.csv | Moderate | Separate reviewer completes the template, records evidence pointers, disagreements and adjudication |

## 6. Bounded conclusion

**Conclusion: a connected governance documentation design exercise and deterministic synthetic-evidence simulation have been completed. Real-system assurance is not established.**

The portfolio demonstrates the ability to organize a fictional AI use case, identify plausible risk pathways, formulate proposed controls, design tests, classify a seeded evidence fixture, document gaps and specify closure evidence. It does not demonstrate that TalentScreen exists, that a control is implemented or effective, that the system is fair or lawful, that regulatory obligations are met, or that residual risk is acceptable. No assurance opinion is expressed.

## 7. Smallest evidence requests for a real assessment

1. **Scope pack:** approved purpose, system boundary, model/provider/version, deployment geography, data categories and accountable owner.
2. **Decision-process pack:** actual workflow, recruiter authority, affected-person notice, correction/appeal route and human-oversight records.
3. **Data and model pack:** data lineage, retention/deletion settings, representative evaluation protocol, raw outputs, subgroup results and limitations.
4. **Control pack:** approved control design, configuration evidence, named owners and relevant supplier/contract records.
5. **Operating pack:** defined population/period, samples, logs, incidents, monitoring results, overrides, exceptions and revalidation.
6. **Legal and independent review:** qualified jurisdiction-specific legal analysis and a genuinely separate reviewer where required.

## 8. Closure discipline

A finding closes only when the specified evidence is received, its provenance and completeness are checked, the relevant test is performed, exceptions are resolved or formally accepted by an authorized owner, and the closure decision is recorded. A planned action, policy draft or successful synthetic test is not closure evidence.
