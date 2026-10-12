---
name: TD-06 Silent draft-insert failures before migration 0027 (historical)
type: tech_debt
schema_version: 1
aliases:
- TD-06
summary: Every Contributor draft insert silently failed the design_documents.doc_type check constraint
  until migration 0027 widened it; fixed 2026-08-21, kept for institutional memory.
tags:
- historical
- constraint-drift
td_id: TD-06
severity: P3
status: resolved
affected_tables:
- design-documents
affected_modules:
- lib-design-documents
affected_endpoints:
- pathways-assemble
remediation: 'Covered by TD-03: tests that exercise the draft upsert would have caught the constraint
  mismatch.'
resolved_on: '2026-08-21'
resolution: Migration 0027_design_documents_draft_type.sql (commit d0cf3e2) widened the doc_type check
  constraint to allow 'draft'.
code_refs:
- supabase/migrations/0027_design_documents_draft_type.sql
- lib/design-documents.ts
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
  ref: supabase/migrations/0027_design_documents_draft_type.sql
- system: github_repo
  method: queried
  date: '2026-10-12'
  ref: d0cf3e2
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

The original `design_documents.doc_type` check allowed only `analysis` and `plan`. The multi-contributor rework began storing contributor drafts there with `doc_type='draft'`, and every insert failed the constraint without any visible error. The full account is in the incident [contributor-draft-inserts-failing-doc-type](../incidents/contributor-draft-inserts-failing-doc-type.md).

## Impact

While the bug was live, `/api/pathways/assemble` never found a draft to commit. The debt that remains is the detection gap: the same kind of constraint drift can recur unnoticed without [TD-03](td-03-no-automated-tests.md).

## Remediation

Already fixed by migration 0027. This entry is kept for institutional memory.
