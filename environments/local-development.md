---
name: Local development
type: environment
schema_version: 1
summary: A developer machine running next dev against env vars in .env.local.
env_kind: local
status: live
host: localhost:3000
deploy_mechanism: '`npm run dev` (`next dev`) with env vars from `.env.local`. Migrations are applied
  to a Supabase project by hand (no Supabase CLI config in the repo). `scripts/smtp-test.mjs` checks SMTP
  settings.'
integrations:
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
- package.json
- scripts/smtp-test.mjs
- lib/wiki-loader.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: package.json
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: scripts/smtp-test.mjs
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/operations/deployment.md
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/operations/infrastructure.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## How it deploys

`npm run dev` (`next dev`) with env vars from `.env.local`. Migrations are applied to a Supabase project by hand (no Supabase CLI config in the repo). `scripts/smtp-test.mjs` checks SMTP settings.

No deploy step. `WIKI_PATH` can point the corpus loaders at another checkout. Dev-only logging of the contributor `<grid_update>` block runs when `NODE_ENV` is not production.

## What runs there

The full app against whichever Supabase project, Anthropic key and SMTP server `.env.local` names. Assemble commits really go to `GITHUB_REPO`/`GITHUB_BRANCH`, so local testing should use a throwaway branch.
