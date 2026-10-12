---
name: POST /api/admin/contributor-registrations/reject
type: endpoint
schema_version: 1
summary: Admin rejects a contributor registration by setting access_status='rejected'; no role or account
  change.
tags:
- admin
- contributor-registration
path: /api/admin/contributor-registrations/reject
methods:
- POST
file: app/api/admin/contributor-registrations/reject/route.ts
access: admin-only
roles:
- admin
tables_read:
- user-roles
tables_written:
- contributor-registrations
integrations:
- supabase-postgres
- supabase-auth
request_shape: 'JSON {registration_id: string}'
response_shape: 'JSON {ok: true}'
status: live
code_refs:
- app/api/admin/contributor-registrations/reject/route.ts
- components/AdminContributorRegistrationsPanel.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/admin/contributor-registrations/reject/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

`{registration_id}` (400 if not a string). Called from components/AdminContributorRegistrationsPanel.tsx.

## Enforcement

`isAdmin` → else 403.

## Side effects

`contributor_registrations.update({access_status:'rejected'})` by id, service-role client. Does not revoke a `pathway_contributor` role if one was already granted (e.g. rejecting after an earlier approval leaves the role in place).

## Errors

500 with Supabase message.
