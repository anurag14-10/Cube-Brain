---
name: pathways (table)
type: table
schema_version: 1
aliases:
- pathways
summary: 'The canonical contributor pathway workspace entity: slug, title, sector, description, the assembled
  document cache and review/publish pointers.'
table_name: pathways
store_kind: table
status: live
key_columns:
- id uuid PK
- slug text unique
- title
- sector
- description (0028)
- created_by uuid → auth.users (set null)
- content_cache text
- review_requested bool (0031)
- assembled_design_doc_id → design_documents (0032)
- published_design_doc_id → design_documents (0032)
- created_at
rls: Signed-in select; insert policy requires a pathway_contributor role row; no update/delete policy
references_tables:
- auth-users
- design-documents
created_in: m0020-pathways
code_refs:
- supabase/migrations/0020_pathways.sql
- supabase/migrations/0028_pathways_description.sql
- supabase/migrations/0031_pathways_review_requested.sql
- supabase/migrations/0032_pathways_design_doc_ids.sql
- supabase/migrations/0033_account_deletion.sql
- app/api/pathways/route.ts
- app/api/pathways/assemble/route.ts
- app/api/admin/pathways/publish/route.ts
- app/api/admin/pathways/delete/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0020_pathways.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0028_pathways_description.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0031_pathways_review_requested.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
contested:
- field: rls
  readings:
  - 'docs/wiki database.md: pathway insert requires pathway_contributor, enforced at the DB layer via
    an exists policy'
  - 'code: POST /api/pathways checks the role in app code and inserts with the service-role client, which
    bypasses that RLS policy'
  note: The policy exists (0020) but the live create path does not go through it; the code supports the
    second reading.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

`slug` matches `content/wiki/pathways/<slug>.md`. `content_cache` holds the latest assembled document (with the
toolkit-asset block). `review_requested` is set true by assemble and false by admin publish. The two
`*_design_doc_id` pointers record which draft version was assembled and which was published (FKs on delete set null
since 0033).

## RLS

Signed-in select. Insert policy: caller must hold `pathway_contributor` in `user_roles`. No update/delete policy.

## Lifecycle

- Create: `POST /api/pathways` — app-level `hasRole` check, then **service-role insert** (so the RLS insert policy is
  not what enforces it in practice).
- Assemble: `POST /api/pathways/assemble` commits the draft to GitHub, then service-role update of `content_cache`,
  `review_requested`, `assembled_design_doc_id` (best-effort after the commit).
- Publish: `POST /api/admin/pathways/publish` copies `content_cache` into `published_pathways`, clears
  `review_requested`, sets `published_design_doc_id`.
- Delete: `POST /api/admin/pathways/delete` — cascades `pathway_contributors` and `contribution_units`, sets
  `designs.pathway_id` null, removes toolkit asset files first.

## Gotchas

- Delete does not remove the GitHub file or the `published_pathways` row.
- The browser reads it directly (`lib/adoption-conversation.ts`, `components/AdminPathwayRowCard.tsx`,
  `components/ToolkitAssetStatusList.tsx`) under the signed-in select policy.
