---
name: Cube Web App fully functional with at least 20 pathways
type: milestone
schema_version: 2
aliases:
- Web App ready for scale use
summary: Charter milestone 1, due 2026-11-15 — the web app ready for scaled use inside EkStep and by other organisations, with 20 pathways created and published.
tags:
- charter-roadmap
doc_refs:
- docs/raw_documents/AI DIffusion Cube - Product Charter.docx
target_date: 2026-11-15
status: in-progress
order: 1
outcome: The web app is ready for scaled use, both internally within EkStep and by other organisations. 20 pathways are created and published, covering all the available know-how. Adopters and contributors can independently explore, analyse and contribute without needing hand-holding.
deliverables:
- 20 pathways created and published
- 'Sign-up notification to the admin for approval and to the user once approved (charter: In Progress)'
- 'Reset password option (charter: Complete)'
- 'Terms and Conditions and disclaimers per the legal team''s guidance (charter: In Progress)'
- 'Option for a user to delete their account (charter: Not started)'
- 'Store toolkit asset files and give users access to them in conversation where relevant (charter: In Progress)'
- 'Enhance the Framework and Pathway schema to enrich the know-how (charter: Not started)'
- 'Enhance pathway creation logic — extraction/generation from raw source material into the schema (charter: Not started)'
- 'Improve analysis logic — Analyse Own Adoption flow and Analysis Document (charter: Not started)'
- 'Define and implement a corpus synthesis process (LLM Wiki approach) across pathways (charter: Not started)'
- 'Fine-tune the web app UI for contribution/curation flows per user feedback (charter: Not started)'
- 'Test cases across all flows, and testing (charter: Not started)'
- 'Deployment in the AWS environment (charter: Not started)'
- 'Error handling and graceful degradation for failed AI calls and malformed uploads (charter: Not started)'
- 'Security and privacy — encryption at rest and in transit, token-based API auth with session timeout, rate limiting, PII checks on pathway ingestion (charter: Not started)'
- 'Reliability and serving architecture — concurrency limits with graceful overflow, defined timeout/retry policy (charter: Not started)'
- 'Structured logging — latency, errors, per-user/per-pathway usage (charter: Not started)'
contested:
- field: deliverables
  readings:
  - 'Product Charter (copy committed 2026-09-28): account deletion "Not started", toolkit asset files "In Progress"'
  - 'diffusion-cube code: migration 0033 (account deletion) and 0034 (toolkit assets) exist in the repo'
  note: The charter's statuses are as of its own last edit. The code shows work landed after or alongside it; neither says the deliverable is accepted. A person on the Program or Solution team sets the status.
sources:
- system: raw_documents
  method: document
  date: '2026-10-12'
  ref: Product Charter § 3 Roadmap (milestone, outcome, 15-Nov-26) and Requirements tab "Web App ready for scale use"
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: status in-progress inferred from charter requirements marked In Progress / Complete; supabase/migrations/0033, 0034
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Outcome

According to the Product Charter, the web app is ready for scaled use, both inside EkStep and by other organisations. Twenty pathways are created and published, covering all the available know-how, and adopters and contributors can explore, analyse and contribute without hand-holding.

## Deliverables

The charter's Requirements tab, headed "Web App ready for scale use", lists the requirements this milestone is judged on. Each line in `deliverables` carries the charter's own status. The charter is intent, so none of these lines is evidence that something is built.

The headline count is 20 published pathways. The brain holds 14 pathway entries as of 2026-10-12, and only 6 of them are linked from the grounding corpus `index.md` (see [Pathway lifecycle](../concepts/pathway-lifecycle.md)).

## Status

`in-progress` is derived: the charter marks some of the milestone's requirements In Progress or Complete. The charter's statuses are as of its last edit, and the code has moved on since (see `contested`). The milestone review at the boundary (Program + Solution team + senior management) decides whether it is met, extended or rescoped.
