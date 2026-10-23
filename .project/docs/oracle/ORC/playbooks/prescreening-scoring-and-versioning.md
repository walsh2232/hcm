# Prescreening Questions, Scoring, and Versioning

**Source:** DOC-001, *Implementing Recruiting*, Chapter 10, printed pp. 197–202 / physical PDF pp. 215–220. [Official PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf).

## Question classifications

- **Disqualification question:** an eligibility/minimum requirement. Candidates must respond; a negative score may automatically disqualify the application. Question context determines which requisitions automatically receive it.
- **Prescreening Question Added Automatically:** context-matched; recruiting users can't manually add/remove the automatically managed question from a requisition.
- **Prescreening Question Added by User:** recruiters can manually add a matching question before applications exist. Once job applications exist, they can't add/remove those questions on that requisition.
- The guide describes internal and external prescreening questionnaires on each requisition. Automatically added disqualification questions aren't removable by the recruiter.

## Create a disqualification question

In Setup and Maintenance, go to **Recruiting and Candidate Experience > Candidate Job Applications > Question Library**. Select **Recruiting** in the Subscriber field, click Create, set the question to **Single Choice** or **Multiple Choice**, select **Score Question**, and set Question Classification to **Disqualification**. Select candidate types and context (Recruiting Organizations, Recruiting Locations, Job Families, Job Functions). Enter response scores; use a negative score for a disqualifying response. **Response Feedback** can tell the recruiter/hiring manager why an answer is disqualifying and isn't visible to candidates.

## Scoring/versioning rules

- Single-/multiple-choice prescreening questions can score each answer; the questionnaire's overall score is calculated automatically.
- For disqualification questions, a single negative-score answer can disqualify; the source says a large arbitrary negative score isn't necessary.
- If a question is already used in questionnaires, the guide says create a new version to change answer labels (including translations), context, question type, or question score.
- Translate question text and predefined-answer descriptions before candidates use the question, otherwise a new question version may be needed.
- Updates to disqualification questions or context-matched questions may require **Update Job Application Questionnaire** to propagate to requisitions without candidate applications.
- For returning external candidates, the guide describes **Prefill Prescreening Questions in External Candidate Applications** under Enterprise Recruiting and Candidate Experience Information > Recruiting Management. Do not conflate prefill with permission to change previously submitted candidate responses.

## Regression cases

Test each candidate type and context, negative and non-negative scores, Active/inactive question, used versus unused questionnaire, requisition with versus without applications, translations, the update scheduled process, and prefill for a returning external candidate.

Source: Chapter 10, printed pp. 197–202 / PDF pp. 215–220.
