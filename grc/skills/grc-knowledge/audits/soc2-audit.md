# SOC 2 Audit Process

## Overview

SOC 2 (System and Organization Controls 2) is an attestation engagement performed by a CPA firm under AICPA AT-C Section 205 (Examination Engagements). It evaluates an organization's controls relevant to one or more Trust Services Categories (TSC): Security (Common Criteria), Availability, Processing Integrity, Confidentiality, and Privacy. Security (CC) is always in scope; the other categories are optional.

## Type I vs Type II

| Attribute | Type I | Type II |
|-----------|--------|---------|
| Focus | Design of controls at a point in time | Design and operating effectiveness over a period |
| Period | Single date (snapshot) | Minimum 3 months (6-12 months recommended); typically 12 months |
| Testing | Controls are described and evaluated for suitability | Controls are tested for consistent operation |
| Evidence | Policies, configurations, screenshots at point in time | Populations, samples, logs, tickets over the period |
| Market acceptance | Limited; often a stepping stone | Preferred by enterprise customers |
| Typical use case | First-time SOC 2, demonstrating commitment | Ongoing assurance, contractual requirement |
| Timeline to complete | 4-8 weeks | 8-16 weeks of fieldwork (after the observation period) |

## Audit Phases

### Phase 1: Scoping

- Define the system boundaries (infrastructure, software, people, procedures, data)
- Select Trust Services Categories (Security is mandatory)
- Identify subservice organizations (carve-out vs inclusive method)
- Document the system description (Section III of the report)
- Determine complementary user entity controls (CUECs)
- Determine complementary subservice organization controls (CSOCs)

### Phase 2: Readiness Assessment (Optional but Recommended)

- Gap analysis against selected TSC criteria
- Review of existing policies, procedures, and controls
- Identification of control gaps and remediation priorities
- Typically performed 3-6 months before the Type II observation period begins
- Not a formal attestation; results are advisory only

### Phase 3: Fieldwork

- Evidence collection and testing for the observation period
- Walkthroughs of key processes
- Sampling and testing of control populations
- Interviews with control owners
- Review of system-generated evidence (logs, reports, dashboards)

### Phase 4: Reporting

- Auditor drafts the report including opinion, system description, and test results
- Management reviews for factual accuracy
- Management writes the assertion letter
- Final report issued with CPA firm's opinion
- Report distribution per NDA and restricted use terms

## Evidence Requirements by Trust Services Category

### CC1 — Control Environment

| Criteria | Typical Evidence |
|----------|-----------------|
| CC1.1 — COSO integrity/ethics | Code of conduct, ethics policy, acknowledgment records |
| CC1.2 — Board oversight | Board/committee meeting minutes, charter, independence documentation |
| CC1.3 — Management structure | Organizational chart, reporting lines, job descriptions |
| CC1.4 — Competence commitment | Training programs, certifications, performance reviews |
| CC1.5 — Accountability | Role definitions, RACI matrices, disciplinary policy |

### CC2 — Communication and Information

| Criteria | Typical Evidence |
|----------|-----------------|
| CC2.1 — Internal information | Internal communication records, policy distribution logs |
| CC2.2 — Internal communication | Security awareness training records, completion rates, phishing test results |
| CC2.3 — External communication | Customer-facing security documentation, status pages, incident notifications |

### CC3 — Risk Assessment

| Criteria | Typical Evidence |
|----------|-----------------|
| CC3.1 — Risk objectives | Documented risk appetite, risk management policy |
| CC3.2 — Risk identification | Risk register, risk assessment methodology and results |
| CC3.3 — Fraud risk | Fraud risk assessment, anti-fraud controls |
| CC3.4 — Change impact | Change impact assessments, risk re-evaluations |

### CC4 — Monitoring Activities

| Criteria | Typical Evidence |
|----------|-----------------|
| CC4.1 — Monitoring controls | Internal audit reports, control self-assessments, metrics dashboards |
| CC4.2 — Deficiency communication | Finding tracking, management reporting, remediation evidence |

### CC5 — Control Activities

| Criteria | Typical Evidence |
|----------|-----------------|
| CC5.1 — Control selection | Control framework mapping, risk-to-control matrix |
| CC5.2 — Technology controls | System configurations, automated control evidence |
| CC5.3 — Policy deployment | Procedure documents, approval workflows, standard operating procedures |

### CC6 — Logical and Physical Access

| Criteria | Typical Evidence |
|----------|-----------------|
| CC6.1 — Access controls | Access control policy, RBAC configuration, access matrices |
| CC6.2 — Access provisioning | Onboarding workflows, access request tickets, approval records |
| CC6.3 — Access removal | Offboarding checklists, termination evidence, access removal tickets |
| CC6.4 — Physical access | Badge access logs, visitor logs, data center access records |
| CC6.5 — Access deregistration | Periodic access reviews, recertification evidence |
| CC6.6 — Access restrictions | Least privilege evidence, privileged access management logs |
| CC6.7 — Data transmission | Encryption in transit evidence (TLS configs), VPN configurations |
| CC6.8 — Malware prevention | Endpoint protection deployment, malware scan results |

### CC7 — System Operations

| Criteria | Typical Evidence |
|----------|-----------------|
| CC7.1 — Vulnerability management | Vulnerability scan reports, patching records, remediation timelines |
| CC7.2 — Anomaly monitoring | SIEM dashboards, alert configurations, monitoring tool screenshots |
| CC7.3 — Change evaluation | Change advisory board records, change risk assessments |
| CC7.4 — Incident response | Incident tickets, postmortem reports, IR plan and test results |
| CC7.5 — Incident recovery | Recovery procedures, RTO/RPO evidence, communication records |

### CC8 — Change Management

| Criteria | Typical Evidence |
|----------|-----------------|
| CC8.1 — Change management | Change management policy, change request tickets, approval records, QA test results, UAT sign-offs, deployment approvals, emergency change procedures |

### CC9 — Risk Mitigation

| Criteria | Typical Evidence |
|----------|-----------------|
| CC9.1 — Risk mitigation | Business continuity plans, insurance certificates |
| CC9.2 — Vendor management | Vendor risk assessments, contracts, SLAs, SOC reports from vendors |

### A1 — Availability (if in scope)

| Criteria | Typical Evidence |
|----------|-----------------|
| A1.1 — Capacity management | Capacity planning documents, auto-scaling configurations |
| A1.2 — Recovery objectives | BCP/DR plans, documented RTO/RPO targets |
| A1.3 — Recovery testing | DR test results, failover test documentation, lessons learned |

## Exceptions and Qualified Opinions

### Types of Opinions

| Opinion | Meaning |
|---------|---------|
| Unqualified | Controls are suitably designed and operating effectively; any exceptions are isolated and not pervasive |
| Qualified | Controls are generally effective but one or more exceptions were identified |
| Adverse | Significant or pervasive control failures; controls are not effective |
| Disclaimer | Auditor unable to obtain sufficient evidence to form an opinion |

### Exception Handling
- Exceptions are individual instances where a control did not operate as designed
- A small number of exceptions does not automatically result in a qualified opinion
- Auditors assess whether exceptions are isolated or systemic
- Management may provide context or compensating controls for noted exceptions
- Repeated exceptions across audit periods indicate systemic issues

## Bridge Letters (Gap Letters)

- Cover the period between the end of one SOC 2 report and the start of the next
- Management assertion that no material changes occurred during the gap
- Not an attestation; signed by management, not the auditor
- Commonly requested by customers during procurement
- Should be as brief as possible (typically 1-2 pages)
- Address: no material changes to controls, no known breaches, no system changes affecting TSC

## SOC 2+

SOC 2+ reports map additional framework criteria alongside Trust Services Criteria:

| Additional Framework | Use Case |
|---------------------|----------|
| HIPAA | Healthcare data processors |
| CSA CCM | Cloud security (CSA STAR) |
| ISO 27001 | International customers requiring ISO mapping |
| NIST CSF | Federal or regulated customers |
| NIST 800-171 | CUI handling (DoD supply chain) |

SOC 2+ does not replace the additional framework's certification or attestation but demonstrates alignment and reduces audit fatigue.

## Management Assertion and System Description

### Management Assertion
- Written statement by management that the system description is fairly presented
- Asserts controls are suitably designed (Type I) and operating effectively (Type II)
- Included as Section I of the SOC 2 report
- Must be signed by an authorized officer of the service organization

### System Description (Section III)
Must include:
- Services provided and system boundaries
- Principal service commitments and system requirements
- Components: infrastructure, software, people, procedures, data
- Subservice organizations and the carve-out/inclusive method
- Complementary user entity controls (CUECs)
- Relevant aspects of the control environment
- Significant changes during the period

## Report Distribution and NDA Requirements

- SOC 2 reports are restricted-use documents
- Distribution limited to management, user entities, and their auditors
- Typically require an NDA before sharing
- SOC 3 (general-use report) can be freely distributed as a summary
- Reports should not be posted publicly
- Auditors may require consent before report is shared with specific parties

## Common Deficiencies and Remediation

| Area | Common Deficiency | Remediation |
|------|-------------------|-------------|
| Access Reviews | Not performed quarterly or insufficiently documented | Automate reviews, enforce cadence, document evidence |
| Change Management | Missing approvals or testing evidence | Enforce SDLC gates, require peer review |
| Logging/Monitoring | Incomplete log coverage or no alert response | Deploy SIEM, define alert playbooks |
| Vendor Management | Missing vendor risk assessments | Implement vendor management program, collect SOC reports |
| Incident Response | IR plan not tested annually | Conduct tabletop exercises, document results |
| Encryption | Data at rest not encrypted | Enable encryption (AES-256), document key management |
| Backup/Recovery | DR plan not tested | Perform annual DR test, document results and lessons learned |

## Typical Timeline and Cost

### Timeline

| Phase | Duration |
|-------|----------|
| Scoping and engagement | 2-4 weeks |
| Readiness assessment (optional) | 4-8 weeks |
| Type II observation period | 6-12 months |
| Fieldwork | 4-8 weeks |
| Report drafting and review | 2-4 weeks |
| **Total (including observation)** | **9-18 months for first report** |

### Cost Ranges

| Factor | Range |
|--------|-------|
| Readiness assessment | $15,000 - $40,000 |
| Type I audit | $20,000 - $60,000 |
| Type II audit | $30,000 - $100,000+ |
| Additional TSC categories | $5,000 - $15,000 each |
| SOC 2+ additional criteria | $10,000 - $25,000 per framework |

Costs vary significantly by organization size, complexity, number of TSC categories, and auditor firm.

## Key References

- AICPA Trust Services Criteria (2017, with 2022 revisions)
- AICPA AT-C Section 205 (Examination Engagements)
- AICPA SOC 2 Reporting Guide
- AICPA System Description Guide
