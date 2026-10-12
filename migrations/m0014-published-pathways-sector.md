---
name: 0014 — Add sector to published_pathways
type: migration
schema_version: 1
aliases:
- 0014_published_pathways_sector.sql
summary: Adds a nullable sector column to published_pathways.
number: '0014'
file: supabase/migrations/0014_published_pathways_sector.sql
tables_touched:
- published-pathways
destructive: false
code_refs:
- supabase/migrations/0014_published_pathways_sector.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0014_published_pathways_sector.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

`add column sector text` (nullable).

## Why

Surface the corpus's real sector spread without a separate sector picker; rows published earlier have none.

## Risk

None.
