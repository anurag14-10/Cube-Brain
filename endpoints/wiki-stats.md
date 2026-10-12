---
name: GET /api/wiki-stats
type: endpoint
schema_version: 1
summary: Returns {total, sectors[]} over the merged grounding corpus for an approved user; no caller remains
  since the 'Explore the Pathways Library' intent was removed.
tags:
- corpus
- inert
path: /api/wiki-stats
methods:
- GET
file: app/api/wiki-stats/route.ts
access: role-gated
roles:
- adopter
- pathway-contributor
- admin
- general-user
tables_read:
- user-roles
- published-pathways
integrations:
- supabase-postgres
- supabase-auth
request_shape: none
response_shape: 'JSON {total: number, sectors: string[]} (sectors exclude ''Cross-Sector'' and untagged)'
status: inert
code_refs:
- app/api/wiki-stats/route.ts
- lib/wiki-content.ts#L109-L126
- lib/explorer-intents.ts
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/wiki-stats/route.ts
- system: diffusion_cube_code
  method: derived
  date: '2026-10-08'
  ref: grep for wiki-stats callers in app/ components/ lib/
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
contested:
- field: status
  readings:
  - 'docs/wiki api-specification.md: used by the companion''s opening line'
  - 'code: no fetch of /api/wiki-stats anywhere; lib/explorer-intents.ts now has a single ANALYSE_FLOW
    with no browse intent'
  note: Code supports inert.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

`getWikiStats()` → `{total: listWikiPathways().length, sectors: unique real sectors}`.

## Enforcement

`hasAnyRole` → else 403 `Your account is awaiting approval.` (not in PUBLIC_PATHS, so anonymous gets the proxy's 401 first).

## Side effects

Read-only.

## Errors

403 only. Inert: the intent it backed was collapsed into the single Analyse flow, and nothing calls it.
