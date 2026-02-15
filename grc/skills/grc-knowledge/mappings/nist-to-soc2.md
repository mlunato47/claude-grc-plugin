# NIST 800-53 Rev 5 to SOC 2 Trust Services Criteria Mapping

## Overview

This document maps NIST SP 800-53 Rev 5 control families to AICPA SOC 2 Trust Services Criteria (TSC) 2017 (with 2022 revisions). NIST 800-53 is a prescriptive control catalog for federal systems; SOC 2 is a principle-based framework for service organizations built around five Trust Services Categories. Despite different origins (federal vs. commercial), substantial overlap exists because both address the same fundamental security and operational objectives.

### SOC 2 Trust Services Categories

| Category | Prefix | Criteria Count | Focus |
|----------|--------|----------------|-------|
| Common Criteria (Security) | CC | CC1.1-CC9.2 | Required for all SOC 2 engagements; security is the baseline |
| Availability | A | A1.1-A1.3 | System availability commitments and SLAs |
| Processing Integrity | PI | PI1.1-PI1.5 | Completeness, accuracy, timeliness of processing |
| Confidentiality | C | C1.1-C1.2 | Protection of confidential information |
| Privacy | P | P1.1-P8.1 | Collection, use, retention, disclosure of personal information |

### SOC 2 Common Criteria Structure (CC Series)

| CC Group | Title | COSO Principle Alignment |
|----------|-------|--------------------------|
| CC1.1-CC1.5 | Control Environment | COSO Principles 1-5 |
| CC2.1-CC2.3 | Communication and Information | COSO Principles 13-15 |
| CC3.1-CC3.4 | Risk Assessment | COSO Principles 6-9 |
| CC4.1-CC4.2 | Monitoring Activities | COSO Principles 16-17 |
| CC5.1-CC5.3 | Control Activities | COSO Principles 10-12 |
| CC6.1-CC6.8 | Logical and Physical Access Controls | TSC-specific |
| CC7.1-CC7.5 | System Operations | TSC-specific |
| CC8.1 | Change Management | TSC-specific |
| CC9.1-CC9.2 | Risk Mitigation | TSC-specific |

## Mapping Methodology

1. **Directionality** -- NIST-to-SOC 2 (forward) with a reverse mapping section at the end. NIST is the source framework due to finer granularity.
2. **Granularity mismatch** -- A single SOC 2 criterion often maps to an entire NIST family or multiple controls. SOC 2 is intentionally broad and outcome-oriented; NIST is specific and implementation-prescriptive.
3. **Coverage levels** -- Full (SOC 2 criterion fully addresses the NIST objective), Partial (addresses in principle but not with NIST specificity), or Minimal (tangential coverage only).
4. **Base controls only** -- Mappings reference NIST base controls (e.g., AC-2), not enhancements (e.g., AC-2(1)), unless an enhancement is critical to the mapping.
5. **SOC 2 flexibility** -- SOC 2 auditors evaluate design suitability and operating effectiveness. The same criterion can be satisfied by different implementations. NIST specifies what must be done; SOC 2 specifies what must be achieved.

## Comprehensive Mapping by NIST Family

### AC -- Access Control

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| AC-1 (Policy and Procedures) | CC1.1, CC5.2 | Full | Documented access control policies as part of control environment |
| AC-2 (Account Management) | CC6.1, CC6.2 | Full | Provisioning, deprovisioning, periodic access review |
| AC-3 (Access Enforcement) | CC6.1, CC6.3 | Full | Logical access restrictions based on authorization |
| AC-4 (Information Flow Enforcement) | CC6.1, CC6.7 | Partial | Data flow controls covered but not at NIST boundary-level specificity |
| AC-5 (Separation of Duties) | CC5.1, CC6.1 | Full | SOC 2 explicitly requires segregation of duties |
| AC-6 (Least Privilege) | CC6.1, CC6.3 | Full | Principle of least privilege is core to CC6 |
| AC-7 (Unsuccessful Logon Attempts) | CC6.1 | Full | Account lockout policies expected under logical access |
| AC-17 (Remote Access) | CC6.1, CC6.6, CC6.7 | Full | VPN, remote access controls, encrypted transmission |
| AC-18, AC-19 (Wireless and Mobile) | CC6.1, CC6.6, CC6.8 | Partial | Wireless and MDM controls loosely covered under general access |
| AC-20 (Use of External Systems) | CC6.6, CC9.2 | Partial | Third-party/vendor access addressed but not at NIST granularity |
| AC-22 (Publicly Accessible Content) | CC6.1 | Minimal | Public content authorization not specifically addressed |

### AT -- Awareness and Training

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| AT-1, AT-2 (Policy and Awareness Training) | CC1.4, CC2.2 | Full | Security awareness training is a common SOC 2 control activity |
| AT-3 (Role-Based Training) | CC1.4 | Partial | SOC 2 expects training but does not mandate role-specific curricula |
| AT-4 (Training Records) | CC1.4 | Partial | Evidence of completion expected; retention less prescribed |

### AU -- Audit and Accountability

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| AU-2, AU-3, AU-12 (Event Logging and Content) | CC7.1, CC7.2 | Full | Defined auditable events, sufficient log detail, audit record generation |
| AU-6 (Review, Analysis, and Reporting) | CC7.2, CC4.1 | Full | Log review and monitoring are core SOC 2 expectations |
| AU-9 (Protection of Audit Information) | CC7.1 | Full | Integrity and access restrictions on log data |
| AU-4, AU-11 (Storage and Retention) | CC7.1 | Partial | Implicitly covered; NIST is more prescriptive on sizing and retention periods |
| AU-5 (Logging Process Failures) | CC7.1, CC7.2 | Partial | Alerting on logging failures is expected but not explicitly required |
| AU-7 (Report Generation) | CC7.2 | Partial | SIEM/log aggregation common but not prescriptively required |

### CA -- Assessment, Authorization, and Monitoring

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| CA-1, CA-2 (Policy and Assessments) | CC4.1, CC4.2 | Full | SOC 2 Type II is itself a control assessment; internal assessments expected |
| CA-5 (POA&M) | CC4.2 | Partial | Remediation tracking expected but POA&M as a formal artifact is NIST-specific |
| CA-7 (Continuous Monitoring) | CC4.1, CC7.1, CC7.2 | Partial | SOC 2 expects ongoing monitoring but not ISCM-level programs |

### CM -- Configuration Management

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| CM-1 through CM-5 (Change Control Process) | CC8.1, CC6.1, CC3.4 | Full | Policy, baselines, change control, impact analysis, deployment restrictions -- all core SOC 2 |
| CM-6 (Configuration Settings) | CC7.1, CC8.1 | Partial | Hardening standards expected but specifics less prescribed |
| CM-7 (Least Functionality) | CC6.1, CC7.1 | Partial | Disabling unnecessary services/ports is expected practice |
| CM-8 (Component Inventory) | CC7.1 | Partial | Asset inventory expected but NIST is more prescriptive |
| CM-10 (Software Usage Restrictions) | CC6.1 | Minimal | License compliance not a primary SOC 2 focus |

### CP -- Contingency Planning

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| CP-1, CP-2 (Policy and Contingency Plan) | A1.1, A1.2, CC9.1 | Full | BCP/DR policy and documented recovery plans (when Availability in scope) |
| CP-4 (Contingency Plan Testing) | A1.2, A1.3 | Full | Annual DR/BCP testing is standard SOC 2 expectation |
| CP-6, CP-7 (Alternate Sites) | A1.2, A1.3 | Full | Geographic redundancy, failover capabilities |
| CP-9 (System Backup) | A1.2 | Full | Backup procedures, frequency, and validation |
| CP-10 (Recovery and Reconstitution) | A1.2, A1.3 | Full | Recovery procedures and RTO/RPO commitments |
| CP-3 (Contingency Training) | A1.2 | Partial | Training expectations exist but less formalized than NIST |

### IA -- Identification and Authentication

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| IA-2 (User Identification and Authentication) | CC6.1, CC6.2 | Full | Unique user identification and authentication |
| IA-2(1), IA-2(2) (MFA) | CC6.1 | Full | MFA for privileged and non-privileged accounts widely expected |
| IA-4 (Identifier Management) | CC6.1, CC6.2 | Full | Unique identifiers, prevention of reuse |
| IA-5 (Authenticator Management) | CC6.1, CC6.3 | Full | Password policies, credential rotation, secure storage |
| IA-3 (Device Authentication) | CC6.1 | Partial | Device-level authentication less commonly assessed in SOC 2 |
| IA-8 (Non-Organizational Users) | CC6.1, CC6.2 | Full | External user authentication requirements |

### IR -- Incident Response

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| IR-1, IR-8 (IR Policy and Plan) | CC7.3, CC7.4 | Full | Documented incident response policy and plan |
| IR-3 (IR Testing) | CC7.3, CC7.4 | Partial | SOC 2 expects IR readiness but has no explicit IR testing criterion; CC7.4 covers incident response execution |
| IR-4 (Incident Handling) | CC7.3, CC7.4 | Full | Detection, analysis, containment, eradication, recovery |
| IR-5, IR-6 (Monitoring and Reporting) | CC7.4, CC7.5, CC2.3 | Full | Incident tracking, notification to affected parties and regulators |
| IR-2 (IR Training) | CC7.3 | Partial | SOC 2 expects IR capability but training specifics less prescribed |

### MA -- Maintenance (Limited SOC 2 Coverage)

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| MA-1, MA-2, MA-3 | CC7.1 | Minimal | SOC 2 has no dedicated maintenance criteria; tangentially covered under system operations |
| MA-4 (Nonlocal Maintenance) | CC6.1, CC6.7 | Partial | Remote maintenance sessions fall under remote access controls |
| MA-5 (Maintenance Personnel) | CC6.2, CC6.4 | Partial | Third-party maintenance personnel covered under vendor access |

### MP -- Media Protection (Limited SOC 2 Coverage)

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| MP-1, MP-2, MP-4 | CC6.5, C1.1 | Partial | Data handling and storage policies; not media-specific |
| MP-3 (Media Marking) | -- | Minimal | No SOC 2 equivalent for media labeling |
| MP-5 (Media Transport) | CC6.5, CC6.7 | Partial | Digital transport via encryption; physical transport not addressed |
| MP-6 (Media Sanitization) | CC6.5 | Partial | Data destruction expected but less prescriptive than NIST |

### PE -- Physical and Environmental Protection

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| PE-2, PE-3 (Physical Access) | CC6.4 | Full | Badge/biometric access, authorization lists |
| PE-6, PE-8 (Monitoring and Visitors) | CC6.4 | Full | CCTV, access logs, visitor escort procedures |
| PE-9 through PE-15 (Environmental) | A1.1 | Partial | Power, fire, HVAC, water damage -- covered tangentially under Availability |
| PE-12 (Emergency Lighting), PE-17 (Alternate Work Site) | -- | Minimal | Not meaningfully addressed by SOC 2 |

### PL -- Planning

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| PL-1, PL-4 (Policy and Rules of Behavior) | CC1.1, CC1.4, CC1.5, CC5.2 | Full | Security policies, acceptable use, codes of conduct |
| PL-2 (System Security Plans) | CC1.1 | Partial | SOC 2 uses system descriptions instead of SSPs |
| PL-10 (Baseline Selection) | -- | Minimal | Baseline selection is NIST-specific |

### PM -- Program Management

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| PM-1, PM-2, PM-9 (Program, Leadership, Risk Strategy) | CC1.1-CC1.3, CC3.1, CC9.1 | Full | Governance, board oversight, CISO, enterprise risk management |
| PM-10 (Authorization Process) | CC3.2 | Partial | SOC 2 does not have a formal authorization lifecycle |

### PS -- Personnel Security

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| PS-3 (Personnel Screening) | CC1.4 | Full | Background checks for employees with system access |
| PS-4, PS-5, PS-6 (Termination, Transfer, Agreements) | CC6.2, CC6.3 | Full | Access revocation, role-change review, NDAs |
| PS-7 (External Personnel) | CC6.2, CC9.2 | Full | Contractor and vendor personnel requirements |

### PT -- PII Processing and Transparency

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| PT-1, PT-5 (Policy and Privacy Notice) | P1.1, P1.2 | Full | Privacy policies and notice content (when Privacy is in scope) |
| PT-2 (Authority to Process PII) | P1.1, P1.2 | Full | Legal basis for processing personal data |
| PT-3 (PII Processing Purposes) | P2.1 | Full | Purpose specification for data collection |
| PT-4 (Consent) | P3.1, P3.2 | Full | Consent mechanisms and choice |

### RA -- Risk Assessment

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| RA-3 (Risk Assessment) | CC3.1, CC3.2, CC3.3 | Full | Periodic risk assessments identifying threats and vulnerabilities |
| RA-5 (Vulnerability Scanning) | CC7.1, CC3.2 | Full | Vulnerability scanning and remediation tracking |
| RA-7 (Risk Response) | CC3.4, CC9.1 | Full | Risk treatment decisions (accept, mitigate, transfer, avoid) |
| RA-2 (Security Categorization) | CC3.1 | Partial | FIPS 199 categorization is NIST-specific; SOC 2 expects risk-based classification |

### SA -- System and Services Acquisition

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| SA-4 (Acquisition Process) | CC9.2 | Full | Security requirements in vendor contracts |
| SA-9 (External System Services) | CC9.2, CC6.6 | Full | Third-party risk management, vendor due diligence |
| SA-11 (Developer Testing) | CC8.1 | Partial | Secure SDLC practices expected but less prescriptive |
| SA-1, SA-2, SA-22 | CC9.2, CC1.3, CC7.1 | Partial | Acquisition policy, resource allocation, EOL management |

### SC -- System and Communications Protection

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| SC-7 (Boundary Protection) | CC6.1, CC6.6 | Full | Firewalls, network segmentation, DMZ architecture |
| SC-8 (Transmission Confidentiality) | CC6.1, CC6.7 | Full | TLS/encryption in transit |
| SC-12, SC-13 (Crypto Key Mgmt and Protection) | CC6.1, CC6.7 | Full | Key lifecycle management, validated cryptographic mechanisms |
| SC-23 (Session Authenticity) | CC6.1 | Full | Session management, anti-hijacking controls |
| SC-28 (Protection at Rest) | CC6.1, C1.1 | Full | Encryption at rest |
| SC-17 (PKI Certificates) | CC6.1 | Partial | Certificate management |

### SI -- System and Information Integrity

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| SI-2 (Flaw Remediation) | CC7.1, CC8.1 | Full | Patch management and vulnerability remediation |
| SI-3 (Malicious Code Protection) | CC7.1 | Full | Anti-malware, endpoint protection |
| SI-4 (System Monitoring) | CC7.1, CC7.2 | Full | IDS/IPS, SIEM, security monitoring |
| SI-5 (Security Alerts and Advisories) | CC7.2 | Full | Threat intelligence and advisory consumption |
| SI-7 (Integrity Verification) | CC7.1, CC8.1 | Partial | Software/firmware integrity verification mechanisms |
| SI-10 (Input Validation) | PI1.2, CC7.1 | Partial | Relevant when Processing Integrity is in scope |
| SI-12 (Information Retention) | CC6.5, C1.2 | Partial | Data retention and disposal |

### SR -- Supply Chain Risk Management

| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |
|-------------------|----------------|----------|-------|
| SR-1, SR-2, SR-3 (SCRM Policy, Plan, Controls) | CC9.2 | Partial | SOC 2 expects vendor oversight but not a formal SCRM plan or supply chain controls |
| SR-6 (Supplier Assessments and Reviews) | CC9.2 | Full | Periodic vendor risk reassessments |

## Coverage Gaps: NIST Controls with Limited SOC 2 Equivalents

The following NIST families and controls have minimal or no direct SOC 2 counterpart.

| NIST Family/Control | Gap Description |
|---------------------|-----------------|
| PE (Physical/Environmental) | CC6.4 covers physical access, but environmental controls (PE-9 through PE-18) are only tangentially addressed through A1.1. NIST is far more prescriptive on emergency power, fire, water, and HVAC. |
| MA (Maintenance) | No dedicated SOC 2 maintenance criteria. At best partially covered under CC7.1 and CC6.1. |
| MP (Media Protection) | CC6.5 partially addresses disposal and transport, but media marking (MP-3), use restrictions (MP-7), and detailed sanitization requirements have no SOC 2 equivalent. |
| PL-10, RA-2 | Baseline selection and FIPS 199 categorization are NIST/federal concepts with no SOC 2 equivalent. |
| CA-3 (Information Exchange) | Formal ISAs/MOUs for interconnections are NIST-specific; SOC 2 addresses connectivity generally under CC6.6 and CC9.2. |
| CM-10, AC-22 | Software license compliance and public content authorization are not within SOC 2 scope. |

## Reverse Mapping: SOC 2 Criteria to NIST Families

SOC 2 criteria are broadly stated and typically span multiple NIST families.

| SOC 2 Criteria | NIST Families | Notes |
|----------------|---------------|-------|
| CC1.1-CC1.5 (Control Environment) | PL, PM, PS, AT | Governance, org structure, personnel, training |
| CC2.1-CC2.3 (Communication) | PL, AT, IR-6, PM | Internal/external communication of security obligations |
| CC3.1-CC3.4 (Risk Assessment) | RA, PM | Risk identification, analysis, change-driven reassessment |
| CC4.1-CC4.2 (Monitoring) | CA, AU-6 | Ongoing evaluations and deficiency remediation |
| CC5.1-CC5.3 (Control Activities) | AC-5, PL, CM | Segregation of duties, control selection |
| CC6.1 (Logical Access - Security Software) | AC, IA, SC | Authentication, authorization, encryption, access enforcement |
| CC6.2 (User Registration) | AC-2, IA-4, PS-4, PS-5 | Provisioning, deprovisioning, access reviews |
| CC6.3 (Least Privilege) | AC-3, AC-6, IA-5 | Entitlement management, privilege restrictions |
| CC6.4 (Physical Access) | PE-2, PE-3, PE-6, PE-8 | Facility access, monitoring, visitor management |
| CC6.5 (Data Disposal) | MP-6, SI-12 | Secure data destruction and media sanitization |
| CC6.6 (External System Access) | AC-17, AC-20, CA-9, SC-7 | Boundary protection, external connections, remote access |
| CC6.7 (Transmission Protection) | SC-8, SC-13, AC-4 | Encryption in transit, TLS, data flow enforcement |
| CC6.8 (Malicious Software) | SI-3, SC-7, AC-19 | Anti-malware, endpoint protection |
| CC7.1 (Monitoring) | SI-4, AU-2, AU-12, CM-8 | Event logging, system monitoring, asset inventory |
| CC7.2 (Anomaly Detection) | SI-4, AU-6, SI-5 | SIEM, alert analysis, threat intelligence |
| CC7.3 (IR Process) | IR-1, IR-3, IR-4, IR-8 | IR plan, testing, handling procedures |
| CC7.4 (IR Containment) | IR-4, IR-5, IR-6 | Containment, eradication, root cause analysis |
| CC7.5 (IR Recovery) | IR-6, CP-2, CP-10 | External notification, recovery procedures |
| CC8.1 (Change Management) | CM-1 through CM-5 | Change control, testing, approval, baseline management |
| CC9.1 (Risk Mitigation) | RA-7, PM-9, CP-2 | Risk treatment and business continuity |
| CC9.2 (Vendor Risk) | SA-4, SA-9, SR, PS-7 | Third-party risk management, contractual requirements |
| A1.1-A1.3 (Availability) | CP, PE-9, PE-11, PE-13, PE-14 | BCP/DR, environmental controls, recovery testing |
| PI1.1-PI1.5 (Processing Integrity) | SI-10, SI-7, AU | Input validation, processing accuracy, output reconciliation |
| C1.1-C1.2 (Confidentiality) | SC-8, SC-28, MP, AC-4 | Encryption, data handling, disposal |
| P1.1-P8.1 (Privacy) | PT | Consent, notice, collection, use, retention, disclosure |

## Key Differences Between Frameworks

| Dimension | NIST 800-53 | SOC 2 |
|-----------|------------|-------|
| Approach | Prescriptive control catalog (~1,000+ controls) | Principle-based criteria (~60 criteria) |
| Assessment | Determine/examine/interview/test per 800-53A | Design suitability and operating effectiveness |
| Baselines | Low / Moderate / High | No baselines; scope set by Trust Services Categories |
| Applicability | Federal agencies (FISMA), FedRAMP CSPs | Voluntary; driven by customer/market demand |
| Output | SSP, SAR, POA&M | SOC 2 Type I or Type II report (restricted use) |
| Assessor | 3PAO (FedRAMP) or internal | Licensed CPA firm |
| Parameters | Specific values required (e.g., "lock after 3 failed attempts") | Organization defines; auditor evaluates reasonableness |
| Cadence | Continuous monitoring + annual reassessment | Type II covers 6-12 month observation period |

## Practical Guidance for Dual-Framework Compliance

1. **Implement to NIST, report to SOC 2** -- NIST controls are more prescriptive. Satisfying NIST generally satisfies corresponding SOC 2 criteria. Map NIST implementations to SOC 2 criteria for auditor evidence.
2. **Unified control matrix** -- Maintain a single matrix mapping each control to both NIST IDs and SOC 2 criteria to avoid duplicate documentation.
3. **Evidence reuse** -- Structure evidence repositories by control domain rather than by framework; the same artifacts serve both.
4. **Gap-fill for SOC 2 extras** -- Processing Integrity (PI) and Privacy (P) may require controls not in NIST 800-53 security families.
5. **Gap-fill for NIST extras** -- PE environmental controls, MA maintenance, and MP media protection are more thorough in NIST than SOC 2 covers.

## References

- **NIST SP 800-53 Rev 5** (September 2020, updated December 2020)
- **NIST SP 800-53B** (October 2020)
- **AICPA Trust Services Criteria** (2017, with 2022 revisions)
- **AICPA TSC-to-800-53 Mapping** (Trust Services Criteria Mapping, Appendix B)
