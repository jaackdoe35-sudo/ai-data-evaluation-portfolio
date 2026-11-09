# Project 01 — AI Response Evaluation

**Status:** Completed self-directed practice sample  
**Evaluation unit:** 30 synthetic prompt/response pairs  
**Rubric:** Five dimensions, each scored from 1 to 5

## Evaluation question

How consistently can an evaluator distinguish a response that is merely fluent from one that is factually supported, follows the instruction, covers the task, communicates clearly and exercises sound judgment?

This exercise demonstrates a repeatable manual review method. It is not an evaluation of a named model or a benchmark result.

## Scope and data

The dataset contains 30 original synthetic prompt/response pairs covering arithmetic, instruction-following, uncertainty, summarization, safety, privacy, formatting, explanation, code reasoning, missing context, translation, tone, data interpretation and scope control.

The examples deliberately include both strong and weak responses. The data and reference judgments are author-created; they are not sampled from a deployed model or independently adjudicated.

## Method

1. Read the user prompt and candidate response together.
2. Score factuality, instruction-following, completeness, clarity, and safety/judgment independently.
3. Record an evidence-linked rationale for each score.
4. Assign the most consequential observed issue a severity tag.
5. Calculate a descriptive overall mean without allowing a high score in one dimension to conceal a critical failure in another.
6. Review recurring error patterns and document limitations.

The full [evaluation rubric](evaluation-rubric.md) defines the scoring anchors, dimension criteria, severity tags and evidence-note rules.

## Results

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

These are descriptive summaries of the authored practice set. They do not represent model accuracy, an industry benchmark, or independently measured evaluator proficiency.

## Key findings

- Unsupported specificity is a recurring failure mode: weak responses invent facts when the prompt lacks evidence.
- Instruction-following is distinct from factuality: a response can be true but still violate an exact-output constraint.
- Summaries must preserve qualifiers; changing a time or scope condition can materially alter the source.
- Safety and privacy errors require explicit severity treatment rather than being hidden in an average score.
- Audience and tone are part of task success, not optional stylistic extras.

The [findings report](findings-report.md) contains the complete observations and recommended evaluator practices.

## Files

- [Evaluation rubric](evaluation-rubric.md)
- [30 evaluated examples](evaluated-responses.csv)
- [Findings report](findings-report.md)

## Evidence boundary

This is a small, synthetic, single-evaluator exercise using author-created reference judgments. There is no independent second-rater adjudication, inter-annotator agreement study, calibrated benchmark, or production model test. The sample demonstrates rubric application, evidence-based rationales, severity tagging and descriptive reporting—not paid client experience or generalizable model performance.

## Reproduction

Review the CSV alongside the rubric and findings report. Each row contains the prompt, candidate response, five dimension scores, overall mean, severity label and evidence rationale.
