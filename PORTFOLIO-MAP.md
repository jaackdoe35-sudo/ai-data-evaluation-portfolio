# Portfolio System Map — How the Projects Connect

This repository is one connected body of self-directed practice across the AI data lifecycle. The projects are not presented as unrelated exercises: each stage creates, evaluates, validates, or governs evidence used by another stage.

## The end-to-end model

```text
TASK DESIGN & SOURCE UNDERSTANDING
  Project 05 — Skills and methodology
  Project 04 — Transcription sample
                 |
                 v
DATA / CONTENT JUDGMENT
  Project 02 — Text annotation
  Project 09 — End-to-end annotation case study
  Project 18 — Image annotation
  Project 19 — Video transcript and caption QA
  Project 14 — Search relevance evaluation
                 |
                 v
QUALITY CONTROL & EVIDENCE INTEGRITY
  Project 03 — Annotation QA report
  Project 10 — CSV schema validator
  Project 11 — Cross-record consistency checker
  Project 13 — Annotation QA dashboard
  Project 15 — Semantic and reference-key audit
  Project 16 — QA utility stress test
                 |
                 v
AI OUTPUT EVALUATION
  Project 01 — Response evaluation rubric and dataset
  Project 06 — Paired response challenge
  Project 07 — Advanced blind evaluation
  Project 08 — Realistic response review
  Project 12 — Evaluation score calculator
                 |
                 v
SAFETY-FOCUSED EVALUATION
  Project 20 — Controlled LLM security scenario catalogue
                 |
                 v
GOVERNANCE & ASSURANCE
  Project 21 — AI governance and assurance case study

Cross-cutting: evidence-based rationales, source traceability, uncertainty handling,
validation, human review, documented limitations and corrective feedback.
```

This is a conceptual workflow, not a claim that every artifact is an input to a production system or that all activities were performed on one shared dataset. The projects use separate synthetic or explicitly sourced practice materials.

## Stage-by-stage connections

### 1. Task design, source understanding and method

- [Project 05 — Skills and methodology](05-skills/skills-and-methodology.md) describes the shared method: parse instructions, identify available evidence, apply a rubric or taxonomy, record a rationale, flag uncertainty and review consistency.
- [Project 04 — Transcription sample](04-transcription/transcription-sample.md) is an example of source-derived text work. It connects to [Project 19 — Video transcript and caption QA](19-video-annotation/README.md), which examines a sourced caption excerpt and its timing/structure.
- These foundations matter because downstream annotation and evaluation are only meaningful when the task, source and limits are understood.

### 2. Data labeling, content judgment and modality-specific work

- [Project 02 — Text annotation](02-data-annotation/README.md) defines a taxonomy and applies it to 50 synthetic messages.
- [Project 09 — End-to-end annotation](09-end-to-end-annotation-case-study/README.md) expands the same discipline into a documented workflow: task definition, taxonomy, 40 records, ambiguity log, QA and findings.
- [Project 18 — Image annotation](18-image-annotation/README.md) applies structured labels and bounding boxes to an original synthetic vector scene.
- [Project 19 — Video transcript and caption QA](19-video-annotation/README.md) handles source-attributed caption cues; it is transcript/caption work, not visual object tracking or audio verification.
- [Project 14 — Search relevance](14-search-relevance-evaluation/README.md) applies the same evidence-and-rationale discipline to query intent and result relevance rather than labeling message content.

**Connection:** these projects demonstrate how task-specific schemas differ by modality and objective while retaining a common method: follow instructions, label only supported information, explain decisions and flag ambiguity.

### 3. Quality control, validation and evidence integrity

- [Project 03 — Quality assurance report](03-quality-assurance/quality-assurance-report.md) reviews the 50-row dataset from Project 02.
- [Project 10 — CSV validator](10-annotation-csv-validator/README.md) checks the schema and categorical constraints used by the end-to-end annotation work in Project 09.
- [Project 11 — Consistency checker](11-annotation-consistency-checker/README.md) flags selected cross-record and cross-field patterns for human review; a flag is not an automatic correction.
- [Project 13 — QA dashboard](13-annotation-qa-dashboard/README.md) summarizes structural and categorical checks in a local report.
- [Project 15 — Semantic and reference-key audit](15-semantic-and-reference-audit/README.md) reviews whether labels, scores, rationales and reference judgments are supported by their task instructions and source evidence.
- [Project 16 — QA stress test](16-annotation-qa-stress-test/README.md) exercises the validator, consistency checker, dashboard and score calculator on deterministic synthetic workloads.

**Connection:** annotation creates structured records; QA tools test defined structural rules; human semantic review checks whether judgments are actually supported; stress testing examines how selected utilities behave at larger synthetic row counts. These are complementary checks, not interchangeable proof of accuracy.

### 4. AI response evaluation and comparative judgment

- [Project 01 — AI response evaluation](01-ai-response-evaluation/README.md) establishes a five-dimension rubric and applies it to 30 synthetic response examples.
- [Project 06 — Paired response challenge](06-paired-response-challenge/README.md) uses comparative judgments, separate scoring and written rationales.
- [Project 07 — Advanced blind evaluation](07-advanced-blind-evaluation/README.md) extends comparative review to subtle instruction, evidence and calibration issues.
- [Project 08 — Realistic response review](08-realistic-response-review/README.md) applies a review protocol to longer scenarios and documents a decision revision.
- [Project 12 — Response score calculator](12-ai-response-score-calculator/README.md) checks score inputs, recalculates arithmetic and summarizes the five-dimension evaluation records.

**Connection:** Project 01 provides a rubric foundation; Projects 06–08 exercise that judgment in increasingly contextual comparative tasks; Project 12 checks score arithmetic and reporting. The calculator does not validate the evaluator's underlying judgment.

### 5. Safety-focused evaluation

- [Project 20 — LLM security evaluation](20-llm-security-evaluation/README.md) extends the portfolio's rubric, evidence-recording and QA discipline to 12 controlled security scenario specifications.

**Connection:** the same evaluation principles apply—define expected behavior, identify observable evidence, record actual outcomes and limitations—but the subject becomes security-relevant behavior such as prompt injection, instruction hierarchy, tool authorization and secret handling. The catalogue has not been executed against a live model; it is a test specification, not a vulnerability finding.

### 6. AI governance and assurance

- [Project 21 — AI governance and assurance](21-ai-governance-and-assurance/README.md) uses a fictional recruitment-screening system to organize an inventory, impact assessment, risk register, proposed controls, data lineage, human oversight, monitoring, incident response, regulatory issue mapping and an evidence-bounded assurance review.

**Connection:** governance brings the earlier disciplines together at the system level:
- annotation and data QA inform data quality, provenance and fitness-for-purpose questions;
- response evaluation informs performance measurement and ongoing monitoring design;
- semantic audits and evidence records inform traceability and assurance;
- security evaluation informs security-risk and control-testing questions;
- human review and escalation connect quality findings to accountable oversight.

The governance artifacts are proposed design work only. They do not establish that controls exist, operate effectively, or meet legal requirements.

## Relationship index

| Project | Primary role | Connects to |
|---|---|---|
| 01 AI response evaluation | Rubric and response judgments | 06, 07, 08, 12, 15, 20, 21 |
| 02 Text annotation | Taxonomy and labeled data | 03, 09, 10, 11, 13, 15, 16, 21 |
| 03 QA report | Dataset review | 02, 09, 10, 11, 13, 15 |
| 04 Transcription sample | Source-derived text | 19 |
| 05 Skills and methodology | Shared operating method | All projects |
| 06 Paired challenge | Comparative evaluation | 01, 07, 08, 12, 15, 20 |
| 07 Advanced blind evaluation | Calibrated comparative review | 01, 06, 08, 12, 15, 20 |
| 08 Realistic response review | Context-rich evaluation | 01, 06, 07, 12, 15, 20 |
| 09 End-to-end annotation | Full annotation workflow | 02, 03, 10, 11, 13, 15, 16, 21 |
| 10 CSV validator | Structural validation | 02, 09, 11, 13, 15, 16 |
| 11 Consistency checker | Human-review flags | 02, 09, 10, 13, 15, 16 |
| 12 Score calculator | Evaluation arithmetic/reporting | 01, 06, 07, 08, 15, 16 |
| 13 QA dashboard | QA summaries | 02, 09, 10, 11, 15, 16 |
| 14 Search relevance | Query/result judgments | 01, 05, 15, 21 |
| 15 Semantic/reference audit | Cross-project evidence review | 01, 02, 06–14, 18–21 |
| 16 QA stress test | Utility robustness at scale | 10, 11, 12, 13 |
| 18 Image annotation | Visual data labeling | 05, 15, 21 |
| 19 Video transcript/caption QA | Source-based caption review | 04, 05, 15, 21 |
| 20 LLM security evaluation | Security test design | 01, 05–08, 12, 15, 21 |
| 21 AI governance and assurance | System-level risk and control design | 02, 03, 09–16, 18–20 |

## How to read the portfolio responsibly

- **Observed / completed practice:** use only where the repository contains the actual sample or test record.
- **Documented:** a process or judgment is described in an artifact.
- **Proposed:** a control or future process is designed but not implemented.
- **Not tested / not run:** no effectiveness result is claimed.
- **Synthetic:** examples are authored for practice rather than drawn from a production client.
- **Source-derived:** the relevant external source is identified and the precise scope of comparison is stated.

The map explains conceptual relationships. It does not imply shared datasets, production integration, independent adjudication, professional client engagements, or operating effectiveness.
