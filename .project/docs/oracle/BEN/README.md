# Oracle Benefits — module knowledge base

**Module code:** BEN  
**Source baseline checked:** 2026-10-22  
**Release reference:** Oracle Benefits 26D What's New/readiness page  
**Reusable skill:** [Oracle HCM Expert](../../../../.agents/skills/oracle-hcm-expert/SKILL.md)

This module has a real source manifest and locally searchable source pipeline. The condensed domain map is navigation and retrieval guidance; exact procedural answers must be based on freshly retrieved passages, exact chapter/page citations, the target quarterly release, and tenant-specific setup.

## Verified official sources

| Source | Document ID | PDF pages | Links |
|---|---|---:|---|
| Implementing Benefits | G34710-01 | 468 | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/faibf/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/faibf/implementing-benefits.pdf) |
| Using Benefits | G34737-01 | 150 | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/facmb/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/facmb/using-benefits.pdf) |
| Human Resources 26D What's New / readiness | — | HTML | [Current release page](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/benf-26d/26D-benefits-wn-f51263.htm) |
| Oracle Human Resources - All Books | — | HTML | [Oracle catalog](https://docs.oracle.com/en/cloud/saas/human-resources/books.html) |

## Retrieval instructions

The canonical source list is [source-manifest.json](source-manifest.json). Run from the repository root after installing [requirements-knowledge.txt](../../../../requirements-knowledge.txt):

```bash
python scripts/oracle_hcm_knowledge.py status --manifest .project/docs/oracle/BEN/source-manifest.json
python scripts/oracle_hcm_knowledge.py refresh --manifest .project/docs/oracle/BEN/source-manifest.json
python scripts/oracle_hcm_knowledge.py ingest --manifest .project/docs/oracle/BEN/source-manifest.json
python scripts/oracle_hcm_knowledge.py search "specific topic or exact Oracle label" --manifest .project/docs/oracle/BEN/source-manifest.json
```

PDFs, extracted text and the SQLite FTS index remain in the local, Git-ignored `.cache/oracle-hcm/ben/` directory. The public repository stores metadata and authored notes only.

## Caveats

Eligibility, plan coverage, effective dates, legislation and relationship configuration drive the outcome. The guide is not a substitute for confirming a specific plan's actual configuration or applicable country rules.

A standalone book titled “Administering Benefits” is not assumed. The actual listed Using guide includes operational tasks; setup guidance uses the Implementing guide. Consult the source catalog for any separate administration/security guide relevant to the precise question.
