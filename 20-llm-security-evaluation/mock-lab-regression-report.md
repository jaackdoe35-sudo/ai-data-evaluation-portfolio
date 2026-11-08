# Agent Security Lab — Deterministic Tool-Boundary Regression Report

**Evidence type:** executed automated regression tests against deterministic application code.
**Source repository:** [agent-security-lab](https://github.com/jaackdoe35-sudo/agent-security-lab)
**Test revision:** `f60e884fa7bee01dbd715bce74bd5bd149790059`
**CI run:** [GitHub Actions run 42008562037](https://github.com/jaackdoe35-sudo/agent-security-lab/actions/runs/42008562037)
**CI result:** success; regression tests and production build steps completed successfully.

## Scope

The tests exercise the lab's deterministic mock agent and synthetic tool adapter. They do not call Gemini, measure model behavior, or represent a real-world compromise. The application has a separate optional Gemini Interactions API adapter, but no successful provider-backed trace was available for this report.

## Executed regression cases

| Test | Expected result | Test assertion |
|---|---|---|
| Prompt-injected refund in vulnerable mock profile | Simulated action accepted | `outcome == executed` |
| Same injected refund in hardened mock profile | Blocked | `outcome == blocked` |
| Direct synthetic refund tool call in hardened profile | Denied at tool boundary | blocked outcome and explicit security event |
| Synthetic refund tool call in vulnerable profile | Simulated action accepted | executed outcome and `SIMULATED` marker |
| Synthetic CRM export in hardened profile | Denied | blocked outcome |
| Synthetic CRM export in vulnerable profile | Only synthetic `.example.test` records returned | executed outcome and reserved test-domain evidence |
| Unknown tool name | Rejected | blocked outcome |
| Benign order lookup in hardened profile | Allowed | normal outcome and synthetic order result |

## What this demonstrates

- The deterministic mock can reproduce a defined vulnerable-versus-hardened contrast.
- The hardened mock denies privileged synthetic actions at the tool adapter, not merely through model wording.
- Benign order lookup remains available in the hardened profile.
- Unknown tools are rejected.
- Synthetic data is used for the CRM fixture.

## What this does not demonstrate

- It does not show that Gemini followed an injection, refused a request, or selected a tool.
- It does not show a live-model attack success rate, refusal rate or reliability estimate.
- It does not prove production-grade authorization: the hardened tool adapter uses a profile flag and has no real identity/approval system.
- It does not prove that any external action or data disclosure occurred.
- CI success proves the tests and build completed, not that a live API key or provider call works.

## Bounded conclusion

The deterministic sandbox regression suite passed in the cited CI run. This is reproducible evidence of mock-agent and synthetic tool-boundary test coverage. Live LLM safety evaluation remains **unverified** pending raw Gemini-backed runs with exact model metadata, tool traces and independent review.
