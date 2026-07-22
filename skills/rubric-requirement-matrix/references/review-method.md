# Review Method

## Source precedence

Use this default order unless the assignment explicitly states otherwise:

1. Direct instructor clarification specific to the assignment
2. Marking rubric
3. Assignment brief and required output
4. Supplied skeleton, interfaces, and data files
5. Sample output and demonstrations
6. Generic language or framework conventions

Do not silently resolve a contradiction. Record both sources, explain the impact, and mark the row `not verified` when instructor clarification is needed.

## Atomic requirements

Split statements joined by "and," separate marks, or separately testable behavior. Keep a parent ID when useful:

- `R3` Manage records
- `R3.1` Add a record
- `R3.2` Reject a duplicate
- `R3.3` Preserve existing records after rejection

## Evidence quality

- **Direct:** exact runtime result, test, file, symbol, or submission artifact
- **Partial:** some implementation exists, but a condition or behavior is untested
- **Indirect:** comment, claim, or documentation without matching implementation
- **Missing:** no relevant evidence found

## Prioritization

Prioritize mandatory failures and high-weight criteria. Prefer the smallest change that closes the gap without expanding scope, changing forbidden files, or making the submission inconsistent with the learner's demonstrated level.
