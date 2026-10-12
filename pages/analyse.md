---
name: Analyse your own adoption (/analyse)
type: page
schema_version: 1
aliases:
- Analyse
- Explorer flow
- Strengthen
- Navigate
summary: The Explorer entry point. It is reachable by anyone at the middleware level, and the page renders a different
  view for anonymous, pending, non-adopter and adopter visitors. Only adopters get the companion workspace (fixedFlow=explorer).
route: /analyse
file: app/analyse/page.tsx
access: public
roles:
- adopter
components:
- components-app-shell
- components-access-gate-message
- app-analyse-strengthen-workspace
- components-adoption-workspace
- components-chat-panel
- components-heatmap-grid
- components-adoption-plan-modal
- components-attachments-panel
- components-toolkit-asset-cards
calls_endpoints:
- chat
- wiki-pathways
- toolkit-assets
- toolkit-assets-download
status: live
code_refs:
- app/analyse/page.tsx
- app/analyse/StrengthenWorkspace.tsx
- proxy.ts
- lib/roles.ts
doc_refs:
- docs/wiki/diffusion-cube/application/frontend.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/analyse/page.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/analyse/StrengthenWorkspace.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: proxy.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/roles.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/frontend.md
contested:
- field: access
  readings:
  - 'docs/wiki frontend.md route table: Auth = ''Session required; tiered by adopter role'''
  - 'code: /analyse is in proxy.ts PUBLIC_PATHS, and an anonymous visitor gets an AccessGateMessage with a ''Log
    in or sign up'' CTA, not a login redirect'
  note: The code supports public-at-middleware with in-page tiers. The role check on this page is UX only; /api/chat
    re-checks the adopter role for flow=explorer.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it renders

A server component that always builds its own [AppShell](../modules/components-app-shell.md), because it lives
outside the `(app)` group. For an adopter it renders
[StrengthenWorkspace](../modules/app-analyse-strengthen-workspace.md) with `key="analyse"`, so moving from
`/contribute` remounts it instead of reusing that flow's state. StrengthenWorkspace mounts
[AdoptionWorkspace](../modules/components-adoption-workspace.md) with `fixedFlow="explorer"`:

- a welcome hero ("What brings you to the Cube?") with a free-text box and a document drop zone;
- then the chat ([ChatPanel](../modules/components-chat-panel.md)), driven by
  [useAdoptionConversation](../modules/lib-adoption-conversation.md). It calls `/api/chat` modes `companion`,
  `extract-insights`, `analysis-doc` and `executive-summary`;
- a resizable right panel with the 4×4 Grid ([HeatmapGrid](../modules/components-heatmap-grid.md)) and the
  Analysis Document / Executive Summary ([AdoptionPlanModal](../modules/components-adoption-plan-modal.md) in
  panel mode, with PDF download);
- source chips resolved through `GET /api/wiki-pathways`, and toolkit-asset download cards.

`?open=<id>` reopens a past Explorer session; rows whose `meta.flow` is not `explorer` are ignored. When the
first message creates the `designs` row, the URL becomes `/analyse?open=<id>` without remounting the
conversation.

## Access behaviour

The tiers are in the page, not in proxy.ts (`/analyse` is a public path):

- **Anonymous:** AccessGateMessage "Analyse your own adoption" with the `STRENGTHEN_INTRO` body and a
  "Log in or sign up" CTA to `/login`.
- **Signed in, zero roles (pending):** `redirect('/explore')`.
- **Signed in, has some role but not `adopter`:** the same message plus "Ask an admin to grant you Explorer
  access", with no button.
- **Adopter:** the workspace. Adopter is auto-granted at sign-up, so most verified accounts land here.

These checks are UX only. The real gate is `/api/chat`, which returns 403 when there are no roles, or when
`flow=explorer` is used without the adopter role.
