# Compliance Calendar

Consolidated recurring compliance activities by frequency and framework. Use this to build an organization-specific compliance calendar.

## FedRAMP Recurring Activities

### Daily / Continuous

| Activity | Control Reference | Responsible Role |
|----------|------------------|-----------------|
| Log review and monitoring | AU-6, SI-4 | SOC Analyst / SIEM |
| Intrusion detection monitoring | SI-4 | SOC Analyst |
| Configuration drift monitoring | CM-3, CM-6 | Security Engineer |
| Automated vulnerability alerting | RA-5, SI-5 | Security Engineer |
| Malware signature updates | SI-3 | Automated / Security Engineer |
| Incident monitoring and triage | IR-4, IR-5 | SOC Analyst |

### Weekly

| Activity | Control Reference | Responsible Role |
|----------|------------------|-----------------|
| POA&M progress review (internal) | CA-5 | ISSO |
| Security advisory review | SI-5 | Security Engineer |
| Failed login / account lockout review | AC-7, AU-6 | ISSO |
| Backup verification spot-check | CP-9 | System Administrator |

### Monthly

| Activity | Control Reference | Responsible Role | Deliverable |
|----------|------------------|-----------------|-------------|
| Vulnerability scan — OS/infrastructure | RA-5 | Security Engineer | Scan report |
| Vulnerability scan — web application | RA-5 | Security Engineer | Scan report |
| Vulnerability scan — database | RA-5 | Security Engineer | Scan report |
| Vulnerability scan — container images | RA-5 | Security Engineer | Scan report |
| POA&M update and submission | CA-5 | ISSO | Updated POA&M |
| Scan deviation requests (if needed) | RA-5 | ISSO | DR documents |
| Unique vulnerability count and aging | RA-5 | ISSO | Metrics report |
| Executive security summary | PM-6 | ISSO/CISO | Monthly summary |
| Continuous monitoring report to AO | CA-7 | ISSO | ConMon report |

### Quarterly

| Activity | Control Reference | Responsible Role | Deliverable |
|----------|------------------|-----------------|-------------|
| Privileged user access review | AC-2, AC-6 | ISSO | Review report |
| Hardware inventory reconciliation | CM-8 | System Administrator | Updated inventory |
| Software inventory reconciliation | CM-8 | System Administrator | Updated inventory |
| Third-party/vendor risk review | SA-9, SR-6 | ISSO | Vendor review report |
| Security metric trend analysis | CA-7 | ISSO | Trend report |
| Firewall rule review | SC-7 | Network Engineer | Rule review report |

### Semi-Annual (Best Practices)

These are common best practices; FedRAMP mandates annual as the minimum for most activities below.

| Activity | Control Reference | Responsible Role | Deliverable |
|----------|------------------|-----------------|-------------|
| Security awareness refresher (optional — annual is the minimum) | AT-2 | Training Coordinator | Training records |
| Interconnection agreement review | CA-3 | ISSO | ISA review log |
| Physical access list review | PE-2, PE-3 | Facilities / ISSO | Updated access list |

### Annual

| Activity | Control Reference | Responsible Role | Deliverable |
|----------|------------------|-----------------|-------------|
| Security assessment (3PAO) | CA-2 | 3PAO / ISSO | SAR |
| SSP comprehensive review and update | PL-2 | ISSO | Updated SSP |
| Contingency plan test | CP-4 | ISSO / CP Director | Test results report |
| Incident response plan test | IR-3 | ISSO / IR Lead | Test results report |
| Security awareness training (all staff) | AT-2 | Training Coordinator | Training records |
| Role-based security training | AT-3 | Training Coordinator | Training records |
| Privacy impact reassessment | RA-8 | Privacy Officer | Updated PIA |
| Risk assessment update | RA-3 | ISSO | Updated RAR |
| Configuration baseline review | CM-2 | Security Engineer | Updated baselines |
| Rules of behavior re-acknowledgment | PL-4 | ISSO | Signed RoB |
| Policy review (all policies) | *-1 (all families) | Policy owners | Updated policies |
| Account comprehensive review | AC-2 | ISSO | Account review report |
| Media sanitization review | MP-6 | ISSO | Sanitization log |
| Supply chain risk review | SR-1, SR-6 | ISSO | SCRM update |

### Event-Driven

| Trigger | Activities | Control Reference |
|---------|-----------|------------------|
| Security incident | IR procedures, reporting, lessons learned | IR-4, IR-5, IR-6, IR-8 |
| Significant change | SIA, affected control assessment, SSP update | CM-3, CA-2, PL-2 |
| New interconnection | ISA negotiation, CA-3 assessment | CA-3 |
| Personnel departure | Account disabling, access revocation | AC-2, PS-4 |
| Personnel role change | Access review and modification | AC-2, PS-5 |
| New vulnerability (critical) | Emergency patch assessment, POA&M entry | SI-2, RA-5 |
| ATO expiration approaching | Reauthorization preparation | CA-6 |

## SOC 2 Recurring Activities

| Frequency | Activity | TSC Reference |
|-----------|----------|---------------|
| Daily | Monitoring and alerting | CC7.2, CC7.3 |
| Monthly | Access review | CC6.1, CC6.2 |
| Monthly | Change management review | CC8.1 |
| Quarterly | Risk assessment update | CC3.1, CC3.2 |
| Quarterly | Vendor management review | CC9.2 |
| Annual (minimum) | Security awareness training | CC1.4 |
| Annual | Comprehensive risk assessment | CC3.1, CC3.2, CC3.3 |
| Annual | Policy review | CC1.1, CC5.2 |
| Annual | Business continuity test | A1.2, A1.3 |
| Annual | Penetration test | CC4.1 |
| Ongoing | SOC 2 Type II observation period | All criteria |

## ISO 27001 Recurring Activities

| Frequency | Activity | Clause/Annex Reference |
|-----------|----------|----------------------|
| Ongoing | Risk treatment implementation | 6.1.3, 8.3 |
| Monthly | ISMS performance monitoring | 9.1 |
| At planned intervals | Internal audit (rotating scope) | 9.2 |
| Annual | Management review | 9.3 |
| Annual | Risk assessment review | 6.1.2 |
| Annual | Statement of Applicability review | 6.1.3 |
| Annual | ISMS policy review | 5.2 |
| Annual | Competence/training assessment | 7.2 |
| Annual | Objectives review and performance | 6.2 |
| Triennial | Recertification audit | External |
| Annual | Surveillance audit (years 1, 2) | External |
| Event-driven | Corrective actions | 10.1 |
| Event-driven | Nonconformity management | 10.1 |

## PCI DSS Recurring Activities

| Frequency | Activity | Requirement |
|-----------|----------|-------------|
| Daily | Log review | 10.4.1 |
| Daily | IDS/IPS alert review | 11.5.1 |
| Weekly | File integrity monitoring review | 11.5.2 |
| Quarterly | Wireless access point scan | 11.2.1 |
| Quarterly | Internal vulnerability scan | 11.3.1 |
| Quarterly | External vulnerability scan (ASV) | 11.3.2 |
| Quarterly | Firewall/router rule review | 1.2.7 |
| Semi-Annual | Service provider compliance review | 12.8.4 |
| Annual | Penetration test (internal + external) | 11.4.1 |
| Annual | Segmentation test | 11.4.5 |
| Annual | Security awareness training | 12.6.2 |
| Annual | Risk assessment | 12.3.1 |
| Annual | Policy review | 12.1.1 |
| Annual | Incident response test | 12.10.2 |
| Annual | PCI DSS assessment (QSA/ISA) | 12.4 |

## CMMC Recurring Activities

| Frequency | Activity | Practice Reference |
|-----------|----------|-------------------|
| Ongoing | CUI handling and marking | 3.1, 3.8 |
| Monthly | Vulnerability scanning | 3.11.2 |
| Quarterly | Access review | 3.1.1 |
| Annual | Security awareness training | 3.2.1, 3.2.2 |
| Annual | Risk assessment | 3.11.1 |
| Annual | Security plan review | 3.12.4 |
| Annual | Incident response test | 3.6.3 |
| Triennial | CMMC assessment (C3PAO for Level 2) | External |

## Building a Compliance Calendar

### Step 1: Identify Applicable Frameworks
List all frameworks the organization must comply with.

### Step 2: Consolidate Activities
Many frameworks require the same activities (e.g., vulnerability scanning, access reviews). Consolidate to avoid duplication while meeting the strictest frequency.

### Step 3: Frequency Harmonization
When multiple frameworks require the same activity at different frequencies, use the most frequent requirement:
- FedRAMP monthly scans satisfy PCI quarterly scan requirement
- FedRAMP annual IR test satisfies SOC 2 and ISO requirements
- PCI daily log review satisfies FedRAMP ongoing log review requirement

### Step 4: Assign Ownership
Every activity needs a named role (not individual) responsible for execution and a backup.

### Step 5: Set Alerts
Calendar reminders should fire well before the deadline:
- Monthly activities: 1 week before
- Quarterly activities: 2 weeks before
- Annual activities: 1 month before

### Step 6: Track Evidence
Each completed activity should produce evidence (report, screenshot, sign-off) that is stored in a central evidence repository.

## Month-by-Month Template (FedRAMP Moderate)

| Month | Monthly (Every Month) | Quarterly (Q) | Annual (Pick a Month) |
|-------|----------------------|---------------|----------------------|
| Jan | Scans, POA&M, ConMon report | Q1: Privileged access review, inventory | Annual risk assessment |
| Feb | Scans, POA&M, ConMon report | | |
| Mar | Scans, POA&M, ConMon report | | Security awareness training (all staff) |
| Apr | Scans, POA&M, ConMon report | Q2: Privileged access review, inventory | SSP annual update begins |
| May | Scans, POA&M, ConMon report | | Contingency plan test |
| Jun | Scans, POA&M, ConMon report | | Incident response test |
| Jul | Scans, POA&M, ConMon report | Q3: Privileged access review, inventory | 3PAO annual assessment begins |
| Aug | Scans, POA&M, ConMon report | | 3PAO assessment continues |
| Sep | Scans, POA&M, ConMon report | | Policy reviews, RoB re-sign |
| Oct | Scans, POA&M, ConMon report | Q4: Privileged access review, inventory | SAR finalized |
| Nov | Scans, POA&M, ConMon report | | Configuration baseline review |
| Dec | Scans, POA&M, ConMon report | | Privacy reassessment, SCRM review |

**Note**: This is a template — adjust annual activities to align with your organization's assessment cycle and ATO anniversary date.
