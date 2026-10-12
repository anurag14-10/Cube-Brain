---
name: Wiki index (/wiki)
type: page
schema_version: 1
aliases:
- The Wiki
- Pathway Library (wiki)
summary: Server page that lists the grounding corpus (content/wiki/pathways/index.md entries) plus published_pathways
  rows, grouped by category. It is deliberately not linked from the Sidebar.
route: /wiki
file: app/(app)/wiki/page.tsx
access: role-gated
roles:
- general-user
- adopter
- pathway-contributor
- admin
components:
- app-app-group-layout
status: live
code_refs:
- app/(app)/wiki/page.tsx
- lib/wiki-content.ts
- components/Sidebar.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/frontend.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/(app)/wiki/page.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/wiki-content.ts
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

It calls `listWikiPathways()` ([lib/wiki-content](../modules/lib-wiki-content.md)): the static entries parsed
from the grounding corpus's `index.md` (category = the `# Heading` they sit under), concatenated with
`published_pathways` rows (slug, title, description, category, sector). Nothing is de-duplicated, so a slug
present in both appears twice. The page renders one card section per category, and each card links to
`/wiki/<slug>`.

Only index-linked static files appear here. On-disk pathway files not linked from `index.md` are invisible,
just as they are excluded from prompt grounding.

## Access behaviour

Inside the `(app)` group: anonymous → `/login`; zero roles → "Awaiting approval"; any role → the page. The
Sidebar comment says the wiki is now corpus material for prompts, not a nav destination, so the page is
reachable only by URL or via links from the Contributor pane ("View it live").
