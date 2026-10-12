---
name: TD-04 contribution_units table built but unused
type: tech_debt
schema_version: 1
aliases:
- TD-04
summary: contribution_units (0022/0025) was built for per-contributor tagged units and never written;
  since migration 0034 (2026-09-30) it is the store for toolkit-asset rows, but the general unit model
  it was designed for is still unused.
tags:
- schema
- partially-resolved
td_id: TD-04
severity: P2
status: in-progress
affected_tables:
- contribution-units
affected_modules:
- lib-toolkit-assets-server
requirement: enhance-framework-and-pathway-schema
remediation: Decide whether the identity / micro-innovation unit rows (section='identity' and the other
  four unit types) will ever be written. If so, wire them in as part of the schema-enhancement requirement.
  If not, document toolkit assets as the table's only use and drop the unused columns such as unit_internal_id
  semantics for non-asset rows.
code_refs:
- supabase/migrations/0022_contribution_units.sql
- supabase/migrations/0025_contribution_units_content.sql
- supabase/migrations/0034_contribution_units_toolkit_assets.sql
- lib/toolkit-assets-server.ts
- app/api/toolkit-assets/route.ts
- app/api/admin/pathways/publish/route.ts
doc_refs:
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
- docs/wiki/diffusion-cube/knowledge/legacy-artifacts.md
- specs/TOOLKIT_ASSETS_SPEC.md
- docs/tasks/toolkit-asset-files/clarifications.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/wiki/diffusion-cube/knowledge/technical-debt.md
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: supabase/migrations/0034_contribution_units_toolkit_assets.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: specs/TOOLKIT_ASSETS_SPEC.md
contested:
- field: status
  readings:
  - 'open — generated wiki (2026-09-28): ''never written by any code path'''
  - 'in-progress — code at 28068b6: written by app/api/toolkit-assets (POST), admin publish, account delete
    and admin pathway delete for unit_type=''toolkit-asset'' rows'
  note: The wiki predates migration 0034. The code supports the second reading. Only the toolkit-asset
    slice is in use, and that code is on feature/toolkit-assets / cube-dev, not yet on main.
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

Migration 0022 (2026-08-21) built `contribution_units` as the store for individually tagged units: identity fields plus the five micro-innovation types. It came with RLS, including the "edit boundary" update policy. Migration 0025 dropped `git_commit_sha` the same day, and on 2026-08-24 the [whole-document commit decision](../decisions/whole-document-github-commit-over-contribution-units.md) replaced unit extraction, so nothing ever wrote the table.

**Partly resolved since the register was written.** Migration 0034 (`3ded7ae`, 2026-09-30) reuses the table for toolkit-asset files: 11 new columns, a shape constraint for `unit_type='toolkit-asset'`, and removal of the two client write policies. At `28068b6`, `app/api/toolkit-assets/route.ts`, `app/api/admin/pathways/publish/route.ts`, `app/api/account/delete/route.ts` and `app/api/admin/pathways/delete/route.ts` write it. See [toolkit-assets-in-contribution-units-service-role-only](../decisions/toolkit-assets-in-contribution-units-service-role-only.md). Migration 0033 already made `user_id` nullable so that published units outlive their author.

## Impact

For any unit type other than toolkit-asset, the schema still implies a capability that does not exist. Someone reading the schema alone would assume that identity and decision units are stored per contributor. They are not: they live only inside the assembled markdown.

## Remediation

Resolve it as part of the charter's [enhance-framework-and-pathway-schema](../requirements/enhance-framework-and-pathway-schema.md) work, or narrow the table's documented purpose to toolkit assets.
