---
name: TD-11 Brand colours hardcoded in components
type: tech_debt
schema_version: 1
aliases:
- TD-11
summary: Brand hex colours are written literally in lib/dimensions.ts, components/AdoptionPlanModal.tsx
  and app/explore/ExploreLibrary.tsx instead of referencing the CSS tokens in app/globals.css.
tags:
- ui
- duplication
td_id: TD-11
severity: P3
status: open
affected_modules:
- lib-dimensions
- components-adoption-plan-modal
- app-explore-explore-library
remediation: Reference app/globals.css theme tokens from the two ordinary React components; the copies
  in lib/email.ts and lib/adoption-plan-pdf.ts are structurally necessary (outside the browser CSS pipeline).
code_refs:
- lib/dimensions.ts
- components/AdoptionPlanModal.tsx
- app/explore/ExploreLibrary.tsx
- app/globals.css
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
  ref: app/explore/ExploreLibrary.tsx
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

At `28068b6` a grep finds six-digit hex literals in `app/explore/ExploreLibrary.tsx` (6), `lib/dimensions.ts` (4) and `components/AdoptionPlanModal.tsx` (1).

## Impact

A theme change has to be made in several files. Only the React-component copies are avoidable.

## Remediation

Move the two components onto CSS custom properties.
