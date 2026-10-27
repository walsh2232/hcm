---
id: PRODUCT-DOC-INDEX-001
title: Oracle Product Reference Library product document index
artifact_type: document-index
status: PROPOSED
version: 1.0.0
owner_role: BA
reviewer_role: PO
last_reviewed: 2026-10-27
---

# Oracle Product Reference Library & Change Tracker

## Why this folder exists

This is the canonical requirements and engineering-design package for the proposed library that refreshes, normalizes, indexes, compares, and archives Oracle product documentation. HCM is the initial content family; the repository taxonomy is designed to extend to OCI and BI Publisher without renaming. It is intentionally readable by people and by a model starting with no chat history.

## Artifact index

| Artifact | Purpose | Current status | Primary owner | Review |
|---|---|---|---|---|
| [PRD-001](PRD-001-reference-library.md) | Product problem, users, scope, outcomes, MVP and success measures | PROPOSED | BA | PO |
| [SRS-001](SRS-001-pipeline.md) | Functional and non-functional requirements with stable IDs | PROPOSED | BA | PO + QA |
| [ARCH-001](ARCH-001-architecture.md) | Component boundaries, tool choices, security and deployment pattern | PROPOSED | SA | SA/DEV |
| [DATA-001](DATA-001-contracts.md) | Source registry, edition manifest, lifecycle statuses and metadata contract | PROPOSED | DEV + DOC | SA/QA |
| [TEST-001](TEST-001-validation.md) | Test levels, cases, evidence requirements and acceptance gates | PROPOSED | QA | BA + DEV |
| [OPS-001](OPS-001-runbook.md) | Weekly operation, failures, retry, recovery and maintenance | PROPOSED | DOC + DEV | QA |
| [PLAN-001](PLAN-001-delivery-raci.md) | Phases, owners, RACI, dependencies, open decisions and definition of done | PROPOSED | BA | PO |
| [STATUS-001](STATUS-001-as-built-vs-proposed.md) | Evidence-led inventory of existing components vs proposed work | IMPLEMENTED-UNVERIFIED | BA + DEV | QA |
| [Model onboarding](../../MODEL_ONBOARDING.md) | First-read order, status vocabulary, turn checkpoints and continuity | PROPOSED | BA | PO |
| [Product artifact template](../templates/product-artifact.md) | Standard metadata and section contract for future product docs | PROPOSED | DOC | BA |

## Status rules

- The documents in this package specify a proposed product and delivery path. Their existence in GitHub does not mean the product pipeline is built.
- STATUS-001 is the only summary intended to describe existing implementation. It links to exact repository paths and marks current validation gaps explicitly.
- A “Built” claim must cite a path. A “Verified” claim must cite the tested commit and result. An “Accepted” claim requires an accountable human decision.
- Requirement IDs are stable. Do not renumber or reuse an ID; supersede it with a cross-reference.
- Product-specific decisions belong in reviewed artifacts and, when architectural/irreversible, in a formal ADR under .project/adr/. Do not rely on chat as the only record.

## Existing project sources used

- Existing intake process: [../docs/README.md](../docs/README.md).
- Source catalogue and field contract: [../docs/source-registry.md](../docs/source-registry.md).
- Source tiers and validation test: [../decision-framework.md](../decision-framework.md).
- Gap and assumption register: [../docs/gaps.md](../docs/gaps.md).
- Role decision rights and RACI: [../roles.md](../roles.md).
- Board and work item: [../kanban.md](../kanban.md) and [../backlog.md](../backlog.md), HCM-036.
- Repository recommendation: public published content in `oracle-product-reference-library`; processing scripts remain in `walsh2232/hcm` for the first MVP slice.
