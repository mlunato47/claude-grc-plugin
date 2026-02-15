# NIST 800-53 to CMMC / NIST 800-171 Mapping

## Overview

NIST SP 800-171 Rev 2 derives from the NIST SP 800-53 Moderate baseline through a tailoring process defined in NIST SP 800-171 Appendix D. The 800-53 Moderate baseline contains approximately 304 controls; from these, NIST selected and condensed requirements applicable to non-federal systems processing, storing, or transmitting Controlled Unclassified Information (CUI). Controls primarily satisfied by the federal government (e.g., the entire PM family, most PL controls, contingency planning) were excluded, as were controls not directly related to protecting the confidentiality of CUI.

The result is **110 security requirements** organized into 14 families (sections 3.1 through 3.14). An additional **61 Non-Federal Organization (NFO) controls** (Appendix E) are expected but not formally assessed.

**CMMC 2.0 Level 2 = NIST 800-171 Rev 2** -- the 110 security requirements map one-to-one to CMMC Level 2 practices. CMMC Level 1 maps to the 17 practices derived from FAR 52.204-21. CMMC Level 3 adds selected requirements from NIST SP 800-172.

## Mapping Methodology

The three-tier mapping chain works as follows:

```
NIST 800-53 (Moderate baseline)
    --> tailored/condensed -->
        NIST 800-171 Rev 2 (110 requirements)
            --> direct alignment -->
                CMMC 2.0 Level 2 (110 practices)
```

**Key principles**:
1. Each 800-171 requirement traces back to one or more 800-53 controls
2. 800-171 requirements often condense multiple 800-53 controls into a single requirement
3. CMMC Level 2 practice IDs use the 800-171 numbering (e.g., CMMC practice 3.1.1 = NIST 800-171 requirement 3.1.1)
4. The 800-53 controls listed are from the Moderate baseline; some also appear in Low or High baselines

**Version note**: NIST 800-171 Rev 2 was developed against 800-53 Rev 4. Some 800-53 control enhancements referenced in the mapping (e.g., AU-2(3), SC-18, SC-19) were withdrawn in 800-53 Rev 5 and incorporated into other controls. The mappings below preserve the official 800-171 Rev 2 Appendix D references for accuracy.

## Comprehensive Mapping by Family

### 3.1 Access Control (22 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.1.1 | Limit system access to authorized users | AC-2, AC-3, AC-17 | L2-3.1.1 |
| 3.1.2 | Limit system access to authorized functions/transactions | AC-2, AC-3, AC-17 | L2-3.1.2 |
| 3.1.3 | Control CUI flow per authorizations | AC-4 | L2-3.1.3 |
| 3.1.4 | Separate duties to reduce risk of malevolent activity | AC-5 | L2-3.1.4 |
| 3.1.5 | Employ least privilege including specific security functions | AC-6, AC-6(1), AC-6(5) | L2-3.1.5 |
| 3.1.6 | Use non-privileged accounts for non-security functions | AC-6(2) | L2-3.1.6 |
| 3.1.7 | Prevent non-privileged users from executing privileged functions | AC-6(9), AC-6(10) | L2-3.1.7 |
| 3.1.8 | Limit unsuccessful logon attempts | AC-7 | L2-3.1.8 |
| 3.1.9 | Provide privacy and security notices per CUI requirements | AC-8 | L2-3.1.9 |
| 3.1.10 | Use session lock with pattern-hiding displays | AC-11, AC-11(1) | L2-3.1.10 |
| 3.1.11 | Terminate user sessions after defined conditions | AC-12 | L2-3.1.11 |
| 3.1.12 | Monitor and control remote access sessions | AC-17(1) | L2-3.1.12 |
| 3.1.13 | Employ cryptographic mechanisms for remote access | AC-17(2) | L2-3.1.13 |
| 3.1.14 | Route remote access via managed access control points | AC-17(3) | L2-3.1.14 |
| 3.1.15 | Authorize remote execution of privileged commands | AC-17(4) | L2-3.1.15 |
| 3.1.16 | Authorize wireless access prior to connection | AC-18 | L2-3.1.16 |
| 3.1.17 | Protect wireless access using authentication and encryption | AC-18(1) | L2-3.1.17 |
| 3.1.18 | Control connection of mobile devices | AC-19 | L2-3.1.18 |
| 3.1.19 | Encrypt CUI on mobile devices and mobile platforms | AC-19(5) | L2-3.1.19 |
| 3.1.20 | Verify and control connections to external systems | AC-20, AC-20(1) | L2-3.1.20 |
| 3.1.21 | Limit use of portable storage on external systems | AC-20(2) | L2-3.1.21 |
| 3.1.22 | Control information posted on publicly accessible systems | AC-22 | L2-3.1.22 |

### 3.2 Awareness and Training (3 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.2.1 | Ensure personnel are aware of security risks and policies | AT-2 | L2-3.2.1 |
| 3.2.2 | Ensure personnel are trained to carry out security duties | AT-3 | L2-3.2.2 |
| 3.2.3 | Provide security awareness training on recognizing insider threats | AT-2(2) | L2-3.2.3 |

### 3.3 Audit and Accountability (9 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.3.1 | Create and retain system audit logs and records | AU-2, AU-3, AU-3(1), AU-12 | L2-3.3.1 |
| 3.3.2 | Ensure actions can be traced to individual users | AU-2, AU-3, AU-6, AU-12 | L2-3.3.2 |
| 3.3.3 | Review and update logged events | AU-2(3) | L2-3.3.3 |
| 3.3.4 | Alert on audit logging process failure | AU-5 | L2-3.3.4 |
| 3.3.5 | Correlate audit review, analysis, and reporting | AU-6(3) | L2-3.3.5 |
| 3.3.6 | Provide audit record reduction and report generation | AU-7 | L2-3.3.6 |
| 3.3.7 | Provide system capability for time stamp comparison | AU-8 | L2-3.3.7 |
| 3.3.8 | Protect audit information and tools from unauthorized access | AU-9 | L2-3.3.8 |
| 3.3.9 | Limit management of audit logging to a subset of privileged users | AU-9(4) | L2-3.3.9 |

### 3.4 Configuration Management (9 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.4.1 | Establish and maintain baseline configurations and inventories | CM-2, CM-6, CM-8, CM-8(1) | L2-3.4.1 |
| 3.4.2 | Establish and enforce security configuration settings | CM-2, CM-6, CM-6(1) | L2-3.4.2 |
| 3.4.3 | Track, review, approve/disapprove, and log changes | CM-3 | L2-3.4.3 |
| 3.4.4 | Analyze security impact of changes prior to implementation | CM-4 | L2-3.4.4 |
| 3.4.5 | Define, document, approve, and enforce physical and logical access restrictions for changes | CM-5 | L2-3.4.5 |
| 3.4.6 | Employ least functionality by configuring systems to provide only essential capabilities | CM-7 | L2-3.4.6 |
| 3.4.7 | Restrict, disable, or prevent use of nonessential programs, functions, ports, protocols, services | CM-7(1), CM-7(2) | L2-3.4.7 |
| 3.4.8 | Apply deny-by-exception (allowlisting) policy for unauthorized software | CM-7(4), CM-7(5) | L2-3.4.8 |
| 3.4.9 | Control and monitor user-installed software | CM-11 | L2-3.4.9 |

### 3.5 Identification and Authentication (11 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.5.1 | Identify system users, processes acting on behalf of users, and devices | IA-2, IA-5 | L2-3.5.1 |
| 3.5.2 | Authenticate (or verify) identities of users, processes, or devices | IA-2, IA-5 | L2-3.5.2 |
| 3.5.3 | Use multi-factor authentication for local and network access to privileged accounts and for network access to non-privileged accounts | IA-2(1), IA-2(2), IA-2(3) | L2-3.5.3 |
| 3.5.4 | Employ replay-resistant authentication mechanisms for network access to privileged and non-privileged accounts | IA-2(8) | L2-3.5.4 |
| 3.5.5 | Prevent reuse of identifiers for a defined period | IA-4 | L2-3.5.5 |
| 3.5.6 | Disable identifiers after a defined period of inactivity | IA-4(4) | L2-3.5.6 |
| 3.5.7 | Enforce a minimum password complexity and change of characters when new passwords are created | IA-5(1) | L2-3.5.7 |
| 3.5.8 | Prohibit password reuse for a specified number of generations | IA-5(1) | L2-3.5.8 |
| 3.5.9 | Allow temporary password use for system logons with immediate change to permanent password | IA-5(1) | L2-3.5.9 |
| 3.5.10 | Store and transmit only cryptographically protected passwords | IA-5(1) | L2-3.5.10 |
| 3.5.11 | Obscure feedback of authentication information | IA-6 | L2-3.5.11 |

### 3.6 Incident Response (3 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.6.1 | Establish IR capability including preparation, detection, analysis, containment, recovery, and user response activities | IR-2, IR-4, IR-5, IR-6, IR-7 | L2-3.6.1 |
| 3.6.2 | Track, document, and report incidents to designated officials and/or authorities | IR-6 | L2-3.6.2 |
| 3.6.3 | Test the organizational incident response capability | IR-3, IR-3(2) | L2-3.6.3 |

### 3.7 Maintenance (6 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.7.1 | Perform maintenance on organizational systems | MA-2 | L2-3.7.1 |
| 3.7.2 | Provide controls on tools, techniques, mechanisms, and personnel for system maintenance | MA-3, MA-3(1), MA-3(2) | L2-3.7.2 |
| 3.7.3 | Ensure equipment removed for off-site maintenance is sanitized of CUI | MA-3(3) | L2-3.7.3 |
| 3.7.4 | Check media containing diagnostic and test programs for malicious code | MA-3(2) | L2-3.7.4 |
| 3.7.5 | Require MFA for establishing nonlocal maintenance sessions and terminate such sessions when complete | MA-4 | L2-3.7.5 |
| 3.7.6 | Supervise maintenance activities of maintenance personnel without required access authorization | MA-5 | L2-3.7.6 |

### 3.8 Media Protection (9 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.8.1 | Protect (i.e., physically control and securely store) system media containing CUI | MP-2, MP-4 | L2-3.8.1 |
| 3.8.2 | Limit access to CUI on system media to authorized users | MP-2 | L2-3.8.2 |
| 3.8.3 | Sanitize or destroy system media containing CUI before disposal or release for reuse | MP-6 | L2-3.8.3 |
| 3.8.4 | Mark media with necessary CUI markings and distribution limitations | MP-3 | L2-3.8.4 |
| 3.8.5 | Control access to media containing CUI and maintain accountability for media during transport | MP-5 | L2-3.8.5 |
| 3.8.6 | Implement cryptographic mechanisms to protect CUI stored on digital media during transport | MP-5(4) | L2-3.8.6 |
| 3.8.7 | Control the use of removable media on system components | MP-7 | L2-3.8.7 |
| 3.8.8 | Prohibit the use of portable storage devices when such devices have no identifiable owner | MP-7(1) | L2-3.8.8 |
| 3.8.9 | Protect the confidentiality of backup CUI at storage locations | CP-9 | L2-3.8.9 |

### 3.9 Personnel Security (2 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.9.1 | Screen individuals prior to authorizing access to systems containing CUI | PS-3 | L2-3.9.1 |
| 3.9.2 | Ensure CUI and systems containing CUI are protected during and after personnel actions such as terminations and transfers | PS-4, PS-5 | L2-3.9.2 |

### 3.10 Physical Protection (6 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.10.1 | Limit physical access to organizational systems, equipment, and operating environments to authorized individuals | PE-2, PE-5 | L2-3.10.1 |
| 3.10.2 | Protect and monitor the physical facility and support infrastructure | PE-2, PE-3, PE-6 | L2-3.10.2 |
| 3.10.3 | Escort visitors and monitor visitor activity | PE-3 | L2-3.10.3 |
| 3.10.4 | Maintain audit logs of physical access | PE-3 | L2-3.10.4 |
| 3.10.5 | Control and manage physical access devices | PE-5 | L2-3.10.5 |
| 3.10.6 | Enforce safeguarding measures for CUI at alternate work sites | PE-17 | L2-3.10.6 |

### 3.11 Risk Assessment (3 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.11.1 | Periodically assess risk to organizational operations, assets, and individuals | RA-3 | L2-3.11.1 |
| 3.11.2 | Scan for vulnerabilities in organizational systems and applications periodically and when new vulnerabilities are identified | RA-5, RA-5(5) | L2-3.11.2 |
| 3.11.3 | Remediate vulnerabilities in accordance with risk assessments | RA-5 | L2-3.11.3 |

### 3.12 Security Assessment (4 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.12.1 | Periodically assess security controls to determine if controls are effective in their application | CA-2 | L2-3.12.1 |
| 3.12.2 | Develop and implement plans of action designed to correct deficiencies and reduce vulnerabilities | CA-5 | L2-3.12.2 |
| 3.12.3 | Monitor security controls on an ongoing basis to ensure continued effectiveness | CA-7 | L2-3.12.3 |
| 3.12.4 | Develop, document, and periodically update system security plans | CA-2, PL-2 | L2-3.12.4 |

### 3.13 System and Communications Protection (16 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.13.1 | Monitor, control, and protect communications at external and key internal boundaries | SC-7 | L2-3.13.1 |
| 3.13.2 | Employ architectural designs, software development techniques, and systems engineering principles that promote effective information security | SA-8 | L2-3.13.2 |
| 3.13.3 | Separate user functionality from system management functionality | SC-2 | L2-3.13.3 |
| 3.13.4 | Prevent unauthorized and unintended information transfer via shared system resources | SC-4 | L2-3.13.4 |
| 3.13.5 | Implement subnetworks for publicly accessible system components that are physically or logically separated from internal networks | SC-7(5) | L2-3.13.5 |
| 3.13.6 | Deny network communications traffic by default and allow by exception (deny all, permit by exception) | SC-7(5) | L2-3.13.6 |
| 3.13.7 | Prevent remote devices from simultaneously establishing non-remote connections with organizational systems and communicating via some other connection to resources in external networks (split tunneling) | SC-7(7) | L2-3.13.7 |
| 3.13.8 | Implement cryptographic mechanisms to prevent unauthorized disclosure of CUI during transmission | SC-8, SC-8(1) | L2-3.13.8 |
| 3.13.9 | Terminate network connections associated with communications sessions at the end of the sessions or after a defined period of inactivity | SC-10 | L2-3.13.9 |
| 3.13.10 | Establish and manage cryptographic keys for required cryptography | SC-12 | L2-3.13.10 |
| 3.13.11 | Employ FIPS-validated cryptography when used to protect the confidentiality of CUI | SC-13 | L2-3.13.11 |
| 3.13.12 | Prohibit remote activation of collaborative computing devices and provide indication of devices in use to users present at the device | SC-15 | L2-3.13.12 |
| 3.13.13 | Control and monitor the use of mobile code | SC-18 | L2-3.13.13 |
| 3.13.14 | Control and monitor the use of VoIP technologies | SC-19 | L2-3.13.14 |
| 3.13.15 | Protect the authenticity of communications sessions | SC-23 | L2-3.13.15 |
| 3.13.16 | Protect the confidentiality of CUI at rest | SC-28 | L2-3.13.16 |

### 3.14 System and Information Integrity (7 Requirements)

| 800-171 Req | Requirement Description | 800-53 Control(s) | CMMC Practice |
|-------------|------------------------|--------------------|---------------|
| 3.14.1 | Identify, report, and correct information and system flaws in a timely manner | SI-2 | L2-3.14.1 |
| 3.14.2 | Provide protection from malicious code at appropriate locations | SI-3 | L2-3.14.2 |
| 3.14.3 | Monitor system security alerts and advisories and take action in response | SI-5 | L2-3.14.3 |
| 3.14.4 | Update malicious code protection mechanisms when new releases are available | SI-3 | L2-3.14.4 |
| 3.14.5 | Perform periodic scans of the system and real-time scans of files from external sources | SI-3 | L2-3.14.5 |
| 3.14.6 | Monitor organizational systems including inbound and outbound communications traffic to detect attacks and indicators of potential attacks | SI-4, SI-4(4) | L2-3.14.6 |
| 3.14.7 | Identify unauthorized use of organizational systems | SI-4 | L2-3.14.7 |

## NIST 800-53 Moderate Controls NOT in 800-171

The 800-53 Moderate baseline contains approximately 304 controls (including enhancements). NIST 800-171 includes 110 requirements derived from these controls. The remaining controls were excluded through a structured tailoring process documented in NIST 800-171 Appendix D. Excluded controls fall into several categories:

### Entire Families Excluded

| 800-53 Family | Reason for Exclusion |
|---------------|---------------------|
| **CP (Contingency Planning)** | Primarily a federal responsibility; operational continuity of federal mission is a federal obligation. Note: CP-9 backup confidentiality is addressed in 3.8.9. |
| **PL (Planning)** | Security planning processes are federal administrative requirements. Note: PL-2 system security plans partially addressed in 3.12.4. |
| **PM (Program Management)** | Entirely federal management structure (CISO role, enterprise architecture, risk strategy). Not applicable to non-federal organizations. |
| **PT (PII Processing and Transparency)** | Added in Rev 5 as a privacy-focused family. 800-171 Rev 2 predates this addition and addresses privacy through other means. |
| **SA (System and Services Acquisition)** | Primarily federal acquisition and SDLC governance. Note: SA-8 security engineering principles addressed in 3.13.2. |
| **SR (Supply Chain Risk Management)** | Added in Rev 5. 800-171 Rev 2 predates this family. CMMC Level 3 addresses supply chain via 800-172. |

### NFO (Non-Federal Organization) Controls -- Appendix E

NIST 800-171 Appendix E identifies 61 controls that are "expected to be routinely satisfied by non-federal organizations without specification." These are not formally assessed under CMMC but are assumed to be in place as basic operational practices.

Examples of NFO controls:

| 800-53 Control | Description | Rationale for NFO Status |
|----------------|-------------|-------------------------|
| AC-1 | Access Control Policy and Procedures | Policy development is an organizational baseline expectation |
| AT-1 | Awareness and Training Policy and Procedures | Policy documentation expected at any mature organization |
| AU-1 | Audit and Accountability Policy and Procedures | Same -- organizational governance baseline |
| PE-1 | Physical and Environmental Protection Policy | Facility operations are a basic business function |
| PS-1 | Personnel Security Policy and Procedures | HR processes are standard organizational practice |
| PS-2 | Position Risk Designation | Standard HR risk categorization |
| IR-1 | Incident Response Policy and Procedures | Policy documentation expected for any IR capability |
| IR-8 | Incident Response Plan | Assumed present if IR capability (3.6.1) is implemented |
| CP-1 through CP-10 | Contingency Planning suite | Business continuity is a standard business practice |

**Key insight**: NFO controls represent the "-1" policy and procedure controls across most families, plus foundational operational controls. While not scored in a CMMC assessment, their absence would undermine the assessed controls. Assessors may note systemic weaknesses if NFO controls are clearly absent.

## CMMC Level 3 -- NIST 800-172 Additions

Level 3 adds 24 selected enhanced security requirements from NIST SP 800-172 to the 110 Level 2 requirements. These address advanced persistent threat (APT) scenarios for critical defense programs.

| 800-172 Requirement Area | Key Enhanced Controls | 800-53 Lineage |
|--------------------------|----------------------|----------------|
| Access Control | Dual authorization for critical operations, access control for mobile devices in processing facilities | AC-2(6), AC-19(4) |
| Awareness and Training | Practical exercises in training (simulated attacks) | AT-2(1), AT-3(3) |
| Audit and Accountability | Audit review to detect APT indicators, cross-organizational log sharing | AU-6(5), AU-6(6) |
| Configuration Management | Automated configuration monitoring, authorize/restrict/disable components by location | CM-3(4), CM-7(6) |
| Identification and Authentication | Hardware token-based or biometric authentication, network access to non-privileged accounts restricted | IA-2(6), IA-2(12) |
| Incident Response | Automated incident handling, security operations center capability | IR-4(1), IR-4(4) |
| Risk Assessment | Threat hunting, advanced analytics for threat detection | RA-3(1), RA-5(4) |
| Security Assessment | Penetration testing (red team exercises), independent assessors | CA-8, CA-2(1) |
| System and Communications Protection | Network segmentation/microsegmentation, hardware-enforced isolation | SC-7(21), SC-7(29) |
| System and Information Integrity | Automated response to integrity violations, behavior-based malicious code analysis | SI-3(7), SI-4(10) |

## FAR 52.204-21 to NIST 800-53 -- CMMC Level 1 (17 Practices)

The 17 Level 1 practices derive from FAR 52.204-21 "Basic Safeguarding of Covered Contractor Information Systems" (15 FAR safeguarding requirements mapped to 17 NIST 800-171 practices per 32 CFR Part 170 Table 1). These are a subset of the 110 Level 2 requirements.

| CMMC Practice | FAR 52.204-21 Requirement | 800-171 Req | 800-53 Control(s) |
|---------------|---------------------------|-------------|-------------------|
| L1-3.1.1 | Limit information system access to authorized users | 3.1.1 | AC-2, AC-3, AC-17 |
| L1-3.1.2 | Limit system access to types of transactions and functions authorized users are permitted to execute | 3.1.2 | AC-2, AC-3, AC-17 |
| L1-3.1.20 | Verify and control/limit connections to and use of external information systems | 3.1.20 | AC-20, AC-20(1) |
| L1-3.1.22 | Control information posted or processed on publicly accessible information systems | 3.1.22 | AC-22 |
| L1-3.5.1 | Identify information system users, processes acting on behalf of users, or devices | 3.5.1 | IA-2, IA-5 |
| L1-3.5.2 | Authenticate (or verify) the identities of those users, processes, or devices | 3.5.2 | IA-2, IA-5 |
| L1-3.8.3 | Sanitize or destroy information system media containing FCI before disposal or release for reuse | 3.8.3 | MP-6 |
| L1-3.10.1 | Limit physical access to organizational information systems, equipment, and the respective operating environments to authorized individuals | 3.10.1 | PE-2, PE-5 |
| L1-3.10.3 | Escort visitors and monitor visitor activity | 3.10.3 | PE-3 |
| L1-3.10.4 | Maintain audit logs of physical access | 3.10.4 | PE-3 |
| L1-3.10.5 | Control and manage physical access devices | 3.10.5 | PE-5 |
| L1-3.13.1 | Monitor, control, and protect organizational communications at the external boundaries and key internal boundaries of the information systems | 3.13.1 | SC-7 |
| L1-3.13.5 | Implement subnetworks for publicly accessible system components that are physically or logically separated from internal networks | 3.13.5 | SC-7(5) |
| L1-3.14.1 | Identify, report, and correct information and information system flaws in a timely manner | 3.14.1 | SI-2 |
| L1-3.14.2 | Provide protection from malicious code at appropriate locations within organizational information systems | 3.14.2 | SI-3 |
| L1-3.14.4 | Update malicious code protection mechanisms when new releases are available | 3.14.4 | SI-3 |
| L1-3.14.5 | Perform periodic scans of the information system and real-time scans of files from external sources as files are downloaded, opened, or executed | 3.14.5 | SI-3 |

## Cross-Reference: Overlapping Compliance

Organizations that achieve FedRAMP Moderate authorization substantially satisfy CMMC Level 2 requirements because both derive from the NIST 800-53 Moderate baseline. Key differences:

| Aspect | FedRAMP Moderate | CMMC Level 2 |
|--------|-----------------|--------------|
| **Control set** | Full 800-53 Moderate (~304 controls incl. enhancements) | 800-171 subset (110 requirements) |
| **Scope** | Federal data in cloud systems | CUI in contractor systems |
| **Assessment** | 3PAO assessment | C3PAO assessment |
| **Continuous monitoring** | Monthly/annual ConMon deliverables | Annual affirmation |
| **Gap for CMMC from FedRAMP** | Minimal -- FedRAMP covers all 800-53 controls underlying 800-171 | Scoping and documentation differences |
| **Gap for FedRAMP from CMMC** | Significant -- CMMC does not cover ~213 additional 800-53 Moderate controls | Full 800-53 implementation required |
