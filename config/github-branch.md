---
name: GITHUB_BRANCH
type: config_var
schema_version: 1
summary: The branch that contributor assemble commits go to (`content/wiki/pathways/<slug>.md`).
var_name: GITHUB_BRANCH
required: false
secret: false
browser_exposed: false
read_by:
- lib-github
integration: github-contents-api
environments:
- vercel-production
- docker-aws-ec2
- local-development
code_refs:
- lib/github.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/github.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/architecture/configuration.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it controls

The branch that contributor assemble commits go to (`content/wiki/pathways/<slug>.md`). If unset, `lib/github.ts` falls back to a hard-coded non-production branch. If set to `main`, every contributor assemble fires the Vercel production deploy workflow.

## Where it is read

- `lib/github.ts` — module-scope constant used by `ghReadFile`, `ghWriteFile`, `ghListFiles`.
