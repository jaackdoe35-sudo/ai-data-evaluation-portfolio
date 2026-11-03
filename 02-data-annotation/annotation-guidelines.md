# Text Annotation Guidelines

**Task:** Label short synthetic customer-style messages by primary intent and sentiment.

## Unit of annotation

One row is one complete message. Assign one primary intent and one sentiment label. Use the message's expressed purpose and tone, not assumptions about the writer's identity or circumstances.

## Intent labels

| Label | Definition | Example signal |
|---|---|---|
| `billing` | Payment, invoice, charge, refund, or subscription-cost question | “Why was I charged twice?” |
| `technical_support` | Product malfunction, error, access issue, or troubleshooting request | “The app crashes on launch.” |
| `account_access` | Login, password reset, verification, or account access | “I cannot sign in.” |
| `cancellation` | Request to stop or cancel a service/order | “Please cancel my plan.” |
| `shipping` | Delivery status, tracking, address for delivery, or late shipment | “Where is my parcel?” |
| `product_information` | Product features, compatibility, availability, or usage information | “Does it support offline mode?” |
| `feedback` | General praise, criticism, or suggestion not primarily requesting support | “The new layout is easier to use.” |
| `other` | Message does not fit the above or is too vague to classify | “Just checking in.” |

Choose the most actionable primary intent. If two intents appear, choose the one that represents the main requested action and note ambiguity in the rationale where necessary.

## Sentiment labels

- `positive`: clear satisfaction, gratitude, praise, or enthusiasm.
- `neutral`: factual inquiry or request without clear positive or negative emotion.
- `negative`: frustration, dissatisfaction, complaint, or distress.
- `mixed`: both positive and negative sentiment are clearly expressed.

Sentiment describes the wording, not whether the customer is objectively right.

## Annotation procedure

1. Read the full message once without labeling.
2. Identify the main requested action or communicative purpose.
3. Select the best-fitting intent using the definitions above.
4. Assign sentiment based on explicit language.
5. Write a short rationale tied to the text.
6. If genuinely ambiguous, use `other` or `mixed` as appropriate and explain why. Do not invent missing context.

## Quality rules

- Do not infer demographic traits, identity, location, or intent beyond the message.
- Do not label a neutral request as negative merely because it concerns a problem.
- A complaint about a failed service is usually negative even if politely phrased.
- A thank-you message can be positive even without a request.
- Use one primary label per field; do not create new labels ad hoc.
- Preserve the original message text exactly in the dataset.
