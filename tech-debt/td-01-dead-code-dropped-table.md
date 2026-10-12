---
name: TD-01 Dead code referencing dropped pathway_submissions tables
type: tech_debt
schema_version: 1
aliases:
- TD-01
summary: Three route handlers, one lib module and one component still query pathway_submissions / pathway_submission_versions,
  which migration 0018 dropped; they would 500 if invoked.
tags:
- dead-code
- schema-drift
td_id: TD-01
severity: P1
status: open
affected_modules:
- lib-pathway-submission-versions
- components-pathway-submissions-panel
affected_tables:
- pathway-submissions
- pathway-submission-versions
- pathway-submission-exec-summaries
affected_endpoints:
- pathway-submissions-push
- admin-pathway-submissions-publish
- admin-pathway-submissions-review
remediation: Delete app/api/pathway-submissions/push/route.ts, both app/api/admin/pathway-submissions/*
  routes, lib/pathway-submission-versions.ts and components/PathwaySubmissionsPanel.tsx (together with
  TD-12's prompt).
code_refs:
- app/api/pathway-submissions/push/route.ts
- app/api/admin/pathway-submissions/publish/route.ts
- app/api/admin/pathway-submissions/review/route.ts
- lib/pathway-submission-versions.ts
- components/PathwaySubmissionsPanel.tsx
- supabase/migrations/0018_drop_retired_tables.sql
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
  ref: app/api/pathway-submissions/push/route.ts
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

`pathway_submissions`, `pathway_submission_versions` and `pathway_submission_exec_summaries` were dropped by migration 0018 (2026-08-21), see [drop-pathway-submissions-tables](../decisions/drop-pathway-submissions-tables.md). Five files still call `.from('pathway_submissions')` / `.from('pathway_submission_versions')`. Verified at `28068b6`: all five files still exist and still query the dropped tables. `lib/adoption-conversation.ts` already carries a comment that its own use was removed. `app/admin/page.tsx` does not render `PathwaySubmissionsPanel`, so no live UI path reaches them.

## Impact

If any of these routes is called, Postgres returns "relation does not exist" and the route returns 500. The dead code also misleads anyone searching for how contributor drafts persist: it matches the old self-serve publish design described in older docs, not the live [two-step publish](../decisions/two-step-assemble-and-admin-publish.md).

## Remediation

Delete the five files and the dead `pathwaySubmissionExecutiveSummarySystemPrompt` / `pathway-exec-summary` mode ([TD-12](td-12-dead-exec-summary-prompt.md)) in one cleanup change. This is a few hours of work.
