---
name: POST /api/account/contact-sharing
type: endpoint
schema_version: 1
summary: Lets an approved contributor change their contact-sharing level from /account; writes only the
  sharing columns of their own contributor_registrations row via the service-role client.
tags:
- account
- contributor-registration
- privacy
path: /api/account/contact-sharing
methods:
- POST
file: app/api/account/contact-sharing/route.ts
access: signed-in
roles:
- pathway-contributor
tables_read:
- contributor-registrations
tables_written:
- contributor-registrations
integrations:
- supabase-postgres
- supabase-auth
request_shape: 'JSON {sharingLevel: value accepted by isSharingLevel (lib/contributor-registration.ts)}'
response_shape: 'JSON {ok: true}'
status: live
code_refs:
- app/api/account/contact-sharing/route.ts
- lib/contributor-registration.ts
- app/account/ManageAccount.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/account/contact-sharing/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

`{sharingLevel}` validated by `isSharingLevel` (400 `Invalid sharing option.`); the docs list the levels as `none | name | name_and_email`. `sharingColumns(level, user.email)` produces the column values written. Applies going forward only — nothing already shown for a published pathway is rewritten. Called from app/account/ManageAccount.tsx.

## Enforcement

Session with email (401). The caller's own `contributor_registrations` row (read through RLS, own row only) must exist with `access_status === 'approved'` → else 403 `Only approved contributors can change this.` The gate is the registration status, not a role.

## Side effects

`contributor_registrations.update(sharingColumns(...)).eq('id', registration.id)` through the service-role client — the table deliberately has no user UPDATE policy, because a row-level policy would also let a user set their own `access_status` to approved.

## Errors

500 `Could not save your choice. Please try again.`
