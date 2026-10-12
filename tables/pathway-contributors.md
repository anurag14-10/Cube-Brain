---
name: pathway_contributors
type: table
schema_version: 1
summary: Membership join table linking a contributor to a pathway workspace, with their organisation and
  role; the membership check every contributor route relies on.
table_name: pathway_contributors
store_kind: table
status: live
key_columns:
- id uuid PK
- pathway_id → pathways (cascade)
- user_id → auth.users (cascade)
- org_id → organisations (set null)
- role text (was org_role)
- joined_at
- unique (pathway_id, user_id)
rls: Signed-in select all rows; insert own row only
references_tables:
- pathways-table
- auth-users
- organisations-table
created_in: m0021-pathway-contributors
code_refs:
- supabase/migrations/0021_pathway_contributors.sql
- supabase/migrations/0026_schema_cleanup.sql
- app/api/pathways/[id]/join/route.ts
- app/api/pathways/route.ts
- app/api/pathways/assemble/route.ts
- lib/toolkit-assets-server.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0021_pathway_contributors.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0026_schema_cleanup.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/pathways/[id]/join/route.ts
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

`pathway_id`, `user_id`, `org_id`, `role` (renamed from `org_role` in 0026 — the org's relationship to the deployment,
from the registration's `pathway_role`), `joined_at`; unique `(pathway_id, user_id)`.

## RLS

Any signed-in user can read every row; users insert only their own row. No update/delete policy.

## Lifecycle

Inserted by `POST /api/pathways/[id]/join` through the caller's session client (after find-or-create of the organisation).
Read by `GET /api/pathways`, `POST /api/pathways/assemble` and `authorizePathwayContributor` in
`lib/toolkit-assets-server.ts` as the per-pathway membership gate. Cascades with the pathway or the auth user.

## Gotchas

- Every signed-in user can enumerate who contributes to which pathway.
- Membership is the second gate after the `pathway_contributor` role for assemble and toolkit-asset routes.
