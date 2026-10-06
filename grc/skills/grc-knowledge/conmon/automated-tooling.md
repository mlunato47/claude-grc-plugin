# Automated Tooling for Continuous Monitoring

> **CR26 note (June 2026):** where this file cites FedRAMP monthly-scanning requirements, that is the legacy Rev5 cadence; FedRAMP 20x's VDR standard requires persistent, class-scaled detection instead (a stronger automation case, not a weaker one) — see `frameworks/fedramp-20x.md`.

## Overview

Automated tooling forms the backbone of an effective Continuous Monitoring (ConMon) program. Automation enables consistent, repeatable, and scalable monitoring activities that would be impractical to perform manually. FedRAMP and NIST guidance strongly encourage automation wherever possible, and certain monitoring activities (such as monthly vulnerability scanning) explicitly require automated tools.

---

## Tool Categories and Evidence Types

### Vulnerability Scanners

| Sub-Category | Purpose | Example Tools | Evidence Produced |
|-------------|---------|---------------|-------------------|
| Infrastructure / OS | Scan hosts for OS and application vulnerabilities | Nessus, Qualys, Rapid7 InsightVM, OpenVAS | Host vulnerability reports, CVSS-scored findings, plugin output, remediation guidance |
| Web Application | Identify OWASP Top 10 and application-layer vulnerabilities | Burp Suite, OWASP ZAP, Acunetix, Qualys WAS | Web app vulnerability reports, request/response evidence, injection proof |
| Container | Scan container images and running containers for known CVEs | Prisma Cloud (Twistlock), Aqua Security, Trivy, Grype | Image CVE reports, base image analysis, layer-by-layer findings |
| Database | Assess database configurations, missing patches, and access controls | DbProtect, Nessus (database plugins), AppDetectivePro | Database vulnerability reports, configuration compliance results |

**Key requirements:**
- Scans must be authenticated (credentialed) to produce accurate results
- All in-scope assets must be included in scan targets
- Infrastructure scans must cover all TCP/UDP ports (not just common ports)
- Scan results must include CVSS base scores for severity classification

### Configuration Compliance Scanners

| Purpose | Example Tools | Evidence Produced |
|---------|---------------|-------------------|
| Validate system configurations against approved baselines | Nessus Compliance, Qualys Policy Compliance, SCAP-compliant tools, Chef InSpec, Ansible | Configuration compliance reports, pass/fail per check, deviation listings, CIS benchmark scores |

**Key requirements:**
- Baselines must be documented and approved (CIS Benchmarks, DISA STIGs, or organizationally defined)
- Compliance scans must map to specific NIST 800-53 controls (primarily CM-6, CM-2)
- Deviations must be documented with justification and compensating controls

### SIEM and Log Management

| Purpose | Example Tools | Evidence Produced |
|---------|---------------|-------------------|
| Aggregate, correlate, and analyze security event logs from all in-scope systems | Splunk, Microsoft Sentinel (formerly Azure Sentinel), Elastic SIEM, IBM QRadar, Google Security Operations (formerly Chronicle) | Alert reports, correlation rule triggers, log retention evidence, incident timelines, audit trail reports |

**Key requirements:**
- Must collect logs from all in-scope assets (servers, network devices, endpoints, applications, databases)
- Log retention must meet organizational and regulatory requirements (Legacy FedRAMP Rev5 AU-11 value, in force until CR26 becomes mandatory Jan 1, 2027: at least 90 days online, with longer retention per NARA schedules and the agency's logging baseline — OMB M-26-14 (May 22, 2026) rescinded M-21-31; the new federal minimum is logs actively searchable for 6 months and retrievable for 12 months — not a flat "1 year"; CR26: no FedRAMP-assigned value)
- Correlation rules must be tuned to detect relevant security events while minimizing false positives
- Must support AU-2, AU-6, SI-4 controls

### Endpoint Detection and Response (EDR)

| Purpose | Example Tools | Evidence Produced |
|---------|---------------|-------------------|
| Monitor endpoints for malicious activity, provide threat detection and response capabilities | CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne, Carbon Black | Threat detection alerts, endpoint telemetry, incident investigation data, malware analysis reports |

**Key requirements:**
- Must be deployed on all in-scope endpoints (servers and workstations)
- Must provide real-time alerting for detected threats
- Supports SI-3 (Malicious Code Protection) and SI-4 (System Monitoring) controls

### Network Monitoring / IDS / IPS

| Purpose | Example Tools | Evidence Produced |
|---------|---------------|-------------------|
| Monitor network traffic for anomalies, intrusions, and policy violations | Snort, Suricata, Zeek (Bro), Palo Alto Networks, Cisco Firepower | Network intrusion alerts, traffic analysis reports, blocked connection logs, flow data |

**Key requirements:**
- Must monitor traffic at authorization boundary and key internal segments
- Signature updates must be applied regularly (daily or more frequently)
- Supports SC-7 (Boundary Protection) and SI-4 (System Monitoring) controls

### Asset Discovery and Inventory

| Purpose | Example Tools | Evidence Produced |
|---------|---------------|-------------------|
| Discover and maintain an authoritative inventory of all hardware and software assets | Qualys Asset Inventory, ServiceNow CMDB, Lansweeper, Axonius, Rumble | Asset inventory reports, new/decommissioned asset lists, unauthorized asset alerts |

**Key requirements:**
- Inventory must be continuously updated (automated discovery preferred)
- Must track hardware, software, virtual assets, containers, and cloud resources
- Supports CM-8 (System Component Inventory) and PM-5 (System Inventory) controls

### Patch Management

| Purpose | Example Tools | Evidence Produced |
|---------|---------------|-------------------|
| Identify, test, and deploy patches to remediate known vulnerabilities | WSUS, SCCM/MECM, Ivanti, ManageEngine, Automox | Patch compliance reports, deployment status, failed patch lists, patch cycle metrics |

**Key requirements:**
- Must track patch status across all in-scope assets
- Patches must be applied within defined SLAs (Legacy FedRAMP Rev5 values, in force until CR26 becomes mandatory Jan 1, 2027: SI-2(c) flat 30 days from release for security-relevant updates; RA-5(d) High 30 / Moderate 90 / Low 180 days from discovery — FedRAMP has no "Critical" category. CR26: VDR timeframes by PAIN and reachability, 12 hours to 192 days; KEVs per CISA due dates)
- Supports SI-2 (Flaw Remediation) control

### GRC Platforms

| Purpose | Example Tools | Evidence Produced |
|---------|---------------|-------------------|
| Centralize compliance management, control tracking, evidence collection, and risk reporting | CSAM, eMASS, RegScale, Telos Xacta, ServiceNow GRC, ZenGRC | System security plans, POA&M reports, assessment results, control status dashboards, evidence repositories |

**Key requirements:**
- Must serve as the system of record for authorization packages
- Must integrate with scanning and monitoring tools to ingest findings automatically
- Must produce FedRAMP-required deliverable formats (legacy Rev5 templates; under CR26, JSON valid against FedRAMP's schemas at github.com/FedRAMP/schemas — OSCAL is optional)

### SOAR (Security Orchestration, Automation, and Response)

| Purpose | Example Tools | Evidence Produced |
|---------|---------------|-------------------|
| Automate incident response workflows, orchestrate tool integration, streamline analyst tasks | Splunk SOAR (Phantom), Palo Alto XSOAR, Swimlane, Tines | Playbook execution logs, automated response evidence, incident enrichment data, response time metrics |

**Key requirements:**
- Playbooks should align with incident response plan procedures
- Must integrate with SIEM, EDR, and ticketing systems
- Supports IR-4 (Incident Handling) and IR-5 (Incident Monitoring) controls

---

## SCAP Protocol Overview

The Security Content Automation Protocol (SCAP) is a suite of specifications maintained by NIST that standardize the format and nomenclature for communicating security configuration and vulnerability information.

| Component | Full Name | Purpose |
|-----------|-----------|---------|
| **XCCDF** | Extensible Configuration Checklist Description Format | Defines security checklists and benchmarks in a structured XML format; provides rules, profiles, and scoring |
| **OVAL** | Open Vulnerability and Assessment Language | Standardized language for checking system state (installed software, configuration settings, patches) |
| **CVE** | Common Vulnerabilities and Exposures | Unique identifiers for publicly known vulnerabilities (e.g., CVE-2024-12345) |
| **CCE** | Common Configuration Enumeration | Unique identifiers for system configuration issues (e.g., CCE-12345-6) |
| **CPE** | Common Platform Enumeration | Standardized naming for hardware, software, and operating systems (e.g., cpe:/o:microsoft:windows_server_2022) |
| **CVSS** | Common Vulnerability Scoring System | Standardized framework for rating vulnerability severity (0.0-10.0 scale) |

SCAP-validated tools can ingest SCAP content (such as DISA STIGs or CIS benchmarks in XCCDF/OVAL format) and produce standardized compliance reports.

---

## FedRAMP Scanner Requirements

**Legacy FedRAMP Rev5 requirements (in force until the Rev5 VDR rules take hold: required Dec 7, 2026, grace to Mar 7, 2027).** FedRAMP imposes specific requirements on scanning activities:

- **Authenticated scans** — All vulnerability scans must use credentialed (authenticated) scanning to produce accurate results. Unauthenticated scans are not accepted as primary evidence.
- **Monthly infrastructure scans** — OS-level vulnerability scans must be performed at least monthly on all in-scope assets.
- **Monthly web application scans** — Web application scans must be performed at least monthly (or quarterly for Low baselines).
- **Monthly database scans** — Database vulnerability scans must be performed at least monthly.
- **Container scans** — Container images must be scanned before deployment and at least monthly for running containers.
- **Full port range** — Scans must cover all 65,535 TCP ports and relevant UDP ports.
- **100% asset coverage** — All assets in the authorization boundary must be scanned. Any gaps must be documented with justification.
- **Unique vulnerability tracking** — CSPs must track and report unique vulnerability counts with month-over-month trending.

**CR26 VDR detection cadences:** Rev5 providers MUST verify machine-based resources at least monthly; Class C SHOULD check drift-prone resources every 14 days, stable resources monthly, and sample every 3 days; Class D 7 days / monthly / daily; non-machine resources every 3 months. Reporting is monthly and human-readable (VER-TFR-MHR).

---

## Tool Output Formats and Integration

Effective ConMon programs integrate tool outputs into a unified workflow:

| Format | Common Usage | Integration Method |
|--------|-------------|-------------------|
| CSV/Excel | Scan exports, POA&M templates | Manual import to GRC platform |
| XML (SCAP) | XCCDF results, OVAL assessments | Automated ingest by SCAP-compatible tools |
| JSON | API responses, cloud-native tool outputs | API-based integration with GRC/SIEM |
| PDF | Human-readable reports, executive summaries | Document management, submission packages |
| Syslog/CEF | Log events from network devices, security tools | Real-time streaming to SIEM |
| STIX/TAXII | Threat intelligence feeds | Automated threat intelligence platform ingest |

**Integration best practices:**
- Use APIs to automate data flow between tools wherever possible
- Maintain a single source of truth for vulnerability findings (typically the GRC platform)
- Automate POA&M creation from scan findings to reduce manual effort and errors
- Ensure all tool outputs include timestamps, asset identifiers, and severity ratings for correlation

---

## References

- NIST SP 800-137: Information Security Continuous Monitoring
- NIST SP 800-126 Rev. 3: The Technical Specification for SCAP
- NIST SP 800-53 Rev. 5: CA-7, RA-5, CM-6, SI-2, SI-4, AU-2, AU-6
- FedRAMP Continuous Monitoring Strategy Guide (legacy; consolidated into the ConMon Playbook v1.0, Nov 2025)
- FedRAMP Vulnerability Scanning Requirements (legacy Rev5; superseded under CR26 by the VDR/VER rulesets)
- CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks
