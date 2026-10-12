---
name: adoption_queries
type: table
schema_version: 1
summary: Write-only log of every companion-mode user message, tagged with the pathway slugs the reply
  drew on; nothing reads it yet.
table_name: adoption_queries
store_kind: table
status: live
key_columns:
- id uuid PK
- design_id uuid → designs (cascade, nullable)
- user_id uuid → auth.users (cascade, default auth.uid())
- content text
- pathway_slugs text[] (0011)
- created_at
rls: Insert-own only; no select policy for any client role
references_tables:
- designs
- auth-users
created_in: m0010-adoption-queries
code_refs:
- supabase/migrations/0010_adoption_queries.sql
- supabase/migrations/0011_adoption_queries_pathway_tags.sql
- app/api/chat/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0010_adoption_queries.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0011_adoption_queries_pathway_tags.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/chat/route.ts
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

`id`, `design_id` (nullable), `user_id` (NOT NULL, defaults to `auth.uid()`), `content` (the last user message),
`pathway_slugs` (from the turn's `<grid_update>` `pathwaysReferenced`, added in 0011), `created_at`.

## RLS

Insert-own only. No select policy — not even the owner can read it back through the API.

## Lifecycle

Inserted fire-and-forget at the end of each streamed `companion` turn in `app/api/chat/route.ts`, through the caller's
session client; an insert error is only `console.error`'d. Cascades away with the design or the auth user.

## Gotchas

- Status is `live` because it is written on every companion turn, but no code reads it — raw material for a deferred
  "what have others asked" feature.
- `/api/chat` is a public path; for a visitor with no session `auth.uid()` is null, so the NOT NULL `user_id` makes the
  insert fail silently.
