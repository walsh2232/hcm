# Working in this repository

This is an Oracle Fusion Cloud HCM implementation repository. It carries both the
project operating system (`.project/`) and the solution artifacts. Read
[`.project/README.md`](.project/README.md) before making changes.

## The rules that are not negotiable

1. **Oracle official documentation is the source of truth.** Every design,
   configuration, or extension decision cites a registered source
   (`DOC-### §location`) from [`.project/docs/source-registry.md`](.project/docs/source-registry.md).
   An unregistered source may not be cited.

2. **Never assert Oracle HCM behaviour from model knowledge.** Model knowledge and
   community material are Tier D: they may form a hypothesis, never justify a
   decision or close a gap. If the registered sources do not answer the question,
   raise a `GAP-###` in [`.project/docs/gaps.md`](.project/docs/gaps.md) and log an
   `ASM-###` with an owner, an expiry, and the cost of being wrong. Do not fill the
   hole with a confident sentence.

   This is the single most likely way to damage this project, because plausible
   and wrong is indistinguishable from correct until it reaches an instance.

3. **No production personal data in this repository.** No extracts, no real
   identifiers, no "anonymised" production rows, no screenshots containing them.
   Synthetic fixtures only. See [`data/README.md`](data/README.md).

4. **No secrets.** No credentials, keys, wallets, or connection strings.

5. **Decisions go in ADRs.** If it is hard to reverse, constrains another module,
   accepts a product limitation, or interprets an ambiguous source, it is an ADR
   ([`.project/adr/`](.project/adr/)), not a comment on a card.

6. **Every change updates the board.** Cards move; `.project/kanban.md` reflects
   reality at the end of every change.

## Before opening a pull request

```bash
python3 scripts/project_lint.py
```

It must pass. Fix failures rather than bypassing them. See
[`scripts/README.md`](scripts/README.md).

## Conventions

- Identifiers, and what each one joins: [`.project/README.md`](.project/README.md).
  The `000` suffix is reserved for documentation examples in every identifier class.
- Branches, commits, pull requests, review: [`CONTRIBUTING.md`](CONTRIBUTING.md).
- Board states, Definition of Ready, Definition of Done: [`.project/workflow.md`](.project/workflow.md).
- Who decides what: [`.project/roles.md`](.project/roles.md).
- Templates for every artifact: [`.project/templates/`](.project/templates/).

## Current state

Documentation intake has not happened. The registry is empty by design
(`GAP-001`), module scope is unconfirmed (`GAP-002`), and three assumptions
(`ASM-001`–`ASM-003`) hold up the current structure. Design work on any module is
gated on intake — see [`.project/kanban.md`](.project/kanban.md).
