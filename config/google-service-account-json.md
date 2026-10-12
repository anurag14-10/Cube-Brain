---
name: GOOGLE_SERVICE_ACCOUNT_JSON
type: config_var
schema_version: 1
summary: Google service-account credentials (JSON) for the fire-and-forget Sheets conversation log.
var_name: GOOGLE_SERVICE_ACCOUNT_JSON
required: false
secret: true
browser_exposed: false
read_by:
- lib-logger
integration: google-sheets
environments:
- vercel-production
- docker-aws-ec2
- local-development
code_refs:
- lib/logger.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/logger.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/architecture/configuration.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it controls

Google service-account credentials (JSON) for the fire-and-forget Sheets conversation log. Optional: if missing, logging fails silently and requests are unaffected.

## Where it is read

- `lib/logger.ts` — `getAuth()`, called by `logConversation` from `app/api/chat/route.ts` after each streamed reply.
