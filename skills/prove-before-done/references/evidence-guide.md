# Evidence Guide

Use this guide when completion has more than one material claim.

## Claim-to-evidence patterns

| Claim | Strong evidence | Insufficient by itself |
|---|---|---|
| Code implemented | Diff plus targeted behavior check | File exists |
| Bug fixed | Original reproduction now passes plus regression test | Code looks plausible |
| Build succeeds | Fresh build exit code and expected output | Prior build directory |
| File generated | Fresh timestamp, expected content, and readable format | Script exit code |
| Data updated | Query or read-back from the source of truth | Request accepted |
| Message sent | Confirmed sent item or provider response with recipient/thread | Draft created |
| Deployment live | Health check and expected behavior at the deployed target | Push succeeded |
| Repository published | Remote URL, visibility, branch, and commit match | Local commit |

## Evidence matrix

Use one row per claim:

| Claim | Acceptance criterion | Check | Fresh evidence | Result |
|---|---|---|---|---|
| | | | | proven / partial / unproven / blocked |

## Freshness

Compare before and after state when a task must create or update an artifact. Confirm identity as well as freshness: correct account, repository, environment, recipient, branch, or destination.

## Failure reporting

Name the failed criterion and preserve useful error text. Separate a product defect from an unavailable tool, credential, service, dependency, or permission.
