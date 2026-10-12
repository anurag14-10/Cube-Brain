---
name: user_roles
type: table
schema_version: 1
summary: Multi-role grants per user (general_user, adopter, pathway_contributor, admin); users can read
  their own rows, every write goes through the service-role client.
table_name: user_roles
store_kind: table
status: live
key_columns:
- (user_id, role) PK
- user_id uuid → auth.users (cascade)
- role text check in (general_user, adopter, pathway_contributor, admin)
- created_at
rls: Select own rows only; no insert/update/delete policy — writes via service-role client
references_tables:
- auth-users
created_in: m0006-user-roles
code_refs:
- supabase/migrations/0006_user_roles.sql
- supabase/migrations/0007_admin_role.sql
- lib/roles.ts
- app/api/auth/grant-default-role/route.ts
- app/api/admin/roles/route.ts
- app/api/admin/contributor-registrations/approve/route.ts
- app/admin/page.tsx
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0006_user_roles.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0007_admin_role.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/roles.ts
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

Composite PK `(user_id, role)`; `role` check constraint widened in 0007 to add `admin`; `created_at`.

## RLS

One policy: users select their own rows (`lib/roles.ts` `hasRole` / `hasAnyRole` use the session client). No client
write policy. Writers, all service-role:

- `POST /api/auth/grant-default-role` — inserts `adopter` right after signup (unique-violation treated as success).
- `POST /api/admin/contributor-registrations/approve` — upserts `pathway_contributor`.
- `POST /api/admin/roles` — admin grant/revoke of any role.

`app/admin/page.tsx` reads every row via the service-role client.

## Lifecycle

Rows cascade away with the auth user. The `admin` role is backed up by the `ADMIN_EMAILS` allow-list in
`lib/roles.ts` (`isAdmin`), so an admin is never locked out if their row disappears.

## Gotchas

- Migration 0007 seeds `admin` rows for two named accounts by email (only if those accounts already existed). The
  addresses are in the migration file; they are deliberately not copied here.
- The 0006 comment describes a `general_user` row created at "signup approval" — that admin-approval signup flow is gone;
  current signup auto-grants `adopter` instead.
