# Independent Second-Rater Protocol

**Purpose:** obtain genuine evaluator disagreement and adjudication evidence. An LLM-generated second opinion is not a substitute for a human independent rater.

1. Freeze the task set, label schema and rubric version; record the commit SHA.
2. Give the second rater `tasks.csv` and the rubric, but not `gold-standard.csv` or the primary candidate's labels.
3. Ask the second rater to complete an independent copy of the submission template without discussion.
4. Compare primary and second-rater labels only after both files are frozen.
5. Calculate raw agreement separately for intent, priority and action_required.
6. For categorical labels, use Cohen's kappa for two raters when its assumptions fit; report the confusion matrix and prevalence limitations. Do not calculate kappa if a field is constant or data are insufficient.
7. Adjudicate each disagreement against the written rubric and message evidence. Preserve both original labels and the adjudicated label with rationale.
8. Update the answer key only if an actual defect is demonstrated. Version any correction and retain the old version.

## Required report
- Rater identifiers or anonymized codes
- Independent completion dates and elapsed time
- Number of records rated
- Raw agreement per field
- Confusion matrices
- Kappa and confidence interval where appropriate
- Disagreement categories
- Adjudication decisions and rationale
- Any rubric ambiguity or reference-key correction

Until a second human completes this protocol, inter-rater agreement is **not measured**.
