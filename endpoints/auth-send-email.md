---
name: POST /api/auth/send-email
type: endpoint
schema_version: 1
aliases:
- Send Email hook
summary: 'Supabase Auth ''Send Email'' hook target: verifies the Standard Webhooks HMAC signature and
  delivers signup/recovery/reauthentication OTP codes and invite/magic-link emails over SMTP via lib/email.ts.'
tags:
- auth
- email
- webhook
- otp
path: /api/auth/send-email
methods:
- POST
file: app/api/auth/send-email/route.ts
access: webhook-secret
integrations:
- supabase-auth
- smtp-nodemailer
request_shape: 'Supabase Send Email hook JSON {user: {email}, email_data: {token, token_hash, redirect_to,
  email_action_type, site_url}} with webhook-id / webhook-timestamp / webhook-signature headers'
response_shape: '200 {} on success; hook error {error: {http_code, message}} with matching status'
status: live
code_refs:
- app/api/auth/send-email/route.ts
- app/api/auth/send-email/route.ts#L45-L65
- app/api/auth/send-email/route.ts#L82-L145
- lib/email.ts
- proxy.ts#L39-L41
doc_refs:
- specs/SIGNUP_OTP_SPEC.md
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/auth/send-email/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

Payload shape: [send-email-hook-payload](../contracts/send-email-hook-payload.md). Dispatch on `email_data.email_action_type`:
- `signup` → `sendSignupCodeEmail({to, code: token, expiresInMinutes: 10})`
- `recovery` → `sendPasswordResetCodeEmail` (code-based reset on /login "Forgot password?")
- `reauthentication` → `sendReauthenticationCodeEmail`
- `invite` → `sendAuthLinkEmail({kind:'invite', url: verifyUrl(token_hash,…)})`
- `magiclink` / `email` → `sendAuthLinkEmail({kind:'magiclink', url, code})`
- anything else (incl. `email_change`) → 400 `This type of email is not supported.`

`verifyUrl` builds `<NEXT_PUBLIC_SUPABASE_URL>/auth/v1/verify?token=…&type=…&redirect_to=…`, matching Supabase's own `{{ .ConfirmationURL }}`. `OTP_EXPIRY_MINUTES = 10` must be kept in sync by hand with the Supabase "Email OTP Expiration" setting (600 s).

## Enforcement

Public in proxy.ts (Supabase calls with no session). The only authentication is `verifySignature`: HMAC-SHA256 over `${webhook-id}.${webhook-timestamp}.${rawBody}` keyed with the base64 secret from `SEND_EMAIL_HOOK_SECRET` (prefix `v1,whsec_` stripped), timestamp within ±5 min, any `v1,<sig>` entry in the space-separated header matching via `timingSafeEqual`.

## Side effects

Sends one email through nodemailer (SMTP_* config). Supabase itself generates, stores, expires and verifies every OTP/link — the app never stores codes.

## Errors

500 `Email sending is not configured.` if the secret is unset; 401 `Invalid signature.`; 400 `Invalid payload.` (bad JSON / missing user email or email_data); 400 unsupported type; 500 on SMTP failure. Supabase surfaces these messages to the caller of signUp/resend.
