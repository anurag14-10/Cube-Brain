---
name: NEXT_PUBLIC_SUPPORT_EMAIL
type: config_var
schema_version: 1
summary: The "Contact Us" address substituted for `{{SUPPORT_EMAIL}}` in `content/legal/terms.md` and
  `privacy.md`.
var_name: NEXT_PUBLIC_SUPPORT_EMAIL
required: false
secret: false
browser_exposed: true
read_by:
- lib-legal
environments:
- vercel-production
- local-development
code_refs:
- lib/legal.ts
- Dockerfile
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/legal.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: Dockerfile
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/architecture/configuration.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it controls

The "Contact Us" address substituted for `{{SUPPORT_EMAIL}}` in `content/legal/terms.md` and `privacy.md`. If unset, `lib/legal.ts` falls back to a hard-coded address (not recorded here). The Grievance Officer's address in those documents is literal text, not this variable.

## Where it is read

- `lib/legal.ts`.

It is inlined at build time. The `Dockerfile` does not declare it as a build arg and `.dockerignore` excludes `.env*`, so the Docker/AWS image always uses the hard-coded fallback. That is why `docker-aws-ec2` is not listed under `environments`.
