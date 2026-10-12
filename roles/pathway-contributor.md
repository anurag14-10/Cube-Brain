---
name: Pathway Contributor (Contributor)
type: role
schema_version: 1
aliases:
- Contributor
- pathway_contributor
summary: The Contributor persona. Granted only by an admin (approving a contributor registration, or a
  direct role grant); gates the /contribute workspace, the contributor companion flow, pathway create/join/check-similar/assemble
  and toolkit-asset upload.
code_refs:
- lib/roles.ts
- proxy.ts
- app/api/chat/route.ts#L56-L80
- app/contribute/page.tsx
- app/api/admin/contributor-registrations/approve/route.ts
- app/api/pathways/route.ts
- app/api/pathways/[id]/join/route.ts
- app/api/pathways/assemble/route.ts
- app/api/pathways/check-similar/route.ts
- lib/toolkit-assets-server.ts#L149-L167
doc_refs:
- docs/wiki/diffusion-cube/business/users-and-personas.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
role_key: pathway_contributor
persona_name: Contributor
granted_by: 'Admin only: POST /api/admin/contributor-registrations/approve (sets access_status=''approved''
  and upserts the role) or POST /api/admin/roles.'
auto_granted: false
prerequisites:
- Any role already held (an approved account) — /contribute redirects zero-role users to /explore
- A contributor_registrations row (organisation, POC, pathway role, description, Terms of Use acceptance)
  — /contribute shows the registration form until one exists
- Admin approval of that registration (or a direct admin role grant)
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/contribute/page.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/admin/contributor-registrations/approve/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/business/users-and-personas.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Who has it

People with a real deployment write-up who registered to contribute and were approved by an admin. One user can hold both this role and `adopter`.

## How it is granted

Through the [contributor registration approval](../workflows/contributor-registration-approval.md) workflow. Approving a `contributor_registrations` row backfills `org_id` (via `ensureOrganisation`), sets `access_status = 'approved'` and upserts `(user_id, 'pathway_contributor')` in a single admin call. An admin can also grant the role directly with `POST /api/admin/roles`.

## What it unlocks

- The `/contribute` workspace (ContributeGrid). The page checks session, then any role, then the registration row (not rejected), then this role.
- `POST /api/chat` companion with `flow: 'contributor'`. Without the role the route returns 403.
- `POST /api/pathways` (create), `POST /api/pathways/[id]/join`, `POST /api/pathways/check-similar` and `POST /api/pathways/assemble`. Assemble also requires membership in `pathway_contributors` and ownership of the design.
- `POST /api/toolkit-assets/upload-url` and `POST /api/toolkit-assets`, through `authorizePathwayContributor`: role plus membership of that pathway.
- Download preview of their own unpublished toolkit assets.

## Gaps vs product intent

- **Role and registration status are two sources of truth.** A direct grant through `/api/admin/roles` leaves `access_status` untouched. Revoking the role does not reject the registration. The contact-sharing setting on `/account` checks `access_status`, not the role.
- **A role without a registration still shows the form.** A user given the role but with no registration row sees the registration form on `/contribute`. Join also requires the registration's organisation.
- **A contributor cannot analyse their own adoption without `adopter`.** The charter intends otherwise.
- **The adopter-to-contributor transition is a hard switch.** The charter's "at the right moment" transition is not built ([W7](../workflows/w7-adopter-to-contributor-transition.md)).
