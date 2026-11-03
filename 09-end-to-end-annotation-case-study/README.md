# Project 06 — End-to-End Support Message Annotation Case Study
## Objective
Demonstrate a complete, inspectable workflow on a small support-message dataset: define a task, specify a taxonomy, annotate records, handle ambiguity and sensitive-data placeholders, validate output, and document limitations.
## Data provenance
All 40 messages in annotated_dataset.csv are original synthetic examples written for this portfolio. They are not copied from customer records, sourced from an employer, or real financial-support conversations. No external dataset license is claimed for these authored examples.
Synthetic data permits a transparent workflow demonstration but does not establish performance on real-world customer language. A future extension can repeat the workflow on an appropriately licensed public corpus with attribution and documented sampling.
## Files
- [Task specification and workflow](methodology.md)
- [Annotation guidelines and taxonomy](annotation-guidelines.md)
- [40-row annotated dataset](annotated_dataset.csv)
- [Quality-control report](qa-report.md)
- [Ambiguity and boundary log](ambiguity-log.md)
- [Findings and limitations](findings-report.md)
## Workflow
1. Define the annotation unit and output fields.
2. Establish label definitions and boundary rules before labeling.
3. Create 40 synthetic messages covering common and difficult support intents.
4. Apply intent, sentiment, urgency, PII, clarification, and rationale labels.
5. Run structural and schema validation.
6. Inspect ambiguous boundary cases and document treatment.
7. Summarize distributions, QA checks, and limitations.
## Evidence boundary
This is a self-authored, single-pass demonstration with a documented self-audit. It is not independent double annotation, adjudication by a second reviewer, inter-annotator agreement, production QA, or evidence of professional client work.