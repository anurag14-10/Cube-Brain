# Masters — Cube-Brain

The controlled vocabularies every `vocab:` / `list_vocab:` field in
`SCHEMA.yml` is checked against. The number in each heading is the id
`SCHEMA.yml` uses (`vocab: "7"` → master 7).

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

Where a master mirrors an enum in the diffusion-cube code (unit types, doc
types, weights), the code is the source of truth. If the code changes, change
the master in the same commit as the entities that use the new value.

---

## 1. Unit types

Mirrors `UNIT_TYPES` in `lib/dimensions.ts`. Definitions live in `concepts/`.

- Strategic Decision — framing, governance or design decision that shaped what got built
- Tactical Decision — stack, sequence, cost or implementation decision specific enough to reuse
- Failure and Fix — what broke, the fix, and what the fix revealed
- Playbook — a genuine multi-step gated sequence
- Toolkit Asset — an actual reusable artifact someone else can lift and adapt

---

## 2. Sub-category stage weights

Mirrors `SubCategoryWeight` in `lib/dimensions.ts`.

- primary — ask or check directly at this stage
- secondary — only if relevant or surfaced by the core question
- dormant — never initiate; follow only if the user raises it

---

## 3. Concept kinds

- unit-type — one of the five unit types
- cross-cutting-concern — Data, Trust
- pathway-section — a section of the pathway document (0–6, Source Trace)
- grid-construct — density, density symbol, grid, cell key, coverage map
- weight-level — primary / secondary / dormant as concepts
- thesis — the 30/70 thesis and similar framing claims
- method — extraction discipline, synthesis test, matching test
- product-term — a word the app or team uses (Adoption, Flow, flowStep, Assemble …)
- ai-term — a model/LLM-side term (grid_update, explorerAction, conversation mode …)
- role-term — persona words (Explorer, Contributor, Adopter)

---

## 4. Thesis groups (30/70)

- build-the-right-thing — Persona + Solution (the ~30%)
- enable-adoption — Institution + Ecosystem (the ~70%)

---

## 5. Audience

The framework-naming rule: what may appear in user-facing prose.

- public-vocabulary — may be said to users (the four dimension names, the four stage names)
- internal-only — never in user-facing prose (sub-category codes, densities, unit-type labels, flowStep)
- contributor-only — may be shown to the contributor of a pathway, never to adopters (Source Trace / Provenance)

---

## 6. Pathway kinds

- single-deployment — one deployment's journey
- cross-deployment-synthesis — lessons drawn across several deployments (e.g. Voice AI for Inclusion)
- horizontal-enabler — an enabling capability pathway illustrated through several deployments (e.g. Data DHARA)

---

## 7. Sectors

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

## 8. Pathway lifecycle

- drafting — a contributor workspace exists (`pathways` row), no assembled document
- assembled — contributor "assemble" committed it to GitHub; NOT live
- published — admin publish copied it to `published_pathways`, or it is committed in an in-repo corpus and linked from its index
- unindexed — on disk in the grounding corpus but not linked from index.md, so excluded from grounding
- retired — removed or superseded

---

## 9. Asset kinds

Mirrors `contribution_units.asset_kind`.

- file — stored in the private `toolkit-assets` bucket
- link — an https URL

---

## 10. Corpus kinds

- static-repo — markdown committed in the diffusion-cube repo
- database — rows in a Supabase table
- merged-view — a read-time merge of the above

---

## 11. Organisation kinds

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

## 12. Implementation status

Shared by features, workflows, pages, endpoints, chat modes, prompts, tables,
modules and environments.

- live — in use on the deployed path
- in-progress — being built, partially present
- planned — intent only; nothing in code
- inert — exists in code or schema, nothing uses it
- dead-code — present and referenced, but broken or unreachable (e.g. queries a dropped table)
- dropped — removed (tables)
- retired — deliberately removed or replaced

---

## 13. Workflow kinds

- user-journey
- admin-process
- system-process
- llm-pipeline
- dev-process

---

## 14. Access levels

What actually gates a page or endpoint.

- public — no session needed
- signed-in — any authenticated session
- role-gated — a specific role from `roles/`
- admin-only — admin role row or ADMIN_EMAILS allow-list
- webhook-secret — called by Supabase with a shared secret
- service-role — server-only, never called by a browser

---

## 15. HTTP methods

- GET
- POST
- PUT
- PATCH
- DELETE

---

## 16. Generated document types

Mirrors `design_documents.doc_type`, plus non-persisted outputs.

- analysis — Explorer Analysis Document
- plan — Executive Summary / Plan Document
- draft — Contributor pathway document draft
- none — produces no stored document

---

## 17. Contract kinds

- llm-output — a block the model must emit (grid_update)
- json-state — JSON persisted in a jsonb column (meta, grid_state, messages)
- api-payload — request/response body of an endpoint
- document-format — markdown/frontmatter structure of a document
- storage-layout — object paths and naming in a bucket
- email-hook — a payload exchanged with Supabase Auth hooks

---

## 18. Store kinds

- table
- storage-bucket
- auth-schema
- view

---

## 19. Module kinds

- lib
- component
- page-file
- route-handler
- middleware
- script
- content
- config
- ci

---

## 20. Integration kinds

- llm
- database
- auth
- object-storage
- email
- version-control
- spreadsheet-logging
- hosting
- ci-cd
- document-parsing
- pdf-generation

---

## 21. Environment kinds

- production
- staging
- local
- container

---

## 22. Enforcement layers

- prompt — an instruction to the model only
- code — application logic
- rls — Postgres row-level security
- db-constraint — check / unique / FK constraint
- storage-policy — bucket limits and policies
- data — encoded in a data structure (e.g. weights)
- process — a human step (admin review)

---

## 23. Decision status

- proposed
- accepted
- superseded
- reverted
- rejected

---

## 24. Requirement types

- functional
- non-functional

---

## 25. Requirement status

Mirrors the Product Charter's Requirements tab.

- not-started
- in-progress
- complete
- dropped

---

## 26. Milestone status

- planned
- in-progress
- at-risk
- done
- missed

---

## 27. Tech-debt severity

- P0 — critical
- P1 — high
- P2 — medium
- P3 — low

---

## 28. Tech-debt status

- open
- in-progress
- resolved
- wont-fix

---

## 29. Risk status

- open
- mitigated
- materialised
- closed

---

## 30. Likelihood and impact

- low
- medium
- high
- critical

---

## 31. Incident severity

- sev1 — production down or data loss
- sev2 — a core flow broken for users
- sev3 — degraded or silent failure
- sev4 — cosmetic or dev-only

---

## 32. Incident status

- open
- monitoring
- fixed
