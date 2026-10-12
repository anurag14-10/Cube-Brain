---
name: Navigate redirect (/navigate)
type: page
schema_version: 1
aliases:
- navigate
summary: Legacy route stub. The Explorer flow was renamed Navigate → Analyse, and this page forwards old links to
  /analyse.
route: /navigate
file: app/navigate/page.tsx
access: public
status: live
code_refs:
- app/navigate/page.tsx
- proxy.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/navigate/page.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: proxy.ts
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it renders

Nothing. `NavigateRedirect` calls `redirect('/analyse')`. The Explorer flow used to be called Navigate, and
before that Strengthen. The `StrengthenWorkspace` component name and many code comments still use those
old names.

## Access behaviour

`/navigate` is in proxy.ts `PUBLIC_PATHS`, so an old bookmark reaches the redirect without hitting the login
wall. The [`/analyse`](analyse.md) page then applies its own tiered gating.
