---
name: pathway_submission_exec_summaries
type: table
schema_version: 1
summary: 'Dropped table: backend-only executive summary per pathway submission (owner write, no owner
  read); dropped in 0018.'
table_name: pathway_submission_exec_summaries
store_kind: table
status: dropped
key_columns:
- id uuid PK
- submission_id unique → pathway_submissions (cascade)
- content
- updated_at
rls: (before drop) owner insert/update only, deliberately no select policy
references_tables:
- pathway-submissions
created_in: m0015-pathway-submission-exec-summaries
dropped_in: m0018-drop-retired-tables
code_refs:
- supabase/migrations/0015_pathway_submission_exec_summaries.sql
- supabase/migrations/0018_drop_retired_tables.sql
- lib/pathway-submission-versions.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0015_pathway_submission_exec_summaries.sql
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

`submission_id` (unique — upserted, not versioned), `content`, `updated_at`.

## RLS

Before the drop: the owner could insert and update but never read it; admins read via service role.

## Lifecycle

Created 0015, dropped 0018. The prompt that generated it survives as dead code in `lib/system-prompts.ts`.

## Gotchas

`lib/pathway-submission-versions.ts` still references it.
