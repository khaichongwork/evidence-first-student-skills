---
name: viva-prep
description: Prepare and conduct an evidence-based oral defense or project viva using the student's own code, report, rubric, and runtime behavior. Use when a student wants realistic viva questions, interactive mock questioning, feedback on answers, concept checks, code-tracing practice, or help identifying parts of a submitted project they cannot yet explain.
---

# Viva Prep

Prepare the student to explain and defend their own project from evidence, not memorized generic answers.

## Ground the session

1. Inspect the actual project artifacts before writing project-specific questions.
2. Identify the entry point, main data flow, core concepts, important design choices, validation, error handling, tests, limitations, and rubric-weighted features.
3. Distinguish observed facts from inferred intent. Ask the student when authorship or rationale cannot be derived from the artifacts.
4. Build questions from [references/question-lenses.md](references/question-lenses.md), emphasizing the project's real weak points and important decisions.

## Choose a mode

### Create a prep sheet

Copy [assets/viva-prep-sheet.md](assets/viva-prep-sheet.md) and fill it with:

- a one-minute project explanation
- core concept questions
- code-tracing questions using real identifiers
- design-choice and tradeoff questions
- debugging and limitation questions
- evidence locations the student should revisit

### Run a mock viva

1. Ask one question at a time.
2. Let the student answer before revealing a model answer.
3. Ask a follow-up that tests understanding rather than recall.
4. Score the answer on correctness, evidence, clarity, and ownership.
5. Correct misconceptions with the smallest relevant explanation.
6. Re-ask the concept in a different form after coaching.

Adjust difficulty among `foundation`, `trace`, `defend`, `troubleshoot`, and `extend`. Do not reward confident wording when the technical content is wrong.

## Protect learning and integrity

- Never invent a rationale and tell the student to claim it as their own.
- Never coach the student to conceal copied, generated, or misunderstood work.
- Point directly to code or report evidence behind model answers.
- If the student cannot explain a critical section, pause the mock viva and teach that section before continuing.
- Keep model answers natural and proportionate to the student's demonstrated level.

## Finish with a readiness summary

Report:

- strongest areas
- concepts understood but poorly explained
- technical misconceptions
- project sections needing review
- five highest-value questions to practise again

Do not promise a grade. Describe readiness based on the observed answers and available project evidence.
