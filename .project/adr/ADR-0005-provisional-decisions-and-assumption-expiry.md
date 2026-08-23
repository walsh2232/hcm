# ADR-0005 — Provisional decisions and assumption expiry

## Status
Accepted — 2026-08-23

## Context

`ADR-0002` makes Oracle documentation the source of truth. Applied naively, that
stops all work whenever documentation is missing — which, at inception, is
everywhere (`GAP-001`). The opposite failure is worse: proceeding on unstated
assumptions that later read as established fact, so that nobody knows which parts
of the design rest on evidence and which rest on a guess made in week two.

Assumption registers usually fail the same way. Entries are written once, never
reviewed, and are quietly treated as facts within a month.

## Decision

We will allow work to proceed on unresolved questions under logged assumptions,
with the assumption made structurally impossible to forget.

1. **Gap first.** An unanswerable question raises a `GAP-###` with a type, an
   owner, and the decision it blocks.
2. **Assumption second.** Work proceeds under an `ASM-###` recording: the
   assumption, its basis and tier, what it affects, an owner, an **expiry date**,
   and **the cost of being wrong** stated concretely.
3. **Artifacts are marked Provisional.** Any ADR or specification resting on an
   open assumption carries status `Provisional` and names the assumption.
4. **Expiry is enforced by the build.** `scripts/project_lint.py` fails on an
   expired assumption. Renewal requires a new expiry and a stated reason; it is a
   deliberate act, not a default.
5. **Promotion requires evidence.** An assumption becomes fact only when a tier A
   or B citation replaces it. Time and repetition do not promote it.

Stating the cost of being wrong is the load-bearing part. It converts "we assumed
X" into a quantified risk the Product Owner can price, and it makes obviously
cheap assumptions cheap to accept and expensive ones visibly expensive.

## Consequences

**Easier:** the project moves while questions are open; the boundary between
evidence and inference stays visible; the cost of a missing document is quantified
rather than argued; assumptions cannot rot silently.

**Harder:** a failing build on an expiry date will arrive at an inconvenient
moment — that is the mechanism working, and overriding it repeatedly is the
failure mode to watch for. Writing an honest cost-of-being-wrong takes real
thought, and a lazy one ("some rework") makes the whole register worthless.

**Cost:** assumption maintenance, and periodic build failures that demand a
decision rather than a dismissal.

## Alternatives considered

- **Block all work until documentation exists** — rejected: the project would do
  nothing for an unbounded period, and scope, environment, and current-state work
  genuinely does not need Oracle sources.
- **Assumption register without expiry** — rejected: unreviewed assumptions
  silently become facts. Expiry is the only mechanism that has been observed to
  prevent it.
- **Warn instead of fail on expiry** — rejected: warnings are read once and then
  filtered out. An expired assumption is a decision resting on nothing, and the
  build should say so.
- **Track assumptions in a risk register instead** — rejected: risks are about
  probability and impact; assumptions are about evidence. Conflating them loses
  the traceability from assumption to the artifact built on it. They stay
  separate, and `risks.md` cross-references assumptions.

## Sources
N/A — internal process decision. No Oracle source applies.
