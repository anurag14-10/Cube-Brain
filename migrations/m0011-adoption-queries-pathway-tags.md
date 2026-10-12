---
name: 0011 — Tag adoption_queries with pathway slugs
type: migration
schema_version: 1
aliases:
- 0011_adoption_queries_pathway_tags.sql
summary: Adds pathway_slugs text[] to adoption_queries so each query records which pathways the reply
  drew on.
number: '0011'
file: supabase/migrations/0011_adoption_queries_pathway_tags.sql
tables_touched:
- adoption-queries
destructive: false
code_refs:
- supabase/migrations/0011_adoption_queries_pathway_tags.sql
- app/api/chat/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0011_adoption_queries_pathway_tags.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

`add column pathway_slugs text[] not null default '{}'`.

## Why

Without it the log was flat — no way to group queries by pathway. Slugs come from the `<grid_update>` block.

## Risk

None.
