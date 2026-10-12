---
name: executive-summary mode
type: chat_mode
schema_version: 1
summary: Generates the Explorer's short two-part Executive Summary (the implementation + a compressed
  summary of the Analysis Document's suggestions), stored as design_documents doc_type 'plan'.
tags:
- explorer
- document
prompt: executive-summary-system-prompt
max_tokens: 4096
access: role-gated
roles:
- adopter
- pathway-contributor
- admin
- general-user
corpora:
- grounding-corpus
- published-pathways-corpus
produces_doc_type: plan
triggered_by: companion grid_update explorerAction {type:'executive-summary'} → handleExplorerAction →
  generateExplorerDocument('plan')
status: live
mode_key: executive-summary
endpoint: chat
model: claude-sonnet-4-6
streaming: true
code_refs:
- app/api/chat/route.ts#L153-L160
- lib/system-prompts.ts#L777-L831
- lib/adoption-conversation.ts#L809-L935
- components/AdoptionWorkspace.tsx
doc_refs:
- docs/wiki/diffusion-cube/integrations/ai-llm.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/chat/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/system-prompts.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/adoption-conversation.ts
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Purpose

A deliberately smaller companion to the Analysis Document, for a colleague skimming in under a minute. Never a replacement for the analysis and never restating it.

## Grounding

Whole grounding corpus, framework block, `standingContext(grid, meta)`. Messages = conversation + (when an analysis exists) the current Analysis Document as a trailing assistant message + "Generate the executive summary now." Part two summarises that document.

## Output

`## <name> — Executive Summary`, then `### The Implementation` (4–8 sentences, descriptive) and `### Summary of the Suggestions` (≤8 bullets carried over from the analysis, still framed as questions/decisions/suggested choices). If no analysis was passed: the exact line "No analysis document has been generated yet." Stored under the existing `plan` doc_type (`<exec_summary/>` card marker); exported with filename suffix `executive-summary` in AdoptionWorkspace.

## Triggered when

The companion sets `explorerAction:'executive-summary'` on the user's yes. The explorer contract text says never before an Analysis Document exists, but that is prompt-only; the client does not enforce it.
