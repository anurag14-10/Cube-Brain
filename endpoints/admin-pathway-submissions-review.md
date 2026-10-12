---
name: POST /api/admin/pathway-submissions/review
type: endpoint
schema_version: 1
summary: 'Dead code: marked a pathway_submissions row ''reviewed''. The table was dropped in migration
  0018, so every call returns 500.'
tags:
- admin
- dead-code
path: /api/admin/pathway-submissions/review
methods:
- POST
file: app/api/admin/pathway-submissions/review/route.ts
access: admin-only
roles:
- admin
tables_read:
- user-roles
tables_written:
- pathway-submissions
integrations:
- supabase-postgres
- supabase-auth
request_shape: 'JSON {submission_id: string}'
response_shape: 'JSON {ok: true} — unreachable; in practice 500 relation-does-not-exist'
status: dead-code
code_refs:
- app/api/admin/pathway-submissions/review/route.ts
- supabase/migrations/0018_drop_retired_tables.sql
- components/PathwaySubmissionsPanel.tsx
doc_refs:
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/admin/pathway-submissions/review/route.ts
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

`{submission_id}` → `pathway_submissions.update({status:'reviewed', reviewed_at: now})`.

## Enforcement

`isAdmin` → else 403.

## Side effects

None. Queries `pathway_submissions`, dropped (with pathway_submission_versions and pathway_submission_exec_summaries) by migration 0018; any call fails at the first select.

## Errors

500 with the Postgres "relation does not exist" message. Only caller is the unmounted components/PathwaySubmissionsPanel.tsx.
