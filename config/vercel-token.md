---
name: VERCEL_TOKEN
type: config_var
schema_version: 1
summary: 'A GitHub Actions repository secret, not an app runtime variable: the Vercel CLI token used for
  `vercel pull` and `vercel deploy --prod`.'
var_name: VERCEL_TOKEN
required: true
secret: true
browser_exposed: false
read_by:
- github-workflow-deploy
integration: vercel
environments:
- vercel-production
code_refs:
- .github/workflows/deploy.yml
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: .github/workflows/deploy.yml
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/operations/deployment.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it controls

A GitHub Actions repository secret, not an app runtime variable: the Vercel CLI token used for `vercel pull` and `vercel deploy --prod`. The token-based CLI deploy works around the Vercel Hobby plan blocking deploys whose commit author is not a team member.

## Where it is read

- `.github/workflows/deploy.yml` — passed as `--token` to both Vercel CLI steps.
