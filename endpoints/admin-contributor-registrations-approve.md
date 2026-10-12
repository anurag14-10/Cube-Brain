---
name: POST /api/admin/contributor-registrations/approve
type: endpoint
schema_version: 1
summary: 'Admin approves a contributor registration: backfills org_id via ensureOrganisation, sets access_status=''approved'',
  and upserts the pathway_contributor role.'
tags:
- admin
- contributor-registration
- roles
path: /api/admin/contributor-registrations/approve
methods:
- POST
file: app/api/admin/contributor-registrations/approve/route.ts
access: admin-only
roles:
- admin
tables_read:
- user-roles
- contributor-registrations
- organisations-table
tables_written:
- contributor-registrations
- organisations-table
- user-roles
integrations:
- supabase-postgres
- supabase-auth
request_shape: 'JSON {registration_id: string}'
response_shape: 'JSON {ok: true}'
status: live
code_refs:
- app/api/admin/contributor-registrations/approve/route.ts
- lib/organisations.ts
- components/AdminContributorRegistrationsPanel.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/admin/contributor-registrations/approve/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

`{registration_id}` (400 if not a string). Called as `/api/admin/contributor-registrations/${action}` from components/AdminContributorRegistrationsPanel.tsx.

## Enforcement

`isAdmin` → else 403. Service-role client throughout.

## Side effects

1. Reads `contributor_registrations (user_id, organisation_name, pathway_role, public_links, org_id)`; 404 if missing.
2. If `org_id` null → `ensureOrganisation(organisation_name, pathway_role, public_links)` and writes `org_id` (the "admin confirms the org on approval" step from migration 0023).
3. `access_status = 'approved'`.
4. `user_roles.upsert({user_id, role:'pathway_contributor'}, onConflict 'user_id,role')` — the role, not `access_status`, is what the contribute gate and every contributor API route check.

## Errors

404 registration not found; 500 on ensureOrganisation throw or either write. Steps are not transactional: a failure after step 3 leaves an approved registration with no role.
