---
name: 0018 — Drop retired pathway_submission tables
type: migration
schema_version: 1
aliases:
- 0018_drop_retired_tables.sql
summary: 'Destructive: drops pathway_submissions, pathway_submission_versions and pathway_submission_exec_summaries,
  after dropping the FK from published_pathways.'
number: '0018'
file: supabase/migrations/0018_drop_retired_tables.sql
tables_touched:
- pathway-submissions
- pathway-submission-versions
- pathway-submission-exec-summaries
- published-pathways
destructive: true
decision: drop-pathway-submissions-tables
code_refs:
- supabase/migrations/0018_drop_retired_tables.sql
- app/api/pathway-submissions/push/route.ts
- lib/pathway-submission-versions.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0018_drop_retired_tables.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Drops `published_pathways_source_submission_id_fkey`, then the three tables in dependency order (exec summaries → versions → submissions).

## Why

The submission model was replaced by contribution units and the pathways workspace model (the file says "contribution_units + GitHub draft files"; in practice a whole-document GitHub commit won).

## Risk

All submission data deleted. Dead code still queries the dropped tables and would fail with "relation does not exist".
