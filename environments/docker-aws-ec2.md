---
name: Docker image on AWS
type: environment
schema_version: 1
summary: 'A prepared but not CI-wired path: an arm64 Next.js standalone Docker image intended for AWS,
  built and deployed by hand.'
env_kind: container
status: in-progress
host: AWS (App Runner / ECS Fargate / EC2 Graviton; EC2 per commit history)
deploy_mechanism: Manual only. Run `docker build` (multi-stage, `node:22-alpine`, `linux/arm64` by default
  via `IMAGE_PLATFORM`, `NEXT_PUBLIC_SUPABASE_URL`/`ANON_KEY` as build args), then `docker run` with runtime
  env vars. No CI job builds or pushes the image.
integrations:
- aws-ec2
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
- Dockerfile
- .dockerignore
- next.config.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: Dockerfile
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: .dockerignore
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/operations/deployment.md
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/operations/infrastructure.md
- system: raw_documents
  method: document
  date: '2026-10-08'
  ref: docs/raw_documents/AI DIffusion Cube - Product Charter.docx
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## How it deploys

Manual only. Run `docker build` (multi-stage, `node:22-alpine`, `linux/arm64` by default via `IMAGE_PLATFORM`, `NEXT_PUBLIC_SUPABASE_URL`/`ANON_KEY` as build args), then `docker run` with runtime env vars. No CI job builds or pushes the image.

The image is built by hand and deployed by hand. There is no IaC, registry push, health check or rollback in the repo. The charter requirement "Deployment in AWS environment" is Not started, and the AWS account is a free account expiring Dec-2026.

## What runs there

The `.next/standalone` server (`node server.js` on port 3000, non-root user) plus `public/` and an explicit copy of `content/`, which `lib/wiki-loader.ts` reads from disk. `NEXT_PUBLIC_SUPPORT_EMAIL` is not a build arg, so this image always shows the hard-coded support address.
