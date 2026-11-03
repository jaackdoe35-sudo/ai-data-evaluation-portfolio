# Paired Response Evaluation Methodology

## Objective
Choose the stronger of two candidate responses to the same prompt. Every preference must be supported by evidence from the prompt, supplied source text, and candidate responses.

## Dimensions
Score each candidate from 1 to 5:
1. Factuality — claims are correct and supported; no invented details.
2. Instruction-following — explicit format, scope, audience, and output constraints are met.
3. Completeness — material information and caveats are included.
4. Clarity — understandable, direct, and unambiguous.
5. Safety and judgment — safety, privacy, authorization, and uncertainty are handled appropriately.

Scale: 1 severe failure; 2 substantial failure; 3 partial; 4 minor limitation; 5 fully meets criterion.

## Decision procedure
1. Extract the prompt's explicit requirements.
2. Identify the factual ground truth supplied in the prompt.
3. Evaluate A and B independently before comparing them.
4. Identify the most consequential difference.
5. Choose A, B, or Tie if neither is meaningfully better.
6. State the decisive evidence.
7. Record confidence from 1 (low) to 5 (high).

A critical safety or privacy failure can outweigh several stylistic advantages. Do not mechanically select the higher arithmetic mean if it contains a serious high-impact defect.

## Actionable feedback
Good feedback identifies the exact claim, omission, or instruction that caused the issue; explains why it matters; and states what a corrected response should do. Avoid vague comments such as “A is better.”

## Calibration limitations
This is a synthetic, single-author practice challenge. The key is not independently validated. Real evaluator reliability requires multiple independent raters, adjudication, and an appropriate agreement statistic.