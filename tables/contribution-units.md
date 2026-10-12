---
name: contribution_units
type: table
schema_version: 1
summary: Built in 0022 for per-unit contributor content; since 0034 it is live as the store for toolkit
  asset files and links (unit_type toolkit-asset), written only via service-role routes.
table_name: contribution_units
store_kind: table
status: live
key_columns:
- id uuid PK
- unit_internal_id text (asset-<uuid> for assets)
- pathway_id → pathways (cascade)
- design_id → designs (set null)
- user_id → auth.users (nullable, set null since 0033)
- section check in (identity, micro-innovation)
- unit_type
- dimension, stage, density
- source_doc
- content (0025)
- published_at
- asset_kind check in (file, link) (0034)
- asset_name, purpose, reuse_condition
- storage_path, file_name, mime_type, size_bytes
- link_url check ^https://
- share_consent, share_consented_at
- unique (pathway_id, unit_internal_id)
rls: 'Select: signed-in AND (published_at not null OR own row). No insert/update/delete policy since 0034
  — all writes via service-role'
references_tables:
- pathways-table
- designs
- auth-users
created_in: m0022-contribution-units
code_refs:
- supabase/migrations/0022_contribution_units.sql
- supabase/migrations/0025_contribution_units_content.sql
- supabase/migrations/0033_account_deletion.sql
- supabase/migrations/0034_contribution_units_toolkit_assets.sql
- lib/toolkit-assets-server.ts
- app/api/toolkit-assets/route.ts
- app/api/admin/pathways/publish/route.ts
- app/api/account/delete/route.ts
- app/api/admin/pathways/delete/route.ts
- components/ToolkitAssetStatusList.tsx
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0022_contribution_units.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0025_contribution_units_content.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0033_account_deletion.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
contested:
- field: status
  readings:
  - 'docs/wiki database.md (refreshed 2026-09-28, covers 0001-0032): inert — nothing in app code writes
    it (TD-04)'
  - 'code at 28068b6 + migration 0034: live — toolkit asset rows are inserted, published and deleted by
    service-role routes'
  note: The doc predates 0034. Code supports live, but only for toolkit-asset rows; the rest of the table
    design is still unused.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

0022 created the unit index (`unit_internal_id`, `section`, `unit_type`, grid tags `dimension`/`stage`/`density`,
`source_doc`, `git_commit_sha`, `published_at`). 0025 added `content` and dropped `git_commit_sha`. 0033 made `user_id`
nullable with on delete set null. 0034 added the toolkit asset columns, the `contribution_units_toolkit_asset_shape`
check (a toolkit-asset row must be `micro-innovation`, named, consented with a timestamp, and either a file with
`storage_path`+`file_name` or a link with `link_url`) and a partial index `(pathway_id, published_at) where
unit_type = 'toolkit-asset'`.

## RLS

One select policy remains: signed-in users see published rows plus their own drafts (used by
`components/ToolkitAssetStatusList.tsx` through the browser client). 0034 dropped the insert and update policies
because they allowed a user to set `published_at` on their own rows (self-publish). Writers, all service-role:

- `POST /api/toolkit-assets` — inserts an unpublished asset row after consent.
- `POST /api/admin/pathways/publish` — sets `published_at` for exactly the asset ids listed in the published document.
- `POST /api/account/delete` — nulls `user_id` on published rows, deletes unpublished rows (and their files).
- `POST /api/admin/pathways/delete` — removes asset files; rows cascade with the pathway.

Readers: `lib/toolkit-assets-server.ts` (published assets for /explore, /analyse and the download route; all consented
assets for assemble), `app/admin/page.tsx`.

## Lifecycle

Asset row created unpublished → listed in the assembled document by `<!-- asset-id -->` marker → published when an
admin publishes that pathway → survives author account deletion (user_id null) → removed only with its pathway.

## Gotchas

- Only `toolkit-asset` rows are ever written. Identity units, other micro-innovation types, `content` and `density` remain
  unused — the whole-document GitHub commit replaced per-unit storage for everything else.
- `unit_type` spellings in the 0022 comment (`failure-fix`, `toolkit-asset`) are DB values, not the framework's display names.
- An asset shared after the last "Send for Review" is not in the document, so it waits for the next publish.
