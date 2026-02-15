# GRC Document Section Requirements

Required sections and structural elements for major GRC artifacts, per FedRAMP template standards and NIST guidelines. Use this reference to validate document completeness.

## System Security Plan (SSP)

Based on FedRAMP SSP template (Appendix A format). Sections marked with * are critical — omission is a finding.

### Front Matter
- [ ] Title page with system name, CSP name, date, version
- [ ] Document revision history*
- [ ] Table of contents
- [ ] List of tables and figures
- [ ] Document purpose and scope

### Section 1 — Information System Name and Title*
- [ ] System name (matches FedRAMP Marketplace if applicable)
- [ ] System abbreviation/acronym

### Section 2 — Information System Categorization*
- [ ] FIPS 199 categorization (Confidentiality, Integrity, Availability)
- [ ] Overall system categorization justification
- [ ] Information types (per NIST 800-60)
- [ ] Categorization table with impact levels

### Section 3 — System Owner Information*
- [ ] Organization name, address
- [ ] System owner name, title, contact information
- [ ] Authorizing Official identification

### Section 4 — Responsible Parties and Key Personnel*
- [ ] ISSO name, title, contact
- [ ] ISSM name, title, contact
- [ ] System administrators
- [ ] Other key security personnel
- [ ] Roles and responsibilities matrix

### Section 5 — System Description*
- [ ] General system description and function
- [ ] System environment and architecture
- [ ] System interconnections table
- [ ] Types of users (privileged, non-privileged, external)
- [ ] User roles and access levels table

### Section 6 — System Architecture*
- [ ] Authorization boundary diagram*
- [ ] Network architecture diagram*
- [ ] Data flow diagram(s)*
- [ ] Architecture narrative describing components
- [ ] Ports, protocols, and services table (PP&S)*

### Section 7 — System Environment
- [ ] Hardware inventory/categories
- [ ] Software inventory/categories
- [ ] Data center locations
- [ ] Cloud service model (IaaS/PaaS/SaaS)
- [ ] Deployment model (public/private/hybrid/community)

### Section 8 — System Interconnections
- [ ] Interconnection table (all external connections)
- [ ] For each: system name, organization, connection type, boundary
- [ ] ISA/MOU references
- [ ] API/data exchange descriptions

### Section 9 — Applicable Laws and Regulations
- [ ] Federal laws (FISMA, Privacy Act, etc.)
- [ ] Regulations (OMB circulars)
- [ ] Standards (FIPS, NIST SP)
- [ ] FedRAMP requirements
- [ ] Agency-specific requirements

### Section 10 — Minimum Security Controls*
- [ ] Control summary table (all baseline controls)
- [ ] Implementation status for each (Implemented, Partially, Planned, N/A)
- [ ] Responsibility designation for each (CSP, Customer, Shared, Inherited)

### Section 11 — Control Implementation Narratives*
- [ ] Every baseline control has a narrative
- [ ] Each narrative addresses the Five W's (What, Who, How, When, Where)
- [ ] All ODPs filled in with specific values
- [ ] All baseline enhancements addressed
- [ ] Responsibility clearly stated per control part
- [ ] Inherited controls identify the source (CSP/infrastructure provider)

### Appendices (FedRAMP-required)
- [ ] Appendix A: FedRAMP Security Controls (full control matrix)
- [ ] Appendix B: Related Documents
- [ ] Appendix C: Acronyms
- [ ] Appendix D: Rules of Behavior
- [ ] Appendix E: Information System Contingency Plan
- [ ] Appendix F: Configuration Management Plan
- [ ] Appendix G: Incident Response Plan
- [ ] Appendix H: CIS/CRM (Customer Implementation Summary)
- [ ] Appendix I: FIPS 199 Categorization
- [ ] Appendix J: Privacy Threshold Analysis / Privacy Impact Assessment
- [ ] Appendix K: Laws and Regulations
- [ ] Appendix L: Integrated Inventory Workbook

### Common SSP Deficiencies
- Missing or outdated authorization boundary diagram
- Control narratives that restate requirements instead of describing implementation
- Incomplete ports/protocols/services table
- Missing interconnection details for API integrations
- ODP values left as TBD or not matching FedRAMP-required values
- Responsibility designations missing or inconsistent
- Appendices referenced but not included

---

## Plan of Action & Milestones (POA&M)

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

### POA&M Severity SLAs (FedRAMP)

| Severity | Remediation SLA | Deviation Threshold |
|----------|----------------|-------------------|
| Critical | 30 days | Requires DR after 30 days |
| High | 30 days | Requires DR after 30 days |
| Moderate | 90 days | Requires DR after 90 days |
| Low | 180 days | Requires DR after 180 days |

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
| Privacy Policy | PT |
| Awareness and Training Policy | AT |
| Program Management Policy | PM |

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

Also called Customer Implementation Summary (CIS) in FedRAMP.

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
| PM | Mostly Customer — customer's program management |
| PS | Mostly Customer — customer's personnel screening and management |
| PT | Shared — CSP provides privacy controls, customer manages PII handling |
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
  - [ ] US-CERT/CISA reporting requirements and timelines
  - [ ] FedRAMP PMO notification requirements
  - [ ] Agency notification requirements
  - [ ] Law enforcement notification criteria
  - [ ] Breach notification (per Privacy Act, state laws)
- [ ] Evidence handling and forensics
- [ ] Communication procedures (internal and external)
- [ ] Training requirements (annual minimum)
- [ ] Testing requirements*
  - [ ] Exercise type and frequency (annual minimum)
  - [ ] Most recent test date and results
  - [ ] Lessons learned process
- [ ] Plan maintenance and review schedule
- [ ] Appendices
  - [ ] Contact information
  - [ ] Incident report template
  - [ ] Forensic tools and procedures
  - [ ] Evidence chain-of-custody form

### CISA Federal Incident Reporting Timelines

Based on legacy US-CERT categories still referenced in FedRAMP guidance. Note: CISA incident reporting requirements continue to evolve — verify against current CISA BODs and federal incident notification guidance.

| Category | Description | Reporting Timeline |
|----------|-------------|-------------------|
| CAT 1 | Unauthorized Access | Within 1 hour |
| CAT 2 | Denial of Service | Within 1 hour |
| CAT 3 | Malicious Code | Within 1 hour |
| CAT 4 | Improper Usage | Weekly |
| CAT 5 | Scans/Probes/Recon | Monthly |
| CAT 6 | Investigation | N/A |

### Common IRP Deficiencies
- Incident categories not defined or too broad
- Severity criteria subjective (no measurable thresholds)
- Reporting timelines don't match CISA requirements
- No forensic evidence handling procedures
- Communication plan doesn't address media/public inquiries
- Testing not conducted annually
- Lessons learned process described but not evidenced
- Missing FedRAMP PMO notification procedures

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
