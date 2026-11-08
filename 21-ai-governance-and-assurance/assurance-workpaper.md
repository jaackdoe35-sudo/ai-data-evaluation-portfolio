# Assurance Workpaper — TalentScreen (Fictional Case)

**Status:** self-authored desk-based workpaper; not an independent audit.  
**Scope:** documentation design for a fictional AI-assisted recruitment-screening workflow.  
**Evidence date:** portfolio review date; no production evidence exists.  
**Exclusions:** no real system access, interviews, applicant data, legal opinion, model testing, control implementation testing or operating-effectiveness testing.

## 1. Assurance question

Does the documentation package define a sufficiently clear governance and risk-control approach to justify a future controlled assessment? It does **not** answer whether a real system is safe, fair, lawful or compliant.

## 2. Claim-to-evidence assessment

| Claim | Evidence inspected | Assessment | What remains necessary |
|---|---|---|---|
| System boundary and accountability are defined | system-inventory.csv | Partially documented; owner/provider/model/geography remain unknown | Approved inventory and accountable owner evidence |
| Material impact pathways are identified | impact-assessment.md; risk-register.csv | Design-level hypotheses documented; no impact measurement | System-specific data, stakeholder evidence and validated assessment |
| Risks have owners and treatments | risk-register.csv | Treatments proposed; owners unknown; no acceptance decisions | Named owners, approved treatment plan and review records |
| Controls are adequately designed | control-matrix.csv; control-test-plan.csv | Proposed objectives and test procedures exist; design not independently validated | Design walkthrough and trace to actual workflow |
| Controls are implemented | evidence-register.csv | No implementation evidence | Configurations, records and direct observation |
| Controls operate effectively | evidence-register.csv; control-test-plan.csv | Not tested | Defined population, sample, period, reperformance and exception analysis |
| Security risks are evaluated | risk-register.csv; Project 20 catalogue | Security risks and test specifications documented; no runtime evaluation | Authorized threat model, test traces and remediation validation |
| Monitoring is effective | monitoring plan (design artifact) | Proposed metrics only; no baseline or telemetry | Approved thresholds, operating reports and alert/response evidence |
| Regulatory applicability is established | regulatory-mapping.md | Preliminary issue map only | Confirmed facts, jurisdiction-specific legal review and documented determination |

## 3. Evidence quality criteria

For each evidence item, assess:
- **Relevance:** does it address the control/risk assertion?
- **Attribution:** can the source, owner and creation context be established?
- **Completeness:** is the full record available, including exceptions?
- **Currency:** does it apply to the current system/version and period?
- **Integrity:** is it protected from unauthorized alteration?
- **Independence:** is it corroborated or independently generated where needed?

A self-authored design document can support the claim that a design was documented. It cannot independently prove that the design is approved, implemented or effective.

## 4. Finding severity convention

- **Critical blocker:** prevents a defensible conclusion about system scope, authority or material risk.
- **High:** material risk/control evidence gap that must be resolved before deployment or reliance.
- **Moderate:** important improvement that does not alone prevent the current bounded documentation conclusion.
- **Low:** editorial or administrative issue.

These are workpaper priorities, not formal audit ratings or risk scores.

## 5. Current findings

| ID | Category | Conclusion | Evidence | Priority | Closure evidence |
|---|---|---|---|---|---|
| F-01 | Scope/accountability | No actual owner, provider, model, jurisdiction or deployment boundary is evidenced | system-inventory.csv | Critical blocker | Approved system inventory and accountable owner |
| F-02 | Risk assessment | Risks are plausible hypotheses; likelihood and residual risk are not assessed | risk-register.csv; risk-methodology.md | High | System-specific evidence and approved assessment |
| F-03 | Control design | Control objectives are proposed; design adequacy has not been independently tested | control-matrix.csv; control-test-plan.csv | High | Design walkthrough and documented test results |
| F-04 | Implementation | No evidence demonstrates that any control is implemented | evidence-register.csv | High | Configuration, workflow, contract or operational records |
| F-05 | Operating effectiveness | No population, sample, period or test results exist | control-test-plan.csv | High | Reperformance and exception analysis over defined period |
| F-06 | Model safety/performance | No live model behavior or performance evidence is present | Project 20 execution status | High | Authorized version-specific test run with raw traces |
| F-07 | Legal applicability | Jurisdiction and actual processing facts are unknown | regulatory-mapping.md; impact-assessment.md | High | Qualified jurisdiction-specific legal determination |

## 6. Bounded conclusion

**Conclusion: documentation design exercise completed; system assurance not established.**

The artifacts show a structured approach to inventory, impact pathways, risk hypotheses, control objectives, evidence requests and future test procedures. They do not demonstrate a real deployment, control implementation, operating effectiveness, fairness, model performance, legal compliance or residual-risk acceptability. No assurance opinion is expressed.

## 7. Evidence requests and closure gates

1. Approved system boundary, owner, provider, model/version, intended purpose and jurisdictions.
2. Actual data inventory, lineage, lawful-purpose analysis, retention and vendor terms.
3. Validated risk assessment with accountable owners and documented acceptance authority.
4. Approved control designs mapped to actual workflow components.
5. Implementation evidence for each material control.
6. Operating-effectiveness evidence with defined test period, population, sample and exceptions.
7. Version-specific model evaluation with raw outputs, traces, scoring protocol and independent review.
8. Qualified legal review where regulatory applicability or obligations are in scope.

## 8. Assessor notes

Do not convert any status from proposed/not available/not tested to implemented/effective without new evidence. Preserve the current limitations when presenting this case study to recruiters.
