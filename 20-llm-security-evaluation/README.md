# LLM Security Evaluation — Controlled Scenario Catalogue

## Purpose

This case study extends the portfolio's annotation, response-evaluation and QA methods into **security-focused LLM evaluation**. It defines a repeatable set of controlled scenarios, expected safe behavior, observable failure indicators and a recording protocol.

It is a self-directed practice artefact. It is not a penetration test, a claim that a live model was compromised, or evidence of paid security work.

## Scope

The 12 scenarios cover:

- Direct and indirect prompt injection
- Instruction hierarchy and untrusted-data boundaries
- Tool authorization and tool-output injection
- Data exfiltration and secret handling
- Policy evasion and refusal consistency
- Confirmation boundaries for consequential actions
- Honest reporting when a test has not been run

All examples are designed for controlled evaluation. They do not include real credentials, private data, live targets or destructive actions.

## Files

- `security-evaluation-cases.json` — 12 scenario specifications, expected behavior and failure/success indicators.
- `evaluation-record-template.csv` — blank template for recording actual model runs. Blank fields are intentional; no execution results are fabricated.
- `validator.py` — standard-library structural validator for the scenario catalogue.
- `tests/test_validator.py` — unit tests for catalogue validation.

## Evaluation procedure

1. Select a model and record its exact name, version/build, interface and test date.
2. Record relevant system/developer instructions and available tools when the environment permits. Do not include secrets in the report.
3. Run each scenario in an isolated, authorized test environment. Reset conversation state between cases unless the test explicitly examines multi-turn behavior.
4. Capture the exact input and observable output. Record tool calls and side effects only when the environment exposes reliable traces.
5. Compare observed behavior with the expected behavior and indicators. Do not score based on intent, speculation or a model's self-description.
6. Mark each test `pass`, `fail`, `partial`, `not_run` or `inconclusive`. Link evidence for every pass/fail.
7. Record limitations, severity rationale and a practical mitigation. Avoid declaring a vulnerability without a demonstrated attack path and impact.

## Result labels

| Label | Meaning |
|---|---|
| `pass` | Observed behavior met the stated expected behavior; evidence is recorded. |
| `fail` | An observable failure indicator occurred; evidence and impact are recorded. |
| `partial` | Some expected protections held, but a material gap remained. |
| `not_run` | The scenario has not been executed. |
| `inconclusive` | Evidence is insufficient or conflicting. |

A test specification passing the Python validator means only that its structure meets the configured schema. It does **not** mean a model passed a security test.

## Current execution status

**NOT RUN — no live model has been evaluated as part of this case study.** The catalogue and its structural validator are the completed deliverables. Model behavior, tool authorization, exploitability, severity and mitigation effectiveness remain unverified until an authorized runtime evaluation is performed.

## Limitations

- No target model/version was selected or executed.
- No model outputs, tool-call traces or external side effects were collected.
- No vulnerability, exploitability or security-control effectiveness is claimed.
- The risk labels are scenario-planning priorities, not CVSS scores or measured severity.
- The validator checks catalogue structure only; it cannot judge semantic correctness or model behavior.
- A single evaluator's observations would not establish independent agreement or generalizable model performance.

## What this demonstrates

This work sample demonstrates the ability to define security evaluation criteria, distinguish trusted instructions from untrusted content, identify observable failure conditions, preserve evidence boundaries, structure results and validate evaluation data. It does not establish professional red-team experience.

## Reproduce the structural checks

From this directory:

```bash
python validator.py
python -m unittest discover -s tests -v
```
