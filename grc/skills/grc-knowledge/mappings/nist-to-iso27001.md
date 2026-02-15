# NIST 800-53 Rev 5 to ISO 27001:2022 Mapping

## Overview

NIST SP 800-53 Rev 5 and ISO/IEC 27001:2022 are the two most widely referenced information security frameworks globally. NIST 800-53 provides a catalog of 1,189 controls across 20 families, used primarily by U.S. federal agencies. ISO 27001:2022 defines an ISMS through 10 management system clauses and 93 Annex A controls in 4 themes.

This mapping enables organizations pursuing dual compliance to identify overlaps, reduce duplicated audit evidence, and pinpoint gaps. **Mapping direction**: NIST 800-53 families --> ISO 27001:2022 Annex A controls.

## Key Differences in Approach

| Dimension | NIST 800-53 Rev 5 | ISO 27001:2022 |
|-----------|-------------------|----------------|
| **Philosophy** | Prescriptive baselines by impact level (Low/Moderate/High) | Risk-based; controls determined via Statement of Applicability (SoA) |
| **Control count** | 1,189 controls and enhancements, 20 families | 93 Annex A controls, 4 themes |
| **Granularity** | Highly granular with numbered enhancements (e.g., AC-2(1)-AC-2(13)) | Broader objectives; implementation detail left to the organization |
| **Baselines** | Predefined per FIPS 199 impact level (SP 800-53B) | No baselines; all 93 controls considered and justified via SoA |
| **Management system** | PM family covers program management; no formal ISMS | Clauses 4-10 define a full PDCA management system |
| **Certification** | No direct certification; used within RMF for ATO decisions | Third-party certification by accredited CBs |
| **Parameters** | Organization-defined parameters (ODPs) | No prescribed parameters; risk-based |
| **Assessment** | SP 800-53A detailed assessment procedures | ISO 19011/27006 guide audits; less prescriptive |

**ISO 27001:2022 Annex A themes**: A.5 Organizational (37 controls), A.6 People (8), A.7 Physical (14), A.8 Technological (34).

## Comprehensive Mapping by NIST Family

### AC -- Access Control --> A.5.15-A.5.18, A.8.1-A.8.5

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| AC-2 | Account Management | A.5.16, A.5.18 | Identity management, Access rights | Full |
| AC-3 | Access Enforcement | A.5.15 | Access control | Full |
| AC-4 | Information Flow Enforcement | A.8.22, A.5.14 | Web filtering, Information transfer | Partial |
| AC-5 | Separation of Duties | A.5.3 | Segregation of duties | Full |
| AC-6 | Least Privilege | A.5.15, A.8.2 | Access control, Privileged access rights | Full |
| AC-7 | Unsuccessful Logon Attempts | A.8.5 | Secure authentication | Partial |
| AC-17 | Remote Access | A.6.7, A.8.5 | Remote working, Secure authentication | Full |
| AC-19 | Access Control for Mobile Devices | A.8.1 | User endpoint devices | Full |
| AC-20 | Use of External Systems | A.5.19 | Info security in supplier relationships | Partial |

ISO covers core access control through A.5.15-A.5.18 and A.8.2-A.8.5 but lacks NIST granular enhancements (e.g., AC-2(1) automated account management, AC-6(5) privileged accounts).

### AT -- Awareness and Training --> A.6.3

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| AT-2 | Literacy Training and Awareness | A.6.3 | Info security awareness, education and training | Full |
| AT-3 | Role-Based Training | A.6.3 | Info security awareness, education and training | Partial |
| AT-4 | Training Records | A.6.3 | Info security awareness, education and training | Implicit |

ISO A.6.3 consolidates all training requirements. NIST distinguishes general awareness from role-based training and explicitly requires training records.

### AU -- Audit and Accountability --> A.8.15-A.8.17

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| AU-2, AU-3, AU-12 | Event Logging, Content, Generation | A.8.15 | Logging | Full |
| AU-4, AU-9, AU-11 | Storage, Protection, Retention | A.8.15 | Logging | Implicit |
| AU-6, AU-7 | Review/Analysis, Reduction | A.8.16 | Monitoring activities | Full |
| AU-8 | Time Stamps | A.8.17 | Clock synchronization | Full |

Clean mapping. NIST enhancements like AU-6(1) automated review and AU-9(4) privileged access to logs have no direct ISO equivalent.

### CA -- Assessment, Authorization, and Monitoring --> A.5.35-A.5.36

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| CA-2 | Control Assessments | A.5.35 | Independent review of info security | Full |
| CA-5 | Plan of Action and Milestones | A.5.36 | Compliance with policies/rules/standards | Partial |
| CA-6 | Authorization | -- | (Clause 5.1 Leadership commitment) | Weak |
| CA-7 | Continuous Monitoring | A.5.36 | Compliance with policies/rules/standards | Partial |
| CA-8 | Penetration Testing | A.8.34 | Protection of info systems during audit testing | Partial |

Heavily RMF-tied. No ISO equivalent to CA-6 (ATO decisions) or formal POA&M tracking. ISO uses Clause 9 (Performance Evaluation) and Clause 10 (Improvement) instead.

### CM -- Configuration Management --> A.8.9, A.8.19, A.8.32

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| CM-2, CM-6, CM-9 | Baseline, Settings, CM Plan | A.8.9 | Configuration management | Full |
| CM-3, CM-4 | Change Control, Impact Analysis | A.8.32 | Change management | Full |
| CM-7, CM-11 | Least Functionality, User Software | A.8.19 | Installation of software on operational systems | Partial |
| CM-8 | System Component Inventory | A.5.9 | Inventory of info and associated assets | Full |
| CM-10 | Software Usage Restrictions | A.5.10 | Acceptable use of info and associated assets | Partial |

A.8.9 (new in 2022) provides strong alignment. A.8.32 covers change control.

### CP -- Contingency Planning --> A.5.29-A.5.30, A.8.13-A.8.14

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| CP-2 | Contingency Plan | A.5.29, A.5.30 | Info security during disruption, ICT readiness for BC | Full |
| CP-4 | Contingency Plan Testing | A.5.30 | ICT readiness for business continuity | Full |
| CP-6, CP-7 | Alternate Storage/Processing Site | A.8.14 | Redundancy of info processing facilities | Full |
| CP-9 | System Backup | A.8.13 | Information backup | Full |
| CP-10 | System Recovery and Reconstitution | A.5.30 | ICT readiness for business continuity | Full |

Strong alignment. A.5.30 (new in 2022) significantly improved ICT continuity coverage.

### IA -- Identification and Authentication --> A.5.16-A.5.17, A.8.5

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| IA-2 | ID and Auth (Org Users) | A.8.5 | Secure authentication | Full |
| IA-2(1), IA-2(2) | MFA (Privileged/Non-Privileged) | A.8.5 | Secure authentication | Partial |
| IA-4 | Identifier Management | A.5.16 | Identity management | Full |
| IA-5 | Authenticator Management | A.5.17 | Authentication information | Full |
| IA-8 | ID and Auth (Non-Org Users) | A.5.16 | Identity management | Partial |
| IA-12 | Identity Proofing | A.5.16 | Identity management | Weak |

NIST is far more prescriptive about MFA (IA-2(1), IA-2(2)), authenticator strength (IA-5(1)), and identity proofing (IA-12). ISO A.8.5 mentions MFA but does not mandate it.

### IR -- Incident Response --> A.5.24-A.5.28, A.6.8

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| IR-2, IR-3, IR-8 | Training, Testing, Plan | A.5.24 | Incident management planning and preparation | Full |
| IR-4, IR-5 | Handling, Monitoring | A.5.25, A.5.26 | Assessment/decision, Response to incidents | Full |
| IR-6 | Incident Reporting | A.5.26, A.6.8 | Response to incidents, Event reporting | Full |

Excellent alignment. A.5.27 (Learning from incidents) and A.5.28 (Collection of evidence) further strengthen coverage.

### MA -- Maintenance --> A.7.13

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| MA-2 | Controlled Maintenance | A.7.13 | Equipment maintenance | Full |
| MA-3 | Maintenance Tools | A.7.13 | Equipment maintenance | Partial |
| MA-4 | Nonlocal Maintenance | A.8.5 | Secure authentication | Weak |
| MA-5 | Maintenance Personnel | A.6.1 | Screening | Partial |

MA-4 (remote maintenance) has no direct ISO equivalent.

### MP -- Media Protection --> A.7.10, A.5.13

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| MP-2, MP-4, MP-5, MP-6, MP-7 | Access, Storage, Transport, Sanitization, Use | A.7.10 | Storage media | Full |
| MP-3 | Media Marking | A.5.13 | Labelling of information | Full |

ISO A.7.10 consolidates the media lifecycle. Strong coverage.

### PE -- Physical and Environmental Protection --> A.7.1-A.7.14

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| PE-2, PE-3, PE-8 | Access Auth, Access Control, Visitors | A.7.1, A.7.2 | Physical security perimeters, Physical entry | Full |
| PE-6 | Monitoring Physical Access | A.7.4 | Physical security monitoring | Full |
| PE-9, PE-11 | Power Equipment, Emergency Power | A.7.11 | Supporting utilities | Full |
| PE-10, PE-12-PE-15 | Emergency/Environmental Controls | A.7.5 | Protecting against physical/environmental threats | Full |
| PE-17 | Alternate Work Site | A.6.7 | Remote working | Full |

Comprehensive coverage. A.7.4 (new in 2022) strengthened alignment with PE-6.

### PL -- Planning --> Clause 6

PL-2 (SSP), PL-10 (Baseline Selection), PL-11 (Baseline Tailoring) map weakly to Clause 6.1 (risk-based planning). PL-4 (Rules of Behavior) maps fully to A.5.10 (Acceptable use). No ISO equivalent to formal SSPs or baseline selection/tailoring; ISO uses risk treatment plans and SoA instead.

### PM -- Program Management --> Clauses 4-10

PM maps primarily to ISMS management system clauses rather than Annex A. PM-2 (Leadership Role) maps to Clause 5.3; PM-9 (Risk Strategy) maps to Clause 6.1; PM-3 (Resources) maps to Clause 7.1. **PM-10 (Authorization Process) has no ISO equivalent** because ISO does not use the ATO construct.

### PS -- Personnel Security --> A.6.1-A.6.5

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| PS-3 | Personnel Screening | A.6.1 | Screening | Full |
| PS-4, PS-5 | Termination, Transfer | A.6.5 | Responsibilities after termination/change | Full |
| PS-6 | Access Agreements | A.6.2 | Terms and conditions of employment | Full |
| PS-8 | Personnel Sanctions | A.6.4 | Disciplinary process | Full |

Good coverage. A.6.6 (NDAs) adds an ISO control not directly in NIST PS.

### PT -- PII Processing and Transparency --> A.5.34

PT-2 through PT-5 (Authority, Purposes, Consent, Privacy Notice) map partially to A.5.34 (Privacy and protection of PII). Coverage is minimal; organizations should adopt ISO 27701 for comprehensive privacy management.

### RA -- Risk Assessment --> A.5.7, A.8.8, Clause 6.1

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| RA-3 | Risk Assessment | -- | (Clause 6.1.2 Risk assessment) | Full |
| RA-5 | Vulnerability Monitoring/Scanning | A.8.8 | Management of technical vulnerabilities | Full |
| RA-7 | Risk Response | -- | (Clause 6.1.3 Risk treatment) | Full |
| RA-10 | Threat Hunting | A.5.7 | Threat intelligence | Partial |

ISO addresses risk through Clause 6.1 rather than Annex A. A.5.7 (new in 2022) aligns with threat awareness. NIST RA-2 (FIPS 199 categorization) has no ISO equivalent.

### SA -- System and Services Acquisition --> A.5.19-A.5.23, A.8.25-A.8.31

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| SA-3 | SDLC | A.8.25 | Secure development life cycle | Full |
| SA-4 | Acquisition Process | A.5.19, A.5.20 | Supplier relationships, Supplier agreements | Full |
| SA-8 | Security Engineering Principles | A.8.27 | Secure system architecture and engineering | Full |
| SA-9 | External System Services | A.5.21, A.5.22 | ICT supply chain, Supplier monitoring/review | Full |
| SA-11 | Developer Testing | A.8.29 | Security testing in dev and acceptance | Full |
| SA-15 | Development Process/Standards | A.8.25, A.8.28 | Secure SDLC, Secure coding | Full |

ISO 2022 significantly strengthened SDLC controls. A.8.26 (App security requirements), A.8.30 (Outsourced development), A.8.31 (Separation of dev/test/prod) round out coverage.

### SC -- System and Communications Protection --> A.8.20-A.8.24

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| SC-7 | Boundary Protection | A.8.20, A.8.21 | Networks security, Network services security | Full |
| SC-8 | Transmission Confidentiality/Integrity | A.8.24, A.5.14 | Use of cryptography, Information transfer | Full |
| SC-12, SC-13 | Key Management, Crypto Protection | A.8.24 | Use of cryptography | Full |
| SC-28 | Protection of Information at Rest | A.8.24 | Use of cryptography | Full |
| SC-5 | DoS Protection | A.8.20 | Networks security | Partial |
| SC-39 | Process Isolation | -- | (No direct equivalent) | Weak |

NIST SC is among the largest families. Low-level controls (SC-39 process isolation, SC-20/SC-22 DNS security) exceed ISO Annex A specificity.

### SI -- System and Information Integrity --> A.8.7-A.8.8, A.8.16

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| SI-2 | Flaw Remediation | A.8.8 | Management of technical vulnerabilities | Full |
| SI-3 | Malicious Code Protection | A.8.7 | Protection against malware | Full |
| SI-4 | System Monitoring | A.8.16 | Monitoring activities | Full |
| SI-5 | Security Alerts/Advisories | A.5.7 | Threat intelligence | Full |
| SI-10 | Information Input Validation | A.8.28 | Secure coding | Partial |
| SI-16 | Memory Protection | -- | (No direct equivalent) | None |

SI-16 (Memory protection) and SI-7 integrity enhancements have no ISO equivalents.

### SR -- Supply Chain Risk Management --> A.5.19-A.5.22

| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |
|-------------|-----------|-------------|-----------|----------|
| SR-2 | SCRM Plan | A.5.19 | Info security in supplier relationships | Full |
| SR-3 | Supply Chain Controls | A.5.20 | Addressing info security in supplier agreements | Full |
| SR-5 | Acquisition Strategies | A.5.21 | Managing info security in the ICT supply chain | Full |
| SR-6 | Supplier Assessments | A.5.22 | Monitoring/review/change mgmt of supplier services | Full |
| SR-11 | Component Authenticity | A.5.21 | Managing info security in the ICT supply chain | Partial |

A.5.23 (cloud services) adds cloud-specific supplier management. NIST SR enhancements around provenance (SR-4) and tamper resistance (SR-9) exceed ISO coverage.

## Gap Analysis

### NIST Families with Weak ISO 27001 Coverage

| NIST Family | Gap Description |
|-------------|-----------------|
| **CA** | No ISO concept of ATO. CA-6 (Authorization), CA-5 (POA&M), CA-7 (ConMon) map loosely to Clauses 9-10. |
| **PL** | No ISO equivalent to SSPs or baseline selection/tailoring. ISO uses risk treatment plans and SoA. |
| **PM** | Maps to ISMS clauses, not Annex A. PM-10 (Authorization process) has no equivalent. |
| **PT** | A.5.34 provides minimal coverage. ISO 27701 needed for comprehensive privacy. |
| **SC** | Low-level technical controls (SC-39, SC-20/SC-22, SC-26 decoys) have no Annex A equivalents. |
| **SI** | SI-16 (Memory protection), SI-7 integrity enhancements have no ISO equivalents. |

### ISO 27001 Controls with Weak NIST 800-53 Coverage

| ISO Control | Gap Description |
|-------------|-----------------|
| **A.5.7** Threat intelligence | Partially covered by RA-3 and RA-10; NIST lacks a dedicated threat intelligence base control. |
| **A.5.23** Cloud services security | NIST uses FedRAMP overlays rather than a base catalog cloud control. |
| **A.5.31** Legal/regulatory requirements | ISO treats legal/regulatory identification as standalone; NIST only tangentially addresses via PM-8. |
| **A.5.32** Intellectual property rights | No direct NIST control for IP protection. |
| **A.6.7** Remote working | NIST AC-17 covers remote access technically; ISO A.6.7 covers broader organizational policy. |
| **A.8.23** Web filtering | NIST uses AC-4 (information flow enforcement); ISO provides a dedicated control. |

## ISMS Clauses 4-10 vs. NIST PM Family

ISO management system clauses define governance that NIST covers through PM family and RMF (SP 800-37).

| ISO 27001 Clause | Clause Title | NIST 800-53 Equivalent |
|------------------|-------------|----------------------|
| 4.1 | Understanding the organization and its context | PM-11 (Mission/Business Process Definition) |
| 4.2 | Needs of interested parties | PM-11, SA-2 |
| 4.3 | Determining ISMS scope | PL-2 (SSP boundary definition) |
| 4.4 | Information security management system | PM-1 (Information Security Program Plan) |
| 5.1 | Leadership and commitment | PM-2 (Senior Information Security Officer) |
| 5.2 | Policy | PL-1, all *-1 policy controls |
| 5.3 | Organizational roles and authorities | PM-2, PM-13 (Security Workforce) |
| 6.1 | Actions to address risks and opportunities | RA-3 (Risk Assessment), PM-9 (Risk Management Strategy) |
| 6.1.3 | Information security risk treatment | RA-7 (Risk Response), PL-10/PL-11 (Baseline Selection/Tailoring) |
| 6.2 | Objectives and planning | PM-1, PM-9 |
| 7.1 | Resources | PM-3 (Information Security Resources), SA-2 |
| 7.2 | Competence | AT-3 (Role-Based Training) |
| 7.3 | Awareness | AT-2 (Literacy Training and Awareness) |
| 7.5 | Documented information | All *-1 policy controls, PL-2 (SSP) |
| 8.2 | Information security risk assessment | RA-3 (Risk Assessment) |
| 8.3 | Information security risk treatment | RA-7, CA-5 (POA&M as risk treatment tracker) |
| 9.1 | Monitoring, measurement, analysis | CA-7 (Continuous Monitoring), PM-6 (Measures of Performance) |
| 9.2 | Internal audit | CA-2 (Control Assessments) |
| 9.3 | Management review | PM-1, CA-7 |
| 10.1 | Continual improvement | CA-5 (POA&M), PM-1 |
| 10.2 | Nonconformity and corrective action | CA-5 (POA&M), SI-2 (Flaw Remediation) |

**Key insight**: A mature NIST 800-53 implementation provides most technical controls for ISO Annex A, but the organization must formalize the PDCA management system (Clauses 4-10): risk assessment methodology, SoA, management review minutes, internal audit program, and continual improvement process. Conversely, an ISO-certified organization pursuing NIST compliance must adopt prescriptive baselines, define ODPs, and produce RMF artifacts (SSP, SAR, POA&M).

## References

- NIST SP 800-53 Rev 5: Security and Privacy Controls for Information Systems and Organizations
- NIST SP 800-53B: Control Baselines for Information Systems and Organizations
- ISO/IEC 27001:2022: Information security management systems -- Requirements
- ISO/IEC 27002:2022: Information security controls (Annex A implementation guidance)
- ISO/IEC 27701:2019: Privacy information management extension to ISO 27001/27002
- OSCAL-based control mapping resources (automate.fedramp.gov)
