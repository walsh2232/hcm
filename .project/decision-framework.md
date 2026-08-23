# Decision-Making & Source Validation Framework

Oracle official documentation is the primary source of truth for this project.
This document defines what "official" means, how a decision is validated against
it, and what happens when it is silent.

## 1. Source tiers

Every source is registered in [`docs/source-registry.md`](docs/source-registry.md)
with a tier. Tier determines what the source may be used for.

| Tier | What it is | May be used to… | May **not** be used to… |
| --- | --- | --- | --- |
| **A — Authoritative** | Oracle documentation supplied by the Product Owner for this project, and Oracle product documentation on `docs.oracle.com` for the deployed release | Justify any decision; close a gap | — |
| **B — Oracle support** | My Oracle Support notes, Oracle-published release readiness material, "What's New" for the deployed release | Justify a decision; close a gap, when consistent with Tier A | Override Tier A |
| **C — Oracle advisory** | Oracle Cloud Customer Connect posts, Oracle product-management blogs, Oracle-run webinars | Form a hypothesis; frame a question to Oracle | Justify a decision or close a gap |
| **D — Community** | Third-party blogs, forums, consultancy material, model knowledge, other implementations | Form a hypothesis only | Justify a decision, close a gap, or appear as a citation |

**Precedence is absolute: A > B > C > D.** A lower tier never contradicts a higher
one. Where a Tier C or D source appears to contradict Tier A, the contradiction is
logged as a `GAP` and the Tier A reading stands until Oracle says otherwise.

External research supplements Oracle sources; it never substitutes for them.

## 2. Release binding

Oracle Fusion Cloud HCM changes quarterly. A source without a release is not a
source. Every registry entry records the release it describes (e.g. `25B`) and the
release(s) it has been validated against. When the environment moves to a new
release:

1. The Documentation Specialist opens a **source currency sweep** card.
2. Every Tier A/B entry is re-checked against the new release's *What's New*.
3. Entries that changed are superseded; ADRs citing them are re-opened as
   **Under review** until re-validated.
4. Entries that could not be re-checked are marked `STALE` and produce a lint
   warning after one full quarter.

## 3. The validation test

Before any design, configuration, or extension decision is recorded, it must pass:

1. **Cited** — a specific registered source and location (`DOC-000 §4.3`, not `DOC-000`).
2. **Current** — the source is validated against the target release.
3. **Consistent** — it does not contradict a higher-tier source or an accepted ADR.
4. **Sufficient** — the source actually answers the question asked, rather than a
   neighbouring one. State plainly when it does not.
5. **Reversible or agreed** — if the decision is hard to reverse (data model,
   security model, integration contract, payroll setup), it requires an ADR and
   Solution Architect accountability, not just a card.

Failing any of 1–4 means the decision is **Provisional** (§5), not that it is
blocked. Failing 5 means it does not proceed without an ADR.

## 4. Gaps

A gap is any question the registered sources cannot answer. Gaps are first-class
work, tracked in [`docs/gaps.md`](docs/gaps.md), and are raised — not worked
around.

| Gap type | Meaning | Default resolution |
| --- | --- | --- |
| `MISSING` | Oracle documents this, we do not hold the document | Request the document from the Product Owner |
| `SILENT` | Oracle documentation does not cover this behaviour | Raise an Oracle SR / Customer Connect question |
| `AMBIGUOUS` | Sources conflict or admit two readings | Escalate to SA + PO; record the chosen reading in an ADR |
| `SCOPE` | A business decision, not a documentation question | Product Owner decides; recorded on the card |
| `STALE` | Source predates the deployed release | Source currency sweep |

Every gap carries: type, owner, the decision it blocks, the assumption being used
meanwhile, and a target date.

## 5. Provisional decisions and assumptions

Work does not stop while a gap is open. It proceeds under a logged assumption:

```
ASM-000  Absence accrual runs nightly, not on demand
  Basis:        Tier C — Customer Connect post, not confirmed in Tier A
  Blocks:       ADR-0000, REQ-ABS-000
  Owner:        Solution Architect
  Expires:      2026-09-30
  If wrong:     Integration schedule and SLA change; ~2d rework in INT
```

Rules:
- Every assumption has an owner, an expiry, and a stated cost of being wrong.
- Any artifact built on an assumption is marked **Provisional** and listed on the
  assumption.
- An expired assumption is a build failure, not a warning. It is renewed with a new
  expiry and a reason, or resolved.
- An assumption may never be promoted to fact without a Tier A or B citation.

## 6. Conflict with business requirements

Where an Oracle source establishes that the product cannot do what the business
asked for, that is not a defect to be argued with — it is a decision to be made.
The Business Analyst restates the underlying need, the Solution Architect presents
the options with the source cited, and the Product Owner chooses:

**(a)** change the process to fit the product · **(b)** configure an approximation
and accept the delta · **(c)** extend (with the maintenance cost stated) ·
**(d)** integrate to something else · **(e)** defer.

The choice is recorded as an ADR that states the rejected options and why. There
is no option (f) "assume it will work".

## 7. Anti-patterns

These are treated as defects in the process:

- Citing a whole document instead of a location within it.
- Presenting model knowledge or another implementation as an Oracle behaviour.
- Closing a gap because the work was completed rather than because it was answered.
- Renewing an assumption indefinitely without new evidence.
- Making an irreversible decision on a card instead of in an ADR.
- Recording a decision only in conversation.
