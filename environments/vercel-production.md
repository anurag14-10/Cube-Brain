---
name: Vercel production
type: environment
schema_version: 1
summary: 'The live production path: Vercel, deployed by GitHub Actions with the Vercel CLI on every push
  to main.'
env_kind: production
status: live
host: Vercel
deploy_mechanism: 'GitHub Actions `.github/workflows/deploy.yml`: on push to `main` (or manual dispatch)
  it runs `vercel pull --environment=production` and then `vercel deploy --prod` as a plain source deploy
  (never `--prebuilt`), authenticated with the CLI token.'
branch: main
integrations:
- vercel
- github-actions
- anthropic-claude
- supabase-postgres
- supabase-auth
- supabase-storage
- github-contents-api
- smtp-nodemailer
- google-sheets
- document-extraction-libs
- jspdf
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
  ref: docs/wiki/diffusion-cube/operations/deployment.md
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/operations/infrastructure.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-08'
  ref: .github/workflows/deploy.yml
contested:
- field: status
  readings:
  - 'docs/wiki deployment.md: which path serves production traffic is an operational fact the repo cannot
    answer'
  - 'derived: Vercel is the only path wired to CI on main, so it is treated as live'
  note: Status is derived, not verified against the Vercel dashboard.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## How it deploys

GitHub Actions `.github/workflows/deploy.yml`: on push to `main` (or manual dispatch) it runs `vercel pull --environment=production` and then `vercel deploy --prod` as a plain source deploy (never `--prebuilt`), authenticated with the CLI token.

Every push to `main` deploys to production. There is no test, lint or approval gate in the workflow. Vercel builds the source itself and ignores `output: "standalone"`. A contributor assemble that commits to `main` (only if `GITHUB_BRANCH=main`) also triggers a deploy.

## What runs there

The full Next.js app (App Router pages, `/api/*` route handlers, `proxy.ts` middleware) with production env vars from the Vercel project. This is the live path. The repo itself cannot prove which environment serves real traffic; this entry treats Vercel as live because it is the only CI-wired path.
