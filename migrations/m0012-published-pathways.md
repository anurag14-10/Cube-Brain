---
name: 0012 — Create published_pathways
type: migration
schema_version: 1
aliases:
- 0012_published_pathways.sql
summary: Creates published_pathways — admin-published community pathways, public-read — and widens pathway_submissions.status
  to include published.
number: '0012'
file: supabase/migrations/0012_published_pathways.sql
tables_touched:
- published-pathways
- pathway-submissions
- auth-users
destructive: false
code_refs:
- supabase/migrations/0012_published_pathways.sql
- lib/wiki-loader.ts
- lib/wiki-content.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0012_published_pathways.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.published_pathways` (unique `slug`, `title`, `description`, `category`, `content`, `source_submission_id` FK set null, `published_by` FK auth.users with no ON DELETE action) with a public select policy; re-creates the `pathway_submissions` status check with `published`.

## Why

Publish community pathways without a git commit and redeploy; the loaders merge this table with the static corpus.

## Risk

The `published_by` FK without ON DELETE later blocked account deletion (fixed in 0033).
