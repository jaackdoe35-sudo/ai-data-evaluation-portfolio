# Project 5 — Search and Content Relevance Evaluation

## Purpose
A practical, self-directed sample of search-result evaluation. Each case includes a user query, inferred intent type, result title and snippet, relevance grade, and concise rationale.

## Relevance scale
- **3 — Highly relevant:** directly satisfies the dominant intent with a strong match.
- **2 — Relevant:** useful and substantially on-topic, but incomplete or less direct.
- **1 — Marginally relevant:** shares a topic or entity but only weakly supports the likely task.
- **0 — Not relevant:** does not satisfy the query's intent, is misleading, or is off-topic.

## Evaluation protocol
1. Read the query and identify its likely intent: informational, navigational, transactional, or local.
2. Identify the key entity, action, constraints, and requested attributes.
3. Assess the result title and snippet against the query—not merely shared keywords.
4. Assign a relevance grade using the scale above.
5. Record a rationale tied to visible evidence in the result.
6. Mark ambiguous cases for review rather than inventing missing context.

## Dataset
The CSV contains 20 synthetic query-result examples. It includes direct matches, partial matches, keyword overlap without intent satisfaction, and off-topic results. Labels and rationales are author-created practice judgments, not externally adjudicated ground truth.

## QA
The dataset is checked for unique IDs, populated fields, valid intent types and grades, and non-empty rationales. The included summary reports the distribution of grades and intent types.

## Limitations
This is a small synthetic practice exercise. It does not use live search-engine results, measure ranking quality, establish inter-rater agreement, or demonstrate production search-evaluator performance. A real evaluation task may supply a different relevance scale, locale, freshness requirement, or policy; follow the task-specific rubric over this sample protocol.
