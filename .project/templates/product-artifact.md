---
id: TEMPLATE-PRODUCT-001
title: Standard product artifact template
artifact_type: template
status: PROPOSED
version: 1.0.0
owner_role: DOC
reviewer_role: BA
---

# Standard Product Artifact Template

Every canonical product artifact begins with YAML front matter and uses the sections relevant to its artifact type.

Required metadata:
- id: stable and never reused
- title: plain-language artifact title
- artifact_type: prd, srs, architecture-design-specification, data-contract-specification, test-strategy, runbook, delivery-plan, status-register, decision-record, or glossary
- status: PROPOSED, IMPLEMENTED-UNVERIFIED, LOCALLY-VERIFIED, CI-VERIFIED, ACCEPTED, BLOCKED, DEFERRED, or SUPERSEDED
- version: semantic-style document version, independent of product release
- owner_role: exactly one accountable owner role
- reviewer_roles: required review roles
- last_reviewed: ISO date
- related_work_item: HCM-### when work is tracked on the project board
- source_refs: precise repository paths, source IDs/locations, or external URLs where applicable

Required content sections, adapted by artifact type:
1. Purpose and intended audience.
2. State: what is proposed, implemented, verified, accepted, or unresolved.
3. Requirements/decisions/contracts with stable identifiers.
4. Dependencies and assumptions.
5. Verification or validation method.
6. Open questions with named role owner and next action.
7. References to canonical artifacts and source locations.

Rules:
- Never state “done” without naming the required evidence.
- Never cite an Oracle guide without an edition and exact page/section/URL.
- Never treat a model-generated statement as an Oracle source.
- Never hide contradictions or promote an assumption to fact.
- When an artifact changes materially, update the version and change history as needed.
- When superseded, keep a link to the successor and retain relevant history.
- Use Markdown tables for structured contracts and stable requirement IDs for test mapping.
- Keep one source of truth for each decision; link to it rather than duplicating conflicting copies.
