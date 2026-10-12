---
name: TD-17 Generated docs/wiki stale since 2026-09-28
type: tech_debt
schema_version: 1
aliases:
- TD-17
summary: The llm-wiki-generated docs/wiki was last refreshed 2026-09-28 and misses migrations 0033–0034,
  the toolkit-assets routes and tables usage, and later decisions; its TD register is itself partly outdated.
tags:
- docs
- staleness
td_id: TD-17
severity: P2
status: open
remediation: Re-run the llm-wiki skill against current code (this is TA-11 in the toolkit-assets plan)
  and reconcile its TD register with this brain.
code_refs:
- supabase/migrations/0033_account_deletion.sql
- supabase/migrations/0034_contribution_units_toolkit_assets.sql
- app/api/toolkit-assets/route.ts
doc_refs:
- docs/wiki/diffusion-cube/application/database.md
- docs/wiki/diffusion-cube/repository-map.md
- docs/wiki/diffusion-cube/architecture/repository-conventions.md
- docs/wiki/diffusion-cube/ai-context.md
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
- specs/TOOLKIT_ASSETS_SPEC.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: docs/wiki/diffusion-cube/application/database.md
- system: github_repo
  method: queried
  date: '2026-10-12'
  ref: d37f3bc
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: specs/TOOLKIT_ASSETS_SPEC.md
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

The wiki was generated in `d37f3bc` (2026-09-28) and patched the same day in `1be6f71` and `619aeff`. No commit has touched `docs/wiki/` since. At `28068b6`:
- `application/database.md` and `repository-conventions.md` describe migrations "0001 through 0032".
- `repository-map.md` and `ai-context.md` say "32 SQL migrations".
- `ai-context.md` still lists `contribution_units` as inert.
- Nothing in the wiki covers migration 0034, the `toolkit-assets` bucket or the `/api/toolkit-assets*` routes.
- The TD register claims are now partly wrong: [TD-04](td-04-contribution-units-unused.md), [TD-08](td-08-stale-root-docs.md) and [TD-12](td-12-dead-exec-summary-prompt.md) all need correcting.

## Impact

`CLAUDE.md` sends every agent to this wiki first, so agents start from an outdated picture of the schema and the debt.

## Remediation

Refresh it as task TA-11 of the toolkit-assets plan, which also covers the Terms review of the public-sharing wording.
