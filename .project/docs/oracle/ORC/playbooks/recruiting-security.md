# Recruiting security foundation

Synthesized from DOC-001, Chapter 34, with current companion pointers in [Security Navigation](../SECURITY-NAVIGATION.md).

The implementation guide states that Recruiting data roles are required for full functionality. Without suitable data roles, main-object visibility can be limited to ownership and lists of values can be empty.

The documented setup for the **Recruiting Administrator View All** data role specifies:
- prerequisite: sign in as TechAdmin;
- task: **Assign Security Profiles to Role**;
- Data Role: Recruiting Administrator View All;
- Job Role: Recruiting Administrator;
- security profiles: Organization — View All Organizations; Person — View All People; Public Person — View All People; Job Requisition — View All Job Requisitions;
- submit the role and assign it to the implementation user in Security Console.

This is the guide's implementation-user setup, not a recommendation to grant broad View All access to production users.

For a missing-access issue, independently test function privilege, data role/security-profile scope, hiring/offer team and ownership rules, profile-option dependencies, feature opt-in/entitlement, and actual role assignment. The label "Recruiter" alone doesn't establish access to every Recruiting object.

Use [Securing HCM](https://docs.oracle.com/en/cloud/saas/human-resources/ochus/index.html) for security design/setup patterns and [Security Reference for HCM](https://docs.oracle.com/en/cloud/saas/human-resources/oawpm/index.html) for role hierarchy and privilege detail. Verify the current tenant state.
