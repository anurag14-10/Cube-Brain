---
name: Vercel
type: integration
schema_version: 1
summary: Hosting for the live production app.
integration_kind: hosting
provider: Vercel
account_notes: 'Hobby plan, per the comment in `.github/workflows/deploy.yml`: it blocks deploys whose
  commit author is not a team member and cannot add team members, hence a token-based CLI source deploy.'
config_vars:
- vercel-token
- vercel-org-id
- vercel-project-id
code_refs:
- .github/workflows/deploy.yml
- next.config.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: .github/workflows/deploy.yml
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: next.config.ts
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

Hosting for the live production app. It is not called from application code. GitHub Actions deploys with the Vercel CLI (`vercel@latest`, installed at run time and not in package.json). Production env vars are held in the Vercel project and pulled with `vercel pull --environment=production`.

## Configuration

CI secrets `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID`. App runtime vars live in the Vercel project settings.

## Failure behaviour

A blocked or failed deploy leaves the previous production deployment serving. Never use `--prebuilt`: tests showed it is still blocked on Hobby even with a token.

## Account

Hobby plan, per the comment in `.github/workflows/deploy.yml`: it blocks deploys whose commit author is not a team member and cannot add team members, hence a token-based CLI source deploy.
