# POA&M Lifecycle Management

## Overview

The Plan of Action and Milestones (POA&M) is a key authorization document that identifies, tracks, and manages security weaknesses and the planned remediation activities to address them. It serves as the primary tool for communicating risk remediation status to the Authorizing Official (AO) and is a mandatory component of every authorization package.

The POA&M is a living document, updated monthly as part of Continuous Monitoring activities. It reflects the current vulnerability and risk posture of the information system and demonstrates the organization's commitment to resolving identified weaknesses.

---

## Purpose and Authority

| Source | Requirement |
|--------|------------|
| **OMB Circular A-130** | Requires federal agencies to maintain POA&Ms for all information systems to document planned remediation actions for identified weaknesses |
| **NIST SP 800-53 Rev. 5 CA-5** | Plan of Action and Milestones control — requires organizations to develop and update POA&Ms for the system documenting planned remedial actions to correct weaknesses or deficiencies |
| **FISMA** | Mandates POA&M reporting as part of agency information security programs |
| **FedRAMP** | Requires monthly POA&M updates submitted to the FedRAMP repository; defines specific required fields and severity-based remediation timelines |

The POA&M does not replace the need to remediate findings. It is a tracking and accountability mechanism, not a risk acceptance mechanism. Risk acceptance is a separate AO decision documented through deviation requests.

---

## Required POA&M Fields

The following fields are required for each POA&M entry. FedRAMP-specific fields are noted.

| Field | Description | Example |
|-------|-------------|---------|
| **Weakness ID** | Unique identifier for the POA&M item (V-XXXXX, POA&M-YYYY-NNN) | V-00142 |
| **Source** | How the weakness was identified (vulnerability scan, assessment, penetration test, incident, audit) | Nessus Monthly Scan — January 2026 |
| **Control** | NIST 800-53 control(s) associated with the weakness | RA-5, SI-2 |
| **Weakness Description** | Clear description of the vulnerability or deficiency | Apache HTTP Server 2.4.51 vulnerable to CVE-2024-XXXXX (path traversal) |
| **Point of Contact** | Person responsible for remediation | Jane Smith, System Administrator |
| **Resources Required** | Estimated resources (labor hours, funding, tools) needed for remediation | 8 hours system admin time, maintenance window |
| **Severity** (FedRAMP) | CVSS-based severity: Critical, High, Moderate, Low | High (CVSS 7.5) |
| **Risk Rating** | Adjusted risk considering compensating controls, exposure, and exploitability | Moderate (compensating WAF in place) |
| **Original Detection Date** | Date the weakness was first identified | 2026-01-15 |
| **Scheduled Completion Date** | Target date for completing remediation | 2026-04-15 |
| **Milestones** | Specific remediation steps with target dates | 1. Test patch in staging (2026-02-01); 2. Deploy to production (2026-03-01); 3. Verify via re-scan (2026-03-15) |
| **Status** | Current status of the POA&M item (see status table below) | In Progress |
| **Status Date** | Date of the most recent status update | 2026-02-01 |
| **Vendor Dependency** | Whether remediation depends on a vendor (patch availability, support) | Yes — awaiting vendor patch for legacy component |
| **Deviation Request** | Whether a deviation request has been submitted and its status | Operational Requirement — Approved 2026-01-20 |
| **Comments/History** | Narrative history of actions taken and status changes | 2026-01-15: Discovered in scan. 2026-02-01: Patch tested in staging. |
| **Completion Evidence** | Evidence that remediation is complete (re-scan results, configuration screenshot) | Re-scan dated 2026-03-15 shows CVE no longer detected |

---

## POA&M Lifecycle

### Phase 1: Discovery

A weakness is identified through one of the following sources:

- Monthly vulnerability scans (infrastructure, web application, database, container)
- Annual security assessment (control assessment findings)
- Penetration testing
- Security incidents
- Configuration compliance scans
- Audit findings
- Self-identified by system team

### Phase 2: Documentation

The finding is documented in the POA&M with all required fields:

1. Assign a unique Weakness ID
2. Record the source and detection date
3. Map to applicable NIST 800-53 control(s)
4. Write a clear, specific weakness description (include CVE IDs where applicable)
5. Assign a severity rating based on CVSS score
6. Assess the adjusted risk rating considering the operational environment
7. Assign a responsible point of contact
8. Set the initial status to Open

### Phase 3: Remediation Planning

Develop a remediation plan with specific milestones:

1. Identify the remediation approach (patch, configuration change, compensating control, architectural change)
2. Estimate resources required (personnel, funding, tools, maintenance windows)
3. Identify any vendor dependencies
4. Define milestones with target dates
5. Set the scheduled completion date based on severity-driven timelines (see below)
6. If remediation cannot meet required timelines, prepare a deviation request
7. Update status to In Progress

### Phase 4: Milestone Tracking

Track progress against milestones on a monthly basis:

1. Update milestone status (completed, in progress, delayed)
2. Document actions taken during the reporting period
3. If milestones are delayed, update target dates and provide justification
4. Escalate blocked items per escalation procedures
5. Record vendor dependency status changes
6. Update the Comments/History field with current actions

### Phase 5: Verification

Confirm that the remediation is effective:

1. Perform a re-scan or re-assessment targeting the specific weakness
2. Verify the vulnerability is no longer detected or the control deficiency is resolved
3. Document the verification method and date
4. Attach evidence (re-scan results, configuration screenshots, test results)
5. Update status to Completed

### Phase 6: Closure

Formalize the closure of the POA&M item:

1. Review completion evidence for sufficiency
2. Obtain ISSO or AO verification (depending on organizational policy)
3. Update status to Closed
4. Record the closure date
5. Retain the closed item in the POA&M for historical reference and audit purposes

---

## Severity-Based Remediation Timelines

FedRAMP defines mandatory remediation timelines based on vulnerability severity:

| Severity | CVSS Score Range | Remediation Timeline | Escalation Trigger |
|----------|-----------------|---------------------|-------------------|
| **Critical** | 9.0 — 10.0 | 30 calendar days from detection | Day 15 if no progress |
| **High** | 7.0 — 8.9 | 30 calendar days from detection | Day 15 if no progress |
| **Moderate** | 4.0 — 6.9 | 90 calendar days from detection | Day 45 if no progress |
| **Low** | 0.1 — 3.9 | 180 calendar days from detection | Day 90 if no progress |

These timelines represent maximums. Organizations should remediate as quickly as operationally feasible. Critical vulnerabilities with known active exploitation should be treated as emergencies with immediate remediation.

### Operational Requirements and Risk Adjustments

When remediation within the standard timeline is not feasible:

- **Compensating controls** may reduce the adjusted risk rating but do not extend the remediation deadline without a formal deviation request
- **Operational constraints** (legacy systems, vendor dependencies, mission-critical availability requirements) must be documented and submitted as deviation requests
- **Risk acceptance** is an AO decision — the ISSO documents the risk, but only the AO can formally accept it
- **Temporary mitigations** (network segmentation, enhanced monitoring, WAF rules) should be implemented while awaiting full remediation

---

## POA&M Statuses

| Status | Definition | When Used |
|--------|-----------|-----------|
| **Open** | Weakness identified and documented; remediation not yet started | Initial state upon discovery |
| **In Progress** | Remediation activities are actively underway with defined milestones | After remediation planning is complete and work has begun |
| **Completed** | Remediation has been implemented but not yet independently verified | After remediation actions are taken, pending re-scan or re-assessment |
| **Closed** | Remediation has been verified through re-scanning or re-assessment | After verification confirms the weakness is resolved |
| **Risk Accepted** | AO has formally accepted the residual risk; no further remediation planned | After AO signs a risk acceptance decision with documented justification |
| **False Positive** | Finding determined to be a false positive with documented evidence | After technical analysis confirms the finding is not valid |
| **Deferred** | Remediation postponed with AO approval and documented justification | When operational constraints prevent timely remediation and a deviation request is approved |

---

## Deviation Requests

When a POA&M item cannot be remediated within the required timeline, a deviation request must be submitted to the AO.

### Deviation Request Types

| Type | Description | Typical Justification |
|------|-------------|----------------------|
| **Operational Requirement** | The vulnerable configuration or software is required for mission operations | Legacy system with no available patch; specific software version required by mission-critical application |
| **False Positive** | The scanner finding does not represent an actual vulnerability | Compensating control renders the finding inapplicable; scanner misidentification; configuration context not detected by scanner |
| **Risk Adjustment** | The actual risk is lower than the CVSS score suggests due to environmental factors | System is air-gapped; vulnerability is in a component not exposed to untrusted networks; compensating controls significantly reduce exploitability |

### Required Justification

Each deviation request must include:

1. **POA&M reference** — Weakness ID and description of the finding
2. **Deviation type** — Operational requirement, false positive, or risk adjustment
3. **Technical justification** — Detailed explanation of why remediation is not feasible or the finding is not valid
4. **Compensating controls** — Specific controls in place that reduce the residual risk
5. **Residual risk assessment** — Assessment of the remaining risk with compensating controls in place
6. **Requested duration** — How long the deviation is needed (not indefinite — must have a review date)
7. **Review date** — When the deviation will be reassessed for continued validity
8. **Supporting evidence** — Screenshots, vendor documentation, architecture diagrams, or other evidence

### Approval Authority

- Deviation requests are submitted by the ISSO
- Reviewed and approved or denied by the AO
- For FedRAMP systems, the FedRAMP PMO may also review deviation requests
- Approved deviations must be documented in the POA&M with the approval date and conditions
- Denied deviations require the original remediation timeline to be followed

---

## Vendor Dependency Documentation

When remediation depends on a third-party vendor:

| Required Documentation | Purpose |
|-----------------------|---------|
| Vendor name and product | Identify the dependency |
| Vendor ticket/case number | Track the vendor's progress |
| Date vendor was notified | Demonstrate timely engagement |
| Expected vendor resolution date | Inform scheduled completion date |
| Interim mitigations | Document compensating controls while awaiting vendor action |
| Escalation actions | Steps taken if vendor is unresponsive (escalation to vendor management, alternative solutions, contract enforcement) |
| Status updates | Monthly updates on vendor progress |

Vendor dependency does not excuse the organization from implementing available mitigations or from meeting remediation timelines where alternative solutions exist.

---

## POA&M Metrics

Track and report the following metrics monthly:

| Metric | Description | Target |
|--------|-------------|--------|
| **Total open items** | Count of all POA&M items in Open, In Progress, or Deferred status | Trending downward |
| **By severity** | Breakdown of open items by Critical, High, Moderate, Low | Zero critical; minimal high |
| **Overdue items** | Items past their scheduled completion date | Zero |
| **Average age** | Mean number of days items have been open | Below severity-based SLA |
| **Closure rate** | Items closed this month / Total items open at start of month | Trending upward |
| **New items** | Items added this month | Context-dependent |
| **MTTR by severity** | Mean time to remediate by severity level | Within SLA |
| **Deviation request count** | Number of active deviation requests | Minimal |

---

## Monthly Reporting Requirements

The POA&M must be updated and submitted monthly with the following:

1. All new findings from the current month's scans and assessments
2. Status updates for all existing items
3. Milestone progress for in-progress items
4. Closure evidence for completed items
5. Updated scheduled completion dates for delayed items (with justification)
6. Deviation request status changes
7. Summary metrics (total open, new, closed, overdue)

For FedRAMP, the POA&M is submitted in the FedRAMP POA&M template format to the designated repository.

---

## Escalation Procedures for Overdue Items

| Escalation Level | Trigger | Action | Responsible Party |
|------------------|---------|--------|-------------------|
| Level 1 | Item reaches 50% of remediation timeline with no progress | ISSO contacts responsible party; documents in POA&M | ISSO |
| Level 2 | Item reaches 75% of remediation timeline with insufficient progress | ISSO escalates to System Owner; remediation plan review | ISSO, System Owner |
| Level 3 | Item is overdue (past scheduled completion date) | System Owner escalates to AO; deviation request or risk acceptance required | System Owner, AO |
| Level 4 | Item is overdue by more than 30 days with no deviation request | AO may issue formal notice; potential impact to authorization status | AO |
| Level 5 | Critical/High items overdue with no approved deviation | AO considers authorization revocation or operational restrictions | AO, CISO |

---

## POA&M Template

Below is a reference template with all required fields. Organizations should adapt this to their GRC platform or use the FedRAMP-provided template.

| Field | Value |
|-------|-------|
| Weakness ID | POA&M-2026-001 |
| Source | Nessus Authenticated Scan — January 2026 |
| Control | SI-2, RA-5 |
| Weakness Description | CVE-2025-XXXXX: OpenSSL 3.0.x buffer overflow vulnerability allowing remote code execution. Affects 12 production servers running Ubuntu 22.04. |
| Point of Contact | John Doe, Infrastructure Lead |
| Resources Required | 16 hours system admin time; scheduled maintenance window; testing in staging environment |
| Severity | Critical (CVSS 9.8) |
| Adjusted Risk Rating | High (servers behind WAF and not directly internet-exposed) |
| Original Detection Date | 2026-01-15 |
| Scheduled Completion Date | 2026-02-14 (30-day critical timeline) |
| Milestone 1 | Test patched OpenSSL in staging — Target: 2026-01-22 — Status: Completed 2026-01-21 |
| Milestone 2 | Deploy patch to production batch 1 (6 servers) — Target: 2026-01-29 — Status: Completed 2026-01-28 |
| Milestone 3 | Deploy patch to production batch 2 (6 servers) — Target: 2026-02-05 — Status: In Progress |
| Milestone 4 | Verify via re-scan — Target: 2026-02-10 — Status: Pending |
| Status | In Progress |
| Status Date | 2026-02-01 |
| Vendor Dependency | No |
| Deviation Request | N/A |
| Comments | 2026-01-15: Detected in monthly scan. 2026-01-16: Severity confirmed, remediation planning initiated. 2026-01-21: Patch validated in staging with no regressions. 2026-01-28: First batch deployed successfully. |
| Completion Evidence | Pending — will attach re-scan results upon completion |

---

## Common Mistakes and Best Practices

### Common Mistakes

| Mistake | Impact |
|---------|--------|
| Vague weakness descriptions ("server needs patching") | Difficult to track, assess risk, or verify remediation |
| Missing CVE IDs for vulnerability scan findings | Cannot accurately track or deduplicate findings |
| No milestones defined for complex remediation | No visibility into progress; delayed escalation |
| Closing items without verification evidence | Cannot prove to AO or assessor that weakness is resolved |
| Setting all items to the same priority | Critical items do not receive appropriate urgency |
| Not updating monthly | POA&M becomes stale and unreliable as a risk management tool |
| Removing closed items from the POA&M | Loses historical record needed for audits and trend analysis |
| Treating deviation requests as permanent | Deviations must have review dates and be reassessed periodically |
| Not tracking vendor dependencies | No accountability for vendor-dependent remediation |

### Best Practices

1. **Be specific in descriptions** — Include CVE IDs, affected assets (count and type), software versions, and the nature of the risk
2. **Define milestones for every item** — Even simple patches benefit from milestones (test, deploy, verify)
3. **Automate where possible** — Use GRC platforms to auto-generate POA&M entries from scan findings
4. **Deduplicate findings** — Track unique vulnerabilities, not individual host instances (aggregate hosts under one POA&M item per unique CVE)
5. **Link to evidence** — Attach or reference scan results, configuration screenshots, and verification evidence
6. **Review weekly internally** — Do not wait for the monthly reporting cycle to track progress
7. **Maintain accountability** — Every item must have a named point of contact, not a team or group
8. **Track aging rigorously** — Implement automated alerts for items approaching their remediation deadline
9. **Reconcile with scans monthly** — Ensure every scan finding has a corresponding POA&M entry and vice versa
10. **Brief the AO regularly** — Do not surprise the AO with overdue items at reporting time

---

## References

- OMB Circular A-130: Managing Information as a Strategic Resource
- NIST SP 800-53 Rev. 5: CA-5 (Plan of Action and Milestones)
- NIST SP 800-37 Rev. 2: Risk Management Framework — Monitor Step
- NIST SP 800-137: Information Security Continuous Monitoring
- FedRAMP POA&M Template and Guidance
- FedRAMP Continuous Monitoring Strategy Guide
