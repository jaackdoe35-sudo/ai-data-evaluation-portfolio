# Assurance Review — TalentScreen (fictional)

**Review type:** Desk-based review of self-authored design artifacts · **Status:** Not independent assurance.

## Objective
Assess whether the documentation package identifies major governance topics, distinguishes proposed controls from operating evidence and states limitations. References: NIST AI RMF concepts, ISO/IEC 42001 and relevant EU AI Act provisions. Not a formal audit against a standard or law.

## Procedures and limitations
Reviewed inventory, risk register and control matrix; prepared impact, lineage, oversight, monitoring, incident and preliminary regulatory artifacts. Checked evidence boundaries. No system access, interviews, sample tests, model evaluation, document authentication, legal opinion or independent review occurred.

## Findings
| Ref | Observation | Evidence status | Priority | Next step |
|---|---|---|---|---|
| A-01 | No actual owner, provider, model or deployment context | Unknown by design | Critical blocker | Define system boundary and accountable owners |
| A-02 | No source data, lawful basis, lineage, retention or vendor terms | Not available | High | Complete data inventory, privacy and vendor review |
| A-03 | Fairness/validity risks have no dataset or measured results | Hypotheses only | High | Approve representative evaluation protocol |
| A-04 | Human oversight has no workflow or reviewer evidence | Not tested | High | Implement and test source-linked review and override |
| A-05 | Controls are proposed; operating evidence is absent | Not available | High | Assign owners, implement and collect evidence |
| A-06 | Regulatory mapping depends on jurisdiction and actual purpose | Preliminary | High | Obtain qualified legal review |
| A-07 | Monitoring baselines and thresholds are absent | Not available | Medium/High | Define validated thresholds and pause authority |
| A-08 | Incident procedure has not been exercised | Not tested | Medium/High | Run tabletop and track corrective actions |

## Conclusion
**No assurance opinion is expressed.** The artifacts are an initial self-authored governance design exercise. They do not establish that TalentScreen exists, is lawful, safe, fair, secure or compliant, or that controls are effective. All controls remain unimplemented and untested; residual risk is not assessed.

## Remediation order
1. Define system, purpose, jurisdictions and accountable roles.
2. Complete legal, privacy and rights-impact assessment.
3. Document actual data lineage, retention, vendor and security architecture.
4. Approve evaluation methodology, ground truth and acceptance criteria.
5. Implement/test human oversight, access, traceability and incident handling.
6. Establish monitoring, change governance and stop conditions.
7. Obtain independent review before any assurance claim.

This is not an audit opinion, certification, legal review or operating-effectiveness test.
