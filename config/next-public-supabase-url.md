---
name: NEXT_PUBLIC_SUPABASE_URL
type: config_var
schema_version: 1
summary: The Supabase project URL, used for Postgres (REST), Auth and Storage.
var_name: NEXT_PUBLIC_SUPABASE_URL
required: true
secret: false
browser_exposed: true
read_by:
- lib-supabase-admin
- lib-supabase-client
- lib-supabase-server
- proxy
integration: supabase-postgres
environments:
- vercel-production
- docker-aws-ec2
- local-development
code_refs:
- lib/supabase/admin.ts
- lib/supabase/client.ts
- lib/supabase/server.ts
- proxy.ts
- app/api/auth/send-email/route.ts
- Dockerfile
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
  ref: docs/wiki/diffusion-cube/architecture/configuration.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it controls

The Supabase project URL, used for Postgres (REST), Auth and Storage. It is inlined into the client bundle at build time.

## Where it is read

- All three Supabase client factories in `lib/supabase/` and `proxy.ts`.
- `app/api/auth/send-email/route.ts` — builds the `/auth/v1/verify` link for invite and magic-link emails.
- `Dockerfile` — build arg.
