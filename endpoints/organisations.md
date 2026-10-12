---
name: GET /api/organisations
type: endpoint
schema_version: 1
summary: Autocomplete search over the organisations registry for the contributor-registration organisation
  field; any approved user.
tags:
- organisations
- autocomplete
path: /api/organisations
methods:
- GET
file: app/api/organisations/route.ts
access: role-gated
roles:
- adopter
- pathway-contributor
- admin
- general-user
tables_read:
- user-roles
- organisations-table
integrations:
- supabase-postgres
- supabase-auth
request_shape: Query ?q=<search text> (default '')
response_shape: JSON array returned by searchOrganisations(q) (lib/organisations.ts)
status: live
code_refs:
- app/api/organisations/route.ts
- lib/organisations.ts
- components/OrganisationInput.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/organisations/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

`GET /api/organisations?q=…` → `searchOrganisations(q)` result as JSON. Called (debounced) by components/OrganisationInput.tsx.

## Enforcement

Session + `hasAnyRole` → else 401 `Unauthorized`. Because adopter is auto-granted at signup, effectively any signed-up user.

## Side effects

Read-only.

## Errors

Only the 401; search errors are whatever `searchOrganisations` returns/throws.
