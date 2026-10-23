# Recruiting source issues and verification log

This file records source-level ambiguity that could affect implementation. It is not a substitute for the source registry or the gap/assumption process.

## SI-001 — Oracle Search index-name strings differ by context

**Status:** Open — tracked as GAP-008. Do not run the affected reingest by guessing.

**Source:** DOC-001, *Implementing Recruiting*, G34431-12.

| Context | Exact string shown in the guide | Location |
|---|---|---|
| Chapter 1, Oracle Search maintenance after P2T/T2T when advanced job-application filters are in use | **fa-hcm-job application** (with a space) | Physical PDF p. 31 / printed p. 13 |
| Chapter 13, Configure Attachment Search and reingest the attachment-search index | **fa-hcm-jobapplication** (without a space) | Physical PDF p. 245 / printed p. 227 |

Both strings were visually checked against the rendered supplied PDF. This is not merely a text-extraction spelling difference.

**Interpretation not established:** the contexts may require distinct index names, or one passage may contain a source typo. The available evidence does not justify replacing or merging the two strings.

**Safe handling:** preserve each string and its context. Before execution, inspect the relevant index name in the target tenant, check the current Oracle guide for the deployed quarterly release, and raise an Oracle Support question if ambiguity remains. Never guess a value or silently “correct” the source.

**Affected topic:** Oracle Search after P2T/T2T and advanced job-application attachment filters. See [Oracle Search indexing playbook](playbooks/oracle-search-indexing-and-p2t.md).

## SI-002 — Guide edition is not tenant-release validation

G34431-12 is the guide/document identifier. It does not establish the quarterly HCM release deployed in a specific tenant. The source registry's Validated field must remain blank until the target release is named and the source is checked against it.
