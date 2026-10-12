---
name: 0004 — Create wiki_cache
type: migration
schema_version: 1
aliases:
- 0004_wiki_cache.sql
summary: Creates the shared wiki_cache table for GitHub-fetched corpus pages; now inert.
number: '0004'
file: supabase/migrations/0004_wiki_cache.sql
tables_touched:
- wiki-cache
destructive: false
code_refs:
- supabase/migrations/0004_wiki_cache.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0004_wiki_cache.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.wiki_cache` (`path` PK, `content`, `fetched_at`) with authenticated read/insert/update.

## Why

Replace a per-instance in-memory cache so parallel serverless instances did not each cold-fetch GitHub raw content and hit rate limits.

## Risk

Low; obsolete since the corpus moved into the repo (`content/`).
