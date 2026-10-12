---
name: 0007 — Add admin role
type: migration
schema_version: 1
aliases:
- 0007_admin_role.sql
summary: Widens the user_roles role check to include admin and seeds admin rows for two existing accounts
  by email.
number: '0007'
file: supabase/migrations/0007_admin_role.sql
tables_touched:
- user-roles
- auth-users
destructive: false
code_refs:
- supabase/migrations/0007_admin_role.sql
- lib/roles.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0007_admin_role.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Drops and re-adds `user_roles_role_check` with `admin` added, then inserts `admin` rows for two named accounts selected from `auth.users` by email (`on conflict do nothing`). The addresses are in the file and are not reproduced here.

## Why

Promote admin from a pure `ADMIN_EMAILS` allow-list to a database-managed role, keeping the env var as a permanent bootstrap fallback in `lib/roles.ts`.

## Risk

Hard-codes personal emails in schema history. Seeds only accounts that already existed when it ran.
