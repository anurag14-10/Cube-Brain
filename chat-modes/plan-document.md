---
name: plan-document mode
type: chat_mode
schema_version: 1
aliases:
- Plan Doc
summary: Accepted by /api/chat and wired to a working 4-section executive Plan Document prompt, but no
  client code calls it; superseded in the UI by executive-summary.
tags:
- document
- inert
prompt: plan-document-system-prompt
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
produces_doc_type: none
triggered_by: Nothing in app/, components/ or lib/ sends mode 'plan-document'; reachable only by a direct
  API call
status: inert
mode_key: plan-document
endpoint: chat
model: claude-sonnet-4-6
streaming: true
code_refs:
- app/api/chat/route.ts#L161-L169
- lib/system-prompts.ts#L706-L766
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
  method: derived
  date: '2026-10-08'
  ref: grep for 'plan-document' across app/ components/ lib/
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: ARCHITECTURE.md
contested:
- field: status
  readings:
  - ARCHITECTURE.md and ai-llm.md list plan-document as a mode with no caveat
  - 'code: no caller; the ''plan'' doc_type is now produced by executive-summary'
  note: Code supports inert.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Purpose

Originally the short, executive-ready Plan Document distinct from the full Analysis Doc. The Explorer flow now produces its second document through [executive-summary](executive-summary.md) instead.

## Grounding

Whole grounding corpus, framework block, `standingContext(grid, meta)`; `versionNumber` from the request (default 1) goes into the title.

## Output

`## <name> Plan Doc v<N>` with four sections: Project Summary, Key Gaps Identified (≤10), Key Recommendations (≤5, each grounded in a named pathway precedent, else the exact "No recommendations available yet…" line), Next Steps (≤5, only user-surfaced actions, else "No next steps identified yet."). The route would log it to Google Sheets; nothing stores it in `design_documents`.

## Triggered when

Never from the UI. Any approved user could invoke it directly (hasAnyRole only).
