---
name: POST /api/admin/pathways/publish
type: endpoint
schema_version: 1
aliases:
- admin publish
summary: 'Step two of two-step publish: an admin copies a pathway''s assembled document (pathways.content_cache)
  into published_pathways (upsert on slug) and publishes exactly the toolkit assets whose ids appear in
  that document.'
tags:
- admin
- publish
- toolkit-assets
path: /api/admin/pathways/publish
methods:
- POST
file: app/api/admin/pathways/publish/route.ts
access: admin-only
roles:
- admin
tables_read:
- user-roles
- pathways-table
tables_written:
- published-pathways
- pathways-table
- contribution-units
integrations:
- supabase-postgres
- supabase-auth
request_shape: 'JSON {pathway_id: uuid}'
response_shape: 'JSON {ok: true, slug, assetsPublished: boolean}'
status: live
code_refs:
- app/api/admin/pathways/publish/route.ts
- app/api/admin/pathways/publish/route.ts#L9-L29
- app/api/admin/pathways/publish/route.ts#L70-L126
- lib/toolkit-assets.ts#L239-L245
- components/AdminPathwaysPanel.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/admin/pathways/publish/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
contested:
- field: tables_written
  readings:
  - 'docs/wiki api-specification.md: upserts published_pathways, clears review_requested, sets published_design_doc_id'
  - 'code: additionally sets contribution_units.published_at for toolkit assets listed in the document'
  note: The generated wiki predates migration 0034 (toolkit assets); the code reading is current.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

Body `{pathway_id}` (400 `pathway_id required`). Called from components/AdminPathwaysPanel.tsx. Response `{ok, slug, assetsPublished}` — `assetsPublished:false` means the pathway went live but the asset update failed.

## Enforcement

Session + `isAdmin(supabase, user.email)` (ADMIN_EMAILS allow-list OR an `admin` row in `user_roles`) → else 403 `Admin only.` All DB work via the service-role client.

## Side effects

1. Reads `pathways (id, slug, title, sector, content_cache, assembled_design_doc_id)`; 404 if missing, 400 if `content_cache` empty ("The contributor must publish from their workspace first").
2. `parseFrontmatter` (local, line-based; handles scalars and inline `[a, b]` arrays) pulls `title`, `description` (→ card hook), `stage`, `sector`, `location`, `tags` from the document's [frontmatter](../contracts/pathway-frontmatter.md); `category` = first two tags joined by ` · `, else `Community`.
3. `published_pathways.upsert({slug, title, description, category, content, sector, location, tags, stage, published_by}, onConflict 'slug')` — re-publishing keeps the slug and URL; `created_at` is never rewritten.
4. `pathways.update({review_requested:false, published_design_doc_id: assembled_design_doc_id})`.
5. Toolkit assets: `assetIdsInDocument(content_cache)` → `contribution_units.update({published_at: now})` where `pathway_id`, `unit_type='toolkit-asset'`, `published_at is null`, `unit_internal_id in ids`. An asset attached after the last assemble is not in the document and stays unpublished. Idempotent.

## Errors

500 `Failed to publish pathway.` on upsert failure. The `pathways` update result is not checked. A duplicate `parseFrontmatter` implementation also lives elsewhere in the codebase.
