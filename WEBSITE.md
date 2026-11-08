# Portfolio website

This is the public presentation layer for Patrick Tobe's AI Data Annotation, Evaluation & Governance portfolio.

## Design and behavior
- Responsive, mobile-first, single-page recruiter portfolio.
- White editorial visual system with restrained blue accents, serif display headings and evidence snapshot.
- Eleven selected project links connect the landing page to repository work, including AI governance and LLM security evaluation.
- Includes a keyboard-operable response-evaluation exercise with immediate explanatory feedback.
- No external JavaScript libraries, web fonts, analytics, tracking pixels, image dependencies or backend.
- Semantic landmarks, skip link, visible keyboard focus and reduced-motion support.

## Evidence policy
Practice examples are self-directed. Datasets are synthetic except the caption exercise, which is based on a published NASA SRT. The page does not claim paid client work, independent benchmark performance, independent annotator agreement, production throughput or audio/video verification of the caption sample.

The AI governance case study is fictional and design-only. Proposed controls are not implemented or tested. The LLM security catalogue contains test specifications only; it has not been run against a live model. The repository is the source of truth for complete samples, evidence and limitations.

## Deployment
The production site is hosted by Vercel project `ai-evaluation-lab` under the Tobe team. Public domains:
- https://ai-evaluation-lab-three.vercel.app
- https://ai-evaluation-lab-tobe6.vercel.app

The active production deployment is created from the reviewed `index.html` in this repository using the connected Vercel deployment integration. The project is not assumed to have Git auto-deploy enabled; repository changes must be explicitly deployed and verified.

No custom domain or paid hosting is required.
