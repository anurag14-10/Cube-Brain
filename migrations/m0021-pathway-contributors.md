---
name: 0021 — Create pathway_contributors
type: migration
schema_version: 1
aliases:
- 0021_pathway_contributors.sql
summary: Creates the pathway_contributors join table (one row per person per pathway, with org and org_role).
number: '0021'
file: supabase/migrations/0021_pathway_contributors.sql
tables_touched:
- pathway-contributors
- pathways-table
- organisations-table
- auth-users
destructive: false
code_refs:
- supabase/migrations/0021_pathway_contributors.sql
- app/api/pathways/[id]/join/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0021_pathway_contributors.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.pathway_contributors` (unique `(pathway_id, user_id)`) with signed-in select-all and insert-own policies.

## Why

Several people from several organisations can contribute to one pathway.

## Risk

Every signed-in user can read all memberships.
