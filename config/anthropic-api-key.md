---
name: ANTHROPIC_API_KEY
type: config_var
schema_version: 1
summary: API key for the Anthropic account that backs every AI feature (model `claude-sonnet-4-6`).
var_name: ANTHROPIC_API_KEY
required: true
secret: true
browser_exposed: false
integration: anthropic-claude
environments:
- vercel-production
- docker-aws-ec2
- local-development
code_refs:
- app/api/chat/route.ts
- app/api/pathways/check-similar/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/chat/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/pathways/check-similar/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/architecture/configuration.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it controls

API key for the Anthropic account that backs every AI feature (model `claude-sonnet-4-6`). Without it all eight `/api/chat` modes and the duplicate-pathway check fail.

## Where it is read

Read at module scope (`new Anthropic({ apiKey })`) in two route handlers, which are endpoints rather than registry modules, so `read_by` is empty:

- `app/api/chat/route.ts` — all streaming chat modes.
- `app/api/pathways/check-similar/route.ts` — non-streaming forced tool-use call.

Per the Product Charter the account behind this key is a free account expiring 2026-10-28.
