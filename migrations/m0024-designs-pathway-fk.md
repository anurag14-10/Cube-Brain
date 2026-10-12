---
name: 0024 — Link designs to pathways
type: migration
schema_version: 1
aliases:
- 0024_designs_pathway_fk.sql
summary: Adds designs.pathway_id (FK pathways, on delete set null) to link Contributor workspaces to their
  pathway.
number: '0024'
file: supabase/migrations/0024_designs_pathway_fk.sql
tables_touched:
- designs
- pathways-table
destructive: false
code_refs:
- supabase/migrations/0024_designs_pathway_fk.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0024_designs_pathway_fk.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

`add column pathway_id uuid references public.pathways (id) on delete set null`.

## Why

Contributor workspaces belong to a pathway; Explorer designs stay null; deleting a pathway unlinks rather than deletes.

## Risk

None.
