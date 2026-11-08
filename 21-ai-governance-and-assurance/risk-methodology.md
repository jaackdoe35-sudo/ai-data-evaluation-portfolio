# Risk Assessment Methodology — TalentScreen Case Study

**Status: proposed method for a fictional case.** No likelihood, residual-risk score or risk acceptance decision is asserted for a real system.

## 1. Scope and unit of analysis

Assess a specific risk scenario for a defined system boundary, use, population, geography, lifecycle stage and decision pathway. The current TalentScreen scenario is fictional and lacks a selected model, dataset, provider, jurisdiction and deployment context. Those unknowns prevent defensible numeric risk ratings.

## 2. Risk statement format

Use: **Because [cause/condition], [event] may occur in [system/process], leading to [impact] for [affected people/assets].**

Separate:
- hazard or failure mode;
- exposure and preconditions;
- affected people/assets;
- consequence;
- existing control (only if evidenced);
- proposed treatment; and
- evidence required to validate the scenario.

Do not present a generic concern as an observed incident.

## 3. Likelihood scale

| Rating | Definition | Evidence expectation |
|---|---|---|
| 1 — Rare | Exceptional under documented conditions | Relevant operating history or strong technical basis |
| 2 — Unlikely | Could occur, but not expected in normal operation | Comparable evidence or tested preventive controls |
| 3 — Possible | Credible under foreseeable conditions | Plausible pathway and supporting evidence |
| 4 — Likely | Expected to occur repeatedly or under common conditions | Relevant frequency data or demonstrated weakness |
| 5 — Almost certain | Recurrent or near-inevitable in the defined context | Direct operating evidence or strong frequency data |

If the evidence cannot support a rating, use **Not assessed**. Do not assign a midpoint merely to complete a spreadsheet.

## 4. Impact scale

Assess impact across separate dimensions before choosing a severity:
- individual rights, access to employment and opportunity;
- physical, psychological, financial or reputational harm;
- privacy and confidentiality;
- legal/regulatory consequences;
- operational disruption;
- security and integrity; and
- scale, duration, reversibility and ability to contest/correct.

| Rating | Definition |
|---|---|
| 1 — Negligible | Minimal, readily reversible inconvenience with no material rights or service impact |
| 2 — Minor | Limited and reversible harm; effective correction is readily available |
| 3 — Moderate | Material individual or operational harm requiring intervention |
| 4 — Major | Serious harm, substantial rights impact, or difficult-to-reverse consequences |
| 5 — Severe | Widespread, severe or effectively irreversible harm, or major rights/safety impact |

Use the highest credible impact dimension where aggregation would otherwise conceal severe harm. Document rationale and affected groups.

## 5. Inherent risk

Only after likelihood and impact have evidence-based values, calculate the 1–25 product as a screening aid. It is not a calibrated probability or regulatory rating.

| Score | Working band |
|---|---|
| 1–4 | Lower |
| 5–9 | Moderate |
| 10–16 | High |
| 17–25 | Very high |

These bands are provisional. They are not an approved organizational risk appetite. Any severe rights-impact scenario requires qualitative escalation regardless of product score.

## 6. Control effectiveness and residual risk

Do not subtract arbitrary points for proposed controls. Evaluate each control separately:
- **Design adequacy:** would the control address the stated cause/pathway if implemented?
- **Implementation:** is there evidence it exists in the actual system?
- **Operating effectiveness:** did it operate consistently over a defined period/sample?
- **Coverage:** does it cover all relevant populations, interfaces and lifecycle changes?
- **Evidence reliability:** is the evidence complete, attributable, current and independently verifiable?

A control marked proposed has no demonstrated risk-reduction credit. Residual risk remains **Not assessed** until implementation and operating evidence exist and the risk is reassessed.

## 7. Risk ownership and acceptance

Each material risk needs:
- accountable risk owner;
- treatment owner;
- target date;
- decision authority;
- acceptance rationale and scope;
- review trigger; and
- evidence of approval.

In this fictional exercise, roles are placeholders. No person or organization has accepted risk.

## 8. Review triggers

Reassess after:
- model/provider/version change;
- change to role criteria, features, data sources or thresholds;
- material change in applicant population or geography;
- adverse outcome, complaint or incident;
- drift or performance/fairness threshold breach;
- vendor/subprocessor or retention change; and
- change in applicable law or regulatory guidance.

## 9. Current assessment limitation

All eight existing register entries are risk hypotheses. Likelihood is not assessed; impact descriptions are qualitative; risk owners are unknown; proposed controls are not implemented; residual risk is not assessed. This is the correct status until system-specific evidence exists.
