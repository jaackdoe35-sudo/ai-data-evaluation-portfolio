# 17 — Audio Transcription and Annotation

<badge>IN PROGRESS — sample not yet completed</badge>

## Objective

Demonstrate human transcription and audio annotation using a real, appropriately licensed recording. This project must replace the constructed-text transcription-formatting example in the portfolio as evidence of audio work.

## Source selected

- Dataset: Mozilla Common Voice Scripted Speech 27.0 — Nigerian Pidgin English
- Dataset locale: `pcm`
- Task: Automatic speech recognition (ASR) source data; this portfolio exercise is a human transcription and quality-review task
- Format: MP3
- Published dataset size: 282.78 MB
- Dataset licence: CC0-1.0
- Catalogue: [Mozilla Common Voice datasets](https://mozilladatacollective.com/organization/cmfh0j9o10006ns07jq45h7xk)
- Release metadata: [Common Voice dataset release repository](https://github.com/common-voice/cv-dataset)

The dataset catalogue identifies this release as CC0-1.0. Common Voice restrictions prohibit attempting to identify speakers and re-hosting or re-sharing the dataset. The portfolio will link to the source and will not upload or redistribute the original audio.

## Sample selection record

Do not claim a completed transcription until an individual clip has been selected and listened to.

| Field | Value |
|---|---|
| Dataset release | Common Voice Scripted Speech 27.0 |
| Locale | Nigerian Pidgin English (`pcm`) |
| Clip identifier | Pending selection |
| Source metadata row | Pending selection |
| Audio duration | Pending measurement |
| Reference transcript | Keep hidden until independent transcription is complete |
| Annotator transcript | Pending |
| Review status | Not started |

## Annotation protocol

1. Record the source dataset, release, clip identifier and applicable licence/usage restrictions.
2. Listen to the selected clip without opening or reading its reference transcript.
3. Produce a verbatim transcript, preserving the words actually spoken.
4. Mark uncertain or unintelligible spans explicitly; do not silently guess.
5. Add timestamps for meaningful segments. Do not claim word-level timestamp precision unless it has been measured.
6. Record speaker changes only when clearly audible. Use neutral labels such as Speaker 1; do not infer identity or demographics.
7. Save the independent transcript before consulting the dataset reference.
8. Compare against the reference and categorize differences: substitution, deletion, insertion, spelling/convention, or genuinely ambiguous audio.
9. Complete a second listening pass and document corrections.
10. Report limitations, including read-speech characteristics and any language/dialect uncertainty.

## Annotation schema

| Field | Description |
|---|---|
| clip_id | Source clip identifier |
| start_time | Segment start timestamp |
| end_time | Segment end timestamp |
| speaker_label | Neutral sequential label, only if distinguishable |
| transcript | Verbatim words for the segment |
| uncertainty_flag | None / uncertain / unintelligible |
| event_tag | Speech / non-speech vocalization / relevant sound |
| reviewer_note | Evidence-based note for a correction or ambiguity |

## Quality review

The completed report should include:

- Independent transcript and reviewed transcript
- Reference comparison performed only after the independent transcript was saved
- Word error rate (WER), where reference-tokenization conventions make it meaningful
- Substitution, deletion and insertion counts
- Timestamp and speaker-label consistency checks
- Uncertainty and unintelligible-span review
- Short error analysis with examples
- Explicit limitations; no claims of professional throughput or independent inter-annotator agreement

## Evidence boundary

This project is a self-directed practice exercise. It is not paid client work, production transcription, an independent benchmark, or proof of proficiency in every Nigerian language variety.

**Current status:** Source dataset and licence selected. No clip has yet been independently transcribed or quality-checked.