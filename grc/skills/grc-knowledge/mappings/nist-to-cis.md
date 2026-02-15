# NIST 800-53 Rev 5 to CIS Controls v8 Mapping

## Overview

This document maps **NIST SP 800-53 Rev 5** (20 control families, ~1,100+ controls) to **CIS Controls v8** (18 controls, 153 safeguards). NIST 800-53 is the authoritative federal control catalog used across RMF, FedRAMP, and FISMA. CIS Controls v8 is a prioritized, actionable set of cybersecurity best practices maintained by the Center for Internet Security and widely adopted in commercial environments.

NIST 800-53 serves as the comprehensive, risk-based catalog -- it is broad, deep, and covers governance, privacy, and physical security in addition to technical controls. CIS Controls v8 is intentionally streamlined and implementation-focused, organizing safeguards into three Implementation Groups (IGs) that provide a prioritized adoption path.

**Mapping direction**: NIST 800-53 families map to one or more CIS Controls. Because NIST is more granular, many NIST controls have no direct CIS equivalent (especially governance, physical, and privacy controls). Conversely, every CIS safeguard maps to at least one NIST control.

---

## Key Differences

| Attribute | NIST 800-53 Rev 5 | CIS Controls v8 |
|-----------|-------------------|-----------------|
| **Purpose** | Comprehensive federal control catalog | Prioritized cybersecurity best practices |
| **Scope** | All control domains including governance, physical, privacy | Technical and operational cybersecurity controls |
| **Structure** | 20 families, ~1,100+ controls with enhancements | 18 controls, 153 safeguards |
| **Prescriptiveness** | Flexible -- describes *what* to achieve | Actionable -- describes *what to do* with specificity |
| **Baselines** | Low (~150), Moderate (~304), High (~392) | IG1 (56), IG2 (74 additional = 130 total), IG3 (23 additional = 153 total) |
| **Governance coverage** | Extensive (PM, PL, CA families) | Minimal -- focuses on technical implementation |
| **Physical security** | Full PE family (15+ controls) | Limited to asset inventory (CIS 1) |
| **Privacy** | Dedicated PT family (Rev 5 addition) | No privacy-specific safeguards |
| **Supply chain** | Dedicated SR family + SA controls | CIS 15 (Service Provider Management) -- narrower scope |
| **Adoption** | Required for US federal systems | Voluntary; widely adopted commercially |

---

## Implementation Group to NIST Baseline Alignment

CIS Implementation Groups roughly correspond to NIST baselines in terms of security rigor, though the mapping is conceptual rather than exact.

| CIS IG Level | Safeguards | Approximate NIST Baseline | Description |
|-------------|------------|---------------------------|-------------|
| **IG1** | 56 safeguards | Low baseline concepts | Essential cyber hygiene. Minimum standard for all organizations. Covers basic asset inventory, access control, data protection, secure configuration, log management, and awareness training. |
| **IG2** | 130 safeguards (IG1 + 74) | Moderate baseline concepts | Expanded coverage for organizations handling sensitive data. Adds vulnerability management, email/browser protections, network monitoring, incident response, and penetration testing. |
| **IG3** | 153 safeguards (IG2 + 23) | High baseline concepts | Full CIS coverage for organizations facing sophisticated threats. Adds advanced logging, application-layer controls, and penetration testing with red team exercises. |

**Important caveat**: NIST Low baseline contains ~150 controls spanning governance, physical, and operational domains that CIS IG1 does not address. IG1 provides stronger technical prescriptiveness in the areas it does cover but has significantly narrower domain coverage.

---

## Comprehensive Mapping by NIST Family

### AC -- Access Control

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| AC-1 (Policy & Procedures) | -- | -- | No CIS equivalent; CIS assumes policy exists |
| AC-2 (Account Management) | CIS 5 (Account Management) | 5.1, 5.2, 5.3, 5.4, 5.5 | Strong alignment. 5.1 = inventory of accounts, 5.2 = use unique passwords, 5.3 = disable dormant accounts, 5.4 = restrict admin privileges, 5.5 = establish/maintain inventory of service accounts |
| AC-3 (Access Enforcement) | CIS 6 (Access Control Management) | 6.1, 6.2, 6.7, 6.8 | 6.1 = establish access granting process, 6.2 = establish access revoking process, 6.7 = centralize access control, 6.8 = define/maintain role-based access |
| AC-4 (Information Flow) | CIS 12 (Network Infrastructure) | 12.2, 12.3, 12.5 | 12.2 = establish/maintain secure network architecture, 12.5 = centralize network AAA |
| AC-5 (Separation of Duties) | CIS 6 | 6.8 | Partial -- 6.8 covers role-based access but does not explicitly require SoD |
| AC-6 (Least Privilege) | CIS 5, CIS 6 | 5.4, 6.8 | 5.4 = restrict admin privileges; 6.8 = role-based access control |
| AC-7 (Unsuccessful Logon Attempts) | CIS 4 (Secure Configuration) | 4.1 | Addressed through secure configuration baselines |
| AC-11 (Device Lock) | CIS 4 | 4.3 | 4.3 = configure automatic session locking on enterprise assets |
| AC-17 (Remote Access) | CIS 12 | 12.6, 12.7 | 12.6 = use of secure network management and communication protocols; 12.7 = ensure remote devices use VPN and connect to enterprise AAA |
| AC-19 (Access Control for Mobile) | CIS 1 (Enterprise Asset Inventory) | 1.1, 1.2 | Partial -- CIS tracks mobile devices as assets but lacks full mobile access policy controls |
| AC-20 (Use of External Systems) | CIS 15 (Service Provider Mgmt) | 15.1 | 15.1 = establish/maintain inventory of service providers |

### AT -- Awareness and Training

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| AT-1 (Policy & Procedures) | -- | -- | No CIS equivalent |
| AT-2 (Literacy Training) | CIS 14 (Security Awareness Training) | 14.1, 14.2, 14.3, 14.4, 14.5, 14.6, 14.7, 14.8, 14.9 | Strong alignment. 14.1 = establish security awareness program, 14.2 = train workforce on recognizing social engineering, 14.3 = train workforce on authentication best practices, 14.4 = train workforce on data handling, 14.5 = train workforce on causes of unintentional data exposure, 14.6 = train workforce on recognizing/reporting security incidents, 14.7 = train workforce on how to identify and report if their assets are missing security updates, 14.8 = train workforce on dangers of connecting to/transmitting data over insecure networks, 14.9 = conduct role-specific security training |
| AT-3 (Role-Based Training) | CIS 14 | 14.9 | 14.9 = conduct role-specific security training |
| AT-4 (Training Records) | -- | -- | No CIS equivalent; CIS does not address training record-keeping |

### AU -- Audit and Accountability

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| AU-1 (Policy & Procedures) | -- | -- | No CIS equivalent |
| AU-2 (Event Logging) | CIS 8 (Audit Log Management) | 8.1, 8.2, 8.5 | 8.1 = establish/maintain audit log management process, 8.2 = collect audit logs, 8.5 = collect detailed audit logs |
| AU-3 (Content of Audit Records) | CIS 8 | 8.5 | 8.5 = collect detailed audit logs (IG2+) |
| AU-4 (Audit Log Storage Capacity) | CIS 8 | 8.1, 8.3 | 8.3 = ensure adequate audit log storage |
| AU-5 (Response to Audit Failures) | CIS 8 | 8.1 | Partial -- CIS addresses log process management but not failure-specific responses |
| AU-6 (Audit Record Review) | CIS 8 | 8.9, 8.11 | 8.9 = centralize audit logs, 8.11 = conduct audit log reviews |
| AU-7 (Audit Record Reduction) | CIS 8 | 8.9, 8.12 | 8.9 = centralize audit logs, 8.12 = collect service provider logs |
| AU-8 (Time Stamps) | CIS 8 | 8.4 | 8.4 = standardize time synchronization |
| AU-9 (Protection of Audit Info) | CIS 8 | 8.1 | Partial -- CIS addresses log management process but not explicit integrity protection |
| AU-11 (Audit Record Retention) | CIS 8 | 8.3, 8.10 | 8.3 = ensure adequate storage, 8.10 = retain audit logs |
| AU-12 (Audit Record Generation) | CIS 8 | 8.2 | 8.2 = collect audit logs |

### CA -- Assessment, Authorization, and Monitoring

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| CA-2 (Control Assessments) | -- | -- | No CIS equivalent; CIS does not prescribe formal control assessments |
| CA-3 (Information Exchange) | CIS 12 | 12.2 | Partial -- secure architecture but not formal ISAs |
| CA-5 (Plan of Action & Milestones) | -- | -- | No CIS equivalent; governance artifact |
| CA-7 (Continuous Monitoring) | CIS 7 (Vulnerability Mgmt), CIS 13 (Network Monitoring) | 7.1-7.7, 13.1-13.11 | CIS addresses technical monitoring but not the full RMF continuous monitoring lifecycle |
| CA-8 (Penetration Testing) | CIS 18 (Penetration Testing) | 18.1-18.5 | Strong alignment. 18.1 = establish/maintain penetration testing program, 18.2 = perform periodic external penetration tests, 18.3 = remediate penetration test findings, 18.4 = validate security measures, 18.5 = perform periodic internal penetration tests |

### CM -- Configuration Management

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| CM-1 (Policy & Procedures) | -- | -- | No CIS equivalent |
| CM-2 (Baseline Configuration) | CIS 4 (Secure Configuration) | 4.1, 4.2 | 4.1 = establish/maintain secure configuration process, 4.2 = establish/maintain secure configuration for network infrastructure |
| CM-3 (Configuration Change Control) | CIS 4 | 4.1 | Partial -- CIS focuses on configuration baselines, not formal change control boards |
| CM-5 (Access Restrictions for Change) | CIS 6 | 6.1, 6.2 | Addressed through access control management |
| CM-6 (Configuration Settings) | CIS 4 | 4.1, 4.4, 4.5, 4.6, 4.8 | 4.4 = implement/manage firewall on servers, 4.5 = implement/manage firewall on end-user devices, 4.6 = securely manage enterprise assets and software, 4.8 = uninstall/disable unnecessary services |
| CM-7 (Least Functionality) | CIS 4, CIS 2 (Software Inventory) | 4.7, 4.8, 2.3, 2.4 | 4.7 = manage default accounts, 4.8 = uninstall/disable unnecessary services, 2.3 = address unauthorized software, 2.4 = utilize automated software inventory tools |
| CM-8 (System Component Inventory) | CIS 1 (Enterprise Asset Inventory), CIS 2 (Software Inventory) | 1.1, 1.2, 1.3, 1.4, 1.5, 2.1, 2.2, 2.3 | Strong alignment. CIS 1 covers hardware asset inventory; CIS 2 covers software inventory |
| CM-10 (Software Usage Restrictions) | CIS 2 | 2.3, 2.7 | 2.3 = address unauthorized software, 2.7 = allowlisting for authorized software libraries |
| CM-11 (User-Installed Software) | CIS 2 | 2.5, 2.6, 2.7 | 2.5 = allowlisting for authorized software, 2.6 = allowlisting for authorized libraries, 2.7 = allowlisting for authorized scripts |

### CP -- Contingency Planning

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| CP-1 (Policy & Procedures) | -- | -- | No CIS equivalent |
| CP-2 (Contingency Plan) | CIS 11 (Data Recovery) | 11.1 | Partial -- 11.1 = establish/maintain data recovery practices. CIS lacks full BCP/DR planning scope |
| CP-4 (Contingency Plan Testing) | CIS 11 | 11.5 | 11.5 = test data recovery (IG2+) |
| CP-6 (Alternate Storage Site) | CIS 11 | 11.3 | 11.3 = protect recovery data (includes offsite/alternate storage) |
| CP-7 (Alternate Processing Site) | -- | -- | No CIS equivalent; CIS does not address alternate processing sites |
| CP-9 (System Backup) | CIS 11 | 11.2, 11.3, 11.4 | 11.2 = perform automated backups, 11.3 = protect recovery data, 11.4 = establish/maintain isolated instance of recovery data |
| CP-10 (System Recovery) | CIS 11 | 11.1, 11.5 | 11.1 = establish data recovery practices, 11.5 = test data recovery |

### IA -- Identification and Authentication

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| IA-1 (Policy & Procedures) | -- | -- | No CIS equivalent |
| IA-2 (Identification & Auth - Org Users) | CIS 6 | 6.3, 6.4, 6.5 | 6.3 = require MFA for externally-exposed applications, 6.4 = require MFA for remote network access, 6.5 = require MFA for administrative access |
| IA-4 (Identifier Management) | CIS 5 | 5.1, 5.5 | 5.1 = establish/maintain inventory of accounts, 5.5 = establish/maintain inventory of service accounts |
| IA-5 (Authenticator Management) | CIS 5, CIS 4 | 5.2, 4.1 | 5.2 = use unique passwords. Password policies addressed through secure configuration |
| IA-6 (Authentication Feedback) | CIS 4 | 4.1 | Addressed through secure configuration baselines |
| IA-8 (Identification & Auth - Non-Org Users) | CIS 6 | 6.3, 6.4 | Partial -- MFA safeguards apply to all users |
| IA-12 (Identity Proofing) | -- | -- | No CIS equivalent; CIS does not address identity proofing processes |

### IR -- Incident Response

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| IR-1 (Policy & Procedures) | CIS 17 (Incident Response Mgmt) | 17.1 | 17.1 = designate personnel to manage incident handling |
| IR-2 (Incident Response Training) | CIS 17 | 17.7 | 17.7 = conduct routine incident response exercises |
| IR-3 (Incident Response Testing) | CIS 17 | 17.7, 17.8 | 17.7 = conduct routine incident response exercises, 17.8 = conduct post-incident reviews |
| IR-4 (Incident Handling) | CIS 17 | 17.2, 17.3, 17.4, 17.5 | 17.2 = establish/maintain contact information for reporting, 17.3 = establish/maintain incident reporting process, 17.4 = establish/maintain incident response process, 17.5 = assign key roles and responsibilities |
| IR-5 (Incident Monitoring) | CIS 17 | 17.9 | 17.9 = establish/maintain security incident thresholds |
| IR-6 (Incident Reporting) | CIS 17 | 17.2, 17.3, 17.6 | 17.6 = define mechanisms for communicating during incident response |
| IR-8 (Incident Response Plan) | CIS 17 | 17.4 | 17.4 = establish/maintain incident response process |

### MA -- Maintenance

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| MA-2 (Controlled Maintenance) | CIS 4 | 4.1 | Partial -- addressed through secure configuration management |
| MA-3 (Maintenance Tools) | -- | -- | No CIS equivalent |
| MA-4 (Nonlocal Maintenance) | CIS 12, CIS 6 | 12.6, 6.4 | Partial -- remote access and MFA safeguards apply |
| MA-5 (Maintenance Personnel) | -- | -- | No CIS equivalent; governance control |

### MP -- Media Protection

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| MP-2 (Media Access) | CIS 3 (Data Protection) | 3.1, 3.9 | Partial -- 3.1 = establish/maintain data management process, 3.9 = encrypt data on removable media |
| MP-6 (Media Sanitization) | CIS 3 | 3.5 | Partial -- 3.5 = securely dispose of data. CIS is less prescriptive on sanitization methods |
| MP-7 (Media Use) | CIS 3 | 3.9 | 3.9 = encrypt data on removable media |

### PE -- Physical and Environmental Protection

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| PE-2 (Physical Access Authorizations) | -- | -- | No CIS equivalent; CIS does not address physical security |
| PE-3 (Physical Access Control) | -- | -- | No CIS equivalent |
| PE-6 (Monitoring Physical Access) | -- | -- | No CIS equivalent |
| PE-8 (Visitor Access Records) | -- | -- | No CIS equivalent |
| PE-13 (Fire Protection) | -- | -- | No CIS equivalent |
| PE-14 (Environmental Controls) | -- | -- | No CIS equivalent |
| PE-17 (Alternate Work Site) | -- | -- | No CIS equivalent |
| General note | CIS 1 | 1.1, 1.2 | CIS 1 (Enterprise Asset Inventory) provides limited overlap -- tracking physical assets but not physical facility security or environmental controls |

### PL -- Planning

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| PL-1 through PL-11 | -- | -- | No CIS equivalent. PL controls (system security plans, rules of behavior, security architecture) are governance artifacts with no CIS counterpart |

### PM -- Program Management

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| PM-1 through PM-32 | -- | -- | No CIS equivalent. PM controls (CISO designation, enterprise architecture, risk strategy, insider threat program) are organizational governance controls outside CIS scope |

### PS -- Personnel Security

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| PS-3 (Personnel Screening) | -- | -- | No CIS equivalent |
| PS-4 (Personnel Termination) | CIS 5, CIS 6 | 5.3, 6.2 | Partial -- 5.3 = disable dormant accounts, 6.2 = establish access revoking process |
| PS-5 (Personnel Transfer) | CIS 6 | 6.1, 6.2 | Partial -- access management processes |
| PS-6 (Access Agreements) | -- | -- | No CIS equivalent; governance artifact |

### PT -- PII Processing and Transparency

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| PT-1 through PT-8 | -- | -- | No CIS equivalent. PT is a Rev 5 addition focused on privacy notices, consent, and PII processing authority. CIS does not address privacy controls |

### RA -- Risk Assessment

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| RA-1 (Policy & Procedures) | -- | -- | No CIS equivalent |
| RA-3 (Risk Assessment) | -- | -- | No direct CIS equivalent; CIS does not prescribe formal risk assessments |
| RA-5 (Vulnerability Monitoring & Scanning) | CIS 7 (Continuous Vulnerability Mgmt) | 7.1-7.7 | Strong alignment. 7.1 = establish/maintain vulnerability management process, 7.2 = establish/maintain remediation process, 7.3 = perform automated OS patching, 7.4 = perform automated application patching, 7.5 = perform automated vulnerability scans of internal assets, 7.6 = perform automated vulnerability scans of externally-exposed assets, 7.7 = remediate detected vulnerabilities |
| RA-7 (Risk Response) | -- | -- | No CIS equivalent; governance control |

### SA -- System and Services Acquisition

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| SA-1 (Policy & Procedures) | -- | -- | No CIS equivalent |
| SA-3 (System Development Lifecycle) | CIS 16 (Application Software Security) | 16.1 | 16.1 = establish/maintain secure application development process |
| SA-4 (Acquisition Process) | CIS 15 (Service Provider Mgmt) | 15.1, 15.2 | 15.1 = establish/maintain inventory of service providers, 15.2 = establish/maintain service provider management policy |
| SA-8 (Security/Privacy Engineering) | CIS 16 | 16.1, 16.10, 16.14 | 16.10 = apply secure design principles in application architectures, 16.14 = conduct threat modeling |
| SA-9 (External System Services) | CIS 15 | 15.1, 15.2, 15.3, 15.4, 15.5 | 15.3 = classify service providers, 15.4 = ensure service provider contracts include security requirements, 15.5 = assess service providers |
| SA-11 (Developer Testing) | CIS 16 | 16.2, 16.3, 16.4, 16.5, 16.6, 16.7, 16.12 | 16.2 = establish/maintain process for accepting/addressing software vulnerabilities, 16.3 = perform root cause analysis on vulnerabilities, 16.4 = establish/maintain code of secure coding practices, 16.5 = use up-to-date compiler/interpreter language features, 16.6 = use standard hardening configuration templates, 16.7 = use standard security features within application frameworks, 16.12 = implement code-level security checks |
| SA-15 (Development Process) | CIS 16 | 16.1, 16.8, 16.9, 16.11, 16.13 | 16.8 = separate production/non-production systems, 16.9 = train developers in application security, 16.11 = leverage vetted modules/services, 16.13 = conduct application penetration testing |

### SC -- System and Communications Protection

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| SC-1 (Policy & Procedures) | -- | -- | No CIS equivalent |
| SC-5 (Denial-of-Service Protection) | CIS 13 (Network Monitoring) | 13.8 | Partial -- 13.8 = deploy network intrusion prevention solutions |
| SC-7 (Boundary Protection) | CIS 12 (Network Infrastructure), CIS 13 | 12.2, 12.3, 12.4, 13.1, 13.4 | 12.2 = establish/maintain secure network architecture, 12.3 = securely manage network infrastructure, 12.4 = establish/maintain architecture diagrams, 13.1 = centralize security event alerting, 13.4 = perform traffic filtering between network segments |
| SC-8 (Transmission Confidentiality) | CIS 3 (Data Protection) | 3.7, 3.10 | 3.7 = establish/maintain data classification scheme, 3.10 = encrypt sensitive data in transit |
| SC-12 (Cryptographic Key Mgmt) | CIS 3 | 3.11 | 3.11 = encrypt sensitive data at rest |
| SC-13 (Cryptographic Protection) | CIS 3 | 3.10, 3.11 | 3.10 = encrypt data in transit, 3.11 = encrypt data at rest |
| SC-17 (PKI Certificates) | -- | -- | No CIS equivalent for certificate management lifecycle |
| SC-23 (Session Authenticity) | -- | -- | No direct CIS equivalent; SC-23 addresses session hijacking prevention, not session locking |
| SC-28 (Protection of Info at Rest) | CIS 3 | 3.11 | 3.11 = encrypt sensitive data at rest |

### SI -- System and Information Integrity

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| SI-1 (Policy & Procedures) | -- | -- | No CIS equivalent |
| SI-2 (Flaw Remediation) | CIS 7 (Vulnerability Mgmt) | 7.1, 7.2, 7.3, 7.4, 7.7 | 7.3 = automated OS patching, 7.4 = automated app patching, 7.7 = remediate detected vulnerabilities |
| SI-3 (Malicious Code Protection) | CIS 10 (Malware Defenses) | 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7 | Strong alignment. 10.1 = deploy/maintain anti-malware, 10.2 = configure automatic anti-malware signature updates, 10.3 = disable autorun/autoplay, 10.4 = configure automatic anti-malware scanning of removable media, 10.5 = enable anti-exploitation features, 10.6 = centrally manage anti-malware, 10.7 = use DNS-based filtering |
| SI-4 (System Monitoring) | CIS 13 (Network Monitoring) | 13.1, 13.2, 13.3, 13.6, 13.7, 13.8 | 13.1 = centralize security event alerting, 13.2 = deploy HIDS, 13.3 = deploy NIDS, 13.6 = collect network traffic flow logs, 13.7 = deploy HIPS, 13.8 = deploy NIPS |
| SI-5 (Security Alerts/Advisories) | CIS 7 | 7.1 | 7.1 = establish/maintain vulnerability management process |
| SI-7 (Software/Info Integrity) | CIS 10 | 10.5 | Partial -- 10.5 = enable anti-exploitation features |
| SI-16 (Memory Protection) | CIS 10 | 10.5 | 10.5 = enable anti-exploitation features |

### SR -- Supply Chain Risk Management

| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |
|-------------------|-------------|----------------|----------------|
| SR-1 (SCRM Policy) | CIS 15 | 15.2 | Partial -- 15.2 covers service provider management policy but not full SCRM |
| SR-2 (Supply Chain Risk Management Plan) | -- | -- | No CIS equivalent for comprehensive SCRM plans |
| SR-3 (Supply Chain Controls & Processes) | CIS 15, CIS 16 | 15.3, 15.4, 16.4 | Partial -- provider classification and secure coding practices |
| SR-5 (Acquisition Strategies) | CIS 15 | 15.4, 15.5 | Partial -- contract requirements and provider assessments |

---

## Reverse Mapping: CIS Controls to NIST Families

| CIS Control | Control Name | Primary NIST Families | IG Level |
|-------------|-------------|----------------------|----------|
| **CIS 1** | Enterprise Asset Inventory | CM-8, PM-5 | IG1: 1.1, 1.2; IG2: 1.3, 1.4, 1.5 |
| **CIS 2** | Software Asset Inventory | CM-7, CM-8, CM-10, CM-11 | IG1: 2.1, 2.2, 2.3; IG2: 2.4, 2.5, 2.6; IG3: 2.7 |
| **CIS 3** | Data Protection | MP-2, MP-6, SC-8, SC-12, SC-13, SC-28 | IG1: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6; IG2: 3.7, 3.8, 3.9, 3.10, 3.11, 3.12; IG3: 3.13, 3.14 |
| **CIS 4** | Secure Configuration | CM-2, CM-6, CM-7, AC-7, AC-11 | IG1: 4.1, 4.3, 4.6, 4.7; IG2: 4.2, 4.4, 4.5, 4.8, 4.9, 4.10, 4.11; IG3: 4.12 |
| **CIS 5** | Account Management | AC-2, AC-6, IA-4, IA-5 | IG1: 5.1, 5.2, 5.3, 5.4; IG2: 5.5, 5.6 |
| **CIS 6** | Access Control Management | AC-2, AC-3, AC-5, AC-6, IA-2, IA-8 | IG1: 6.1, 6.2, 6.3, 6.4, 6.5; IG2: 6.6, 6.7, 6.8 |
| **CIS 7** | Continuous Vulnerability Management | RA-5, SI-2, SI-5 | IG1: 7.1, 7.2, 7.3, 7.4; IG2: 7.5, 7.6, 7.7 |
| **CIS 8** | Audit Log Management | AU-2, AU-3, AU-4, AU-6, AU-8, AU-11, AU-12 | IG1: 8.1, 8.2, 8.3; IG2: 8.4, 8.5, 8.9, 8.10, 8.11, 8.12 |
| **CIS 9** | Email and Web Browser Protections | SC-7, SI-3, SI-8 | IG1: 9.1, 9.2; IG2: 9.3, 9.4, 9.5, 9.6, 9.7 |
| **CIS 10** | Malware Defenses | SI-3, SI-7, SI-16 | IG1: 10.1, 10.2, 10.3, 10.4; IG2: 10.5, 10.6, 10.7 |
| **CIS 11** | Data Recovery | CP-2, CP-4, CP-6, CP-9, CP-10 | IG1: 11.1, 11.2, 11.3, 11.4; IG2: 11.5 |
| **CIS 12** | Network Infrastructure Management | AC-4, AC-17, SC-7 | IG1: 12.1; IG2: 12.2, 12.3, 12.4, 12.5, 12.6, 12.7; IG3: 12.8 |
| **CIS 13** | Network Monitoring and Defense | SI-4, SC-5, SC-7 | IG2: 13.1, 13.2, 13.3, 13.4, 13.5, 13.6; IG3: 13.7, 13.8, 13.9, 13.10, 13.11 |
| **CIS 14** | Security Awareness and Training | AT-2, AT-3 | IG1: 14.1, 14.2, 14.3, 14.4, 14.5, 14.6, 14.7, 14.8; IG2: 14.9 |
| **CIS 15** | Service Provider Management | SA-4, SA-9, SR-1, SR-3, SR-5 | IG1: 15.1, 15.2, 15.3, 15.4; IG2: 15.5 |
| **CIS 16** | Application Software Security | SA-3, SA-8, SA-11, SA-15 | IG2: 16.1, 16.2, 16.3, 16.4, 16.5, 16.6, 16.7, 16.8, 16.9, 16.10, 16.11, 16.12; IG3: 16.13, 16.14 |
| **CIS 17** | Incident Response Management | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8 | IG1: 17.1, 17.2, 17.3; IG2: 17.4, 17.5, 17.6, 17.7, 17.8; IG3: 17.9 |
| **CIS 18** | Penetration Testing | CA-8 | IG2: 18.1, 18.2, 18.3; IG3: 18.4, 18.5 |

---

## Gap Analysis

### NIST Families with No or Minimal CIS Coverage

| NIST Family | Gap Description |
|-------------|-----------------|
| **PE** (Physical and Environmental) | CIS does not address physical facility access, environmental controls, fire protection, or visitor management. Organizations must supplement CIS with separate physical security standards |
| **PL** (Planning) | CIS does not require system security plans, security architecture documentation, or rules of behavior |
| **PM** (Program Management) | CIS does not address CISO designation, enterprise architecture, risk strategy, insider threat programs, or security workforce planning |
| **PS** (Personnel Security) | CIS does not address background screening, access agreements, or personnel security policy. Partial overlap with CIS 5/6 for termination/transfer actions |
| **PT** (PII Processing and Transparency) | CIS has no privacy-specific controls. Organizations handling PII must use NIST Privacy Framework or other privacy-specific standards |
| **CA** (Assessment, Authorization, and Monitoring) | CIS does not prescribe formal control assessments, POA&Ms, or authorization decisions. CIS 18 (Penetration Testing) covers CA-8 only |
| **MA** (Maintenance) | CIS does not address maintenance windows, controlled maintenance, or maintenance tool controls |

### CIS Safeguards with Limited NIST Specificity

| CIS Safeguard | Description | NIST Notes |
|---------------|-------------|------------|
| 9.1 | Ensure use of only fully supported browsers and email clients | NIST addresses software currency through CM-7 and SI-2 but does not specifically call out browsers/email clients |
| 9.7 | Deploy and maintain email server anti-malware protections | NIST SI-8 (Spam Protection) covers this but is less prescriptive about email-specific anti-malware |
| 10.3 | Disable autorun and autoplay for removable media | NIST addresses removable media in MP-7 but does not prescribe specific technical mechanisms |
| 10.7 | Use DNS-based filtering | No direct NIST equivalent; falls under general monitoring (SI-4) |
| 12.1 | Ensure network infrastructure is up to date | NIST addresses through SI-2 (Flaw Remediation) and CM-2 (Baseline Configuration) broadly |
