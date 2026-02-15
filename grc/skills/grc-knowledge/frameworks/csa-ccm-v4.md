# CSA CCM v4 — Cloud Controls Matrix Reference

## Overview

The **Cloud Controls Matrix (CCM)** is a cybersecurity controls framework published by the **Cloud Security Alliance (CSA)**. CCM v4.0, released in January 2021, provides **197 control objectives** across **17 domains** specifically designed for cloud computing environments. It serves as a de-facto standard for cloud security assurance and is the basis for the **CSA STAR** (Security, Trust, Assurance, and Risk) program.

CCM is unique in that it embeds a **shared responsibility model** directly into its control structure, designating accountability across Cloud Service Providers (CSPs), Cloud Service Customers (CSCs), and third parties.

**Key characteristics**:
- Cloud-native framework — controls are purpose-built for IaaS, PaaS, and SaaS environments
- Free to download and use (Creative Commons license)
- Provides pre-built mappings to ISO 27001, NIST 800-53, AICPA TSC, GDPR, PCI DSS, and others
- Paired with the **CAIQ** (Consensus Assessments Initiative Questionnaire) for standardized self-assessment
- Foundation of the **CSA STAR** certification and attestation program
- Defines control ownership via the **Shared Security Responsibility Model (SSRM)**

---

## 17 Control Domains (197 Controls)

### 1. A&A — Audit & Assurance (6 controls)

| Control ID | Title |
|------------|-------|
| A&A-01 | Audit and Assurance Policy and Procedures |
| A&A-02 | Independent Assessments |
| A&A-03 | Risk-Based Planning Assessment |
| A&A-04 | Requirements Compliance |
| A&A-05 | Audit Management Process |
| A&A-06 | Remediation |

### 2. AIS — Application & Interface Security (7 controls)

| Control ID | Title |
|------------|-------|
| AIS-01 | Application and Interface Security Policy and Procedures |
| AIS-02 | Application Security Baseline Requirements |
| AIS-03 | Application Security Metrics |
| AIS-04 | Secure Application Design and Development |
| AIS-05 | Automated Application Security Testing |
| AIS-06 | Automated Secure Application Deployment |
| AIS-07 | Application Vulnerability Remediation |

### 3. BCR — Business Continuity Management & Operational Resilience (11 controls)

| Control ID | Title |
|------------|-------|
| BCR-01 | Business Continuity Management Policy and Procedures |
| BCR-02 | Risk Assessment and Impact Analysis |
| BCR-03 | Business Continuity Strategy |
| BCR-04 | Business Continuity Planning |
| BCR-05 | Documentation |
| BCR-06 | Business Continuity Exercises |
| BCR-07 | Communication |
| BCR-08 | Backup |
| BCR-09 | Disaster Response Plan |
| BCR-10 | Response Plan Exercise |
| BCR-11 | Equipment Redundancy |

### 4. CCC — Change Control & Configuration Management (9 controls)

| Control ID | Title |
|------------|-------|
| CCC-01 | Change Management Policy and Procedures |
| CCC-02 | Quality Testing |
| CCC-03 | Change Management Technology |
| CCC-04 | Unauthorized Change Protection |
| CCC-05 | Change Agreements |
| CCC-06 | Change Management Baseline |
| CCC-07 | Detection of Baseline Deviation |
| CCC-08 | Exception Management |
| CCC-09 | Change Restoration |

### 5. CEK — Cryptography, Encryption & Key Management (21 controls)

| Control ID | Title |
|------------|-------|
| CEK-01 | Encryption and Key Management Policy and Procedures |
| CEK-02 | CEK Roles and Responsibilities |
| CEK-03 | Data Encryption |
| CEK-04 | Encryption Algorithm |
| CEK-05 | Encryption Change Management |
| CEK-06 | Encryption Change Cost Benefit Analysis |
| CEK-07 | Encryption Risk Management |
| CEK-08 | CSC Key Management Capability |
| CEK-09 | Encryption and Key Management Audit |
| CEK-10 | Key Generation |
| CEK-11 | Key Purpose |
| CEK-12 | Key Rotation |
| CEK-13 | Key Revocation |
| CEK-14 | Key Destruction |
| CEK-15 | Key Activation |
| CEK-16 | Key Suspension |
| CEK-17 | Key Deactivation |
| CEK-18 | Key Archival |
| CEK-19 | Key Compromise |
| CEK-20 | Key Recovery |
| CEK-21 | Key Inventory Management |

### 6. DCS — Datacenter Security (15 controls)

| Control ID | Title |
|------------|-------|
| DCS-01 | Off-Site Equipment Disposal Policy and Procedures |
| DCS-02 | Off-Site Transfer Authorization Policy and Procedures |
| DCS-03 | Secure Area Policy and Procedures |
| DCS-04 | Secure Media Transportation Policy and Procedures |
| DCS-05 | Assets Classification |
| DCS-06 | Assets Cataloguing and Tracking |
| DCS-07 | Controlled Access Points |
| DCS-08 | Equipment Identification |
| DCS-09 | Secure Area Authorization |
| DCS-10 | Surveillance System |
| DCS-11 | Unauthorized Access Response Training |
| DCS-12 | Cabling Security |
| DCS-13 | Environmental Systems |
| DCS-14 | Secure Utilities |
| DCS-15 | Equipment Location |

### 7. DSP — Data Security & Privacy Lifecycle Management (19 controls)

| Control ID | Title |
|------------|-------|
| DSP-01 | Security and Privacy Policy and Procedures |
| DSP-02 | Secure Disposal |
| DSP-03 | Data Inventory |
| DSP-04 | Data Classification |
| DSP-05 | Data Flow Documentation |
| DSP-06 | Data Ownership and Stewardship |
| DSP-07 | Data Protection by Design and Default |
| DSP-08 | Data Privacy by Design and Default |
| DSP-09 | Data Protection Impact Assessment |
| DSP-10 | Sensitive Data Transfer |
| DSP-11 | Personal Data Access, Reversal, Rectification and Deletion |
| DSP-12 | Limitation of Purpose in Personal Data Processing |
| DSP-13 | Personal Data Sub-processing |
| DSP-14 | Disclosure of Data Sub-processors |
| DSP-15 | Limitation of Production Data Use |
| DSP-16 | Data Retention and Deletion |
| DSP-17 | Sensitive Data Protection |
| DSP-18 | Disclosure Notification |
| DSP-19 | Data Location |

### 8. GRC — Governance, Risk & Compliance (8 controls)

| Control ID | Title |
|------------|-------|
| GRC-01 | Governance Program Policy and Procedures |
| GRC-02 | Risk Management Program |
| GRC-03 | Organizational Policy Reviews |
| GRC-04 | Policy Exception Process |
| GRC-05 | Information Security Program |
| GRC-06 | Governance Responsibility Model |
| GRC-07 | Information System Regulatory Mapping |
| GRC-08 | Special Interest Groups |

### 9. HRS — Human Resources (13 controls)

| Control ID | Title |
|------------|-------|
| HRS-01 | Background Screening Policy and Procedures |
| HRS-02 | Acceptable Use of Technology Policy and Procedures |
| HRS-03 | Clean Desk Policy and Procedures |
| HRS-04 | Remote and Home Working Policy and Procedures |
| HRS-05 | Asset Returns |
| HRS-06 | Employment Termination |
| HRS-07 | Employment Agreement Process |
| HRS-08 | Employment Agreement Content |
| HRS-09 | Personnel Roles and Responsibilities |
| HRS-10 | Non-Disclosure Agreements |
| HRS-11 | Security Awareness Training |
| HRS-12 | Personal and Sensitive Data Awareness and Training |
| HRS-13 | Compliance User Responsibility |

### 10. IAM — Identity & Access Management (16 controls)

| Control ID | Title |
|------------|-------|
| IAM-01 | Identity and Access Management Policy and Procedures |
| IAM-02 | Strong Password Policy and Procedures |
| IAM-03 | Identity Inventory |
| IAM-04 | Separation of Duties |
| IAM-05 | Least Privilege |
| IAM-06 | User Access Provisioning |
| IAM-07 | User Access Changes and Revocation |
| IAM-08 | User Access Review |
| IAM-09 | Segregation of Privileged Access Roles |
| IAM-10 | Management of Privileged Access Roles |
| IAM-11 | CSCs Approval for Agreed Privileged Access Roles |
| IAM-12 | Safeguard Logs Integrity |
| IAM-13 | Uniquely Identifiable Users |
| IAM-14 | Strong Authentication |
| IAM-15 | Passwords Management |
| IAM-16 | Authorization Mechanisms |

### 11. IPY — Interoperability & Portability (4 controls)

| Control ID | Title |
|------------|-------|
| IPY-01 | Interoperability and Portability Policy and Procedures |
| IPY-02 | Application Portability |
| IPY-03 | Secure Interoperability and Portability Management |
| IPY-04 | Data Portability |

### 12. IVS — Infrastructure & Virtualization Security (9 controls)

| Control ID | Title |
|------------|-------|
| IVS-01 | Infrastructure and Virtualization Security Policy and Procedures |
| IVS-02 | Capacity and Resource Planning |
| IVS-03 | Network Security |
| IVS-04 | OS Hardening and Base Controls |
| IVS-05 | Production and Non-Production Environments |
| IVS-06 | Segmentation and Segregation |
| IVS-07 | Migration to Cloud Environments |
| IVS-08 | Network Architecture Documentation |
| IVS-09 | Network Defense |

### 13. LOG — Logging & Monitoring (13 controls)

| Control ID | Title |
|------------|-------|
| LOG-01 | Logging and Monitoring Policy and Procedures |
| LOG-02 | Audit Logs Protection |
| LOG-03 | Security Monitoring and Alerting |
| LOG-04 | Audit Logs Access and Accountability |
| LOG-05 | Audit Logs Monitoring and Response |
| LOG-06 | Clock Synchronization |
| LOG-07 | Logging Scope |
| LOG-08 | Log Records |
| LOG-09 | Log Protection |
| LOG-10 | Encryption Monitoring and Reporting |
| LOG-11 | Transaction/Activity Logging |
| LOG-12 | Access Control Logs |
| LOG-13 | Failures and Anomalies Reporting |

### 14. SEF — Security Incident Management, E-Discovery & Cloud Forensics (8 controls)

| Control ID | Title |
|------------|-------|
| SEF-01 | Security Incident Management Policy and Procedures |
| SEF-02 | Service Management Policy and Procedures |
| SEF-03 | Incident Response Plans |
| SEF-04 | Incident Response Testing |
| SEF-05 | Incident Response Metrics |
| SEF-06 | Event Triage Processes |
| SEF-07 | Security Breach Notification |
| SEF-08 | Points of Contact Maintenance |

### 15. STA — Supply Chain Management, Transparency & Accountability (14 controls)

| Control ID | Title |
|------------|-------|
| STA-01 | SSRM Policy and Procedures |
| STA-02 | SSRM Supply Chain |
| STA-03 | SSRM Guidance |
| STA-04 | SSRM Control Ownership |
| STA-05 | SSRM Documentation Review |
| STA-06 | SSRM Control Implementation |
| STA-07 | Supply Chain Inventory |
| STA-08 | Supply Chain Risk Management |
| STA-09 | Primary Service and Contractual Agreement |
| STA-10 | Supply Chain Agreement Review |
| STA-11 | Internal Compliance Testing |
| STA-12 | Supply Chain Service Agreement Compliance |
| STA-13 | Supply Chain Governance Review |
| STA-14 | Supply Chain Data Security Assessment |

### 16. TVM — Threat & Vulnerability Management (10 controls)

| Control ID | Title |
|------------|-------|
| TVM-01 | Threat and Vulnerability Management Policy and Procedures |
| TVM-02 | Malware Protection Policy and Procedures |
| TVM-03 | Vulnerability Remediation Schedule |
| TVM-04 | Detection Updates |
| TVM-05 | External Library Vulnerabilities |
| TVM-06 | Penetration Testing |
| TVM-07 | Vulnerability Identification |
| TVM-08 | Vulnerability Prioritization |
| TVM-09 | Vulnerability Management Reporting |
| TVM-10 | Vulnerability Management Metrics |

### 17. UEM — Universal Endpoint Management (14 controls)

| Control ID | Title |
|------------|-------|
| UEM-01 | Endpoint Devices Policy and Procedures |
| UEM-02 | Application and Service Approval |
| UEM-03 | Compatibility |
| UEM-04 | Endpoint Inventory |
| UEM-05 | Endpoint Management |
| UEM-06 | Automatic Lock Screen |
| UEM-07 | Operating Systems |
| UEM-08 | Storage Encryption |
| UEM-09 | Anti-Malware Detection and Prevention |
| UEM-10 | Software Firewall |
| UEM-11 | Data Loss Prevention |
| UEM-12 | Remote Locate |
| UEM-13 | Remote Wipe |
| UEM-14 | Third-Party Endpoint Security Posture |

---

## CSA STAR Program

The **STAR** (Security, Trust, Assurance, and Risk) program uses CCM as its control baseline and provides three levels of assurance.

| Level | Name | Mechanism | Description |
|-------|------|-----------|-------------|
| **Level 1** | Self-Assessment | CAIQ or CCM self-assessment | Organization completes the CAIQ questionnaire or CCM-based self-assessment and publishes results on the CSA STAR Registry. No third-party validation. |
| **Level 2** | Third-Party Audit | SOC 2 + CCM **or** ISO 27001 + CCM | Independent audit performed by an accredited assessor. Two paths: **STAR Attestation** (SOC 2 + CCM, performed by a CPA firm) or **STAR Certification** (ISO 27001 + CCM, performed by a CSA-accredited certification body). |
| **Level 3** | Continuous Monitoring | Continuous security monitoring | Continuous, automated assessment of cloud security posture. Builds on Level 2 with real-time or near-real-time assurance. Currently under development by CSA. |

**STAR Registry**: Public registry at `cloudsecurityalliance.org/star/registry` where organizations publish their self-assessments and certifications. CSCs use the registry to evaluate CSP security posture during vendor due diligence.

---

## CAIQ — Consensus Assessments Initiative Questionnaire

The **CAIQ v4** is a standardized questionnaire companion to CCM v4 that translates each CCM control into yes/no questions for structured self-assessment.

**Key facts**:
- Contains **261 questions** mapped to all 197 CCM v4 controls
- Questions are formatted as "Does your organization...?" for CSP self-response
- Each question maps directly to a CCM control ID (e.g., A&A-01.1, A&A-01.2)
- Responses are typically: Yes, No, Not Applicable, or CSC-Owned
- Published in spreadsheet format (XLSX) for ease of completion
- CSPs complete the CAIQ and publish it on the STAR Registry (Level 1)
- CSCs use completed CAIQs to compare CSP security postures during procurement

**CAIQ assessment workflow**:
1. Download current CAIQ template from CSA website
2. Complete responses for all applicable control questions
3. Provide supplementary notes and evidence references where needed
4. Submit to CSA for publication on the STAR Registry
5. Update annually or when material changes occur

---

## Shared Security Responsibility Model (SSRM)

CCM v4 formalizes the shared responsibility model through the STA domain. Each control specifies ownership across three parties.

| Party | Abbreviation | Responsibility |
|-------|-------------|----------------|
| Cloud Service Provider | CSP | Implements and operates controls for the cloud infrastructure and platform layers |
| Cloud Service Customer | CSC | Implements and operates controls for workloads, data, and configurations within the cloud service |
| Third Party | 3P | Provides assurance, audit, or specialized services (e.g., auditors, managed security providers) |

**Ownership model per service type**:

| Control Area | IaaS | PaaS | SaaS |
|-------------|------|------|------|
| Physical security | CSP | CSP | CSP |
| Network infrastructure | CSP | CSP | CSP |
| Hypervisor / virtualization | CSP | CSP | CSP |
| Operating system | CSC | CSP | CSP |
| Application | CSC | CSC | CSP |
| Data classification & protection | CSC | CSC | CSC |
| Identity & access (customer users) | CSC | CSC | CSC |
| Encryption key management | CSC/CSP | CSC/CSP | CSP |

The STA-04 control (SSRM Control Ownership) requires that ownership is explicitly documented for every CCM control, ensuring no gaps in accountability between CSP and CSC.

---

## CCM v3.0.1 to v4.0 Changes

| Attribute | CCM v3.0.1 | CCM v4.0 |
|-----------|-----------|----------|
| Control objectives | 133 | 197 (+64 new controls) |
| Domains | 16 | 17 (+1 new domain) |
| New domain added | -- | LOG (Logging & Monitoring) |
| SSRM integration | Not embedded | Formally embedded in STA domain |
| CAIQ alignment | CAIQ v3 (295 questions) | CAIQ v4 (261 questions, restructured) |

**Major changes by domain**:
- **CEK** expanded from 4 to 21 controls, adding granular key lifecycle management (generation, rotation, revocation, destruction, archival, recovery)
- **DSP** restructured with expanded privacy controls aligned to GDPR and other privacy regulations (privacy by design, DPIA, data subject rights, sub-processor disclosure)
- **LOG** added as an entirely new domain with 13 controls addressing logging scope, log protection, clock synchronization, and anomaly reporting
- **STA** expanded to incorporate SSRM formally, with dedicated controls for control ownership documentation and supply chain risk assessment
- **UEM** expanded to cover modern endpoint scenarios including remote wipe, remote locate, and third-party endpoint posture
- **A&A** reorganized with clearer separation between audit policy, independent assessment, and remediation tracking
- Several v3.0.1 domains were renamed for clarity (e.g., EKM became CEK, MOS was absorbed into UEM)

---

## Relationship to Other Frameworks

CCM v4 provides official mappings to major regulatory and compliance frameworks, enabling organizations to demonstrate compliance across multiple standards simultaneously.

| Framework | Mapping Relationship |
|-----------|---------------------|
| **ISO/IEC 27001:2013** | CCM controls map to Annex A controls; basis for STAR Certification (Level 2) |
| **ISO/IEC 27017:2015** | Cloud-specific extension of 27001; CCM provides complementary cloud controls |
| **ISO/IEC 27018:2019** | PII protection in public cloud; DSP domain aligns closely |
| **NIST SP 800-53 Rev. 5** | CSA provides detailed control-level mappings; CCM is more cloud-specific while 800-53 is broader |
| **NIST Cybersecurity Framework** | CCM domains map to CSF functions (Identify, Protect, Detect, Respond, Recover) |
| **AICPA TSC (SOC 2)** | CCM is layered onto SOC 2 for STAR Attestation (SOC 2+); Common Criteria map to multiple CCM domains |
| **PCI DSS v4.0** | Mapped for organizations processing payment card data in cloud environments |
| **GDPR** | DSP domain controls address key GDPR articles (data protection by design, DPIA, data subject rights, cross-border transfers) |
| **CIS Controls v8** | CIS provides official mapping document; CIS focuses on technical hygiene while CCM addresses governance and cloud architecture |
| **ENISA IAF** | European cloud security framework; complementary to CCM for EU-based assessments |
| **FedRAMP** | CCM-to-NIST-800-53 mappings enable FedRAMP alignment; not a direct substitution |

---

## Implementation Guidance

**Scoping considerations for GRC analysts**:
1. Identify which CCM controls are CSP-owned vs. CSC-owned based on the service model (IaaS/PaaS/SaaS)
2. Map existing organizational controls to CCM control IDs to identify gaps
3. Use CAIQ responses from CSPs to validate provider control coverage
4. Align CCM implementation with existing compliance programs (e.g., SOC 2, ISO 27001) to reduce duplication
5. Leverage CSA's official cross-framework mappings to consolidate evidence collection across audits
6. Publish STAR self-assessment (Level 1) as a baseline, then progress to Level 2 certification or attestation
7. Review the STAR Registry for CSP assessments during vendor risk management and procurement
