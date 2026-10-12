---
name: 0006 — Create user_roles
type: migration
schema_version: 1
aliases:
- 0006_user_roles.sql
summary: Creates user_roles for explicit multi-role grants (general_user, adopter, pathway_contributor)
  with select-own RLS only.
number: '0006'
file: supabase/migrations/0006_user_roles.sql
tables_touched:
- user-roles
- auth-users
destructive: false
code_refs:
- supabase/migrations/0006_user_roles.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0006_user_roles.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.user_roles` (PK `(user_id, role)`, role check), enables RLS with a single select-own policy — no client write policy.

## Why

A user may hold several roles; role assignment is backend-only (service role or dashboard).

## Risk

Low. Every write path must use the service-role client.
