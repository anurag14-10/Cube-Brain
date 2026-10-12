---
name: POST /api/auth/grant-default-role
type: endpoint
schema_version: 1
summary: Called by the login page right after sign-up to give the new account the 'adopter' role (idempotent),
  so the Analyse flow is open with no admin approval.
tags:
- auth
- roles
- signup
path: /api/auth/grant-default-role
methods:
- POST
file: app/api/auth/grant-default-role/route.ts
access: signed-in
roles:
- general-user
- adopter
- pathway-contributor
- admin
tables_written:
- user-roles
integrations:
- supabase-auth
- supabase-postgres
request_shape: none
response_shape: 'JSON {ok: true}'
status: live
code_refs:
- app/api/auth/grant-default-role/route.ts
- app/login/page.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/auth/grant-default-role/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/login/page.tsx
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

Empty POST → `{ok:true}`. app/login/page.tsx fires it after a successful sign-up and swallows any failure (`.catch(() => {})`).

## Enforcement

Session only (401 `Not authenticated.`). Any signed-in user may call it, and it always grants exactly `adopter` to the caller — so it is also the self-serve way a user whose roles were revoked by an admin can regain `adopter`.

## Side effects

`user_roles.insert({user_id, role:'adopter'})` via service-role client (no client insert policy, migration 0006).

## Errors

Unique violation `23505` is treated as success; other errors → 500. Because the client ignores failures, a failed grant leaves a zero-role ("awaiting approval") account.
