# AI Impact Assessment — TalentScreen (fictional)

**Status:** Draft qualitative assessment; not independently reviewed. No real system, data or affected person is involved.

## Context
TalentScreen extracts candidate information and prioritizes applications for recruiter review. Although it is not intended to make final hiring decisions, rankings can influence attention and access to employment.

## Stakeholders and potential impacts
| Stakeholder | Potential benefit | Potential harm / evidence question |
|---|---|---|
| Applicants | Consistent handling, faster review | Unfair ranking, inaccurate extraction, privacy loss; how can errors be challenged? |
| Recruiters | Reduced repetitive review | Automation bias; can source evidence be inspected and outputs overridden? |
| Hiring managers | Structured candidate information | False confidence; what criteria are actually job-related? |
| Organization | Efficiency and traceability | Discrimination, legal, security and reputational exposure |
| Vendors | Clear service requirements | Unclear processing, subprocessors, model changes and data reuse |

## Risk pathways
- **Fairness:** historical patterns, proxies, missingness and feature choices may disadvantage groups. No cohort or outcome data exists.
- **Validity:** parsing errors, CV format variation and unsupported inference may distort candidate profiles.
- **Privacy:** purpose, lawful basis, minimization, access, retention and deletion require jurisdiction-specific assessment.
- **Oversight:** formal human sign-off may mask over-reliance. Review must be informed and capable of changing outcomes.
- **Transparency:** applicants and recruiters may need notice, source traceability and correction routes.
- **Security:** malicious files, compromised integrations, excessive access or prompt injection may manipulate outputs or expose data.
- **Lifecycle:** changes to job criteria, populations, model versions or vendor terms can invalidate prior evaluation.

## Required mitigations before deployment
1. Confirm purpose, jurisdictions and provider/deployer roles.
2. Complete privacy and rights-impact work where required.
3. Inventory features and data sources; prohibit unapproved proxies and protected-trait inference.
4. Define representative evaluation, error analysis and acceptance criteria.
5. Require source-linked explanations, uncertainty, reviewer training, override and escalation.
6. Provide appropriate applicant transparency and correction routes.
7. Complete security threat modelling, access reviews and vendor due diligence.
8. Establish monitoring thresholds, revalidation and pause authority.

## Unknowns
Jurisdiction, legal entity, model, provider, source data, feature list, thresholds, retention, notice, vendor terms, reviewer workflow and performance dataset are unspecified. These are blocking unknowns, not blanks to infer.

**Outcome:** potentially elevated inherent impact; residual risk not assessed. This is not a formal rating, legal classification or deployment approval.
