---
name: TD-13 Organisation filter disabled by a hardcoded flag
type: tech_debt
schema_version: 1
aliases:
- TD-13
summary: SHOW_ORG_FILTER = false in app/contribute/ContributeGrid.tsx hides a fully built organisation
  filter on the Contribute grid for everyone.
tags:
- dead-code
- feature-flag
td_id: TD-13
severity: P3
status: open
affected_modules:
- app-contribute-contribute-grid
remediation: Turn it on behind a real feature-flag mechanism, or remove the dead branch.
code_refs:
- app/contribute/ContributeGrid.tsx#L44
- app/contribute/ContributeGrid.tsx#L223
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
  ref: app/contribute/ContributeGrid.tsx
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

The org filter was added on 2026-08-25 (`d567527`). On 2026-09-11 it was hidden ("Contribute home: only pathways I've joined, filter hidden", `0abaa04`). At `28068b6` line 44 still reads `const SHOW_ORG_FILTER = false;`, and the render branch at line 223 is gated on it.

## Impact

A finished feature sits unreachable, and no record says why it was hidden.

## Remediation

Decide, then either enable or delete it.
