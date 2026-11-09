# Project 20 — Reproducible Repeated-Trial Protocol

**Current evidence status:** limited preliminary anonymous free-model demonstration documented separately (seven scenarios, two trials each). The 12-scenario catalogue has not completed this protocol. The full raw provider-response export is not committed; dynamic routing and absent independent human adjudication limit conclusions.

## Objective
Produce auditable, case-level observations for all 12 scenarios without conflating model behavior, application authorization, tool enforcement or evaluator interpretation.

## Minimum repeat design
- Freeze the scenario catalogue, rubric, harness commit and tool simulator before execution.
- Execute **10 independent trials per scenario** (120 planned case-level trials).
- Pin the provider and exact model version for the primary run. If the provider does not expose a stable version, record that limitation and treat model identity as uncontrolled.
- Randomize case order within each trial block; do not change prompts or expected outcomes mid-run.
- Use a fresh conversation/session for each trial unless the scenario explicitly tests multi-turn state.
- Run vulnerable and hardened configurations as separate arms; do not treat hardened-profile results as evidence about the underlying model alone.
- Record tool invocation and tool-side effect from the harness trace, not from the model's narrative claim.
- Preserve every request, response, tool event, timestamp, provider request ID, harness version and error.
- Have a second human evaluator independently adjudicate all critical cases and a predeclared sample of the remainder. An LLM self-review is not independent adjudication.

## Required raw record per trial
1. Unique run ID, scenario ID, trial number, arm and UTC start/end timestamps.
2. Provider, exact model/version, routing metadata, region if exposed, API/harness version and relevant parameters.
3. Exact input prompt and conversation context, with secrets redacted before storage.
4. Raw provider response and cryptographic SHA-256 digest.
5. Full ordered tool-call trace, including arguments, authorization decision, tool result and observed side effect.
6. Result classification (`pass`, `fail`, `partial`, `inconclusive`, `not_run`) and rubric scores.
7. Evidence file references, evaluator ID, confidence and rationale.
8. Protocol deviations, retries, timeouts, provider errors and any excluded run with reason.

## Analysis
Report the denominator for every metric. Provide per-scenario counts and observed proportions, exact binomial confidence intervals where appropriate, and a clear statement that small samples remain imprecise. Separate model response behavior, harness/policy authorization decision, tool execution and independent evaluator judgment.

Do not claim an authorization bypass merely because a model proposed an action. Do not claim safety merely because the model refused in prose. A refusal is not proof that the tool was blocked; a blocked tool call is not proof that the model's reasoning was safe.

## Release gate
A scenario is eligible for a behavioral conclusion only when all ten planned trials have complete raw records or documented exclusions; model identity and routing limitations are explicit; tool traces and side effects are observable; evaluator rubric and adjudication are recorded; and no unexplained missing trials or post-hoc prompt changes remain.

If these conditions are not met, label the scenario `preliminary` or `inconclusive`. Never fill missing raw records with reconstructed or synthetic responses.

## Current execution status
The new `repeated-trial-ledger.csv` contains 120 planned rows marked `not_run`. It is a work queue, not evidence of completed execution. This repository change does not execute a remote model or manufacture results.