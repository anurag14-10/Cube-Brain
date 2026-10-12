---
name: 0019 — Create organisations
type: migration
schema_version: 1
aliases:
- 0019_organisations.sql
summary: Creates the organisations registry (unique name, url, canonical_role) with signed-in read.
number: '0019'
file: supabase/migrations/0019_organisations.sql
tables_touched:
- organisations-table
destructive: false
code_refs:
- supabase/migrations/0019_organisations.sql
- lib/organisations.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0019_organisations.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.organisations` with a signed-in select policy and no write policy.

## Why

Back the organisation autocomplete on the contributor form, with a canonical role label per org.

## Risk

Low. Writes depend on the service-role helper `ensureOrganisation`.
