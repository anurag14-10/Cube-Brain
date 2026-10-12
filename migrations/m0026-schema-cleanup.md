---
name: 0026 — Schema cleanup
type: migration
schema_version: 1
aliases:
- 0026_schema_cleanup.sql
summary: 'Destructive: drops organisation_type and poc_phone from contributor_registrations and renames
  pathway_name, poc_role and pathway_contributors.org_role.'
number: '0026'
file: supabase/migrations/0026_schema_cleanup.sql
tables_touched:
- contributor-registrations
- pathway-contributors
destructive: true
code_refs:
- supabase/migrations/0026_schema_cleanup.sql
- lib/contributor-registration.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0026_schema_cleanup.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Drops two columns; renames `pathway_name` → `pathway_description`, `poc_role` → `pathway_role`, and `pathway_contributors.org_role` → `role`.

## Why

Remove unused fields and name columns for what they hold (the role is the org's relationship to the deployment).

## Risk

Data in the two dropped columns is lost; renames break any code still using the old names.
