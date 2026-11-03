# Annotation Quality Assurance Report

**Dataset reviewed:** `02-data-annotation/annotated-dataset.csv`  
**Rows expected:** 50 synthetic messages

## Structural checks

- Data rows: **50**
- Unique IDs: **50**
- Required fields populated: **50/50 rows**
- Intent labels used: **8**
- Sentiment labels used: **4**
- Duplicate message IDs: **0**

## Label distribution

### Intent
- `account_access`: 7
- `billing`: 9
- `cancellation`: 5
- `feedback`: 8
- `other`: 1
- `product_information`: 6
- `shipping`: 7
- `technical_support`: 7

### Sentiment
- `mixed`: 3
- `negative`: 20
- `neutral`: 21
- `positive`: 6

## Manual consistency review

The dataset was authored against the definitions in `annotation-guidelines.md`. The following boundary decisions were applied:

- Price, invoice, payment, and charge questions use `billing`.
- Login, password, and verification-code problems use `account_access`.
- Malfunction and error reports use `technical_support`.
- Delivery tracking and arrival questions use `shipping`.
- Clear praise plus criticism uses `mixed` sentiment.
- The row with an unspecified “message” is labeled `other` because the content does not support a more specific intent.

## Limitations

This is a self-review of a synthetic dataset by one annotator. The structural counts can be checked mechanically, but the labels have not been independently adjudicated. No inter-annotator agreement score is claimed. A production workflow should add a second annotator, blinded review, adjudication of disagreements, and periodic guideline updates.

## QA outcome

The dataset contains 50 unique, fully populated rows with labels drawn from the documented schema. This establishes structural completeness, not proof that every subjective label is objectively correct.
