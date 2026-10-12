---
name: POST /api/account/delete
type: endpoint
schema_version: 1
summary: 'Self-serve permanent account deletion with password re-verification: detaches published contribution_units,
  removes draft asset files and draft units, then deletes the auth user so FK cascades take everything
  personal.'
tags:
- account
- privacy
- auth
path: /api/account/delete
methods:
- POST
file: app/api/account/delete/route.ts
access: signed-in
roles:
- adopter
- pathway-contributor
- admin
- general-user
tables_read:
- contribution-units
tables_written:
- contribution-units
- toolkit-assets-bucket
- auth-users
integrations:
- supabase-auth
- supabase-postgres
- supabase-storage
request_shape: 'JSON {password: string}'
response_shape: 'JSON {ok: true}'
status: live
code_refs:
- app/api/account/delete/route.ts
- app/api/account/delete/route.ts#L26-L39
- app/api/account/delete/route.ts#L47-L88
- supabase/migrations/0033_account_deletion.sql
- components/DeleteAccountButton.tsx
doc_refs:
- specs/ACCOUNT_DELETION_SPEC.md
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/account/delete/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0033_account_deletion.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

`{password}` (400 `Enter your password.` if empty) → `{ok:true}`. Called from components/DeleteAccountButton.tsx.

## Enforcement

Session with an email (401). The password is re-verified with `createStatelessClient().auth.signInWithPassword` on a throwaway client so the caller's cookies are untouched; Supabase's own sign-in rate limit is the only brute-force guard.

## Side effects

In this order, all via the service-role client:
1. `contribution_units.update({user_id:null})` for the caller's rows with `published_at` not null — explicit detach so published units survive. Fails loudly (500) if migration 0033 has not made `user_id` nullable / `ON DELETE SET NULL`, before anything is lost.
2. Collect `storage_path` of the caller's unpublished `toolkit-asset` units → `removeAssetObjects` (storage failure logged, not blocking).
3. Delete the caller's unpublished `contribution_units`.
4. `auth.admin.deleteUser(user.id)` — cascades `user_roles`, `contributor_registrations`, `designs` (→ `design_documents`, `adoption_queries`), `library_conversations`, `pathway_contributors`. Per migration 0033, `published_pathways` / `pathways` keep their rows with the user reference nulled.

Rows already copied to the Google Sheets conversation log are not removed.

## Errors

403 `Incorrect password.`; 429 on `over_request_rate_limit`; 500 on any other password-check error, units update/delete failure, or deleteUser failure. `user_not_found` from deleteUser (a concurrent double-submit) is treated as success.
