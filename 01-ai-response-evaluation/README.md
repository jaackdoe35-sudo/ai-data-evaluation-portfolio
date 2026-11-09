# Project 01 — AI Response Evaluation

**Work type:** self-directed rubric application  
**Status:** completed practice sample  
**Evaluation unit:** 30 synthetic prompt/response pairs  
**Rubric:** five dimensions, each scored from 1 to 5

## Executive summary

This exercise demonstrates a structured way to distinguish a fluent answer from one that is supported by the supplied evidence and follows the task. Each of 30 authored prompt/response pairs is scored for factuality, instruction-following, completeness, clarity, and safety/judgment. The records include rationales and a severity label for the most consequential issue.

## Evaluation problem

A response can sound confident and still be wrong, incomplete, unsafe or non-compliant with an exact instruction. The evaluator must identify which requirement failed, cite the prompt or supplied evidence that supports the judgment, and avoid allowing a strong score in one dimension to conceal a critical failure elsewhere.

## Data and scope

The dataset contains 30 original synthetic prompt/response pairs covering arithmetic, instruction-following, uncertainty, summarization, safety, privacy, formatting, explanation, code reasoning, missing context, translation, tone, data interpretation and scope control.

The data and reference judgments are author-created. They are not sampled from a deployed model, independently adjudicated or representative of an industry benchmark.

## Method

1. Read the prompt and candidate response together.
2. Score factuality, instruction-following, completeness, clarity, and safety/judgment independently.
3. Apply the anchors in the [evaluation rubric](evaluation-rubric.md).
4. Record an evidence-linked rationale for each score.
5. Assign the most consequential observed issue a severity tag.
6. Calculate descriptive summaries without allowing a mean score to mask critical failures.
7. Review recurring error patterns and state the limits of the exercise.

## Descriptive results

| Measure | Observed result |
|---|---:|
| Prompt/response pairs | 30 |
| Mean overall score | 3.98 / 5 |
| Factuality | 3.53 / 5 |
| Instruction-following | 3.80 / 5 |
| Completeness | 3.63 / 5 |
| Clarity | 4.70 / 5 |
| Safety and judgment | 4.23 / 5 |
| Critical-severity examples | 1 |
| Major-severity examples | 10 |
| Minor-severity examples | 4 |
| No material issue identified | 15 |

These figures summarize the author-created practice set only. They do not represent model accuracy, evaluator proficiency, inter-rater reliability or a comparison against an external standard.

## Findings and evaluator decisions

- **Unsupported specificity:** weak responses sometimes invent details when the prompt lacks evidence. The evaluator should distinguish a supported inference from fabricated precision.
- **Instruction compliance:** a true answer can still fail an exact-output or scope requirement.
- **Source fidelity:** summaries must preserve qualifiers; changing a time, condition or scope can materially alter the source.
- **Severity:** safety and privacy failures require explicit treatment and should not disappear inside an average.
- **Communication:** clarity and tone matter, but cannot compensate for unsupported claims.

The [findings report](findings-report.md) contains the detailed observations and recommended practices.

## Deliverables

- [Evaluation rubric](evaluation-rubric.md)
- [30 evaluated examples](evaluated-responses.csv)
- [Findings report](findings-report.md)

## Quality controls

The five dimensions are scored separately and accompanied by written rationales. Severity labels are recorded independently of the aggregate mean. A reviewer can inspect the row-level prompt, response, score and rationale rather than relying only on a summary statistic.

## Limitations and evidence boundary

This is a small, synthetic, single-evaluator exercise using author-created reference judgments. There is no independent second-rater adjudication, inter-annotator agreement study, calibrated benchmark, or production model test. The sample demonstrates rubric application, evidence-based rationales, severity tagging and descriptive reporting—not paid client experience or generalizable model performance.

## Next validation that would strengthen the work

Use a frozen set of externally sourced or independently authored responses, have at least one second evaluator score them without seeing the first ratings, adjudicate disagreements against a pre-defined rubric, and report agreement and disagreement categories. If evaluating live models, preserve model/version metadata and complete raw outputs.
