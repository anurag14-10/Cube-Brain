---
name: POST /api/admin/pathways/delete
type: endpoint
schema_version: 1
summary: 'Admin deletes a `pathways` row: removes its toolkit-asset files from storage first, then relies
  on FK cascades (pathway_contributors, contribution_units) and set-null (designs.pathway_id); GitHub
  and published_pathways copies are untouched.'
tags:
- admin
- pathways
path: /api/admin/pathways/delete
methods:
- POST
file: app/api/admin/pathways/delete/route.ts
access: admin-only
roles:
- admin
tables_read:
- user-roles
- contribution-units
tables_written:
- pathways-table
- pathway-contributors
- contribution-units
- designs
- toolkit-assets-bucket
integrations:
- supabase-postgres
- supabase-auth
- supabase-storage
request_shape: 'JSON {pathway_id: string}'
response_shape: 'JSON {ok: true}'
status: live
code_refs:
- app/api/admin/pathways/delete/route.ts
- lib/toolkit-assets-server.ts#L213-L218
- components/AdminPathwaysPanel.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/admin/pathways/delete/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
contested:
- field: tables_written
  readings:
  - 'docs/wiki: deletes a pathways row, relies on FK cascade/set-null'
  - 'code: also removes toolkit-asset objects from the toolkit-assets bucket before the delete'
  note: Storage cleanup arrived with migration 0034; wiki predates it.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

Body `{pathway_id}` (400 if not a string). Called from components/AdminPathwaysPanel.tsx.

## Enforcement

`isAdmin` (allow-list or `admin` role) → else 403 `Not authorized.` Service-role client for all work.

## Side effects

1. Selects `contribution_units.storage_path` for `unit_type='toolkit-asset'` on this pathway (any publish state) and calls `removeAssetObjects` on the `toolkit-assets` bucket — storage failure is logged, never blocks.
2. `pathways.delete().eq('id', pathway_id)`. Cascades: `pathway_contributors` (0021), `contribution_units` (0022) on `pathway_id`; `designs.pathway_id` set null (0024) so contributor workspaces survive unlinked.
3. Does **not** touch `content/wiki/pathways/<slug>.md` in GitHub nor the `published_pathways` row — a published pathway stays live in the library and grounding after its workspace is deleted.

## Errors

500 with Supabase message on delete failure.
