---
name: Adopter (Explorer)
type: role
schema_version: 1
aliases:
- Explorer
- adopter
summary: The Explorer persona. Auto-granted right after signup (OTP verified) so a new account can use
  Analyse with no admin step; gates /analyse and the companion's explorer flow.
code_refs:
- lib/roles.ts
- proxy.ts
- app/api/chat/route.ts#L56-L80
- app/api/auth/grant-default-role/route.ts
- app/login/page.tsx#L211-L227
- app/analyse/page.tsx
doc_refs:
- docs/wiki/diffusion-cube/business/users-and-personas.md
- specs/SIGNUP_OTP_SPEC.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
role_key: adopter
persona_name: Explorer
granted_by: 'Self-serve: the client calls POST /api/auth/grant-default-role after a verified signup (service-role
  insert into user_roles). An admin can also add or remove it via POST /api/admin/roles.'
auto_granted: true
prerequisites:
- A verified Supabase Auth account with a live session (email OTP confirmed)
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/auth/grant-default-role/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/analyse/page.tsx
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/business/users-and-personas.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Who has it

In effect every signed-up user. `completeSignup()` in `app/login/page.tsx` fires `POST /api/auth/grant-default-role` once there is a verified session. The route inserts `(user_id, 'adopter')` into `user_roles` with the service-role client, and treats a duplicate (23505) as success.

## How it is granted

Automatically at signup ([auto-grant adopter](../features/auto-grant-adopter.md), part of [W4](../workflows/w4-signup-and-access.md)). Admins can also toggle it on `/admin` (`POST /api/admin/roles`). A failed grant is silently ignored on the client (`.catch(() => {})`). The user still lands on `/explore`, and only an admin can repair it.

## What it unlocks

- `/analyse`: the page checks `hasRole('adopter')` and renders the Analyse workspace. Without it, the page shows "Ask an admin to grant you Explorer access".
- `POST /api/chat` with `mode: 'companion'` and `flow: 'explorer'`: the route returns 403 without the role (`app/api/chat/route.ts`). This is the real gate.
- Holding any role, this one included, makes the account "approved" (`hasAnyRole`). That opens `/adoptions` and `/wiki` (the `(app)` route group) and the non-companion chat modes.

## Gaps vs product intent

- **Analysing your own adoption is adopter-only.** The charter says any user with an ongoing or planned adoption, "whether a new Adopter or an existing Contributor", can analyse it. In code, a `pathway_contributor` without `adopter` is refused on `/analyse` and in the explorer flow.
- **The flow choice is a hard fork.** Each adoption is locked to one flow (`designs.meta.flow`) by its entry point. The charter's smooth adopter-to-contributor transition ([W7](../workflows/w7-adopter-to-contributor-transition.md)) is planned only.
- **The adopter check covers only `flow === 'explorer'`.** A companion call with an empty or unknown `flow` falls through to the Explorer prompt after only the any-role check. See [API route is the real enforcement](../rules/api-route-is-real-enforcement.md).
- `docs/wiki` still describes a four-intent Explorer menu in places (via CLAUDE.md). The code has one 5-step flow ([Analyse flow steps](../workflows/analyse-flow-steps.md)).
