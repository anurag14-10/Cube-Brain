---
name: VERCEL_PROJECT_ID
type: config_var
schema_version: 1
summary: A GitHub Actions repository secret naming the Vercel project that is deployed.
var_name: VERCEL_PROJECT_ID
required: true
secret: false
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

A GitHub Actions repository secret naming the Vercel project that is deployed. It is an identifier, not a credential.

## Where it is read

- `.github/workflows/deploy.yml` — step `env` for `vercel pull` and `vercel deploy`.
