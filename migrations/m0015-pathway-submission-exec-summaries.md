---
name: 0015 — Create pathway_submission_exec_summaries
type: migration
schema_version: 1
aliases:
- 0015_pathway_submission_exec_summaries.sql
summary: Creates a backend-only executive summary table per submission (owner can write, never read).
  Dropped in 0018.
number: '0015'
file: supabase/migrations/0015_pathway_submission_exec_summaries.sql
tables_touched:
- pathway-submission-exec-summaries
- pathway-submissions
destructive: false
code_refs:
- supabase/migrations/0015_pathway_submission_exec_summaries.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0015_pathway_submission_exec_summaries.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.pathway_submission_exec_summaries` (unique `submission_id`, `content`) with owner insert/update policies and deliberately no select policy.

## Why

An internal-review summary generated alongside each draft, never shown to the contributor.

## Risk

Superseded by 0018; its prompt remains as dead code.
