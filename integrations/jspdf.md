---
name: jsPDF
type: integration
schema_version: 1
summary: Client-side PDF export of generated documents (`downloadPlanAsPdf`), used by the adoption plan
  modal and the pathway document pane.
integration_kind: pdf-generation
provider: Open-source library (in-browser)
sdk: jspdf@^4.2.1
account_notes: No account; bundled npm package.
code_refs:
- lib/adoption-plan-pdf.ts
- components/AdoptionPlanModal.tsx
- components/PathwayDocumentPane.tsx
- package.json
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/adoption-plan-pdf.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: components/AdoptionPlanModal.tsx
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/third-party-integrations.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Used for

Client-side PDF export of generated documents (`downloadPlanAsPdf`), used by the adoption plan modal and the pathway document pane.

## Configuration

None.

## Failure behaviour

Runs entirely in the browser; a failure only affects that download.

## Account

No account; bundled npm package.
