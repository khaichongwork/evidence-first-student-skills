#!/usr/bin/env python3
"""Collect a read-only, privacy-conscious snapshot of a local Git repository."""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


EVIDENCE_FILES = (
    "package.json",
    "pyproject.toml",
    "requirements.txt",
    "Cargo.toml",
    "go.mod",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
    "Makefile",
    "CMakeLists.txt",
)


def git(repo: Path, *args: str) -> tuple[int, str]:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    return result.returncode, result.stdout.strip()


def collect(repo: Path) -> dict[str, object]:
    repo = repo.resolve()
    if not repo.is_dir():
        raise ValueError("repository path is not a directory")

    inside_code, inside = git(repo, "rev-parse", "--is-inside-work-tree")
    if inside_code != 0 or inside != "true":
        raise ValueError("path is not inside a Git work tree")

    _, branch = git(repo, "branch", "--show-current")
    head_code, head = git(repo, "rev-parse", "HEAD")
    if head_code != 0:
        head = "(unborn)"
    _, status = git(repo, "status", "--porcelain=v1")
    _, diff_stat = git(repo, "diff", "--stat")
    _, staged_stat = git(repo, "diff", "--cached", "--stat")

    return {
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository": repo.name,
        "branch": branch or "(detached)",
        "head": head,
        "working_tree_clean": not bool(status),
        "status": status.splitlines(),
        "unstaged_diff_stat": diff_stat.splitlines(),
        "staged_diff_stat": staged_stat.splitlines(),
        "detected_project_files": [name for name in EVIDENCE_FILES if (repo / name).is_file()],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".", help="Git repository to inspect")
    parser.add_argument("--compact", action="store_true", help="emit compact JSON")
    args = parser.parse_args()

    try:
        payload = collect(Path(args.repo))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps(payload, indent=None if args.compact else 2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
