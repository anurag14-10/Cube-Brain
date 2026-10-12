---
name: Login / Sign up / Reset (/login)
type: page
schema_version: 1
aliases:
- sign in
- sign up
- forgot password
summary: Client page that handles password sign-in, two-step OTP sign-up with Terms/Privacy acceptance, and code-based
  password reset. It talks to Supabase Auth directly from the browser.
route: /login
file: app/login/page.tsx
access: public
roles:
- anonymous-visitor
components:
- components-organisation-input
- components-password-input
calls_endpoints:
- auth-grant-default-role
- organisations
status: live
code_refs:
- app/login/page.tsx
- lib/legal.ts
- proxy.ts
doc_refs:
- docs/wiki/diffusion-cube/application/frontend.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/login/page.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/legal.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: proxy.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/frontend.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it renders

A centred card (`LoginForm`, wrapped in Suspense) with three modes:

- **Sign in:** `signInWithPassword`. If Supabase returns `email_not_confirmed` (an abandoned sign-up), it calls
  `auth.resend({type:'signup'})` and jumps to the code step. On success it shows a toast and calls
  `router.replace(next)`, where `next` comes from `?next=` (default `/`).
- **Sign up (details → verify):** name, email, organisation
  ([OrganisationInput](../modules/components-organisation-input.md), which autocompletes from
  `GET /api/organisations`), password (min 6), plus a "Before you sign up" notice and two required
  checkboxes: Privacy consent and Terms agreement. The links open `/privacy?from=signup` and
  `/terms?from=signup` in new tabs. `auth.signUp` stores `name`, `organization`, `privacy_consent_at`,
  `terms_accepted_at` and `terms_version` (`LEGAL_VERSION`) in `user_metadata`. A masked anti-enumeration
  response (no identities) is reported as "account already exists". A live session (Confirm email turned off)
  skips the code step.
- **Verify code:** a 6-digit OTP input that auto-submits when complete. It verifies through
  `auth.verifyOtp({type:'email'})`. The resend button has a 60 s cooldown, and after 5 wrong codes the user is
  nudged to request a new one. `completeSignup()` fire-and-forgets `POST /api/auth/grant-default-role` (the
  adopter auto-grant; failure is non-fatal) and always lands on `/explore`.
- **Forgot password (email → code → new password):** `resetPasswordForEmail`, then
  `verifyOtp({type:'recovery'})`, which signs the user in, then `auth.updateUser({password})`. The UI never
  reveals whether the account exists. Rate-limit errors are mapped to friendly copy.

`?mode=signup` opens straight onto the sign-up form; this is the fallback target of the legal pages' Back
link. The OTP emails themselves are sent by Supabase through the Send Email hook (`/api/auth/send-email`), not
by this page.

## Access behaviour

- **Anonymous:** full form. `/login` is in `PUBLIC_PATHS`.
- **Signed in:** proxy.ts redirects any signed-in request for `/login` to `/`, so the page is effectively
  anonymous-only.
- `next` is used unvalidated in `router.replace(next)` after sign-in and password reset. It is normally set by
  proxy.ts to the originally requested path.
