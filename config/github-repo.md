---
name: GITHUB_REPO
type: config_var
schema_version: 1
summary: Target repository in `owner/repo` form (no URL prefix) for contributor assemble commits.
var_name: GITHUB_REPO
required: true
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

Target repository in `owner/repo` form (no URL prefix) for contributor assemble commits. Needed only for the assemble path; the rest of the app runs without it.

## Where it is read

- `lib/github.ts` — module-scope constant with a non-null assertion; a missing value only fails when assemble runs.
