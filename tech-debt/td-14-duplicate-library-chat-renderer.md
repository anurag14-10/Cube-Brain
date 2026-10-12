---
name: TD-14 Library chat has its own renderer and composer
type: tech_debt
schema_version: 1
aliases:
- TD-14
summary: app/explore/ExploreLibrary.tsx carries its own markdown/bold renderer, textarea and send button,
  separate from components/ChatPanel.tsx.
tags:
- duplication
- ui
td_id: TD-14
severity: P3
status: open
affected_modules:
- app-explore-explore-library
- components-chat-panel
remediation: Extract shared chat primitives (message renderer, composer) if the two surfaces keep converging.
code_refs:
- app/explore/ExploreLibrary.tsx#L617-L625
- components/ChatPanel.tsx
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

The Library was ported from a separate standalone app. At `28068b6`, `ExploreLibrary.tsx` still has its own `renderBold` and composer. The toolkit-assets work (TA-09) then added a second, Library-only parsing path: the trailing `<toolkit_assets>` tag is stripped while streaming in ExploreLibrary, whereas `/analyse` cards travel through `<grid_update>` in ChatPanel.

## Impact

A fix to one chat surface does not reach the other.

## Remediation

Extract shared primitives when convenient.
