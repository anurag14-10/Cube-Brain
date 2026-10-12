---
name: Anthropic
type: organisation
schema_version: 2
summary: Vendor of the Claude API. Every model-calling surface of the Cube (all /api/chat modes and the
  check-similar duplicate check) calls claude-sonnet-4-6 through @anthropic-ai/sdk.
doc_refs:
- docs/tasks/toolkit-asset-files/requirement.md
- app/api/chat/route.ts
- app/api/pathways/check-similar/route.ts
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
last_updated: '2026-10-12'
---

## Relationship to the Cube

Anthropic is the single LLM vendor. `app/api/chat/route.ts` streams every chat mode from `claude-sonnet-4-6`. `app/api/pathways/check-similar/route.ts` makes a forced tool-use call (`report_match`) to the same model.

## Notes

- The toolkit-asset requirement records that "the AI account expires 28-Oct-2026". If the account is not renewed, every conversational feature stops. Uploading, approving and downloading toolkit assets keep working. The dated threat is tracked as the risk [Anthropic API account expiry](../risks/anthropic-account-expiry.md).
- There is no retry and no second provider configured in the app, so an outage or lapse has no fallback.
