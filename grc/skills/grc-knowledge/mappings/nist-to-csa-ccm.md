# NIST 800-53 Rev 5 to CSA CCM v4 Mapping

## Overview

**NIST SP 800-53 Rev 5** is a general-purpose security and privacy controls catalog (20 families, 1,000+ controls) applicable to any information system regardless of deployment model. It is the foundational control set for FedRAMP, FISMA, and CMMC.

**CSA Cloud Controls Matrix (CCM) v4** is a cloud-specific controls framework (17 domains, 197 controls) purpose-built for cloud computing. It underpins the CSA STAR program: self-assessment (Level 1), third-party audit (Level 2), and continuous monitoring (Level 3).

**Key relationship characteristics**:
- NIST is technology-agnostic; CCM is cloud-native (multi-tenancy, shared responsibility, virtualization, containerization)
- Many NIST controls map to multiple CCM domains due to CCM's domain-oriented structure
- CCM includes domains (Interoperability & Portability, DevSecOps) with no single NIST family equivalent
- CCM v4 provides a reverse mapping to NIST Rev 4; this reference updates that mapping to Rev 5

**When to use this mapping**: CSPs pursuing FedRAMP + STAR certification, SOC 2+ with CCM overlay, translating federal controls to cloud-native implementations, or dual-framework audit assessments.

## Comprehensive Mapping by NIST Control Family

### AC — Access Control

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| AC-1 (Policy & Procedures) | IAM-01 | IAM policy aligned to business objectives |
| AC-2 (Account Management) | IAM-04, IAM-05, IAM-06 | Registration (IAM-04), provisioning (IAM-05), credential lifecycle (IAM-06) |
| AC-3 (Access Enforcement) | IAM-07, IAM-08 | Least privilege (IAM-07); segregation of duties (IAM-08) |
| AC-4 (Information Flow) | IVS-09, DSP-04 | Network architecture (IVS); data flow restrictions (DSP) |
| AC-5, AC-6 (SoD & Least Priv) | IAM-07, IAM-08 | Direct mappings |
| AC-7 (Unsuccessful Logon) | IAM-10 | Login attempt thresholds and lockout |
| AC-11, AC-12 (Session Controls) | IAM-11 | Session timeout and reauthentication |
| AC-17 (Remote Access) | IAM-14, IVS-06 | Strong auth for remote access; network security |
| AC-18 (Wireless Access) | IVS-07 | Wireless network security |
| AC-19 (Mobile Devices) | UEM-01 through UEM-14 | Dedicated Unified Endpoint Management domain |
| AC-20 (External Systems) | IAM-15, STA-06 | External system connections and third-party access |
| AC-21, AC-22 (Sharing & Content) | DSP-04, DSP-08, DSP-10 | Data handling, transfer, and public disclosure controls |

### AT — Awareness and Training

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| AT-1, AT-4 (Policy & Records) | HRS-09 | Security awareness training policy and documentation |
| AT-2 (Literacy Training) | HRS-09, HRS-10 | General awareness (HRS-09); cloud-specific training (HRS-10) |
| AT-3 (Role-Based Training) | HRS-11 | Specialized training for security-responsible personnel |

### AU — Audit and Accountability

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| AU-1 (Policy) | LOG-01 | Audit logging policy |
| AU-2 (Event Logging) | LOG-02, LOG-03 | Auditable events (LOG-02); security monitoring/alerting (LOG-03) |
| AU-3 (Audit Content) | LOG-04 | Log field content (timestamp, source, event type) |
| AU-4, AU-11 (Storage & Retention) | LOG-08, LOG-12 | Log storage capacity and retention period requirements |
| AU-5 (Response to Failures) | LOG-05 | Audit processing failure handling |
| AU-6, AU-7 (Review & Reduction) | LOG-06, LOG-07, LOG-09 | Log review, aggregation, correlation, and analysis |
| AU-8 (Time Stamps) | LOG-10 | Synchronized time sources |
| AU-9 (Protection of Audit Info) | LOG-11 | Protection from unauthorized modification or deletion |
| AU-12 (Audit Generation) | LOG-02, LOG-13 | Enabling audit on all relevant components |

### CA — Assessment, Authorization, and Monitoring

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| CA-1 (Policy) | A&A-01, GRC-01 | Audit/assurance policy and governance program |
| CA-2 (Assessments) | A&A-02, A&A-03 | Independent assessments and risk-based planning |
| CA-3, CA-9 (Connections) | IVS-06, IAM-15 | System interconnection and network security |
| CA-5 (POA&M) | A&A-04 | Remediation tracking and corrective action plans |
| CA-6 (Authorization) | A&A-05 | Risk acceptance and authorization decisions |
| CA-7 (Continuous Monitoring) | A&A-06, GRC-03 | Continuous assurance and ongoing risk monitoring |
| CA-8 (Penetration Testing) | TVM-06 | Penetration testing requirement |

### CM — Configuration Management

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| CM-1, CM-9 (Policy & Plan) | CCC-01 | Change management policy and CM program |
| CM-2, CM-6 (Baselines & Settings) | CCC-04 | Configuration baselines and hardening standards |
| CM-3, CM-4 (Change Control) | CCC-02, CCC-03 | Change request process and quality/impact testing |
| CM-5 (Access Restrictions) | CCC-05 | Change authority restricted to authorized personnel |
| CM-7 (Least Functionality) | CCC-06 | Disabling unnecessary services and functions |
| CM-8 (Inventory) | CCC-07, DCS-06 | IT asset inventory (CCC-07); physical asset inventory (DCS-06) |
| CM-10, CM-11 (Software Usage) | CCC-08, CCC-09 | Software installation restrictions and license management |

### CP — Contingency Planning

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| CP-1 (Policy) | BCR-01 | Business continuity management policy |
| CP-2 (Contingency Plan) | BCR-02, BCR-03 | BCP risk assessment and continuity strategy |
| CP-3, CP-4 (Training & Testing) | BCR-06, BCR-07 | Personnel training and regular plan testing |
| CP-6, CP-7 (Alternate Sites) | BCR-08, BCR-09, BCR-10 | Alternate storage, DR capability, geographic redundancy |
| CP-8 (Telecom) | BCR-05 | Communication redundancy |
| CP-9, CP-10 (Backup & Recovery) | BCR-04, BCR-11 | Backup/recovery procedures and RTO/RPO objectives |

### IA — Identification and Authentication

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| IA-1 (Policy) | IAM-01 | Shared policy with AC-1 |
| IA-2 (User ID & Auth) | IAM-02, IAM-03 | Credential lifecycle and identity verification |
| IA-2(1), IA-2(2) (MFA) | IAM-13 | Multi-factor authentication requirement |
| IA-3 (Device ID & Auth) | IAM-16 | Device identification and authentication |
| IA-4, IA-5 (ID & Auth Mgmt) | IAM-02, IAM-04, IAM-12 | Registration, credentials, token/certificate management |
| IA-6 (Auth Feedback) | IAM-10 | Login mechanism security |
| IA-8 (Non-Org Users) | IAM-09, IAM-15 | Third-party access roles and external identity management |

### IR — Incident Response

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| IR-1 (Policy) | SEF-01 | Security incident management policy |
| IR-2, IR-3 (Training & Testing) | SEF-02, SEF-03 | IR training/awareness and periodic plan testing |
| IR-4 (Incident Handling) | SEF-04 | Investigation, containment, and eradication |
| IR-5, IR-6 (Monitoring & Reporting) | SEF-05, SEF-06 | Incident tracking, metrics, and reporting obligations |
| IR-7 (IR Assistance) | SEF-07 | Coordination with external parties |
| IR-8 (IR Plan) | SEF-08 | IR plan documentation and review |

### MA — Maintenance / MP — Media Protection

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| MA-1, MA-2 (Maintenance) | IVS-01, DCS-02 | System-level (IVS) and physical facility (DCS) maintenance |
| MA-4, MA-5 (Remote & Personnel) | IAM-14, HRS-06, DCS-04 | Remote access, personnel vetting, escort requirements |
| MP-1 through MP-3 (Policy & Marking) | DSP-01, DSP-03 | Data security policy, classification, and labeling |
| MP-4 through MP-6 (Handling) | DSP-14, DSP-15, DSP-16 | Secure storage, transport, and sanitization |

### PE — Physical and Environmental Protection

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| PE-1 (Policy) | DCS-01 | Datacenter security policy |
| PE-2, PE-8 (Access Auth & Visitors) | DCS-02, DCS-03 | Access control mechanisms and visitor management |
| PE-3 (Physical Access Control) | DCS-04, DCS-05 | Controlled entry points and area separation/caging |
| PE-6 (Monitoring) | DCS-07 | Physical access monitoring and surveillance |
| PE-9 through PE-11 (Power) | DCS-08 | Power redundancy, UPS, and generators |
| PE-12 through PE-15 (Environmental) | DCS-09 | Fire, HVAC, water detection, environmental safety |
| PE-17 (Alternate Work Site) | IAM-14 | Remote work security via access management |

### PL — Planning / PM — Program Management

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| PL-1, PM-1 (Program & Plans) | GRC-01, GRC-02 | Governance and risk management program |
| PL-4 (Rules of Behavior) | HRS-04, HRS-05 | Acceptable use and responsibility agreements |
| PM-2 (Senior Security Officer) | GRC-04 | Designated security leadership |
| PM-9, PM-10, PM-11 (Strategy) | GRC-02, GRC-05, GRC-06, A&A-05 | Risk strategy, appetite, business alignment, authorization |
| PM-30 (Supply Chain Risk) | STA-01 | Supply chain management program |

### PS — Personnel Security

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| PS-1 through PS-3 (Policy & Screening) | HRS-01, HRS-02, HRS-03 | HR security policy, risk designation, background verification |
| PS-4, PS-5 (Termination & Transfer) | HRS-07, HRS-08, IAM-05, IAM-06 | Offboarding, role change, credential revocation, reprovisioning |
| PS-6, PS-7 (Agreements & External) | HRS-04, HRS-05, HRS-06 | Acceptable use, confidentiality, third-party personnel |

### PT — PII Processing and Transparency

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| PT-1 (Policy) | DSP-01 | Data security and privacy policy |
| PT-2 (Authority to Process) | DSP-02, DSP-05 | Data classification and legal basis for processing |
| PT-3 (Processing Purposes) | DSP-06, DSP-07 | Purpose limitation (DSP-06); data minimization (DSP-07) |
| PT-4, PT-5 (Consent & Notice) | DSP-08, DSP-09, DSP-18 | Consent mechanisms and transparency/notice requirements |
| PT-6 through PT-8 (Records) | DSP-10, DSP-17, DSP-19 | Data inventory, transfer agreements, and disclosure tracking |

### RA — Risk Assessment

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| RA-1 (Policy) | GRC-02 | Risk management program |
| RA-2 (Categorization) | DSP-02 | Data classification aligns with security categorization |
| RA-3, RA-7 (Risk Assessment & Response) | GRC-05, GRC-07, GRC-08 | Methodology, treatment, and exception processes |
| RA-5 (Vulnerability Monitoring) | TVM-01, TVM-02 | Vulnerability management policy and scanning |
| RA-9 (Criticality Analysis) | TVM-03 | Asset criticality for vulnerability prioritization |
| RA-10 (Threat Hunting) | TVM-10 | Proactive threat detection |

### SA — System and Services Acquisition

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| SA-1 (Policy) | STA-01, AIS-01 | Supply chain (STA) and application security (AIS) policy |
| SA-3, SA-15 (SDLC) | AIS-01, AIS-02 | SDLC policy and secure development standards |
| SA-4, SA-9 (Acquisition & External) | STA-03 through STA-06 | Vendor assessment, integrity, agreements, compliance |
| SA-8, SA-17 (Security Engineering) | AIS-03, AIS-04 | Security architecture and secure coding |
| SA-10, SA-11 (Dev Config & Testing) | AIS-05, AIS-06, AIS-07 | Dev environment config, automated testing, manual review |
| SA-22 (Unsupported Components), SR family | STA-07, STA-08, STA-09 | Governance, data security, end-of-life management |

### SC — System and Communications Protection

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| SC-1 (Policy) | CEK-01, IVS-01 | Encryption policy (CEK); infrastructure security policy (IVS) |
| SC-5, SC-7 (DoS & Boundary) | IVS-06, IVS-09 | Network segmentation, perimeter defense, DDoS protection |
| SC-8 (Transmission Confidentiality) | CEK-03, CEK-04 | Data-in-transit encryption and approved algorithms |
| SC-12 (Key Management) | CEK-05 through CEK-11 | Granular controls: generation, protection, access, rotation, revocation, archival, destruction |
| SC-13 (Cryptographic Protection) | CEK-02, CEK-04 | Encryption scope and approved algorithms/key lengths |
| SC-17 (PKI Certificates) | CEK-12, CEK-13 | Certificate issuance and validation |
| SC-23, SC-28 (Session & At-Rest) | IVS-05, CEK-14, CEK-15 | Session integrity; data-at-rest encryption |
| SC-39 (Process Isolation) | IVS-08 | Multi-tenant process and workload isolation |

### SI — System and Information Integrity

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| SI-1 (Policy) | TVM-01 | Vulnerability management policy |
| SI-2 (Flaw Remediation) | TVM-04, TVM-05 | Patch management and remediation timelines |
| SI-3 (Malicious Code) | TVM-07, UEM-06 | Malware defense (TVM-07); endpoint anti-malware (UEM-06) |
| SI-4 (Monitoring) | LOG-03, TVM-08 | Security monitoring and runtime threat detection |
| SI-5 (Security Alerts) | TVM-09 | Threat intelligence and advisory distribution |
| SI-7, SI-10 (Integrity & Validation) | AIS-04 | Software integrity and input validation via secure coding |
| SI-12 (Info Management) | DSP-01 | Data handling and retention |
| SI-16 (Memory Protection) | IVS-08 | Process isolation controls |

### SR — Supply Chain Risk Management

| NIST Controls | CSA CCM v4 Controls | Coverage Notes |
|---------------|---------------------|----------------|
| SR-1 (Policy & Procedures) | STA-01 | Supply chain management policy |
| SR-2 (SCRM Plan) | STA-02 | Supply chain risk management program |
| SR-3 (Supply Chain Controls) | STA-03, STA-04 | Vendor assessment (STA-03); integrity verification (STA-04) |
| SR-5, SR-6 (Acquisition & Assess) | STA-05, STA-06, STA-07 | Vendor agreements, compliance monitoring, and governance |
| SR-8 (Notification Agreements) | STA-10, STA-11 | Vendor incident notification and supply chain transparency |
| SR-10, SR-11 (Inspection & Auth) | STA-12, STA-13, STA-14 | Component inspection, counterfeit prevention, and provenance |

## CCM Domains with No Direct NIST Family Equivalent

These CCM domains aggregate controls from multiple NIST families or address cloud-specific concerns with no direct NIST counterpart.

| CCM Domain | Code | Controls | NIST (Partial) | Notes |
|------------|------|----------|----------------|-------|
| **Interoperability & Portability** | IPY | IPY-01 through IPY-04 | SA, SC | Data portability, vendor lock-in prevention, API interoperability |
| **Change Control & Config Mgmt** | CCC | CCC-01 through CCC-09 | SA, CM | Change management, configuration management, application security testing |
| **Universal Endpoint Management** | UEM | UEM-01 through UEM-14 | AC-19, SI-3 | Dedicated endpoint/mobile device management domain |
| **Datacenter Security** | DCS | DCS-01 through DCS-09 | PE | Direct PE mapping with cloud-specific datacenter additions |
| **Governance, Risk & Compliance** | GRC | GRC-01 through GRC-08 | PM, PL, CA | Consolidated governance, risk, and compliance domain |

## Cloud-Specific Controls in CCM Not Addressed by NIST 800-53

NIST 800-53 is cloud-deployment-agnostic. The following CCM controls address cloud-specific concerns requiring supplementation when using NIST as the primary framework.

| CCM Control Area | CCM Controls | NIST Gap |
|-----------------|--------------|----------|
| **Multi-tenancy Isolation** | IVS-08 | SC-39 covers process isolation but not multi-tenant cloud architectures |
| **Data Portability** | IPY-01, IPY-02 | No NIST equivalent for vendor lock-in prevention or data export |
| **API Security** | IPY-03, IPY-04 | SA-8 covers security engineering broadly but not cloud APIs |
| **Virtualization Security** | IVS-04 | SC-3 covers function isolation but not hypervisor/VM-specific threats |
| **Container Security** | CCC-04, AIS-04 | Not in NIST 800-53; partially covered by SP 800-190 |
| **Shared Responsibility** | STA-05, GRC-01 | NIST does not define shared responsibility models; FedRAMP CRM partially addresses |
| **Cloud Key Management** | CEK-16 through CEK-21 | SC-12 covers key mgmt broadly but not BYOK/HYOK or key sovereignty |
| **Data Residency** | DSP-11, DSP-12 | No NIST controls for geographic data sovereignty requirements |

## Shared Responsibility Mapping Considerations

Cloud environments introduce a shared responsibility model that affects how controls from both NIST and CCM are implemented. Control responsibility must be assigned to the correct party.

### Responsibility Layers by Cloud Service Model

| Layer | IaaS | PaaS | SaaS |
|-------|------|------|------|
| Physical Security (DCS, PE) | CSP | CSP | CSP |
| Network Infrastructure (IVS, SC) | CSP + Customer | CSP | CSP |
| Compute/Virtualization (IVS, SC) | CSP + Customer | CSP | CSP |
| Operating System (CM, SI) | Customer | CSP | CSP |
| Middleware/Runtime (SA, CM) | Customer | CSP + Customer | CSP |
| Application (AIS, SA) | Customer | Customer | CSP |
| Data (DSP, CEK, MP) | Customer | Customer | CSP + Customer |
| Identity & Access (IAM, AC, IA) | CSP + Customer | CSP + Customer | CSP + Customer |
| Governance & Compliance (GRC, CA, PM) | Customer | Customer | Customer |

### Key Mapping Considerations

- **Control inheritance**: In FedRAMP environments, CSP-provided controls documented as "inherited" in the customer SSP should be traced to corresponding CCM controls the CSP implements (typically DCS, IVS, and portions of IAM and CEK)
- **Compensating controls**: Where NIST requires a control unsupported by the cloud service model (e.g., PE for a SaaS customer), CCM often provides a cloud-appropriate alternative or assigns responsibility to the CSP
- **Continuous monitoring scope**: NIST CA-7 and CCM A&A-06 both require continuous monitoring, but CSP-side covers infrastructure/platform while customer-side covers application/data/access
- **Multi-framework audit efficiency**: SOC 2+ with CCM overlay enables single evidence collection for both FedRAMP and STAR, with approximately 70-80% control overlap at the Moderate baseline

## Quick Reference: NIST Family to CCM Domain Index

| NIST Family | Primary CCM Domain(s) | Secondary CCM Domain(s) |
|-------------|----------------------|------------------------|
| AC | IAM | IVS, DSP, UEM |
| AT | HRS | -- |
| AU | LOG | -- |
| CA | A&A | GRC, IVS |
| CM | CCC | DCS |
| CP | BCR | -- |
| IA | IAM | CEK |
| IR | SEF | -- |
| MA | IVS | DCS, HRS |
| MP | DSP | -- |
| PE | DCS | -- |
| PL | GRC | HRS |
| PM | GRC | A&A |
| PS | HRS | IAM |
| PT | DSP | -- |
| RA | GRC, TVM | DSP |
| SA | STA, AIS | -- |
| SC | CEK, IVS | -- |
| SI | TVM | UEM, LOG, AIS |
| SR | STA | -- |
