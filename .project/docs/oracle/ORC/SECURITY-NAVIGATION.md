# HCM security guides — Recruiting navigation

This is a targeted navigation map for Recruiting implementation. It does not replace the official security guides.

## Current source editions

| Source | Edition | Physical PDF pages | Official HTML | Official PDF |
|---|---|---:|---|---|
| Securing HCM | G34732-10 | 280 | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/ochus/index.html) | [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/ochus/securing-hcm.pdf) |
| Security Reference for HCM | G34733-07 | 1,756 | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/oawpm/index.html) | [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/oawpm/security-reference-for-hcm.pdf) |
| Implementing Recruiting | G34431-12 | 448 | [HTML](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/index.html) | [PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf) |

The live editions of the security books carry 2026 copyright notices. A guide ID is an edition identifier, not confirmation of the quarterly update deployed in a tenant.

## Which source answers which question?

| Question | Start here | Cross-check |
|---|---|---|
| Which Recruiting job role has a privilege? | [Security Reference for HCM](https://docs.oracle.com/en/cloud/saas/human-resources/oawpm/index.html) | *Implementing Recruiting*, Ch. 34, and actual role assignment in the tenant |
| How are HCM roles, data roles, and security profiles configured? | [Securing HCM](https://docs.oracle.com/en/cloud/saas/human-resources/ochus/index.html) | Recruiting-specific data-security settings in *Implementing Recruiting*, Ch. 34 |
| Requisition visibility differs by user | *Implementing Recruiting*, Ch. 9 and Ch. 34 | HCM security profiles, team/ownership rules, and role privileges |
| Offer action is missing | *Implementing Recruiting*, Ch. 21 and Ch. 34 | Security Reference role/privilege details and actual data role |
| Candidate search returns too few results | *Implementing Recruiting*, Ch. 13 and Ch. 34 | Candidate-search security profile and its profile-option prerequisites |
| Role inheritance is unclear | Security Reference for HCM | Security Console and Securing HCM |

## Security Reference for HCM — Recruiting role pages

The contents page of G34733-07 lists these role entries. Printed page to physical PDF page is +12 for substantive pages in this edition.

| Role | Printed page | Physical PDF page |
|---|---:|---:|
| Recruiter (Job Role) | 1622 | 1634 |
| Recruiting Administrator (Job Role) | 1646 | 1658 |
| Recruiting Agent (Job Role) | 1657 | 1669 |
| Recruiting Manager (Job Role) | 1662 | 1674 |

Use those sections for the role hierarchy, duty roles, privileges, and data-security policy. These pointers do not reproduce the full role definitions.

## Securing HCM — useful chapters

Printed page to physical PDF page is +12 for substantive pages in G34732-10.

| Ch. | Topic | Printed page | Physical PDF page |
|---:|---|---:|---:|
| 1 | An Introduction to HCM Security in the Cloud | 1 | 13 |
| 2 | Creating Implementation Users | 7 | 19 |
| 3 | Creating HCM Data Roles for Implementation Users | 15 | 27 |
| 4 | Enabling Basic Data Access for Abstract Roles | 27 | 39 |
| 5 | Assigning Roles to Implementation Users | 31 | 43 |
| 6 | Setting Up Applications Security | 35 | 47 |
| 7 | Managing Location-Based Access | 55 | 67 |
| 8 | Single Sign-On | 61 | 73 |
| 9 | API Authentication | 67 | 79 |
| 10 | Export and Import of Security Setup Data | 73 | 85 |
| 11 | Preparing for Application Users | 89 | 101 |
| 12 | Creating Application Users | 97 | 109 |
| 13 | Managing Application Users | 103 | 115 |
| 14 | Provisioning Roles to Application Users | 115 | 127 |
| 15 | Reporting on Application Users and Roles | 135 | 147 |
| 16 | HCM Data Roles and Security Profiles | 153 | 165 |
| 17 | Person Security Profiles | 161 | 173 |
| 18 | Organization and Other Security Profiles | 167 | 179 |
| 19 | Using the Security Console | 187 | 199 |
| 20 | Creating and Editing Job, Abstract, and Duty Roles | 195 | 207 |

## Recruiting-specific source pointers

The provided *Implementing Recruiting* guide states that data roles are mandatory for Recruiting to be fully functional. Without proper data roles, main-object visibility can be limited to ownership and lists of values can be empty. Chapter 34 includes the Recruiting Administrator View All data-role setup and Recruiting-specific security profiles.

- [DOC-001 source dossier](DOC-001.md)
- Official PDF for *Implementing Recruiting*: https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf
- Target-tenant assignments must be inspected in the Security Console; documentation alone does not prove a user has been granted a role.

**Processing state:** source identities, contents page, and Recruiting role page references verified against Oracle's current PDF viewer on 2026-10-22. Full companion bodies are not indexed locally.
