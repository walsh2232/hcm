# Oracle HCM Implementation & Development

Repository for the design, configuration, extension, and integration work of an
Oracle Fusion Cloud HCM implementation.

> **Status: inception / documentation intake started.** The first Recruiting source
> (*Implementing Recruiting*, guide edition G34431-12) has been received, fingerprinted,
> and indexed locally. Official companion sources are catalogued in the registry.
> Project-wide design remains gated by unresolved module scope and target quarterly
> release in [`.project/docs/gaps.md`](.project/docs/gaps.md). The full derived text
> corpus and source PDFs are intentionally not committed to this public repository.

## Start here

| If you want to… | Read |
| --- | --- |
| Understand how this project runs | [`.project/README.md`](.project/README.md) |
| See what is being worked on | [`.project/kanban.md`](.project/kanban.md) |
| See what is coming | [`.project/backlog.md`](.project/backlog.md) |
| Know who decides what | [`.project/roles.md`](.project/roles.md) |
| Know how a decision gets validated | [`.project/decision-framework.md`](.project/decision-framework.md) |
| Find the authoritative Oracle source for a design | [`.project/docs/source-registry.md`](.project/docs/source-registry.md) |
| See why something was built this way | [`.project/adr/`](.project/adr/) |
| Contribute a change | [`CONTRIBUTING.md`](CONTRIBUTING.md) |

## Repository layout

```
.project/          Project operating system: Kanban, backlog, ADRs, doc registry,
                   role charters, decision framework, templates, sprints
config/            Environment & instance registry, non-secret configuration
data/              HDL / HSDL templates and synthetic fixtures (no production PII)
extensions/        Fast Formulas, Redwood/VBS extensions, page configurations
integrations/      Inbound & outbound interfaces (REST, SOAP, ATOM, HDL, HCM Extracts)
reports/           BI Publisher and OTBI report definitions
security/          Role design matrices, data security policy design
scripts/           Repository tooling (project lint, validators)
tests/             Test strategy, test cases, automation
```

Each directory carries its own `README.md` describing what belongs there and the
naming conventions that apply.

## Ground rules

1. **Oracle official documentation is the source of truth.** Every design decision
   cites a registered source. See [`.project/decision-framework.md`](.project/decision-framework.md).
2. **No undocumented assumptions.** If there is no source, an assumption is logged
   with an owner and an expiry date, and a gap is raised.
3. **No production PII in the repository.** Ever. Synthetic fixtures only.
4. **Decisions live in ADRs, not in chat.** If it shaped the solution, it is an ADR.
