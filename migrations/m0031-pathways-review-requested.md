---
name: 0031 — Add pathways.review_requested
type: migration
schema_version: 1
aliases:
- 0031_pathways_review_requested.sql
summary: Adds review_requested to pathways — set by assemble, cleared by admin publish.
number: '0031'
file: supabase/migrations/0031_pathways_review_requested.sql
tables_touched:
- pathways-table
destructive: false
code_refs:
- supabase/migrations/0031_pathways_review_requested.sql
- app/api/pathways/assemble/route.ts
- app/api/admin/pathways/publish/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0031_pathways_review_requested.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

`add column review_requested boolean not null default false`.

## Why

Flag assembled pathways awaiting admin review (two-step publish). The migration has no comment.

## Risk

None.
