# 18 — Image Annotation and Visual Quality Review

<badge>PLANNED — no image annotated yet</badge>

## Objective

Demonstrate image annotation using a source image whose individual licence and reuse conditions can be verified.

## Planned task

A compact image-annotation case study will include:

- Image-level description grounded only in visible content
- Object/category labels
- Attributes such as colour, state and count where visually supportable
- Bounding boxes for clearly identifiable objects when useful
- Occlusion, truncation and ambiguity flags
- A QA pass for missed objects, duplicate boxes, invalid labels and unsupported descriptions

## Source and rights policy

Select an individual image from Wikimedia Commons or another source only after checking the exact file page, author, licence, attribution requirements, and any restrictions. Do not assume that every image on a platform has the same licence. Record the source URL and licence in the completed sample. If the licence requires attribution or share-alike terms, comply with them.

## Annotation schema

| Field | Description |
|---|---|
| image_id | Stable sample identifier |
| image_source | Exact source-file page |
| licence | Exact file-level licence |
| object_id | Unique object annotation ID |
| category | Controlled object label |
| bbox | Coordinates using a documented convention |
| attributes | Visible, task-relevant properties |
| occlusion | None / partial / substantial |
| truncation | Whether the object crosses the image boundary |
| confidence | Annotator confidence with defined scale |
| reviewer_note | Evidence-based ambiguity or QA note |

## Quality checks

- Bounding boxes use one documented coordinate convention.
- Boxes stay within image dimensions and have positive width and height.
- Labels come from the declared taxonomy.
- Duplicate or overlapping boxes are reviewed rather than automatically treated as errors.
- Descriptions do not infer identity, intent, relationships or hidden properties.
- Ambiguous and partially visible objects are flagged consistently.

## Evidence boundary

This is a planned project. No image has yet been selected, annotated or reviewed. It must not be presented as completed image-annotation experience until those steps are documented.