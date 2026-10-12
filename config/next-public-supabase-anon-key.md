---
name: NEXT_PUBLIC_SUPABASE_ANON_KEY
type: config_var
schema_version: 1
summary: Supabase anon (publishable) key.
var_name: NEXT_PUBLIC_SUPABASE_ANON_KEY
required: true
secret: false
browser_exposed: true
read_by:
- lib-supabase-client
- lib-supabase-server
- proxy
integration: supabase-auth
environments:
- vercel-production
- docker-aws-ec2
- local-development
code_refs:
- lib/supabase/client.ts
- lib/supabase/server.ts
- proxy.ts
- Dockerfile
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/supabase/client.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/supabase/server.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/architecture/configuration.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it controls

Supabase anon (publishable) key. Every browser and session client uses it, so all access through it is limited by RLS. It is public by design and inlined into the client bundle at build time.

## Where it is read

- `lib/supabase/client.ts` — browser client.
- `lib/supabase/server.ts` — cookie-bound session client and the stateless client used to re-check a password.
- `proxy.ts` — middleware session refresh and the route gate.
- `Dockerfile` — must be passed as a build arg, because it is inlined at `next build`.
