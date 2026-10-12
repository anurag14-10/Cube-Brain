---
name: 0013 — Create pathway_submission_versions
type: migration
schema_version: 1
aliases:
- 0013_pathway_submission_versions.sql
summary: Creates version history for pathway submission drafts, makes design_id unique on pathway_submissions,
  adds an owner update policy and published_pathways.commit_message.
number: '0013'
file: supabase/migrations/0013_pathway_submission_versions.sql
tables_touched:
- pathway-submission-versions
- pathway-submissions
- published-pathways
destructive: false
code_refs:
- supabase/migrations/0013_pathway_submission_versions.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0013_pathway_submission_versions.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.pathway_submission_versions` (unique `(submission_id, version_number)`) with owner-scoped select/insert; adds unique `(design_id)` and an owner update policy on `pathway_submissions`; adds `published_pathways.commit_message`.

## Why

Mirror design_documents' append-only versioning for drafts; one draft per adoption; let a contributor push their own submission with their session client.

## Risk

Superseded by 0018. `commit_message` stays as an inert column.
