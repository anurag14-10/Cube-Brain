---
name: analysis-doc mode
type: chat_mode
schema_version: 1
aliases:
- Analysis Document generation
summary: Generates the Explorer's Analysis Document — a Sections 0–6 pathway-shaped analysis of the user's
  own adoption (no Source Trace) — stored as design_documents doc_type 'analysis'.
tags:
- explorer
- document
prompt: analysis-doc-system-prompt
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
produces_doc_type: analysis
triggered_by: companion grid_update explorerAction {type:'analysis'} → handleExplorerAction → generateExplorerDocument('analysis')
  in lib/adoption-conversation.ts
status: live
mode_key: analysis-doc
endpoint: chat
model: claude-sonnet-4-6
streaming: true
code_refs:
- app/api/chat/route.ts#L151-L152
- lib/system-prompts.ts#L629-L703
- lib/adoption-conversation.ts#L809-L935
- lib/explorer-intents.ts#L60-L78
- lib/design-documents.ts
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

The Explorer flow's primary deliverable: a standing description of the user's adoption in the same Sections 0–6 shape as a corpus pathway document, with related pathway experience woven in. Describes, never prescribes.

## Grounding

Whole grounding corpus (`loadWikiContext`), framework block, and `standingContext(grid, meta)` (grid densities/notes + name/sector/geography/stage/summary). Messages = the full conversation (images expanded) + trailing user turn "Generate the analysis document now."

## Output

Markdown: `## <meta.name>`, sector · geography line, "Generated <date>" line, then Section 0 Reading guide, 1 Pathway identity, 2 Coverage and gaps (density-symbol grid + ≤8 open questions), 3 Micro-innovations, 4 Toolkits and playbooks, 5 (explicitly omitted), 6 Retrieval guide. No Source Trace appendix. Fallback line when the conversation is too thin. The client inserts it with `insertDesignDocumentVersion(designId, 'analysis', contentHash, text, prev+1)` and appends a client-built message carrying `<analysis_doc/>`; regeneration is skipped when `hashConversationState(messages, grid)` matches the stored row's `content_hash`.

## Triggered when

The companion sets `explorerAction:'analysis'` — either on the turn the user says yes to the offered write-up (step 5), or immediately on a document upload from which sector and problem are clear (the "On document uploads" override in `ANALYSE_FLOW`). There is no manual generate button. The route only checks `hasAnyRole`.
