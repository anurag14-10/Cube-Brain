#!/usr/bin/env python3
"""Package skills/cube-brain as a `.skill` for Claude Desktop / web upload.

A `.skill` is a zip of the skill folder (`cube-brain/SKILL.md`,
`cube-brain/references/…`), uploaded via Customize → Skills. Chat surfaces
have no shell, so they cannot be pointed at a brain after upload: `--repo`
bakes the GitHub owner/name into the Configuration block of the packaged
copy. The source tree is never modified.

Usage:
  python3 scripts/build_skill.py                              # repo as in SKILL.md
  python3 scripts/build_skill.py --repo tekdi/Cube-Brain      # bake another repo
  python3 scripts/build_skill.py --out ~/Desktop/Cube-Brain   # write it elsewhere

Pure standard library. The zip is reproducible: same source, same bytes.
"""
from __future__ import annotations

import argparse
import io
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "cube-brain"

# The frontmatter contract Anthropic's skill upload enforces.
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
DESCRIPTION_LIMIT = 1024
FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def frontmatter(text: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        sys.exit("SKILL.md has no closed YAML frontmatter")
    fields: dict[str, str] = {}
    current = None
    for line in m.group(1).splitlines():
        if line and not line.startswith((" ", "\t", "#")):
            key, _, value = line.partition(":")
            current = key.strip()
            fields[current] = value.strip()
        elif current and line.strip():
            fields[current] = (fields[current] + " " + line.strip()).strip()
    return fields


def validate(text: str) -> None:
    fields = frontmatter(text)
    extra = set(fields) - ALLOWED_KEYS
    if extra:
        sys.exit(f"frontmatter key(s) not accepted on upload: {', '.join(sorted(extra))}")
    if fields.get("name") != SKILL_DIR.name:
        sys.exit(f"frontmatter name must be `{SKILL_DIR.name}` (the folder name)")
    description = fields.get("description", "").lstrip(">").strip()
    if not description:
        sys.exit("frontmatter is missing `description`")
    if len(description) > DESCRIPTION_LIMIT:
        sys.exit(f"description is {len(description)} characters; the upload limit is {DESCRIPTION_LIMIT}")
    if "<" in description or ">" in description:
        sys.exit("description must not contain angle brackets")


def bake_repo(text: str, repo: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        sys.exit(f"--repo must be owner/name, got {repo!r}")
    baked, n = re.subn(r"(?m)^repo: \S+", f"repo: {repo}", text, count=1)
    if n != 1:
        sys.exit("no `repo:` line in SKILL.md's Configuration block")
    return baked


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", help="GitHub owner/name to bake in (default: as in SKILL.md)")
    ap.add_argument("--out", default=str(ROOT / "dist"), help="output folder (default: dist/)")
    a = ap.parse_args()

    skill_md = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    if a.repo:
        skill_md = bake_repo(skill_md, a.repo)
    validate(skill_md)
    repo = re.search(r"(?m)^repo: (\S+)", skill_md).group(1)

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(SKILL_DIR.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            rel = path.relative_to(SKILL_DIR.parent)
            info = zipfile.ZipInfo(str(rel), date_time=FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            data = skill_md.encode("utf-8") if path.name == "SKILL.md" and rel.parent.name == SKILL_DIR.name \
                else path.read_bytes()
            archive.writestr(info, data)

    out = Path(a.out).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    target = out / "cube-brain.skill"
    target.write_bytes(buffer.getvalue())
    print(f"wrote {target} ({len(buffer.getvalue()) // 1024} kB) — brain repo baked in: {repo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
