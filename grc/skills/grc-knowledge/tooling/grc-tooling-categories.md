# GRC Tooling Categories Reference

## Overview

This reference describes the major categories of tools used across GRC programs. Each category is defined by its purpose, key capabilities, and compliance relevance. No specific vendors or products are named.

## Category Summary

| Category | Primary Purpose | Key Compliance Relevance |
|----------|----------------|--------------------------|
| GRC Platform | Centralized control tracking and evidence lifecycle | All frameworks — system of record |
| Vulnerability Management | Identify and prioritize technical vulnerabilities | RA-5, Req 11.3, SI-2 |
| Configuration Compliance / SCAP | Validate configurations against benchmarks | CM-6, CM-2, Req 2.2 |
| SIEM / Log Management | Aggregate, correlate, and alert on security events | AU-2, AU-6, AU-12, Req 10 |
| Identity and Access Management | Control and govern identities and privileges | AC-2, AC-6, IA-2, Req 7, Req 8 |
| Endpoint Protection / EDR | Detect and respond to endpoint threats | SI-3, SI-4, Req 5 |
| Asset Management / CMDB | Maintain authoritative hardware/software inventory | CM-8, PM-5, Req 12.5.1 |
| Ticketing / Workflow | Track changes, incidents, and service requests | CM-3, IR-5, Req 6.5.1 |
| Policy Management | Author, review, approve, and distribute policies | PL-1, AT-2, Req 12 |
| Backup and Recovery | Schedule, verify, and restore backups | CP-9, CP-10 |
| Penetration Testing | Simulate adversarial attacks against systems | CA-8, Req 11.4 |
| OSCAL Tooling | Machine-readable security documentation | FedRAMP OSCAL requirements |

## GRC Platform / Compliance Management

**Purpose**: Centralized system of record for control implementation status, evidence management, and policy lifecycle governance across one or more compliance frameworks.

**Key capabilities**: Control libraries mapped to multiple frameworks, automated and manual evidence collection with timestamped artifacts, workflow automation for assessments and approvals, POA&M tracking with milestone management, risk register with scoring and treatment tracking, executive dashboards, multi-framework crosswalking, role-based access for system owners, ISSOs, assessors, and AOs.

**Integration points**:

| Integration Type | Purpose |
|-----------------|---------|
| SSO / Directory Services | Authenticate users, sync organizational roles |
| Ticketing Systems | Link POA&M items and findings to remediation tickets |
| Cloud Provider APIs | Pull configuration data, resource inventories, compliance state |
| Vulnerability Scanners | Ingest scan results and map findings to controls (RA-5) |
| SIEM | Import security events as evidence for AU controls |
| CI/CD Pipelines | Trigger evidence collection on deployment events |

## Vulnerability Management

**Purpose**: Identify, classify, prioritize, and track remediation of security vulnerabilities across infrastructure, applications, containers, and databases.

| Scanner Type | Target | Typical Output |
|-------------|--------|----------------|
| Infrastructure | Servers, network devices, OS | CVE findings, missing patches, severity ratings |
| Web Application | Web apps, APIs | OWASP Top 10, injection flaws, auth weaknesses |
| Container | Images, registries, running containers | Image vulnerabilities, base image risks |
| Database | Database instances, schemas | Misconfigurations, excessive privileges |

**Scan methodology**: Authenticated scans use credentials for internal inspection with fewer false negatives; unauthenticated scans simulate an external attacker. Agent-based scanning installs lightweight agents for continuous assessment; agentless scanning uses network-based discovery without host software.

**Key outputs**: CVE identifiers, CVSS scores (Base, Temporal, Environmental), remediation guidance, exploitability indicators, affected asset lists, trending reports.

**Compliance use**: RA-5, SI-2, PCI DSS Req 11.3, FedRAMP monthly scanning requirements.

## Configuration Compliance / SCAP

**Purpose**: Validate that system configurations align with approved baselines, industry benchmarks, and hardening standards (CIS Benchmarks, DISA STIGs, organizational baselines).

**SCAP components**:

| Component | Full Name | Purpose |
|-----------|-----------|---------|
| XCCDF | Extensible Configuration Checklist Description Format | Define checklists and benchmarks in structured XML |
| OVAL | Open Vulnerability and Assessment Language | Express system state checks and vulnerability conditions |
| CVE | Common Vulnerabilities and Exposures | Uniquely identify known vulnerabilities |
| CCE | Common Configuration Enumeration | Uniquely identify configuration issues |
| CPE | Common Platform Enumeration | Standardize naming of hardware, OS, and applications |

**Key outputs**: Compliance scores (percentage of rules passed), deviation reports, remediation scripts, rule-by-rule pass/fail evidence.

**Compliance use**: CM-6 (Configuration Settings), CM-2 (Baseline Configuration), SA-4.

## SIEM / Log Management

**Purpose**: Collect, normalize, store, correlate, and analyze log data from across the system boundary to detect security incidents and provide audit evidence.

**Key capabilities**: Log collection from servers, network devices, applications, databases, cloud services, and security tools; event normalization and enrichment; correlation rules and detection logic; real-time alerting and escalation; long-term retention (typically 90 days online, 1 year archived); search and forensic investigation; compliance dashboards and reporting.

**Compliance use**: AU-2, AU-6, AU-12, SI-4, PCI DSS Req 10. Provides audit trail evidence and anomaly detection for incident response.

## Identity and Access Management (IAM)

**Purpose**: Manage the lifecycle of user identities, enforce authentication and authorization policies, and govern access to systems and data.

| Component | Purpose |
|-----------|---------|
| Directory Services | Centralized identity store; user provisioning and group management |
| Multi-Factor Authentication (MFA) | Two or more authentication factors for system access |
| Single Sign-On (SSO) | Federated authentication via SAML, OIDC |
| Privileged Access Management (PAM) | Vault, rotate, monitor privileged credentials; session recording |
| Access Governance | Periodic access reviews, role mining, separation of duties |
| Identity Lifecycle Management | Automated provisioning and de-provisioning tied to HR events |

**Compliance use**: AC-2, AC-6, IA-2, IA-5, PCI DSS Req 7, Req 8. Quarterly access reviews satisfy AC-2(j) and SOC 2 CC6.1.

## Endpoint Protection / EDR

**Purpose**: Prevent, detect, and respond to malware and adversarial activity on endpoints.

**Key capabilities**: Signature-based and behavioral malware detection, EDR with telemetry collection and threat hunting, application allowlisting, host-based firewall management, forensic data collection, automated containment and isolation.

**Compliance use**: SI-3 (Malware Protection), SI-4, PCI DSS Req 5. Provides malware scanning coverage and detection evidence for continuous monitoring.

## Asset Management / CMDB

**Purpose**: Maintain an authoritative inventory of all hardware, software, and information assets within the authorization boundary.

**Key capabilities**: Automated asset discovery, classification by type/criticality/data sensitivity/ownership, lifecycle tracking from procurement through decommission, software license management, dependency mapping, integration with scanners for 100% coverage.

**Compliance use**: CM-8 (System Component Inventory), PM-5, PCI DSS Req 12.5.1. Authoritative source for scan coverage and boundary completeness.

## Ticketing / Workflow

**Purpose**: Track change requests, incidents, service requests, and remediation actions through structured workflows with audit trails.

**Key capabilities**: Change management with approval gates and CAB review, incident tracking with severity classification and escalation, SLA tracking, linkage to POA&M items and vulnerability findings, full audit trail of state transitions and approvals.

**Compliance use**: CM-3 (Configuration Change Control), IR-5, IR-6, PCI DSS Req 6.5.1.

## Policy Management

**Purpose**: Author, review, approve, publish, distribute, and track acknowledgment of security policies, standards, and procedures.

**Key capabilities**: Collaborative drafting with version control, review and approval workflows, scheduled review cycles with automated reminders, employee acknowledgment tracking, policy-to-framework mapping, document repository with retention management.

**Compliance use**: PL-1, AT-2, PCI DSS Req 12. Evidence that policies are reviewed at defined intervals and communicated to personnel.

## Backup and Recovery

**Purpose**: Protect availability through scheduled backups, integrity verification, and tested recovery procedures.

**Key capabilities**: Automated scheduling aligned with RPO, integrity testing, offsite/geographically separated storage, recovery testing with documented results, encryption in transit and at rest, retention management.

**Compliance use**: CP-9 (System Backup), CP-10 (Recovery and Reconstitution). Restoration testing provides CP-4 evidence. PCI DSS does not have a dedicated backup requirement.

## Penetration Testing

**Purpose**: Simulate adversarial attacks to identify exploitable vulnerabilities and validate detective and preventive controls.

| Test Type | Scope | Methodology |
|-----------|-------|-------------|
| External | Internet-facing assets, perimeter | Simulate external attacker without internal access |
| Internal | Internal network, lateral movement | Simulate insider or post-breach attacker |
| Web Application | Application logic, auth flows | OWASP Testing Guide methodology |
| Social Engineering | Personnel, email, physical | Phishing campaigns, pretexting, physical attempts |
| Wireless | Wireless networks, rogue APs | Test encryption, authentication, segmentation |

**Key outputs**: Findings report with exploitation evidence, risk ratings, remediation recommendations, retest validation.

**Compliance use**: CA-8, PCI DSS Req 11.4, Req 6.4. FedRAMP requires annual penetration testing.

## OSCAL Tooling

**Purpose**: Create, validate, and transform security documentation in OSCAL format for machine-readable compliance artifacts and automated validation.

**Key capabilities**: Author OSCAL documents (SSP, SAP, SAR, POA&M, Component Definition, Catalog, Profile) in JSON, XML, or YAML; schema validation; format conversion; automated SSP assembly from component definitions; control implementation mapping; version diff and change tracking.

**FedRAMP OSCAL requirements**: FedRAMP requires machine-readable OSCAL SSPs for new authorizations, enabling automated validation and submission through review pipelines.

**Compliance use**: Enables data-centric compliance, automated control inheritance tracking, continuous authorization workflows, and interoperability between GRC platforms and federal assessment processes.

## Capability Matrix — Framework Mapping

| Tool Category | NIST 800-53 | PCI DSS v4 | FedRAMP | HIPAA | SOC 2 |
|--------------|-------------|------------|---------|-------|-------|
| GRC Platform | All families | All Reqs | All controls | All safeguards | All TSC |
| Vulnerability Mgmt | RA-5, SI-2 | Req 11.3 | RA-5 | Technical safeguards | CC7.1 |
| Config Compliance | CM-2, CM-6 | Req 2.2 | CM-2, CM-6 | Technical safeguards | CC6.1 |
| SIEM / Log Mgmt | AU-2, AU-6, AU-12 | Req 10 | AU family | Audit controls (164.312(b)) | CC7.2, CC7.3 |
| IAM | AC-2, AC-6, IA-2 | Req 7, Req 8 | AC, IA families | Access controls (164.312(a)) | CC6.1, CC6.2, CC6.3 |
| Endpoint / EDR | SI-3, SI-4 | Req 5 | SI-3, SI-4 | Technical safeguards | CC6.8 |
| Asset Mgmt / CMDB | CM-8, PM-5 | Req 12.5.1 | CM-8 | Asset inventory | CC6.1 |
| Ticketing / Workflow | CM-3, IR-5 | Req 6.5.1 | CM-3, IR-5 | Administrative safeguards | CC8.1 |
| Policy Mgmt | PL-1, AT-2 | Req 12 | PL-1 | Policies (164.316) | CC1.1 |
| Backup / Recovery | CP-9, CP-10 | -- | CP-9, CP-10 | Contingency (164.308(a)(7)) | A1.2 |
| Penetration Testing | CA-8 | Req 11.4 | CA-8 | Risk analysis support | CC4.1 |
| OSCAL Tooling | N/A | N/A | OSCAL mandate | N/A | N/A |

## References

- NIST SP 800-53 Rev. 5 — Security and Privacy Controls
- NIST SP 800-137 — Information Security Continuous Monitoring
- NIST OSCAL — Open Security Controls Assessment Language
- SCAP 1.3 — Security Content Automation Protocol
- CIS Benchmarks — Center for Internet Security configuration guidelines
- DISA STIGs — Security Technical Implementation Guides
