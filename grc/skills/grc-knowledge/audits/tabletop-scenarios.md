# Tabletop Exercise Scenario Templates

Templates for generating incident response (IR) and contingency plan (CP) tabletop exercises. FedRAMP requires annual testing of both the IRP (IR-3) and contingency plan (CP-4).

## Exercise Types

| Type | Description | Duration | Participants |
|------|-------------|----------|-------------|
| **Tabletop** | Discussion-based walkthrough of a scenario | 1-3 hours | IR/CP team, management |
| **Functional** | Hands-on simulation with actual system interaction | 2-8 hours | Technical staff, IR team |
| **Full-Scale** | End-to-end simulation including external parties | 4-16 hours | All stakeholders |

FedRAMP typically requires at minimum a tabletop exercise annually. Functional or full-scale exercises are recommended but not strictly required.

## Incident Response Scenarios

### Scenario IR-1: Unauthorized Access — Compromised Credentials

**Category**: CAT 1 — Unauthorized Access
**Severity**: High
**Controls Exercised**: IR-4, IR-5, IR-6, AC-2, AU-6, IA-5

**Setup**:
> Your SIEM alerts on unusual login activity. A privileged service account has authenticated from an IP address outside your known ranges at 2:00 AM local time. The account has queried multiple database tables containing [customer/user data]. The account's password was last rotated 120 days ago.

**Injects** (reveal progressively):
1. The source IP traces to a commercial VPN service
2. The same account was used to create a new IAM role with elevated permissions
3. A developer reports receiving a phishing email last week but didn't report it
4. Log analysis shows the account accessed 3 additional systems over the past 48 hours

**Discussion Questions**:
- How do you confirm this is a real incident vs. legitimate activity?
- What is your immediate containment action?
- Who do you notify first — internally and externally?
- How do you determine the scope of data accessed?
- What are your CISA reporting obligations and timeline?
- How do you handle the credential rotation for a privileged service account without causing an outage?
- What evidence do you preserve and how?

### Scenario IR-2: Ransomware / Malware

**Category**: CAT 3 — Malicious Code
**Severity**: Critical
**Controls Exercised**: IR-4, IR-5, IR-6, SI-3, CP-2, CP-9, CP-10

**Setup**:
> At 9:15 AM Monday, multiple users report being unable to access the internal ticketing system. The system administration team discovers that several application servers display a ransom message demanding payment. File system analysis shows encrypted files with a .locked extension across two application servers.

**Injects**:
1. The malware appears to have entered via a vulnerable third-party library in a web application
2. One of the affected servers handles the system's audit logging
3. The last verified clean backup is 18 hours old
4. The malware has persistence mechanisms and is attempting lateral movement to the database tier

**Discussion Questions**:
- What is your first containment step?
- How do you maintain logging if the log server is affected?
- Do you isolate the entire environment or just affected servers?
- What is your recovery strategy — rebuild from backup or attempt decryption?
- How do you verify backups are clean before restoring?
- What is your communication plan for affected users/customers?
- How does this affect your FedRAMP ConMon deliverables this month?

### Scenario IR-3: Data Exfiltration / Breach

**Category**: CAT 1 — Unauthorized Access
**Severity**: Critical
**Controls Exercised**: IR-4, IR-5, IR-6, IR-8, SC-7, AU-6, PT-1

**Setup**:
> Your DLP tool alerts on a large data transfer (500GB) from a production database to an external endpoint over the past 72 hours. The transfer used an authorized API credential but the destination is not a known integration partner. The data includes PII.

**Injects**:
1. The API credential belongs to a developer who left the organization 2 weeks ago
2. The transfer was spread across small increments to avoid volume-based alerts
3. The data includes names, email addresses, and encrypted SSNs for approximately 50,000 records
4. A journalist contacts your communications team asking about a data breach

**Discussion Questions**:
- How do you confirm what data was exfiltrated?
- What are your breach notification obligations (federal, state, contractual)?
- How do you handle the media inquiry?
- What was the failure in the offboarding process?
- How do you determine if the SSNs are at risk given they were encrypted?
- What is the CISA reporting timeline for this incident?
- What is the FedRAMP PMO notification process?

### Scenario IR-4: Supply Chain Compromise

**Category**: CAT 1 — Unauthorized Access
**Severity**: Critical
**Controls Exercised**: IR-4, IR-6, SR-1, SR-3, SA-9, SI-7

**Setup**:
> A widely-used open source library that your application depends on has been reported as compromised. The library maintainer's account was taken over, and a malicious version was published 5 days ago. Your CI/CD pipeline automatically pulled the update 3 days ago, and it has been deployed to production.

**Injects**:
1. The malicious code opens a reverse shell on port 443, blending with normal HTTPS traffic
2. Your SBOM analysis confirms the compromised version is in production
3. Two other FedRAMP-authorized CSPs have already reported this to FedRAMP PMO
4. The compromise affects a logging library — your audit trail for the past 3 days may be tampered with

**Discussion Questions**:
- How do you determine if the backdoor was exploited in your environment?
- Can you trust your logs from the affected period?
- What is your rollback strategy?
- How does your SBOM/dependency management process need to change?
- What are your obligations to notify customers?

### Scenario IR-5: Insider Threat

**Category**: CAT 1 — Unauthorized Access
**Severity**: High
**Controls Exercised**: IR-4, IR-5, AC-2, AC-6, AU-6, PS-4

**Setup**:
> A system administrator who submitted their resignation last week is observed accessing production systems outside of business hours. Audit logs show the admin exported several configuration files and database schemas. The admin has legitimate access as they are still employed during their notice period.

**Injects**:
1. The exported configurations include database connection strings and API keys
2. The admin has been downloading documents from the internal wiki about system architecture
3. HR confirms the admin is leaving for a competitor
4. The admin's access was never reduced after submitting resignation

**Discussion Questions**:
- At what point does this become an incident vs. an HR matter?
- What immediate access changes should be made?
- How do you balance the employee's rights during the notice period with security?
- What credentials need to be rotated?
- Should the admin be placed on administrative leave?

## Contingency Plan Scenarios

### Scenario CP-1: Data Center / Region Outage

**Controls Exercised**: CP-2, CP-6, CP-7, CP-9, CP-10

**Setup**:
> Your primary cloud region experiences a major outage. The cloud provider reports a networking issue affecting all availability zones in the region. No ETA for recovery has been provided. Your system has been unavailable for 45 minutes.

**Injects**:
1. The cloud provider updates their status: estimated recovery in 4-6 hours
2. Your alternate region has the application deployed but the database replica is 15 minutes behind
3. DNS failover has triggered but some customers are still hitting the primary region due to DNS caching
4. Your monitoring system was also in the affected region

**Discussion Questions**:
- Does this trigger your contingency plan activation? Who makes that decision?
- What is your RPO and can you accept 15 minutes of data loss?
- How do you communicate with customers during the outage?
- How do you monitor the system when your monitoring is also down?
- What is your reconstitution plan when the primary region recovers?
- How do you handle transactions that were in-flight during the failover?

### Scenario CP-2: Database Corruption

**Controls Exercised**: CP-2, CP-9, CP-10, SI-7

**Setup**:
> During a routine database maintenance window, a migration script contains an error that corrupts a critical table. The corruption is discovered 4 hours after the maintenance window, during which time approximately 200 new records were added to the affected table.

**Injects**:
1. The last clean backup was taken 12 hours ago (pre-maintenance)
2. Point-in-time recovery is available but restoring to pre-corruption would lose 4 hours of new data
3. The corrupted table is referenced by foreign keys in 6 other tables
4. The application is returning errors for any operation touching the affected data

**Discussion Questions**:
- Restore from backup (losing 4 hours) or attempt manual repair?
- How do you recover the 200 new records added post-corruption?
- What is your communication to affected users?
- How should the change management process be updated to prevent this?
- What testing should have caught the migration script error?

### Scenario CP-3: Sustained DDoS Attack

**Controls Exercised**: CP-2, SC-5, SC-7, IR-4, SI-4

**Setup**:
> Your system is under a sustained DDoS attack. The attack started 2 hours ago with volumetric flooding, then shifted to application-layer attacks targeting your authentication endpoint. Your WAF is mitigating most of the traffic but legitimate users are experiencing significant latency and intermittent failures.

**Injects**:
1. The attack volume increases from 10 Gbps to 50 Gbps
2. Your cloud provider's DDoS protection is engaged but the application layer attack continues
3. The attackers begin rotating attack vectors every 30 minutes
4. A federal agency customer escalates — they consider this a service disruption

**Discussion Questions**:
- At what point does degraded service become a contingency plan trigger?
- What is your escalation path with your cloud provider?
- How do you distinguish legitimate traffic from attack traffic?
- What are your SLA obligations to federal customers?
- Do you need to report this to CISA?

## Exercise Planning Checklist

### Before the Exercise
- [ ] Define exercise objectives (which plans/procedures are being tested)
- [ ] Select scenario appropriate to system and threat landscape
- [ ] Identify participants and their roles
- [ ] Prepare scenario materials and injects
- [ ] Brief the exercise facilitator
- [ ] Notify participants (date, time, duration, expectations)
- [ ] Prepare evaluation criteria
- [ ] Confirm this is an exercise (not a real incident) with all parties

### During the Exercise
- [ ] Facilitator introduces scenario and ground rules
- [ ] Walk through scenario step by step
- [ ] Introduce injects at appropriate intervals
- [ ] Document decisions, actions, and gaps identified
- [ ] Note roles and responsibilities that are unclear
- [ ] Track time taken for key decisions
- [ ] Capture action items

### After the Exercise
- [ ] Conduct hot wash (immediate debrief)
- [ ] Document lessons learned
- [ ] Identify gaps in plans, procedures, or training
- [ ] Create action items with owners and due dates
- [ ] Update IRP/CP based on findings
- [ ] File exercise report as evidence for IR-3 / CP-4
- [ ] Track action item completion

## Exercise Report Template

The exercise report serves as evidence for IR-3 (IR testing) and CP-4 (CP testing):

1. **Exercise summary** — Date, duration, scenario, participants
2. **Objectives** — What was being tested
3. **Scenario description** — Full scenario as presented
4. **Chronology** — Timeline of decisions and actions
5. **Findings** — Gaps, weaknesses, and strengths identified
6. **Lessons learned** — Key takeaways
7. **Action items** — Specific improvements with owners and dates
8. **Plan updates** — Changes made to IRP/CP based on exercise
9. **Next exercise** — Recommended scenario and date for next test
