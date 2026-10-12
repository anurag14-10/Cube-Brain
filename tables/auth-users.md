---
name: auth.users (Supabase Auth)
type: table
schema_version: 1
aliases:
- auth_users
summary: Supabase-managed auth user table; the FK target of almost every app table, whose delete behaviour
  defines what account deletion removes and what survives.
table_name: auth.users
store_kind: auth-schema
status: live
key_columns:
- id uuid PK
- email
rls: Supabase-managed (auth schema); the app uses the Auth API and the service-role Auth Admin API, never
  direct SQL
code_refs:
- supabase/migrations/0001_designs.sql
- supabase/migrations/0033_account_deletion.sql
- app/api/account/delete/route.ts
- app/api/admin/reject/route.ts
- app/admin/page.tsx
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0001_designs.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0033_account_deletion.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/account/delete/route.ts
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

Managed by Supabase Auth. The app relies on `id` and `email`.

## RLS

Not exposed through the REST API. Access is via `supabase.auth.*` (session) and `auth.admin.*` (service role):
`deleteUser` in `POST /api/account/delete` and `POST /api/admin/reject`, `listUsers` in `app/admin/page.tsx`,
`getUserById` in the dead push route.

## Lifecycle

Created by email + password signup confirmed with a 6-digit OTP (emails delivered via the Send Email hook).
Not created by any migration. On delete:

| Cascades | Set null |
|---|---|
| designs (→ design_documents, adoption_queries), user_roles, contributor_registrations, pathway_contributors, library_conversations, design_documents, adoption_queries | pathways.created_by, published_pathways.published_by (0033), contribution_units.user_id (0033) |

## Gotchas

- Before 0033, `published_pathways.published_by` had no ON DELETE action and blocked deleting anyone who had published,
  and `contribution_units.user_id` cascaded published units away.
- Migration 0007 reads emails from this table to seed admins.
