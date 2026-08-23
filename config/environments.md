# Environment & Instance Registry

**Status: not yet populated.** Owned by `HCM-012`; blocked on `GAP-004`.

Every Oracle HCM instance the project touches is recorded here before it is used.
An unregistered instance is an instance nobody is accountable for.

| Instance | Purpose | Release | Refreshed from | Cadence | Data classification | Masking required | Change owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| _(none registered)_ | | | | | | | |

## Column contract

| Column | Rule |
| --- | --- |
| Instance | The environment's project name (DEV, TEST, UAT, PROD, CONV, TRAIN…) |
| Purpose | What it is for, and what it must **not** be used for |
| Release | Current Oracle release, updated at each quarterly update |
| Refreshed from | Source instance for refreshes |
| Cadence | How often, and what triggers an out-of-cycle refresh |
| Data classification | `Synthetic` / `Masked production` / `Production` |
| Masking required | Yes/No and which masking routine applies |
| Change owner | Who may approve a configuration change here |

Any instance classified `Production` or `Masked production` carries personal data
and is subject to the constraints established by `HCM-034`. No data from such an
instance may be committed to this repository under any circumstances
(`ADR-0003`, `RISK-005`).
