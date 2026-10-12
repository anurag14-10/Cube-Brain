---
name: SMTP via nodemailer
type: integration
schema_version: 1
summary: Delivers every Supabase Auth email (signup code, password-reset code, reauthentication code,
  invite and magic-link links) through a pooled transport with short timeouts (3–4 s), so the 5-second
  hook deadline is met.
integration_kind: email
provider: Any SMTP server (provider-agnostic)
sdk: nodemailer@^9.0.3
account_notes: The SMTP provider and account are configured only through env; not recorded in the repo.
config_vars:
- smtp-host
- smtp-port
- smtp-secure
- smtp-user
- smtp-pass
- email-from-address
code_refs:
- lib/email.ts
- app/api/auth/send-email/route.ts
- scripts/smtp-test.mjs
- package.json
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/email.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/auth/send-email/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/third-party-integrations.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Used for

Delivers every Supabase Auth email (signup code, password-reset code, reauthentication code, invite and magic-link links) through a pooled transport with short timeouts (3–4 s), so the 5-second hook deadline is met. `scripts/smtp-test.mjs` is a manual connectivity check. Two admin-approval email functions remain in `lib/email.ts` with no callers.

## Configuration

`SMTP_HOST`, `SMTP_PORT`, `SMTP_SECURE`, `SMTP_USER`, `SMTP_PASS`, `EMAIL_FROM_ADDRESS`.

## Failure behaviour

A failed send fails the hook call. There is no secondary provider. Logs record only the counts and message id, never the subject or recipient (subjects carry OTPs).

## Account

The SMTP provider and account are configured only through env; not recorded in the repo.
