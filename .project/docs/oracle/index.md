# Oracle HCM module knowledge index

**Evidence baseline:** 2026-10-22  
**Reusable expert skill:** [Oracle HCM Expert](../../../.agents/skills/oracle-hcm-expert/SKILL.md)  
**Retrieval engine:** [oracle_hcm_knowledge.py](../../../scripts/oracle_hcm_knowledge.py)  
**Authoritative source registry:** [source-registry.md](../source-registry.md)

The knowledge system combines concise authored domain maps with full-text retrieval from official Oracle guides. The public repository contains links, bibliographic metadata, source-age caveats, and original summaries. Oracle manuals, extracted full text, and SQLite indexes are fetched and stored locally under `.cache/oracle-hcm/<module>/`; they are not committed.

## Populated modules

| Code | Domain | Landing page | Domain map | Source manifest |
|---|---|---|---|---|
| ORC | Recruiting | [README](ORC/README.md) | [Map](ORC/domain-map.md) | [Manifest](ORC/source-manifest.json) |
| GHR | Global Human Resources | [README](GHR/README.md) | [Map](GHR/domain-map.md) | [Manifest](GHR/source-manifest.json) |
| ABS | Absence Management | [README](ABS/README.md) | [Map](ABS/domain-map.md) | [Manifest](ABS/source-manifest.json) |
| BEN | Benefits | [README](BEN/README.md) | [Map](BEN/domain-map.md) | [Manifest](BEN/source-manifest.json) |
| TIM | Time and Labor | [README](TIM/README.md) | [Map](TIM/domain-map.md) | [Manifest](TIM/source-manifest.json) |
| LRN | Learning | [README](LRN/README.md) | [Map](LRN/domain-map.md) | [Manifest](LRN/source-manifest.json) |

## Build local retrieval

Install the PDF extraction dependency once:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements-knowledge.txt
```

Then build each module's own local index (example: Recruiting):

```bash
python scripts/oracle_hcm_knowledge.py refresh --manifest .project/docs/oracle/ORC/source-manifest.json
python scripts/oracle_hcm_knowledge.py ingest --manifest .project/docs/oracle/ORC/source-manifest.json
python scripts/oracle_hcm_knowledge.py search "candidate selection process" --manifest .project/docs/oracle/ORC/source-manifest.json
```

Use the relevant module manifest path for GHR, ABS, BEN, TIM, or LRN. Do not search one module's index for another module's implementation steps.

## Scheduled source maintenance

GitHub Actions runs the metadata/fingerprint refresh weekly and on relevant pushes. It uses the official Oracle HCM readiness catalog to discover the most recent release page for each registered module and opens a review PR when source metadata or content fingerprints change. It does not download/publish the full manuals as workflow artifacts or commit extracted content.

## Not yet populated

Payroll, Compensation, Performance Management, Goal Management, Talent Review/Succession, Journeys, Help Desk, Workforce Health & Safety, HCM Common, Security, Integrations, Data Conversion, OTBI/BI Publisher, and extensions remain to be inventoried from Oracle's actual documentation catalogs. They are not marked as source-covered until their live source URLs and guide identities are verified.
