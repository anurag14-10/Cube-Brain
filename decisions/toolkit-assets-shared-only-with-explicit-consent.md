---
name: Toolkit asset files are stored and shared only after an explicit "OK to share publicly"
type: decision
schema_version: 2
summary: A contributor's file or link becomes a shared Toolkit Asset only after an explicit Yes to "OK to share this publicly?"; nothing is stored or shared without it.
tags:
- toolkit-asset
- consent
- curation
doc_refs:
- docs/tasks/toolkit-asset-files/requirement.md
- specs/TOOLKIT_ASSETS_SPEC.md
decided_on: 2026-09-30
status: accepted
context: Contributors can attach the real file or link behind a Toolkit Asset. A published asset can be downloaded by anyone using 100 Pathways, including visitors who are not signed in.
decision: Nothing is stored or shared without the contributor's explicit "OK to share this publicly?". A file is kept only when the contributor answers Yes.
alternatives: []
consequences:
- The brain's own rule `asset-needs-consent` requires `share_consent: true` on any unit that carries an asset
- Files are not scanned for viruses or personal data; the admin's review of the pathway is the only check
decided_by: []
sources:
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/tasks/toolkit-asset-files/requirement.md (final scope approved 2026-09-30); specs/TOOLKIT_ASSETS_SPEC.md § 1 Goals and § 3 User flows
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Context

Contributors can attach the real file or link behind a [Toolkit Asset](../concepts/toolkit-asset.md). Once published, anyone using 100 Pathways can download it, including visitors who are not signed in.

## Decision

Nothing is stored or shared without the contributor's explicit answer to "OK to share this publicly?". A file is kept only after a Yes.

## Alternatives considered

None are recorded in the source.

## Consequences

- The brain mirrors the decision: the `asset-needs-consent` rule in `SCHEMA.yml` makes `share_consent: true` mandatory on any unit with `asset_kind`.
- Files are not scanned for viruses or personal data. The admin's review of the pathway is the only check (requirement, "Known limits").
- The requirement records the scope as approved on 2026-09-30, but not who approved it, so `decided_by` is blank.
