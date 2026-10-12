#!/usr/bin/env python3
"""Which pathways are live in Supabase's `published_pathways`, vs the brain. Read-only.

Community pathways made live by admin publish exist ONLY in this table, so
without it the brain cannot see them, and cannot confirm `lifecycle: published`
for them (SOURCES.md `supabase_db`). This reads the table's public metadata
through Supabase's REST API with the project's ANON key -- the table's RLS
policy is `select using (true)` (migration 0012), so no privileged key is
needed, and a service-role key is refused.

It requests only slug, title, sector, stage, contributor_org, created_at.
Never `content` (unless --content), never `published_by` (a user id), never
any other table. Only GET requests are made.

Credentials come from the environment only -- this never reads .env files:
  SUPABASE_URL       (or NEXT_PUBLIC_SUPABASE_URL)
  SUPABASE_ANON_KEY  (or NEXT_PUBLIC_SUPABASE_ANON_KEY)

Usage:
  python3 scripts/probe_published_pathways.py               # compare with pathways/
  python3 scripts/probe_published_pathways.py --content SLUG > /tmp/x.md
        # one published document's text, for a Mode C ingest of a DB-only pathway
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

FIELDS = "slug,title,sector,stage,contributor_org,created_at"


def env(*names: str) -> str:
    for n in names:
        if os.environ.get(n):
            return os.environ[n]
    sys.exit(f"set {' or '.join(names)} in the environment (never commit it)")


def refuse_service_role(key: str) -> None:
    try:
        payload = key.split(".")[1]
        claims = json.loads(base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4)))
    except (IndexError, ValueError):
        return
    if claims.get("role") == "service_role":
        sys.exit("refusing a service-role key: this probe needs only the anon key")


def get(url: str, key: str, query: dict) -> list[dict]:
    req = urllib.request.Request(
        f"{url.rstrip('/')}/rest/v1/published_pathways?{urllib.parse.urlencode(query)}",
        headers={"apikey": key, "Authorization": f"Bearer {key}", "Accept": "application/json"},
        method="GET")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main() -> int:
    brain = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--content", metavar="SLUG")
    a = ap.parse_args()
    url = env("SUPABASE_URL", "NEXT_PUBLIC_SUPABASE_URL")
    key = env("SUPABASE_ANON_KEY", "NEXT_PUBLIC_SUPABASE_ANON_KEY")
    refuse_service_role(key)

    if a.content:
        rows = get(url, key, {"select": "content", "slug": f"eq.{a.content}"})
        if not rows:
            sys.exit(f"{a.content}: not in published_pathways")
        sys.stdout.write(rows[0]["content"])
        return 0

    rows = get(url, key, {"select": FIELDS, "order": "slug"})
    live = {r["slug"]: r for r in rows}
    entries = {}
    for p in sorted((brain / "pathways").glob("*.md")):
        text = p.read_text(encoding="utf-8")
        entries[p.stem] = (yaml.safe_load(text.split("---", 2)[1]) or {}) if text.startswith("---") else {}

    print(f"# published_pathways — {len(live)} live row(s)\n")
    for slug, r in live.items():
        fm = entries.get(slug)
        if fm is None:
            print(f"  MISSING   {slug}: live since {str(r.get('created_at'))[:10]} "
                  f"({r.get('sector') or 'no sector'}, {r.get('stage') or 'no stage'}) — no brain entry; ingest it")
        elif "published-pathways-corpus" not in (fm.get("corpora") or []):
            print(f"  CORPORA   {slug}: live in the DB but `corpora` omits published-pathways-corpus "
                  "(a same-slug DB row replaces the library copy — see concepts/pathway-lifecycle)")
    for slug, fm in entries.items():
        if "published-pathways-corpus" in (fm.get("corpora") or []) and slug not in live:
            print(f"  GONE      {slug}: brain says published-pathways-corpus but no live row")
    print("\nRecord what you act on with sources: {system: supabase_db, method: queried, "
          "date: <today>, ref: published_pathways metadata}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
