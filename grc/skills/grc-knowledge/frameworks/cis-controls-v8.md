# CIS Controls v8.1 Reference

## Overview

The CIS Critical Security Controls (CIS Controls) are a prioritized, community-developed set of cybersecurity best practices published by the Center for Internet Security (CIS). Version 8.1 (June 2024) reorganizes and updates the controls to reflect modern enterprise environments including cloud, mobile, hybrid, and work-from-home architectures.

CIS Controls v8.1 contains **18 Controls** comprising **153 Safeguards** (formerly Sub-Controls). Controls are ordered by attack-mitigation priority rather than by compliance domain. Each Safeguard is assigned to one or more Implementation Groups to provide a phased adoption path.

## Implementation Groups (IGs)

| IG | Description | Safeguards | Cumulative | Typical Organization |
|----|-------------|:----------:|:----------:|----------------------|
| **IG1** | Essential Cyber Hygiene | 56 | 56 | Small/medium, limited IT staff, low data sensitivity |
| **IG2** | Enterprise IT management | 74 | 130 | Multiple departments, regulatory obligations, moderate risk |
| **IG3** | Full control set | 23 | 153 | Mature security programs, high-value assets, advanced threats |

IG1 is the minimum recommended baseline. Each successive IG is cumulative -- IG2 includes all of IG1, and IG3 includes all of IG1 and IG2.

## Controls and Safeguards

### Control 01 -- Inventory and Control of Enterprise Assets

Actively manage all enterprise assets connected to the network so that only authorized assets are given access.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 1.1 | Establish and Maintain Detailed Enterprise Asset Inventory | IG1 |
| 1.2 | Address Unauthorized Assets | IG1 |
| 1.3 | Utilize an Active Discovery Tool | IG2 |
| 1.4 | Use DHCP Logging to Update Enterprise Asset Inventory | IG2 |
| 1.5 | Use a Passive Asset Discovery Tool | IG3 |

### Control 02 -- Inventory and Control of Software Assets

Actively manage all software so that only authorized software is installed and can execute.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 2.1 | Establish and Maintain a Software Inventory | IG1 |
| 2.2 | Ensure Authorized Software is Currently Supported | IG1 |
| 2.3 | Address Unauthorized Software | IG1 |
| 2.4 | Utilize Automated Software Inventory Tools | IG2 |
| 2.5 | Allowlist Authorized Software | IG2 |
| 2.6 | Allowlist Authorized Libraries | IG2 |
| 2.7 | Allowlist Authorized Scripts | IG3 |

### Control 03 -- Data Protection

Develop processes and technical controls to identify, classify, securely handle, retain, and dispose of data.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 3.1 | Establish and Maintain a Data Management Process | IG1 |
| 3.2 | Establish and Maintain a Data Inventory | IG1 |
| 3.3 | Configure Data Access Control Lists | IG1 |
| 3.4 | Enforce Data Retention | IG1 |
| 3.5 | Securely Dispose of Data | IG1 |
| 3.6 | Encrypt Data on End-User Devices | IG1 |
| 3.7 | Establish and Maintain a Data Classification Scheme | IG2 |
| 3.8 | Document Data Flows | IG2 |
| 3.9 | Encrypt Data on Removable Media | IG2 |
| 3.10 | Encrypt Sensitive Data in Transit | IG2 |
| 3.11 | Encrypt Sensitive Data at Rest | IG2 |
| 3.12 | Segment Data Processing and Storage Based on Sensitivity | IG2 |
| 3.13 | Deploy a Data Loss Prevention Solution | IG3 |
| 3.14 | Log Sensitive Data Access | IG3 |

### Control 04 -- Secure Configuration of Enterprise Assets and Software

Establish and maintain secure configurations for enterprise assets and software.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 4.1 | Establish and Maintain a Secure Configuration Process | IG1 |
| 4.2 | Establish and Maintain a Secure Configuration Process for Network Infrastructure | IG1 |
| 4.3 | Configure Automatic Session Locking on Enterprise Assets | IG1 |
| 4.4 | Implement and Manage a Firewall on Servers | IG1 |
| 4.5 | Implement and Manage a Firewall on End-User Devices | IG1 |
| 4.6 | Securely Manage Enterprise Assets and Software | IG1 |
| 4.7 | Manage Default Accounts on Enterprise Assets and Software | IG1 |
| 4.8 | Uninstall or Disable Unnecessary Services on Enterprise Assets and Software | IG2 |
| 4.9 | Configure Trusted DNS Servers on Enterprise Assets | IG2 |
| 4.10 | Enforce Automatic Device Lockout on Portable End-User Devices | IG2 |
| 4.11 | Enforce Remote Wipe Capability on Portable End-User Devices | IG2 |
| 4.12 | Separate Enterprise Workspaces on Mobile End-User Devices | IG2 |

### Control 05 -- Account Management

Use processes and tools to assign and manage authorization to credentials for user accounts.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 5.1 | Establish and Maintain an Inventory of Accounts | IG1 |
| 5.2 | Use Unique Passwords | IG1 |
| 5.3 | Disable Dormant Accounts | IG1 |
| 5.4 | Restrict Administrator Privileges to Dedicated Administrator Accounts | IG1 |
| 5.5 | Establish and Maintain an Inventory of Service Accounts | IG2 |
| 5.6 | Centralize Account Management | IG2 |

### Control 06 -- Access Control Management

Create, assign, manage, and revoke access credentials and privileges for user, administrator, and service accounts.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 6.1 | Establish an Access Granting Process | IG1 |
| 6.2 | Establish an Access Revoking Process | IG1 |
| 6.3 | Require MFA for Externally-Exposed Applications | IG1 |
| 6.4 | Require MFA for Remote Network Access | IG1 |
| 6.5 | Require MFA for Administrative Access | IG1 |
| 6.6 | Establish and Maintain an Inventory of Authentication and Authorization Systems | IG2 |
| 6.7 | Centralize Access Control | IG2 |
| 6.8 | Define and Maintain Role-Based Access Control | IG3 |

### Control 07 -- Continuous Vulnerability Management

Continuously assess and track vulnerabilities on all enterprise assets to remediate and minimize the window of opportunity for attackers.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 7.1 | Establish and Maintain a Vulnerability Management Process | IG1 |
| 7.2 | Establish and Maintain a Remediation Process | IG1 |
| 7.3 | Perform Automated Operating System Patch Management | IG1 |
| 7.4 | Perform Automated Application Patch Management | IG1 |
| 7.5 | Perform Automated Vulnerability Scans of Internal Enterprise Assets | IG2 |
| 7.6 | Perform Automated Vulnerability Scans of Externally-Exposed Enterprise Assets | IG2 |
| 7.7 | Remediate Detected Vulnerabilities | IG2 |

### Control 08 -- Audit Log Management

Collect, alert, review, and retain audit logs of events that could help detect, understand, or recover from an attack.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 8.1 | Establish and Maintain an Audit Log Management Process | IG1 |
| 8.2 | Collect Audit Logs | IG1 |
| 8.3 | Ensure Adequate Audit Log Storage | IG1 |
| 8.4 | Standardize Time Synchronization | IG2 |
| 8.5 | Collect Detailed Audit Logs | IG2 |
| 8.6 | Collect DNS Query Audit Logs | IG2 |
| 8.7 | Collect URL Request Audit Logs | IG2 |
| 8.8 | Collect Command-Line Audit Logs | IG2 |
| 8.9 | Centralize Audit Logs | IG2 |
| 8.10 | Retain Audit Logs | IG2 |
| 8.11 | Conduct Audit Log Reviews | IG2 |
| 8.12 | Collect Service Provider Logs | IG3 |

### Control 09 -- Email and Web Browser Protections

Improve protections and detections of threats from email and web vectors.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 9.1 | Ensure Use of Only Fully Supported Browsers and Email Clients | IG1 |
| 9.2 | Use DNS Filtering Services | IG1 |
| 9.3 | Maintain and Enforce Network-Based URL Filters | IG2 |
| 9.4 | Restrict Unnecessary or Unauthorized Browser and Email Client Extensions | IG2 |
| 9.5 | Implement DMARC | IG2 |
| 9.6 | Block Unnecessary File Types | IG2 |
| 9.7 | Deploy and Maintain Email Server Anti-Malware Protections | IG2 |

### Control 10 -- Malware Defenses

Prevent or control the installation, spread, and execution of malicious applications, code, or scripts.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 10.1 | Deploy and Maintain Anti-Malware Software | IG1 |
| 10.2 | Configure Automatic Anti-Malware Signature Updates | IG1 |
| 10.3 | Disable Autorun and Autoplay for Removable Media | IG1 |
| 10.4 | Configure Automatic Anti-Malware Scanning of Removable Media | IG2 |
| 10.5 | Enable Anti-Exploitation Features | IG2 |
| 10.6 | Centrally Manage Anti-Malware Software | IG2 |
| 10.7 | Use Behavior-Based Anti-Malware Software | IG2 |

### Control 11 -- Data Recovery

Establish and maintain data recovery practices sufficient to restore in-scope enterprise assets to a pre-incident and trusted state.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 11.1 | Establish and Maintain a Data Recovery Process | IG1 |
| 11.2 | Perform Automated Backups | IG1 |
| 11.3 | Protect Recovery Data | IG1 |
| 11.4 | Establish and Maintain an Isolated Instance of Recovery Data | IG1 |
| 11.5 | Test Data Recovery | IG2 |

### Control 12 -- Network Infrastructure Management

Establish and maintain secure configuration and management of network infrastructure.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 12.1 | Ensure Network Infrastructure is Up-to-Date | IG1 |
| 12.2 | Establish and Maintain a Secure Network Architecture | IG2 |
| 12.3 | Securely Manage Network Infrastructure | IG2 |
| 12.4 | Establish and Maintain Architecture Diagram(s) | IG2 |
| 12.5 | Centralize Network AAA | IG2 |
| 12.6 | Use Secure Network Management and Communication Protocols | IG2 |
| 12.7 | Ensure Remote Devices Utilize a VPN and Connect to Enterprise AAA Infrastructure | IG2 |
| 12.8 | Establish and Maintain Dedicated Computing Resources for All Administrative Work | IG3 |

### Control 13 -- Network Monitoring and Defense

Operate processes and tooling to establish and maintain comprehensive network monitoring and defense.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 13.1 | Centralize Security Event Alerting | IG2 |
| 13.2 | Deploy a Host-Based Intrusion Detection Solution | IG2 |
| 13.3 | Deploy a Network Intrusion Detection Solution | IG2 |
| 13.4 | Perform Traffic Filtering Between Network Segments | IG2 |
| 13.5 | Manage Access Control for Remote Assets | IG2 |
| 13.6 | Collect Network Traffic Flow Logs | IG2 |
| 13.7 | Deploy a Host-Based Intrusion Prevention Solution | IG3 |
| 13.8 | Deploy a Network Intrusion Prevention Solution | IG3 |
| 13.9 | Deploy Port-Level Access Control | IG3 |
| 13.10 | Perform Application Layer Filtering | IG3 |
| 13.11 | Tune Security Event Alerting Thresholds | IG3 |

### Control 14 -- Security Awareness and Skills Training

Establish and maintain a security awareness program to influence behavior among the workforce.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 14.1 | Establish and Maintain a Security Awareness Program | IG1 |
| 14.2 | Train Workforce Members to Recognize Social Engineering Attacks | IG1 |
| 14.3 | Train Workforce Members on Authentication Best Practices | IG1 |
| 14.4 | Train Workforce Members on Data Handling Best Practices | IG1 |
| 14.5 | Train Workforce Members on Causes of Unintentional Data Exposure | IG1 |
| 14.6 | Train Workforce Members on Recognizing and Reporting Security Incidents | IG1 |
| 14.7 | Train Workforce on How to Identify and Report Missing Security Updates | IG1 |
| 14.8 | Train Workforce on the Dangers of Connecting to and Transmitting Data Over Insecure Networks | IG1 |
| 14.9 | Conduct Role-Specific Security Awareness and Skills Training | IG2 |

### Control 15 -- Service Provider Management

Evaluate service providers who hold sensitive data or are responsible for critical IT platforms or processes.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 15.1 | Establish and Maintain an Inventory of Service Providers | IG1 |
| 15.2 | Establish and Maintain a Service Provider Management Policy | IG2 |
| 15.3 | Classify Service Providers | IG2 |
| 15.4 | Ensure Service Provider Contracts Include Security Requirements | IG2 |
| 15.5 | Assess Service Providers | IG2 |
| 15.6 | Monitor Service Providers | IG2 |
| 15.7 | Securely Decommission Service Providers | IG2 |

### Control 16 -- Application Software Security

Manage the security lifecycle of in-house developed, hosted, or acquired software.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 16.1 | Establish and Maintain a Secure Application Development Process | IG2 |
| 16.2 | Establish and Maintain a Process to Accept and Address Software Vulnerabilities | IG2 |
| 16.3 | Perform Root Cause Analysis on Security Vulnerabilities | IG2 |
| 16.4 | Establish and Maintain a Code-Level Security Review Process | IG2 |
| 16.5 | Use Up-to-Date and Trusted Third-Party Software Components | IG2 |
| 16.6 | Establish and Maintain a Severity Rating System for Application Vulnerabilities | IG2 |
| 16.7 | Use Standard Hardening Configuration Templates for Application Infrastructure | IG2 |
| 16.8 | Separate Production and Non-Production Systems | IG2 |
| 16.9 | Train Developers in Application Security Concepts and Secure Coding | IG2 |
| 16.10 | Apply Secure Design Principles in Application Architectures | IG2 |
| 16.11 | Leverage Vetted Modules or Services for Application Security Components | IG2 |
| 16.12 | Implement Code-Level Security Checks | IG3 |
| 16.13 | Conduct Application Penetration Testing | IG3 |
| 16.14 | Conduct Threat Modeling | IG3 |

### Control 17 -- Incident Response Management

Develop and maintain an incident response capability to prepare, detect, and quickly respond to an attack.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 17.1 | Designate Personnel to Manage Incident Handling | IG1 |
| 17.2 | Establish and Maintain Contact Information for Reporting Security Incidents | IG1 |
| 17.3 | Establish and Maintain an Enterprise Process for Reporting Incidents | IG1 |
| 17.4 | Establish and Maintain an Incident Response Process | IG2 |
| 17.5 | Assign Key Roles and Responsibilities | IG2 |
| 17.6 | Define Mechanisms for Communicating During Incident Response | IG2 |
| 17.7 | Conduct Routine Incident Response Exercises | IG2 |
| 17.8 | Conduct Post-Incident Reviews | IG2 |
| 17.9 | Establish and Maintain Security Incident Thresholds | IG3 |

### Control 18 -- Penetration Testing

Test the effectiveness and resiliency of enterprise assets through identifying and exploiting weaknesses in controls.

| Safeguard | Description | IG |
|-----------|-------------|----|
| 18.1 | Establish and Maintain a Penetration Testing Program | IG2 |
| 18.2 | Perform Periodic External Penetration Tests | IG2 |
| 18.3 | Remediate Penetration Test Findings | IG2 |
| 18.4 | Validate Security Measures | IG3 |
| 18.5 | Perform Periodic Internal Penetration Tests | IG3 |

## Mapping to NIST CSF Functions

| CIS Control | Primary CSF Function | Secondary |
|-------------|---------------------|-----------|
| 01 -- Enterprise Asset Inventory | Identify | |
| 02 -- Software Asset Inventory | Identify | |
| 03 -- Data Protection | Protect | Identify |
| 04 -- Secure Configuration | Protect | |
| 05 -- Account Management | Identify | Protect |
| 06 -- Access Control | Protect | |
| 07 -- Vulnerability Management | Identify | Protect |
| 08 -- Audit Log Management | Detect | |
| 09 -- Email and Web Browser Protections | Protect | Detect |
| 10 -- Malware Defenses | Protect | Detect |
| 11 -- Data Recovery | Recover | |
| 12 -- Network Infrastructure Management | Protect | |
| 13 -- Network Monitoring and Defense | Detect | Respond |
| 14 -- Security Awareness and Training | Protect | |
| 15 -- Service Provider Management | Identify | Protect |
| 16 -- Application Software Security | Protect | |
| 17 -- Incident Response Management | Respond | Recover |
| 18 -- Penetration Testing | Identify | Protect |

## CIS Benchmarks Relationship

CIS Benchmarks are prescriptive, platform-specific hardening guides that provide the technical implementation detail for many CIS Controls Safeguards:

- **CIS Controls** define *what* to do (e.g., Safeguard 4.1 -- establish secure configuration processes).
- **CIS Benchmarks** define *how* to do it for a specific platform (e.g., CIS Benchmark for Windows Server 2022, Ubuntu Linux 24.04, AWS Foundations).
- Benchmarks are scored at **Level 1** (broadly applicable, minimal performance impact) and **Level 2** (deeper hardening, may restrict functionality).
- Over 100 CIS Benchmarks exist across operating systems, cloud providers, databases, middleware, network devices, and desktop software.
- Benchmark recommendations include mappings back to CIS Controls Safeguard IDs.

## CIS Controls Assessment Specification (CAS)

CAS provides a standardized methodology for measuring each Safeguard's implementation. For each Safeguard, CAS defines:

| CAS Element | Purpose |
|-------------|---------|
| **Input(s)** | Data or artifacts required for assessment (e.g., asset inventory, configuration policy) |
| **Measure(s)** | Quantitative metrics derived from the inputs (e.g., count of assets with compliant configurations) |
| **Metric(s)** | Calculation producing a compliance ratio (e.g., compliant assets / total assets) |
| **Test(s)** | Procedures to validate the accuracy of the measures |

CAS enables organizations to move beyond binary pass/fail assessments and instead measure the degree of implementation as a percentage, supporting continuous improvement.

## Changes from v7.1 to v8

| Aspect | v7.1 | v8 / v8.1 |
|--------|------|-----------|
| Controls | 20 | 18 |
| Sub-Controls / Safeguards | 171 | 153 |
| Implementation Groups | Introduced in v7.1 | Refined; IG1 designated as minimum essential cyber hygiene |
| Cloud and SaaS | Limited coverage | Explicit inclusion throughout; removed on-premises-only assumptions |
| Mobile / WFH | Minimal | Dedicated Safeguards for mobile device management, remote access, portable devices |
| Terminology | Sub-Controls | Safeguards |
| Network model | Implicit perimeter-based | Zero-trust-aligned; asset-centric regardless of location |
| Service providers | Not explicitly covered | Control 15 added for third-party / service provider management |
| Data governance | Partially addressed | Control 3 expanded with data classification, DLP, data flow documentation |

Key consolidations: Former CSC 3 and CSC 11 were restructured across Controls 4, 7, and 12. Former CSC 17 was expanded into Control 14 with more granular Safeguards. Former CSC 19 and CSC 20 were consolidated into Controls 17 and 18.

## Safeguard Summary by Control and IG

| Control | Title | IG1 | IG2 | IG3 | Total |
|---------|-------|:---:|:---:|:---:|:-----:|
| 01 | Enterprise Asset Inventory | 2 | 4 | 5 | 5 |
| 02 | Software Asset Inventory | 3 | 6 | 7 | 7 |
| 03 | Data Protection | 6 | 12 | 14 | 14 |
| 04 | Secure Configuration | 7 | 12 | 12 | 12 |
| 05 | Account Management | 4 | 6 | 6 | 6 |
| 06 | Access Control | 5 | 7 | 8 | 8 |
| 07 | Vulnerability Management | 4 | 7 | 7 | 7 |
| 08 | Audit Log Management | 3 | 11 | 12 | 12 |
| 09 | Email and Web Browser Protections | 2 | 7 | 7 | 7 |
| 10 | Malware Defenses | 3 | 7 | 7 | 7 |
| 11 | Data Recovery | 4 | 5 | 5 | 5 |
| 12 | Network Infrastructure Management | 1 | 7 | 8 | 8 |
| 13 | Network Monitoring and Defense | 0 | 6 | 11 | 11 |
| 14 | Security Awareness and Training | 8 | 9 | 9 | 9 |
| 15 | Service Provider Management | 1 | 7 | 7 | 7 |
| 16 | Application Software Security | 0 | 11 | 14 | 14 |
| 17 | Incident Response Management | 3 | 8 | 9 | 9 |
| 18 | Penetration Testing | 0 | 3 | 5 | 5 |
| **Totals** | | **56** | **130** | **153** | **153** |

Note: IG2 and IG3 columns show cumulative safeguard counts (inclusive of all lower IGs). Official CIS totals are IG1=56, IG2=130 (cumulative), IG3=153 (cumulative). Individual per-control counts are approximate and should be verified against the official CIS Controls v8.1 document.
