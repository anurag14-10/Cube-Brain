# Masters — Cube-Brain

The controlled vocabularies every `vocab:` / `list_vocab:` field in
`SCHEMA.yml` is checked against. The number in each heading is the id
`SCHEMA.yml` uses (`vocab: "10"` → master 10).

Since schema v2 the framework's closed sets — dimensions, stages,
sub-categories, grid keys — and the corpora and teams are **variables**
here, not folders. What each one means is defined in `concepts/` (one page
per dimension, one per stage) or in the explanation beside the term.

## Writing terms so they can be checked

- **One term per bullet.** `- term — explanation` is fine: only the part
  before the dash is the term. A term on a bare line is invisible to the
  validator.
- **No full stop at the end of a term line**, and no `; ` inside one — the
  parser reads those as prose and skips them.
- **Terms are case-sensitive** and must be written in entity files exactly as
  here.

## Leaving a field blank is legitimate

If nothing here fits, leave the field blank and propose a term in this file
(in the same commit, with a one-line reason). Never write an uncontrolled
value — it looks authoritative and matches nothing.

## Values that mirror the code

Where a master mirrors an enum in the diffusion-cube code (unit types,
dimensions, sub-categories, grid keys), the code is the source of truth. If
the code changes, change the master in the same commit as the entities that
use the new value.

---

## 1. Unit types

The first five mirror `UNIT_TYPES` in `lib/dimensions.ts`; definitions live
in `concepts/`. The sixth is the brain's own: a pathway document's Section 5
pattern, stored as a unit so it sits beside its evidence.

- Strategic Decision — framing, governance or design decision that shaped what got built
- Tactical Decision — stack, sequence, cost or implementation decision specific enough to reuse
- Failure and Fix — what broke, the fix, and what the fix revealed
- Playbook — a genuine multi-step gated sequence
- Toolkit Asset — an actual reusable artifact someone else can lift and adapt
- Problem-Solution Pattern — problem → root cause → solution → result → condition, built from units, may span pathways

---

## 2. Dimensions

The framework's four lenses on one deployment — four questions, never four
phases. Closed set; adding one is a framework change. Defined in
`concepts/<dimension>.md`.

- persona — Are we solving the right problem for the right person?
- solution — Are we building the right system to solve it?
- institution — Can the institution own, absorb, govern, and sustain it?
- ecosystem — Can the required network of actors execute and support it?

---

## 3. Stages

The four adopter stages, in order. Closed set. Defined in
`concepts/<stage>.md`. A deployment's stage is only ever taken from what the
user states.

- explore — Is AI appropriate, and what would it take?
- define — What must be true before building?
- pilot — What breaks with real users and real institutional conditions?
- scale — Can the institution own, sustain, and continuously improve it?

---

## 4. Sub-categories

`<dimension>-<letter>`, 22 in all. A unit's `sub_category` must belong to
its `dimension`. Each one's stage weights and questions are on its
dimension's concept page. The codes are internal-only — never in
user-facing prose.

- persona-a — Problem and Persona
- persona-b — Current Journey and Friction
- persona-c — Outcome and Success
- persona-d — Scope, Inclusion, and Trust
- solution-a — AI Fit and Comparative Advantage
- solution-b — UX, Channel, and Integration
- solution-c — Model, Architecture, and Infrastructure
- solution-d — Data and Knowledge Readiness
- solution-e — Performance, Reliability, and Scale
- institution-a — Mandate, Ownership, and Decision Rights
- institution-b — Workforce and Change
- institution-c — Governance, Safety, and Redress
- institution-d — Accountability, Liability, and Compliance
- institution-e — Data Stewardship
- institution-f — Operating Model and Sustainability
- institution-g — Institutionalisation and Continuous Improvement
- ecosystem-a — Partner Architecture and Roles
- ecosystem-b — External Data and Infrastructure Dependencies
- ecosystem-c — Delivery, Distribution, and Trust
- ecosystem-d — Coordination, Procurement, and Incentives
- ecosystem-e — Resilience, Portability, and Contingencies
- ecosystem-f — Ecosystem Learning and Diffusion

---

## 5. Grid keys

The 16 dimension × stage cells, spelled exactly as the app stores them in
`designs.grid_state`. They are the keys of a pathway's `coverage` map. Each
cell's core question is on its dimension's concept page.

- persona:Explore
- persona:Define
- persona:Pilot
- persona:Scale
- solution:Explore
- solution:Define
- solution:Pilot
- solution:Scale
- institution:Explore
- institution:Define
- institution:Pilot
- institution:Scale
- ecosystem:Explore
- ecosystem:Define
- ecosystem:Pilot
- ecosystem:Scale

---

## 6. Concept kinds

- dimension — one of the four dimensions (page carries its sub-categories and cells)
- stage — one of the four stages
- unit-type — one of the five unit types
- cross-cutting-concern — Data, Trust
- pathway-section — a section of the pathway document (0–6, Source Trace)
- grid-construct — density, density symbol, grid, cell key, coverage map
- weight-level — primary / secondary / dormant as concepts
- thesis — the 30/70 thesis and similar framing claims
- method — extraction discipline, synthesis test, matching test
- rule — a product or business rule the Cube must keep (matching discipline, suggestions not recommendations …)

---

## 7. Thesis groups (30/70)

- build-the-right-thing — Persona + Solution (the ~30%)
- enable-adoption — Institution + Ecosystem (the ~70%)

---

## 8. Audience

The framework-naming rule: what may appear in user-facing prose.

- public-vocabulary — may be said to users (the four dimension names, the four stage names)
- internal-only — never in user-facing prose (sub-category codes, densities, unit-type labels, flowStep)
- contributor-only — may be shown to the contributor of a pathway, never to adopters (Source Trace / Provenance)

---

## 9. Pathway kinds

- single-deployment — one deployment's journey
- cross-deployment-synthesis — lessons drawn across several deployments (e.g. Voice AI for Inclusion)
- horizontal-enabler — an enabling capability pathway illustrated through several deployments (e.g. Data DHARA)

---

## 10. Sectors

Normalised from pathway frontmatter. Write the qualifier (e.g. "skill
development and employment support") in `use_case_category`, not here.

- Agriculture
- Agriculture / Dairy
- Livelihoods
- Education
- Public Health
- Climate
- Governance and Public Services
- Industry and Investment
- Data Infrastructure
- Cross-Sector

---

## 11. Pathway lifecycle

- drafting — a contributor workspace exists, no assembled document
- assembled — the contributor's document is committed to GitHub but NOT live
- published — live through admin publish, or committed in an in-repo corpus and linked from its index
- unindexed — on disk in the grounding corpus but not linked from index.md, so excluded from grounding
- retired — removed or superseded

---

## 12. Asset kinds

- file — stored in the app's private toolkit-assets storage
- link — an https URL

---

## 13. Corpora

The bodies of pathway documents the app grounds the model in. They are NOT
one source of truth: the same slug can hold different text in each. A
pathway's `corpora` names where its copies live; the file paths go in its
`doc_refs`.

- grounding-corpus — `content/wiki/pathways`, framework-structured documents, whole-corpus grounding for the Explorer and Contributor flows, discovered only through `index.md`
- library-corpus — `content/library-wiki/pathways`, conversational overview documents behind the public Diffusion Library, grounded one document at a time
- published-pathways-corpus — the `published_pathways` table, community pathways made live by admin publish and merged into both in-repo corpora by slug (the database copy wins)

---

## 14. Organisation kinds

- product-owner
- implementation-partner
- contributing-organisation
- deploying-institution
- government-body
- ecosystem-partner
- funder
- research-partner
- vendor

---

## 15. Teams

From the Product Charter's execution model. Members are the `people/`
entries whose `teams` names the team. Both teams meet weekly to review
against the current milestone, and hold a formal milestone review with
senior management at each milestone boundary.

- solution-team — "Kamesh + Tekdi Team": solution functionality, UI/UX, data and technical architecture, builds and maintains the web app and the planned Claude Skill channel, handles product and technical user issues
- program-team — "David, Anupama + Team": stakeholder communication, the pathway content lifecycle (review and publish contributor submissions), onboarding adopters, relaying user feedback to the Solution Team

---

## 16. Decision status

- proposed
- accepted
- superseded
- reverted
- rejected

---

## 17. Milestone status

- planned
- in-progress
- at-risk
- done
- missed

---

## 18. Risk status

- open
- mitigated
- materialised
- closed

---

## 19. Likelihood and impact

- low
- medium
- high
- critical
