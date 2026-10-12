---
name: pathway_submissions
type: table
schema_version: 1
summary: 'Dropped table: the original one-draft-per-adoption pathway submission; dropped in 0018 but still
  queried by dead route code.'
table_name: pathway_submissions
store_kind: table
status: dropped
key_columns:
- id uuid PK
- design_id → designs (cascade, unique since 0013)
- user_id → auth.users (cascade)
- content text
- status check in (pending_review, reviewed, published)
- created_at
- reviewed_at
rls: (before drop) owner select/insert/update
references_tables:
- designs
- auth-users
created_in: m0009-pathway-submissions
dropped_in: m0018-drop-retired-tables
code_refs:
- supabase/migrations/0009_pathway_submissions.sql
- supabase/migrations/0012_published_pathways.sql
- supabase/migrations/0013_pathway_submission_versions.sql
- supabase/migrations/0018_drop_retired_tables.sql
- app/api/pathway-submissions/push/route.ts
- lib/pathway-submission-versions.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0009_pathway_submissions.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0012_published_pathways.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0013_pathway_submission_versions.sql
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

`design_id` (unique from 0013), `user_id`, `content`, `status` (0012 added `published`), `created_at`, `reviewed_at`.

## RLS

Before the drop: owner select, insert (0009) and update (0013). Review/publish went through the service-role client.

## Lifecycle

Created 0009 → extended 0012/0013 → dropped 0018 along with its two dependent tables, replaced by the
pathways / pathway_contributors workspace model and a whole-document GitHub commit.

## Gotchas

Still referenced by dead code that would fail with "relation does not exist":
`app/api/pathway-submissions/push/route.ts`, `app/api/admin/pathway-submissions/publish/route.ts`,
`app/api/admin/pathway-submissions/review/route.ts`, `lib/pathway-submission-versions.ts`,
`components/PathwaySubmissionsPanel.tsx`.
