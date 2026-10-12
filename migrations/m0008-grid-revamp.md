---
name: 0008 — Grid revamp (delete designs, rename cube_state)
type: migration
schema_version: 1
aliases:
- 0008_grid_revamp.sql
summary: 'Destructive: deletes every designs row (cascading design_documents) and renames cube_state to
  grid_state for the 4×4 grid.'
number: '0008'
file: supabase/migrations/0008_grid_revamp.sql
tables_touched:
- designs
- design-documents
destructive: true
decision: grid-revamp-four-by-four
code_refs:
- supabase/migrations/0008_grid_revamp.sql
- lib/dimensions.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0008_grid_revamp.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

`delete from public.designs;` then `alter table public.designs rename column cube_state to grid_state`.

## Why

The 7-dimension cube was replaced by the 4 dimensions × 4 stages grid (`lib/dimensions.ts`); old rows had an incompatible shape and were confirmed as test data, so they were cleared rather than migrated.

## Risk

Irreversible data loss of all adoptions and their documents at the time it ran. Safe only because the rows were test data.
