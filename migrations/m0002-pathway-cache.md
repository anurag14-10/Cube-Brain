---
name: 0002 — Create pathway_cache
type: migration
schema_version: 1
aliases:
- 0002_pathway_cache.sql
summary: Creates the shared pathway_cache table for AI-generated per-pathway outputs; now inert.
number: '0002'
file: supabase/migrations/0002_pathway_cache.sql
tables_touched:
- pathway-cache
destructive: false
code_refs:
- supabase/migrations/0002_pathway_cache.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0002_pathway_cache.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.pathway_cache` keyed by `slug` with `content_hash`, `cube_state`, `card`, `summary`; RLS lets any authenticated user read/insert/update.

## Why

Cache explore-init scoring and explore-copy card text so a wiki update invalidates it via the content hash instead of a manual bust.

## Risk

Low. The table is now unused, but remains writable by any authenticated user.
