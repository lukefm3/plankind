# PlanKind Insights

Public website and demonstration data product for PlanKind, an evidence-based
planning, evaluation, and analytics practice.

## Structure

- `website/` - deployable static website
- `scripts/update_fema_data.R` - public-data collection and processing
- `processed_data/` - validated, publication-ready outputs
- `raw_data/` - intentionally excluded from version control
- `functions/` - reusable R functions
- `reports/` - report source files
- `graphics/` - generated figures and design assets
- `docs/` - technical and project documentation
- `.github/workflows/` - automated data refresh and GitHub Pages deployment

## Update the demonstration dashboard

```powershell
Rscript scripts/update_fema_data.R
```

The script downloads recent FEMA disaster declarations, validates them, writes
clean CSV/JSON outputs to `processed_data/`, and copies the publication files
into `website/data/`.

## Replace the data source

1. Change `source_url` in `scripts/update_fema_data.R`.
2. Update the parsing function in `functions/clean_fema_data.R`.
3. Keep the output schema aligned with `website/assets/dashboard.js`, or revise
   the JavaScript labels and column names.
4. Test locally and update `docs/data-pipeline.md`.

## Publish

This project is designed for a public repository named `plankind`. In GitHub,
enable **Settings > Pages > Source > GitHub Actions**. The website will be
available at `https://lukefm3.github.io/plankind/`.

