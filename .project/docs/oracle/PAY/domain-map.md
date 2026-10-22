# Oracle Global Payroll — domain map

**Evidence baseline:** 2026-10-22  
**Primary setup/operating references:** see [README.md](README.md) and [source-manifest.json](source-manifest.json).

## Topic map

- Payroll implementation order, legislative data groups, payroll statutory units, tax reporting units and payroll definitions
- Elements, balances, Fast Formulas, calculation components, costing, banking and payment methods
- Payroll flows, task actions, flow patterns, diagnostics and error recovery
- Run results, prepayments, payments, balances, costing and reconciliation
- Employee-facing payroll information and payslip/statement workflows
- Cross-module dependencies with Global HR, Absence, Time and Labor, Benefits, Finance and third parties
- Canadian payroll legislative and implementation steps as a jurisdiction-specific branch, not as global payroll defaults

## Retrieval sequence

1. Confirm the product/module and tenant's actual quarterly release; identify the process/object and the persona affected.
2. For release changes, open the linked feature detail and summary; check impact, action-to-enable, prerequisites, opt-in, and changes to roles/processes.
3. Search the exact implementation/setup guide for the referenced task, profile option, lookup, formula, security privilege, scheduled process or interface.
4. Search the operational/using guide for the resulting workflow, statuses and expected outcome. If Oracle publishes one combined implementation/using guide, use its specific section.
5. Retrieve adjacent prerequisites, exceptions and error handling. Do not infer missing steps from general HCM patterns.
6. Cite the exact Oracle chapter URL and section or the PDF page from the local search locator. Distinguish guide age from release-specific validation.
7. If the evidence doesn't explain a tenant defect, gather reproducible facts and consult authorized Oracle Support content instead of inventing a workaround.

## Domain-specific caution

Payroll is jurisdiction-specific and consequential. The Canadian guide is separately identified; never use its rules as global defaults. Confirm legislation and legislative data, LDG, payroll statutory units, tax/reporting units, effective dates, pay frequencies, processing definitions and the target environment's quarterly release.

## What this map is not

This is a source-navigation aid and a short list of domain areas. It is not an assertion that every capability is present or enabled, nor a substitute for the complete Oracle guide. Exact UI paths, role privileges, fields, endpoints, scheduled process names and formulas must be retrieved from the source index before use.
