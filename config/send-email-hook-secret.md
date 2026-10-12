---
name: SEND_EMAIL_HOOK_SECRET
type: config_var
schema_version: 1
summary: The Standard Webhooks secret (format `v1,whsec_<base64>`) that verifies Supabase's Send Email
  Auth Hook calls.
var_name: SEND_EMAIL_HOOK_SECRET
required: true
secret: true
browser_exposed: false
integration: supabase-auth
environments:
- vercel-production
- docker-aws-ec2
- local-development
code_refs:
- app/api/auth/send-email/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/auth/send-email/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/architecture/configuration.md
contested:
- field: summary
  readings:
  - 'docs/wiki configuration.md: "secret(s) (space-separated for rotation)"'
  - 'code: the env var is decoded as ONE secret; it is the webhook-signature HEADER that is a space-separated
    list of v1 signatures (any match passes)'
  note: The code supports the second reading. Rotation works by Supabase sending several signatures, not
    by listing several secrets in the env var.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it controls

The Standard Webhooks secret (format `v1,whsec_<base64>`) that verifies Supabase's Send Email Auth Hook calls. The endpoint is public, so this signature check is its only authentication. If it is missing, the hook returns 500 and no auth email (signup OTP, password reset) is sent.

## Where it is read

- `app/api/auth/send-email/route.ts` — `verifySignature`: HMAC-SHA256 over `id.timestamp.body` with a 5-minute tolerance. This is a route handler, not a registry module, so `read_by` is empty.
