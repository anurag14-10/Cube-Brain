---
name: Explore — the Diffusion Library (/explore)
type: page
schema_version: 1
aliases:
- Diffusion Library
- Library
- Explore
summary: The public, no-login pathway library. It shows card tiles merging published_pathways with the static library
  list, plus a per-pathway or library-wide chat (chat mode `library`) that is saved only for signed-in users.
route: /explore
file: app/explore/page.tsx
access: public
roles:
- anonymous-visitor
- general-user
- adopter
- pathway-contributor
- admin
components:
- components-app-shell
- app-explore-explore-library
- components-toolkit-asset-cards
calls_endpoints:
- chat
- toolkit-assets
- toolkit-assets-download
status: live
code_refs:
- app/explore/page.tsx
- app/explore/ExploreLibrary.tsx
- proxy.ts
- app/api/chat/route.ts
doc_refs:
- docs/wiki/diffusion-cube/application/frontend.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/explore/page.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/explore/ExploreLibrary.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: proxy.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/chat/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/frontend.md
contested:
- field: calls_endpoints
  readings:
  - 'proxy.ts comment: /api/wiki-pathways is one of /explore''s own API dependencies and so must be public'
  - 'code: neither app/explore/page.tsx nor ExploreLibrary.tsx calls /api/wiki-pathways; only AdoptionWorkspace
    (Analyse/Contribute/Adoptions) does'
  note: The code supports the second reading. The endpoint is still public in proxy.ts.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it renders

A server component. It always loads `published_pathways` (slug, title, description, sector, stage, location,
tags, category) with the **service-role** client, because anonymous visitors have no session. It maps the rows
to `LibraryPathway` cards and gives each an accent colour from a slug hash, the same function the publish
route uses. It then renders [AppShell](../modules/components-app-shell.md) around
[ExploreLibrary](../modules/app-explore-explore-library.md):

- a hero with a library-wide question box, which opens a chat grounded in the overview of every pathway;
- a filter popover (Stage / Sector / Tags) over the card grid. Cards are the DB pathways plus the static
  `lib/library-pathways.ts` list, and a DB row wins when the slug matches;
- clicking a card opens a per-pathway chat. An empty history makes `/api/chat` (mode `library`) send the hidden
  kickoff prompt. Replies can end with a `<toolkit_assets>` tag; it is stripped from view and rendered as
  [ToolkitAssetCards](../modules/components-toolkit-asset-cards.md) (`GET /api/toolkit-assets`, downloads via
  `/api/toolkit-assets/[id]/download`).

`?open=<id>` reopens a saved `library_conversations` row for a signed-in user. RLS scopes it to their own rows,
and it is resolved server-side so the grid never flashes first. The Sidebar's "Recent Explorations" links
here.

## Access behaviour

- **Anonymous:** full library and chat. `/explore` and `/api/chat` are in `PUBLIC_PATHS`, and the chat route
  skips its approval check only for mode `library`. Chats stay in memory and are never saved. The Sidebar shows
  "Sign in" instead of the account footer.
- **Signed in, any status (including no role):** same view inside the normal shell. Chats are upserted to
  `library_conversations` after every reply, and recent ones appear in the Sidebar. A pending account (zero
  roles) waits here: `/analyse` and `/contribute` redirect such users to `/explore`.
- No role is ever required. This is the one page meant to need neither login nor registration.
