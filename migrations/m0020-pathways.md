---
name: 0020 — Create pathways
type: migration
schema_version: 1
aliases:
- 0020_pathways.sql
summary: Creates the canonical pathways entity (slug, title, sector, created_by, content_cache) with a
  role-gated insert policy.
number: '0020'
file: supabase/migrations/0020_pathways.sql
tables_touched:
- pathways-table
- user-roles
- auth-users
destructive: false
code_refs:
- supabase/migrations/0020_pathways.sql
- app/api/pathways/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0020_pathways.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.pathways` with signed-in select and an insert policy requiring a `pathway_contributor` row in `user_roles`.

## Why

A pathway exists independently of any contributor; `content_cache` holds the latest assembled text for fast reads.

## Risk

The insert policy is bypassed in practice — the create route uses the service-role client.
