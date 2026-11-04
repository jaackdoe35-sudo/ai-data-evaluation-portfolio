# 19 — Video Transcript Annotation and Caption QA

**Status: source and transcript verified; sample is caption-derived and not audio-verified.**

## Selected video

**Apollo 11: This Is Goddard** — NASA Goddard Space Flight Center, released July 31, 2019.

- [Official NASA video and resource page](https://svs.gsfc.nasa.gov/13270)
- [Direct WebM video file](https://svs.gsfc.nasa.gov/vis/a010000/a013200/a013270/Apollo11.webm) — 154.4 MB, 1920 × 1080
- [Official SRT caption file](https://svs.gsfc.nasa.gov/vis/a010000/a013200/a013270/Apollo11.en_US.srt)
- [Official WebVTT caption file](https://svs.gsfc.nasa.gov/vis/a010000/a013200/a013270/Apollo11.en_US.vtt)
- Duration: source page identifies the work as a 1969 documentary; the supplied SRT runs beyond the first minute and contains timed captions.
- Source credit: NASA's Goddard Space Flight Center.

NASA states that its content is generally not subject to copyright in the United States and may be used for educational or informational purposes, subject to its media guidelines and third-party-material exceptions. This page credits NASA Goddard Space Flight Center. The portfolio sample is an educational, factual annotation exercise and does not imply NASA endorsement. See [NASA media usage guidelines](https://www.nasa.gov/nasa-brand-center/images-and-media/).

## Sample contents

- `caption-sample.json`: a short, source-attributed excerpt of the official SRT, preserving cue IDs, timestamps, speaker labels and non-speech descriptions.
- `README.md`: annotation scope, QA checks and evidence limitations.

## Annotation scope

This is **video-transcript / caption annotation**, not visual object tracking. The text is taken from NASA's published caption file. The sample preserves source wording rather than silently correcting it.

Review dimensions:
1. Timestamp syntax and chronological order.
2. Cue segmentation and readability.
3. Speaker-label consistency where labels are present in the source.
4. Treatment of non-speech descriptions such as `[cheering in Goddard control room]`.
5. Uncertainty and possible source-caption defects flagged without inventing corrections.

## Evidence boundary

The official NASA page lists the video and downloadable SRT/VTT captions and states that a complete transcript is available. The SRT content was inspected directly. The video has **not** been independently listened to or visually reviewed in this workflow. Therefore:
- Caption wording is source-derived, not independently transcribed.
- Audio-to-caption accuracy is unverified.
- Speaker identity and sound-event labels are retained from the source captions, not independently confirmed.
- This sample does not establish professional production experience or independent transcription accuracy.

## Reproducibility

Use the official NASA resource page and caption links above to retrieve the source material. The original recording remains hosted by NASA; this repository links to the source rather than redistributing the 154.4 MB video binary.
