---
name: Privacy Notice (/privacy)
type: page
schema_version: 1
aliases:
- Privacy Notice
summary: Public Privacy Notice page. It renders content/legal/privacy.md through LegalDocument and is linked from
  the Sign up form's consent checkbox.
route: /privacy
file: app/privacy/page.tsx
access: public
roles:
- anonymous-visitor
- general-user
- adopter
- pathway-contributor
- admin
components:
- components-legal-document
status: live
code_refs:
- app/privacy/page.tsx
- components/LegalDocument.tsx
- content/legal/privacy.md
- proxy.ts
doc_refs:
- docs/wiki/diffusion-cube/application/frontend.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/privacy/page.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: components/LegalDocument.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: content/legal/privacy.md
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

`<LegalDocument file="privacy" title="Privacy Notice" versionLine="Version 1.0 · Last updated: 18-Sep-26" />`.
This is the same shell as [/terms](terms.md): a SiteHeader with a smart Back link, the markdown rendered by
WikiMarkdown with links on, and a footer nav to both legal pages. The source text is
[content/legal/privacy.md](../modules/content-legal-privacy.md).

## Access behaviour

Public (`/privacy` is in `PUBLIC_PATHS`). Everyone sees the same content. Opened with `?from=signup` (the
consent checkbox and notice on `/login`), the Back link returns to the half-filled sign-up form.
