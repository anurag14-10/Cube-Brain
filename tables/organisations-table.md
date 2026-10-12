---
name: organisations (table)
type: table
schema_version: 1
aliases:
- organisations
summary: The app's organisation registry used by contributor registration autocomplete and pathway_contributors.org_id;
  written only server-side by ensureOrganisation.
table_name: organisations
store_kind: table
status: live
key_columns:
- id uuid PK
- name text unique
- url text (set once, never overwritten)
- canonical_role text
- created_at
rls: Signed-in select; no insert/update policy — writes via service-role client
created_in: m0019-organisations
code_refs:
- supabase/migrations/0019_organisations.sql
- lib/organisations.ts
- app/api/organisations/route.ts
- app/api/admin/contributor-registrations/approve/route.ts
- app/api/pathways/[id]/join/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0019_organisations.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/organisations.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/organisations/route.ts
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

`id`, `name` (unique), `url`, `canonical_role` (Org Role label pre-filled when an existing org is picked), `created_at`.

## RLS

`Signed-in users can view organisations`. No write policy. All access in code is through `lib/organisations.ts`, which
uses the service-role client for both `searchOrganisations` (behind `GET /api/organisations`, signed-in check) and
`ensureOrganisation` (case-insensitive find-or-create).

## Lifecycle

Created on demand by `ensureOrganisation`, called from admin approval of a contributor registration and from
`POST /api/pathways/[id]/join`. Never deleted by the app.

## Gotchas

- Not the brain's `organisations/` folder — that holds real-world organisations; this is the app's DB table.
- `url` is only set on create; a later contributor naming the same org cannot overwrite it.
- Matching is by `ilike` on the trimmed name, so near-duplicate spellings create separate rows.
