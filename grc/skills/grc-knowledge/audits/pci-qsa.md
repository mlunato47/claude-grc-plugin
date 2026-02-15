# PCI DSS QSA Assessment

## Overview

A Qualified Security Assessor (QSA) performs on-site assessments of entities that store, process, or transmit cardholder data to validate compliance with the Payment Card Industry Data Security Standard (PCI DSS). The current version is PCI DSS v4.0.1. QSA companies are qualified and trained by the PCI Security Standards Council (PCI SSC).

## QSA Role and Qualification

### QSA Company Requirements
- Must be qualified by the PCI SSC
- Subject to annual requalification
- Must maintain professional liability insurance
- Must employ QSA-qualified individuals (QSA employees)
- Must adhere to the PCI SSC Code of Professional Responsibility

### QSA Employee Requirements
- Must complete PCI SSC QSA training and pass the examination
- Annual requalification through continuing professional education
- Must hold one or more qualifying certifications (CISSP, CISA, CISM, ISO 27001 Lead Auditor, etc.)
- Must maintain independence from the entity being assessed
- Minimum years of information security experience

### Independence Requirements
- QSA must not have implemented or managed the controls being assessed
- Must disclose any relationships that could impair independence
- Cannot provide assessment services to entities where a conflict exists
- Cooling-off period applies for former employees of the assessed entity

## ISA (Internal Security Assessor) Alternative

- ISA is a PCI SSC-trained internal employee of the assessed organization
- Can perform internal assessments and complete the Report on Compliance (ROC)
- ISA training and qualification administered by PCI SSC
- Some acquirers and payment brands may still require external QSA validation
- Useful for large merchants and service providers with mature security programs
- ISA must maintain independence from the operational teams being assessed

## Assessment Scoping

### Cardholder Data Environment (CDE)
- All system components that store, process, or transmit cardholder data (CHD)
- All system components that store, process, or transmit sensitive authentication data (SAD)
- Includes people, processes, and technology within the CDE

### Scope Categories

| Category | Definition | PCI DSS Applicability |
|----------|-----------|----------------------|
| CDE Systems | Directly handle CHD/SAD | All requirements apply |
| Connected-to Systems | Have network connectivity to CDE systems | Applicable requirements based on connectivity |
| Security-Impacting Systems | Could affect the security of the CDE | Applicable requirements based on function |
| Out-of-Scope Systems | No connectivity to or impact on the CDE | Not assessed (must be validated as out-of-scope) |

### Network Segmentation Validation
- Segmentation is not a PCI DSS requirement but reduces scope
- If segmentation is used, its effectiveness must be validated
- Penetration testing must include segmentation controls
- Segmentation must be tested every 6 months (for service providers) or annually (for merchants)
- Inadequate segmentation can bring the entire network into scope

## ROC (Report on Compliance)

### Structure

| Section | Content |
|---------|---------|
| Executive Summary | Assessment overview, scope, findings summary |
| Scope of Assessment | CDE description, network diagrams, data flow diagrams, scope validation |
| Assessment Details | Findings for each PCI DSS requirement (1-12) |
| Compensating Controls | Worksheet for any compensating controls in use |
| Assessment Attestation | QSA company attestation of findings |

### Requirement Status Options

| Status | Definition |
|--------|-----------|
| In Place | Requirement is fully met |
| In Place with CCW | Met through a compensating control (documented in Compensating Controls Worksheet) |
| Not Applicable | Requirement does not apply (with justification) |
| Not Tested | Requirement was not evaluated (requires justification) |
| Not in Place | Requirement is not met |

## SAQ (Self-Assessment Questionnaire)

| SAQ Type | Applicable To | Approximate Questions |
|----------|--------------|----------------------|
| SAQ A | E-commerce merchants with fully outsourced payment page | ~30 |
| SAQ A-EP | E-commerce merchants with website affecting transaction security | ~140 |
| SAQ B | Merchants with imprint machines or standalone dial-out terminals only | ~40 |
| SAQ B-IP | Merchants with standalone PTS-approved payment terminals (IP connected) | ~80 |
| SAQ C | Merchants with payment application connected to the internet | ~130 |
| SAQ C-VT | Merchants with web-based virtual terminal (manual entry only) | ~70 |
| SAQ D (Merchant) | All other merchants | ~300+ |
| SAQ D (SP) | All service providers eligible for SAQ | ~300+ |
| SAQ P2PE | Merchants using validated P2PE solution | ~30 |

SAQ eligibility is determined by the merchant's payment processing environment and acquirer requirements.

## Assessment Process

### Phase 1: Scoping

1. Identify all locations and flows of cardholder data
2. Create or validate network diagrams and data flow diagrams
3. Identify all system components in the CDE
4. Classify connected-to and security-impacting systems
5. Validate network segmentation (if used)
6. Document the scope and get agreement from the assessed entity

### Phase 2: Evidence Collection

- Gather policies, procedures, and standards
- Collect system configurations and screenshots
- Obtain access to systems for testing (with proper authorization)
- Request population lists for sampling (users, devices, change records)
- Coordinate vulnerability scan and penetration test schedules

### Phase 3: Testing

- Test each applicable requirement using the defined testing procedures
- Conduct interviews with responsible personnel
- Inspect documentation and configurations
- Observe processes and controls in operation
- Review automated scan results and penetration test reports

### Phase 4: Reporting

- Document findings for each requirement in the ROC template
- Identify requirements that are Not in Place
- Document compensating controls where applicable
- Draft the ROC and supporting evidence
- Complete the Attestation of Compliance (AOC)

## Evidence Requirements by Requirement Group

| Requirement | Area | Key Evidence |
|-------------|------|-------------|
| Req 1 | Network Security Controls | Firewall configs, network diagrams, rule reviews, change records |
| Req 2 | Secure Configuration | Hardening standards, default password removal, system configs |
| Req 3 | Protect Stored Account Data | Data retention policies, encryption configs, key management procedures |
| Req 4 | Protect Data in Transit | TLS configurations, certificate management, transmission policies |
| Req 5 | Malware Protection | Anti-malware deployment, scan logs, update evidence |
| Req 6 | Secure Development | SDLC documentation, code reviews, vulnerability management, WAF configs |
| Req 7 | Restrict Access | Access control policies, RBAC configs, need-to-know documentation |
| Req 8 | Identify Users | Authentication configs, MFA evidence, password policies, shared account controls |
| Req 9 | Physical Access | Physical access logs, visitor logs, media handling, POS device inspection |
| Req 10 | Logging and Monitoring | Log configs, SIEM evidence, time synchronization, log retention |
| Req 11 | Security Testing | ASV scan results, internal scan results, penetration test reports, IDS/IPS configs |
| Req 12 | Security Policies | InfoSec policy, risk assessments, awareness training, incident response plan |

## Compensating Controls

### When Compensating Controls Apply
- An entity cannot meet a requirement as explicitly stated
- A legitimate technical or business constraint prevents direct compliance
- The entity has implemented alternative controls that mitigate the risk

### Compensating Controls Worksheet (CCW)

| Field | Description |
|-------|-------------|
| Requirement | The original PCI DSS requirement number |
| Constraint | Why the original requirement cannot be met |
| Objective | The intent of the original requirement |
| Compensating Control | Description of the alternative control(s) |
| Validation | How the QSA validated the compensating control |
| Risk Assessment | Analysis demonstrating equivalent risk mitigation |

### Compensating Control Requirements
- Must meet the intent and rigor of the original requirement
- Must provide a similar level of defense
- Must be above and beyond other PCI DSS requirements
- Must address the additional risk imposed by not adhering to the original requirement
- Must be re-evaluated annually

## Customized Approach (PCI DSS v4.0+)

### Overview
- Alternative to the defined (traditional) approach
- Allows entities to meet the objective of a requirement using different controls
- Requires a targeted risk analysis for each customized implementation
- QSA must perform more rigorous validation

### Requirements for Customized Approach

| Element | Description |
|---------|-------------|
| Objective Statement | The security objective defined in PCI DSS for the requirement |
| Controls Matrix | Entity's controls that meet the stated objective |
| Targeted Risk Analysis | Analysis demonstrating controls adequately address risk |
| Testing Procedures | QSA-developed procedures to validate the customized implementation |
| Evidence | Documentation supporting the customized approach |

### Customized Approach Limitations
- Not available for all requirements (some are mandatory as defined)
- Requires more effort from both the entity and QSA
- QSA must document the derivation of testing procedures
- May increase assessment cost and duration

## AOC (Attestation of Compliance)

### Merchant AOC
- Signed by the merchant's executive officer and the QSA
- Confirms assessment scope, methodology, and results
- Identifies any requirements not in place
- Must be submitted to the merchant's acquirer

### Service Provider AOC
- Signed by the service provider's executive officer and the QSA
- Includes the same elements as merchant AOC
- Must identify services covered and any excluded services
- Submitted to requesting entities and payment brands

## Common Assessment Findings

| Requirement | Common Finding |
|-------------|---------------|
| Req 2 | Default credentials not changed on network devices |
| Req 3 | PAN stored without business justification; inadequate key management |
| Req 6 | Missing security in SDLC; public-facing web apps not protected |
| Req 7 | Overly broad access privileges; lack of periodic review |
| Req 8 | MFA not implemented for all required access; shared accounts in use |
| Req 10 | Insufficient log retention; logs not monitored for suspicious activity |
| Req 11 | Missing quarterly ASV scans; penetration testing gaps |
| Req 12 | Outdated security policies; incomplete incident response testing |

## Remediation and Reassessment

- Findings of "Not in Place" must be remediated before compliance can be attested
- Remediated controls must be retested by the QSA
- If remediation occurs during the assessment period, the QSA can validate at that time
- Significant remediation may require a follow-up assessment
- Entities must submit updated AOC once all requirements are in place

## PCI Forensic Investigator (PFI)

- PFI-qualified companies investigate suspected or confirmed cardholder data breaches
- Engaged by payment brands or acquirers following a data breach
- Responsibilities include:
  - Determining the scope and cause of the breach
  - Identifying compromised data and affected accounts
  - Recommending containment and remediation actions
  - Producing a PFI Final Incident Report
- PFI engagement does not replace the regular QSA assessment
- Findings from PFI may trigger additional PCI DSS requirements or enhanced monitoring

## Timeline and Validation Cycle

### Annual Validation Cycle

| Activity | Frequency | Responsible Party |
|----------|-----------|------------------|
| ROC/SAQ submission | Annual | Merchant/SP with QSA/ISA |
| AOC submission | Annual (with ROC/SAQ) | Merchant/SP |
| ASV external vulnerability scans | Quarterly | Approved Scanning Vendor (ASV) |
| Internal vulnerability scans | Quarterly | Internal team or third party |
| Penetration testing | Annual (semi-annual for SP segmentation) | Qualified tester |
| Segmentation testing | Annual (merchants), Semi-annual (SPs) | QSA or qualified tester |
| Security awareness training | Annual (at hire and annually) | Internal team |

### Typical Assessment Timeline

| Phase | Duration |
|-------|----------|
| Scoping and planning | 2-4 weeks |
| Evidence collection | 2-6 weeks |
| On-site/remote testing | 2-4 weeks |
| Remediation (if needed) | 4-12 weeks |
| ROC drafting and review | 2-4 weeks |
| **Total** | **12-30 weeks** |

## Key References

- PCI DSS v4.0.1 (June 2024)
- PCI DSS ROC Reporting Template
- PCI DSS SAQ Documents (A through P2PE)
- PCI SSC Qualification Requirements for QSAs
- PCI DSS Scoping and Segmentation Guidance
- PCI DSS Customized Approach Guidance
