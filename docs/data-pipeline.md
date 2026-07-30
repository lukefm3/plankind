# Demonstration data pipeline

## Purpose

The public Resilience Monitor demonstrates how PlanKind can turn an external
data source into a maintained decision-support product.

## Source

FEMA OpenFEMA Disaster Declarations Summaries API.

## Flow

1. GitHub Actions starts the workflow daily or on demand.
2. R requests recent declarations from OpenFEMA.
3. `clean_fema_data()` selects and standardizes publication fields.
4. Validation checks dates, required fields, and record counts.
5. Clean CSV and JSON files are saved to `processed_data/`.
6. Publication copies are written to `website/data/`.
7. GitHub Pages deploys the complete `website/` directory.

## Adaptation

Change the source and parsing logic while preserving explicit validation,
metadata, reproducible outputs, and documentation.

