---
name: Third-party and open-source tools count as Toolkit Assets when the deployment built on them
type: decision
schema_version: 2
summary: A third-party or open-source tool or repo counts as a Toolkit Asset when the deployment actually built on or adapted it and others could reuse it the same way; tools mentioned in passing or only evaluated do not.
tags:
- toolkit-asset
- corpus-definition
doc_refs:
- specs/TOOLKIT_ASSETS_SPEC.md
decided_on: 2026-09-30
status: accepted
context: In the 2026-09-30 live test of toolkit asset files, the contributor companion declined a GitHub link to a third-party repository as "a third-party dependency, not your own artifact", although the deployment had built on it.
decision: Third-party or open-source tools and repos count as Toolkit Assets when the deployment actually built on them and others could reuse them the same way. Tools only mentioned in passing or only evaluated do not.
alternatives:
- Only artifacts the contributor's own team created count as Toolkit Assets (the companion's behaviour before the decision)
consequences:
- Matches the corpus precedent, where MahaVISTAAR lists OpenAgriNet and Voicera as Toolkit Assets
- The contributor companion's toolkit-asset rules gained this qualification
decided_by:
- anurag-goutam
sources:
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: 'specs/TOOLKIT_ASSETS_SPEC.md § 10, live test round 1 — "Decision (owner, 2026-09-30)"; spec owner: Anurag Goutam'
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Context

During the first live test of toolkit asset files on 2026-09-30, the contributor companion refused a GitHub link to a third-party repository. It called the repository "a third-party dependency, not your own artifact", even though the deployment had built on it.

## Decision

A third-party or open-source tool or repository counts as a [Toolkit Asset](../concepts/toolkit-asset.md) when the deployment actually built on it or adapted it, and others could reuse it the same way. A tool that is only mentioned in passing, or only evaluated, does not count.

## Alternatives considered

Count only artifacts the contributor's own team created. That was the companion's behaviour before the decision.

## Consequences

- It matches the corpus precedent: the [MahaVISTAAR](../pathways/mahavistaar.md) pathway lists OpenAgriNet and Voicera as Toolkit Assets ([OpenAgriNet architecture](../units/mahavistaar-openagrinet-seven-layer-architecture.md), [VoiceEra platform](../units/mahavistaar-voiceera-orchestration-platform.md)).
- When extracting units, a tool the deployment built on is a Toolkit Asset, and a decision to adopt it is a Decision unit.
