# Project 09 — End-to-End Support Message Annotation Case Study

**Work type:** self-directed, synthetic annotation exercise  
**Status:** completed single-pass practice sample with documented self-audit  
**Dataset:** 40 original synthetic support messages  
**Output:** structured labels, rationales, clarification flags and QA documentation

## Executive summary

This case study demonstrates how to turn a support-message task into a repeatable annotation workflow. It defines the annotation unit and label taxonomy before applying intent, sentiment, urgency, synthetic PII, clarification and rationale fields to 40 authored examples. The work includes schema checks, an ambiguity log and a findings report.

## Task and decision problem

A support operations team needs incoming messages classified consistently so that requests can be routed and reviewed. The annotation challenge is to keep related concepts separate: a negative sentiment is not automatically high urgency, a mention of fraud is not always a confirmed fraud event, and missing context should be flagged rather than silently invented.

## Data and scope

All 40 messages in `annotated_dataset.csv` are original synthetic examples written for this portfolio. They are not copied from customer records, sourced from an employer, or real financial-support conversations. No external dataset license is claimed.

The sample covers common support intents and deliberately includes boundary cases. Synthetic data permits a transparent workflow demonstration but does not establish performance on real-world customer language.

## Method

1. Define the annotation unit, output fields and allowed values.
2. Establish label definitions, inclusion/exclusion rules and boundary examples before labeling.
3. Create 40 synthetic messages covering common and difficult support intents.
4. Apply intent, sentiment, urgency, PII, clarification and rationale labels.
5. Run structural/schema validation and inspect flagged records.
6. Record ambiguous boundary decisions and summarize the observed label patterns.
7. Document what the checks do—and do not—establish.

The [task methodology](methodology.md) and [annotation guidelines](annotation-guidelines.md) provide the operational rules.

## Observed results

- **40** synthetic messages annotated.
- **6** records explicitly flagged for clarification rather than forcing an unsupported narrow label.
- **0** structural/schema issues reported by the implemented checks.
- Each record includes a concise rationale; the [QA report](qa-report.md), [ambiguity log](ambiguity-log.md) and [findings report](findings-report.md) expose the review trail.

These are descriptive facts about this authored exercise. Zero schema issues is not equivalent to zero semantic errors.

## Quality controls and decision logic

The workflow separates intent, sentiment and urgency instead of treating them as interchangeable. It records synthetic PII placeholders, uses clarification flags for insufficient context, and makes row-level rationales inspectable. Structural validation checks whether outputs conform to defined rules; it cannot independently prove that each semantic label is correct.

## Deliverables

- [Task specification and workflow](methodology.md)
- [Annotation guidelines and taxonomy](annotation-guidelines.md)
- [40-row annotated dataset](annotated_dataset.csv)
- [Quality-control report](qa-report.md)
- [Ambiguity and boundary log](ambiguity-log.md)
- [Findings and limitations](findings-report.md)

## Limitations and evidence boundary

This is a self-authored, single-pass demonstration with a documented self-audit. It is not independent double annotation, second-reviewer adjudication, inter-annotator agreement, production QA, or evidence of professional client work. The messages are synthetic and the labels were not independently adjudicated. No production throughput or generalization to other domains, locales or languages is claimed.

## Next validation that would materially strengthen the evidence

Apply the taxonomy to an appropriately licensed, source-attributed public dataset; freeze the sampling procedure; have a second human annotator label a subset independently; calculate agreement before adjudication; record disagreements and taxonomy revisions; then repeat the structural and semantic QA review.
