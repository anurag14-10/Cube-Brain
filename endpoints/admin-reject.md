---
name: POST /api/admin/reject
type: endpoint
schema_version: 1
summary: Admin rejects a pending signup by deleting the Supabase Auth user outright (cascading everything
  personal).
tags:
- admin
- auth
path: /api/admin/reject
methods:
- POST
file: app/api/admin/reject/route.ts
access: admin-only
roles:
- admin
tables_read:
- user-roles
tables_written:
- auth-users
integrations:
- supabase-auth
request_shape: 'JSON {user_id: string}'
response_shape: 'JSON {ok: true}'
status: live
code_refs:
- app/api/admin/reject/route.ts
- components/AdminDashboard.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/admin/reject/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

`{user_id}` (400 if not a string). Called from components/AdminDashboard.tsx.

## Enforcement

`isAdmin` → else 403.

## Side effects

`createAdminClient().auth.admin.deleteUser(user_id)` — removes the `auth.users` row; FK cascades take roles, registrations, designs, etc. (the same cascade path as [account-delete](account-delete.md), but **without** its pre-step that detaches published `contribution_units` or removes draft asset files). The person can sign up again with the same email. With adopter auto-granted at signup there are few zero-role "pending" users left to reject, so this is mostly a hard-delete tool.

## Errors

500 with the Auth error message.
