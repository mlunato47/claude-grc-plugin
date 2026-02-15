# NIST 800-53 Rev 5 to PCI DSS v4.0.1 Mapping

## Overview

This document maps NIST 800-53 Rev 5 control families to PCI DSS v4.0.1 requirements. NIST 800-53 is the comprehensive federal security controls catalog used across government systems, while PCI DSS is an industry-specific standard focused exclusively on protecting cardholder data environments (CDEs).

NIST 800-53 serves as the "universal hub" for cross-framework mapping. Because NIST covers the full spectrum of security and privacy, every PCI DSS requirement can be traced to one or more NIST controls. The reverse is not true — many NIST controls address concerns outside PCI DSS's scope.

## Key Differences

| Dimension | NIST 800-53 Rev 5 | PCI DSS v4.0.1 |
|-----------|-------------------|----------------|
| **Issuing body** | NIST (federal) | PCI Security Standards Council (industry) |
| **Scope** | Entire information system boundary | Cardholder data environment (CDE) and connected systems |
| **Applicability** | Federal agencies, contractors, voluntary for private sector | Any entity that stores, processes, or transmits cardholder data |
| **Structure** | 20 families, ~1,000+ controls and enhancements | 12 top-level requirements, ~250 sub-requirements |
| **Baselines** | Low (~150), Moderate (~304), High (~392) | Single set of requirements; SAQ tiers reduce scope by merchant type |
| **Assessment model** | 3PAO / agency assessor per RMF | QSA (Qualified Security Assessor) or ISA (Internal Security Assessor) |
| **Output** | SSP, SAR, POA&M, ATO decision | Report on Compliance (ROC) or Self-Assessment Questionnaire (SAQ) |
| **Risk tailoring** | Explicitly supports tailoring and overlays | Customized approach allows alternative controls meeting stated objective |
| **Compliance cadence** | Continuous monitoring (ConMon) post-ATO | Annual assessment + quarterly scans (ASV) |

### Scoping Considerations

PCI DSS is scoped strictly to the CDE -- systems that store, process, or transmit cardholder data, plus connected systems that could impact CDE security. Network segmentation can reduce scope. NIST 800-53 applies to the entire information system authorization boundary regardless of data type. When mapping, a single NIST control may address functions both inside and outside the CDE. PCI DSS requirements apply only within CDE scope.

## PCI DSS v4.0.1 Requirements Summary

| Req | Title | Focus Area |
|-----|-------|------------|
| 1 | Install and Maintain Network Security Controls | Firewalls, network segmentation, traffic filtering |
| 2 | Apply Secure Configurations to All System Components | Hardening, default credential removal |
| 3 | Protect Stored Account Data | Encryption at rest, key management, data retention |
| 4 | Protect Cardholder Data with Strong Cryptography During Transmission | TLS, encryption in transit |
| 5 | Protect All Systems and Networks from Malicious Software | Anti-malware, endpoint protection |
| 6 | Develop and Maintain Secure Systems and Software | SDLC, patching, vulnerability management, WAF |
| 7 | Restrict Access to System Components and Cardholder Data by Business Need to Know | Least privilege, RBAC |
| 8 | Identify Users and Authenticate Access to System Components | MFA, password policies, credential management |
| 9 | Restrict Physical Access to Cardholder Data | Physical security, visitor management, media controls |
| 10 | Log and Monitor All Access to System Components and Cardholder Data | Audit logging, log review, time synchronization |
| 11 | Test Security of Systems and Networks Regularly | Vulnerability scanning, penetration testing, IDS/IPS, file integrity |
| 12 | Support Information Security with Organizational Policies and Programs | Policies, risk assessments, awareness training, incident response |

## Comprehensive Mapping by NIST Family

### AC — Access Control

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| AC-2 | Account Management | 7.2.1, 7.2.2, 8.2.1, 8.2.2 | PCI Req 7 covers access provisioning; Req 8 covers user identification |
| AC-3 | Access Enforcement | 7.2.1, 7.2.3 | PCI Req 7.2 requires access control systems to enforce least privilege |
| AC-4 | Information Flow Enforcement | 1.2.1, 1.3.1, 1.3.2, 1.4.1 | PCI Req 1 addresses network traffic control between zones |
| AC-5 | Separation of Duties | 7.2.4 | PCI Req 7.2.4 requires appropriate separation of duties |
| AC-6 | Least Privilege | 7.2.1, 7.2.2, 7.2.5 | PCI Req 7 is explicitly built on least privilege / need-to-know |
| AC-7 | Unsuccessful Logon Attempts | 8.3.4 | PCI Req 8.3.4 requires lockout after no more than 10 invalid attempts |
| AC-11 | Device Lock | 8.2.8 | PCI Req 8.2.8 requires session timeout after 15 minutes of inactivity |
| AC-12 | Session Termination | 8.2.8 | Same PCI requirement covers idle session management |
| AC-14 | Permitted Actions Without Identification | 8.2.1 | PCI Req 8.2.1 requires all users to be assigned a unique ID |
| AC-17 | Remote Access | 8.4.2, 12.3.1 | PCI Req 8.4.2 requires MFA for remote CDE access |
| AC-18 | Wireless Access | 1.2.8, 11.2.1, 11.2.2 | PCI addresses wireless via network controls and rogue AP detection |
| AC-19 | Access Control for Mobile Devices | 12.3.1 | PCI Req 12.3.1 requires targeted risk analysis for technologies |
| AC-20 | Use of External Systems | 12.8, 12.9 | PCI Reqs 12.8/12.9 address third-party/service provider management |

### AT — Awareness and Training

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| AT-2 | Literacy Training and Awareness | 12.6.1, 12.6.2 | PCI Req 12.6 requires security awareness training at least annually |
| AT-3 | Role-Based Training | 12.6.3, 6.5.1 | PCI Req 12.6.3 covers role-specific content; Req 6.5.1 covers developer training |
| AT-4 | Training Records | 12.6.2 | PCI implicitly requires evidence but is less prescriptive than NIST |

### AU — Audit and Accountability

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| AU-2 | Event Logging | 10.2.1, 10.2.2 | PCI Req 10.2 specifies auditable events in detail |
| AU-3 | Content of Audit Records | 10.2.1.1, 10.2.1.2, 10.2.1.3 | PCI Req 10.2.1 requires user ID, event type, date/time, success/failure, affected data, origination |
| AU-4 | Audit Log Storage Capacity | 10.5.1 | PCI Req 10.5.1 requires retention of audit log history for 12 months |
| AU-5 | Response to Audit Logging Process Failures | 10.7.1, 10.7.2 | PCI Req 10.7 addresses failures in critical security controls including logging |
| AU-6 | Audit Record Review, Analysis, and Reporting | 10.4.1, 10.4.1.1 | PCI Req 10.4.1 requires daily review of audit logs |
| AU-8 | Time Stamps | 10.6.1, 10.6.2, 10.6.3 | PCI Req 10.6 requires time synchronization (NTP) |
| AU-9 | Protection of Audit Information | 10.3.1, 10.3.2, 10.3.3 | PCI Req 10.3 protects logs from modification and unauthorized access |
| AU-11 | Audit Record Retention | 10.5.1 | PCI Req 10.5.1 mandates 12 months retention, 3 months immediately available |
| AU-12 | Audit Record Generation | 10.2.1 | PCI Req 10.2 covers what events must generate audit records |

### CA — Assessment, Authorization, and Monitoring

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| CA-2 | Control Assessments | 11.3.1, 11.4.1, 12.4 | PCI requires annual assessments (ROC/SAQ); Req 11 covers testing |
| CA-7 | Continuous Monitoring | 10.4.1, 11.5.1, 11.5.2 | PCI requires daily log review and file integrity monitoring |
| CA-8 | Penetration Testing | 11.4.1, 11.4.2, 11.4.3 | PCI Req 11.4 mandates internal and external pen testing |
| CA-9 | Internal System Connections | 1.2.4, 1.2.5 | PCI Req 1 covers connections between trusted and untrusted networks |

### CM — Configuration Management

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| CM-2 | Baseline Configuration | 2.2.1 | PCI Req 2.2.1 requires configuration standards for all system components |
| CM-3 | Configuration Change Control | 6.5.1, 6.5.2 | PCI Req 6.5 requires change control procedures for system components |
| CM-6 | Configuration Settings | 2.2.2, 2.2.3, 2.2.4, 2.2.5 | PCI Req 2.2 requires hardening with specific sub-requirements |
| CM-7 | Least Functionality | 2.2.4, 2.2.5 | PCI Req 2.2.4 disables unnecessary services; 2.2.5 removes unnecessary functionality |
| CM-8 | System Component Inventory | 12.5.1 | PCI Req 12.5.1 requires inventory of in-scope system components |
| CM-10 | Software Usage Restrictions | 6.3.2 | PCI Req 6.3.2 requires inventory of custom and third-party software |
| CM-11 | User-Installed Software | 2.2.4, 2.2.5 | PCI limits unnecessary software and services |

### CP — Contingency Planning

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| CP-2 | Contingency Plan | 12.10.1 | PCI Req 12.10.1 requires an incident response plan (narrower than NIST CP) |
| CP-4 | Contingency Plan Testing | 12.10.2 | PCI Req 12.10.2 requires annual testing of the incident response plan |
| CP-9 | System Backup | 12.3.1 | PCI has limited backup requirements; covered under targeted risk analysis |
| CP-10 | System Recovery and Reconstitution | 12.10.1 | PCI addresses recovery within incident response. PCI lacks NIST's broader BIA, alternate site, and telecom continuity controls. |

### IA — Identification and Authentication

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| IA-2 | Identification and Authentication (Org Users) | 8.2.1, 8.3.1 | PCI Req 8.2.1 requires unique IDs; Req 8.3.1 covers authentication factors |
| IA-2(1) | MFA to Privileged Accounts | 8.4.1 | PCI Req 8.4.1 requires MFA for all non-console administrative access into the CDE |
| IA-2(2) | MFA to Non-Privileged Accounts | 8.4.2 | PCI Req 8.4.2 requires MFA for all remote network access |
| IA-4 | Identifier Management | 8.2.1, 8.2.2, 8.2.3 | PCI Req 8.2 covers user ID lifecycle management |
| IA-5 | Authenticator Management | 8.3.1, 8.3.5, 8.3.6, 8.3.7 | PCI Req 8.3 specifies password/passphrase requirements in detail |
| IA-5(1) | Password-Based Authentication | 8.3.6, 8.3.7 | PCI Req 8.3.6 requires minimum 12 characters; 8.3.7 forbids reuse of last 4 passwords |
| IA-6 | Authentication Feedback | 8.3.1 | PCI implicitly requires obscuring authentication feedback |
| IA-8 | Identification and Authentication (Non-Org Users) | 8.2.1, 8.2.2 | PCI Req 8 applies to all users including third parties |
| IA-11 | Re-authentication | 8.2.8 | PCI Req 8.2.8 covers session timeout and re-authentication |

### IR — Incident Response

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| IR-2 | Incident Response Training | 12.10.1 | PCI includes training within the IRP requirement |
| IR-3 | Incident Response Testing | 12.10.2 | PCI Req 12.10.2 requires annual IRP testing |
| IR-4 | Incident Handling | 12.10.4, 12.10.5 | PCI Req 12.10.4 covers personnel responsibilities; 12.10.5 covers monitoring/responding |
| IR-5 | Incident Monitoring | 12.10.5 | PCI Req 12.10.5 includes monitoring and responding to alerts |
| IR-6 | Incident Reporting | 12.10.1 | PCI requires notification procedures in IRP; card brand notification rules apply separately |
| IR-8 | Incident Response Plan | 12.10.1 | PCI Req 12.10.1 specifies required IRP elements |

### MA — Maintenance

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| MA-2 | Controlled Maintenance | 6.3.1 | PCI Req 6.3.1 addresses patching and security updates |
| MA-4 | Nonlocal Maintenance | 8.4.2 | Remote maintenance access maps to remote access MFA requirements |
| MA-5 | Maintenance Personnel | 8.2.1, 9.4.2 | PCI covers personnel identification and visitor management |

### MP — Media Protection

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| MP-2 | Media Access | 9.4.1, 9.4.2 | PCI Req 9.4 restricts access to media with cardholder data |
| MP-4 | Media Storage | 3.1.1, 9.4.3 | PCI Req 3 protects stored account data; Req 9.4 covers physical media |
| MP-5 | Media Transport | 9.4.3, 9.4.4 | PCI Req 9.4.3/9.4.4 cover media sent outside the facility |
| MP-6 | Media Sanitization | 3.1.1, 9.4.6, 9.4.7 | PCI Req 9.4.6/9.4.7 require destruction of media when no longer needed |
| MP-7 | Media Use | 9.4.1 | PCI Req 9.4 addresses physical media use restrictions |

### PE — Physical and Environmental Protection

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| PE-2 | Physical Access Authorizations | 9.2.1, 9.2.2 | PCI Req 9.2 defines physical access controls for CDE facilities |
| PE-3 | Physical Access Control | 9.2.1, 9.2.3, 9.2.4 | PCI Req 9.2 requires badge systems, locks, and access logging |
| PE-6 | Monitoring Physical Access | 9.2.4 | PCI Req 9.2.4 requires video cameras or access control mechanisms |
| PE-8 | Visitor Access Records | 9.3.1, 9.3.2, 9.3.3 | PCI Req 9.3 addresses visitor identification and management |
| PE-16 | Delivery and Removal | 9.4.3, 9.4.4 | PCI Req 9.4 covers media entering and leaving the facility |

### PL — Planning

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| PL-2 | System Security and Privacy Plans | 12.1.1 | PCI Req 12 addresses high-level security program; no SSP equivalent |
| PL-4 | Rules of Behavior | 12.1.1, 12.6.1 | PCI covers acceptable use via policies and training |

### PM — Program Management

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| PM-1 | Information Security Program Plan | 12.1.1, 12.4.1 | PCI Req 12 establishes program management; Req 12.4.1 adds executive responsibility for service providers |
| PM-9 | Risk Management Strategy | 12.3.1, 12.3.2 | PCI Req 12.3 requires targeted risk analysis methodology |
| PM-10 | Authorization Process | N/A | PCI has no ATO-equivalent process |
| PM-14 | Testing, Training, and Monitoring | 11.1.1, 12.6 | PCI covers testing and training across multiple requirements |

### PS — Personnel Security

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| PS-3 | Personnel Screening | 12.7.1 | PCI Req 12.7.1 requires background checks for CDE personnel |
| PS-4 | Personnel Termination | 8.2.4, 8.2.6 | PCI Req 8.2 covers revoking access upon termination |
| PS-5 | Personnel Transfer | 7.2.5 | PCI Req 7.2.5 covers access review for transferred personnel |

### PT — PII Processing and Transparency

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| PT-1 through PT-8 | PII Processing Controls | 3.1.1, 3.2.1 | PT family (new in Rev 5) focuses on privacy/PII transparency. PCI addresses cardholder data minimization via Req 3 but does not cover general privacy transparency. Limited direct mapping. |

### RA — Risk Assessment

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| RA-2 | Security Categorization | 12.5.2 | PCI Req 12.5.2 requires defining CDE scope (analogous to categorization) |
| RA-3 | Risk Assessment | 12.3.1, 12.3.2 | PCI Req 12.3.1 requires targeted risk analysis; 12.3.2 requires entity-wide risk assessment |
| RA-5 | Vulnerability Monitoring and Scanning | 6.3.1, 11.3.1, 11.3.2 | PCI Req 11.3 requires internal/external vulnerability scans; Req 6.3.1 covers patch management |
| RA-7 | Risk Response | 12.3.1 | PCI Req 12.3.1 covers risk treatment decisions |

### SA — System and Services Acquisition

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| SA-3 | System Development Life Cycle | 6.5.1, 6.5.2, 6.5.3 | PCI Req 6.5 addresses change control and SDLC processes |
| SA-8 | Security and Privacy Engineering Principles | 6.2.1 | PCI Req 6.2.1 requires bespoke/custom software developed securely |
| SA-9 | External System Services | 12.8, 12.9 | PCI Reqs 12.8/12.9 cover service provider management and agreements |
| SA-10 | Developer Configuration Management | 6.5.1, 6.5.4 | PCI Req 6.5 covers change management in development |
| SA-11 | Developer Testing and Evaluation | 6.2.3, 6.2.4 | PCI Req 6.2.3 covers code review; 6.2.4 addresses common vulnerability prevention |
| SA-15 | Development Process, Standards, and Tools | 6.2.1, 6.2.2 | PCI Req 6.2 covers secure development practices and standards |

### SC — System and Communications Protection

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| SC-4 | Information in Shared Resources | 3.3.1, 3.3.2 | PCI Req 3.3 covers SAD after authorization and PAN display masking |
| SC-7 | Boundary Protection | 1.2.1, 1.3.1, 1.3.2, 1.4.1, 1.4.4 | PCI Req 1 is the primary boundary protection requirement |
| SC-8 | Transmission Confidentiality and Integrity | 4.2.1, 4.2.1.1 | PCI Req 4 requires strong cryptography for CHD in transit |
| SC-12 | Cryptographic Key Establishment and Management | 3.6.1, 3.7.1 through 3.7.9 | PCI Req 3.6/3.7 cover key management procedures in detail |
| SC-13 | Cryptographic Protection | 3.5.1, 4.2.1 | PCI Req 3.5 covers encryption at rest; Req 4.2 covers encryption in transit |
| SC-23 | Session Authenticity | 8.2.8, 6.2.4 | PCI addresses session management across Reqs 6 and 8 |
| SC-28 | Protection of Information at Rest | 3.5.1, 3.5.1.1, 3.5.1.2 | PCI Req 3.5 requires rendering PAN unreadable via cryptography |

### SI — System and Information Integrity

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| SI-2 | Flaw Remediation | 6.3.1, 6.3.3 | PCI Req 6.3.1 requires timely installation of security patches |
| SI-3 | Malicious Code Protection | 5.2.1, 5.2.2, 5.2.3, 5.3.1 | PCI Req 5 comprehensively addresses anti-malware |
| SI-4 | System Monitoring | 10.4.1, 10.4.1.1, 11.5.1 | PCI Req 10.4 and 11.5 cover monitoring and alerting |
| SI-5 | Security Alerts, Advisories, and Directives | 6.3.1 | PCI Req 6.3.1 covers awareness of new vulnerabilities |
| SI-7 | Software, Firmware, and Information Integrity | 11.5.2, 11.5.2.1 | PCI Req 11.5.2 requires file integrity monitoring (FIM) |
| SI-10 | Information Input Validation | 6.2.4 | PCI Req 6.2.4 addresses injection and input validation |
| SI-11 | Error Handling | 6.2.4 | PCI Req 6.2.4 covers preventing information leakage in errors |
| SI-16 | Memory Protection | 6.2.4 | PCI Req 6.2.4 addresses memory-related vulnerabilities |

### SR — Supply Chain Risk Management

| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |
|-------------|-------|----------------------|----------------|
| SR-2 | Supply Chain Risk Management Plan | 12.8.1 | PCI Req 12.8 covers third-party risk but not a formal SCRM plan |
| SR-3 | Supply Chain Controls and Processes | 6.3.2, 12.8.2 | PCI Req 6.3.2 covers third-party software inventory; 12.8.2 covers SP agreements |
| SR-6 | Supplier Assessments and Reviews | 12.8.4 | PCI Req 12.8.4 requires monitoring SP compliance status annually |

## NIST Families with Limited PCI DSS Coverage

The following NIST families have minimal or no direct counterparts in PCI DSS:

| NIST Family | Coverage Gap |
|-------------|-------------|
| **AT (Awareness and Training)** | PCI Req 12.6 covers security awareness but is less granular than NIST AT enhancements |
| **PL (Planning)** | PCI has no SSP concept; the ROC/SAQ serves as documentation but is assessment-focused, not plan-focused |
| **PM (Program Management)** | PCI Req 12 covers program elements but lacks NIST's enterprise architecture, insider threat, and strategic planning controls |
| **PS (Personnel Security)** | PCI Req 12.7 requires background checks but does not address position risk designation, formal agreements, or sanctions |
| **PT (PII Processing)** | PCI addresses cardholder data specifically, not general PII processing or privacy transparency |

## PCI DSS Requirements Spanning Multiple NIST Families

Several PCI DSS requirements draw from controls across multiple NIST families, making one-to-one mapping insufficient:

| PCI DSS Requirement | NIST Families Involved | Explanation |
|---------------------|----------------------|-------------|
| **Req 3 (Protect Stored Account Data)** | MP, SC, CM, SA | Combines media protection, cryptographic controls, configuration standards, and data retention logic |
| **Req 6 (Secure Systems and Software)** | SA, SI, CM, RA | Spans SDLC, vulnerability management, configuration, and risk assessment |
| **Req 8 (Identify and Authenticate)** | IA, AC | Combines identification/authentication and access control concepts |
| **Req 11 (Test Security)** | CA, RA, SI | Merges assessment, vulnerability scanning, and integrity monitoring |
| **Req 12 (Organizational Policies)** | PL, PM, AT, IR, PS, RA | Consolidates governance, training, incident response, personnel, and risk assessment |

## Quick Cross-Reference: PCI DSS to Primary NIST Families

| PCI DSS Req | Primary NIST Families | Secondary NIST Families |
|-------------|----------------------|------------------------|
| 1 | SC, AC | CM |
| 2 | CM | SC, SA |
| 3 | MP, SC | CM, SA |
| 4 | SC | IA |
| 5 | SI | CM |
| 6 | SA, SI | CM, RA |
| 7 | AC | PS |
| 8 | IA, AC | MA |
| 9 | PE, MP | PS |
| 10 | AU | SI |
| 11 | CA, RA, SI | SC |
| 12 | PL, PM, IR, AT, PS, RA | CP, SR |

## Practical Mapping Guidance

1. **Start with PCI DSS scope**: Define the CDE boundary first. Only map NIST controls relevant to systems within or connected to the CDE.
2. **Use NIST Moderate as the reference baseline**: Most PCI-compliant environments align with NIST Moderate in rigor.
3. **Leverage the customized approach**: PCI DSS v4.0.1's customized approach parallels NIST's tailoring guidance -- both allow alternative implementations that meet the stated objective.
4. **Account for PCI-specific prescriptiveness**: PCI specifies exact parameter values (12-character passwords, 15-minute timeouts, 90-day review cycles). NIST defers to organization-defined parameters. Ensure NIST parameter values meet or exceed PCI thresholds.
5. **Address gaps in both directions**: Organizations subject to both must satisfy the more restrictive requirement. NIST requires broader scope (entire system); PCI requires more specific technical configurations within the CDE.
