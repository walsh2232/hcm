# Data

HCM Data Loader templates and **synthetic** fixtures.

```
data/templates/   HDL / HSDL templates per business object, version controlled
data/fixtures/    Synthetic test data — generated, never derived from production
data/live/        Working directory for real loads. GITIGNORED. Never committed.
```

## The rule that matters

**No production personal data enters this repository. Ever.**

Not in a fixture, not in a sample file, not in a screenshot, not "just this once
to reproduce a defect", not with the names changed. HCM data is personal data —
national identifiers, salaries, health-related absence, performance ratings — and
a git repository keeps it forever, across every clone, in every branch, after
every deletion.

`.gitignore` excludes `data/live/`, `*.dat`, and loose `*.csv` outside
`templates/` and `fixtures/`. That is a backstop, not the control. The control is
that nobody puts it there.

If production data does reach the repository, it is a data incident: stop, notify
the Solution Architect and the Product Owner, and follow the organisation's
incident process. Do not quietly force-push over it.

## Naming

```
data/templates/<MODULE>/<BusinessObject>.dat        e.g. templates/GHR/Worker.dat
data/fixtures/<MODULE>/<scenario>-<n>.csv           e.g. fixtures/ABS/accrual-carryover-01.csv
```

Every template names, in a header comment, the `DOC-###` establishing its
structure and the release it was validated against. Object structures change
between releases; an undated template is a defect waiting to happen.

Test data strategy: `HCM-027`. Template library and validation harness: `HCM-024`.
