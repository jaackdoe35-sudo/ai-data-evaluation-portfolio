# 19 — Video Transcript Annotation and Caption QA

**Status: 22-cue transcript sample validated against NASA's official SRT; audio/video verification not performed.**

## Selected video

**Apollo 11: This Is Goddard** — NASA Goddard Space Flight Center, released July 31, 2019.

- [Official NASA video and resource page](https://svs.gsfc.nasa.gov/13270)
- [Direct WebM video file](https://svs.gsfc.nasa.gov/vis/a010000/a013200/a013270/Apollo11.webm) — 154.4 MB, 1920 × 1080
- [Official SRT caption file](https://svs.gsfc.nasa.gov/vis/a010000/a013200/a013270/Apollo11.en_US.srt)
- [Official WebVTT caption file](https://svs.gsfc.nasa.gov/vis/a010000/a013200/a013270/Apollo11.en_US.vtt)
- Source credit: NASA's Goddard Space Flight Center.

NASA states that its content is generally not subject to copyright in the United States and may be used for educational or informational purposes, subject to its media guidelines and third-party-material exceptions. See [NASA media usage guidelines](https://www.nasa.gov/nasa-brand-center/images-and-media/). This portfolio exercise does not imply NASA endorsement.

## Sample contents

- [`caption-sample.json`](./caption-sample.json): 22 source-attributed caption cues with IDs, timestamps, text, speaker labels where supplied, cue classifications and QA notes.
- The excerpt covers 00:00:00–00:01:31.960 of the official SRT.

## Annotation scope

This is **video-transcript / caption annotation**, not visual object tracking. The sample is derived from NASA's published SRT. Source wording is preserved rather than silently corrected.

Review dimensions:
1. Timestamp syntax and chronological order.
2. Cue segmentation and readability.
3. Speaker-label consistency where labels are present in the source.
4. Classification of on-screen text versus speech.
5. Source-caption irregularities flagged without inventing corrections.

## Evidence boundary

The official NASA SRT was opened and compared cue-by-cue with all 22 sample records. Cue IDs, start/end timestamps and caption wording match the source excerpt. Source speaker prefixes (for example, `JFK:` and `NARRATOR:`) are represented in separate `speaker` fields where present. The video file itself was not downloaded or uploaded into the GitHub repository, and has not been independently listened to or visually reviewed. The source video remains directly downloadable from NASA using the link above.

Therefore:
- Caption wording is source-derived, not independently transcribed.
- Audio-to-caption accuracy is unverified.
- Speaker identity and visual text are retained from the source captions, not independently confirmed.
- This sample does not establish professional production experience or independent transcription accuracy.

## Reproducibility

Use the official NASA resource page and caption links above to retrieve the source media. The 22-cue excerpt was checked against the SRT source; the comparison covers cue IDs, timestamps and caption wording. The repository stores the compact annotation sample and links to NASA's original video rather than redistributing the 154.4 MB binary.
