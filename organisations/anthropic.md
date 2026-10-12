---
name: Anthropic
type: organisation
schema_version: 1
summary: Vendor of the Claude API. Every model-calling surface of the Cube (all /api/chat modes and the
  check-similar duplicate check) calls claude-sonnet-4-6 through @anthropic-ai/sdk.
code_refs:
- app/api/chat/route.ts
- app/api/pathways/check-similar/route.ts
doc_refs:
- docs/tasks/toolkit-asset-files/requirement.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
org_kinds:
- vendor
website: https://www.anthropic.com
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: 'app/api/chat/route.ts (model: ''claude-sonnet-4-6'')'
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/tasks/toolkit-asset-files/requirement.md (AI account expires 28-Oct-2026)
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Relationship to the Cube

Anthropic is the single LLM vendor. `app/api/chat/route.ts` streams every chat mode from `claude-sonnet-4-6`. `app/api/pathways/check-similar/route.ts` makes a forced tool-use call (`report_match`) to the same model. The technical side (SDK, configuration, failure behaviour) belongs to the integration entity `integrations/anthropic-claude`.

## Notes

- The toolkit-asset requirement records that "the AI account expires 28-Oct-2026". If the account is not renewed, every conversational feature stops. Uploading, approving and downloading toolkit assets keep working. The dated threat is tracked as a risk (`risks/anthropic-account-expiry`).
- There is no retry and no second provider. See the tech-debt register entry on Anthropic retries.
