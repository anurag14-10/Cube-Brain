---
name: TD-09 ARCHITECTURE.md says the grid is chips, not a table
type: tech_debt
schema_version: 1
aliases:
- TD-09
summary: ARCHITECTURE.md still says density is 'rendered as status chips, not a table', while components/HeatmapGrid.tsx
  renders a literal <table>.
tags:
- docs
td_id: TD-09
severity: P2
status: open
affected_modules:
- components-heatmap-grid
remediation: Update ARCHITECTURE.md (glossary row for Density and the grid paragraph) to describe the
  Grid button + HeatmapGrid table modal.
code_refs:
- ARCHITECTURE.md#L82
- ARCHITECTURE.md#L477
- components/HeatmapGrid.tsx#L32
doc_refs:
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/wiki/diffusion-cube/knowledge/technical-debt.md
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: ARCHITECTURE.md
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

Verified at `28068b6`: `ARCHITECTURE.md` line 82 ("Rendered as status chips, not a table") and line 477 ("surfaced as four status chips and a Grid button, not a table") contradict `components/HeatmapGrid.tsx`, which renders `<table className="w-full border-collapse text-sm">`. The grid moved to a modal opened by a "Grid" button on 2026-08-31 (`fc24e3d`).

## Impact

The one document written to correct the stale `CLAUDE.md` has itself drifted on this detail.

## Remediation

Edit those two paragraphs.
