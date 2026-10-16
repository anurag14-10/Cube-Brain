---
name: Sahayika — WhatsApp assistant for community health workers
type: pathway
schema_version: 2
aliases:
- Sahayika
summary: An NGO-led WhatsApp assistant that answers community health workers' maternal and child health
  and scheme questions from a doctor-curated knowledge base, escalating the rest to nurse-midwives — piloted
  with 120 workers. Recorded from synthetic test documents.
tags:
- Public Health
- synthetic-test
title: Sahayika
pathway_kind: single-deployment
sector: Public Health
use_case_category: Clinical and government-scheme question answering for community health workers, with
  human escalation
geography: Rural districts of one Indian state (not named in the source)
population_served: 120 community health workers in the pilot, working on maternal and child health, using
  government-issued smartphones on patchy connections, in Hindi and a local dialect
stage_reached: pilot
key_dates: Project month 0 — grant proposal; month 3 — design note v1.2; month 6 — workers first use the
  bot; month 8 — nurse-midwife interviews; month 14 — steering group pilot review. No calendar dates in the
  source
scale_impact: 120 health workers in the pilot. Weekly active share fell from 70% (pilot month 1) to 35% (pilot
  month 3); escalations fell from 212 to 61 a month while the median wait rose from 4 hours to 80 hours
  (as of project month 14)
cost_anchor: Not documented in the source
build_effort: 18-month grant covering design, build and a 120-worker pilot; part-time NGO programme staff
  plus the research lab's researchers; three partners (NGO, research lab, philanthropic foundation)
gaps:
- Why weekly use halved over pilot months 1–3 — not investigated; health workers were not interviewed about
  it. The project team's working guess (novelty wore off) is unverified
- Funding for running costs after the grant — unresolved at month 14; the state health mission has not been
  approached
- Whether answering directly and reviewing after the fact produced any unsafe answers — no review findings
  are documented
- Outcome of the reworked escalation route and the second pilot — not yet run
sources:
- system: conversation
  method: stated
  date: '2026-10-16'
  ref: Sahayika project documents shared by vinod303 in a Claude session — 01-grant-proposal.md, 02-design-note.md,
    03-pilot-dashboard-notes.md, 04-nurse-interview-notes.md, 05-steering-group-minutes.md, 99-sahayika-evaluation.md.
    Not in the diffusion-cube repo; every file is marked "Synthetic test document"
first_logged: '2026-10-16'
last_updated: '2026-10-16'
---

## Identity

> **Synthetic test record.** Every source document is marked "Synthetic test document". Treat this pathway as test material, not a real deployment, until a contributor confirms otherwise.

According to the research partner's Sahayika evaluation, Sahayika is an NGO-led project, built with a private research lab and funded by a philanthropic foundation, that answers community health workers' questions over WhatsApp. Workers asked about danger signs, drug doses and government schemes because their supervising nurse-midwives were often unreachable for days. The NGO led field work and relations with the district health office, and the lab led the build and the evaluation.

- **Flow:** a worker sends a text or voice question; the system retrieves from a knowledge base curated by two doctors and drafts an answer with an LLM. If retrieval confidence is sufficient, the answer goes straight to the worker; if not, the question goes to five nurse-midwives in the block and the majority answer (three agreeing) is sent back.
- **Oversight:** answers reach the worker first; doctors review a weekly sample afterwards and update the knowledge base.
- **Languages:** Hindi and a local dialect; voice notes are transcribed before retrieval.
- **Stage reached:** [Pilot](../concepts/pilot.md).
- **Organisations:** named only by role in the source (an NGO, a private research lab, a philanthropic foundation, the district health office, the state health mission), so no organisation entries are linked.

## Effort

An 18-month grant covering design, build and a pilot with 120 health workers, staffed part-time from existing NGO programme staff plus the lab's researchers. Workers first used the bot six months in; the evaluation covers the first 14 months. No cost figures are documented.

## Coverage

The source has no 4×4 grid, so `coverage` is left blank. The units below sit mostly in [Institution](../concepts/institution.md) × Pilot.

## Gaps

The documents themselves name four open questions: why weekly use halved, how running costs will be funded after the grant, whether answer-first review let anything unsafe through, and how the reworked escalation route performs. The full list is in `gaps`.

## Where the reusable value is

Five units, all from the escalation route and its governance:

- **The human fallback needs an owner:** escalation duty has to be assigned by whoever sets the staff's duties ([unit](../units/sahayika-escalation-duty-needs-supervisor-assignment.md)); design the role with the people who will staff it, not brief them on it ([unit](../units/sahayika-briefed-not-consulted-nurse-midwives.md)).
- **Governance choices:** answer first, review after ([unit](../units/sahayika-answer-first-review-after.md)); hold expansion until the escalation route is rebuilt ([unit](../units/sahayika-hold-expansion-until-escalation-holds.md)).
- **Sustainability:** running costs deferred to "during the pilot" were still unfunded at month 14 ([unit](../units/sahayika-running-costs-deferred-past-pilot.md)).

## Corpus copies

None. The documents are not in any Cube corpus; `corpora`, `doc_refs` and `lifecycle` are left blank.
