# Oracle Absence Management — module knowledge base

**Module code:** ABS  
**Source baseline checked:** 2026-10-22  
**Release reference:** Oracle Absence Management 26D What's New/readiness page  
**Reusable skill:** [Oracle HCM Expert](../../../../.agents/skills/oracle-hcm-expert/SKILL.md)

This module has a real source manifest and locally searchable source pipeline. The condensed domain map is navigation and retrieval guidance; exact procedural answers must be based on freshly retrieved passages, exact chapter/page citations, the target quarterly release, and tenant-specific setup.

## Verified official sources

| Source | Document ID | PDF pages | Links |
|---|---|---:|---|
| Implementing Absence Management | G34709-01 | 192 | [HTML]( https://docs.oracle.com/en/cloud/saas/human-resources/faiam/implementing-absence-management/index.html ) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/faiam/implementing-absence-management.pdf) |
| Using Absence Management | G34736-01 | 40 | [HTML]( https://docs.oracle.com/en/cloud/saas/human-resources/fauam/using-absence-management/index.html ) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/fauam/using-absence-management.pdf) |
| Human Resources 26D What's New / readiness | — | HTML | [Current release page](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/amg-26d/26D-absence-mgmt-wn-t78665.htm) |
| Oracle Human Resources - All Books | — | HTML | [Oracle catalog](https://docs.oracle.com/en/cloud/saas/human-resources/books.html) |

## Retrieval instructions

The canonical source list is [source-manifest.json](source-manifest.json). Run from the repository root after installing [requirements-knowledge.txt](../../../../requirements-knowledge.txt):

```bash
python scripts/oracle_hcm_knowledge.py status --manifest .project/docs/oracle/ABS/source-manifest.json
python scripts/oracle_hcm_knowledge.py refresh --manifest .project/docs/oracle/ABS/source-manifest.json
python scripts/oracle_hcm_knowledge.py ingest --manifest .project/docs/oracle/ABS/source-manifest.json
python scripts/oracle_hcm_knowledge.py search "specific topic or exact Oracle label" --manifest .project/docs/oracle/ABS/source-manifest.json
```

PDFs, extracted text and the SQLite FTS index remain in the local, Git-ignored `.cache/oracle-hcm/abs/` directory. The public repository stores metadata and authored notes only.

## Caveats

The two core manuals currently show 2024 copyright dates. Treat them as implementation/operating references, not proof that a procedure is unchanged in 26D. Validate release-dependent behaviour against the current readiness pages.

A standalone book titled “Administering Absence Management” is not assumed. The actual listed Using guide includes operational tasks; setup guidance uses the Implementing guide. Consult the source catalog for any separate administration/security guide relevant to the precise question.
