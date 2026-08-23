# Contributing

## Branching

| Branch | Purpose |
| --- | --- |
| `main` | Integration branch. Protected. |
| `feature/HCM-###-short-slug` | One work item from the Kanban board. |
| `docs/HCM-###-short-slug` | Documentation-only change. |
| `fix/HCM-###-short-slug` | Defect fix, linked to a `DEF-###`. |

Every branch maps to exactly one board card. No card, no branch — open the card
first (`.project/templates/story.md`).

## Commit messages

```
<type>(<module>): <summary>          e.g. feat(ABS): add accrual plan design spec

Refs: HCM-000
Source: DOC-000 §4.3
```

`type` is one of `feat`, `fix`, `docs`, `config`, `test`, `chore`, `adr`.
`module` is a module code from [`.project/docs/modules/README.md`](.project/docs/modules/README.md).
`Source:` is required for any commit that encodes a configuration or design
decision; use `Source: NONE (GAP-###)` when the gap is logged and accepted.

## Definition of Ready / Done

A card may not enter **In Progress** unless it meets the Definition of Ready, and
may not enter **Done** unless it meets the Definition of Done. Both are in
[`.project/workflow.md`](.project/workflow.md).

## Pull requests

- Title: `HCM-###: <summary>`
- Body must state: what changed, which registered sources back it, which board
  card it closes, and how it was validated.
- `scripts/project_lint.py` must pass. CI runs it on every PR.
- A PR that changes a design decision must add or supersede an ADR in the same PR.

## Review

| Change type | Required reviewer role |
| --- | --- |
| Architecture, integration pattern, security model | Solution Architect |
| Requirement or process specification | Business Analyst + Product Owner |
| Configuration or code | Developer (peer) + QA |
| Test cases | QA lead |
| Documentation registry entry | Documentation Specialist |

Role definitions and decision rights: [`.project/roles.md`](.project/roles.md).
