# Data Governance and Lineage — TalentScreen (fictional)

**Status:** Proposed conceptual design. No actual source, integration, data flow or retention configuration was inspected.

## Illustrative flow
1. Applicant CVs/forms and employer job descriptions/criteria are identified as possible sources.
2. Ingestion validates files, scans for malware, parses formats and assigns source identifiers.
3. Extraction stores structured values with exact source-span references and uncertainty markers.
4. Normalization follows documented rules while retaining the original source.
5. Matching compares extracted facts with approved job-related criteria and records criteria version.
6. Output includes summary, criterion-level evidence, missing fields and a review queue.
7. Recruiter inspects sources, corrects errors and makes consequential decisions.
8. Retention/deletion follows a documented lawful purpose, schedule, legal holds and jurisdictional requirements.

## Required metadata
For each field: purpose, source, collection method, legal basis assessment, sensitivity, transformation, quality rule, permitted users, recipients, retention, deletion trigger, lineage pointer and accountable owner. Unknowns remain unknown.

## Proposed controls
- Preserve immutable source-document references and distinguish extracted values from corrections.
- Link every material summary claim to source text or mark it unavailable.
- Do not infer qualifications, identity, protected traits or intent from ambiguous content.
- Define schema, null semantics, locale/date handling and duplicate rules.
- Test format, language and accessibility-related variation.
- Record dataset version, sampling, exclusions, label provenance and agreement limitations.
- Apply least privilege, strong authentication, controlled exports, encryption, access logging and periodic access review.
- Set retention only after legal/purpose assessment; test deletion and backup expiry.

## Evidence required
Approved data inventory, source notices/contracts, legal basis, data-flow diagram, dataset documentation, lineage and quality tests, access logs, retention/deletion evidence, vendor terms and version/change history.

**Conclusion:** this is a proposed data flow; no actual lineage, lawful basis or data quality has been verified.
