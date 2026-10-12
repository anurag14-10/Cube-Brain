---
name: GITHUB_TOKEN
type: config_var
schema_version: 1
summary: 'Bearer token for the GitHub Contents API: a classic PAT with `repo` scope or a fine-grained
  token with contents write on the target repo.'
var_name: GITHUB_TOKEN
required: true
secret: true
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

Bearer token for the GitHub Contents API: a classic PAT with `repo` scope or a fine-grained token with contents write on the target repo. Needed only for contributor assemble.

## Where it is read

- `lib/github.ts` — `headers()` on every Contents API call.
