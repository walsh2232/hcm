# Recruiting AI recommendations and data synchronization

**Source:** DOC-001, *Implementing Recruiting*, Chapter 25, printed pp. 333–344 / physical PDF pp. 351–362. [Official guide](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf). This is a troubleshooting aid, not an assertion of tenant entitlement or configuration.

## Separate the stages

1. **App activation:** Tools > **AI Apps Administration** > select the app > Activate App. A Processing status may persist for several minutes before Active.
2. **Profile options:** the source describes site-level `ORA_HRT_AI_SKILLS_ASSISTANT` and/or `ORA_HRD_AI_BEST_ROLES` set to Yes for applicable integrations. Check the feature-specific instructions; not every option applies to every feature.
3. **Recruiting data sync:** for recruiting recommendations, the guide names **Synchronize Recruiting Data for Candidate Recommendations** and says this process is for environments live on Oracle Recruiting and using a Recruiting AI feature. The Dynamic Skills case described in the guide requires selecting Recommended Skills.
4. **Logs:** review parent/child jobs and process logs for ingest files, counts, and errors.
5. **Downstream processing:** the guide states anonymized HCM data is transferred to the connected AI service for processing; recommendations may not become available immediately after ingestion.
6. **UI/access verification:** confirm the feature is configured for Recruiting, appropriate user access exists, and the target page contains the feature.

## Preconditions and caveats

The guide states the described AI Apps features require English as the environment's operation language. It describes role requirements for activation and notes Dynamic Skills activation also requires AI Talent Best Match activation. Verify current edition-specific prerequisites and feature entitlement.

For applicable recurrent ingestion, the guide suggests an initial weekly cadence with later adjustment based on hiring/data activity. A first run may take longer because historical data is processed. Treat this as source guidance to review, not a tenant-independent SLA.

## Diagnose missing recommendations

Check entitlement and release → app status → site profile options → correct scheduled-process feature selection → parent/child status and logs → elapsed downstream processing time → user security and UI setup. Escalate when logs or current source cannot explain the result; do not infer a model-quality issue from an empty UI alone.
