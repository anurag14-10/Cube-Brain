# Sync the Cube-Brain with the diffusion-cube code

The brain records, on every product entry, the commit it was last checked
against (`verified_at_commit`). Syncing brings those entries level with the
repo HEAD and adds entries for anything new.

## 1. Get the plan (deterministic — no reasoning yet)

```bash
git -C "$CUBE_REPO" pull --ff-only        # only if the user wants the latest remote state
python3 scripts/cube_sync_plan.py          # or --since <sha>, or --json
```

It prints: the commits since the brain's last verified commit, every changed
file with the brain entries that describe it, files with **NO ENTRY** and the
type they should become, and env vars newly read by the code.

## 2. Work the plan, by path type

| Change | Update |
|---|---|
| `supabase/migrations/NNNN_*.sql` added | New `migrations/mNNNN-*`; update every `tables/` entry it touches (columns, RLS, status; `dropped_in` if dropped); new table → new `tables/` entry with `created_in`; a destructive or design-changing migration usually embodies a `decisions/` entry. |
| `app/api/**/route.ts` | `endpoints/` entry: methods, access (the real gate), roles, tables_read/written, status. New route → new entry; deleted route → `status: retired` + supersession fields (do not delete the file). Then any `features/` / `workflows/` listing it. |
| `app/**/page.tsx` | `pages/` entry: access behaviour, components, endpoints. |
| `lib/system-prompts.ts` | `prompts/`, `chat-modes/` (max_tokens, triggers), `contracts/grid-update`, and `rules/` whose wording changed. |
| `lib/grid-update.ts`, `lib/adoption-conversation.ts` | `contracts/` (grid-update, designs-meta, grid-state) + modules. |
| `lib/dimensions.ts`, `content/framework.md` | Framework layer: `seed_from_repo.py --only framework --dry-run`; apply deliberately with `--force` only to files not enriched by hand; if unit types or weights changed, update MASTERS 1/2 in the same commit. |
| `content/wiki/pathways/*.md`, `content/library-wiki/pathways/*.md` | `references/ingest-pathway.md`. `index.md` change → pathway `lifecycle`. |
| other `lib/`, `components/` files | `modules/` entry (responsibilities, depends_on, tables, integrations, status). |
| new `process.env.X` | `config/x.md` — name, required, secret, browser_exposed, read_by. Never the value. |
| `package.json` | `integrations/` sdk ranges; new external service → new integration. |
| `Dockerfile`, `.github/workflows/*`, `next.config.ts`, `proxy.ts` | `environments/`, `modules/`. |
| `specs/*`, `docs/tasks/*`, `docs/raw_documents/*` | `requirements/`, `milestones/`, `decisions/`, `risks/`. |

For every touched product entry: re-read the code, update fields, set
`verified_at_commit` to HEAD and `last_updated` to today. Status changes
follow MASTERS 12 (`live` / `dead-code` / `inert` / `retired` …).

## 3. Always add

- A `releases/` entry per merged PR or direct-to-main change set: date, PR
  number, commits, authors, and refs to the features/migrations/decisions it
  brought.
- `decisions/` for any choice the diff makes visible (a removed flow, a new
  gate, a new storage approach) — context and alternatives from the PR
  description, spec, or the user; if nobody stated why, write what the code
  shows and mark it `derived`.
- `tech-debt/` resolution when a change fixes a TD (`status: resolved`,
  `resolved_on`, `resolution`), and new TDs for shortcuts the diff introduces.
- `incidents/` if the change fixes something that was broken in use.

## 4. Finish

Regenerate + validate (SKILL.md Mode B step 7), activity entry, and one commit:
`cube-brain: sync to diffusion-cube <short-sha> (<n> entries updated, <m> new)`.
Then `python3 scripts/cube_report.py --section freshness` should show all
product entries current.
