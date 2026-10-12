---
name: ADMIN_EMAILS
type: config_var
schema_version: 1
summary: Comma-separated, case-insensitive allow-list of admin email addresses.
var_name: ADMIN_EMAILS
required: false
secret: false
browser_exposed: false
read_by:
- lib-roles
- lib-email
environments:
- vercel-production
- docker-aws-ec2
- local-development
code_refs:
- lib/roles.ts
- lib/email.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/roles.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/email.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/architecture/configuration.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it controls

Comma-separated, case-insensitive allow-list of admin email addresses. `isAdmin` in `lib/roles.ts` treats any listed address as admin even without an `admin` row in `user_roles` — the permanent bootstrap fallback introduced alongside migration 0007. Holds personal email addresses: never record its value.

## Where it is read

- `lib/roles.ts` — `isAdminEmail` / `isAdmin` (live; gates every admin route and the /admin page).
- `lib/email.ts` — `sendAdminApprovalEmail` addresses all admins, but that function has no callers (relic of the retired admin-approval signup), so this read is dead code.

Note: the `contributor_registrations` admin RLS policy checks `user_roles` only, so an env-only admin must go through service-role reads.
