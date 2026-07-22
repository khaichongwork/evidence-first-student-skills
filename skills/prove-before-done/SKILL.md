---
name: prove-before-done
description: Verify implementation, debugging, automation, migration, and delivery tasks with fresh task-specific evidence before reporting success. Use when a user asks whether work is complete, requests a final check, wants a fix or output verified, or expects completion claims backed by tests, runtime results, generated artifacts, or live external state.
---

# Prove Before Done

Require evidence for every material completion claim. Treat "implemented," "tested," "fixed," "published," and "working" as separate claims unless one check directly proves more than one.

## Verify the task

1. Extract acceptance criteria from the request, specification, issue, or rubric. Do not silently replace them with easier criteria.
2. Inspect the actual changed files and current state. Preserve unrelated user changes.
3. Create one evidence row per material claim.
4. Select the smallest check that directly tests each claim.
5. Run safe checks and capture fresh results. Re-check external state when the claim concerns a remote service, publication, message, or deployment.
6. Classify each claim as `proven`, `partially proven`, `unproven`, or `blocked`.
7. Report the outcome without upgrading partial evidence into success.

For a local Git repository, run `python scripts/collect_repo_evidence.py <repo>` to capture a read-only snapshot before choosing project-specific build or test commands.

## Choose direct evidence

Prefer evidence in this order:

1. Current end-to-end behavior or live remote state
2. Relevant automated tests or deterministic validation
3. Build, type-check, lint, or parser success
4. Static inspection of the exact changed code
5. Assumptions or prior results

Do not treat a zero exit code as sufficient when success also requires a changed artifact, expected content, correct account, fresh timestamp, or reachable remote result. Read [references/evidence-guide.md](references/evidence-guide.md) when the task has multiple outputs, high impact, or an ambiguous success condition.

## Apply safety gates

- Never fabricate, infer, or recycle evidence from an older run.
- Never say a check passed when it was not run.
- Do not run destructive or externally consequential verification unless it is already authorized and necessary.
- Distinguish product failure from unavailable credentials, dependencies, network access, or user input.
- Do not hide failing checks behind a successful unrelated check.
- Do not expose secrets or personal data in logs or final evidence.

## Report compactly

Lead with one of these outcomes:

- **Verified complete**: every material acceptance criterion has direct, fresh evidence.
- **Partially verified**: implementation exists, but one or more material claims lack direct proof.
- **Not verified**: evidence contradicts the completion claim.
- **Blocked**: a named external requirement prevents meaningful verification.

Then list the claim, evidence, and result. Include exact commands only when they help the user reproduce the check.
