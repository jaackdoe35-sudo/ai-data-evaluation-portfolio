# Portfolio website

This is the public presentation layer for Patrick Tobe's AI Data Annotation & Evaluation portfolio.

## Design and behavior

- Responsive, mobile-first, single-page recruiter portfolio.
- Clear name, target roles, strongest work samples and direct contact are visible without navigating away.
- Forest-green and warm-neutral visual system with a dark editorial hero and evidence snapshot.
- Nine focused sample links connect the landing page to the underlying GitHub materials.
- Includes a keyboard-operable response-evaluation exercise with immediate explanatory feedback.
- Uses no external JavaScript libraries, web fonts, analytics, tracking pixels, image dependencies or backend.
- Includes semantic landmarks, a skip link, visible keyboard focus and reduced-motion support.

## Evidence policy

Practice examples are self-directed. Datasets are synthetic except the caption exercise, which is based on a published NASA SRT. The page does not claim paid client work, independent benchmark performance, independent annotator agreement, production throughput or audio/video verification of the caption sample. The repository is the source of truth for full samples and limitations.

## Deployment

The production site is hosted by the Vercel project `ai-evaluation-lab` at:

- https://ai-evaluation-lab-three.vercel.app

The current production deployment was created from an inline source upload and verified as READY. Vercel's Git integration is **not connected** to this repository, so pushes to GitHub do not automatically deploy this Vercel project. Vercel SSO protection has been disabled to allow public recruiter access.

The repository also contains an optional GitHub Pages workflow at `.github/workflows/pages.yml`. It is not the active production deployment path; GitHub Pages availability and configuration must be checked separately before using it.

No custom domain or paid hosting is required.
