---
name: explain-my-own-code
description: Teach a learner how their existing code works using the real project structure, identifiers, execution flow, and concrete examples at an appropriate level. Use when someone asks for a line-by-line explanation, program flow, data structure walkthrough, debugging explanation, concept mapping, presentation preparation, or a check that they genuinely understand code they possess.
---

# Explain My Own Code

Teach from the learner's actual code. Optimize for understanding and accurate ownership, not impressive terminology.

## Inspect before explaining

1. Open the real entry point and relevant surrounding files. Do not explain a snippet as if it were the whole program.
2. Determine the learner's level from their request or prior answers. If unclear, start at an intermediate beginner level and adjust quickly.
3. Identify the program's observable purpose, entry point, main flow, data model, important state changes, and outputs.
4. Separate facts visible in code from inferred intent and unknown external behavior.

Read [references/teaching-levels.md](references/teaching-levels.md) when choosing depth, terminology, or the size of each explanation step.

## Explain in layers

1. **Purpose:** State what the selected code does in plain language.
2. **Map:** Show where it sits in the project and what calls it.
3. **Flow:** Trace one realistic input through the exact functions, conditions, and state changes.
4. **Concepts:** Connect concrete code to relevant programming concepts.
5. **Details:** Explain difficult lines, operators, APIs, or data structures using real identifiers.
6. **Limits:** Identify assumptions, edge cases, and behavior that cannot be confirmed without running the project.
7. **Teach-back:** Ask the learner to predict a small variation or explain the flow back in their own words.

Copy [assets/code-explanation-notes.md](assets/code-explanation-notes.md) when the learner wants durable study notes.

## Keep the explanation trustworthy

- Quote only the smallest code fragment needed for context.
- Use exact filenames, symbols, and line references when available.
- Do not claim code was written by the learner or by any particular tool without evidence.
- Do not rewrite or refactor the project unless the user asks for a change.
- When code is incorrect, explain observed behavior before proposing a fix.
- When a concept depends on runtime data, run a safe test or label the explanation as provisional.
- Do not supply a memorized defense intended to hide lack of understanding; teach the missing concept.

## Adapt the output

Use a short walkthrough for simple functions, a numbered trace for control flow, a state table for changing data, and a small diagram only when relationships would otherwise be difficult to follow. End with two or three targeted comprehension checks rather than a generic quiz.
