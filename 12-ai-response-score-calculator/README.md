# Project 12 — AI Response Evaluation Score Calculator

## Purpose
A small Python command-line tool that recalculates overall AI-response evaluation scores from the five dimensions in the portfolio rubric and generates a readable Markdown summary.

## What it does
- Checks for the required evaluation columns.
- Accepts integer ratings from 1 to 5 and `N/A` where a dimension genuinely cannot be assessed.
- Rejects duplicate IDs, invalid scores and invalid severity labels.
- Recalculates each response's arithmetic mean, excluding N/A dimensions.
- Summarizes mean scores by dimension and counts issue-severity categories.
- Writes a Markdown report with record-level results.

## Run
Requires Python 3 and uses only the standard library.

```bash
python score_calculator.py sample_evaluations.csv --output sample_summary.md
python -m unittest discover -s tests -v
```

## Sample result
The included five-record sample produces an overall mean of 4.00/5. See [sample summary](sample_summary.md).

## Limitations
The calculator verifies score format and performs arithmetic. It does not determine whether the evaluator's judgments are correct, validate factual claims in candidate responses, or replace the underlying prompt, response and evidence review. Severity is carried from the input rather than inferred by the tool.
