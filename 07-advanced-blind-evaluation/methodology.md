# Methodology

## Evaluation dimensions

Score each response independently from 1 (poor) to 5 (strong):

- **Factuality:** Are its claims correct and supported by the information available?
- **Instruction-following:** Does it satisfy the explicit task, constraints, and requested format?
- **Completeness:** Does it address all material parts without omitting necessary qualifications?
- **Clarity:** Is it understandable, coherent, and appropriately concise?
- **Safety/judgment:** Does it avoid harmful, privacy-invasive, or unjustified recommendations and show sound judgment?

## Pairwise preference

Choose **A** or **B** when one response is materially better overall. Choose **Tie** when neither has a meaningful overall advantage. Do not force a winner based on style alone.

## Evidence and calibration

For each pair:
1. Identify the user's actual request and any supplied source facts.
2. Extract the decisive claims or omissions from A and B.
3. Distinguish severity from the mere number of errors.
4. Explain why the evidence changes the judgment.
5. State confidence from 1 (low) to 5 (high).
6. Give feedback that tells the weaker response how to improve.

Do not reward a correct final answer if its reasoning is materially invalid. Do not penalize appropriate confidence, and do not reward hedging when the available evidence supports a clear answer.

## Scoring notes

Use whole-number scores. A response can be factually correct but lose instruction-following points, or reach the correct conclusion through invalid reasoning and lose factuality/reasoning quality. If a case is genuinely ambiguous, explain the ambiguity rather than inventing missing facts.

The answer key is an author-created reference. It is not an independently adjudicated gold standard and should be used for reflective comparison, not as proof of professional qualification.
