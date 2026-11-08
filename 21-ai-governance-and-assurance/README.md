# AI Governance & Assurance — Simulated Recruitment AI Case Study

**Status: DESIGN ONLY.** TalentScreen is fictional. No real organization, model, applicant data, deployed workflow, owner or operating control was assessed.

## Use case
TalentScreen is an illustrative AI-assisted recruitment screening system. It extracts application information, compares it with published role criteria and prioritizes a human review queue. The assumed recruiter decision authority is a design requirement, not evidence of actual oversight.

## Work products
- [System inventory](system-inventory.csv): purpose, users, data, outputs, ownership and unknowns.
- [Risk register](risk-register.csv): eight qualitative risk hypotheses and proposed treatments.
- [Control matrix](control-matrix.csv): ten proposed control objectives, framework references, design/operating evidence and test procedures.
- [Impact assessment](impact-assessment.md): affected stakeholders, impact pathways, proportionality and open questions.
- [Data governance and lineage](data-governance-and-lineage.md): conceptual data flow, provenance, quality, access and retention.
- [Human oversight](human-oversight.md): source-linked review, correction, override and escalation design.
- [Monitoring plan](monitoring-plan.md): proposed metrics, cadence and pause triggers.
- [Incident response](incident-response.md): draft triage, containment, escalation and recovery playbook.
- [Regulatory mapping](regulatory-mapping.md): preliminary NIST AI RMF, ISO/IEC 42001 and EU AI Act issue map.
- [Assurance report](assurance-report.md): desk-based review, evidence gaps and remediation priorities.
- [Evidence register](evidence-register.csv): expected evidence and current availability.
- [Validator](validator.py): structural CSV and reference checks only.

## Framework boundaries
NIST AI RMF 1.0 (Govern, Map, Measure, Manage), ISO/IEC 42001, EU AI Act Regulation (EU) 2024/1689 and the IAPP AI Governance Skills Framework are used as reference points, not certifications. Recruitment use raises an EU AI Act Annex III, point 4(a) classification question; applicability and any exception require fact-specific legal analysis. This project does not make a legal determination.

## Evidence vocabulary
**Observed** means direct evidence was inspected. **Documented** means an artifact describes a process. **Proposed** means not implemented. **Not available** means evidence is absent. **Not tested** means no effectiveness test occurred. **Unknown** remains unresolved. Documentation does not prove implementation.

## Current conclusion
The package is a self-authored documentation exercise. It does not establish legal compliance, certification, real deployment, fairness, model performance, operating effectiveness or audit experience. All controls remain proposed; residual risk is not assessed.

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
