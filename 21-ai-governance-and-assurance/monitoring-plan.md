# Evaluation and Monitoring Plan — TalentScreen (fictional)

**Status:** Proposed only. No model, dataset, baseline, telemetry or production environment exists.

| Dimension | Candidate measures | Evidence required |
|---|---|---|
| Extraction validity | Field precision/recall, omissions, unsupported claims | Source-grounded sample |
| Matching validity | Criterion agreement, false positives/negatives | Approved criteria and adjudicated cases |
| Fairness | Error/outcome comparisons across appropriate cohorts | Lawful representative cohort data and statistical plan |
| Robustness | Variation across formats, language and missing data | Stratified challenge set |
| Human oversight | Error detection, correction, override, escalation | Controlled workflow tests and logs |
| Privacy | Minimization, access, retention/deletion exceptions | Data inventory, access logs, deletion tests |
| Security | Access, ingestion, prompt-injection resilience | Authorized security evidence |
| Transparency | Notice completeness and comprehension | Approved notices and user research |
| Drift | Input, missingness, criteria/model and outcome shifts | Versioned telemetry |

## Proposed cadence
Each release: regression suite. Weekly: ingestion failures, access anomalies and missingness. Monthly: sampled quality, overrides, complaints and escalations. Quarterly: risk, cohort outcomes where lawful, vendor/criteria changes. Event-driven: model/provider change, new job family, incident, complaint or credible disparate-impact signal. These are suggestions, not statutory requirements.

## Pause triggers
Define numeric thresholds from baseline evidence and approved impact tolerances. Until then, pause/restrict use for unexplained error increase, credible disparate-impact signal, unsupported candidate attributes, broken source traceability, failed access/deletion control, security incident, missing version provenance or loss of human override. Do not invent thresholds.

**Evidence status:** no measured results, baselines, thresholds or drift data exist. This is a plan, not performance evidence.
