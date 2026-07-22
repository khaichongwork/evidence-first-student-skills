#!/usr/bin/env python3
"""Validate this repository's Agent Skill packages without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {
    "prove-before-done",
    "rubric-requirement-matrix",
    "viva-prep",
    "explain-my-own-code",
}
LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|#)([^)]+)\)")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        raise ValueError("unclosed YAML frontmatter")
    values: dict[str, str] = {}
    for raw in parts[1].splitlines():
        if not raw.strip():
            continue
        if ":" not in raw:
            raise ValueError(f"invalid frontmatter line: {raw}")
        key, value = raw.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def validate_skill(folder: Path) -> list[str]:
    errors: list[str] = []
    skill_file = folder / "SKILL.md"
    if not skill_file.is_file():
        return ["SKILL.md is missing"]

    text = skill_file.read_text(encoding="utf-8")
    try:
        frontmatter = parse_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]

    if set(frontmatter) != {"name", "description"}:
        errors.append("frontmatter must contain only name and description")
    if frontmatter.get("name") != folder.name:
        errors.append("frontmatter name must match the folder name")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", folder.name):
        errors.append("folder name must use lowercase hyphen-case")
    description = frontmatter.get("description", "")
    if len(description) < 80 or "Use when" not in description:
        errors.append("description must clearly state what the skill does and when to use it")
    if "TODO" in text:
        errors.append("unresolved TODO found")
    if len(text.splitlines()) > 500:
        errors.append("SKILL.md exceeds 500 lines")

    for target in LINK_RE.findall(text):
        clean_target = target.split("#", 1)[0]
        if clean_target and not (folder / clean_target).is_file():
            errors.append(f"broken local link: {target}")

    metadata = folder / "agents" / "openai.yaml"
    if not metadata.is_file():
        errors.append("agents/openai.yaml is missing")
    else:
        metadata_text = metadata.read_text(encoding="utf-8")
        if f"${folder.name}" not in metadata_text:
            errors.append("default prompt must explicitly mention the skill")
        short_match = re.search(r'^\s*short_description:\s*"([^"]+)"', metadata_text, re.MULTILINE)
        if not short_match or not 25 <= len(short_match.group(1)) <= 64:
            errors.append("short_description must be 25 to 64 characters")

    for resource_name in ("scripts", "references", "assets"):
        resource = folder / resource_name
        if resource.is_dir() and not any(path.is_file() for path in resource.rglob("*")):
            errors.append(f"empty resource directory: {resource_name}")

    return errors


def main() -> int:
    found = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    failures: list[str] = []
    if found != EXPECTED:
        failures.append(f"expected skills {sorted(EXPECTED)}, found {sorted(found)}")

    for name in sorted(found):
        errors = validate_skill(SKILLS / name)
        if errors:
            failures.extend(f"{name}: {error}" for error in errors)
        else:
            print(f"PASS {name}")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}", file=sys.stderr)
        return 1

    print(f"Validated {len(found)} skills successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
