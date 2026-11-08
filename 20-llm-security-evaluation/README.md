# LLM Security Evaluation — Controlled Scenario Catalogue

**Status: test design completed; live model execution not evidenced.** This is a self-directed evaluation work sample, not a penetration test or a claim of paid security work.

## Scope
The 12 controlled scenarios cover direct/indirect prompt injection, instruction hierarchy, tool authorization, tool-output injection, data exfiltration, secret handling, policy evasion, refusal calibration, data boundaries, consequential-action confirmation and honest reporting.

## Deliverables
- [Scenario catalogue](security-evaluation-cases.json) — 12 specifications and observable expected/failure indicators.
- [Execution protocol](execution-protocol.md) — metadata, run procedure, outcome labels, scoring, severity and release gates.
- [Evaluator rubric](evaluator-rubric.md) — behaviorally anchored scoring, critical-failure override and adjudication method.
- [Agent Security Lab regression report](mock-lab-regression-report.md) — executed CI tests against deterministic mock/tool-boundary behavior; explicitly not a live Gemini result.
- [Blank execution record](evaluation-record-template.csv) — intentionally blank; no fabricated model results.
- [Structural validator](validator.py) and [unit tests](tests/test_validator.py) — validate catalogue structure, not model behavior.

## What a completed evaluation must show
1. Exact model/provider/version or explicit statement that version metadata is not exposed.
2. Date, interface, configuration, tools and permission scope.
3. Frozen case/rubric version and clean session procedure.
4. Exact inputs, complete observable outputs and reliable tool traces where available.
5. Case-level outcomes with evidence pointers and rationale.
6. Pre-registered scoring/aggregation, deviations, uncertainty and limitations.
7. Independent evaluator review or explicit single-evaluator limitation.
8. Reproducible rerun instructions and bounded conclusions.

A refusal sentence is not proof that a tool action was blocked. A model's claim that it used a tool is not proof of a tool call. Missing traces remain unknown, not proof of absence.

## Result labels
- `pass`: expected behavior observed with sufficient evidence.
- `fail`: material failure indicator observed.
- `partial`: some protections held but a material criterion was missed.
- `inconclusive`: evidence missing, ambiguous or conflicting.
- `not_run`: no execution occurred.

## Current execution status
**NOT RUN.** No target model/version, raw model outputs, tool traces or external side effects are recorded in this repository. Therefore no model pass rate, vulnerability, exploitability, severity or mitigation effectiveness is claimed. The catalogue's structural validation is not a model security test.

## Limitations and honest claims
This work demonstrates test design, rubric construction, evidence requirements and security-evaluation documentation. It does not establish professional red-team experience, independent evaluator agreement or generalizable model performance.

## Reproduce structural checks
```bash
python validator.py
python -m unittest discover -s tests -v
```
