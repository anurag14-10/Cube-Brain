# Storage adapter — GitHub connector (Claude Desktop chat, web, mobile)

Use this when there is no shell or no local clone of the brain. Every read and
write goes through GitHub connector calls against `repo` on `branch` (the
Configuration block in `SKILL.md`). There is no working copy, no scripts run
against the brain, and CI does the regeneration and validation after a push.

## 0. Check it works before promising anything

Before proposing a capture — before drafting anything — confirm you can
**read** (fetch `CONVENTIONS.md` from `repo`) and that the connector exposes
the write tools: identity, create branch, push files or create/update file,
and, for anyone not in `admins`, fork and create pull request. Then settle
the route in `references/write-route.md` §1–2. Missing tools are handled
there (§5), not here.

| Symptom | Cause | Fix to name |
|---|---|---|
| No GitHub tools at all | Connector not added, or added but switched off for this chat | **Settings → Connectors → Add custom connector**, URL `https://api.githubcopilot.com/mcp/`, OAuth — once per account, covers Desktop, web and mobile. Already added? Switch it on in this chat's tools menu, then start a new chat. Do not clone the repo into a sandbox instead. |
| Tools work, `repo` returns 404 | Private repo not granted — for an org-owned repo, the org has not approved the OAuth app | The repo owner / org admin approves the GitHub app for that repo or org. The repo exists; never say it does not. |
| Write to `repo` refused (403, often "Resource not accessible by integration"), writer **not** in `admins` | Expected — they are not a collaborator | Not a fault, never a reason to ask for collaborator access: take the Fork route, `references/write-route.md` §5. |
| Write to `repo` refused, writer **in** `admins` | The connector's GitHub App is not installed on `repo`, or lacks write | GitHub → Settings → Applications → the connector's app → Repository access → add `repo`; or re-authorise with write scope. |
| Write to the writer's **own fork** refused | App not granted on their account / the new fork, or no write scope | Repository access → **All repositories**, or re-authorise with write scope. |

If you cannot write, say so plainly, claim nothing was saved, and give the
drafted markdown inline so the user can paste it. Never fall back to local or
sandbox files.

## 1. Orient

Fetch `CONVENTIONS.md`, `SCHEMA.yml`, `MASTERS.md` and `INDEX.md` at the start
of the first brain task in a conversation. They are the rules; do not work
from memory of them.

## 2. Answering (Mode A)

- Find candidates in `INDEX.md` (slugs + aliases), then fetch the entries.
- For field questions ("units at Ecosystem × Scale") use the connector's code
  search on `repo` (e.g. `"stage: scale" "dimension: ecosystem" path:units`)
  if it has one; otherwise list the folder and fetch the likely files.
  Say when a search could have missed entries.
- Each dimension's sub-categories and cells are on `concepts/<dimension>.md`;
  each stage on `concepts/<stage>.md`.
- Cite the file path of every entry a claim rests on.

## 3. Capturing (Mode B) — what changes

Steps 1–5 of Mode B are the same (classify, resolve, corroborate, propose,
draft). Then:

1. **Fetch every file you will change immediately before merging into it** —
   not earlier in the conversation. Someone may have pushed since.
2. **Write the activity entry as a new file**, never by editing the digest:
   `activities/entries/{YYYY-MM}/{YYYY-MM-DDTHHMMSSZ}-{github-login}-a1.md`
   containing one line `- {YYYY-MM-DD}: [{type}] {name} — {one line}`. The
   login comes from the identity call, in lowercase. Use the current UTC time;
   if you do not know it, `T000000Z`. List the month folder first and raise
   `-a1` to the first unused `-aN`. Never write `activities/{YYYY-MM}.md` or
   `INDEX.md` — CI regenerates both.
3. **One multi-file push per logging event** — the entity files and the
   activity entry together, commit message starting `cube-brain:`. Only a
   login in `admins` pushes to `branch`; anyone else pushes to a capture
   branch and opens a PR — `references/write-route.md` §5. Several
   single-file commits leave half-written states and an unreadable history.
4. **Validation runs in CI, not here.** The whole-brain validator needs the
   full tree. Check by hand what it would check: required fields for the type,
   every `ref` / `list_ref` slug exists (fetch or search it), every vocab value
   is a `MASTERS.md` term, `schema_version: 2`. Tell the user the build
   validates after the push.
5. **Stale write** (rejected because the file changed): re-fetch, re-merge,
   retry **once**. Never force. If it fails again, tell the user.
6. **Deletes are often refused** by the connector. Do not loop. Mark the entry
   `deprecated: true` with a `supersession_note` saying why, and tell the user
   the file needs removing from a clone.

## 4. Ingesting a pathway (Mode C)

The pathway documents live in the project repo (`diffusion-cube`), which the
connector may or may not reach. If it cannot, ask the user to paste or attach
the document. Then follow `references/ingest-pathway.md`, skipping its script
steps; write the pathway and all its units in one push — to `branch` for an
admin, otherwise to a capture branch with a PR (`references/write-route.md`).

## 5. Report only what happened

Confirm success only against a successful push result, naming the files
written and the commit — or, for a PR, its number and link, as pending review
(`references/write-route.md` §7). A failed or partial push that goes
unmentioned is the worst outcome this skill can produce.
