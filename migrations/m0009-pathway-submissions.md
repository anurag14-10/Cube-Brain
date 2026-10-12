---
name: 0009 — Create pathway_submissions
type: migration
schema_version: 1
aliases:
- 0009_pathway_submissions.sql
summary: Creates pathway_submissions — a user's adoption previewed as a candidate corpus pathway for curation.
  Dropped in 0018.
number: '0009'
file: supabase/migrations/0009_pathway_submissions.sql
tables_touched:
- pathway-submissions
- designs
- auth-users
destructive: false
code_refs:
- supabase/migrations/0009_pathway_submissions.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0009_pathway_submissions.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.pathway_submissions` (`design_id`, `user_id`, `content`, `status` pending_review|reviewed, `reviewed_at`) with owner select/insert.

## Why

Let a user turn an adoption into a draft pathway page flagged for human curation, never auto-published.

## Risk

Superseded; the table was dropped and code referencing it is now dead.
