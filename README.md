# AI Data Annotation & Evaluation Portfolio

**Target roles:** AI Data Annotator · AI Response Evaluator · LLM Evaluator · Annotation Quality Reviewer · Data Quality Analyst · Search Relevance Evaluator

This repository contains self-directed, synthetic work samples demonstrating structured annotation, response evaluation, search relevance judgment, quality checks, and small supporting data-validation tools.

**[Recruiter overview](RECRUITER-OVERVIEW.md)** · **[Documentation, semantic and reference audit](15-semantic-and-reference-audit/README.md)**

## Start here — strongest work samples

| Priority | Work sample | What a reviewer can inspect |
|---|---|---|
| 1 | [End-to-end support annotation case study](09-end-to-end-annotation-case-study/README.md) | Task methodology, detailed taxonomy, 40 annotated messages, ambiguity log, QA report and findings |
| 2 | [AI response evaluation](01-ai-response-evaluation/README.md) | Five-dimension rubric, 30 scored prompt/response examples, evidence rationales and findings |
| 3 | [Text annotation](02-data-annotation/README.md) | Annotation guidelines and 50 synthetic messages labeled by intent and sentiment |
| 4 | [Search relevance evaluation](14-search-relevance-evaluation/README.md) | 20 synthetic query-result cases, intent types, relevance grades and rationales |
| 5 | [Realistic response review](08-realistic-response-review/README.md) | Six scenario-based reviews, five-dimension scores, decision revision and reflection |
| 6 | [Paired-response evaluation](06-paired-response-challenge/README.md) and [advanced blind evaluation](07-advanced-blind-evaluation/README.md) | Comparative judgment, error severity, evidence-based preference and evaluator feedback |

## Supporting QA tools

These are small, rule-based utilities supporting annotation and evaluation workflows. They are not marketed as separate software-development services.

- [Annotation CSV Validator](10-annotation-csv-validator/README.md) — checks schema, required values, duplicate IDs, labels and synthetic PII-token consistency.
- [Annotation Consistency Checker](11-annotation-consistency-checker/README.md) — flags selected cross-record and cross-field patterns for human review.
- [AI Response Score Calculator](12-ai-response-score-calculator/README.md) — recalculates rubric arithmetic and produces a Markdown summary.
- [Annotation QA Dashboard](13-annotation-qa-dashboard/README.md) — summarizes configured annotation distributions and structural/categorical flags.

The tools use Python's standard library. Their tests cover selected behaviors; they do not establish semantic correctness or production readiness.

## Additional practice materials

- [Quality assurance report](03-quality-assurance/quality-assurance-report.md) — structural checks and label distributions for the 50-row annotation sample.
- [Evaluation methodology](05-skills/skills-and-methodology.md) — documented evaluation and annotation workflows.
- [Transcription-formatting example](04-transcription/transcription-sample.md) — constructed text demonstrating speaker labels and uncertainty conventions; **not an audio transcription**.

## Working approach

1. Parse task requirements, schemas and constraints.
2. Identify available evidence and unknowns.
3. Apply the task-specific rubric or annotation taxonomy.
4. Record observable evidence and concise rationales.
5. Flag ambiguity instead of inventing missing information.
6. Validate structure, allowed labels and calculations.
7. Report findings with limitations and reproducible references.

## Evidence boundaries and limitations

All annotation, evaluation and search-relevance examples are synthetic, self-directed practice materials. They are not paid work, employment, client engagements, proprietary production data, or externally sourced benchmark results.

Preference scores are agreement with author-created reference material, not independently validated proficiency scores. The semantic and reference-key audit records corrections and limitations. The end-to-end annotation case study was produced in a single pass and self-audited; it does not establish independent annotator agreement, production throughput, or professional client experience.

The supporting tools are small rule-based demonstrations. Passing tests verifies only the behaviors covered by those tests. No claim of production readiness, independent semantic accuracy, or complex engineering expertise is made.

## Roles this portfolio is designed to support

- AI Data Annotator / Annotation Specialist
- AI Response Evaluator / LLM Evaluator
- AI Trainer / AI Data Reviewer
- Annotation Quality Reviewer
- Data Quality Assurance Analyst
- Search and Content Relevance Evaluator

Actual eligibility depends on each employer's location restrictions, language requirements, assessment, schedule, device requirements and payment arrangements.

## Contact

Use the repository owner's GitHub profile to contact the candidate.
