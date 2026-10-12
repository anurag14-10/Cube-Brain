---
name: 0023 — Extend contributor_registrations
type: migration
schema_version: 1
aliases:
- 0023_contributor_registrations_extend.sql
summary: Adds org_id, terms_accepted_at, access_status (pending/approved/rejected), share_name, share_contact
  and contact_info, and an admin select-all policy.
number: '0023'
file: supabase/migrations/0023_contributor_registrations_extend.sql
tables_touched:
- contributor-registrations
- organisations-table
- user-roles
destructive: false
code_refs:
- supabase/migrations/0023_contributor_registrations_extend.sql
- lib/contributor-registration.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0023_contributor_registrations_extend.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Adds the six columns and `Admins can view all contributor registrations` (requires an `admin` row in `user_roles`).

## Why

Drive the admin approval gate and record contact-sharing consent surfaced to Explorers.

## Risk

The admin policy does not honour the `ADMIN_EMAILS` fallback, so the admin console uses the service role.
