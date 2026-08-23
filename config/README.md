# Configuration

Non-secret configuration that describes the delivery landscape.

| File | Purpose | Owner |
| --- | --- | --- |
| [`environments.md`](environments.md) | Instance registry — purpose, release, refresh, data classification | Solution Architect |

## Hard rules

**No secrets in this directory, or anywhere in this repository.** No passwords, no
API keys, no wallets, no certificates, no connection strings containing
credentials. `.gitignore` blocks the common patterns, but the rule is the control
and the ignore file is only a backstop. Secrets belong in the organisation's
secret manager; this directory records that a credential exists and where it is
held, never its value.

Endpoint hostnames are recorded only where they are not themselves sensitive. When
in doubt, record the environment name and hold the endpoint elsewhere.
