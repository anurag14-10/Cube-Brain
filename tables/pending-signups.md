---
name: pending_signups
type: table
schema_version: 1
summary: Inert pre-auth signup queue from the retired admin-approval signup flow; RLS on with zero policies,
  no code references it.
table_name: pending_signups
store_kind: table
status: inert
key_columns:
- id uuid PK
- name
- email
- organization
- status check in (pending, approved, rejected)
- approval_token unique
- created_at
- approved_at
rls: RLS enabled with zero policies — service-role only
created_in: m0005-pending-signups
code_refs:
- supabase/migrations/0005_pending_signups.sql
- lib/email.ts
- lib/supabase/admin.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0005_pending_signups.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/email.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/supabase/admin.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

`name`, `email` (indexed), `organization`, `status`, `approval_token` (unique, single-use), `created_at`, `approved_at`.

## RLS

Enabled with no policies: anon/authenticated access is denied; only the service-role client could touch it.

## Lifecycle

Backed the old "request access → admin approves → set password" signup. Superseded by self-serve OTP signup with
`adopter` auto-granted. No code reads or writes it. Leftovers of that flow remain as dead code:
`sendAdminApprovalEmail` / `sendUserApprovedEmail` in `lib/email.ts` (no callers) and `POST /api/admin/reject`.

## Gotchas

- May still hold personal data from the old flow. Never copy rows.
