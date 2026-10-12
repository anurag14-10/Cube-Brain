---
name: Your adoptions (/adoptions)
type: page
schema_version: 1
aliases:
- adoptions list
- saved adoptions
summary: Client page that lists every `designs` row the user owns (Explorer and Contributor) as cards and reopens
  one in AdoptionWorkspace. It is reachable only by URL, because the Sidebar does not link it.
route: /adoptions
file: app/(app)/adoptions/page.tsx
access: role-gated
roles:
- general-user
- adopter
- pathway-contributor
- admin
components:
- app-app-group-layout
- components-adoption-workspace
- components-confirm-dialog
calls_endpoints:
- chat
- wiki-pathways
- toolkit-assets
- toolkit-assets-download
- pathways-assemble
- toolkit-assets-upload-url
status: live
code_refs:
- app/(app)/adoptions/page.tsx
- app/(app)/layout.tsx
- lib/adoptions-cache.ts
- components/Sidebar.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/frontend.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/(app)/adoptions/page.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/(app)/layout.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/adoptions-cache.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: components/Sidebar.tsx
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/frontend.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it renders

`AdoptionsPageContent` (inside Suspense):

- loads the list via [adoptions-cache](../modules/lib-adoptions-cache.md) (`designs`, newest first, with a
  60 s in-tab cache);
- shows "+ Analyse" / "+ Contribute" buttons only when the browser-side `hasRole` checks find adopter /
  pathway_contributor;
- renders a card grid with name, sector · geography, summary, relative updated time, and a 🗑 delete (confirm
  dialog, then `designs` delete through the browser client under RLS);
- selecting a card (or `?open=<id>`) swaps the view to [AdoptionWorkspace](../modules/components-adoption-workspace.md)
  with no `fixedFlow`. The flow then comes from the row's `meta.flow`, so it continues the Explorer or
  Contributor conversation with the same endpoints those pages use.

## Access behaviour

Inside the `(app)` group: proxy.ts requires a session (anonymous → `/login?next=/adoptions`), and the
[(app) layout](../modules/app-app-group-layout.md) shows "Awaiting approval" for an account with zero roles.
Any role passes. The Sidebar does not link this page (nav is Explore / Analyse / Contribute / Admin, and its
"Recent Explorations" open `/analyse?open=` or `/explore?open=`), so it is reachable only by typed URL or old
links.
