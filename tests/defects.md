# Defect Log

`DEF-###`. Severity is QA's call; priority is the Product Owner's. Where the two
disagree, both are recorded — that disagreement is information.

| ID | Title | Module | Severity | Priority | Requirement | Test case | Found in | Status | Owner | Resolution |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| _(none)_ | | | | | | | | | | |

## Severity

| Level | Meaning |
| --- | --- |
| S1 | Blocks a critical business process; no workaround |
| S2 | Major function impaired; workaround exists but is costly |
| S3 | Minor function impaired; acceptable workaround |
| S4 | Cosmetic or documentation |

## Rules

- A defect names the test case that found it and the requirement it violates.
- A defect closed without a passing re-test is not closed.
- A defect that turns out to be product behaviour is not a defect: it becomes a
  gap or a fit/gap classification, with the `DOC-###` that establishes the
  behaviour. Reclassify it — do not close it silently.
- Defects deferred past a release are accepted explicitly by the Product Owner,
  on the record, with the business impact stated.
