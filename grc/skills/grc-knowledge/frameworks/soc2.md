# SOC 2 — Trust Services Criteria Reference

## Overview

SOC 2 (System and Organization Controls 2) is an attestation framework developed by the **AICPA** (American Institute of Certified Public Accountants) under the **SSAE 18** (Statement on Standards for Attestation Engagements No. 18) standard. It evaluates a service organization's controls relevant to the **Trust Services Criteria (TSC)**, codified in the **2017 Trust Services Criteria** (TSP Section 100).

SOC 2 reports are restricted-use documents intended for customers, regulators, and business partners who need assurance that a service organization operates with adequate controls over its systems and data.

**Key characteristics**:
- Applies to **service organizations** (SaaS providers, data centers, managed service providers, etc.)
- Engagement performed by a licensed **CPA firm**
- Based on **COSO 2013** internal control framework (the CC-series criteria map directly to COSO principles)
- Criteria are **principle-based**, not prescriptive — the organization defines its own controls to satisfy each criterion
- Management describes the system in a **system description** (using DC Section 200 guidelines)

---

## Five Trust Service Categories

| Category | Code | Required? | Scope |
|----------|------|-----------|-------|
| **Security** | CC (Common Criteria) | Always required | Protection against unauthorized access (logical and physical) |
| **Availability** | A | Optional | System is available for operation and use as committed or agreed |
| **Processing Integrity** | PI | Optional | System processing is complete, valid, accurate, timely, and authorized |
| **Confidentiality** | C | Optional | Information designated as confidential is protected as committed or agreed |
| **Privacy** | P | Optional | Personal information is collected, used, retained, disclosed, and disposed of in conformity with commitments and criteria |

Security (Common Criteria) is the foundation of every SOC 2 report. The additional categories are selected based on the nature of the service and customer expectations.

---

## Common Criteria (CC-Series) — Security

The CC-series criteria are mandatory in every SOC 2 engagement. They are organized into nine groups aligned with the COSO 2013 principles.

### CC1 — Control Environment

| Criteria | Description |
|----------|-------------|
| CC1.1 | The entity demonstrates a commitment to integrity and ethical values. |
| CC1.2 | The board of directors demonstrates independence from management and exercises oversight of the development and performance of internal control. |
| CC1.3 | Management establishes, with board oversight, structures, reporting lines, and appropriate authorities and responsibilities in the pursuit of objectives. |
| CC1.4 | The entity demonstrates a commitment to attract, develop, and retain competent individuals in alignment with objectives. |
| CC1.5 | The entity holds individuals accountable for their internal control responsibilities in the pursuit of objectives. |

### CC2 — Communication and Information

| Criteria | Description |
|----------|-------------|
| CC2.1 | The entity obtains or generates and uses relevant, quality information to support the functioning of internal control. |
| CC2.2 | The entity internally communicates information, including objectives and responsibilities for internal control, necessary to support the functioning of internal control. |
| CC2.3 | The entity communicates with external parties regarding matters affecting the functioning of internal control. |

### CC3 — Risk Assessment

| Criteria | Description |
|----------|-------------|
| CC3.1 | The entity specifies objectives with sufficient clarity to enable the identification and assessment of risks relating to objectives. |
| CC3.2 | The entity identifies risks to the achievement of its objectives across the entity and analyzes risks as a basis for determining how the risks should be managed. |
| CC3.3 | The entity considers the potential for fraud in assessing risks to the achievement of objectives. |
| CC3.4 | The entity identifies and assesses changes that could significantly impact the system of internal control. |

### CC4 — Monitoring Activities

| Criteria | Description |
|----------|-------------|
| CC4.1 | The entity selects, develops, and performs ongoing and/or separate evaluations to ascertain whether the components of internal control are present and functioning. |
| CC4.2 | The entity evaluates and communicates internal control deficiencies in a timely manner to those parties responsible for taking corrective action, including senior management and the board of directors, as appropriate. |

### CC5 — Control Activities

| Criteria | Description |
|----------|-------------|
| CC5.1 | The entity selects and develops control activities that contribute to the mitigation of risks to the achievement of objectives to acceptable levels. |
| CC5.2 | The entity also selects and develops general control activities over technology to support the achievement of objectives. |
| CC5.3 | The entity deploys control activities through policies that establish what is expected and in procedures that put policies into action. |

### CC6 — Logical and Physical Access Controls

| Criteria | Description |
|----------|-------------|
| CC6.1 | The entity implements logical access security software, infrastructure, and architectures over protected information assets to protect them from security events to meet the entity's objectives. |
| CC6.2 | Prior to issuing system credentials and granting system access, the entity registers and authorizes new internal and external users whose access is administered by the entity. For those users whose access is administered by the entity, user system credentials are removed when user access is no longer authorized. |
| CC6.3 | The entity authorizes, modifies, or removes access to data, software, functions, and other protected information assets based on roles, responsibilities, or the system design and changes, giving consideration to the concepts of least privilege and segregation of duties, to meet the entity's objectives. |
| CC6.4 | The entity restricts physical access to facilities and protected information assets (for example, data center facilities, backup media storage, and other sensitive locations) to authorized personnel to meet the entity's objectives. |
| CC6.5 | The entity discontinues logical and physical protections over physical assets only after the ability to read or recover data and software from those assets has been diminished and is no longer required to meet the entity's objectives. |
| CC6.6 | The entity implements logical access security measures to protect against threats from sources outside its system boundaries. |
| CC6.7 | The entity restricts the transmission, movement, and removal of information to authorized internal and external users and processes, and protects it during transmission, movement, or removal to meet the entity's objectives. |
| CC6.8 | The entity implements controls to prevent or detect and act upon the introduction of unauthorized or malicious software to meet the entity's objectives. |

### CC7 — System Operations

| Criteria | Description |
|----------|-------------|
| CC7.1 | To meet its objectives, the entity uses detection and monitoring procedures to identify (1) changes to configurations that result in the introduction of new vulnerabilities, and (2) susceptibilities to newly discovered vulnerabilities. |
| CC7.2 | The entity monitors system components and the operation of those components for anomalies that are indicative of malicious acts, natural disasters, and errors affecting the entity's ability to meet its objectives; anomalies are analyzed to determine whether they represent security events. |
| CC7.3 | The entity evaluates security events to determine whether they could or have resulted in a failure of the entity to meet its objectives (security incidents) and, if so, takes actions to prevent or address such failures. |
| CC7.4 | The entity responds to identified security incidents by executing a defined incident response program to understand, contain, remediate, and communicate security incidents, as appropriate. |
| CC7.5 | The entity identifies, develops, and implements activities to recover from identified security incidents. |

### CC8 — Change Management

| Criteria | Description |
|----------|-------------|
| CC8.1 | The entity authorizes, designs, develops or acquires, configures, documents, tests, approves, and implements changes to infrastructure, data, software, and procedures to meet its objectives. |

### CC9 — Risk Mitigation

| Criteria | Description |
|----------|-------------|
| CC9.1 | The entity identifies, selects, and develops risk mitigation activities for risks arising from potential business disruptions. |
| CC9.2 | The entity assesses and manages risks associated with vendors and business partners. |

---

## Additional Criteria by Trust Service Category

### Availability (A-Series)

| Criteria | Description |
|----------|-------------|
| A1.1 | The entity maintains, monitors, and evaluates current processing capacity and use of system components (infrastructure, data, and software) to manage capacity demand and to enable the implementation of additional capacity to help meet its objectives. |
| A1.2 | The entity authorizes, designs, develops or acquires, implements, operates, approves, maintains, and monitors environmental protections, software, data backup processes, and recovery infrastructure to meet its objectives. |
| A1.3 | The entity tests recovery plan procedures supporting system recovery to meet its objectives. |

### Processing Integrity (PI-Series)

| Criteria | Description |
|----------|-------------|
| PI1.1 | The entity obtains or generates, uses, and communicates relevant, quality information regarding the objectives related to processing, including definitions of data processed and product and service specifications, to support the use of products and services. |
| PI1.2 | The entity implements policies and procedures over system inputs, including controls over completeness and accuracy, to result in products, services, and reporting to meet the entity's objectives. |
| PI1.3 | The entity implements policies and procedures over system processing to result in products, services, and reporting to meet the entity's objectives. |
| PI1.4 | The entity implements policies and procedures to make available or deliver output completely, accurately, and timely in accordance with specifications to meet the entity's objectives. |
| PI1.5 | The entity implements policies and procedures to store inputs, items in processing, and outputs completely, accurately, and timely in accordance with system specifications to meet the entity's objectives. |

### Confidentiality (C-Series)

| Criteria | Description |
|----------|-------------|
| C1.1 | The entity identifies and maintains confidential information to meet the entity's objectives related to confidentiality. |
| C1.2 | The entity disposes of confidential information to meet the entity's objectives related to confidentiality. |

### Privacy (P-Series)

| Criteria | Description |
|----------|-------------|
| P1.1 | The entity provides notice to data subjects about its privacy practices to meet the entity's objectives related to privacy. |
| P1.2 | The entity communicates choices available regarding the collection, use, retention, disclosure, and disposal of personal information to data subjects and obtains implicit or explicit consent. |
| P2.1 | The entity collects personal information consistent with the entity's objectives related to privacy. |
| P3.1 | The entity collects personal information only for the purposes identified in the notice. |
| P3.2 | The entity's use of personal information is limited to activities consistent with the entity's objectives related to privacy. |
| P4.1 | The entity discloses personal information to third parties with the explicit consent of data subjects, and such disclosure is consistent with the entity's objectives related to privacy. |
| P4.2 | The entity's disclosures of personal information are limited to third parties who have agreements with the entity to protect personal information consistent with the entity's objectives. |
| P4.3 | The entity obtains privacy commitments from vendors and other third parties who have access to personal information to meet the entity's objectives related to privacy. |
| P5.1 | The entity grants identified and authenticated data subjects the ability to access their stored personal information for review and, upon request, provides such information to data subjects to meet the entity's objectives related to privacy. |
| P5.2 | The entity corrects, amends, or appends personal information based on information provided by data subjects and communicates such corrections, amendments, or appendments to third parties to meet the entity's objectives related to privacy. |
| P6.1 | The entity discloses personal information to third parties who are authorized and have agreed to the entity's privacy policies, only for the purposes identified in the notice. |
| P6.2 | The entity creates, receives, and retains records of detected or reported unauthorized disclosures of personal information to meet the entity's objectives related to privacy. |
| P6.3 | The entity obtains commitments from vendors and other third parties who handle personal information, that they will notify the entity of actual or suspected unauthorized disclosures of personal information. |
| P6.4 | The entity obtains commitments from vendors and other third parties who handle personal information, that they will notify affected data subjects and relevant authorities of confirmed unauthorized disclosures. |
| P6.5 | The entity provides a mechanism for data subjects to file complaints or inquiries regarding their personal information and responds to such complaints or inquiries in a timely manner. |
| P7.1 | The entity collects and maintains accurate, up-to-date, complete, and relevant personal information to meet the entity's objectives related to privacy. |
| P8.1 | The entity retains personal information consistent with the entity's objectives related to privacy. |

---

## SOC 2 Report Types

| Attribute | Type I | Type II |
|-----------|--------|---------|
| **Scope** | Design of controls at a point in time | Design and operating effectiveness over a period |
| **Observation period** | Single date (snapshot) | Minimum 3 months (6-12 months recommended); typically 12 months |
| **Auditor testing** | Inquiry and inspection only | Inquiry, inspection, observation, and re-performance |
| **Maturity signal** | Suitable for first-time reports or new systems | Industry standard; expected by enterprise customers |
| **Common use** | Demonstrate control design before a full audit cycle | Provide ongoing assurance of operating effectiveness |

Organizations typically start with a Type I, then transition to Type II for subsequent reporting periods.

---

## SOC 2+ Reports

A **SOC 2+** report layers additional frameworks or regulatory criteria alongside the Trust Services Criteria within a single engagement. The auditor tests the SOC 2 criteria plus the supplemental criteria simultaneously.

**Common SOC 2+ combinations**:

| Additional Framework | Use Case |
|---------------------|----------|
| HITRUST CSF | Healthcare SaaS, business associate agreements |
| ISO 27001 Annex A | International customers requiring ISO alignment |
| CSA CCM v4 | Cloud service providers seeking STAR attestation |
| NIST 800-53 | Federal customers, FedRAMP readiness |
| NIST Cybersecurity Framework | Cross-industry risk management alignment |
| Custom criteria | Specific regulatory or contractual requirements |

The SOC 2+ approach reduces audit fatigue by consolidating multiple assessments into a single engagement with one auditor.

---

## SOC Report Sections

Every SOC 2 report contains four primary sections:

| Section | Author | Contents |
|---------|--------|----------|
| **Section I — Management Assertion** | Service organization management | Assertion that the system description is fairly presented and controls are suitably designed (Type I) / suitably designed and operating effectively (Type II) |
| **Section II — Independent Service Auditor's Report** | CPA firm (auditor) | Auditor's opinion: unqualified, qualified, adverse, or disclaimer of opinion |
| **Section III — System Description** | Service organization management | Infrastructure, software, people, procedures, data; boundaries of the system; applicable trust service categories; complementary controls |
| **Section IV — Applicable Trust Services Criteria, Related Controls, Tests of Controls, and Results of Tests** | CPA firm (auditor) | Each criterion, the control(s) addressing it, tests performed (Type II), and test results including any exceptions |

Some reports include a **Section V** with other information provided by the service organization (e.g., future plans, responses to exceptions). This section is not covered by the auditor's opinion.

---

## SOC 1 vs SOC 2 vs SOC 3

| Attribute | SOC 1 (SSAE 18 / ISAE 3402) | SOC 2 (SSAE 18) | SOC 3 (SSAE 18) |
|-----------|------------------------------|------------------|------------------|
| **Focus** | Controls relevant to user entities' financial reporting (ICFR) | Controls relevant to security, availability, processing integrity, confidentiality, privacy | Same as SOC 2 |
| **Standard** | AT-C Section 320 | AT-C Section 205 + TSP Section 100 | AT-C Section 205 + TSP Section 100 |
| **Audience** | Restricted (customers, auditors) | Restricted (customers, auditors, regulators) | General use (public) |
| **Detail level** | Full control descriptions and test results | Full control descriptions and test results | Summary-level opinion only; no control detail |
| **Report types** | Type I and Type II | Type I and Type II | No type distinction (always period-based) |
| **Common use** | Payroll processors, financial SaaS, loan servicers | SaaS platforms, data centers, managed services | Marketing and website trust seal |

---

## Bridge Letters (Gap Coverage Letters)

A **bridge letter** (also called a **gap letter**) is a written assertion from service organization management covering the period between the end of the most recent SOC 2 report observation period and the current date.

**Key characteristics**:
- Not an auditor-attested document; it is a management representation
- Typically a 1-2 page letter signed by an executive (CISO, VP of Engineering, or CEO)
- Covers the "gap period" (e.g., if a Type II report covers Jan 1 - Dec 31, 2025, a bridge letter would cover Jan 1, 2026 through the date of the letter)
- Asserts that no material changes have occurred to the system or its controls since the report period ended
- Discloses any significant changes, incidents, or new subservice organizations during the gap period

**When bridge letters are needed**:
- Customer procurement teams requesting current-state assurance
- When the next Type II report is still in progress
- Contract or regulatory requirements specifying maximum gap duration (typically 3-6 months)

---

## Common Evidence by Criteria Category

| CC Group | Typical Evidence |
|----------|-----------------|
| CC1 (Control Environment) | Code of conduct, org chart, board/committee meeting minutes, job descriptions, background check policy, performance evaluations |
| CC2 (Communication & Information) | Internal communications, policy distribution records, security awareness training completion, external-facing SLAs and privacy notices |
| CC3 (Risk Assessment) | Risk assessment reports, risk register, fraud risk assessment, change impact analyses |
| CC4 (Monitoring) | Internal audit reports, control self-assessments, management review meeting minutes, exception/deficiency tracking |
| CC5 (Control Activities) | Policy documents, procedure runbooks, IT general controls documentation, segregation of duties matrix |
| CC6 (Access Controls) | User access reviews, provisioning/deprovisioning tickets, MFA configuration, firewall rules, encryption standards, physical access logs, media disposal records |
| CC7 (System Operations) | Vulnerability scan reports, SIEM/log monitoring dashboards, IDS/IPS configurations, incident response plan and post-incident reports, penetration test results |
| CC8 (Change Management) | Change request tickets, CAB meeting minutes, deployment logs, code review approvals, rollback procedures |
| CC9 (Risk Mitigation) | BCP/DR plans, DR test results, vendor risk assessments, vendor security questionnaires, third-party audit reports |

| Additional Category | Typical Evidence |
|---------------------|-----------------|
| Availability (A) | Uptime monitoring dashboards, capacity planning documents, backup configuration and restoration test results, DR test reports |
| Processing Integrity (PI) | Data validation rules, reconciliation reports, error handling logs, QA/testing results, SLA performance metrics |
| Confidentiality (C) | Data classification policy, confidential data inventory, encryption-at-rest and in-transit configurations, data retention/disposal schedules and records |
| Privacy (P) | Privacy notice (posted), consent records, data subject access request (DSAR) logs, data processing agreements, privacy impact assessments, breach notification procedures |

---

## Complementary Controls

SOC 2 reports frequently identify controls that must be implemented by parties other than the service organization itself.

### Complementary User Entity Controls (CUECs)

CUECs are controls that the **customer** (user entity) is responsible for implementing. They are listed in Section III of the SOC 2 report.

**Common CUECs**:

| Area | Example CUEC |
|------|-------------|
| Access management | Customer is responsible for managing its own user accounts, including timely deprovisioning of terminated employees |
| Authentication | Customer is responsible for enforcing MFA for its users accessing the service |
| Data classification | Customer is responsible for classifying data prior to uploading to the system |
| Monitoring | Customer is responsible for reviewing audit logs available within the platform |
| Incident notification | Customer is responsible for promptly notifying the service organization of suspected security incidents |
| Backup verification | Customer is responsible for verifying its data backups and testing restoration |

Failure to implement CUECs can undermine the effectiveness of the service organization's controls and may affect the customer's own audit posture.

### Complementary Subservice Organization Controls (CSOCs)

CSOCs are controls that must be implemented by **subservice organizations** (e.g., AWS, Azure, GCP) on which the service organization depends.

**Subservice organization handling methods**:

| Method | Description | Impact on Report |
|--------|-------------|-----------------|
| **Inclusive method** | Subservice organization's controls are included in the system description and tested by the auditor | Comprehensive but requires subservice organization cooperation |
| **Carve-out method** | Subservice organization's controls are excluded from the system description; only the service organization's monitoring of the subservice organization is tested | Most common; CSOCs are listed as assumptions |

When the carve-out method is used, the report lists CSOCs that must be in place at the subservice organization. The service organization typically satisfies this by obtaining the subservice organization's own SOC 2 report and reviewing it annually.

---

## COSO Alignment

The CC-series criteria map directly to the 17 principles of the **COSO 2013 Internal Control — Integrated Framework**:

| CC Group | COSO Component | COSO Principles |
|----------|---------------|-----------------|
| CC1.1 - CC1.5 | Control Environment | Principles 1-5 |
| CC2.1 - CC2.3 | Information & Communication | Principles 13-15 |
| CC3.1 - CC3.4 | Risk Assessment | Principles 6-9 |
| CC4.1 - CC4.2 | Monitoring Activities | Principles 16-17 |
| CC5.1 - CC5.3 | Control Activities | Principles 10-12 |
| CC6 - CC9 | Additional criteria specific to TSC | Not directly mapped to COSO principles (TSC-specific supplemental criteria for IT-related objectives) |

---

## Scoping and Readiness Considerations

**Pre-audit readiness assessment checklist**:
1. Define the system boundary (which products, services, and infrastructure are in scope)
2. Select applicable Trust Service Categories beyond Security
3. Identify all subservice organizations and determine carve-out vs. inclusive method
4. Perform a gap assessment against the applicable criteria
5. Document all controls and map them to criteria (controls may satisfy multiple criteria)
6. Prepare the system description per DC Section 200 requirements
7. Collect evidence for each control (see Common Evidence table above)
8. Identify and document CUECs and CSOCs
9. Conduct an internal readiness review or pre-assessment
10. Remediate gaps before the observation period begins (for Type II)

**Common audit exceptions**:
- Access reviews not performed at the documented frequency
- Terminated users not deprovisioned within the documented SLA
- Change management procedures bypassed without documented approval
- Incomplete or missing evidence for annual control activities (risk assessments, BCP tests)
- Vendor risk assessments not completed for all in-scope third parties
