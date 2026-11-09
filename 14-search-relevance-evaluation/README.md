# Project 14 — Search and Content Relevance Evaluation

**Work type:** self-directed search-judgment exercise  
**Status:** completed synthetic practice sample  
**Dataset:** 20 synthetic query-result examples  
**Scale:** four relevance grades (0–3)

## Executive summary

This sample demonstrates query-intent interpretation and evidence-based relevance grading. Each case contains a query, an intent category, a result title and snippet, a relevance grade, and a concise rationale. The protocol evaluates whether the result satisfies the likely task—not merely whether it repeats the query's keywords.

## Evaluation problem

Search evaluation requires identifying the user's underlying intent and comparing the visible result evidence against the requested entity, action and constraints. A result may share keywords with a query while failing its actual purpose; conversely, a useful result may use different wording while satisfying the intent.

## Data and scope

The CSV contains 20 synthetic query-result examples authored for this portfolio. It includes direct matches, partial matches, keyword overlap without intent satisfaction, and off-topic results. Labels and rationales are author-created practice judgments, not externally adjudicated ground truth.

The exercise does not use live search-engine results or represent a commercial search-quality benchmark.

## Method

1. Read the query and identify its likely intent: informational, navigational, transactional or local.
2. Identify the key entity, action, constraints and requested attributes.
3. Assess the result title and snippet against the query—not merely shared keywords.
4. Assign a relevance grade using the documented scale.
5. Record a rationale tied to visible evidence in the result.
6. Mark ambiguous cases for review rather than inventing missing context.
7. Run the documented schema checks for unique IDs, populated fields, allowed intent types/grades and non-empty rationales.

## Relevance scale

- **3 — Highly relevant:** directly satisfies the dominant intent with a strong match.
- **2 — Relevant:** useful and substantially on-topic, but incomplete or less direct.
- **1 — Marginally relevant:** shares a topic or entity but only weakly supports the likely task.
- **0 — Not relevant:** does not satisfy the query's intent, is misleading, or is off-topic.

## Decision quality considerations

A sound relevance judgment separates topical similarity from task satisfaction, respects explicit constraints, and explains which part of the title/snippet supports the grade. Locale, freshness, transactional availability and local context can materially change a judgment; a real task's supplied rubric and evaluation date take precedence over this practice scale.

## Deliverables and QA

- [20-case dataset](search_relevance_dataset.csv)
- [Summary and QA report](qa_summary.md)

The schema checks establish structural completeness only. They do not independently validate the relevance labels or establish agreement between evaluators.

## Limitations and evidence boundary

This is a small synthetic practice exercise. It does not use live search-engine results, measure ranking quality, establish inter-rater agreement, or demonstrate production search-evaluator performance. A real evaluation task may supply a different relevance scale, locale, freshness requirement or policy; follow the task-specific rubric over this sample protocol.

## Next validation that would strengthen the work

Use a dated sample of real, permitted search-result pages; preserve query locale, result position, timestamp and visible snippet; define intent and relevance anchors before rating; and obtain independent second-rater judgments for a subset. Report agreement and adjudication separately from simple schema validation.
