---
name: Anonymous visitor
type: role
schema_version: 1
summary: No account or session. Can use the public Diffusion Library (/explore and its library chat),
  read the Terms and Privacy pages, download published toolkit assets, and see explanatory gate pages
  for Analyse and Contribute.
code_refs:
- proxy.ts#L58-L129
- app/explore/page.tsx
- app/analyse/page.tsx#L37-L43
- app/contribute/page.tsx#L21-L36
- app/api/chat/route.ts#L56-L67
- app/api/toolkit-assets/[id]/download/route.ts
doc_refs:
- docs/wiki/diffusion-cube/business/users-and-personas.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
persona_name: Visitor
granted_by: Nobody — the absence of a session.
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: proxy.ts PUBLIC_PATHS
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Who has it

Anyone on the web without a session.

## How it is granted

It isn't granted. `proxy.ts` lets the PUBLIC_PATHS through with no session: `/login`, `/explore`, `/analyse`, `/navigate`, `/contribute`, `/terms`, `/privacy`, `/api/chat`, `/api/wiki-pathways`, `/api/toolkit-assets` and `/api/auth/send-email`. An anonymous request to `/` is redirected to `/explore`. Any other path goes to `/login?next=…`, or gets a 401 for `/api/*`.

## What it unlocks

- [Diffusion Library](../features/diffusion-library.md): `/explore` cards from `published_pathways`, read with the service-role client, plus the static library corpus. Also the `library` chat mode, the only `/api/chat` mode with no role check.
- Published toolkit asset metadata (`GET /api/toolkit-assets?ids=`) and downloads (`GET /api/toolkit-assets/[id]/download`).
- `/terms` and `/privacy`.
- `/analyse` and `/contribute` render an AccessGateMessage explaining the feature, with a "Log in or sign up" button.

## Gaps vs product intent

- **No rate limiting.** The public `library` chat calls the Anthropic API on every request. This feeds the unbounded-LLM-spend risk. Public asset downloads are not limited either (egress cost).
- **Anonymous library chats are not saved.** Only signed-in users get `library_conversations`.
