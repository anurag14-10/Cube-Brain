---
name: companion mode
type: chat_mode
schema_version: 1
aliases:
- Adoption Companion
- Analyse chat turn
- Contributor chat turn
summary: 'The conversational turn of both role flows: the Explorer (Analyse) companion by default, or
  the Contributor pipeline companion when flow=''contributor''. Grounded in the whole corpus; every reply
  ends with a <grid_update> block.'
tags:
- explorer
- contributor
- grid
prompt: explorer-system-prompt
max_tokens: 8192
access: role-gated
roles:
- adopter
- pathway-contributor
corpora:
- grounding-corpus
- published-pathways-corpus
contract: grid-update
produces_doc_type: none
triggered_by: 'sendMessage in lib/adoption-conversation.ts on every user message in an /analyse or /contribute
  workspace (body: mode ''companion'', designId, flow, grid, meta, existingPublishedDoc for contributor)'
status: live
mode_key: companion
endpoint: chat
model: claude-sonnet-4-6
streaming: true
code_refs:
- app/api/chat/route.ts#L73-L80
- app/api/chat/route.ts#L184-L202
- app/api/chat/route.ts#L216
- app/api/chat/route.ts#L249-L260
- lib/system-prompts.ts#L313-L400
- lib/system-prompts.ts#L413-L494
- lib/adoption-conversation.ts#L955-L1116
doc_refs:
- docs/wiki/diffusion-cube/integrations/ai-llm.md
- ARCHITECTURE.md
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
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: ARCHITECTURE.md
contested:
- field: prompt
  readings:
  - explorer-system-prompt (flow 'explorer', blank or absent)
  - contributor-system-prompt (flow 'contributor')
  note: One mode, two prompts selected by the request's flow; `prompt` records the default branch.
- field: produces_doc_type
  readings:
  - 'ARCHITECTURE.md and the route''s max_tokens comment: Explorer step 5 generates a full Deep Dive Report
    inline wrapped in <deliverable> tags'
  - 'code: explorerSystemPrompt / ANALYSE_FLOW never mention <deliverable>; step 5 sets explorerAction
    ''analysis'' and the document comes from the analysis-doc mode'
  note: DELIVERABLE_START/END handling survives in lib/grid-update.ts and adoption-conversation.ts as
    legacy; the code's prompt text supports 'none'.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Purpose

The main chat turn of an adoption workspace. One mode serves both product flows; `meta.flow` (fixed at workspace creation) picks the prompt:
- **Explorer / Analyse** (`flow` 'explorer' or empty): [explorer-system-prompt](../prompts/explorer-system-prompt.md) running the 5-step `ANALYSE_FLOW` from lib/explorer-intents.ts — gather context silently, compare against the corpus (exact vs adjacent match), name what matters next, offer the Analysis Document.
- **Contributor** (`flow` 'contributor'): [contributor-system-prompt](../prompts/contributor-system-prompt.md) — the 4-step document-first pipeline (wait for documents → settle sufficiency + stage → auto-generate → open revise/publish loop) plus toolkit-asset candidate detection.

## Grounding

Explorer: whole grounding corpus via `loadWikiContext()` (index.md-linked files in `content/wiki/pathways/` + every `published_pathways` row, each with "Contributed by" and "Documented as of / First published" lines), `content/framework.md` + structural legend, `content/resources.md`, and all published toolkit assets (`loadPublishedToolkitAssets()`). Contributor: same corpus (for style reference) and framework, plus the pathway's current published document when `existingPublishedDoc` is sent; no resources, no toolkit assets. Both get `currentProgressBlock` — the grid, stage, flowStep and last turn's reasoning state from `meta`, re-injected every turn because the `<grid_update>` is stripped before messages are stored.

## Output

Streamed prose (Explorer: 2–4 sentences or lead-in + ≤4 bullets; Contributor: exactly the step-specified acknowledgements) followed by a [grid-update](../contracts/grid-update.md) block. Explorer contract adds `meta.persona`, `meta.cubeAssessment`, `explorerAction` and (when assets exist) `toolkitAssetsReferenced`; Contributor adds `pathwayAction` and `toolkitAssetCandidates`. The client (sendMessage) merges changed cells and meta into `designs`, stores `pathwaysReferenced`/`toolkitAssetsReferenced` on the message, then:
- `explorerAction` 'analysis' / 'executive-summary' → second call in [analysis-doc](analysis-doc.md) / [executive-summary](executive-summary.md);
- `pathwayAction` 'generate' / 'revise' → [pathway-draft](pathway-draft.md); 'publish' → `POST /api/pathways/assemble`;
- `toolkitAssetCandidates` → client-built consent-card messages.

Server side, after the stream: `adoption_queries` row (last user text + `pathwaysReferenced` slugs) and a Google Sheets `logConversation` row. max_tokens 8192 (raised from 2048 to leave room for long replies).

## Triggered when

Every message the user sends in an /analyse or /contribute workspace. Gate: `hasAnyRole`, then `flow==='contributor'` needs `pathway_contributor`, `flow==='explorer'` needs `adopter`. A request with no `flow` skips the flow role check and gets the Explorer prompt — any approved role can reach it by calling the API directly.
