---
name: Terms of Use (/terms)
type: page
schema_version: 1
aliases:
- Terms of Use
summary: Public Terms of Use page. It renders content/legal/terms.md through LegalDocument and is linked from the
  Sign up and Register to Contribute checkboxes.
route: /terms
file: app/terms/page.tsx
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
- app/terms/page.tsx
- components/LegalDocument.tsx
- content/legal/terms.md
- proxy.ts
doc_refs:
- docs/wiki/diffusion-cube/application/frontend.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/terms/page.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: components/LegalDocument.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: content/legal/terms.md
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

`<LegalDocument file="terms" title="Terms of Use" versionLine="Version 1.0 · Last updated: 18-Sep-26" />`.
[LegalDocument](../modules/components-legal-document.md) reads
[content/legal/terms.md](../modules/content-legal-terms.md) from disk, swaps in the support address
(`withSupportEmail`) and renders the text with `WikiMarkdown`, with links turned on. The page has a
[SiteHeader](../modules/components-site-header.md) whose Back link is
[LegalBackLink](../modules/components-legal-back-link.md). It is a standalone page, not inside AppShell, and
sets page metadata `title: 'Terms of Use · Diffusion Cube'`.

The version line is hard-coded in the page file. It is separate from `LEGAL_VERSION` in `lib/legal.ts`, which
is what sign-up stores in `user_metadata.terms_version`. The two can drift.

## Access behaviour

Public: `/terms` is in proxy.ts `PUBLIC_PATHS` because a visitor without an account must be able to read it
during sign-up. Everyone sees the same content. Opened with `?from=signup` or `?from=contribute`, the Back link
closes the tab, or falls back to navigating to that form. Otherwise it goes back to 100pathways.com.
