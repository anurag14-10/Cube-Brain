---
name: SUPABASE_SERVICE_ROLE_KEY
type: config_var
schema_version: 1
summary: Supabase service-role key.
var_name: SUPABASE_SERVICE_ROLE_KEY
required: true
secret: true
browser_exposed: false
read_by:
- lib-supabase-admin
integration: supabase-postgres
environments:
- vercel-production
- docker-aws-ec2
- local-development
code_refs:
- lib/supabase/admin.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/supabase/admin.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/architecture/configuration.md
contested:
- field: summary
  readings:
  - 'lib/supabase/admin.ts header comment: "Only used from Route Handlers for the signup-approval flow"'
  - 'code usage: imported by ~20 route handlers, server pages and lib modules (publish, delete, toolkit
    assets, explore public reads)'
  note: The header comment is stale; usage is far broader.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it controls

Supabase service-role key. It bypasses RLS entirely and is the only way to write `user_roles`, `published_pathways`, `organisations`, `contribution_units` and the `toolkit-assets` bucket, or to call the Auth Admin API (deleteUser, listUsers). Server-only: it must never carry a `NEXT_PUBLIC_` prefix.

## Where it is read

- `lib/supabase/admin.ts` — `createAdminClient()`. Imported by the admin routes, account deletion, assemble/publish, toolkit-asset routes, `lib/organisations.ts`, `lib/toolkit-assets-server.ts`, `lib/library-wiki-loader.ts`, `app/explore/page.tsx` and `app/admin/page.tsx`.
