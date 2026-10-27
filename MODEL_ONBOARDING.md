---
id: MODEL-ONBOARDING-001
title: First-session onboarding and continuity protocol
artifact_type: operating-standard
status: PROPOSED
version: 1.0.0
owner_role: BA
reviewer_role: PO
last_reviewed: 2026-10-27
canonical: true
---

# Model Onboarding and Continuity Protocol

## Purpose

This file lets a new ChatGPT session, coding agent, or human contributor resume work without relying on hidden chat history. Repository state and approved artifacts outrank recollection, summaries, and assumptions.

## Required first-read order

1. Read this file completely.
2. Read [.project/product/README.md](.project/product/README.md) for the document map and status vocabulary.
3. Read [.project/product/STATUS-001-as-built-vs-proposed.md](.project/product/STATUS-001-as-built-vs-proposed.md) before claiming that anything exists or works.
4. Read [.project/product/PRD-001-reference-library.md](.project/product/PRD-001-reference-library.md).
5. Read [.project/product/SRS-001-pipeline.md](.project/product/SRS-001-pipeline.md) and [.project/product/ARCH-001-architecture.md](.project/product/ARCH-001-architecture.md).
6. Read [.project/product/DATA-001-contracts.md](.project/product/DATA-001-contracts.md), [.project/product/TEST-001-validation.md](.project/product/TEST-001-validation.md), and [.project/product/OPS-001-runbook.md](.project/product/OPS-001-runbook.md).
7. Read [.project/product/PLAN-001-delivery-raci.md](.project/product/PLAN-001-delivery-raci.md).
8. Read the existing governance: [.project/decision-framework.md](.project/decision-framework.md), [.project/docs/README.md](.project/docs/README.md), [.project/docs/source-registry.md](.project/docs/source-registry.md), [.project/docs/gaps.md](.project/docs/gaps.md), [.project/roles.md](.project/roles.md), [.project/workflow.md](.project/workflow.md), [.project/backlog.md](.project/backlog.md), and [.project/kanban.md](.project/kanban.md).
9. Before changing code, inspect the current branch, open PRs, latest commit, workflow files, and exact implementation/test files referenced in STATUS-001. Paths and status recorded here are navigation aids, not proof that the current branch is unchanged.

## Canonical source and decision rules

- Official Oracle product documentation registered in the source registry is the primary source for Oracle-product behavior. Apply the project's source tiers and release-binding rules in decision-framework.md.
- Repository code proves what is implemented; passing tests on the exact commit prove only the behavior those tests exercise.
- A PR description, previous assistant message, old run, or summary is not proof that the current commit passes.
- When evidence is insufficient, say so, record a GAP/ASM where the project framework requires it, and do not fill the hole with plausible-sounding Oracle terminology.
- Never treat a guide edition identifier as proof of the target tenant's quarterly release.
- Never report an action as completed unless the tool or repository confirms it.

## Required status labels

Use exactly one primary status for each requirement, component, and delivery item:

| Status | Meaning | Evidence required |
|---|---|---|
| PROPOSED | Specified but not built | Approved or draft specification |
| IMPLEMENTED-UNVERIFIED | Code/artifact exists; current behavior has not been adequately exercised | Repository path and commit |
| LOCALLY-VERIFIED | Relevant tests/checks passed locally on a named commit | Commands, results, commit |
| CI-VERIFIED | Required CI passed on the exact commit under review | Linked workflow run and commit SHA |
| ACCEPTED | The accountable human role accepted the deliverable against criteria | Recorded acceptance/review |
| BLOCKED | Cannot progress without a named dependency/decision | Owner, blocker, next action |
| DEFERRED | Explicitly outside the current delivery slice | Rationale and revisit trigger |
| SUPERSEDED | Replaced by a newer artifact/implementation | Successor reference |

Do not collapse “exists”, “test passed”, “CI passed”, and “accepted” into a single “done” label.

## Turn-by-turn continuity protocol

A substantive turn means a user request that changes scope, a design decision, implementation, test result, or a meaningful finding. Small clarifications that do not affect artifacts do not count.

1. At the start of a new ChatGPT session, follow the first-read order and inspect current GitHub state.
2. After every two substantive user/assistant work cycles, compare the last two cycles with this document set.
3. Also perform that comparison before a consequential architecture decision, repository write, PR creation, status claim, milestone close, or scope change.
4. Produce a brief checkpoint in the working response: (a) decisions confirmed, (b) artifact paths updated or needing updates, (c) proposed vs built vs verified state, (d) contradictions/gaps, (e) next owner/action.
5. If the user made a decision, update the canonical artifact and decision log in the same work batch or explicitly record why it remains pending. If it was brainstorming only, label it PROPOSED; do not silently promote it.
6. Review the most recent two substantive turns against the PRD, SRS, architecture, status register, backlog, and relevant code/tests. If conversation and files disagree, stop and reconcile before continuing.
7. At the end of a task, update STATUS-001 and the delivery plan if implementation or validation state changed. Report the exact commit/PR and what was or was not tested.

## Working agreement and division of responsibility

- Product Owner (user): owns product scope, priority, business trade-offs, publication intent/authorization, and acceptance.
- ChatGPT/model acting as delivery assistant: drafts artifacts, inspects evidence, implements the requested changes through available tools, runs or requests checks where possible, maintains traceability, and calls out uncertainty. The model cannot independently accept its own work or declare an unexecuted test passed.
- Business Analyst: owns atomic requirement wording, traceability, and acceptance-criteria quality.
- Solution Architect: owns architecture/pattern proposals and risks; a human reviewer is required for material or irreversible design decisions.
- Developer: owns implementation quality and repairs.
- QA: independently judges test sufficiency, pass/fail, and defect severity.
- Documentation Specialist: owns source registry completeness, edition/currency metadata, and the documentation lifecycle.
- When one model performs multiple roles, keep the role labels and independent-review gate; do not pretend that one model is independent from itself.

## Repository status at inception of this package

The checked project is [walsh2232/hcm](https://github.com/walsh2232/hcm). Product-documentation work is tracked as HCM-036. The proposed design keeps this repository as the initial processing workbench, while published, coworker-facing Markdown lives in a separate public repository provisionally named `oracle-product-reference-library`. That output repository has not been created in this work.

The repository boundary and product taxonomy are documented as proposals in `.project/product/PRD-001-reference-library.md`, `ARCH-001-architecture.md`, and `PLAN-001-delivery-raci.md`. The output taxonomy starts at `products/hcm/` and is designed to add `products/oci/` and `products/bi-publisher/` without renaming the repository. The existing scripts remain in `walsh2232/hcm` for the first MVP slice; a separate generic pipeline repo is a later option, not an approved requirement.

Existing implementations are listed in STATUS-001. In particular:
- PDF intake, HTML fallback, normalizer, and SQLite FTS5 search scripts already exist under scripts/oracle_docs/.
- The project lint workflow currently has workflow_dispatch only; the weekly schedule is not implemented.
- The current HTML ingester appears to reference an undefined name in link parsing. Treat the relevant test as suspect until rerun against the exact current commit.
- “DEE” came from this raw speech-to-text excerpt: “...include things like requirements documents things like DEE make sure your reference like what tools you want to use...” The surrounding words do not establish whether DEE was intended or was transcription noise. Do not invent an expansion; see PLAN-001.

## Definition of a reliable handoff

A fresh model must be able to answer, using repository evidence: What is the product? What is approved vs proposed? What exists today? Where is it? What passed on which commit? What is blocked? Who owns the decision/action? What should happen next? If any answer relies only on chat memory, the handoff is incomplete.
