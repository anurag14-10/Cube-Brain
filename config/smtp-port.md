---
name: SMTP_PORT
type: config_var
schema_version: 1
summary: 'SMTP port: 587 for STARTTLS, 465 for implicit TLS.'
var_name: SMTP_PORT
required: false
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
contested:
- field: required
  readings:
  - 'docs/wiki configuration.md: Required = Yes'
  - 'code: optional — falls back to a default port when unset'
  note: The code supports optional.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it controls

SMTP port: 587 for STARTTLS, 465 for implicit TLS. The code defaults it when unset. It also decides `secure` unless `SMTP_SECURE` overrides it.

## Where it is read

- `lib/email.ts`, `scripts/smtp-test.mjs` — `Number(process.env.SMTP_PORT ?? <default>)`.
