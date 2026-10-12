---
name: Admin console (/admin)
type: page
schema_version: 1
aliases:
- Admin
- admin console
summary: 'Server-rendered admin console with three panels: users and roles (grant/revoke, reject pending signups),
  contributor registrations (approve/reject), and pathways (review assembled document and toolkit assets, publish,
  delete).'
route: /admin
file: app/admin/page.tsx
access: admin-only
roles:
- admin
components:
- components-admin-dashboard
- components-admin-contributor-registrations-panel
- components-admin-pathways-panel
- components-admin-pathway-row-card
- components-confirm-dialog
calls_endpoints:
- admin-roles
- admin-reject
- admin-contributor-registrations-approve
- admin-contributor-registrations-reject
- admin-pathways-publish
- admin-pathways-delete
- toolkit-assets-download
status: live
code_refs:
- app/admin/page.tsx
- lib/roles.ts
doc_refs:
- docs/wiki/diffusion-cube/application/frontend.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/admin/page.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/roles.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/frontend.md
contested:
- field: file
  readings:
  - 'docs/wiki frontend.md and the (app)/layout.tsx comment: the (app) route group covers /adoptions, /wiki and
    /admin'
  - 'code: the admin page is app/admin/page.tsx, outside the (app) group; it renders its own plain layout with no
    AppShell or Sidebar'
  note: The code supports the second reading. The (app) approval gate does not wrap /admin; the page's own isAdmin
    check does.
- field: summary
  readings:
  - 'docs/wiki frontend.md: loads auth users, user_roles, published_pathways, pathways and contributor_registrations'
  - 'code: also loads contribution_units toolkit assets (unit_type=''toolkit-asset'') per pathway for the review
    card'
  note: The docs predate migration 0034 (toolkit assets).
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it renders

A server component with no AppShell: a "← Back" link and three sections. All data is loaded in parallel with
the **service-role** client:

- `auth.admin.listUsers({page:1, perPage:1000})` + `user_roles` → [AdminDashboard](../modules/components-admin-dashboard.md).
  A user × role checkbox table (general_user / adopter / pathway_contributor / admin) using
  `POST /api/admin/roles`. Users with no role sort first, highlighted, with a "Reject" button
  (`POST /api/admin/reject`, which deletes the auth user).
- `contributor_registrations` → [AdminContributorRegistrationsPanel](../modules/components-admin-contributor-registrations-panel.md).
  Approve / Reject (`/api/admin/contributor-registrations/{approve|reject}`); approving grants
  pathway_contributor.
- `pathways` + `published_pathways` slugs + `contribution_units` toolkit assets →
  [AdminPathwaysPanel](../modules/components-admin-pathways-panel.md) /
  [AdminPathwayRowCard](../modules/components-admin-pathway-row-card.md). Expanding a row fetches
  `pathways.content_cache` (the assembled document) and lists the toolkit assets in the review against those
  shared later. "Publish" appears only for `review_requested` rows (`POST /api/admin/pathways/publish`);
  "Delete" uses `POST /api/admin/pathways/delete`.

## Access behaviour

- **Anonymous:** not a public path, so proxy.ts redirects to `/login?next=/admin`.
- **Signed in, not admin:** `isAdmin(supabase, user.email)` is false, so `redirect('/')`. Admin means the email is
  in `ADMIN_EMAILS` **or** the user has an `admin` row in `user_roles`.
- **Admin:** full console. The Sidebar shows the Admin link only when `isAdmin` is true.

The page check is UX. Every `/api/admin/*` route re-checks `isAdmin` itself. The user list is capped at 1000 by
the single `listUsers` call; there is no pagination.
