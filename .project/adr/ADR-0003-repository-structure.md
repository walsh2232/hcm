# ADR-0003 — Repository structure for enterprise-scale HCM delivery

## Status
Accepted — 2026-08-23

## Context

Oracle HCM delivery produces artifacts that are not application source code:
configuration workbooks, HDL files, HCM Extract definitions, fast formulas,
BI Publisher and OTBI reports, role design matrices, approval rules, and
extensions. Teams routinely scatter these across a document store, a ticketing
tool, several laptops, and the instance itself — after which the instance becomes
the only record of what was configured and why.

At the same time, the project management artifacts (board, backlog, decisions,
requirements) usually live in a separate tool, so a decision and the artifact it
produced never appear in the same place, and neither is reviewable in a pull
request.

## Decision

We will keep the project operating system and the solution artifacts in one
repository, separated by top-level directory, with a `README.md` in each stating
what belongs there and the naming convention that applies.

```
.project/     Board, backlog, ADRs, documentation registry, roles, templates, sprints
config/       Environment & instance registry, non-secret configuration
data/         HDL/HSDL templates and synthetic fixtures — never production PII
extensions/   Fast Formulas, Redwood/VBS extensions, page configurations
integrations/ Inbound & outbound interfaces (REST, SOAP, ATOM, HDL, HCM Extracts)
reports/      BI Publisher and OTBI definitions
security/     Role design matrices, data security policy design
scripts/      Repository tooling
tests/        Test strategy, cases, automation
```

Three rules hold across all of them:

1. **`.project/` is process, everything else is solution.** A directory is one or
   the other, never both.
2. **No production data, ever.** `.gitignore` excludes `data/live/`, extract
   outputs, and credential patterns by default. Synthetic fixtures only. This is a
   hard rule, not a guideline — HCM data is personal data, and a repository is
   forever.
3. **Every artifact traces to a card and a source.** Directory `README`s state the
   naming convention that carries the identifier.

Module code, not marketing name, is the sub-directory key within solution
directories (`integrations/ABS/`, not `integrations/absence/`).

## Consequences

**Easier:** one place to look; decisions reviewable alongside the artifacts they
justify; conventions discoverable without asking; onboarding by reading directory
`README`s; mechanical enforcement of traceability.

**Harder:** non-developer roles (BA, PO, QA) must work through git and pull
requests, which is a real adoption cost and needs support. Some Oracle artifacts —
configuration held only in the instance, sandbox contents — cannot be fully
represented as files, so the repository holds the *design* and the export, not the
live state. That divergence must be actively managed, and it is the main weakness
of this decision.

**Cost:** convention maintenance, and enforcing it at review until it is habit.

## Alternatives considered

- **Separate repositories for process and solution** — rejected: the link between
  a decision and its artifact is what makes either useful, and cross-repository
  links rot.
- **Project management in a dedicated tool (Jira, Azure DevOps)** — rejected *for
  this repository*, not in principle: the board must be reviewable in the same
  pull request as the change. If an external tool becomes the system of record for
  work items, this ADR is superseded and `.project/kanban.md` becomes a mirror.
- **Organise solution directories by module first, artifact type second**
  (`ABS/integrations/`) — rejected: cross-cutting concerns (security, conversion,
  integration patterns) would be duplicated across every module.

## Sources
N/A — internal process decision. No Oracle source applies.
