---
name: 0017 — Add contributor_org to published_pathways
type: migration
schema_version: 1
aliases:
- 0017_published_pathways_contributor.sql
summary: Adds contributor_org so community pathways can be attributed to the contributing organisation.
number: '0017'
file: supabase/migrations/0017_published_pathways_contributor.sql
tables_touched:
- published-pathways
destructive: false
code_refs:
- supabase/migrations/0017_published_pathways_contributor.sql
- lib/wiki-loader.ts
- app/api/admin/pathways/publish/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0017_published_pathways_contributor.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

`ALTER TABLE published_pathways ADD COLUMN contributor_org text`.

## Why

Let the LLM context and UI attribute surfaced insights to the contributor rather than asserting them as the Cube's own.

## Risk

The live admin publish route never sets this column, so attribution only appears on legacy rows.
