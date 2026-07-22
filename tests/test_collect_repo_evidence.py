from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "prove-before-done"
    / "scripts"
    / "collect_repo_evidence.py"
)
SPEC = importlib.util.spec_from_file_location("collect_repo_evidence", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CollectRepoEvidenceTests(unittest.TestCase):
    def git(self, repo: Path, *args: str) -> None:
        subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)

    def test_collects_relative_privacy_conscious_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp) / "sample-repo"
            repo.mkdir()
            self.git(repo, "init")
            self.git(repo, "config", "user.name", "Test User")
            self.git(repo, "config", "user.email", "test@example.invalid")
            (repo / "package.json").write_text("{}\n", encoding="utf-8")
            self.git(repo, "add", "package.json")
            self.git(repo, "commit", "-m", "initial")
            (repo / "notes.txt").write_text("changed\n", encoding="utf-8")

            payload = MODULE.collect(repo)

            self.assertEqual(payload["repository"], "sample-repo")
            self.assertIn("package.json", payload["detected_project_files"])
            self.assertFalse(payload["working_tree_clean"])
            self.assertNotIn(str(repo.parent), str(payload))

    def test_rejects_non_git_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, "not inside a Git work tree"):
                MODULE.collect(Path(temp))

    def test_marks_repository_without_commits_as_unborn(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp) / "empty-repo"
            repo.mkdir()
            self.git(repo, "init")

            payload = MODULE.collect(repo)

            self.assertEqual(payload["head"], "(unborn)")


if __name__ == "__main__":
    unittest.main()
