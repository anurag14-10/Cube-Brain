---
name: TD-12 Dead pathway-submission executive-summary prompt and chat mode
type: tech_debt
schema_version: 1
aliases:
- TD-12
summary: pathwaySubmissionExecutiveSummarySystemPrompt is only reachable through the /api/chat mode 'pathway-exec-summary',
  which no client code sends; a leftover of the pathway_submissions era.
tags:
- dead-code
- llm
td_id: TD-12
severity: P3
status: open
affected_modules:
- lib-system-prompts
- components-pathway-submissions-panel
affected_endpoints:
- chat
remediation: Remove the prompt builder, the 'pathway-exec-summary' entry in the mode list and its branch
  in app/api/chat/route.ts, alongside the TD-01 cleanup.
code_refs:
- lib/system-prompts.ts#L843
- app/api/chat/route.ts#L34
- app/api/chat/route.ts#L182-L183
doc_refs:
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/wiki/diffusion-cube/knowledge/technical-debt.md
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: app/api/chat/route.ts
contested:
- field: summary
  readings:
  - 'wiki: the prompt ''has no caller anywhere in the codebase'''
  - 'code at 28068b6: app/api/chat/route.ts dispatches mode ''pathway-exec-summary'' to it, but no client
    (lib/adoption-conversation.ts, components, app pages) ever sends that mode'
  note: 'Same outcome: the prompt is unreachable from the product. The route branch is a public entry
    point (/api/chat is in PUBLIC_PATHS, and non-library modes require a role), so removing it also shrinks
    the attack surface.'
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

The executive summary of a pathway submission was generated alongside each draft in the `pathway_submissions` era (migration 0015, commit `0b8c5de`, 2026-08-14). The table was dropped by 0018. The prompt builder and its `/api/chat` branch remain, but no client sends `mode: 'pathway-exec-summary'`.

## Impact

The dead prompt code makes `lib/system-prompts.ts`, the true source of runtime behaviour, harder to read. A caller that knows the mode can still run an extra LLM call through it.

## Remediation

Delete it together with [TD-01](td-01-dead-code-dropped-table.md).
