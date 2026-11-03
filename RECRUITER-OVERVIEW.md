# Recruiter Overview — Software Development, AI Evaluation & Data Quality

## Candidate positioning

**Software developer with demonstrated work in Android application development and structured AI/data evaluation practice.**

This portfolio combines an independently developed Android application with practical work samples in AI response evaluation, text annotation, evaluation methodology, and dataset quality assurance. It is relevant to software development roles as well as technical AI operations and evaluation roles.

## Software engineering evidence

### [MemoryImprovement — Android application](https://github.com/jaackdoe35-sudo/MemoryImprovement)

An offline-first Android application for organizing information, practising active recall, and tracking memory performance over time.

The repository documents:
- Kotlin and Jetpack Compose application development.
- Room persistence and local preferences.
- Offline-first workflows and local data management.
- Memory-palace structures with nested locations.
- Multiple recall and review modes.
- Progress tracking and delayed-retention checkpoints.
- Gradle build workflows and GitHub Actions CI.
- Unit tests, debug APK assembly, and separate instrumentation-test workflow.

**Validation boundary:** The project is under development. Its README distinguishes compilation and APK assembly from feature completeness and emulator integration-test validation. A physical-device acceptance test remains outstanding. The portfolio does not claim that every feature is complete or that the app's memory techniques are clinically or scientifically validated.

## AI evaluation and data quality evidence

| Work sample | Evidence available | What it demonstrates |
|---|---|---|
| [AI response evaluation rubric](01-ai-response-evaluation/evaluation-rubric.md) | Five scoring dimensions, rating anchors, severity tags and evidence-note rules | Structured evaluation criteria |
| [30-example evaluation dataset](01-ai-response-evaluation/evaluated-responses.csv) | Synthetic prompt/response examples with scores and rationales | Consistent rubric application |
| [Evaluation findings report](01-ai-response-evaluation/findings-report.md) | Descriptive score summary, observed patterns and limitations | Evidence-based reporting |
| [Annotation guidelines](02-data-annotation/annotation-guidelines.md) | Label definitions and boundary rules | Taxonomy-based annotation |
| [50-row annotated dataset](02-data-annotation/annotated-dataset.csv) | Synthetic messages with intent and sentiment labels | Structured text labeling |
| [Quality assurance report](03-quality-assurance/quality-assurance-report.md) | Row counts, unique IDs, populated fields and label distribution | Dataset checks and transparent QA reporting |
| [Advanced blind evaluation](07-advanced-blind-evaluation/challenge.md) | Five paired-response cases | Comparative judgment and error analysis |
| [Evaluator reflection](07-advanced-blind-evaluation/reflection.md) | 5/5 preference agreement with an author-created key, plus qualitative rationale review | Reflective practice and transparent reporting |
| [Realistic response review](08-realistic-response-review/README.md) | Six completed cases, scoring results and reflection | Contextual evaluation, pairwise judgment and five-dimensional scoring |
| [End-to-end annotation case study](09-end-to-end-annotation-case-study/README.md) | 40-row dataset, methodology, taxonomy, ambiguity log, QA report and findings | End-to-end annotation workflow and quality documentation |

## Working approach

- Translate task instructions into explicit criteria and schemas.
- Separate source-supported facts from unsupported claims.
- Record evidence for evaluation and annotation decisions.
- Treat missing information as unknown rather than filling gaps.
- Validate structured data for completeness, consistency and allowed values.
- Document ambiguity, limitations and corrective actions.
- Use software engineering practices where they improve repeatability and reliability.

## Tools and technologies evidenced in the repositories

**Software project:** Kotlin, Jetpack Compose, Room, Gradle, GitHub Actions.

**Portfolio artifacts:** Markdown, CSV, GitHub version control, annotation schemas, evaluation rubrics and QA reports.

This section lists technologies documented in the linked project; it does not imply experience with every commercial annotation platform, cloud environment, or production ML stack.

## Experience and evidence boundary

The AI evaluation and annotation examples are synthetic and self-directed. They are not paid work, employment, client engagements, or independent benchmark results. Preference scores are agreement with author-created reference keys, not externally validated proficiency scores.

The end-to-end annotation case study was produced in a single pass and self-audited. It does not establish independent annotator agreement, production QA, throughput, or professional client experience.

The Android application is a separate independently developed project. Its implementation, commit history, and CI evidence should be reviewed directly. It remains under development, with physical-device acceptance testing and other validation still required.

## Suitable role families

- Android developer / junior software developer
- Application developer
- AI response evaluator / model evaluator
- AI data annotator / annotation specialist
- Dataset QA / data quality analyst
- AI evaluation operations and tooling support

Actual eligibility depends on each employer's location restrictions, language requirements, technical assessment, device requirements, schedule, and payment arrangements.

## Contact

Use the repository owner's GitHub profile to contact the candidate.
