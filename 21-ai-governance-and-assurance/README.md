# AI Governance & Assurance — Simulated Recruitment AI Case Study

**Status:** connected design case study with deterministic synthetic-evidence simulation. TalentScreen is fictional. No real organization, model, applicant data, deployed workflow, owner or operating control was assessed.

## Scenario and objective

TalentScreen is an illustrative AI-assisted recruitment-screening workflow. It extracts application information, compares it with published role criteria and prioritizes a human review queue. The exercise demonstrates a documented approach to AI governance, risk and assurance—not a real audit, compliance assessment or certification.

## Work products

- [System inventory](system-inventory.csv) — purpose, inputs, outputs, system boundary and explicit unknowns.
- [Impact assessment](impact-assessment.md) — affected stakeholders, impact pathways and pre-deployment questions.
- [Risk register](risk-register.csv) and [risk methodology](risk-methodology.md) — eight risk hypotheses; likelihood and residual risk remain unassessed without system evidence.
- [Control matrix](control-matrix.csv) — ten proposed control objectives and evidence expectations.
- [Control test plan](control-test-plan.csv) — design, implementation and operating-effectiveness procedures with acceptance criteria.
- [Evidence register](evidence-register.csv) — expected evidence and availability status.
- [Data governance and lineage](data-governance-and-lineage.md), [human oversight](human-oversight.md), [monitoring plan](monitoring-plan.md) and [incident response](incident-response.md).
- [Framework crosswalk](framework-crosswalk.md) — NIST AI RMF 1.0 thematic mapping and limited public-source alignment to ISO/IEC 42001:2023, with evidence status and gaps.
- [Regulatory issue map](regulatory-mapping.md) — conditional EU AI Act recruitment analysis and current consolidated application-date note; not a legal determination.
- [Evidence judgment and findings](evidence-judgment-and-findings.md) — evidence hierarchy, synthetic simulation interpretation, prioritized findings and closure conditions.
- [Assurance report](assurance-report.md) and [assurance workpaper](assurance-workpaper.md) — bounded conclusions; no assurance opinion.
- [Recruiter evidence matrix](recruiter-evidence-matrix.md) — role-to-artifact mapping and evidence limitations.
- [Connected case study](connected-case-study.md) — lifecycle traceability from inventory through assurance.
- [Decision log](decision-log.csv), [remediation tracker](remediation-tracker.csv) and [independent review template](independent-review-template.csv).
- [Synthetic evidence fixture](synthetic-control-evidence.json), [simulation runner](run_assurance_simulation.py) and [simulation report](simulation-report.md).
- [Validator](validator.py) — structural CSV/reference checks only.

## Governance lifecycle

The case connects intake and inventory, impact analysis, risk identification, control design, test planning, evidence collection, deterministic synthetic simulation, remediation and a bounded assurance conclusion. Risk-to-control traceability links R-001–R-008 to C-001–C-010, test procedures and evidence expectations.

## Framework literacy

The crosswalk uses NIST AI RMF 1.0 as a version-stamped voluntary risk-management reference and maps selected governance themes to publicly described ISO/IEC 42001:2023 management-system themes. It does not claim NIST conformance, ISO conformity or certification. A full clause-level ISO assessment would require lawful access to the current standard and a defined organizational scope.

The EU AI Act analysis treats recruitment classification as conditional on actual purpose, influence on selection, profiling, operator roles and territorial scope. It is not a legal opinion and does not decide applicability.

## Assurance approach and evidence discipline

The work separates:
1. documentation;
2. design adequacy;
3. implementation evidence;
4. operating-effectiveness evidence; and
5. independent assurance.

A document demonstrates that a design was written. A test plan is not an executed test. A synthetic fixture tests the evaluator's behavior against seeded records; it is not evidence from a deployed system. No proposed control receives implementation or risk-reduction credit without direct evidence.

## Current conclusion

**Connected governance documentation design exercise completed; real-system assurance not established.** The artifacts demonstrate structured risk/control documentation, framework literacy, evidence evaluation and test planning. They do not establish legal compliance, certification, real deployment, fairness, model performance, operating effectiveness, independent audit experience or acceptable residual risk. No assurance opinion is expressed.

## Reproduction

```bash
python validator.py
python -m unittest discover -s tests -v
python run_assurance_simulation.py
```

These checks validate artifact structure and the deterministic simulation logic. They do not validate a real system or legal interpretation.

## Primary references

- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- ISO/IEC 42001: https://www.iso.org/standard/42001
- EU AI Act consolidated text: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727
- EU AI Act Service Desk: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113

Educational portfolio material only; not legal advice, audit opinion or certification.
