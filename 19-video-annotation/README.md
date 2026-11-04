# 19 — Video Annotation and Temporal Event Review

**Status: in development — source and file-level licence verified; frame annotations not completed**

## Selected source

[Tochi speaking Nigerian Pidgin.webm](https://commons.wikimedia.org/wiki/File:Tochi_speaking_Nigerian_Pidgin.webm), donated by Wikitongues through its oral-histories project.

- Duration: 3 minutes 21 seconds
- Format: WebM (VP9 video / Opus audio)
- Dimensions: 1920 × 1080
- File-page licence: CC0 1.0 Universal Public Domain Dedication

The individual file page is the rights reference. The media has not yet been downloaded or inspected frame by frame in this workflow.

## Planned annotation schema

| Field | Description |
|---|---|
| video_id | Stable source identifier |
| start_time / end_time | Clip and event boundaries in seconds |
| frame_time | Timestamp of sampled frame |
| track_id | Stable ID for a visible object across frames |
| category | Controlled visible-object label |
| bbox | Frame-level pixel coordinates |
| action_or_event | Observable event, if any |
| scene_change | Yes/no with timestamp |
| uncertainty_flag | Unclear boundaries or object continuity |
| reviewer_note | Evidence-based QA note |

## Quality protocol

1. Record exact source, licence, dimensions, frame rate and excerpt.
2. Document the frame-sampling interval.
3. Maintain track IDs only while visual continuity is supported.
4. Mark entry, exit, occlusion and scene changes at measured timestamps.
5. Validate boxes against frame dimensions.
6. Review temporal order, ID switches, missed objects and unsupported action labels.
7. State that sparse frame sampling is not continuous motion tracking.

## Evidence boundary

The source page and CC0 licence are verified. No frames have been inspected and no timestamped object/event annotations have been produced. This is a sourced protocol, not a completed video-annotation sample.
