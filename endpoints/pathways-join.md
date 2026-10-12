---
name: POST /api/pathways/[id]/join
type: endpoint
schema_version: 1
summary: Adds the calling pathway_contributor to a pathway's `pathway_contributors`, resolving (or creating)
  their organisation from their contributor registration; idempotent.
tags:
- contributor
- pathways
- organisations
path: /api/pathways/[id]/join
methods:
- POST
file: app/api/pathways/[id]/join/route.ts
access: role-gated
roles:
- pathway-contributor
tables_read:
- user-roles
- pathways-table
- pathway-contributors
- contributor-registrations
- organisations-table
tables_written:
- pathway-contributors
- organisations-table
integrations:
- supabase-postgres
- supabase-auth
request_shape: Path param id = pathways.id (uuid); no body
response_shape: 'JSON {ok: true} or {ok: true, alreadyJoined: true}'
status: live
code_refs:
- app/api/pathways/[id]/join/route.ts
- lib/organisations.ts
- components/PathwaySelector.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/pathways/[id]/join/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

`POST /api/pathways/<pathway uuid>/join`, no body. Returns `{ok:true}` on insert, `{ok:true, alreadyJoined:true}` if a `pathway_contributors` row for (pathway, caller) already exists.

## Enforcement

Session (401) + `hasRole('pathway_contributor')` (403). Pathway existence checked through the session client (404 `Pathway not found`).

## Side effects

1. Reads the caller's `contributor_registrations (organisation_name, pathway_role, public_links)`; blank `organisation_name` → 400 `No contributor registration found. Please complete registration first.`
2. `ensureOrganisation(orgName, orgRole, orgUrl)` (lib/organisations.ts) finds or creates the `organisations` row — the same helper the registration-approve route uses, so the two paths converge on one org row.
3. Inserts `pathway_contributors {pathway_id, user_id, org_id, role: pathway_role}` through the **session** client (allowed by the table's own-row RLS insert policy).

## Errors

400 (no registration), 404 (no pathway), 500 (`ensureOrganisation` throw or insert error, message passed through).
