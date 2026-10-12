---
name: Supabase Postgres
type: integration
schema_version: 1
summary: 'All persistence: 11 live tables, 3 inert and 3 dropped, defined by 34 migrations in `supabase/migrations/`
  (schema of record; no ORM, raw `.from()` calls).'
integration_kind: database
provider: Supabase
sdk: '@supabase/supabase-js@^2.110.0'
account_notes: Plan and ownership of the Supabase project are not recorded in the repo.
config_vars:
- next-public-supabase-url
- next-public-supabase-anon-key
- supabase-service-role-key
code_refs:
- lib/supabase/admin.ts
- lib/supabase/client.ts
- lib/supabase/server.ts
- supabase/migrations/0001_designs.sql
- package.json
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/supabase/admin.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/supabase/client.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/third-party-integrations.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Used for

All persistence: 11 live tables, 3 inert and 3 dropped, defined by 34 migrations in `supabase/migrations/` (schema of record; no ORM, raw `.from()` calls). Three client kinds:

- Browser client (`lib/supabase/client.ts`, `@supabase/ssr` `createBrowserClient`) — RLS-scoped.
- Server session client (`lib/supabase/server.ts`, cookie-bound) — RLS-scoped.
- Service-role client (`lib/supabase/admin.ts`) — bypasses RLS. Used for admin work, publishing, toolkit assets and public reads for anonymous visitors.

## Configuration

`NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`. `@supabase/ssr@^0.12.0` provides the cookie and browser clients.

## Failure behaviour

There is no uniform handling. Most routes return a 500 or error JSON. RLS violations come back as Postgres errors. Fire-and-forget writes (`adoption_queries`) fail silently.

## Account

Plan and ownership of the Supabase project are not recorded in the repo.
