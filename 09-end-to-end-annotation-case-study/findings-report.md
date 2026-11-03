# Findings Report — End-to-End Support Message Annotation
## Executive summary
A 40-record synthetic support-message dataset was annotated using a predefined taxonomy. Each row contains a primary intent, sentiment, urgency, synthetic PII tag, clarification flag, and evidence-based rationale. Implemented schema checks returned zero issues.
## Key observations
1. The schema separates intent from sentiment and urgency, avoiding the assumption that negative sentiment automatically means urgent.
2. The taxonomy distinguishes adjacent routes such as suspected fraud vs merchant dispute, transfer cancellation vs transfer reversal, and withdrawal-limit inquiry vs limit-change request.
3. Six records were flagged for clarification rather than forcing a narrow label unsupported by the text.
4. Synthetic PII placeholders were identified without using real personal information.
5. Each annotation includes a concise rationale to make decisions inspectable.
## What this demonstrates
- Translating a task into a structured schema.
- Defining labels and boundary rules before annotation.
- Applying a consistent row-level annotation format.
- Handling ambiguity and sensitive-data placeholders.
- Performing schema validation and documenting QA limits.
- Reporting findings without overstating the evidence.
## What it does not demonstrate
- Performance on real customer messages.
- Independent annotation agreement or adjudication.
- Financial-services compliance expertise.
- Production throughput or proprietary platform experience.
- A model's classification accuracy.
- Generalization to other languages, countries, or support domains.
## Recommended next validation
Apply the schema to an appropriately licensed public corpus, preserve original IDs and source labels, document sampling, and have a second human annotator independently label a subset before adjudication.