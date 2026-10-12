---
name: contributor_registrations
type: table
schema_version: 1
summary: One-time contributor registration (organisation, POC, pathway description, terms acceptance,
  contact-sharing level) with an admin approval status that gates the pathway_contributor role.
table_name: contributor_registrations
store_kind: table
status: live
key_columns:
- id uuid PK
- user_id uuid unique → auth.users (cascade)
- organisation_name
- pathway_role (was poc_role)
- pathway_description (was pathway_name)
- poc_name
- poc_email
- public_links (holds org website)
- org_id uuid → organisations (set null)
- access_status text check in (pending, approved, rejected)
- terms_accepted_at
- share_name, share_contact, contact_info
rls: Owner select + insert; admins (user_roles admin row) select all; no update policy — updates via service-role
  routes
references_tables:
- auth-users
- organisations-table
created_in: m0016-contributor-registrations
code_refs:
- supabase/migrations/0016_contributor_registrations.sql
- supabase/migrations/0023_contributor_registrations_extend.sql
- supabase/migrations/0026_schema_cleanup.sql
- lib/contributor-registration.ts
- app/api/admin/contributor-registrations/approve/route.ts
- app/api/admin/contributor-registrations/reject/route.ts
- app/api/account/contact-sharing/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0016_contributor_registrations.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0023_contributor_registrations_extend.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0026_schema_cleanup.sql
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

From 0016: `organisation_name`, `poc_name`, `poc_email`, `public_links`, `logo_url`, `declaration_accepted`,
`mou_accepted`, `consent_name/logo/quote/blog`. 0023 added `org_id`, `terms_accepted_at`, `access_status`, `share_name`,
`share_contact`, `contact_info`. 0026 dropped `organisation_type` and `poc_phone` and renamed `pathway_name` →
`pathway_description` and `poc_role` → `pathway_role`.

## RLS

Owner select and insert; `Admins can view all contributor registrations` (requires an `admin` row in `user_roles` —
the `ADMIN_EMAILS` fallback does not satisfy RLS, so the admin console reads with the service-role client).
Writers: `lib/contributor-registration.ts` (browser insert), approve/reject admin routes (service-role update of
`access_status`, `org_id`), `POST /api/account/contact-sharing` (service-role update of the three sharing columns,
approved contributors only).

## Lifecycle

Inserted once per user (unique `user_id`) → `pending` → admin approve (find-or-create the organisation, backfill
`org_id`, grant `pathway_contributor`) or reject. Cascades away with the auth user.

## Gotchas

- Holds personal data (POC name/email, `contact_info`). Never copy rows into the brain.
- `consent_*` columns are no longer collected (left false; attribution is mandatory under Terms §5.6). `logo_url` is
  unused. `declaration_accepted` and `mou_accepted` are both set from one Terms checkbox.
- `public_links` is reused to carry the organisation website to `ensureOrganisation`.
