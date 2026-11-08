# AI Governance & Assurance — Simulated Recruitment AI Case Study

**Status: DESIGN ONLY.** TalentScreen is fictional. No real organization, model, applicant data, deployed workflow, owner or operating control was assessed.

## Scenario
TalentScreen is an illustrative AI-assisted recruitment screening system. It extracts application information, compares it with published role criteria and prioritizes a human review queue. The assumed recruiter decision authority is a design requirement, not evidence of actual oversight.

## Work products
- [System inventory](system-inventory.csv) — purpose, inputs, outputs, owner/provider unknowns and system boundary.
- [Impact assessment](impact-assessment.md) — stakeholders, impact pathways, unknowns and pre-deployment requirements.
- [Risk register](risk-register.csv) — eight risk hypotheses; likelihood and residual risk are deliberately not rated without evidence.
- [Risk methodology](risk-methodology.md) — likelihood/impact definitions, scoring discipline, control credit and acceptance rules.
- [Control matrix](control-matrix.csv) — ten proposed control objectives, evidence expectations and test procedures.
- [Control test plan](control-test-plan.csv) — design, implementation and operating-effectiveness test steps with acceptance criteria.
- [Evidence register](evidence-register.csv) — expected evidence and actual availability status.
- [Data governance and lineage](data-governance-and-lineage.md), [human oversight](human-oversight.md), [monitoring plan](monitoring-plan.md) and [incident response](incident-response.md).
- [Regulatory mapping](regulatory-mapping.md) — preliminary issue map, not a legal determination.
- [Assurance report](assurance-report.md) and [assurance workpaper](assurance-workpaper.md) — bounded findings, evidence quality and closure requirements.
- [Recruiter evidence matrix](recruiter-evidence-matrix.md) — role-to-artifact mapping and explicit evidence gaps.
- [Validator](validator.py) — structural CSV/reference checks only.

## Assurance approach
The workpaper separates:
1. documented design;
2. design adequacy;
3. implementation evidence;
4. operating-effectiveness evidence; and
5. independent assurance.

These are different evidence levels. A proposed control receives no risk-reduction credit. No control is described as implemented or effective without direct evidence. No residual risk is rated until controls and context are evidenced.

## Framework references and boundaries
NIST AI RMF 1.0, ISO/IEC 42001, EU AI Act Regulation (EU) 2024/1689 and the IAPP AI Governance Skills Framework are reference points, not certifications. Recruitment use raises an EU AI Act Annex III, point 4(a) classification question; applicability and any exception require fact-specific legal analysis. This project does not make a legal determination.

## Current conclusion
**Documentation design exercise completed; system assurance not established.** The artifacts demonstrate a structured way to identify governance topics, formulate risk hypotheses, design controls, specify tests and track evidence gaps. They do not establish legal compliance, certification, real deployment, fairness, model performance, operating effectiveness, audit experience or acceptable residual risk. No assurance opinion is expressed.

## Reproduction
```bash
python validator.py
python -m unittest discover -s tests -v
```
The validator checks structure and cross-references, not legal interpretation or control effectiveness.

## Primary references
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- EU AI Act consolidated text: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- EU AI Act implementation timeline: https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline
- ISO/IEC 42001: https://www.iso.org/standard/42001
- IAPP AI Governance Skills Framework: https://iapp.org/resources/article/ai-governance-skills-framework/

Educational portfolio material only; not legal advice, audit opinion or certification.
