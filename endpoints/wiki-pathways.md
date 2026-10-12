---
name: GET /api/wiki-pathways
type: endpoint
schema_version: 1
summary: 'Public, lightweight index of the grounding corpus (static index.md entries + published_pathways):
  slug, title, description, sector, stage, timestamp, contributor — used for source-attribution chips.'
tags:
- corpus
- public
path: /api/wiki-pathways
methods:
- GET
file: app/api/wiki-pathways/route.ts
access: public
roles:
- anonymous-visitor
- adopter
- pathway-contributor
- admin
- general-user
tables_read:
- published-pathways
integrations:
- supabase-postgres
request_shape: none
response_shape: JSON [{slug, title, description, sector?, stage?, timestamp?, contributor?}]
status: live
code_refs:
- app/api/wiki-pathways/route.ts
- lib/wiki-content.ts#L45-L107
- components/AdoptionWorkspace.tsx
- proxy.ts#L19-L42
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/wiki-pathways/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/wiki-content.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
contested:
- field: response_shape
  readings:
  - 'route comment and docs: used by the public /explore Library page to render its card grid'
  - 'code: the only fetch caller is components/AdoptionWorkspace.tsx (source chips); /explore builds its
    cards from lib/library-pathways.ts + published_pathways server-side'
  note: Public exposure is still deliberate (proxy PUBLIC_PATHS); the /explore usage claim is stale.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

No input. `listWikiPathways()` merges `listStaticPathways()` (parses `content/wiki/pathways/index.md` bullets, then reads each file's `sector:`/`stage:`/`timestamp:`/`contributor:` frontmatter lines) with `published_pathways (slug, title, description, category, sector)` newest first; the route projects `{slug, title, description, sector, stage, timestamp, contributor}`. Published rows carry no stage/timestamp/contributor here. Static and DB entries are concatenated, not de-duplicated by slug.

## Enforcement

None — listed in proxy.ts `PUBLIC_PATHS`. Exposes the same metadata `published_pathways` RLS already makes public.

## Side effects

Read-only (filesystem + session-client select).

## Errors

None explicit; unreadable index yields `[]` for the static half.
