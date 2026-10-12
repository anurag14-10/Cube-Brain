---
name: pathway_submission_versions
type: table
schema_version: 1
summary: 'Dropped table: append-only version history of pathway submission drafts; dropped in 0018, still
  referenced by lib/pathway-submission-versions.ts.'
table_name: pathway_submission_versions
store_kind: table
status: dropped
key_columns:
- id uuid PK
- submission_id → pathway_submissions (cascade)
- version_number
- content
- commit_message
- created_at
- unique (submission_id, version_number)
rls: (before drop) select/insert where the parent submission is the caller's
references_tables:
- pathway-submissions
created_in: m0013-pathway-submission-versions
dropped_in: m0018-drop-retired-tables
code_refs:
- supabase/migrations/0013_pathway_submission_versions.sql
- supabase/migrations/0018_drop_retired_tables.sql
- lib/pathway-submission-versions.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0013_pathway_submission_versions.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0018_drop_retired_tables.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/pathway-submission-versions.ts
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

`submission_id`, `version_number`, `content`, `commit_message`, `created_at`; unique `(submission_id, version_number)`.

## RLS

Before the drop: select/insert through an `exists` check on the owning submission.

## Lifecycle

Created 0013, dropped 0018. Its role (versioned drafts) moved to `design_documents` rows with `doc_type = 'draft'`.

## Gotchas

`lib/pathway-submission-versions.ts` still queries it (dead code).
