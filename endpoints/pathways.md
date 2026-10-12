---
name: GET|POST /api/pathways
type: endpoint
schema_version: 1
summary: GET lists every `pathways` workspace row (with the caller's joined flag and contributing org
  names) for any approved user; POST creates a new pathway row for a pathway_contributor.
tags:
- contributor
- pathways
path: /api/pathways
methods:
- GET
- POST
file: app/api/pathways/route.ts
access: role-gated
roles:
- adopter
- pathway-contributor
- admin
- general-user
tables_read:
- user-roles
- pathways-table
- pathway-contributors
- organisations-table
tables_written:
- pathways-table
integrations:
- supabase-postgres
- supabase-auth
request_shape: 'GET: none. POST: JSON {title: string, sector: string, description: string} — all three
  required'
response_shape: 'GET: JSON [{id, slug, title, sector, description, created_at, isContributor: bool, orgs:
  string[]}]. POST: 201 JSON {id, slug}'
status: live
code_refs:
- app/api/pathways/route.ts
- app/api/pathways/route.ts#L33-L73
- app/api/pathways/route.ts#L76-L110
- app/contribute/ContributeGrid.tsx
- components/PathwaySelector.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/pathways/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

- **GET** — no params. Returns all pathways newest first, each with `isContributor` (caller has a `pathway_contributors` row) and `orgs` (distinct `organisations.name` across that pathway's contributors, via the `pathway_contributors → organisations(name)` embed). Callers: `app/contribute/ContributeGrid.tsx`, `components/PathwaySelector.tsx`.
- **POST** — `{title, sector, description}`, each trimmed and required (400 `title required` / `sector required` / `description required`). Slug = `slugify(title)` (lowercase, strip non `[a-z0-9\s-]`, spaces → `-`, max 80 chars) made unique by suffixing `-1`, `-2` … against `pathways.slug`. Returns `201 {id, slug}`.

## Enforcement

- GET: session + `hasAnyRole` → else 401 `Unauthorized` (note: 401, not 403, for an approved-less account).
- POST: session (401) + `hasRole('pathway_contributor')` (403 `Contributor role required`).
- Reads go through the session client (RLS applies); the insert uses the service-role client (`createAdminClient`) with `created_by: user.id`.

## Side effects

POST inserts one `pathways` row. It does **not** add the creator to `pathway_contributors` — the client calls [pathways-join](pathways-join.md) separately.

## Errors

500 with the Supabase error message on select/insert failure. `uniqueSlug` loops one query per collision.
