# Semantic and Reference-Key Audit

**Status:** Focused self-review completed; independent adjudication not performed.  
**Scope:** Portfolio datasets and synthetic evaluation keys on the current main branch.

## Audit method

Each dataset was read alongside its task instructions, taxonomy, rubric, and any report or reference key. The review checked whether labels and scores were supported by the supplied text, whether rationales described the decisive evidence, whether constraints were applied consistently, and whether answer keys contained internally inconsistent judgments.

This is a single-reviewer audit. It is not independent gold-label validation, inter-annotator agreement, or evidence of production annotation accuracy.

## Findings and corrections

### Project 1 — AI response evaluation (30 cases)

Reviewed all 30 prompt/response records against the five-dimension rubric and findings summary.

- The arithmetic, exact-count, unsupported-specificity, summarization, privacy, safety, translation, and code-semantics examples have rationales that identify the central defect.
- E010's advice to add vinegar to a bleach/ammonia mixture is correctly treated as a critical safety failure.
- E012's recommendation to search leaked databases and people-finder sources is correctly treated as a major privacy/judgment failure. It is an unsafe recommendation, not evidence that private information was actually obtained.
- E016's answer is technically related but poorly adapted to a 10-year-old; its minor severity is consistent with the rubric.
- E028 asserts a definitive battery diagnosis without evidence; the major severity is defensible.
- The reported means and severity distribution are checked automatically by the repository workflow.

**Residual limitation:** Dimension scores and severity labels remain authored judgments. Some score boundaries are subjective and need a second reviewer for adjudication.

### Project 2 — Introductory text annotation (50 records)

Reviewed every message against the eight-label intent taxonomy and four sentiment definitions.

**Correction:** A016 (“Can I change the email address linked to my profile?”) was labeled `account_access`. That is not a login, password, verification, or access failure; it is a profile update. Because this small taxonomy has no profile-update label, it is now labeled `other`, with the rationale documenting the taxonomy limitation.

The QA report and automated expected counts were updated accordingly:
- `account_access`: 6
- `other`: 2
- Other intent and sentiment counts remain unchanged.

**Residual limitation:** Some messages could reasonably be routed differently under a different support taxonomy. For example, pricing questions can be product-information or billing depending on the client's routing convention. The current guideline defines price questions as billing.

### Project 6 — Paired-response challenge (10 cases)

Reviewed all ten prompts and the author-created key. The arithmetic, source-fidelity, missing-context, exact-format, safety, code semantics, date extraction, privacy, unsupported inference, and unauthorized-action examples have a defensible preferred response or tie under the stated rubric.

C01 is a defensible tie: both answers are mathematically correct, while B explains the remaining 75% more explicitly. C10 correctly rejects fabricated account access and refund promises.

### Project 7 — Advanced blind evaluation (5 cases)

**Correction:** The reference key previously marked C01 as Tie. Recalculation gives:
- Correct notebook subtotal: ₦10,000.
- Correct pen subtotal: ₦2,000.
- Correct total: ₦12,000.
- Response A has both subtotals correct but adds them incorrectly as ₦12,500.
- Response B reports the pen subtotal incorrectly as ₦2,500 and also gives ₦12,500.

A is materially better because its component calculations are correct and its only arithmetic error is the final addition. The key is corrected to A, and the rationale now explains why. C02–C05 key decisions are consistent with the supplied constraints and arithmetic.

### Project 8 — Realistic response review (6 cases)

Reviewed all six scenarios, reference decisions, and recorded evaluation results.

- C01 correctly favors the response that does not invent carrier escalation, delivery timing, or monitoring.
- C02 correctly favors the response preserving the damaged-item shipping-fee exception.
- C03 correctly distinguishes an observed score difference from a causal claim; differing sample sizes/response rates and unknown comparability prevent causal attribution.
- C04 correctly treats 03/07/2026 as ambiguous without a date convention. The raw value should be preserved rather than normalized by assumption.
- C05 correctly prefers proportionate, label-led precautions over blanket refusal. Cleanup advice is conditional on product-label instructions and circumstances; it must not be generalized to mixed chemicals or symptomatic exposure.
- C06 correctly treats possible causes as hypotheses and avoids destructive action before evidence is collected.

**Data-quality note:** C01's confidence field in `evaluation-results.csv` is blank. It has not been filled because no verified confidence value is available. This is an incomplete worksheet field, not a fabricated value.

### Project 9 — End-to-end support annotation (40 records)

Reviewed all records against the detailed financial-support taxonomy, urgency rules, sentiment definitions, PII rules, and ambiguity log.

The key boundary distinctions are generally reflected in the labels: suspected unauthorized activity versus merchant dispute; transfer cancellation versus reversal; missing card versus lost card; duplicate charge versus fee inquiry; withdrawal-limit inquiry versus limit-change request; and unclear intent versus a specific route.

The six clarification cases (S023, S024, S025, S032, S035, S040) are disclosed in the ambiguity log. S032 preserves uncertainty about a possible duplicate rather than asserting it as fact. S040 does not assume both a lost card and suspicious payment occurred.

PII examples use synthetic tokens only. The structural audit checks tag/span agreement and token presence in the source message.

**Residual limitation:** This dataset was authored and reviewed by one annotator. Borderline urgency and sentiment decisions remain judgment calls. No independent financial-services domain reviewer or compliance specialist has adjudicated it.

### Project 14 — Search relevance evaluation (20 cases)

Reviewed each query, intent, result title/snippet, grade, and rationale against the four-grade relevance scale.

The labels distinguish direct matches (for example SR001–SR006, SR010–SR011, SR016, SR019), partial/constraint-mismatched results (SR007–SR009, SR012–SR017), and results that fail the dominant intent (SR018, SR020). The grade choices are plausible under this practice scale; cases with missing requested attributes are not treated as full matches.

**Residual limitation:** Search relevance grading is inherently rubric- and locale-dependent. The dataset uses synthetic snippets, not live results. A second rater could reasonably debate some grade-1 versus grade-2 boundaries, especially where a result is topically related but misses a key constraint. The four review-flagged cases remain useful examples of ambiguity.

## Reference-key integrity

- Project 6 C01: tie is defensible because both responses are correct; B provides a more explicit explanation.
- Project 7 C01: corrected from Tie to A because B contains an additional incorrect subtotal.
- Project 8 C01–C06: rationales align with the supplied notes and task constraints. C04 preserves date ambiguity; C05 retains product-label and exposure caveats.
- All keys are author-created references. None is represented as an independently adjudicated gold standard.

## Tool robustness audit — executed

Additional negative and edge-case tests were added and executed in GitHub Actions:

- CSV validator: empty datasets, duplicate headers, absent required columns, PII tokens missing from source text, and valid PII token acceptance.
- Consistency checker: empty datasets, PII token/source mismatch, matching PII token acceptance, and duplicate normalized text with the same label.
- Score calculator: empty datasets, all-N/A scores, fractional scores, non-finite scores, invalid severity, and missing headers.
- QA dashboard: empty datasets, invalid primary intent, duplicate headers, and HTML escaping of rendered label values.

The final verification run completed successfully. Test counts: validator 9, consistency checker 7, score calculator 11, dashboard 9, search relevance 5 — **41 tests passed**. The four command-line tools also executed against their sample CSVs; the generated score report and dashboard were checked for non-empty output. The dashboard HTML artifact was uploaded by the workflow.

The added checks exposed an important test-design issue: the first HTML-escaping test put script-like text in a field that the dashboard does not render. The test was corrected to place it in a rendered label field, then the full workflow passed. Earlier workflow runs failed during this process; they are not the final result.

## Release implications

This audit improves internal consistency and corrects two material reference/label issues. It does **not** establish independent annotation accuracy or professional proficiency. For an employer-facing portfolio, keep the synthetic/self-directed disclosure and these limitations visible. Independent review remains the strongest next evidence improvement.
