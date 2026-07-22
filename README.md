# Evidence-First Student Skills

[![Validate skills](https://github.com/ewkhaichong9916-rgb/evidence-first-student-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/ewkhaichong9916-rgb/evidence-first-student-skills/actions/workflows/validate.yml)

Four small Agent Skills for verifying project work, reviewing requirements, preparing for a viva, and understanding existing code. They are designed to support genuine learning and evidence-based completion without ghostwriting or fabricated proof.

## Skills

| Skill | Use it to |
|---|---|
| [`prove-before-done`](skills/prove-before-done/) | Require fresh evidence before reporting that a task is complete |
| [`rubric-requirement-matrix`](skills/rubric-requirement-matrix/) | Map every rubric item to concrete project evidence and minimal next actions |
| [`viva-prep`](skills/viva-prep/) | Create project-specific questions or conduct an interactive mock viva |
| [`explain-my-own-code`](skills/explain-my-own-code/) | Teach a learner how their real code works at an appropriate level |

Each skill is independent. Install only the ones you need.

## Install

Copy a skill directory into a location supported by your agent:

```text
<project>/.agents/skills/<skill-name>/
```

For GitHub Copilot project skills, use:

```text
<project>/.github/skills/<skill-name>/
```

For a personal installation, copy the selected directory to the personal skills directory documented by your agent. The directory containing `SKILL.md` must retain its bundled `scripts/`, `references/`, `assets/`, and `agents/` files.

## Example prompts

```text
Use $prove-before-done to verify this fix before calling it complete.

Use $rubric-requirement-matrix to compare my project with this assignment brief.

Use $viva-prep to run a mock viva using my actual Java project.

Use $explain-my-own-code to trace how this function changes the linked list.
```

## Design principles

- Inspect actual artifacts instead of trusting filenames or claims.
- Separate implementation from verified behavior.
- Cite concrete project evidence.
- Prefer minimal, requirement-bound improvements.
- Never invent test results, authorship, rationale, or academic evidence.
- Teach missing concepts instead of helping a learner conceal them.

## Validate

Run the repository checks from the root:

```bash
python tests/validate_skills.py
python -m unittest discover -s tests -v
```

The GitHub Actions workflow runs the same checks on every push and pull request.

## License

MIT
