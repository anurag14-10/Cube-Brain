---
name: AWS (EC2 / container hosting)
type: integration
schema_version: 1
summary: 'Target of the prepared Docker path: an arm64 Next.js standalone image intended for App Runner,
  ECS Fargate or EC2 Graviton (Dockerfile header; a past commit message says "AWS EC2").'
integration_kind: hosting
provider: Amazon Web Services
account_notes: Free account per the Product Charter (summarised in docs/wiki ai-context.md), expiring
  December 2026; the charter says plan a replacement account by November 2026. The charter's "Deployment
  in AWS environment" requirement is Not started.
code_refs:
- Dockerfile
- next.config.ts
- .dockerignore
doc_refs:
- docs/raw_documents/AI DIffusion Cube - Product Charter.docx
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: Dockerfile
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: next.config.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/third-party-integrations.md
- system: raw_documents
  method: document
  date: '2026-10-08'
  ref: docs/raw_documents/AI DIffusion Cube - Product Charter.docx
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/ai-context.md
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/operations/deployment.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Used for

Target of the prepared Docker path: an arm64 Next.js standalone image intended for App Runner, ECS Fargate or EC2 Graviton (Dockerfile header; a past commit message says "AWS EC2"). No infrastructure-as-code, compose file or CI job exists in the repo.

## Configuration

No AWS-specific variables. The app's runtime env vars are supplied at `docker run`; `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY` must be build args.

## Failure behaviour

Not defined in the repo: no health checks, rollback or monitoring for this path.

## Account

Free account per the Product Charter (summarised in docs/wiki ai-context.md), expiring December 2026; the charter says plan a replacement account by November 2026. The charter's "Deployment in AWS environment" requirement is Not started.
