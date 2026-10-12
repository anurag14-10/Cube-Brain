---
name: Home (/)
type: page
schema_version: 1
aliases:
- root
- landing
summary: The root route. It only redirects to /explore; anonymous visitors are sent to /explore by proxy.ts before
  the page runs.
route: /
file: app/(app)/page.tsx
access: role-gated
roles:
- general-user
- adopter
- pathway-contributor
- admin
components:
- app-app-group-layout
status: live
code_refs:
- app/(app)/page.tsx
- proxy.ts
doc_refs:
- docs/wiki/diffusion-cube/application/frontend.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/(app)/page.tsx
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

Nothing of its own. `HomePage` calls `redirect('/explore')`. It sits inside the `(app)` route group, so the
[`(app)` layout](../modules/app-app-group-layout.md) wraps it. That layout shows "Awaiting approval" to a
signed-in account with zero `user_roles` rows.

## Access behaviour

- **Anonymous:** [proxy.ts](../modules/proxy.md) sees no session on a non-public path. For `/` exactly it
  redirects to `/explore` rather than `/login`, so an anonymous visitor never reaches this file.
- **Signed in, no role (pending):** the `(app)` layout renders the "Awaiting approval" screen. Next.js renders
  layout and page segments in parallel, so it is not verified whether the page's redirect wins over that
  screen.
- **Any role:** redirected to `/explore`.
- **Signed-in user hitting `/login`:** proxy.ts redirects them here, and this page forwards them to `/explore`.
