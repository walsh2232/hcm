# Oracle Workforce Health and Safety — module knowledge base

**Module code:** HSE  
**Evidence baseline:** 2026-10-22  
**Reusable skill:** [Oracle HCM Expert](../../../../.agents/skills/oracle-hcm-expert/SKILL.md)

This folder contains the source manifest, module domain map and operational instructions for a source-grounded retrieval workflow. The manifest records official Oracle guide identities and URL provenance. Full PDF/HTML text and SQLite search indexes are fetched into Git-ignored local cache; they are not copied into this public repository.

## Official guides and readiness sources

| Guide/source | Document ID | Pages | Official source |
|---|---|---:|---|
| Using Workforce Health and Safety | G34746-03 | 36 | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/fawhs/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/fawhs/using-workforce-health-and-safety.pdf) |
| Release readiness context | — | HTML | [Workforce Health and Safety 26B Feature Summary](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26b/wohs-26b/26B-workforce-health-wn-t73860.htm) |
| Oracle guide/readiness catalog | — | HTML | [Official Oracle catalog](https://docs.oracle.com/en/cloud/saas/human-resources/books.html) |

See [source-manifest.json](source-manifest.json) for all source URLs, their roles, release metadata and freshness policy. See [domain-map.md](domain-map.md) for topic routing and domain-specific caveats.

## Build and query this module's local index

From the repository root, after `python -m pip install -r requirements-knowledge.txt`:

```bash
python scripts/oracle_hcm_knowledge.py status --manifest .project/docs/oracle/HSE/source-manifest.json
python scripts/oracle_hcm_knowledge.py refresh --manifest .project/docs/oracle/HSE/source-manifest.json
python scripts/oracle_hcm_knowledge.py ingest --manifest .project/docs/oracle/HSE/source-manifest.json
python scripts/oracle_hcm_knowledge.py search "exact product term or task name" --manifest .project/docs/oracle/HSE/source-manifest.json
```

## Important qualification

Oracle's Books catalog lists Using Workforce Health and Safety, but no separate Implementing guide. Its guide copyright is 2023 and the latest product feature summary currently registered is 26B. Treat feature/release guidance as stale-risk until a newer official source is found; escalate undocumented tenant behaviour rather than inventing fixes.

An Oracle Help Center page being public does not prove that a feature is licensed, enabled, configured, or supported in a particular customer's environment. Verify the tenant release and exact source passage before prescribing configuration changes.
