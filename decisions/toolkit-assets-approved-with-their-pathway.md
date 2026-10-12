---
name: Toolkit assets are reviewed and published together with their pathway
type: decision
schema_version: 2
summary: A pathway's toolkit assets have no approval step of their own; the admin reviews them as part of the pathway, and they go live when the pathway is approved.
tags:
- toolkit-asset
- curation
- pathway-lifecycle
doc_refs:
- docs/tasks/toolkit-asset-files/requirement.md
- specs/TOOLKIT_ASSETS_SPEC.md
decided_on: 2026-09-30
status: accepted
context: Toolkit asset files needed a curation path. The Program Team already reviews and publishes contributor pathways.
decision: Assets are approved together with the pathway. Sending the pathway for review adds its asset list to the write-up; the admin reviews the assets inside the pathway review, with a preview of each file; approving the pathway publishes its assets. An asset added after the pathway was sent for review goes live the next time the pathway is reviewed and approved.
alternatives:
- A separate approval queue for assets
consequences:
- The Program Team reviews assets in the same step as the pathway, with no extra queue
- Late-added assets bring the "Send for Review" action back, so they reach the next review
decided_by: []
sources:
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/tasks/toolkit-asset-files/requirement.md item 3 (final scope approved 2026-09-30); specs/TOOLKIT_ASSETS_SPEC.md § 1 Goals, 2026-09-30 checkpoint decisions
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Context

Toolkit asset files needed a curation path. The Program Team already owns the pathway content lifecycle: reviewing and publishing contributor submissions (see [Pathway lifecycle](../concepts/pathway-lifecycle.md)).

## Decision

Assets have no approval step of their own. When a contributor sends a pathway for review, its asset list is added to the write-up. The admin reviews the assets as part of the pathway, with a preview of each file, and approving the pathway publishes them. An asset added after the pathway was sent goes live at the next review and approval.

## Alternatives considered

A separate approval queue for assets. The requirement names it only by ruling it out ("there is no separate approval step for assets").

## Consequences

- The Program Team reviews assets in the same step as the pathway, with no extra queue.
- At the 2026-09-30 checkpoint the owner chose to bring "Send for Review" back whenever a pathway has shared assets that are not yet in the sent document.
- The requirement records approval on 2026-09-30 but not by whom, so `decided_by` is blank.
