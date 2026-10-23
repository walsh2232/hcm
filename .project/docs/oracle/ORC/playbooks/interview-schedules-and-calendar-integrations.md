# Interview Schedules and Calendar Integrations

**Source:** DOC-001, *Implementing Recruiting*, Chapter 11 — Candidate Interviews. Use the [official PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf) for the full procedures and tables.

## Start by identifying the failure mode

- **No available interview slots:** inspect the schedule template, number of openings, schedule/slot timezone, and low/no-openings notification configuration.
- **Internal notifications are wrong or duplicated:** check intended recipients and delivered tokens; don't change a token only because the name seems misleading.
- **No interviewer free/busy data:** check whether Microsoft 365 calendar integration is enabled and whether the user has IRC_MANAGE_JOB_REQUISITION_INTERVIEW_SCHEDULE.
- **Candidate receives Recruiting email but no calendar event:** distinguish external from internal candidates and inspect documented integration limits.
- **Meeting link isn't generated:** identify Microsoft Teams versus Zoom and check provider setup and privileges separately.

## Interview notifications: preserve the token's intended behavior

The guide says not to change the ${InterviewerUserName} recipient token in notifications sent to requisition owners (recruiters and hiring managers). Those notifications have their own recipient behavior; changing the token can cause unintended outcomes, including duplicate notifications.

Test interviewer add/remove/update, schedule/reschedule/cancel, candidate-managed slot selection/reschedule, and low/no opening conditions. Verify recipients for each event rather than assuming all notifications go to the same person.

## Microsoft 365 calendar integration

The guide describes integration as enabling interview coordinators to view interviewer free/busy data and create, reschedule, or delete events synchronized with interviewer calendars. **On-premises mailboxes aren't supported** by this integration.

Important distinctions:

- Interviewers continue to receive Oracle Recruiting interview notifications in addition to Microsoft 365 calendar invitations.
- Internal candidates' availability isn't shown in the availability viewer; they also aren't sent Microsoft 365 interview events by this integration and continue to receive existing Recruiting notifications.
- With **Single User** access type, users can't select a meeting host; the default configured user is used. Users can't respond to interviews from Interview Details, and calendar events are sent to the interview creator only when that creator is also an interviewer. Responses already made in Microsoft 365 continue to be displayed in Recruiting.
- The interviewer availability viewer requires IRC_MANAGE_JOB_REQUISITION_INTERVIEW_SCHEDULE. Confirm role assignment independently from the calendar connection.

## Video conferencing

- **Microsoft Teams:** the guide's route is Setup and Maintenance > Recruiting and Candidate Experience > Recruiting and Candidate Experience Management > **Enterprise Recruiting and Candidate Experience Information**; edit **Microsoft Graph Integration** and enable Teams.
- **Zoom:** the guide separates OAuth app creation, credentials/redirect URL/allow-list, meeting scopes, Oracle Recruiting configuration, and assignment of **Authorize Zoom Integration**. Treat credentials and redirect URLs as environment-specific; never commit secrets.

## Regression checklist

- Candidate-managed and hiring-team-managed schedule types.
- Invite, update, cancellation, completion, add/remove interviewer, and reschedule notifications.
- User with and without interview-schedule privilege.
- External versus internal candidate calendar expectations.
- Microsoft 365 All Users versus Single User access type.
- Teams/Zoom link generation, token expiry/authorization, and separate TEST and PROD credentials.
- Schedule timezone and candidate/interviewer timezone differences.

**Source locations:** notification/timezone procedures, printed pp. 205–207 / PDF pp. 223–225; Microsoft 365 integration, printed pp. 210–214 / PDF pp. 228–232; Teams/Zoom sections, printed pp. 214–220 / PDF pp. 232–238.
