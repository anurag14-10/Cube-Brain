---
name: 0028 — Add pathways.description
type: migration
schema_version: 1
aliases:
- 0028_pathways_description.sql
summary: Adds a short description to pathways for the duplicate check and the pathway picker.
number: '0028'
file: supabase/migrations/0028_pathways_description.sql
tables_touched:
- pathways-table
destructive: false
code_refs:
- supabase/migrations/0028_pathways_description.sql
- app/api/pathways/check-similar/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0028_pathways_description.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

`add column description text not null default ''`.

## Why

Let the "start a new pathway" similarity check compare more than titles, and disambiguate similar titles in the picker.

## Risk

None.
