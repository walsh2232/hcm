# Oracle HCM module knowledge index

**Evidence baseline:** 2026-10-22  
**Reusable expert skill:** [Oracle HCM Expert](../../../.agents/skills/oracle-hcm-expert/SKILL.md)  
**Retrieval engine:** [oracle_hcm_knowledge.py](../../../scripts/oracle_hcm_knowledge.py)  
**Authoritative source registry:** [source-registry.md](../source-registry.md)

The knowledge system combines concise authored domain maps with full-text retrieval from official Oracle guides. The public repository contains links, bibliographic metadata, source-age caveats, and original summaries. Oracle manuals, extracted full text, and SQLite indexes are fetched and stored locally under `.cache/oracle-hcm/<module>/`; they are not committed.

## Populated modules

| Code | Domain | Landing page | Domain map | Source manifest |
|---|---|---|---|---|
| ABS | Absence Management | [README](ABS/README.md) | [Map](ABS/domain-map.md) | [Manifest](ABS/source-manifest.json) |
| BEN | Benefits | [README](BEN/README.md) | [Map](BEN/domain-map.md) | [Manifest](BEN/source-manifest.json) |
| CMP | Compensation | [README](CMP/README.md) | [Map](CMP/domain-map.md) | [Manifest](CMP/source-manifest.json) |
| GHR | Global Human Resources | [README](GHR/README.md) | [Map](GHR/domain-map.md) | [Manifest](GHR/source-manifest.json) |
| HDS | Help Desk | [README](HDS/README.md) | [Map](HDS/domain-map.md) | [Manifest](HDS/source-manifest.json) |
| HSE | Workforce Health and Safety | [README](HSE/README.md) | [Map](HSE/domain-map.md) | [Manifest](HSE/source-manifest.json) |
| JRN | Journeys | [README](JRN/README.md) | [Map](JRN/domain-map.md) | [Manifest](JRN/source-manifest.json) |
| LRN | Learning | [README](LRN/README.md) | [Map](LRN/domain-map.md) | [Manifest](LRN/source-manifest.json) |
| ORC | Recruiting | [README](ORC/README.md) | [Map](ORC/domain-map.md) | [Manifest](ORC/source-manifest.json) |
| PAY | Global Payroll | [README](PAY/README.md) | [Map](PAY/domain-map.md) | [Manifest](PAY/source-manifest.json) |
| RPT | HCM Analytics and Reporting | [README](RPT/README.md) | [Map](RPT/domain-map.md) | [Manifest](RPT/source-manifest.json) |
| TAL | Talent Management | [README](TAL/README.md) | [Map](TAL/domain-map.md) | [Manifest](TAL/source-manifest.json) |
| TIM | Time and Labor | [README](TIM/README.md) | [Map](TIM/domain-map.md) | [Manifest](TIM/source-manifest.json) |

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

Use the relevant manifest path for any of the thirteen populated modules. The script builds an isolated cache/index for each module. Do not search one module's index for another module's implementation steps.

## Scheduled source maintenance

GitHub Actions runs the metadata/fingerprint refresh weekly and on relevant pushes. It uses the official Oracle HCM readiness catalog to discover the most recent release page for each registered module and opens a review PR when source metadata or content fingerprints change. It does not download/publish the full manuals as workflow artifacts or commit extracted content.

## Not yet populated

HCM Common, Security, Integrations, Data Conversion, additional country-specific payroll localization, and extensions remain to be inventoried from Oracle's actual documentation catalogs. They are not marked as source-covered until their live source URLs and guide identities are verified.
