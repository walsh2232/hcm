---
id: OPS-ORCH-001
title: Proposed weekly refresh operations and recovery runbook
artifact_type: operations-runbook
status: PROPOSED
version: 1.0.0
owner_role: DOC
reviewer_roles: [DEV, QA]
last_reviewed: 2026-10-27
related_work_item: HCM-036
---

# OPS-001 — Weekly Refresh Operations

## 1. Status and scope

This is the runbook for the proposed automated library. The weekly refresh is not currently active in the existing repository. Use this document to guide implementation and manual rehearsal; do not describe it as a live production procedure until the workflow is deployed and the first successful run is recorded.

## 2. Routine run

Expected workflow:
1. Start from the default branch's accepted catalogue and scripts.
2. Read the catalogue and validate schema and URL allowlists.
3. Check each active guide's canonical page/edition metadata.
4. Identify new/changed candidates; do not reprocess content whose stable hashes and relevant metadata are unchanged unless a forced run is requested.
5. Retrieve candidate source with bounded timeout/retry and enforce host, path, content type and size constraints.
6. Convert and create manifest plus diagnostics.
7. Validate source chain completeness, page/URL provenance, extracted text coverage, Markdown links, and test suite.
8. Compare prior accepted edition and create archive/change plan.
9. If unchanged, publish a no-change run report and finish without a content PR.
10. If candidate passes automated checks, create/update bot branch and PR; do not merge automatically.
11. Store the workflow run URL, candidate hashes, warnings, outcomes and PR URL in the report.
12. A human reviewer checks warnings, sample pages and archive operation and makes the merge/acceptance decision.

## 3. Trigger model

- Scheduled: once per week at a selected non-top-of-hour UTC minute after the workflow is merged to the default branch.
- Manual: workflow_dispatch for testing, recovery, or rerunning a failed guide after root cause is understood.
- Forced full re-ingest: explicit manual input or a reviewed tooling change; never silently force every guide weekly.
- Schedule availability must be monitored. GitHub notes that scheduled events run from the default branch, can be delayed under load, and can be disabled for a public repository after 60 days without activity. Use the official documentation linked in ARCH-001.

## 4. Failure classes and actions

| Failure | Required behavior | Operator action |
|---|---|---|
| DNS, timeout, 429 or 5xx | Bounded retry with backoff; then FAILED, current edition untouched | Inspect source availability and run logs; retry manually after issue is understood |
| 404 or source link changed | Mark STALE/FAILED; do not infer that the guide is retired | Verify official catalogue or Help Center replacement; update source registry through review |
| Redirect outside allowlist | Reject and record final URL | Investigate whether Oracle has moved the guide; update allowlist only by reviewed catalogue/config change |
| Unexpected content type | Reject as candidate | Verify whether Oracle changed PDF/HTML delivery |
| HTML Next-link loop | Abort and mark incomplete | Inspect URL chain and parser tests; do not publish |
| Max page cap reached | Mark INCOMPLETE unless known complete termination is independently established | Raise cap only after reviewing source scope and crawler safety |
| Empty/low-text pages | Mark NEEDS_VISUAL_REVIEW or INCOMPLETE according to policy | Compare with source PDF/HTML; do not claim OCR occurred |
| Parser/test failure | No current-edition change; PR blocked | Fix defect, add regression test, rerun exact test suite |
| Candidate diff is unusually large | Keep PR open, add explicit warning and manual review | Determine whether source edition changed, extraction regressed, or layout changed |
| Archive/index contract fails | Block candidate | Repair manifest/index and exercise lifecycle tests |
| No run in expected window | Alert status remains stale | Check Actions status, default-branch workflow, actor permissions, repository activity and scheduler state; dispatch manually if authorized |

## 5. Recovery and re-run

1. Identify run ID, source guide ID and failing stage from the report.
2. Capture the exact current branch and commit SHA.
3. Verify whether the failure is source availability, policy rejection, parser defect, validation gap, or GitHub permissions.
4. Keep last-known-good current content unchanged.
5. Reproduce using fixtures before retrying a live source if the failure involves parsing or lifecycle behavior.
6. Make the smallest repair on a reviewed branch and add a regression test.
7. Rerun offline tests and project lint on the proposed commit.
8. Use manual dispatch to test the workflow; confirm the candidate PR contains archive and diff changes.
9. Record disposition, evidence and owner in the run report and defect tracker.
10. Do not manually edit generated current content without also updating its manifest and source provenance.

## 6. GitHub and credential controls

- The workflow must use the minimum necessary GITHUB_TOKEN permissions.
- Read-only jobs should remain read-only. Only the publication job receives content write and pull-request write access.
- Never use a broad personal access token if the repo-scoped workflow token is sufficient.
- Never run untrusted contributor code in a workflow carrying write permissions.
- Do not log environment variables, token material, full authorization headers, or sensitive local paths.
- Use reviewed third-party action versions, preferably pinned to full commit SHAs.
- No production tenant credentials, tenant configuration extracts or PII are inputs to this pipeline.

## 7. Maintenance

- Review source catalogue completeness at least weekly and after Oracle quarterly documentation changes.
- Keep dependencies and GitHub Actions reviewed; record any added package in ARCH-001 and run regression tests.
- Verify workflow run history and default-branch status each month, and after any repository rename, transfer, permission change or token-policy change.
- Re-run a controlled archive/recovery fixture when lifecycle code changes.
- Update this runbook when actual operations diverge from the proposed flow; status must not remain PROPOSED after acceptance.

## 8. Operator report minimum

For every scheduled/manual attempt record: run ID, trigger, commit SHA, start/end time, number of guides checked, unchanged/candidate/failed/incomplete counts, candidate PRs, checks passed/failed, warnings, and the next human action. “Workflow completed” is not equivalent to “all guides successfully refreshed.”
