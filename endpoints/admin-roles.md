---
name: POST /api/admin/roles
type: endpoint
schema_version: 1
summary: Admin grants or revokes one of the four role values on a user via raw insert/delete on user_roles.
tags:
- admin
- roles
path: /api/admin/roles
methods:
- POST
file: app/api/admin/roles/route.ts
access: admin-only
roles:
- admin
tables_read:
- user-roles
tables_written:
- user-roles
integrations:
- supabase-postgres
- supabase-auth
request_shape: 'JSON {user_id: string, role: ''general_user''|''adopter''|''pathway_contributor''|''admin'',
  action: ''add''|''remove''}'
response_shape: 'JSON {ok: true}'
status: live
code_refs:
- app/api/admin/roles/route.ts
- lib/roles.ts
- components/AdminDashboard.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/admin/roles/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

`{user_id, role, action}`; `role` must be in `VALID_ROLES` and `action` `add|remove` (400 `Invalid request.`). Called from components/AdminDashboard.tsx.

## Enforcement

`isAdmin(supabase, user.email)` re-checked server-side (403 `Not authorized.`).

## Side effects

`add` → `user_roles.insert({user_id, role})` (plain insert, not upsert); `remove` → delete where `user_id` and `role`. Service-role client (user_roles has no client insert policy, migration 0006). Granting `pathway_contributor` here bypasses the contributor-registration approval path (no `contributor_registrations` row is touched).

## Errors

A duplicate `add` violates the (user_id, role) unique key and returns 500 with the Postgres message. Revoking an ADMIN_EMAILS admin's `admin` row does not remove admin access (the allow-list still matches).
