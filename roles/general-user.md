---
name: General User
type: role
schema_version: 1
aliases:
- general_user
summary: A role value in the Role type and the user_roles check constraint that no code branches on. Granting
  it only makes an account 'approved' (hasAnyRole) without unlocking Analyse or Contribute.
code_refs:
- lib/roles.ts#L3
- app/api/admin/roles/route.ts#L5
- components/AdminDashboard.tsx#L16-L21
- app/(app)/layout.tsx
- supabase/migrations/0006_user_roles.sql
doc_refs:
- docs/wiki/diffusion-cube/business/users-and-personas.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
role_key: general_user
persona_name: General User
granted_by: Admin only, via the 'General User' toggle on /admin (POST /api/admin/roles).
auto_granted: false
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/roles.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0006_user_roles.sql
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Who has it

Only accounts an admin has explicitly toggled. No signup path grants it today.

## How it is granted

Through `POST /api/admin/roles` from the "General User" checkbox on `/admin`. Migration 0006's comment describes a default `general_user` row "created at signup approval". That belonged to the retired approval-email flow (`specs/SIGNUP_APPROVAL_OPTIONS.md`) and was replaced by auto-granting `adopter`.

## What it unlocks

Only what *any* role unlocks, because every gate that matters checks a specific role:
- It counts as approved for `hasAnyRole`, which opens the `(app)` group (`/adoptions`, `/wiki`), `GET /api/pathways`, and the non-companion `/api/chat` modes.
- On `/analyse` it gets the "Ask an admin to grant you Explorer access" gate. On `/contribute` it gets the registration form.

## Gaps vs product intent

- It is a role with no distinct behaviour. `docs/wiki` (users-and-personas) says so too.
- **The non-companion chat modes are open to it.** `analysis-doc`, `executive-summary`, `plan-document`, `extract-insights`, `pathway-draft` and `pathway-exec-summary` check only `hasAnyRole`, so a General User can call them directly. Prompting is the only constraint. See [API route is the real enforcement](../rules/api-route-is-real-enforcement.md).
