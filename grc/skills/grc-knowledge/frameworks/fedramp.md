# FedRAMP (Federal Risk and Authorization Management Program)

## Overview

FedRAMP is a U.S. government-wide program that provides a standardized approach to security authorizations for Cloud Service Offerings (CSOs). Established in 2011 and codified by the FedRAMP Authorization Act (part of the FY2023 NDAA), FedRAMP ensures that cloud products and services used by federal agencies meet consistent security requirements based on NIST SP 800-53.

**Governing Body**: General Services Administration (GSA) FedRAMP Program Management Office (PMO)

**Legal Authority**: FedRAMP Authorization Act (44 U.S.C. 3607-3616), OMB Memoranda (A-130, M-23-16), FISMA

**Core Principle**: "Do once, use many" -- a CSP achieves authorization once and that authorization package can be reused by any federal agency, eliminating redundant assessments.

### Key Organizational Roles

| Entity | Role |
|--------|------|
| **GSA FedRAMP PMO** | Program governance, baseline maintenance, marketplace management, process oversight |
| **JAB** | Joint Authorization Board (CIOs of DoD, DHS, GSA); issued P-ATOs for high-visibility CSOs. **Dissolved May 2024**; governance functions transitioned to the FedRAMP Board per the FedRAMP Authorization Act. Legacy P-ATOs remain valid. |
| **Authorizing Official (AO)** | Senior agency official who accepts risk and grants an Agency ATO |
| **3PAO** | Third Party Assessment Organization; conducts independent security assessments |
| **CSP** | Cloud Service Provider; implements controls and maintains authorization |
| **A2LA** | American Association for Laboratory Accreditation; accredits 3PAOs |

## FedRAMP Rev 5 Transition

FedRAMP transitioned from NIST 800-53 Rev 4 to Rev 5 baselines. Key changes:

- Adoption of NIST SP 800-53 Rev 5 and SP 800-53B as the control catalog and baseline source
- Introduction of the PT (PII Processing and Transparency) and SR (Supply Chain Risk Management) families
- Consolidation of some control enhancements and withdrawal of others
- Revised parameter values aligned with current threat landscape
- Updated SSP, SAR, and POA&M templates to reflect Rev 5 structure
- CSPs with existing authorizations must transition to Rev 5 baselines per PMO-published timelines

## Baselines

FedRAMP defines four baselines derived from NIST SP 800-53B, with additional FedRAMP-specific controls and parameter constraints layered on top.

### Baseline Summary

| Baseline | FIPS 199 Impact | Total Controls (FedRAMP) | Use Case |
|----------|----------------|--------------------------|----------|
| **Low** | Low (C, I, A) | ~158 | Low-risk data; publicly available information |
| **Moderate** | Moderate (C, I, A) | ~322 | Controlled unclassified information (CUI); most federal workloads |
| **High** | High (C, I, A) | ~410 | Law enforcement, emergency services, financial, health data |
| **LI-SaaS** | Low Impact SaaS | ~158 (tailored Low) | Low-impact SaaS not storing PII beyond login credentials |

### Baseline Selection Guidance

- **Moderate** is by far the most common baseline; roughly 80% of FedRAMP authorizations are Moderate.
- **High** applies to systems processing high-impact data (FIPS 199 High for any of C, I, or A). Typical for law enforcement, healthcare, and financial systems.
- **Low** is appropriate for systems handling only publicly releasable data with minimal confidentiality needs.
- **LI-SaaS** (Low Impact SaaS) is a tailored Low baseline for SaaS products that store no PII beyond that needed for login. It uses the FedRAMP Low baseline with additional tailoring and has a streamlined authorization process.

### Control Family Distribution by Baseline

| Family | Low | Moderate | High |
|--------|-----|----------|------|
| AC (Access Control) | 17 | 39 | 52 |
| AT (Awareness & Training) | 4 | 5 | 6 |
| AU (Audit & Accountability) | 10 | 16 | 20 |
| CA (Assessment & Authorization) | 7 | 10 | 11 |
| CM (Configuration Management) | 7 | 14 | 18 |
| CP (Contingency Planning) | 6 | 13 | 16 |
| IA (Identification & Authentication) | 9 | 16 | 19 |
| IR (Incident Response) | 7 | 11 | 15 |
| MA (Maintenance) | 4 | 7 | 9 |
| MP (Media Protection) | 4 | 8 | 9 |
| PE (Physical & Environmental) | 12 | 18 | 22 |
| PL (Planning) | 4 | 5 | 6 |
| PM (Program Management) | 10 | 16 | 16 |
| PS (Personnel Security) | 7 | 8 | 8 |
| PT (PII Processing) | 4 | 7 | 8 |
| RA (Risk Assessment) | 5 | 7 | 8 |
| SA (System & Services Acquisition) | 11 | 20 | 25 |
| SC (System & Communications) | 12 | 29 | 40 |
| SI (System & Information Integrity) | 9 | 14 | 19 |
| SR (Supply Chain Risk Mgmt) | 7 | 12 | 14 |

## FedRAMP-Specific Controls and Parameters

FedRAMP baselines are **not** identical to NIST SP 800-53B baselines. FedRAMP adds controls, control enhancements, and prescriptive parameter values beyond what NIST specifies. These additions reflect federal cloud-specific risk considerations.

### FedRAMP Additional Requirements Beyond NIST

| Area | FedRAMP Addition | Notes |
|------|------------------|-------|
| Integrated Inventory (CM-8) | CSP must maintain automated, real-time asset inventory | Includes virtual assets, containers, serverless components |
| FIPS 140 Validation (SC-13) | Cryptographic modules must be FIPS 140-2 or 140-3 validated | Not just "consistent with"; must hold active CMVP certificate |
| US-Person Personnel (PS-6) | Personnel with access to federal data must be US persons or have equivalent background checks | Applies to privileged and non-privileged access |
| Data Location (SA-9(5)) | Data at rest must be stored within the United States | Including backups, replicas, and DR sites |
| Incident Reporting (IR-6) | CISA reporting within 1 hour of incident discovery | Stricter than most agency-specific policies |
| Penetration Testing (CA-8) | Annual penetration test by 3PAO or qualified independent entity | Must cover all High and Moderate attack vectors |
| Continuous Monitoring (CA-7) | Monthly OS/infrastructure scans, monthly web application scans, annual 3PAO assessment | More prescriptive cadence than base NIST |
| CIS/CRM (SA-9) | Customer Responsibility Matrix required for all shared/inherited controls | Not in base NIST; FedRAMP-specific artifact |

### FedRAMP Parameter Values for Key Controls

FedRAMP prescribes specific values where NIST leaves organization-defined parameters (ODPs). These are mandatory and non-negotiable.

| Control | Parameter | FedRAMP Value |
|---------|-----------|---------------|
| **AC-2** | Account inactivity disable | 90 days of inactivity |
| **AC-2(3)** | Auto-disable of temporary, emergency, and inactive accounts | 35 days of inactivity |
| **AC-7** | Consecutive invalid login attempts | 3 consecutive attempts within 15 minutes |
| **AC-7** | Lockout action | Lock account for 30 minutes or until released by admin |
| **AC-11** | Session lock after inactivity | 15 minutes of inactivity |
| **AC-12** | Session termination | 30 minutes of inactivity for non-privileged; 15 minutes for privileged |
| **AU-4** | Audit storage capacity | Sufficient to retain per AU-11 requirements |
| **AU-6** | Audit review frequency | At least weekly |
| **AU-11** | Audit record retention | At least 12 months online, 18 months total (online + offline/archive) |
| **CM-6** | Configuration baseline standard | DISA STIGs (preferred); CIS Benchmarks Level 2 (where STIGs unavailable); vendor hardening guides |
| **IA-4** | Identifier reuse prevention | At least 2 years before reuse |
| **IA-5(1)** | Minimum password length | 12 characters (Moderate/High) |
| **IA-5(1)** | Password complexity | Mix of upper, lower, numeric, special characters |
| **IA-5(1)** | Password lifetime maximum | 60 days |
| **IA-5(1)** | Password reuse prohibition | 24 passwords remembered |
| **RA-5** | Vulnerability scanning frequency (OS/infra) | At least monthly |
| **RA-5** | Vulnerability scanning frequency (web app) | At least monthly |
| **RA-5** | Vulnerability scanning frequency (database) | At least monthly |
| **RA-5** | Vulnerability scanning frequency (container) | At deployment and at least monthly |
| **RA-5(d)** | Remediation timeline (Critical) | 30 days |
| **RA-5(d)** | Remediation timeline (High) | 30 days |
| **RA-5(d)** | Remediation timeline (Moderate) | 90 days |
| **RA-5(d)** | Remediation timeline (Low) | 180 days |
| **SI-2** | Flaw remediation timeline (Critical) | 30 days |
| **SI-2** | Flaw remediation timeline (High) | 30 days |
| **SI-2** | Flaw remediation timeline (Moderate) | 90 days |
| **SI-2** | Flaw remediation timeline (Low) | 180 days |
| **CP-9** | Backup frequency (system-level) | Daily incremental, weekly full |
| **CP-10** | Recovery time objective (RTO) | Defined by CSP per FIPS 199 impact |

## Authorization Paths

### JAB Provisional Authorization (P-ATO)

The JAB P-ATO path was historically for high-visibility, cross-government CSOs expected to be used by multiple agencies. The JAB (CIOs of DoD, DHS, GSA) served as the AO and issued Provisional ATOs. **Note: The JAB was dissolved in May 2024 and its governance functions transitioned to the FedRAMP Board under the FedRAMP Authorization Act. Existing P-ATOs remain valid. The process below describes the historical JAB path for reference.**

**Process Steps:**

| Step | Activity | Typical Duration |
|------|----------|------------------|
| 1 | **FedRAMP Connect** -- CSP submits business case; FedRAMP PMO prioritizes | 1-3 months |
| 2 | **Readiness Assessment** -- 3PAO conducts FedRAMP Ready assessment (optional but strongly recommended) | 4-6 weeks |
| 3 | **Full Security Assessment** -- 3PAO conducts comprehensive assessment per SAP | 3-6 months |
| 4 | **Authorization Package Submission** -- CSP submits SSP, SAR, POA&M to PMO | 2-4 weeks |
| 5 | **PMO Review** -- FedRAMP PMO reviews package, issues review comments | 4-8 weeks |
| 6 | **JAB Review** -- JAB reviews risk posture and makes P-ATO decision | 2-4 weeks |
| 7 | **P-ATO Issuance** -- JAB issues P-ATO letter; CSO listed on Marketplace | 1 week |
| 8 | **Continuous Monitoring** -- Monthly ConMon deliverables to PMO and leveraging agencies | Ongoing |

**Total typical timeline: 6-18 months**

### Agency Authorization (Agency ATO)

An individual agency sponsors the CSP and the agency AO issues the ATO. This is the more common path.

**Process Steps:**

| Step | Activity | Typical Duration |
|------|----------|------------------|
| 1 | **Agency Sponsorship** -- Agency identifies need and agrees to sponsor CSP | 1-2 months |
| 2 | **Readiness Assessment** -- Optional FedRAMP Ready assessment by 3PAO | 4-6 weeks |
| 3 | **Full Security Assessment** -- 3PAO conducts assessment | 3-6 months |
| 4 | **Authorization Package** -- CSP prepares and submits package to agency | 2-4 weeks |
| 5 | **Agency Review** -- Agency security team reviews, may request remediation | 4-12 weeks |
| 6 | **ATO Decision** -- Agency AO issues ATO letter | 1-2 weeks |
| 7 | **FedRAMP PMO Review** -- PMO reviews package for listing on Marketplace | 4-8 weeks |
| 8 | **Marketplace Listing** -- CSO listed as Authorized | 1 week |
| 9 | **Continuous Monitoring** -- Monthly ConMon to sponsoring agency and PMO | Ongoing |

**Total typical timeline: 6-14 months**

### JAB P-ATO vs. Agency ATO Comparison

| Factor | JAB P-ATO | Agency ATO |
|--------|-----------|------------|
| Authorizing Official | JAB (DoD, DHS, GSA CIOs) | Individual Agency AO |
| Scope of Authorization | Government-wide provisional | Single agency (reusable by others) |
| Selection Criteria | FedRAMP Connect prioritization | Agency sponsorship required |
| PMO Review | Before authorization | After authorization |
| ConMon Reporting | To FedRAMP PMO | To sponsoring agency + PMO |
| Best For | High-demand, multi-agency CSOs | Agency-specific or niche CSOs |
| Rigor | Generally higher bar | Varies by agency |

## FedRAMP Marketplace, Connect, and Authorization Statuses

**FedRAMP Marketplace** (marketplace.fedramp.gov) is the authoritative public registry of CSOs, their authorization status, baseline level, authorization type, and 3PAO directory.

**FedRAMP Connect** is the intake and prioritization process for CSPs seeking a JAB P-ATO. CSPs submit a business case demonstrating federal agency demand, FedRAMP Ready status, and unique government-wide applicability. The PMO evaluates and selects CSPs for JAB prioritization periodically.

| Status | Meaning |
|--------|---------|
| **FedRAMP Ready** | 3PAO completed Readiness Assessment Report (RAR); CSP meets minimum requirements for full assessment |
| **In Process** | CSP is actively working toward authorization with a JAB or agency sponsor |
| **Authorized** | ATO or P-ATO granted; CSO is approved for federal use and listed on Marketplace |
| **Revoked** | Authorization withdrawn due to non-compliance or unacceptable risk |

**FedRAMP Ready** requires a 3PAO Readiness Assessment validating: well-defined system boundary, key controls implemented (not just planned), substantially complete SSP, manageable vulnerability scan posture, IR/CP plans in place, and FIPS-validated cryptographic modules.

## Key FedRAMP Documents and Artifacts

| Document | Description | Owner |
|----------|-------------|-------|
| **System Security Plan (SSP)** | Comprehensive control implementation narratives, system architecture, data flows, boundary diagram, interconnections | CSP |
| **Security Assessment Plan (SAP)** | Assessment scope, methodology, rules of engagement, test procedures | 3PAO |
| **Security Assessment Report (SAR)** | Assessment findings, risk ratings, risk exposure tables, recommendations | 3PAO |
| **Plan of Action & Milestones (POA&M)** | Open findings tracker with severity, remediation milestones, status, due dates | CSP |
| **Customer Implementation Summary (CIS)** | Summary of customer-responsible controls for agency review | CSP |
| **Customer Responsibility Matrix (CRM)** | Detailed matrix showing CSP vs. customer responsibility for each control | CSP |
| **Readiness Assessment Report (RAR)** | 3PAO assessment of CSP readiness for full assessment | 3PAO |
| **Significant Change Request (SCR)** | Formal request to modify authorized system boundary or architecture | CSP |
| **Deviation Request (DR)** | Request to accept risk for a finding that cannot be remediated within SLA | CSP |
| **Continuous Monitoring Monthly Report** | Monthly executive summary with scan results, POA&M status, inventory changes | CSP |
| **Policies & Procedures (per family)** | Policy and procedure documents for each NIST 800-53 control family (AC, AT, AU, etc.) | CSP |
| **Digital Identity Worksheet** | Per NIST SP 800-63-3; documents authentication assurance level selection | CSP |
| **Laws and Regulations Template** | Identifies applicable laws, regulations, and standards for the CSO | CSP |
| **OSCAL-formatted SSP** | Machine-readable SSP in NIST OSCAL format (increasingly encouraged) | CSP |

## 3PAO Requirements

### Accreditation

- 3PAOs must be accredited by the **American Association for Laboratory Accreditation (A2LA)** under the FedRAMP 3PAO program.
- Accreditation is based on **ISO/IEC 17020:2012** (Conformity Assessment -- Requirements for Bodies Performing Inspection).
- A2LA conducts initial assessments and periodic surveillance assessments to maintain accreditation.
- 3PAOs must demonstrate competency in NIST SP 800-53, FedRAMP requirements, cloud architecture, and penetration testing.

### 3PAO Responsibilities

| Activity | Frequency | Deliverable |
|----------|-----------|-------------|
| Initial Full Assessment | Once (pre-authorization) | SAP, SAR, POA&M review |
| Annual Assessment | Annually | Updated SAR, POA&M validation |
| Readiness Assessment | Optional (pre-full assessment) | Readiness Assessment Report (RAR) |
| Significant Change Assessment | As needed (per SCR) | Focused SAR addendum |
| Penetration Testing | Annually (included in assessment) | Penetration test report (within SAR) |

### 3PAO Independence

- The 3PAO must be organizationally independent from the CSP.
- The same 3PAO can perform consecutive annual assessments, but agencies may require rotation.
- 3PAO assessors must not have consulting relationships with the CSP they assess.

## Significant Change Request (SCR) Process

A Significant Change Request is required when a CSP makes material changes to an authorized CSO. Significant changes include:

- Changes to system boundary (adding/removing components, services, or interconnections)
- Changes to data flows or data types processed
- Migration to a new infrastructure provider or data center
- Major architecture changes (e.g., monolith to microservices)
- Changes to cryptographic implementations
- Changes to authentication mechanisms
- Addition of new external services or APIs

### SCR Process Steps

1. **CSP submits SCR** to the sponsoring agency (Agency ATO) or FedRAMP PMO (JAB P-ATO)
2. **AO/PMO reviews** the SCR and determines assessment scope
3. **3PAO assesses** impacted controls (focused assessment, not full reassessment)
4. **CSP updates SSP** to reflect changes
5. **AO/PMO approves** the change and updates authorization documentation

Changes that are **not** significant (routine patching, minor configuration changes, staff changes) require documentation in the SSP and monthly ConMon reports but do not require an SCR.

## Continuous Monitoring Requirements

FedRAMP continuous monitoring is more prescriptive than general NIST ISCM guidance. CSPs must adhere to the following cadence:

### Monthly Requirements

| Deliverable | Details |
|-------------|---------|
| Vulnerability Scans (OS/Infrastructure) | Authenticated scans of all OS-level assets; scan results in POA&M |
| Vulnerability Scans (Web Application) | DAST scans of all externally facing web applications |
| Vulnerability Scans (Database) | Authenticated scans of all database instances |
| Vulnerability Scans (Container) | Scan container images at build/deploy and monthly in runtime |
| POA&M Update | Refresh all open items; add new findings; update milestones and statuses |
| Inventory Update | Hardware, software, and virtual asset inventory reconciliation |
| ConMon Summary Report | Executive summary of security posture, scan trends, POA&M aging |

### Quarterly Requirements

| Deliverable | Details |
|-------------|---------|
| Privileged User Access Review | Validate all privileged accounts remain appropriate |
| Network Scan / Architecture Review | Confirm no unauthorized changes to network topology |
| Hardware/Software Inventory Reconciliation | Full reconciliation against CM-8 inventory |

### Annual Requirements

| Deliverable | Details |
|-------------|---------|
| 3PAO Security Assessment | Independent assessment of a subset of controls (typically 1/3 rotation) |
| Penetration Test | Full-scope penetration test by 3PAO |
| Contingency Plan Test | CP test and after-action report |
| Incident Response Plan Test | Tabletop or functional IR exercise |
| Security Awareness Training | All personnel with system access |
| SSP Update | Full refresh of SSP to reflect current state |
| Privacy Impact Assessment | Reassessment if PII processing has changed |

### POA&M Remediation Timelines

| Severity | Remediation SLA | Deviation Request Required If Exceeded |
|----------|----------------|----------------------------------------|
| Critical | 30 days | Yes |
| High | 30 days | Yes |
| Moderate | 90 days | Yes |
| Low | 180 days | Yes |

Findings that cannot be remediated within SLA require a **Deviation Request (DR)** with a risk-based justification. The AO or JAB must approve the DR. Types of DRs include: Risk Adjustment, False Positive, Operational Requirement, and Vendor Dependency.

## Key Differences from Base NIST SP 800-53

| Dimension | NIST SP 800-53 Rev 5 | FedRAMP Rev 5 |
|-----------|----------------------|---------------|
| **Control Counts** | Low: ~150, Moderate: ~304, High: ~392 | Low: ~158, Moderate: ~322, High: ~410 |
| **Additional Controls** | Baseline per 800-53B only | Adds controls and enhancements beyond NIST baselines |
| **Parameters (ODPs)** | Organization-defined (flexible) | Prescriptive values mandated by PMO |
| **Assessment** | Organization selects assessor | Must use A2LA-accredited 3PAO |
| **Authorization** | Agency AO per RMF | JAB P-ATO or Agency ATO with PMO oversight |
| **ConMon Cadence** | Organization-defined | Specific monthly/quarterly/annual requirements |
| **Artifact Templates** | No mandated templates | FedRAMP-provided SSP, SAR, POA&M, CIS/CRM templates |
| **Remediation SLAs** | Organization-defined | 30/30/90/180 days by severity (Critical/High/Moderate/Low) |
| **Data Sovereignty** | No federal requirement | Data must reside within US boundaries |
| **Cryptography** | FIPS 140 "consistent with" | FIPS 140-2/140-3 validated modules required |
| **Incident Reporting** | Per organizational policy | CISA within 1 hour of incident discovery |
| **Supply Chain** | SR family selected per baseline | Enhanced supply chain requirements for cloud context |
| **Marketplace/Reuse** | No reuse mechanism | "Do once, use many" via FedRAMP Marketplace |
| **OSCAL** | Encouraged | Increasingly required for package submissions |

## References

- NIST SP 800-53 Rev 5: Security and Privacy Controls for Information Systems and Organizations
- NIST SP 800-53B: Control Baselines for Information Systems and Organizations
- NIST SP 800-37 Rev 2: Risk Management Framework for Information Systems and Organizations
- NIST SP 800-63-3: Digital Identity Guidelines
- FedRAMP Authorization Act (44 U.S.C. 3607-3616)
- FedRAMP Security Assessment Framework (SAF)
- FedRAMP Continuous Monitoring Strategy Guide
- FedRAMP Significant Change Request Form and Guidance
- FedRAMP Initial Authorization Package Checklist
- FedRAMP OSCAL guides and templates (automate.fedramp.gov)
