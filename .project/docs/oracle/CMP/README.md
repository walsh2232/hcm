# Oracle Compensation — module knowledge base

**Module code:** CMP  
**Evidence baseline:** 2026-10-22  
**Reusable skill:** [Oracle HCM Expert](../../../../.agents/skills/oracle-hcm-expert/SKILL.md)

This folder contains the source manifest, module domain map and operational instructions for a source-grounded retrieval workflow. The manifest records official Oracle guide identities and URL provenance. Full PDF/HTML text and SQLite search indexes are fetched into Git-ignored local cache; they are not copied into this public repository.

## Official guides and readiness sources

| Guide/source | Document ID | Pages | Official source |
|---|---|---:|---|
| Implementing Compensation | G34711-06 | 446 | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/faiwc/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/faiwc/implementing-compensation.pdf) |
| Using Compensation | G34739-01 | 68 | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/facmc/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/facmc/using-compensation.pdf) |
| Release readiness context | — | HTML | [Oracle HCM readiness catalog — Compensation What's New 26D](https://docs.oracle.com/en/cloud/saas/readiness/hcm.html) |
| Oracle guide/readiness catalog | — | HTML | [Official Oracle catalog](https://docs.oracle.com/en/cloud/saas/human-resources/books.html) |

See [source-manifest.json](source-manifest.json) for all source URLs, their roles, release metadata and freshness policy. See [domain-map.md](domain-map.md) for topic routing and domain-specific caveats.

## Build and query this module's local index

From the repository root, after `python -m pip install -r requirements-knowledge.txt`:

```bash
python scripts/oracle_hcm_knowledge.py status --manifest .project/docs/oracle/CMP/source-manifest.json
python scripts/oracle_hcm_knowledge.py refresh --manifest .project/docs/oracle/CMP/source-manifest.json
python scripts/oracle_hcm_knowledge.py ingest --manifest .project/docs/oracle/CMP/source-manifest.json
python scripts/oracle_hcm_knowledge.py search "exact product term or task name" --manifest .project/docs/oracle/CMP/source-manifest.json
```

## Important qualification

Pay-impacting actions require precise setup and effective-dated validation. Confirm legal employer, grade, salary basis, plan cycle, eligibility, worker population, approvals and downstream payroll behaviour; do not infer a tenant's configuration from general guide instructions.

An Oracle Help Center page being public does not prove that a feature is licensed, enabled, configured, or supported in a particular customer's environment. Verify the tenant release and exact source passage before prescribing configuration changes.
