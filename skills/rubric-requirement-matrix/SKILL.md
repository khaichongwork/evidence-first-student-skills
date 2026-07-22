---
name: rubric-requirement-matrix
description: Convert assignment briefs, marking rubrics, sample outputs, starter code, and existing student projects into an evidence-based requirement matrix with gaps and minimal next actions. Use when reviewing coursework against stated requirements, identifying likely deductions, checking submission readiness, or reconciling a rubric with the actual project without overbuilding it.
---

# Rubric Requirement Matrix

Map every assessable requirement to concrete evidence in the student's actual project. Keep the review conservative, traceable, and faithful to the supplied brief.

## Build the matrix

1. Read the actual contents of the brief, rubric, sample output, starter files, and project. Do not trust filenames or summaries alone.
2. Record non-negotiable constraints first: editable files, required language or version, mandatory structure, prohibited changes, packaging rules, and sample acceptance values.
3. Split compound rubric statements into atomic requirements. Preserve the original wording and source locator.
4. Assign stable IDs such as `R1`, `R2.1`, and `R2.2`.
5. Locate evidence in exact files, symbols, line numbers, runtime output, tests, or submission artifacts.
6. Mark each row as `met`, `partially met`, `not met`, `not verified`, or `not applicable`.
7. Separate visible implementation from verified behavior. Code presence alone does not prove runtime correctness.
8. Rank gaps by rubric weight, likelihood of deduction, and cost of the smallest credible improvement.
9. Copy [assets/requirements-matrix.md](assets/requirements-matrix.md) when a durable matrix file is useful.

Read [references/review-method.md](references/review-method.md) when sources conflict, criteria are subjective, or supplied sample behavior differs from the prose.

## Keep recommendations credible

- Prefer the assignment document, rubric, sample output, and supplied skeleton over generic best practices.
- Recommend minimal changes that directly close a requirement gap.
- Do not replace the expected design with a more advanced architecture merely because it is more modern.
- Preserve teacher-provided files unless changes are explicitly allowed.
- Label uncertain grading judgments as risks, not facts.
- State when evidence cannot be checked because a required file, environment, or rubric is missing.

## Respect academic ownership

Help the student understand, inspect, test, and improve their own work. Do not fabricate execution evidence, citations, contribution history, or explanations designed to conceal that the student does not understand submitted work. If implementation changes are requested, keep them within the authorized files and explain their connection to the rubric.

## Deliver the review

Lead with overall readiness and the highest-risk deduction. Then provide:

1. Constraint summary
2. Requirement matrix
3. Highest-priority gaps
4. Minimal next actions
5. Items that remain unverified

Use concise, copyable language and cite the relevant source or project location in every material row.
