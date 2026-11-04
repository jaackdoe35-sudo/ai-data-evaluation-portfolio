# Portfolio website

This is the public presentation layer for the AI Data Annotation & Evaluation portfolio.

## Design and behavior

- Responsive, mobile-first single-page site.
- Hybrid visual identity: dark editorial hero and demonstration area, warm neutral case-study sections, forest-green closing section.
- Includes a self-contained response-evaluation interaction using a synthetic policy example.
- Uses no external JavaScript libraries, fonts, analytics, tracking pixels, image dependencies or backend.
- Honors reduced-motion preferences and uses semantic landmarks, keyboard-operable controls and accessible labels.

## Evidence policy

All portfolio samples are synthetic and self-directed. The website links to the repository as the authoritative evidence source. It does not claim paid client experience, independent benchmark performance, production readiness or independent annotator agreement.

## Deployment

The GitHub Actions workflow at `.github/workflows/pages.yml` publishes the repository root to GitHub Pages when changes to `index.html` or the workflow are pushed to `main`, or when manually dispatched. The repository's Pages build/deployment setting may need to be configured to use GitHub Actions. A successful workflow run and a reachable Pages URL must be verified before claiming the site is live.

No custom domain or paid hosting is required.
