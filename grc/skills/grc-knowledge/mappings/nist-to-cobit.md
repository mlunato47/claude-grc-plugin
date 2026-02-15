# NIST 800-53 Rev 5 to COBIT 2019 Mapping

## Overview

This document maps NIST 800-53 Rev 5 control families to COBIT 2019 governance and management objectives. These two frameworks serve fundamentally different purposes and operate at different levels of abstraction.

**NIST 800-53 Rev 5** is a security and privacy controls catalog. It provides prescriptive, technical, and procedural controls organized into 20 families. It is security-specific, designed for federal information systems, and focuses on protecting confidentiality, integrity, and availability.

**COBIT 2019** is ISACA's enterprise IT governance and management framework. It addresses the full scope of enterprise information and technology (I&T) governance, including value delivery, risk optimization, resource optimization, and stakeholder engagement. Security is one concern among many.

| Attribute | NIST 800-53 Rev 5 | COBIT 2019 |
|-----------|-------------------|------------|
| **Governing Body** | NIST (U.S. Dept. of Commerce) | ISACA |
| **Primary Purpose** | Security and privacy controls | Enterprise IT governance and management |
| **Scope** | Information system security posture | Full enterprise I&T lifecycle |
| **Abstraction Level** | Prescriptive controls with parameters | High-level governance/management objectives |
| **Structure** | 20 families, ~1,000+ controls | 5 domains, 40 objectives, capability levels 0-5 |
| **Audience** | ISSOs, ISSMs, security engineers, auditors | CIOs, IT directors, governance boards, IT auditors |
| **Mandatory For** | U.S. federal agencies (FISMA) | Voluntary (often adopted in regulated industries) |

## Key Differences in Scope and Purpose

1. **Abstraction level**: A single COBIT objective (e.g., DSS05 Managed Security Services) maps to multiple NIST control families (AC, IA, SC, AU). COBIT defines *what* should be governed; NIST specifies *how* to implement security controls.

2. **Governance vs. controls**: COBIT's EDM domain (Evaluate, Direct and Monitor) has no direct NIST equivalent at the control level. NIST PM (Program Management) is the closest family but remains operationally focused compared to COBIT's board-level governance objectives.

3. **Scope breadth**: COBIT covers IT service management, project management, vendor management, data management, innovation, and enterprise architecture. Most of these have no NIST 800-53 counterpart because NIST is scoped to security and privacy.

4. **Complementary use**: Organizations typically use COBIT as the governance wrapper and NIST 800-53 as the detailed control implementation within that governance structure. COBIT answers "are we doing the right things?" while NIST answers "are we doing them securely?"

## Comprehensive Mapping by NIST Family

### AC — Access Control

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| AC-1 (Policy and Procedures) | APO01 (Managed I&T Management Framework) | COBIT APO01 covers policy establishment broadly |
| AC-2 (Account Management) | DSS05 (Managed Security Services) | DSS05 addresses identity and access provisioning |
| AC-3 (Access Enforcement) | DSS05, DSS06 (Managed Business Process Controls) | DSS06 adds business-level authorization controls |
| AC-4 (Information Flow Enforcement) | DSS05 | Network and data flow controls under security services |
| AC-5 (Separation of Duties) | DSS06 | DSS06 explicitly addresses SoD in business processes |
| AC-6 (Least Privilege) | DSS05, DSS06 | Covered across security services and process controls |
| AC-7 (Unsuccessful Logon Attempts) | DSS05 | Detailed technical control; COBIT addresses at objective level |
| AC-17 (Remote Access) | DSS05 | Remote access management under security services |
| AC-20 (Use of External Systems) | APO10 (Managed Vendors), DSS05 | Vendor/third-party system access |

### AT — Awareness and Training

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| AT-1 (Policy and Procedures) | APO07 (Managed Human Resources) | HR policies include training governance |
| AT-2 (Literacy Training and Awareness) | APO07 | Workforce competency and awareness programs |
| AT-3 (Role-Based Training) | APO07 | Skills development and role-based competency |
| AT-4 (Training Records) | APO07 | HR record-keeping practices |

### AU — Audit and Accountability

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| AU-1 (Policy and Procedures) | APO01 | Policy framework establishment |
| AU-2 (Event Logging) | DSS05, MEA01 (Managed Performance and Conformance Monitoring) | DSS05 for security logging; MEA01 for monitoring |
| AU-3 (Content of Audit Records) | DSS05 | Technical detail within security services |
| AU-6 (Audit Record Review, Analysis, and Reporting) | MEA01, MEA02 (Managed System of Internal Control) | MEA01 for performance monitoring; MEA02 for control assurance |
| AU-9 (Protection of Audit Information) | DSS05 | Integrity of audit logs as security function |
| AU-12 (Audit Record Generation) | DSS05 | Technical logging implementation |

### CA — Assessment, Authorization, and Monitoring

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| CA-1 (Policy and Procedures) | APO01 | Governance framework policies |
| CA-2 (Control Assessments) | MEA02, MEA04 (Managed Assurance) | Internal control assessment and assurance activities |
| CA-5 (Plan of Action and Milestones) | MEA02 | Tracking control deficiencies and remediation |
| CA-6 (Authorization) | MEA03 (Managed Compliance with External Requirements) | Formal acceptance of risk; compliance authorization |
| CA-7 (Continuous Monitoring) | MEA01, MEA02 | Ongoing monitoring and control evaluation |
| CA-9 (Internal System Connections) | DSS05 | System interconnection security |

### CM — Configuration Management

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| CM-1 (Policy and Procedures) | APO01 | Policy framework |
| CM-2 (Baseline Configuration) | BAI10 (Managed Configuration) | Configuration baselines and management |
| CM-3 (Configuration Change Control) | BAI06 (Managed IT Changes), BAI10 | BAI06 for change process; BAI10 for configuration integrity |
| CM-4 (Impact Analyses) | BAI06 | Change impact assessment |
| CM-6 (Configuration Settings) | BAI10, DSS05 | Secure configuration under both objectives |
| CM-7 (Least Functionality) | DSS05, BAI10 | Hardening and minimized services |
| CM-8 (System Component Inventory) | BAI09 (Managed Assets), BAI10 | Asset and configuration item inventory |

### CP — Contingency Planning

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| CP-1 (Policy and Procedures) | APO01 | Policy framework |
| CP-2 (Contingency Plan) | DSS04 (Managed Continuity) | Direct mapping — business continuity planning |
| CP-3 (Contingency Training) | DSS04 | Continuity awareness and training |
| CP-4 (Contingency Plan Testing) | DSS04 | BCP/DR testing and exercises |
| CP-6 (Alternate Storage Site) | DSS04 | Recovery site and storage strategies |
| CP-7 (Alternate Processing Site) | DSS04 | Failover and recovery sites |
| CP-9 (System Backup) | DSS04 | Backup and restoration capabilities |
| CP-10 (System Recovery and Reconstitution) | DSS04 | Recovery procedures and reconstitution |

### IA — Identification and Authentication

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| IA-1 (Policy and Procedures) | APO01 | Policy framework |
| IA-2 (User Identification and Authentication) | DSS05 | Identity management and authentication services |
| IA-4 (Identifier Management) | DSS05 | User and system identifier lifecycle |
| IA-5 (Authenticator Management) | DSS05 | Credential and authenticator management |
| IA-8 (Identification and Authentication for Non-Org Users) | DSS05, APO10 | External user authentication; vendor access |

### IR — Incident Response

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| IR-1 (Policy and Procedures) | APO01 | Policy framework |
| IR-2 (Incident Response Training) | DSS02 (Managed Service Requests and Incidents) | Training for incident handlers |
| IR-4 (Incident Handling) | DSS02 | Incident detection, analysis, containment, recovery |
| IR-5 (Incident Monitoring) | DSS02, MEA01 | Incident tracking and trend analysis |
| IR-6 (Incident Reporting) | DSS02 | Internal and external incident reporting |
| IR-8 (Incident Response Plan) | DSS02 | IRP development and maintenance |

### MA — Maintenance

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| MA-1 (Policy and Procedures) | APO01 | Policy framework |
| MA-2 (Controlled Maintenance) | DSS01 (Managed Operations), BAI09 | Scheduled and controlled maintenance activities |
| MA-3 (Maintenance Tools) | DSS01, BAI09 | Tool management and asset maintenance |
| MA-4 (Nonlocal Maintenance) | DSS01, DSS05 | Remote maintenance with security controls |
| MA-5 (Maintenance Personnel) | DSS01, APO07 | Personnel authorization for maintenance |

### MP — Media Protection

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| MP-1 (Policy and Procedures) | APO01 | Policy framework |
| MP-2 (Media Access) | DSS05, APO14 (Managed Data) | Media access restrictions |
| MP-4 (Media Storage) | DSS05, APO14 | Secure storage of media |
| MP-6 (Media Sanitization) | DSS05, BAI09 | Sanitization and disposal; asset lifecycle |

### PE — Physical and Environmental Protection

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| PE-1 (Policy and Procedures) | APO01 | Policy framework |
| PE-2 (Physical Access Authorizations) | DSS05 | Physical access control under security services |
| PE-3 (Physical Access Control) | DSS05 | Entry controls, badges, barriers |
| PE-6 (Monitoring Physical Access) | DSS05, DSS01 | Surveillance and monitoring of facilities |
| PE-8 (Visitor Access Records) | DSS05 | Visitor management |
| PE-9 through PE-15 (Environmental Controls) | DSS01 | Power, lighting, fire, temperature, humidity — operations |
| PE-17 (Alternate Work Site) | DSS01, DSS05 | Alternate facility security |

### PL — Planning

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| PL-1 (Policy and Procedures) | APO01 (Managed I&T Management Framework) | Governance and management framework policies |
| PL-2 (System Security and Privacy Plans) | APO01, APO02 (Managed Strategy) | Security planning as part of I&T strategy |
| PL-4 (Rules of Behavior) | APO01 | Acceptable use and behavioral expectations |
| PL-7 (Concept of Operations) | APO02 | Strategic and operational concept documentation |
| PL-8 (Security and Privacy Architectures) | APO03 (Managed Enterprise Architecture) | Architecture-level security integration |

### PM — Program Management

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| PM-1 (Information Security Program Plan) | APO01, EDM01 (Ensured Governance Framework Setting) | Program-level planning and governance framework |
| PM-2 (Information Security Program Leadership Role) | EDM01, APO01 | CISO role; governance leadership |
| PM-3 (Information Security and Privacy Resources) | EDM04 (Ensured Resource Optimization) | Resource allocation and optimization |
| PM-4 (Plan of Action and Milestones Process) | MEA02 | Tracking and managing remediation |
| PM-5 (System Inventory) | BAI09 | Enterprise system inventory |
| PM-7 (Enterprise Architecture) | APO03 | Enterprise architecture alignment |
| PM-8 (Critical Infrastructure Plan) | EDM03 (Ensured Risk Optimization) | Risk management at the enterprise level |
| PM-9 (Risk Management Strategy) | EDM03, APO12 (Managed Risk) | Enterprise risk strategy and appetite |
| PM-10 (Authorization Process) | MEA03 | Compliance with authorization requirements |
| PM-11 (Mission and Business Process Definition) | EDM02 (Ensured Benefits Delivery) | Aligning I&T with mission and business value |
| PM-28 (Risk Framing) | EDM03, APO12 | Risk context and framing |
| PM-30 (Supply Chain Risk Management Strategy) | APO10, EDM03 | Supply chain governance |
| PM-31 (Continuous Monitoring Strategy) | MEA01, EDM05 (Ensured Stakeholder Engagement) | Monitoring strategy and stakeholder reporting |

### PS — Personnel Security

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| PS-1 (Policy and Procedures) | APO01 | Policy framework |
| PS-2 (Position Risk Designation) | APO07 (Managed Human Resources) | Role classification and risk designation |
| PS-3 (Personnel Screening) | APO07 | Background investigations and vetting |
| PS-4 (Personnel Termination) | APO07, DSS05 | Access revocation upon termination |
| PS-5 (Personnel Transfer) | APO07, DSS05 | Access modification upon role change |
| PS-6 (Access Agreements) | APO07 | NDAs, acceptable use agreements |

### PT — PII Processing and Transparency

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| PT-1 (Policy and Procedures) | APO01 | Policy framework |
| PT-2 (Authority to Process PII) | APO14 (Managed Data), MEA03 | Data governance and legal compliance |
| PT-3 (PII Processing Purposes) | APO14 | Purpose limitation and data governance |
| PT-4 (Consent) | APO14, DSS06 | Consent management; business process controls |

### RA — Risk Assessment

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| RA-1 (Policy and Procedures) | APO01 | Policy framework |
| RA-2 (Security Categorization) | APO12 (Managed Risk), APO13 (Managed Security) | Risk identification and classification |
| RA-3 (Risk Assessment) | APO12 | Risk assessment methodology and execution |
| RA-5 (Vulnerability Monitoring and Scanning) | APO12, DSS05 | Vulnerability management as part of risk and security |
| RA-7 (Risk Response) | APO12 | Risk treatment decisions |
| RA-9 (Criticality Analysis) | APO12 | Asset and mission criticality analysis |

### SA — System and Services Acquisition

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| SA-1 (Policy and Procedures) | APO01 | Policy framework |
| SA-2 (Allocation of Resources) | APO06 (Managed Budget and Costs) | Budget and resource allocation |
| SA-3 (System Development Life Cycle) | BAI02 (Managed Requirements Definition), BAI03 (Managed Solutions Identification and Build) | SDLC requirements and solution development |
| SA-4 (Acquisition Process) | APO10 (Managed Vendors), BAI03 | Procurement and vendor management |
| SA-8 (Security and Privacy Engineering Principles) | BAI03, APO13 | Security-by-design in solution development |
| SA-9 (External System Services) | APO10, APO09 (Managed Service Agreements) | Third-party services and SLAs |
| SA-10 (Developer Configuration Management) | BAI03, BAI10 | Developer environment configuration |
| SA-11 (Developer Testing and Evaluation) | BAI03, BAI07 (Managed IT Change Acceptance) | Testing and quality assurance |
| SA-22 (Unsupported System Components) | BAI09, BAI10 | End-of-life asset management |

### SC — System and Communications Protection

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| SC-1 (Policy and Procedures) | APO01 | Policy framework |
| SC-5 (Denial-of-Service Protection) | DSS05 | Network security services |
| SC-7 (Boundary Protection) | DSS05, APO13 | Network boundary and segmentation |
| SC-8 (Transmission Confidentiality and Integrity) | DSS05 | Encryption in transit |
| SC-12 (Cryptographic Key Management) | DSS05 | Key management practices |
| SC-13 (Cryptographic Protection) | DSS05, APO13 | Cryptographic standards and implementation |
| SC-28 (Protection of Information at Rest) | DSS05 | Encryption at rest |

### SI — System and Information Integrity

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| SI-1 (Policy and Procedures) | APO01 | Policy framework |
| SI-2 (Flaw Remediation) | DSS03 (Managed Problems), DSS05 | Patching and vulnerability remediation |
| SI-3 (Malicious Code Protection) | DSS05 | Anti-malware and endpoint protection |
| SI-4 (System Monitoring) | DSS05, MEA01 | Security monitoring and performance monitoring |
| SI-5 (Security Alerts, Advisories, and Directives) | DSS05, APO12 | Threat intelligence and advisory management |
| SI-7 (Software, Firmware, and Information Integrity) | DSS05, BAI10 | Integrity verification mechanisms |
| SI-10 (Information Input Validation) | DSS06 | Input validation in business process controls |

### SR — Supply Chain Risk Management

| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |
|-------------------|----------------------|----------------|
| SR-1 (Policy and Procedures) | APO01 | Policy framework |
| SR-2 (Supply Chain Risk Management Plan) | APO10 (Managed Vendors), EDM03 | Vendor risk management and governance |
| SR-3 (Supply Chain Controls and Processes) | APO10, APO13 | Supplier security requirements |
| SR-5 (Acquisition Strategies, Tools, and Methods) | APO10, BAI03 | Secure procurement practices |
| SR-6 (Supplier Assessments and Reviews) | APO10, MEA03 | Vendor assessment and compliance |
| SR-8 (Notification Agreements) | APO10, APO09 | Contractual notification requirements |

## EDM Governance Objectives — Mapping to NIST PM Family

COBIT's EDM domain represents board-level governance with no precise NIST equivalent. The NIST PM (Program Management) family is the closest counterpart but operates at an operational program level rather than enterprise governance.

| COBIT EDM Objective | Description | NIST PM Controls | Gap Analysis |
|---------------------|-------------|------------------|--------------|
| EDM01 — Ensured Governance Framework Setting and Maintenance | Establish and maintain the governance framework, principles, structures, and processes | PM-1 (Program Plan), PM-2 (Leadership Role) | NIST PM does not address board-level governance structure or IT governance principles |
| EDM02 — Ensured Benefits Delivery | Optimize the value contribution to the business from I&T investments | PM-11 (Mission/Business Process Definition) | NIST has no controls for IT value or benefits realization |
| EDM03 — Ensured Risk Optimization | Ensure enterprise I&T risk does not exceed risk appetite | PM-9 (Risk Strategy), PM-28 (Risk Framing) | NIST RA family provides detailed risk controls; PM provides strategy alignment |
| EDM04 — Ensured Resource Optimization | Ensure adequate and sufficient I&T resources to support enterprise objectives | PM-3 (Resources) | NIST addresses security resources only, not enterprise-wide I&T resource optimization |
| EDM05 — Ensured Stakeholder Engagement | Ensure stakeholders are supportive of I&T strategy and transparent reporting | PM-31 (Continuous Monitoring Strategy) | NIST does not address stakeholder engagement or I&T transparency reporting beyond security |

## COBIT Objectives with No or Limited NIST 800-53 Mapping

The following COBIT objectives address enterprise IT governance and management concerns that fall largely outside the scope of NIST 800-53's security and privacy controls. Objectives marked with "(partial)" have tangential overlap with NIST controls noted in the detailed mapping tables above but are primarily governance-focused.

| COBIT Objective | Title | Why Limited/No NIST Mapping |
|----------------|-------|---------------------|
| APO02 | Managed Strategy | IT strategic planning (partial overlap with PL-2, PL-7) |
| APO03 | Managed Enterprise Architecture | Enterprise architecture governance (partial overlap with PL-8) |
| APO04 | Managed Innovation | Technology innovation management has no security equivalent |
| APO05 | Managed Portfolio | IT portfolio and investment management |
| APO06 | Managed Budget and Costs | IT financial management (partial overlap with SA-2) |
| APO08 | Managed Relationships | Business-IT relationship management |
| APO09 | Managed Service Agreements | SLA governance (partial overlap with SA-9) |
| APO11 | Managed Quality | IT quality management programs |
| BAI01 | Managed Programs | Program management for IT initiatives |
| BAI04 | Managed Availability and Capacity | Availability and capacity planning (partial overlap with CP family) |
| BAI05 | Managed Organizational Change | Organizational change management for IT changes |
| BAI07 | Managed IT Change Acceptance and Transitioning | Go-live and acceptance testing governance (partial overlap with SA-11) |
| BAI08 | Managed Knowledge | Knowledge management systems and practices |
| BAI11 | Managed Projects | Individual IT project management |
| EDM02 | Ensured Benefits Delivery | IT value and benefits realization |
| EDM04 | Ensured Resource Optimization | Enterprise I&T resource optimization |
| EDM05 | Ensured Stakeholder Engagement | Stakeholder communication and transparency |

**Note**: "No or limited mapping" does not mean these objectives are irrelevant to security. Strong IT governance, project management, and quality programs indirectly support security posture. However, NIST 800-53 does not prescribe controls in these areas. Where partial overlap exists, NIST addresses only the security dimension of the broader COBIT objective.

## Using This Mapping

**From NIST to COBIT**: When an organization already implements NIST 800-53 and wants to demonstrate COBIT alignment, use this mapping to show which COBIT objectives are satisfied by existing NIST controls. Expect gaps in governance (EDM) and IT management areas (APO02-09, BAI01, BAI04-05, BAI07-08, BAI11) that require separate governance initiatives.

**From COBIT to NIST**: When a COBIT-governed organization needs to implement NIST 800-53 (e.g., for FedRAMP or FISMA), use this mapping to identify which COBIT objectives already address NIST requirements. Expect to add significant prescriptive detail — COBIT's high-level objectives must be decomposed into specific technical and procedural controls to satisfy NIST assessment procedures.

**Key insight**: COBIT and NIST 800-53 are complementary, not competing. COBIT provides the governance and management structure; NIST 800-53 provides the detailed security control catalog. Organizations subject to federal security requirements benefit from using both: COBIT for IT governance maturity and NIST for auditable security compliance.
