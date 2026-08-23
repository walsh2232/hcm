# Reporting & Analytics

OTBI analyses and BI Publisher report definitions.

```
reports/<MODULE>/<report-name>/
    design.md      Purpose, audience, data definition, security, refresh
    definition/    Exported report/analysis definition and layouts
    tests/         Expected-output checks against synthetic fixtures
```

## Selection

The rule for choosing OTBI versus BI Publisher versus extract-and-warehouse is
established by `HCM-029`. As a working principle pending that ADR: OTBI for
operational and ad-hoc analysis over transactional subject areas, BI Publisher for
statutory, high-volume, and pixel-precise document output.

## Every report design states

- Audience, decision it supports, and refresh expectation
- Subject areas or data model used, and the `DOC-###` confirming availability
- **Security inheritance** — reporting must not become a route around the role
  model. State which roles see which rows, and how that is enforced.
- Personal data exposed and the justification for exposing it
- Performance expectation at production volume
