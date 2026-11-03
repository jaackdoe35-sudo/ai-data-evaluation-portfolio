# Recruiter Overview — AI Data Annotation & Evaluation

## Candidate positioning

**AI Data Annotation & Evaluation Specialist**

This portfolio presents practical, self-directed work samples in AI response evaluation, text annotation, annotation guidelines, quality assurance, ambiguity handling, search relevance evaluation, and structured reporting. It is intended for annotation, AI evaluation, and data quality roles.

## Relevant work samples

| Work sample | Evidence available | What it demonstrates |
|---|---|---|
| [AI response evaluation rubric](01-ai-response-evaluation/evaluation-rubric.md) | Five scoring dimensions, rating anchors, severity tags and evidence-note rules | Structured evaluation criteria |
| [30-example evaluation dataset](01-ai-response-evaluation/evaluated-responses.csv) | Synthetic prompt/response examples with scores and rationales | Rubric application and evidence-based judgments |
| [Evaluation findings report](01-ai-response-evaluation/findings-report.md) | Descriptive score summary, observed patterns and limitations | Clear findings and limitations |
| [Annotation guidelines](02-data-annotation/annotation-guidelines.md) | Label definitions and boundary rules | Taxonomy-based annotation |
| [50-row annotated dataset](02-data-annotation/annotated-dataset.csv) | Synthetic messages with intent and sentiment labels | Structured text labeling |
| [Quality assurance report](03-quality-assurance/quality-assurance-report.md) | Row counts, unique IDs, populated fields and label distribution | Dataset checks and transparent QA reporting |
| [Advanced blind evaluation](07-advanced-blind-evaluation/challenge.md) | Five paired-response cases | Comparative judgment and error analysis |
| [Evaluator reflection](07-advanced-blind-evaluation/reflection.md) | 5/5 preference agreement with an author-created key, plus qualitative rationale review | Reflective practice and transparent reporting |
| [Realistic response review](08-realistic-response-review/README.md) | Six completed cases, scoring results and reflection | Contextual evaluation and five-dimensional scoring |
| [End-to-end annotation case study](09-end-to-end-annotation-case-study/README.md) | 40-row dataset, methodology, taxonomy, ambiguity log, QA report and findings | End-to-end annotation workflow and quality documentation |
| [Annotation CSV Validator](10-annotation-csv-validator/README.md) | Python utility, sample CSV and unit tests | Structural and categorical validation |
| [Annotation Consistency Checker](11-annotation-consistency-checker/README.md) | Python utility, sample CSV and unit tests | Rule-based flags for human review |
| [AI Response Evaluation Score Calculator](12-ai-response-score-calculator/README.md) | Python utility, sample evaluations, generated report and unit tests | Rubric arithmetic, score summaries and severity counts |
| [Annotation Data Quality Review Dashboard](13-annotation-qa-dashboard/README.md) | Python utility, sample annotations, HTML dashboard and unit tests | Label distributions and structural QA reporting |
| [Search and Content Relevance Evaluation](14-search-relevance-evaluation/README.md) | 20 synthetic query-result cases, relevance grades, rationales and QA summary | Search intent identification, constraint matching and relevance judgment |

## Working approach

- Translate task instructions into explicit criteria and schemas.
- Separate source-supported facts from unsupported claims.
- Record evidence for evaluation and annotation decisions.
- Treat missing information as unknown rather than filling gaps.
- Validate structured data for completeness, consistency and allowed values.
- Document ambiguity, limitations and corrective actions.
- Escalate unclear or conflicting cases for review rather than silently guessing.

## Supporting technical skills

Basic scripting and spreadsheet skills can support data cleaning, CSV validation, duplicate detection, label checks, and evaluation summaries. The small Python demonstrations in this portfolio show how simple rule-based checks can support annotation QA. They are supporting methods for annotation and quality work—not a separate software-development role or a claim of expertise in complex engineering.

## Experience and evidence boundary

The AI evaluation, annotation and search-relevance examples are synthetic and self-directed. They are not paid work, employment, client engagements, or independent benchmark results. Preference scores are agreement with author-created reference keys, not externally validated proficiency scores.

The end-to-end annotation case study was produced in a single pass and self-audited. It does not establish independent annotator agreement, production QA, throughput, or professional client experience.

The supporting tools are small demonstrations against documented synthetic schemas. Their tests cover selected rule behavior; they do not prove semantic annotation accuracy or production readiness.

## Suitable role families

- AI Data Annotator / Annotation Specialist
- AI Response Evaluator / LLM Evaluator
- AI Trainer / AI Data Reviewer
- Annotation Quality Reviewer
- Data Quality Assurance Analyst
- Search and Content Relevance Evaluator

Actual eligibility depends on each employer's location restrictions, language requirements, assessment, device requirements, schedule, and payment arrangements.

## Contact

Use the repository owner's GitHub profile to contact the candidate.
