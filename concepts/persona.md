---
name: Persona
type: concept
schema_version: 2
aliases:
- Persona
- Persona dimension
- persona-a
- Persona A
- Problem and Persona
- persona-b
- Persona B
- Current Journey and Friction
- persona-c
- Persona C
- Outcome and Success
- persona-d
- Persona D
- Scope, Inclusion, and Trust
- persona:Explore
- persona:Define
- persona:Pilot
- persona:Scale
summary: Are we solving the right problem for the right person?
concept_kind: dimension
definition: Persona — Are we solving the right problem for the right person?
audience: public-vocabulary
broader: grid
central_question: Are we solving the right problem for the right person?
shift: From starting with AI to starting with a specific human outcome
thesis_group: build-the-right-thing
order: 1
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/dimensions.ts
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/framework.md
doc_refs:
- lib/dimensions.ts
- content/framework.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Definition

Are we solving the right problem for the right person?

*From starting with AI to starting with a specific human outcome*

## Sub-categories

Units are tagged `sub_category: persona-<letter>`. Weight per stage: primary =
ask directly, secondary = only if surfaced, dormant = never initiate. The
letters are internal-only.

| Code | Variable | Sub-category | Explore | Define | Pilot | Scale |
|---|---|---|---|---|---|---|
| A | `persona-a` | Problem and Persona | primary | secondary | dormant | secondary |
| B | `persona-b` | Current Journey and Friction | primary | secondary | dormant | dormant |
| C | `persona-c` | Outcome and Success | secondary | primary | primary | primary |
| D | `persona-d` | Scope, Inclusion, and Trust | secondary | primary | primary | primary |

### A. Problem and Persona

- What is the specific problem or pain point being addressed?
- Who specifically experiences this problem?
- In what context, location, language, or circumstance do they experience it?
- Who is currently excluded or underserved, and why?
- What evidence shows that this is a meaningful and persistent problem?

### B. Current Journey and Friction

- How is this need addressed today?
- Which people, channels, systems, and institutions are involved in the current journey?
- Where does the current approach fail, slow down, become unaffordable, or exclude people?
- What do users currently do when the formal system does not work?
- Is AI addressing the actual bottleneck, or merely adding another layer to an already broken process?

### C. Outcome and Success

- If the intervention works, what will be different in the persona's life, decision, or experience?
- What measurable outcome will demonstrate that the problem has been addressed?
- What is the scale of the affected population and the expected depth of impact?
- How quickly must the outcome occur for it to be valuable?
- What leading indicators would show that the solution is moving toward the intended outcome?

### D. Scope, Inclusion, and Trust

- What is the system expected to do, and what is explicitly outside its scope?
- What questions, decisions, or situations must be refused or escalated?
- Which languages, accessibility needs, and edge-user groups must be supported?
- What would make the persona trust, use, or reject the solution?
- Are new user segments appearing that the original design did not anticipate?
- Does the solution strengthen the persona's agency and capability, or create new dependency?

## Grid cells

Keyed `persona:<Stage>` in a pathway's `coverage` and in the app's `designs.grid_state`.

### Persona × Explore — `persona:Explore`

- **Core question:** Who specifically is excluded from this service today — and what do they do instead?
- **Listening for:** The workaround is the data. It reveals the real replacement baseline.
- **Insight form:** Excluded user + named barrier + current workaround
- **Corpus example:** MahaVISTAAR: women farmers receiving contradictory advice from fertiliser sellers. No trusted official source in their language. ([pathway](../pathways/mahavistaar.md))
- **Primary sub-categories here:** A, B

### Persona × Define — `persona:Define`

- **Core question:** What is the one question a user will ask that this system must answer, or the pilot fails?
- **Listening for:** Forces scope to its minimum. Shapes data model, prompt design, safety boundaries.
- **Insight form:** Single critical use case + binary success definition
- **Corpus example:** Voice AI Adoption Barriers: Pradical Works fixed connect rate, talk-time distribution, and lead conversion as success metrics before a single call went out — the resulting pilot data was measurably cleaner than every other pilot in the same cohort. ([pathway](../pathways/voice-ai-adoption-barriers.md))
- **Primary sub-categories here:** C, D

### Persona × Pilot — `persona:Pilot`

- **Core question:** Which user interactions are failing — is that a scope problem or a quality problem?
- **Listening for:** Scope = outside mandate. Quality = mandate questions answered badly. Different fixes.
- **Insight form:** Failure taxonomy: scope vs quality vs experience
- **Corpus example:** AI-Assisted Job Matching: pilot support issues are logged into eight categories from day one — software, data, vacancy input, recommendation quality, workflow, access, training, unknown — so a bad recommendation's real cause is never guessed at after the fact. ([pathway](../pathways/ai-assisted-job-matching.md))
- **Primary sub-categories here:** C, D

### Persona × Scale — `persona:Scale`

- **Core question:** Are new user segments arriving that the pilot wasn't designed for?
- **Listening for:** Scale reveals "the user" was multiple users — feature phone vs smartphone, dialect A vs B.
- **Insight form:** User segment expansion map + design change required per segment
- **Corpus example:** Blue Dots: a model tuned for Dharwad's Kannada underperformed in a neighbouring district using the "same" state language. A local glossary and pace-matched conversation design recovered the engagement a single state-language model had cost. ([pathway](../pathways/blue-dots.md))
- **Primary sub-categories here:** C, D

## Data and trust here

- **Data:** evidence for problem/population/outcome
- **Trust:** does the excluded user trust this channel enough to use it

## How it is used

Every unit carries `dimension: persona`; the dimension name is public
vocabulary, the sub-category letters are not.
