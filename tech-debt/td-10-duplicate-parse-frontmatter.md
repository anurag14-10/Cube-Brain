---
name: TD-10 Duplicate parseFrontmatter implementations
type: tech_debt
schema_version: 1
aliases:
- TD-10
summary: app/api/admin/pathways/publish/route.ts has a private parseFrontmatter that duplicates lib/strip-frontmatter.ts's
  exported one.
tags:
- duplication
td_id: TD-10
severity: P3
status: open
affected_modules:
- lib-strip-frontmatter
affected_endpoints:
- admin-pathways-publish
remediation: Import parseFrontmatter from lib/strip-frontmatter.ts in the admin publish route (check the
  return-shape difference first).
code_refs:
- app/api/admin/pathways/publish/route.ts#L9
- lib/strip-frontmatter.ts#L19
doc_refs:
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/wiki/diffusion-cube/knowledge/technical-debt.md
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: app/api/admin/pathways/publish/route.ts
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

Verified at `28068b6`: there are two frontmatter parsers. One is private to `app/api/admin/pathways/publish/route.ts` (line 9) and returns `Record<string, string | string[]>`. The other is the shared `parseFrontmatter` in `lib/strip-frontmatter.ts` (line 19), which returns `PathwayFrontmatter | null`.

## Impact

The two implementations can drift apart. Explore card fields (migration 0030) are parsed at publish time by one parser and displayed elsewhere using the other.

## Remediation

Use the shared helper.
