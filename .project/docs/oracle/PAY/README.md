# Oracle Global Payroll — module knowledge base

**Module code:** PAY  
**Evidence baseline:** 2026-10-22  
**Reusable skill:** [Oracle HCM Expert](../../../../.agents/skills/oracle-hcm-expert/SKILL.md)

This folder contains the source manifest, module domain map and operational instructions for a source-grounded retrieval workflow. The manifest records official Oracle guide identities and URL provenance. Full PDF/HTML text and SQLite search indexes are fetched into Git-ignored local cache; they are not copied into this public repository.

## Official guides and readiness sources

| Guide/source | Document ID | Pages | Official source |
|---|---|---:|---|
| Implementing Global Payroll | G34713-09 | 484 | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/faigp/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/faigp/implementing-global-payroll.pdf) |
| Using Global Payroll for Employees | G34741-02 | 26 | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/oapay/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/oapay/using-global-payroll-for-employees.pdf) |
| Implementing Payroll for Canada (jurisdiction-specific) | G34716-03 | Not recorded | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/fapcd/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/fapcd/implementing-payroll-for-canada.pdf) |
| Release readiness context | — | HTML | [Payroll 26D Feature Summary](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/payr-26d/26D-payroll-wn-t78658.htm) |
| Oracle guide/readiness catalog | — | HTML | [Official Oracle catalog](https://docs.oracle.com/en/cloud/saas/human-resources/books.html) |

See [source-manifest.json](source-manifest.json) for all source URLs, their roles, release metadata and freshness policy. See [domain-map.md](domain-map.md) for topic routing and domain-specific caveats.

## Build and query this module's local index

From the repository root, after `python -m pip install -r requirements-knowledge.txt`:

```bash
python scripts/oracle_hcm_knowledge.py status --manifest .project/docs/oracle/PAY/source-manifest.json
python scripts/oracle_hcm_knowledge.py refresh --manifest .project/docs/oracle/PAY/source-manifest.json
python scripts/oracle_hcm_knowledge.py ingest --manifest .project/docs/oracle/PAY/source-manifest.json
python scripts/oracle_hcm_knowledge.py search "exact product term or task name" --manifest .project/docs/oracle/PAY/source-manifest.json
```

## Important qualification

Payroll is jurisdiction-specific and consequential. The Canadian guide is separately identified; never use its rules as global defaults. Confirm legislation and legislative data, LDG, payroll statutory units, tax/reporting units, effective dates, pay frequencies, processing definitions and the target environment's quarterly release.

An Oracle Help Center page being public does not prove that a feature is licensed, enabled, configured, or supported in a particular customer's environment. Verify the tenant release and exact source passage before prescribing configuration changes.
