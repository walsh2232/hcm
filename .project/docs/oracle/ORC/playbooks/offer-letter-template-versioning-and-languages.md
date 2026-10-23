# Offer Letter Template Versioning and Languages

**Source:** DOC-001, *Implementing Recruiting*, Chapter 20, printed pp. 267–278 / physical PDF pp. 285–296. [Official guide](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf).

## Safe template authoring sequence

1. Prepare the RTF template in Microsoft Word with the BI Publisher plugin, using an XML sample file that exposes the available offer tokens and representative values.
2. Add tokens and conditions; preview the generated letter using the sample XML to check layout and conditional sections.
3. Package the RTF with the companion sample XML as described in the source, then upload it as a Job Offer Letter Template content item to the Recruiting Content Library.
4. Set title, language, visibility (internal/external), activation/start timing, and activate the item only after preview/approval.
5. Do not modify or delete the uploaded template file directly in BI Publisher's Shared Folders; the guide says the upload places a copy there automatically.

## Versioning has candidate-impact implications

The guide states that an active offer associated with a template uses the current version of that template when the candidate views the letter. Updating the version of the same content-library item can therefore alter letters for existing active offers. If existing offers must retain the old terms/layout, create a new content-library item for the new version and inactivate the old item for new offer drafts; existing offers keep their original selected item unless redrafted and assigned another template.

Do not treat template versioning as a harmless global text update. Include existing active offers and redraft behavior in change impact analysis.

## Choose a multilingual design deliberately

- **Simple approach:** separate content-library items for each language/audience combination. Recruiters choose the correct item; maintenance repeats across items.
- **Compound approach:** one RTF per audience with repeated language sections controlled by BI Publisher conditions. The generated letter follows the language in which the candidate applied; conditionally include a fallback language if the organization's language policy needs it.
- The language condition uses BI Publisher's **XDOLOCALE** token. The guide's example for English is `<?if:$_XDOLOCALE='en'?>`; regional variants use a hyphen, such as `fr-CA`, not an underscore.

## E-signature: resolved-token distinction

The chapter describes different handling when recruiters are allowed to download offer letters with resolved tokens. In that method, token/condition content irrelevant at the moment of download can be removed from the adjusted RTF; for custom e-signature conditions, the guide describes a second shared BI Publisher subtemplate for adjusted offer letters. Confirm the organization's actual download/adjustment mode before editing e-signature sections.

## Regression cases

Preview every language and fallback branch; test internal/external visibility and start dates; compare same-item version updates against a separate new content-library item; test active offers that are not redrafted and ones that are; verify candidate-view language; and test e-signature behavior both with and without resolved-token adjustment.
