---
name: 0033 — Account deletion FK changes
type: migration
schema_version: 1
aliases:
- 0033_account_deletion.sql
summary: Relaxes three FKs so self-serve account deletion cascades personal data while published content
  survives with the user reference nulled.
number: '0033'
file: supabase/migrations/0033_account_deletion.sql
tables_touched:
- published-pathways
- pathways-table
- contribution-units
- design-documents
- auth-users
destructive: false
decision: account-deletion-preserves-published-content
code_refs:
- supabase/migrations/0033_account_deletion.sql
- app/api/account/delete/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0033_account_deletion.sql
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

1. `published_pathways.published_by` → on delete set null. 2. `pathways.assembled_design_doc_id` / `published_design_doc_id` → on delete set null. 3. `contribution_units.user_id` made nullable and → on delete set null (was cascade).

## Why

`POST /api/account/delete` deletes the auth user and lets per-user tables cascade; published content must outlive its author (see specs/ACCOUNT_DELETION_SPEC.md).

Not covered by the generated `docs/wiki` database page, which stops at 0032.

## Risk

Low. The delete route nulls published units explicitly first and fails loudly if this migration is missing, rather than silently losing published units.
