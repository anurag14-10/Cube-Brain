---
name: POST /api/admin/pathway-submissions/publish
type: endpoint
schema_version: 1
summary: 'Dead code: the pre-0018 admin publish path that copied a pathway_submissions row into published_pathways.
  The table it reads was dropped in migration 0018.'
tags:
- admin
- dead-code
- publish
path: /api/admin/pathway-submissions/publish
methods:
- POST
file: app/api/admin/pathway-submissions/publish/route.ts
access: admin-only
roles:
- admin
tables_read:
- user-roles
- pathway-submissions
- designs
- published-pathways
tables_written:
- published-pathways
- pathway-submissions
integrations:
- supabase-postgres
- supabase-auth
request_shape: 'JSON {submission_id: string}'
response_shape: 'JSON {ok: true, slug} — unreachable; in practice 404 {error:''Submission not found.''}'
status: dead-code
code_refs:
- app/api/admin/pathway-submissions/publish/route.ts
- supabase/migrations/0018_drop_retired_tables.sql
- components/PathwaySubmissionsPanel.tsx
doc_refs:
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/admin/pathway-submissions/publish/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0018_drop_retired_tables.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/knowledge/technical-debt.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

`{submission_id}` → would select `pathway_submissions (id, content, design_id, designs(meta))`, derive title/description/sector from `designs.meta` (name/summary/sector), pick a unique slug against `content/wiki/pathways/*.md` + `published_pathways.slug`, insert into `published_pathways` (with `source_submission_id`, `published_by`) and mark the submission `published`.

## Enforcement

`isAdmin` → else 403.

## Side effects

None in practice. Queries `pathway_submissions`, dropped (with pathway_submission_versions and pathway_submission_exec_summaries) by migration 0018; any call fails at the first select. The fetch error is mapped to `404 'Submission not found.'`, so the breakage presents as a not-found rather than a 500.

## Errors

Always 404 after auth. Its only caller, components/PathwaySubmissionsPanel.tsx, is not imported by any page, so nothing in the UI reaches it. Replaced by [pathways-assemble](pathways-assemble.md) + [admin-pathways-publish](admin-pathways-publish.md).
