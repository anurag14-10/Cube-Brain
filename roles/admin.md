---
name: Admin
type: role
schema_version: 1
aliases:
- admin
summary: Role/registration/pathway management. An admin is anyone with an 'admin' user_roles row OR an
  email on the ADMIN_EMAILS allow-list (permanent bootstrap fallback). Gates /admin and every app/api/admin/*
  route.
code_refs:
- lib/roles.ts#L21-L39
- app/admin/page.tsx
- app/api/admin/roles/route.ts
- app/api/admin/pathways/publish/route.ts
- app/api/toolkit-assets/[id]/download/route.ts
doc_refs:
- docs/wiki/diffusion-cube/business/users-and-personas.md
- specs/ACCOUNT_DELETION_SPEC.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
role_key: admin
persona_name: Admin
granted_by: Another admin via POST /api/admin/roles, or by listing the email in the ADMIN_EMAILS environment
  variable (no DB row needed).
auto_granted: false
prerequisites:
- A signed-in session; plus either an 'admin' user_roles row or an ADMIN_EMAILS match
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/roles.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/admin/page.tsx
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Who has it

The people who run the Program Team's review-and-publish job and the Solution Team's user management. `isAdmin()` returns true for an `ADMIN_EMAILS` match or an `admin` row in `user_roles`.

## How it is granted

`ADMIN_EMAILS` (comma-separated, compared case-insensitively) is a deliberate permanent fallback, so there is never a bootstrapping problem. All other grants are ordinary `admin` rows added on `/admin` through `POST /api/admin/roles`. An `ADMIN_EMAILS` admin who deletes the account and signs up again is admin again.

## What it unlocks

- The `/admin` page: users and roles (AdminDashboard), contributor registrations, and pathways including toolkit asset previews. A non-admin is redirected to `/`.
- `POST /api/admin/roles` (add or remove any of the four roles), `/api/admin/reject` (deletes a user's auth account), `/api/admin/contributor-registrations/approve|reject`, `/api/admin/pathways/publish` (copies the assembled document to `published_pathways` and publishes the listed toolkit assets) and `/api/admin/pathways/delete`.
- Downloading unpublished toolkit assets for review.
- The Admin link in the sidebar.

## Gaps vs product intent

- **Admin does not imply other roles.** `hasRole` checks exact role values. An `ADMIN_EMAILS` admin with no `user_roles` row fails `hasAnyRole`, so they see "Awaiting approval" in the `(app)` group and are redirected away from `/analyse` and `/contribute`.
- **No audit trail.** Role changes, approvals and publishes are not logged anywhere a person can read. `published_pathways.published_by` records only the last publisher.
- **`/api/admin/reject` deletes the user outright.** It was meant for pending signups, but it works on any user id.
- **Dead admin routes.** `/api/admin/pathway-submissions/review|publish` still require admin but query the dropped `pathway_submissions` table.
