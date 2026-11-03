# Annotation QA Scale-Test Results

**Result:** PASS  
**Workflow run:** [41640720649](https://github.com/jaackdoe35-sudo/ai-data-evaluation-portfolio/actions/runs/41640720649)  
**Test commit:** `3737b06029bbc9c3a4c40af08b2634c78512a0e3`  
**Artifact:** `annotation-qa-scale-test-results` (workflow artifact ID `13232133471`)

## Scope and environment

Four existing rule-based utilities were exercised against deterministic synthetic datasets of 10,000, 50,000 and 100,000 rows:

- Annotation CSV Validator
- Annotation Consistency Checker
- Annotation QA Dashboard
- AI Response Score Calculator

The run used CPython 3.15.1 on a GitHub-hosted Ubuntu runner (`Linux-7.0.0-1017-azure-x86_64-with-glibc2.39`). The workloads ran sequentially.

## Measured results

Elapsed time is wall-clock time for the measured Python operation. Memory is peak Python allocation tracked by `tracemalloc`, converted to MiB.

| Utility | 10k rows (s) | 10k peak (MiB) | 50k rows (s) | 50k peak (MiB) | 100k rows (s) | 100k peak (MiB) |
|---|---:|---:|---:|---:|---:|---:|
| CSV Validator | 0.2212 | 8.262 | 0.9135 | 39.992 | 1.8484 | 80.767 |
| Consistency Checker | 0.2317 | 10.479 | 1.2058 | 52.972 | 2.6857 | 106.018 |
| QA Dashboard | 0.1306 | 7.898 | 0.7019 | 40.243 | 1.4371 | 80.268 |
| Score Calculator | 0.5977 | 7.744 | 2.9794 | 40.138 | 6.1846 | 79.920 |

## Checks observed

The uploaded JSON result reported `PASS`. All four utilities processed the expected row counts and reported no unexpected findings. The deterministic generator reproduced identical input files; the tools left the measured input files unchanged. Four negative checks passed:

- Validator rejects duplicate headers.
- Validator reports undecodable input.
- Consistency checker reports missing required columns.
- Dashboard rejects duplicate headers.

## Interpretation

For these generated workloads on this runner, elapsed time and tracked Python allocations increased approximately in proportion to dataset size. At 100,000 rows, the consistency checker had the highest tracked peak allocation (106.018 MiB), while the score calculator had the longest measured operation (6.1846 seconds).

These figures describe only this run and environment. `tracemalloc` does **not** measure process RSS, native allocations or total system memory. The tools load rows into memory; this test does not demonstrate streaming or bounded-memory behavior. Sequential runs do not test concurrency, sustained throughput, soak behavior, deployment conditions or service-level reliability.

## Evidence boundary

This is a reproducible synthetic scale test of the current implementations, not a production certification, client-data test, independent semantic-accuracy assessment or proof of production readiness. The consistency checker detects only its configured patterns. A clean result does not establish that the underlying annotations are semantically correct.

