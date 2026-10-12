---
name: 0030 — Add Explore card fields to published_pathways
type: migration
schema_version: 1
aliases:
- 0030_published_pathways_explore_fields.sql
summary: Adds location, tags[] and stage to published_pathways, parsed from document frontmatter at publish.
number: '0030'
file: supabase/migrations/0030_published_pathways_explore_fields.sql
tables_touched:
- published-pathways
destructive: false
code_refs:
- supabase/migrations/0030_published_pathways_explore_fields.sql
- app/api/admin/pathways/publish/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0030_published_pathways_explore_fields.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Adds `location text`, `tags text[]`, `stage text` (all non-null with empty defaults).

## Why

Explore library cards need these without extra contributor input; accent is derived from the slug at runtime.

## Risk

None.
