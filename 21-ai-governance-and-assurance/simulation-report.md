# Synthetic Governance & Assurance Simulation Report

**Case:** TALENTSCREEN-SIM-001  
**Type:** fictional recruitment AI governance simulation  
**Evidence date:** 2026-11-08  
**Status:** reproducible training simulation; not a real audit or assurance opinion.

## Scope and method
The evaluator reads the synthetic evidence fixture and applies explicit control-specific predicates to ten governance controls. The expected outcomes are seeded in the fixture before execution. The script verifies that the deterministic assessment matches those expected outcomes. This tests the consistency of the exercise and evaluator code; it does not independently validate a real control environment.

## Results
Run `python run_assurance_simulation.py` to generate the machine-readable report. Expected exercise outcomes:
- Pass: C-003, C-007
- Partial: C-002, C-008, C-009, C-010
- Fail: C-001, C-004, C-005, C-006
- Not tested: none

## Findings

| ID | Control | Result | Finding | Recommended remediation |
|---|---|---|---|---|
| SIM-F01 | C-001 | Fail | Inventory not approved and no accountable owner assigned | Approve system boundary, name accountable owner and provider, record intended/prohibited use and change authority |
| SIM-F02 | C-002 | Partial | Applicant challenge/correction route missing | Define accessible notice, correction, appeal and escalation route; test with representative scenarios |
| SIM-F03 | C-004 | Fail | Only 2 of 4 material risks have owners; only 2 treatments approved | Assign risk and treatment owners; obtain documented treatment/acceptance decisions; set review triggers |
| SIM-F04 | C-005 | Fail | Reviewer missed 1 of 4 seeded material errors | Investigate error type; revise interface/training; retest with blind seeded cases; set a pre-agreed critical-error threshold |
| SIM-F05 | C-006 | Fail | No pre-registered thresholds or subgroup results; 91% aggregate accuracy alone cannot support acceptance | Freeze representative test set and thresholds before run; report subgroup performance and uncertainty; adjudicate errors |
| SIM-F06 | C-008 | Partial | 4 of 20 log records omit model version | Make model/version a required immutable event field; reject incomplete events; retest traceability |
| SIM-F07 | C-009 | Partial | Access test blocked 5/5 attempts, but no incident tabletop was performed | Conduct tabletop covering detection, containment, escalation, notification decision and recovery; record actions |
| SIM-F08 | C-010 | Partial | Alert received, but pause decision and revalidation are missing | Define decision authority and pause criteria; record response and rerun evaluation before resumption |

## Priority and conclusion
C-001, C-004, C-005 and C-006 are the highest-priority exercise findings because accountability, risk ownership, human oversight and model evaluation evidence are foundational to a defensible recruitment system. No real-world risk severity or legal conclusion is assigned.

**Bounded conclusion:** the synthetic evidence fixture contains four seeded control failures and four partial-control gaps. The evaluator script reproduces the expected classifications. The simulation demonstrates the ability to inspect structured evidence, identify gaps, formulate findings and recommend closure evidence. It does not establish that TalentScreen exists, that any real control was tested, or that the author has conducted a professional audit.

## Required independent review
A second reviewer should independently assess the evidence fixture and findings without seeing the expected results, then record agreement and adjudication using `independent-review-template.csv`. Until completed by a human reviewer, independent assurance is not established.
