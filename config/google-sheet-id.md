---
name: GOOGLE_SHEET_ID
type: config_var
schema_version: 1
summary: ID of the spreadsheet the conversation log appends to (range `logs!A:F`).
var_name: GOOGLE_SHEET_ID
required: false
secret: false
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

ID of the spreadsheet the conversation log appends to (range `logs!A:F`). Optional, like the credentials.

## Where it is read

- `lib/logger.ts` — `logConversation`.
