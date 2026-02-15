# Monthly Continuous Monitoring Deliverables

## Overview

Monthly ConMon deliverables provide the Authorizing Official (AO) and stakeholders with evidence that security controls remain effective, vulnerabilities are being identified and addressed, and the system's risk posture is understood. For FedRAMP-authorized systems, these deliverables are submitted monthly to the FedRAMP PMO and the authorizing agency through the designated repository.

---

## Vulnerability Scan Reports

### Infrastructure / OS Scans

- **Frequency:** Monthly, at minimum
- **Scope:** All in-scope hosts (servers, workstations, network devices, virtual machines, cloud instances)
- **Requirements:**
  - Authenticated (credentialed) scans
  - Full port range (all 65,535 TCP ports and relevant UDP ports)
  - 100% asset coverage within the authorization boundary
  - Scans must be completed within the reporting month
- **Deliverable format:** Raw scanner output (XML/CSV) plus summary report (PDF or equivalent)
- **Content must include:** Host IP/hostname, vulnerability title, CVE ID, CVSS score, severity (Critical/High/Moderate/Low), plugin/check ID, remediation guidance

### Web Application Scans

- **Frequency:** Monthly (Moderate/High baselines); quarterly (Low baseline)
- **Scope:** All externally and internally accessible web applications within the boundary
- **Requirements:**
  - Authenticated scanning where applicable (scan with a logged-in session)
  - Coverage of OWASP Top 10 categories
  - Both automated dynamic scanning and manual testing where warranted
- **Deliverable format:** Scanner report with findings mapped to OWASP categories and CVSS scores

### Database Scans

- **Frequency:** Monthly
- **Scope:** All in-scope database instances (relational, NoSQL, data warehouses)
- **Requirements:**
  - Authenticated scans with appropriate database credentials
  - Check for missing patches, default accounts, excessive privileges, configuration weaknesses
- **Deliverable format:** Database vulnerability report with severity ratings

### Container Scans

- **Frequency:** At image build/deployment and monthly for running containers
- **Scope:** All container images in use within the authorization boundary
- **Requirements:**
  - Scan base images and application layers separately
  - Identify known CVEs in OS packages and application dependencies
  - Track image provenance and signing
- **Deliverable format:** Container vulnerability report with CVE listings per image

---

## Scan Requirements Detail

### Authenticated Scanning

All scans must be credentialed. Unauthenticated scan results significantly undercount vulnerabilities and are not accepted as primary ConMon evidence. Scanning credentials must:

- Have sufficient privileges to enumerate installed software, patches, and configurations
- Be stored securely (encrypted credential vaults)
- Be rotated per organizational password policy
- Not be shared across environments (production vs. non-production)

### False Positive Management

When a scan finding is determined to be a false positive:

1. Document the finding with the specific plugin/check ID and affected asset
2. Provide technical justification explaining why the finding is not valid
3. Include evidence supporting the false positive determination (screenshots, configuration excerpts, vendor advisories)
4. Submit as part of the monthly POA&M or as a standalone false positive report
5. Request scanner vendor confirmation if possible
6. Re-validate false positive determinations at least annually

### Scan Deviation Requests

When an asset cannot be scanned during the reporting period:

1. Document the reason for the scan gap (maintenance window conflict, system unavailability, network segmentation issue)
2. Identify affected assets and the percentage of total inventory not scanned
3. Provide a planned date for completing the scan
4. Submit the deviation request to the AO for acknowledgment
5. Include scan deviation details in the monthly executive summary

---

## POA&M Updates

The POA&M must be updated monthly with the following changes:

- **New findings:** All newly discovered vulnerabilities from the current month's scans added as new POA&M items
- **Status changes:** Items that have moved from Open to In Progress, Completed, Closed, Risk Accepted, or False Positive
- **Milestone updates:** Progress against planned milestones for in-progress items
- **Overdue items:** Identification of any items past their scheduled completion date with updated timelines and justification
- **Closed items:** Items verified as remediated through re-scanning (retain in POA&M for historical reference)
- **Deviation request updates:** Status of any pending or approved deviation requests

See `poam-management.md` for complete POA&M lifecycle guidance.

---

## Unique Vulnerability Count and Trending

Monthly reporting must include:

| Metric | Description |
|--------|-------------|
| Total unique vulnerabilities | Count of distinct CVEs/findings across all scan types |
| By severity | Breakdown by Critical, High, Moderate, Low |
| New this month | Vulnerabilities first identified in the current reporting period |
| Remediated this month | Vulnerabilities confirmed closed through re-scanning |
| Net change | Month-over-month change in total open vulnerabilities |
| Trending chart | Visual representation of vulnerability counts over time (minimum 6-month window) |
| Age analysis | Distribution of open vulnerabilities by age (0-30 days, 31-90 days, 91-180 days, 180+ days) |

The trending data enables the AO to assess whether the system's vulnerability posture is improving, stable, or degrading.

---

## Inventory Updates

Monthly inventory deliverables must document:

- **New assets:** Any hardware, software, or virtual assets added to the authorization boundary during the reporting period, including justification and approval reference
- **Decommissioned assets:** Assets removed from the boundary, including decommissioning date and data sanitization confirmation
- **Changed assets:** Significant changes to existing assets (OS upgrades, role changes, IP address changes)
- **Total asset count:** Current count by category (servers, workstations, network devices, containers, cloud instances)
- **Scan coverage:** Percentage of inventoried assets included in vulnerability scans

Inventory accuracy is critical — scanning tools can only scan assets they know about.

---

## Significant Change Notifications

Any change that could affect the security posture of the system must be reported. Examples include:

- New interconnections or data flows
- Changes to the authorization boundary (new components, services, or environments)
- Changes to authentication mechanisms
- Deployment of new software or major version upgrades
- Changes to encryption implementations
- Infrastructure migrations (on-premises to cloud, region changes)
- Changes to key personnel (ISSO, System Owner)
- Incidents that may affect authorization status

Significant changes may trigger a reassessment of affected controls or a full reauthorization depending on severity. Refer to organizational significant change policy and FedRAMP Significant Change Request procedures.

---

## Monthly Executive Summary

A concise narrative report summarizing the system's security posture for the reporting month. Must include:

1. **Overall risk posture** — Summary assessment (improving, stable, degrading) with supporting data
2. **Scan results summary** — Total findings by severity across all scan types
3. **POA&M summary** — Total open items, new items, closed items, overdue items
4. **Remediation progress** — Key milestones achieved, critical/high items addressed
5. **Significant events** — Incidents, significant changes, personnel changes
6. **Scan coverage** — Percentage of assets scanned, any deviations
7. **Action items** — Items requiring AO attention or decision (deviation requests, risk acceptances)
8. **Next month outlook** — Planned activities, upcoming deadlines, anticipated changes

---

## Scan Coverage Metrics

| Metric | Target | Calculation |
|--------|--------|-------------|
| Infrastructure scan coverage | 100% | Assets scanned / Total in-scope assets |
| Web application scan coverage | 100% | Applications scanned / Total in-scope web apps |
| Database scan coverage | 100% | Databases scanned / Total in-scope databases |
| Container scan coverage | 100% | Images scanned / Total in-scope container images |
| Authenticated scan rate | 100% | Authenticated scans / Total scans performed |

Any coverage below 100% must be accompanied by a scan deviation request with justification and remediation timeline.

---

## FedRAMP Monthly Submission Requirements

For FedRAMP-authorized systems, the following must be submitted monthly:

| Deliverable | Format | Submission Method |
|------------|--------|-------------------|
| Infrastructure scan results | Raw output + summary | FedRAMP secure repository |
| Web application scan results | Raw output + summary | FedRAMP repository |
| Database scan results | Raw output + summary | FedRAMP repository |
| Container scan results (if applicable) | Raw output + summary | FedRAMP repository |
| Updated POA&M | FedRAMP POA&M template (Excel) | FedRAMP repository |
| Inventory workbook | FedRAMP inventory template | FedRAMP repository |
| Unique vulnerability count/trending | Included in executive summary or standalone | FedRAMP repository |
| Significant change requests (if any) | FedRAMP SCR template | FedRAMP repository |
| Monthly executive summary | PDF or document format | FedRAMP repository |

**Submission deadline:** Deliverables are typically due by the end of the month following the reporting period (e.g., January deliverables due by end of February), though specific timelines may vary by agency.

---

## References

- FedRAMP Continuous Monitoring Strategy Guide
- FedRAMP Monthly ConMon Submission Guidance
- FedRAMP POA&M Template
- FedRAMP Inventory Workbook Template
- NIST SP 800-137: Information Security Continuous Monitoring
- NIST SP 800-53 Rev. 5: CA-7, RA-5
