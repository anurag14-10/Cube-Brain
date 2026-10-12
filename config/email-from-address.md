---
name: EMAIL_FROM_ADDRESS
type: config_var
schema_version: 1
summary: The From address on every email the app sends (all Supabase Auth emails delivered through the
  Send Email hook).
var_name: EMAIL_FROM_ADDRESS
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

The From address on every email the app sends (all Supabase Auth emails delivered through the Send Email hook). It must be an address the SMTP user may send as.

## Where it is read

- `lib/email.ts` — `sendEmail` (passed as `from`).
- `scripts/smtp-test.mjs` — required by the manual SMTP check.
