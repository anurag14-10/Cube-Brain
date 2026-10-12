---
name: GitHub Actions
type: integration
schema_version: 1
summary: One workflow, `Deploy to Vercel`.
integration_kind: ci-cd
provider: GitHub
account_notes: Runs in the diffusion-cube GitHub repository; secrets are repository secrets.
config_vars:
- vercel-token
- vercel-org-id
- vercel-project-id
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
  ref: docs/wiki/diffusion-cube/integrations/third-party-integrations.md
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/operations/deployment.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Used for

One workflow, `Deploy to Vercel`. It runs on push to `main` or manual dispatch on ubuntu-latest with Node 24: checkout → install the Vercel CLI → `vercel pull --environment=production` → `vercel deploy --prod`. There is no build, lint or test job, and nothing builds the Docker image.

## Configuration

`VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID` as Actions secrets.

## Failure behaviour

A failing workflow simply does not deploy. Because there are no test or lint gates, any commit to `main` (including a contributor assemble commit if `GITHUB_BRANCH=main`) deploys.

## Account

Runs in the diffusion-cube GitHub repository; secrets are repository secrets.
