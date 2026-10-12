---
name: Contribute a pathway (/contribute)
type: page
schema_version: 1
aliases:
- Contribute
- Contributor flow
summary: 'The Contributor entry point. It is public at middleware level, and the page walks a gate chain: anonymous
  → pending → registration form → rejected → under review → the ContributeGrid workspace for pathway_contributor
  holders.'
route: /contribute
file: app/contribute/page.tsx
access: public
roles:
- pathway-contributor
components:
- components-app-shell
- components-access-gate-message
- app-contribute-contribute-access-gate
- components-contributor-registration-gate
- app-contribute-contribute-grid
- components-pathway-selector
- components-adoption-workspace
- components-chat-panel
- components-pathway-document-pane
- components-toolkit-asset-consent-card
- components-toolkit-asset-status-list
- components-attachments-panel
- components-heatmap-grid
calls_endpoints:
- pathways
- pathways-join
- pathways-check-similar
- chat
- pathways-assemble
- toolkit-assets
- toolkit-assets-upload-url
- toolkit-assets-download
- wiki-pathways
- organisations
status: live
code_refs:
- app/contribute/page.tsx
- app/contribute/ContributeGrid.tsx
- app/contribute/ContributeAccessGate.tsx
- proxy.ts
doc_refs:
- docs/wiki/diffusion-cube/application/frontend.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/contribute/page.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/contribute/ContributeGrid.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/contribute/ContributeAccessGate.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: proxy.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/frontend.md
contested:
- field: access
  readings:
  - 'docs/wiki frontend.md route table: Auth = ''Session required; tiered by registration + pathway_contributor
    role'''
  - 'code: /contribute is in proxy.ts PUBLIC_PATHS; an anonymous visitor gets an explainer AccessGateMessage with
    a login CTA'
  note: The code supports public-at-middleware. The page tiers are UX only; /api/chat re-checks pathway_contributor
    for flow=contributor, and the pathways/toolkit-asset routes check role and membership themselves.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it renders

For an approved contributor it renders [ContributeGrid](../modules/app-contribute-contribute-grid.md), a
four-state view machine:

1. **pathways:** "Share your learnings." A grid of the pathways the user has joined (`GET /api/pathways`,
   filtered by `isContributor`). Clicking a card opens the most recent chat for that pathway, or a new one.
   The organisation filter chips are built but switched off (`SHOW_ORG_FILTER = false`).
2. **pick:** [PathwaySelector](../modules/components-pathway-selector.md). Join an existing pathway
   (`POST /api/pathways/[id]/join`), or create one (`POST /api/pathways`) after an LLM duplicate check
   (`POST /api/pathways/check-similar`, "Did you mean…?").
3. **new / existing:** [AdoptionWorkspace](../modules/components-adoption-workspace.md) with
   `fixedFlow="contributor"`. A document-first chat (`/api/chat` `companion` + `pathway-draft`), automatic
   draft generation and revision, toolkit-asset consent cards (`/api/toolkit-assets/upload-url` → signed
   upload → `POST /api/toolkit-assets`), and the [PathwayDocumentPane](../modules/components-pathway-document-pane.md)
   with a version dropdown and "Send for Review" (`POST /api/pathways/assemble`).

`?open=<id>` deep-links straight into an existing contributor chat. `/wiki/<slug>?from=contribute&designId=<id>`
links back here.

## Access behaviour

Gate chain in the page (`/contribute` is in `PUBLIC_PATHS`):

- **Anonymous:** AccessGateMessage "Turn your deployment into a pathway" with a "Log in or sign up" CTA.
- **Signed in, zero roles:** `redirect('/explore')`.
- **No `contributor_registrations` row:** [ContributeAccessGate](../modules/app-contribute-contribute-access-gate.md)
  → [ContributorRegistrationGate](../modules/components-contributor-registration-gate.md), the one-time
  registration form. It calls `router.refresh()` on submit.
- **Registration `access_status = 'rejected'`:** "Registration not approved" message.
- **Registered but no `pathway_contributor` role yet:** "Application under review". Approval in `/admin` grants
  the role.
- **pathway_contributor:** ContributeGrid.

These checks are UX only. The API routes check the role (and pathway membership) on every call.
