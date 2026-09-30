# GRC Document Section Requirements

Required sections and structural elements for major GRC artifacts, per FedRAMP template standards and NIST guidelines. Use this reference to validate document completeness.

## System Security Plan (SSP)

Based on the legacy FedRAMP Rev5 SSP template ("FedRAMP (High, Moderate, Low, LI-SaaS) Baseline System Security Plan"; control implementation statements live in Appendix A). Sections marked with * are critical — omission is a finding.

> **Status (as of Sept 30, 2026):** every legacy FedRAMP template carries a June 23, 2026 LEGACY NOTICE. The Rev5 template remains usable for packages on the Rev5 path until the CR26 deadlines (Rev5 Certification Package rules optional July 4, 2026, required Jan 1, 2027; FedRAMP stops accepting new Rev5 certifications June 11, 2027). Under CR26 the SSP is replaced by the **FedRAMP Certification Package** (FRC-CSO-PKG) delivered against FedRAMP JSON schemas (FRC-CSO-JSN; OSCAL is optional — the OSCAL mandate was dropped by NTC-0009), and Rev5 control documentation moves to **Security Decision Records** (SDR-CSF-CTF statuses: Implemented, Partially Implemented, Planned, Alternative Implementation, Not Applicable).

### Front Matter
- [ ] Title page with system name, CSP name, date, version
- [ ] Document revision history*
- [ ] Table of contents
- [ ] List of tables and figures

### Section 1 — Introduction
- [ ] Template introduction (instructional text deleted in the final version)

### Section 2 — Purpose
- [ ] Purpose of the SSP for this CSO

### Section 3 — System Information*
- [ ] Official system name (matches FedRAMP Marketplace if applicable), abbreviation, FedRAMP Package ID
- [ ] FIPS 199 categorization (Confidentiality, Integrity, Availability) with justification (worksheet in Appendix K)
- [ ] Information types (per NIST 800-60)
- [ ] Cloud service model (IaaS/PaaS/SaaS) and deployment model (public/private/hybrid/community)
- [ ] Operational status

### Section 4 — System Owner*
- [ ] Organization name and point of contact (name, title, email, phone)
- [ ] Authorizing Official identification

### Section 5 — Assignment of Security Responsibility*
- [ ] ISSO/ISSM name, title, contact
- [ ] Other key security roles and responsibilities

### Section 6 — Leveraged FedRAMP-Authorized Services*
- [ ] Every FedRAMP-authorized (CR26: FedRAMP Certified) service the CSO inherits from, with package ID, impact level, and what is inherited

### Section 7 — External Systems and Services Not Having FedRAMP Authorization
- [ ] Table 7.1: every non-authorized external system/service (non-FedRAMP cloud services, corporate shared services, update services for in-boundary software)
- [ ] For each: purpose, data types, direction, and risk/mitigation description
- [ ] ISA/MOU (any CA-3 agreement type) references for interconnections
- [ ] API/data exchange descriptions

### Section 8 — Illustrated Architecture and Narratives*
- [ ] Authorization boundary diagram*
- [ ] Network architecture diagram*
- [ ] Data flow diagram(s)*
- [ ] Narrative describing boundary, components, tenant separation, and admin access paths (must match the diagrams exactly)
- [ ] Types of users (privileged, non-privileged, external) and roles/access levels

### Section 9 — Services, Ports, and Protocols*
- [ ] Ports, protocols, and services table (PP&S) covering every connection

### Section 10 — Cryptographic Modules Implemented for DAR and DIT*
- [ ] Every module protecting federal data at rest and in transit, with CMVP certificate status (detailed in Appendix Q)
- [ ] FIPS 140-3 (active CMVP validation; 140-2 certificates Historical since Sept 22, 2026)

### Section 11 — Separation of Duties
- [ ] Table 11.1: roles, privileges, and how conflicting duties are separated

### Section 12 — SSP Appendices List
- [ ] Every appendix referenced is included

### Appendix A — FedRAMP Security Controls (control implementation)*
- [ ] Control summary for every baseline control with implementation status (Implemented, Partially Implemented, Planned, Alternative Implementation, Not Applicable)
- [ ] Responsibility designation for each control part (CSP, Customer, Shared, Inherited)
- [ ] Every baseline control has a narrative addressing the Five W's (What, Who, How, When, Where)
- [ ] All ODPs filled in with specific values (Legacy FedRAMP Rev5 values in force until CR26 becomes mandatory Jan 1, 2027; CR26 removed most FedRAMP-assigned values)
- [ ] All baseline enhancements addressed
- [ ] Inherited controls identify the source (CSP/infrastructure provider)

### Appendices (legacy Rev5 template, A-Q)
- [ ] Appendix A: FedRAMP Security Controls (one per baseline: LI-SaaS, Low, Moderate, High)
- [ ] Appendix B: Related Acronyms
- [ ] Appendix C: Security Policies and Procedures
- [ ] Appendix D: User Guide
- [ ] Appendix E: Digital Identity Worksheet
- [ ] Appendix F: Rules of Behavior
- [ ] Appendix G: Information System Contingency Plan (ISCP)
- [ ] Appendix H: Configuration Management Plan (CMP)
- [ ] Appendix I: Incident Response Plan (IRP)
- [ ] Appendix J: CIS and CRM Workbook
- [ ] Appendix K: FIPS 199 Worksheet
- [ ] Appendix L: CSO-Specific Required Laws and Regulations
- [ ] Appendix M: Integrated Inventory Workbook
- [ ] Appendix N: Continuous Monitoring Plan
- [ ] Appendix O: POA&M
- [ ] Appendix P: Supply Chain Risk Management Plan (SCRMP)
- [ ] Appendix Q: Cryptographic Modules Table

### Common SSP Deficiencies
- Missing or outdated authorization boundary diagram
- Control narratives that restate requirements instead of describing implementation
- Incomplete ports/protocols/services table
- Missing interconnection details for API integrations
- ODP values left as TBD or not matching FedRAMP-required values (legacy Rev5)
- Responsibility designations missing or inconsistent
- Appendices referenced but not included

---

## Plan of Action & Milestones (POA&M)

The official legacy FedRAMP Rev5 POA&M template is SSP Appendix O, with columns: POAM ID, Controls, Weakness Name, Weakness Description, Weakness Detector Source, Weakness Source Identifier, Asset Identifier, Point of Contact, Resources Required, Remediation Plan, Original Detection Date, Scheduled Completion Date, Status Date, Vendor Dependency, Last Vendor Check-in Date, Vendor Dependent Product Name, Original Risk Rating, Adjusted Risk Rating, Risk Adjustment, False Positive, Operational Requirement, Deviation Rationale, Supporting Documents, Comments, BOD 22-01 tracking, BOD 22-01 Due Date, CVE (KEV tracking now falls under BOD 26-04). The generalized field list below applies across frameworks. **CR26:** the POA&M is not a CR26 construct on the CSP side (agencies still keep POA&Ms); unremediated items become **Accepted Vulnerabilities** reported in each quarterly OCR, with fields per VER-RPT-AVI (tracking ID, detection time/source, evaluation time, internet-reachable, likely-exploitable, PAIN rating, rationale).

### Required Columns/Fields*

| # | Field | Description | Required |
|---|-------|-------------|----------|
| 1 | POA&M ID | Unique identifier (e.g., V-001, POA&M-2024-001) | Yes* |
| 2 | Weakness Name/Title | Brief descriptive title | Yes* |
| 3 | Weakness Description | Detailed description of the finding | Yes* |
| 4 | Point of Contact | Responsible individual or role | Yes* |
| 5 | Security Control | Associated control ID (e.g., AC-2) | Yes* |
| 6 | Source | How found: assessment, scan, incident, self-identified | Yes* |
| 7 | Original Detection Date | When the weakness was first identified | Yes* |
| 8 | Original Risk Rating | Initial severity: Critical, High, Moderate, Low | Yes* |
| 9 | Adjusted Risk Rating | Risk after compensating controls (if applicable) | Conditional |
| 10 | Vendor Dependency | Yes/No — does remediation depend on vendor action? | Yes* |
| 11 | Scheduled Completion Date | Target remediation date (per severity SLA) | Yes* |
| 12 | Planned Milestones | Specific remediation steps with target dates | Yes* |
| 13 | Milestone Changes | Updates to milestone dates with justification | Yes |
| 14 | Status | Open, In Progress, Completed, Closed, Deferred | Yes* |
| 15 | Completion Date | Actual date the weakness was remediated | Conditional |
| 16 | Comments/Evidence | Remediation details, evidence references | Yes |
| 17 | Deviation Request | DR ID if remediation SLA is exceeded | Conditional |
| 18 | False Positive Justification | If item is FP, justification and evidence | Conditional |
| 19 | Operational Requirement | If accepted risk, justification and approval | Conditional |
| 20 | Cost Estimate | Estimated remediation cost | Recommended |

### POA&M Entry Quality Criteria
- [ ] Unique and consistent ID scheme
- [ ] Description is specific enough to understand the weakness without additional context
- [ ] Description avoids vague language ("improve security", "address findings")
- [ ] Milestones are granular (not just "remediate finding")
- [ ] Milestone dates are between detection date and scheduled completion
- [ ] Severity rating uses a consistent scale
- [ ] SLA compliance: completion date within severity-based timeline
- [ ] Vendor dependencies explicitly noted
- [ ] Status reflects current remediation state
- [ ] Closed items include evidence of remediation and verification

### POA&M Severity SLAs (Legacy FedRAMP Rev5 value, in force until CR26 becomes mandatory Jan 1, 2027)

| Severity | Remediation SLA | Deviation Threshold |
|----------|----------------|-------------------|
| Critical | 30 days (not a distinct FedRAMP category; treated as High) | Requires DR after 30 days |
| High | 30 days | Requires DR after 30 days |
| Moderate | 90 days | Requires DR after 90 days |
| Low | 180 days | Requires DR after 180 days |

**CR26 (VDR/VER, required Dec 7, 2026; grace to Mar 7, 2027):** remediation timeframes are set by PAIN rating and reachability (VDR-TFR-PVR), KEVs per CISA due dates (VDR-TFR-KEV); anything not remediated within 192 days becomes an Accepted Vulnerability with written justification (VER-TFR-MAV); monthly human-readable reporting (VER-TFR-MHR).

### Common POA&M Deficiencies
- Vague descriptions that could apply to any finding
- Missing or generic milestones ("working on remediation")
- Overdue items without deviation requests
- Status not updated monthly
- Severity ratings inconsistent with CVSS scores
- No evidence referenced for closed items
- Vendor dependencies not flagged

---

## Policy Documents

### Required Structural Elements*

| Element | Description | Required |
|---------|-------------|----------|
| Purpose | Why the policy exists | Yes* |
| Scope | Who and what it covers | Yes* |
| Roles and Responsibilities | Named roles and their duties | Yes* |
| Policy Statements | Mandated requirements (SHALL/MUST) | Yes* |
| Procedures Reference | Pointer to implementing procedures | Yes* |
| Definitions | Key terms used in the policy | Recommended |
| Compliance/Enforcement | Consequences for non-compliance | Yes* |
| Exceptions Process | How to request exceptions | Recommended |
| Review Frequency | How often the policy is reviewed | Yes* |
| Approval Authority | Who approves the policy | Yes* |
| Effective Date | When the policy takes effect | Yes* |
| Version/Revision History | Document history | Yes* |
| Related Documents | Referenced policies, standards, procedures | Recommended |

### Policy Language Quality

**Enforceable language** (required for policy statements):
- "shall", "must", "is required to", "will" (as imperative)

**Advisory language** (acceptable for guidance, not for requirements):
- "should", "may", "is recommended", "is encouraged"

**Unenforceable language** (finding if used for requirements):
- "try to", "make best effort", "as appropriate", "as feasible"
- "in a timely manner" (without timeframe)
- "as needed" (without criteria for when it's needed)

### Policy-to-Control-Family Alignment

| Policy Document | Primary Control Families |
|----------------|------------------------|
| Access Control Policy | AC, IA |
| Audit and Accountability Policy | AU |
| Configuration Management Policy | CM, SA |
| Contingency Planning Policy | CP |
| Identification and Authentication Policy | IA |
| Incident Response Policy | IR |
| Maintenance Policy | MA |
| Media Protection Policy | MP |
| Personnel Security Policy | PS |
| Physical and Environmental Protection Policy | PE |
| Planning Policy | PL |
| Risk Assessment Policy | RA, CA |
| System and Communications Protection Policy | SC |
| System and Information Integrity Policy | SI |
| Supply Chain Risk Management Policy | SR, SA |
| Privacy Policy | PT (not in any FedRAMP baseline) |
| Awareness and Training Policy | AT |
| Program Management Policy | PM (not in any FedRAMP baseline) |

### Common Policy Deficiencies
- Using advisory language ("should") for mandatory requirements
- Missing review frequency or review date
- No version control / revision history
- Scope is ambiguous (doesn't specify which systems, personnel, locations)
- Role names are generic ("management") instead of specific ("ISSO", "System Owner")
- Procedures embedded in policy instead of referenced separately
- Missing enforcement/compliance section
- Not aligned with actual system implementation

---

## Customer Responsibility Matrix (CRM)

Paired with the Customer Implementation Summary (CIS) in FedRAMP: the legacy Rev5 SSP Appendix J is the "CIS and CRM Workbook". CR26 has no CIS/CRM template (the Secure Configuration Guide ruleset applies instead).

### Required Structure

- [ ] Organized by control family (AC, AT, AU, etc.)
- [ ] Every baseline control with customer responsibility listed
- [ ] Responsibility designation for each control part:
  - **CSP-Implemented**: CSP fully handles (customer has no action)
  - **Customer-Implemented**: Customer must fully implement
  - **Shared**: Both parties have responsibilities (must specify split)
  - **Inherited**: Control inherited from underlying infrastructure
- [ ] For Shared controls: specific description of what the customer must do
- [ ] Customer-responsible ODP values identified (where customer must define parameters)
- [ ] Clear, actionable customer requirements (not just "customer is responsible")

### CRM Coverage by Family (Expected Distribution)

| Family | Typical Responsibility Pattern |
|--------|-------------------------------|
| AC | Mostly Shared — CSP provides platform, customer manages user accounts/roles |
| AT | Mostly Customer — customer trains own personnel |
| AU | Shared — CSP generates logs, customer configures retention/review |
| CA | Shared — CSP maintains authorization, customer maintains own assessment |
| CM | Shared — CSP manages infrastructure config, customer manages application config |
| CP | Shared — CSP provides infrastructure resilience, customer plans application recovery |
| IA | Shared — CSP provides authentication mechanisms, customer manages credentials |
| IR | Shared — CSP handles infrastructure incidents, customer handles application-level |
| MA | Mostly CSP — infrastructure maintenance; customer handles application maintenance |
| MP | Mostly CSP (cloud) — media handling at data center level |
| PE | CSP-Inherited (cloud) — physical data center security |
| PL | Shared — CSP provides security plan, customer provides customer-specific planning |
| PM | Mostly Customer — customer's program management (not in any FedRAMP baseline) |
| PS | Mostly Customer — customer's personnel screening and management |
| PT | Shared — CSP provides privacy controls, customer manages PII handling (not in any FedRAMP baseline) |
| RA | Shared — CSP scans infrastructure, customer scans application layer |
| SA | Shared — CSP manages acquisition, customer manages own development |
| SC | Shared — CSP provides network/transport protections, customer configures application |
| SI | Shared — CSP monitors infrastructure, customer monitors application |
| SR | Shared — CSP manages supply chain, customer manages own vendors |

### Common CRM Deficiencies
- PE controls omitted (assumed CSP) without explicit inheritance statement
- PS controls assumed customer-only but shared for CSP admin access
- Shared controls described vaguely ("customer and CSP share responsibility")
- No specifics on what the customer must actually do or configure
- Missing customer-responsible ODP values
- CP and IR shared responsibilities unclear (which tier does customer handle?)
- AU requirements unclear (does customer get raw logs? Processed alerts?)
- Configuration controls (CM-6, CM-7) don't specify customer vs. CSP scope

---

## Contingency Plan (CP)

Based on NIST 800-34 Rev 1 and FedRAMP CP template.

### Required Sections

- [ ] Purpose and scope
- [ ] Applicable laws, regulations, policies
- [ ] System description and architecture (brief, reference SSP)
- [ ] Roles and responsibilities (CP Director, team leads, team members)
- [ ] Business Impact Analysis (BIA)*
  - [ ] Critical system functions identified and prioritized
  - [ ] Maximum tolerable downtime (MTD) per function
  - [ ] Recovery Time Objective (RTO)*
  - [ ] Recovery Point Objective (RPO)*
- [ ] Recovery strategies*
  - [ ] Backup strategy (frequency, type, location, encryption)
  - [ ] Alternate site (type: hot/warm/cold, location, activation time)
  - [ ] Alternate communications
  - [ ] Equipment replacement strategy
- [ ] Recovery procedures*
  - [ ] Phase 1: Activation and notification
  - [ ] Phase 2: Recovery operations (step-by-step)
  - [ ] Phase 3: Reconstitution (return to normal)
- [ ] Testing*
  - [ ] Test type (tabletop, functional, full-scale)
  - [ ] Test frequency (annual minimum for FedRAMP)
  - [ ] Most recent test date and results
  - [ ] Lessons learned and corrective actions
- [ ] Plan maintenance
  - [ ] Review frequency
  - [ ] Update triggers (personnel change, system change, test findings)
  - [ ] Distribution list
- [ ] Appendices
  - [ ] Contact information (notification cascade)
  - [ ] Vendor contact information
  - [ ] Detailed recovery procedures
  - [ ] Alternate site details
  - [ ] System inventory relevant to recovery

### Common CP Deficiencies
- RTO/RPO values missing or "TBD"
- Backup strategy described but not tested/verified
- Recovery procedures too generic to actually follow
- Test results not documented or tests not conducted annually
- Alternate site arrangements described vaguely
- Contact lists outdated
- No reconstitution procedures (how to return to primary)

---

## Incident Response Plan (IRP)

Based on the traditional four-phase incident response lifecycle (NIST 800-61 Rev 2) as used in most FedRAMP IRP templates. Note: NIST 800-61 Rev 3 (2025) restructured the model around CSF 2.0 functions (Govern, Identify, Protect, Detect, Respond, Recover); organizations should check whether their AO or FedRAMP requires the updated model.

### Required Sections

- [ ] Purpose, scope, and applicability
- [ ] Incident response team structure and roles*
  - [ ] IR Manager / IR Lead
  - [ ] IR Analysts / Handlers
  - [ ] Communications lead
  - [ ] Legal/Privacy liaison
  - [ ] Management escalation chain
- [ ] Incident categories and severity levels*
  - [ ] Category definitions (malware, unauthorized access, DoS, data breach, etc.)
  - [ ] Severity levels (Critical, High, Medium, Low) with criteria
  - [ ] Impact assessment criteria
- [ ] Incident handling procedures*
  - [ ] Phase 1: Preparation
  - [ ] Phase 2: Detection and Analysis
  - [ ] Phase 3: Containment, Eradication, and Recovery
  - [ ] Phase 4: Post-Incident Activity
- [ ] Reporting requirements*
  - [ ] Internal reporting chain and timelines
  - [ ] CISA (formerly US-CERT; merged 2023) reporting requirements and timelines
  - [ ] FedRAMP notification requirements (CR26: fedramp_security@fedramp.gov and trust-center publication)
  - [ ] Agency notification requirements
  - [ ] Law enforcement notification criteria
  - [ ] Breach notification (per Privacy Act, state laws)
- [ ] Evidence handling and forensics
- [ ] Communication procedures (internal and external)
- [ ] Training requirements (annual minimum)
- [ ] Testing requirements*
  - [ ] Exercise type and frequency (IR-3 Legacy FedRAMP Rev5 value, in force until CR26 becomes mandatory Jan 1, 2027: functional exercises annually at Moderate; every 6 months, including functional exercises annually, at High. CR26: no FedRAMP-assigned value)
  - [ ] Most recent test date and results
  - [ ] Lessons learned process
- [ ] Plan maintenance and review schedule
- [ ] Appendices
  - [ ] Contact information
  - [ ] Incident report template
  - [ ] Forensic tools and procedures
  - [ ] Evidence chain-of-custody form

### Federal Incident Reporting Timelines

The older US-CERT "CAT 1-6" incident categories were retired in 2017; CISA's current Federal Incident Notification Guidelines use a one-hour deadline with impact classification (functional, information, recoverability) and attack-vector taxonomy rather than numbered categories.

**Legacy FedRAMP Rev5 value (IR-6, in force until CR26 becomes mandatory Jan 1, 2027):** report within one hour to CISA (formerly US-CERT), FedRAMP, and affected agencies per the legacy FedRAMP Incident Communications Procedures.

**CR26 (IEC ruleset; Rev5 grace to June 1, 2027):** reporting timeframes scale with the estimated **Potential Agency Impact N-rating (PAIN)** — N1 minimal effect on one or more agencies through N5 debilitating effect on more than one agency; default PAIN-5 if not estimated. Providers report to FedRAMP (fedramp_security@fedramp.gov) and agency customers and publish to a trust center; agencies report to CISA.

| Class | PAIN-3/4/5 initial report | PAIN-2 initial report | PAIN-1 initial report |
|-------|---------------------------|-----------------------|-----------------------|
| D (High) | 15 minutes (ongoing every 3 hours; final 3 hours after recovery) | 1 hour (ongoing every 6 hours; final 6 hours after recovery) | 1 hour (ongoing every 24 hours; final 24 hours after recovery) |
| C (Moderate) | 1 hour | 24 hours | 1 business day |
| B (Low) | 6 hours | 1 business day | 1 business day |

### Common IRP Deficiencies
- Incident categories not defined or too broad
- Severity criteria subjective (no measurable thresholds)
- Reporting timelines don't match CISA requirements (legacy one hour) or the CR26 IEC PAIN-based timeframes
- No forensic evidence handling procedures
- Communication plan doesn't address media/public inquiries
- Testing not conducted annually
- Lessons learned process described but not evidenced
- Missing FedRAMP notification procedures

---

## Configuration Management Plan (CMP)

### Required Sections

- [ ] Configuration management roles and responsibilities
- [ ] Configuration item identification
- [ ] Baseline configuration documentation
- [ ] Configuration change control process*
  - [ ] Change request submission
  - [ ] Impact analysis (security impact analysis required)
  - [ ] Approval authority (CCB or equivalent)
  - [ ] Implementation procedures
  - [ ] Testing/validation
  - [ ] Documentation update
- [ ] Configuration monitoring
- [ ] Hardware and software inventory management
- [ ] Patch management process
- [ ] Vulnerability management integration
- [ ] Least functionality / allowed software
- [ ] Plan maintenance and review

### Common CMP Deficiencies
- Change control process described but CCB membership not identified
- Security impact analysis not integrated into change process
- Baseline configurations referenced but not documented
- Inventory management described but update frequency not specified
- No integration between vulnerability scanning results and CM process
