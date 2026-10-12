---
name: Supabase Auth
type: integration
schema_version: 1
summary: Email + password accounts confirmed with a 6-digit OTP, password reset by OTP, and session cookies
  refreshed in `proxy.ts`.
integration_kind: auth
provider: Supabase
sdk: '@supabase/ssr@^0.12.0'
account_notes: Hook and OTP-expiry settings live in the Supabase dashboard (Auth Hooks; Email OTP Expiration
  set to 600 s per the code comment), not in the repo.
config_vars:
- next-public-supabase-url
- next-public-supabase-anon-key
- supabase-service-role-key
- send-email-hook-secret
code_refs:
- proxy.ts
- lib/supabase/server.ts
- app/api/auth/send-email/route.ts
- app/api/account/delete/route.ts
- package.json
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: proxy.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/supabase/server.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/third-party-integrations.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Used for

Email + password accounts confirmed with a 6-digit OTP, password reset by OTP, and session cookies refreshed in `proxy.ts`. With the **Send Email hook**, Supabase generates and verifies codes but POSTs them to `/api/auth/send-email`, which delivers them over SMTP. The Auth Admin API (service role) is used for `deleteUser` (account deletion, admin reject) and `listUsers` (/admin). A stateless anon client re-verifies the password before account deletion.

## Configuration

`NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY` (admin API), `SEND_EMAIL_HOOK_SECRET` (hook signature).

## Failure behaviour

If the hook secret is missing or the signature fails, the hook returns an error and no auth email is sent; Supabase reports the error. SMTP failures surface the same way. The sign-in rate limit on password re-checks returns 429.

## Account

Hook and OTP-expiry settings live in the Supabase dashboard (Auth Hooks; Email OTP Expiration set to 600 s per the code comment), not in the repo.
