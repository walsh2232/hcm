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

## Oracle Recruiting documentation intake

The Recruiting intake is underway under [draft PR #1](https://github.com/walsh2232/hcm/pull/1). The source registry contains DOC-001 (*Implementing Recruiting*, G34431-12) and companion-source identities. The private local corpus for DOC-001 has 35 chapter files, 648 searchable topic headings, 650 CSV topic-index entries, 751 retrieval chunks, and 16 source-linked task playbooks.

- [Recruiting source workspace](.project/docs/oracle/ORC/README.md)
- [DOC-001 source dossier](.project/docs/oracle/ORC/DOC-001.md)
- [Recruiting playbook index](.project/docs/oracle/ORC/playbooks/README.md)
- [Source issues](.project/docs/oracle/ORC/SOURCE-ISSUES.md) and [GAP-008](.project/docs/gaps.md)
- [Local PDF intake and search tooling](scripts/oracle_docs/README.md)

The HTML ingestion fallback is ready for a local/network-enabled run, but outbound DNS/network access was unavailable during this build, so companion guide bodies are not yet fully indexed. The full PDF and full extracted text corpus are intentionally not committed to this public repo. The edition identifier G34431-12 is not evidence of the target tenant's quarterly release. The companion HTML-ingestion fallback and separate multi-guide search utility are implemented. The latest local wiki validator passes 75/75 checks and the offline tooling regression suite passes 13/13 tests. Live companion retrieval was blocked by outbound DNS/network restrictions, so companion texts remain navigation-only. Latest remote CI after all new changes is still to be confirmed.

## Ground rules

1. **Oracle official documentation is the source of truth.** Every design decision
   cites a registered source. See [`.project/decision-framework.md`](.project/decision-framework.md).
2. **No undocumented assumptions.** If there is no source, an assumption is logged
   with an owner and an expiry date, and a gap is raised.
3. **No production PII in the repository.** Ever. Synthetic fixtures only.
4. **Decisions live in ADRs, not in chat.** If it shaped the solution, it is an ADR.
