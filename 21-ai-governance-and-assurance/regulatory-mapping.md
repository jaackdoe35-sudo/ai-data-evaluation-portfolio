# Regulatory Issue Map — TalentScreen (Fictional Recruitment AI)

**Review date:** 9 November 2026  
**Status:** preliminary, conditional issue analysis; not legal advice or a legal applicability determination.  
**Scenario:** TalentScreen is fictional. It is assumed to extract application information, compare it with role criteria and prioritize a recruiter review queue. No legal entity, provider, deployer, model, deployment geography, applicant location or actual decision impact is specified.

## 1. Decision-first applicability analysis

Do not start by assuming that every recruitment tool is legally high-risk. Establish these facts first:

1. Does the software meet the applicable legal definition of an AI system?
2. What is the provider's documented intended purpose, and what does the system actually do?
3. Where is it placed on the market, put into service or used, and whose data/decisions are affected?
4. Who is the provider, deployer, importer, distributor or other relevant operator?
5. Does the system filter, score, rank, recommend, reject or otherwise materially influence candidate selection?
6. Does it profile natural persons, and can a human reviewer genuinely understand, challenge and override the output?
7. Which employment, equality, privacy, data-protection and automated-decision rules apply in each relevant jurisdiction?

Until those facts are known, the legal status is **UNDETERMINED**. A label such as "decision support" or "human in the loop" is not enough to resolve classification.

## 2. EU AI Act — conditional recruitment classification

### 2.1 Relevant use case

Annex III, point 4(a) lists AI systems intended for recruitment or selection of natural persons, including systems used to place targeted job advertisements, analyse/filter applications or evaluate candidates.

The Commission's AI Act Service Desk employment examples describe automated job-matching and ranking systems used to filter and shortlist candidates as high-risk where their rankings serve as a primary decision input, even where recruiters retain discretion.

**TalentScreen issue:** the fictional system prioritizes a human review queue. That description creates a material Annex III, point 4(a) classification question. It does not, by itself, establish whether the ranking materially influences selection, whether the system profiles people, or whether the system falls within the Act's territorial scope.

### 2.2 Article 6(3) filter

For an Annex III system, Article 6(3) provides a limited route for not treating it as high-risk where it does not pose a significant risk of harm to health, safety or fundamental rights, including because it does not materially influence decision-making, and one of the listed conditions is met (for example, a narrow procedural or preparatory task).

However, an Annex III system that performs profiling of natural persons remains high-risk under Article 6(3). A provider relying on the non-high-risk route must document its assessment before placing the system on the market or putting it into service and comply with the applicable registration provision.

**Assessment for this fictional case:** no exception is claimed. A queue-prioritization tool could be merely preparatory in some designs, but if ranking materially determines which candidates are seen or advances/excludes them, the exception may not be available. The actual workflow and profiling question must be established.

### 2.3 Application dates — amended Article 113

The European Commission AI Act Service Desk's consolidated text, based on the AI Act as amended by the Digital Omnibus on AI and current to 27 July 2026, states that:
- the Regulation generally applies from 2 August 2026, subject to staged provisions;
- Chapter III, Sections 1, 2 and 3 for Annex III high-risk systems apply from **2 December 2027**;
- Chapter III, Sections 1, 2 and 3 for Annex I high-risk systems apply from **2 August 2028**.

For the assumed Annex III recruitment use case, 2 December 2027 is the relevant scheduled application date for those high-risk provisions under the consolidated Article 113 text. This is a date statement, not a conclusion that TalentScreen is in scope. Recheck the authentic Official Journal text and amendments before relying on it for a live legal decision.

### 2.4 Potential obligations if the system is in scope and classified high-risk

The following are issue areas to assess, not findings that the fictional system currently breaches or satisfies the Act:

| Provision | Subject | Governance/control evidence to request | Related portfolio artifacts |
|---|---|---|---|
| Article 9 | Risk-management system | Lifecycle risk process, identified risks, testing, mitigation and review records | risk-register.csv; risk-methodology.md; remediation-tracker.csv |
| Article 10 | Data and data governance | Training/validation/testing data governance, relevance, representativeness, bias detection and mitigation records | data-governance-and-lineage.md; C-003; TP-003/006 |
| Article 11 and Annex IV | Technical documentation | Provider technical documentation appropriate to the system and required information | system-inventory.csv; C-007 |
| Article 12 | Record-keeping | Logging capability and relevant event records | C-008; TP-008 |
| Article 13 | Transparency and information to deployers | Instructions for use and information needed by deployers | C-007; human-oversight.md |
| Article 14 | Human oversight | Design measures enabling oversight, understanding, intervention and safe use | human-oversight.md; C-005; TP-005 |
| Article 15 | Accuracy, robustness and cybersecurity | Appropriate performance, robustness and cybersecurity evidence | C-006/C-009; TP-006/009 |
| Article 26 | Deployer obligations | Use according to instructions, assigned competent oversight, monitoring, input-data relevance, logs and workplace information duties where applicable | human-oversight.md; monitoring-plan.md; incident-response.md |
| Article 27 | Fundamental-rights impact assessment | Determine whether the deployer falls within the specified categories and whether the provision applies | impact-assessment.md; regulatory-mapping.md |

### 2.5 Article 27 is not an automatic requirement for every private employer

Article 27 applies to specified deployers of high-risk AI systems: bodies governed by public law, private entities providing public services, and deployers of certain Annex III systems identified in points 5(b) and 5(c), subject to the provision's terms and exceptions. A private employer using an Annex III, point 4(a) recruitment system is not automatically within Article 27 solely because it is a recruitment system.

Other fundamental-rights, data-protection, employment and equality assessments may still be required under other applicable law or governance policy. The actual deployer status and legal context must be checked.

## 3. Other legal regimes — jurisdiction-specific screening, not assumed applicability

| Legal area | Trigger questions | Evidence needed |
|---|---|---|
| Data protection/privacy | Where are controller/processor and affected applicants located? What personal data, purposes, lawful basis, retention, transfers and rights are involved? | Data map, privacy notices, records of processing, processor contracts, retention/deletion evidence, DPIA where required |
| Employment and equality | Which employment market and protected-class rules apply? Are criteria job-related and validated? Could proxies or disparate impact arise? | Job criteria, feature inventory, validation, subgroup analysis, accommodations, adverse-impact review and appeal process |
| Automated decision-making | Does the system make or materially support decisions with legal or similarly significant effects? What human intervention is meaningful? | Decision flow, authority matrix, override records, explanation and challenge route |
| Consumer/AI-specific laws | Is the tool within a jurisdiction's AI-specific law, and which actor obligations apply? | Jurisdiction, system purpose, actor role, classification and effective-date analysis |
| Contract and procurement | Is a third-party model/vendor involved? What audit, transparency, incident and change rights exist? | Contracts, SLAs, vendor due diligence, model documentation and change notifications |

No jurisdiction-specific conclusion is made for Nigeria, the United States, the United Kingdom, the EU or any other country because the fictional system has no specified geography or legal entity. The candidate's physical location does not establish the fictional system's legal location.

## 4. Required regulatory decision record

A real assessment should record, at minimum:

| Field | Current fictional-case status |
|---|---|
| System provider and deployer | Unknown |
| Legal entities and establishment locations | Unknown |
| Market placement/use locations | Unknown |
| Intended purpose and actual workflow | High-level fictional description only |
| AI-system definition analysis | Not assessed |
| EU AI Act territorial-scope analysis | Not assessed |
| Annex III 4(a) analysis | Potentially relevant; not determined |
| Article 6(3) exception analysis | Not determined; profiling status unknown |
| Provider/deployer role allocation | Not determined |
| Article 27 deployer category | Not determined |
| Other employment/privacy/equality laws | Not assessed |
| Legal reviewer and approval | None |

## 5. Sources — primary/official

1. [EU AI Act Service Desk — Article 6](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6) — classification rules and Article 6(3).
2. [EU AI Act Service Desk — Annex III](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3) — point 4(a), recruitment and selection.
3. [EU AI Act Service Desk — Employment examples](https://ai-act-service-desk.ec.europa.eu/en/employment-0) — Commission examples on candidate ranking and selection.
4. [EU AI Act Service Desk — Article 26](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26) — deployer obligations.
5. [EU AI Act Service Desk — Article 27](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-27) — specified deployer categories for fundamental-rights impact assessments.
6. [EU AI Act Service Desk — Article 113](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113) — consolidated application dates; page notes the 27 July 2026 consolidated text.
7. [EUR-Lex consolidated AI Act text, 27 July 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727) — consult the authentic Official Journal acts for legal reliance.

## 6. Conclusion and review trigger

**Conclusion:** recruitment AI raises a significant conditional regulatory issue under EU AI Act Annex III, point 4(a), but the fictional facts do not support a final classification or applicability decision. The amended timeline for Annex III high-risk provisions is 2 December 2027 under the consolidated Article 113 text. Article 27's deployer scope must be tested separately; it is not automatically triggered for every private recruitment deployer.

Refresh this map whenever the system's intended purpose, ranking influence, profiling, provider/deployer role, geography, applicable law or legislative text changes. Obtain qualified legal review before treating this educational analysis as an organization's compliance position.

This document is an educational portfolio work sample, not legal advice.
