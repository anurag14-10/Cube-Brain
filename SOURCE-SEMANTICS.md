# Source semantics — Cube-Brain

What each source *means in this project*. Every claim is dated and says how
it was established. Add a line the first time somebody learns one of these the
hard way.

---

## `diffusion_cube_code`

### Terms that mean something particular here

- **"design" / `designs` = an adoption.** The UI says adoption or
  conversation; the table is `designs` (legacy name). `design_documents` are
  the generated documents of an adoption. (code, 2026-10-08)
- **"assemble" ≠ publish.** `POST /api/pathways/assemble` commits a draft to
  GitHub and sets `review_requested`; nothing goes live until an admin calls
  `POST /api/admin/pathways/publish`, which writes `published_pathways`.
- **"Navigate" = "Analyse".** The Explorer flow was renamed; old stored
  intent values (`navigate`, `discover`, `strengthen`, `troubleshoot`, `open`)
  all resolve to the one `ANALYSE_FLOW`. `/navigate` still exists as a page.
- **`plan` doc_type = Executive Summary.** Not a project plan.
- **"wiki" means three things**: the in-repo grounding corpus
  (`content/wiki/pathways`), the `/wiki` page that browses it, and the
  generated developer docs (`docs/wiki/diffusion-cube`). Say which.
- **"organisations"** is both a DB table (a registry rows found-or-created at
  join) and, in this brain, an entity type for real organisations. The table
  is `tables/organisations-table`.

### Structural facts that bite

- `content/wiki/pathways/index.md` is the **sole discovery path** for the
  grounding corpus: a file on disk but not linked from it is excluded from
  grounding and the `/wiki` listing. (docs wiki TD-07, 2026-09-28)
- Two in-repo corpora hold **independently maintained** documents under the
  same slugs (`mahavistaar`, `blue-dots`, …). Same slug ≠ same text.
- `published_pathways` rows override in-repo files **by slug** at read time.
- `contribution_units` was inert until migration 0034 repurposed it for
  toolkit-asset files; it is no longer purely inert.
- Migration 0008 is destructive (deleted old 7-dimension rows).

### What this source structurally cannot answer

Usage, popularity, who made a decision, when a decision was made (only when
it was committed), what is planned.

---

## `diffusion_cube_docs`

- The generated wiki under `docs/wiki/diffusion-cube` was last refreshed
  2026-09-28 against branch `Swanand_DC`; it documents 32 migrations, the repo
  has 34 (0033 account deletion, 0034 toolkit assets). Treat it as stale for
  anything after that date. (checked 2026-10-08)
- `ARCHITECTURE.md` is reliable except its grid table-vs-chips paragraph.
- `CLAUDE.md`'s product description at repo root is current in summary, but
  older statements quoted by the wiki (four-intent menu, single-step publish)
  are superseded.

---

## `raw_documents`

- The Product Charter carries its own Requirements and Feedback tabs; there is
  no external ticket tracker. Statuses are as of the charter's last edit.
- The charter records the Anthropic API account as a **free account expiring
  28-Oct-2026** and the AWS account expiring **December 2026**. Re-verify
  before relying on either.

---

## `supabase_db`

- Contains production user data. Only schema, published-pathway metadata and
  counts may be read into this brain.

---

## Fields no source can fill

- `decisions.status` and `decided_by` — a person must say.
- `pathways.lifecycle = published` for DB-only pathways without DB access.
- Anything about clearance to name a contributor publicly — not recorded here
  at all; the app's Terms §5.6 governs it.
