---
name: SMTP_HOST
type: config_var
schema_version: 1
summary: SMTP server host.
var_name: SMTP_HOST
required: true
secret: false
browser_exposed: false
read_by:
- lib-email
- scripts-smtp-test
integration: smtp-nodemailer
environments:
- vercel-production
- docker-aws-ec2
- local-development
code_refs:
- lib/email.ts
- scripts/smtp-test.mjs
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/email.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: scripts/smtp-test.mjs
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/architecture/configuration.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it controls

SMTP server host. The transport is provider-agnostic. If unset, `getTransport` throws a clear error rather than letting nodemailer fall back to localhost.

## Where it is read

- `lib/email.ts` — `getTransport` (a lazily created pooled transport).
- `scripts/smtp-test.mjs`.
