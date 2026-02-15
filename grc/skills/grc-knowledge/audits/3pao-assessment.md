# 3PAO Assessment for FedRAMP

## Overview

A Third Party Assessment Organization (3PAO) performs independent security assessments of cloud service offerings (CSOs) seeking FedRAMP authorization. 3PAOs are accredited by the American Association for Laboratory Accreditation (A2LA) under ISO/IEC 17020:2012 and must meet FedRAMP-specific requirements for independence, competence, and quality management.

## 3PAO Role and Requirements

### Accreditation
- Must hold A2LA accreditation under ISO/IEC 17020 (Type A — independent)
- Subject to annual A2LA surveillance and biennial reassessment
- Must employ assessors with relevant certifications (CISSP, CISA, CEH, etc.)
- Required to maintain a quality management system
- Must demonstrate proficiency in NIST SP 800-53 control assessment

### Independence Requirements
- Organizational independence from the CSP being assessed
- No financial interest in the CSP beyond the assessment engagement
- Cannot have implemented controls they are now assessing
- Must disclose any conflicts of interest to the FedRAMP PMO
- Assessment team members must sign independence attestations

## Assessment Types

| Type | Trigger | Scope | Frequency |
|------|---------|-------|-----------|
| Initial Assessment | New authorization | Full baseline | Once |
| Annual Assessment | Ongoing authorization | Full baseline subset + all prior findings | Yearly |
| Significant Change Assessment | Major system change | Changed components and affected controls | As needed |

### Initial Assessment
- Covers the complete FedRAMP baseline (Low, Moderate, or High)
- Full testing of all applicable controls
- Results in the initial SAR submitted with the authorization package

### Annual Assessment
- Tests a subset of controls per the FedRAMP annual assessment guidance
- Must ensure full baseline coverage over the three-year authorization cycle
- Includes validation of POA&M remediation
- Reviews continuous monitoring artifacts from the past year

### Significant Change Assessment
- Triggered by changes to the authorization boundary, data flows, or architecture
- Scope limited to affected controls and components
- Must be completed before the change is implemented in production (or within a PMO-approved timeframe)

## Assessment Phases

### Phase 1: Planning

#### Security Assessment Plan (SAP)
The SAP defines the assessment scope, methodology, and logistics:

| SAP Element | Description |
|-------------|-------------|
| Scope | Systems, components, and controls to be assessed |
| Methodology | Testing approach per control family |
| Rules of Engagement (ROE) | Authorized testing activities, boundaries, escalation procedures |
| Schedule | Timeline for each assessment activity |
| Sampling | Sample sizes for user populations, devices, configurations |
| Resources | Assessment team members and their roles |
| Communication Plan | Points of contact, status reporting frequency |

#### Sampling Methodology
- User account samples: statistically significant sample based on population size per NIST 800-53A guidance
- Configuration checks: representative sample across OS types, device classes
- Vulnerability scanning: 100% of IP-addressable assets in the boundary
- Penetration testing: critical attack vectors based on threat model
- Document review: all required policies and procedures (no sampling)

### Phase 2: Execution

#### Document Review
- System Security Plan (SSP) completeness and accuracy
- Policies and procedures for each control family
- Configuration management documentation
- Incident response plans and test results
- Contingency plan and test results
- POA&M currency and accuracy

#### Interviews
- System administrators and engineers
- Security personnel (ISSO, ISSM)
- Management (system owner, AO representative)
- Development and operations staff
- Help desk and user support personnel

#### Testing Methods by Control Type

| Control Type | Testing Methods |
|--------------|----------------|
| Management | Document review, interviews, process walkthroughs |
| Operational | Observation, interviews, artifact inspection, process testing |
| Technical | Automated scanning, manual testing, configuration review, log analysis |

#### Automated Testing
- Vulnerability scanning (Nessus, Qualys, or equivalent)
- SCAP/STIG compliance scanning
- Web application scanning (OWASP ZAP, Burp Suite, or equivalent)
- Database scanning
- Container image scanning (if applicable)

#### Manual Testing
- Penetration testing (network, web application, social engineering)
- Access control verification
- Audit log review
- Encryption validation
- Physical security inspection (if applicable)
- Wireless security testing

### Phase 3: Reporting

#### Security Assessment Report (SAR)

The SAR documents all assessment findings and is a required component of the authorization package.

**SAR Structure:**
1. Executive Summary
2. Assessment Scope and Methodology
3. System Overview
4. Risk Exposure Table
5. Detailed Findings
6. Appendices (scan results, test evidence, sampling details)

#### Risk Exposure Table

The risk exposure table summarizes all findings with severity and risk ratings:

| Finding ID | Control | Vulnerability | Likelihood | Impact | Risk Level | Status |
|-----------|---------|---------------|------------|--------|------------|--------|
| FIND-001 | AC-2 | Inactive accounts not disabled | High | Moderate | High | Open |
| FIND-002 | SC-7 | Missing boundary protection | High | High | Critical | Open |

## Finding Severity Classification

| Severity | Definition | Impact on Authorization |
|----------|------------|------------------------|
| Critical | Exploitation would cause catastrophic harm; no compensating controls | Likely DATO; must remediate before ATO |
| High | Exploitation would cause serious harm; limited compensating controls | May block ATO; requires remediation plan |
| Moderate | Exploitation could cause moderate harm; some compensating controls exist | ATO possible with POA&M; 90-day remediation |
| Low | Exploitation would cause limited harm; compensating controls in place | ATO possible with POA&M; 180-day remediation |

## Risk Calculation Methodology

Risk is calculated as **Likelihood x Impact**:

### Likelihood Scale

| Level | Description |
|-------|-------------|
| Very High | Almost certain to be exploited; actively exploited in the wild |
| High | Likely to be exploited; exploit code publicly available |
| Moderate | Possible exploitation; requires moderate skill |
| Low | Unlikely exploitation; requires significant skill and access |
| Very Low | Highly unlikely; requires insider access and advanced capability |

### Impact Scale

| Level | Description |
|-------|-------------|
| Very High | Complete system compromise; loss of all CIA for federal data |
| High | Major compromise; significant loss of confidentiality or availability |
| Moderate | Partial compromise; limited data exposure or service disruption |
| Low | Minor impact; minimal data exposure, no service disruption |
| Very Low | Negligible impact; informational finding only |

## Evidence Collection Requirements

- All evidence must be dated within the assessment period
- Screenshots must include timestamps and system identification
- Automated scan results must include raw output files
- Interview notes must identify the interviewee by role
- Configuration samples must identify the specific system and component
- Evidence must be stored securely and retained per FedRAMP requirements
- Chain of custody must be maintained for all evidence artifacts

## Common High-Failure Controls

| Control | Common Finding | Root Cause |
|---------|---------------|------------|
| AC-2 | Account management deficiencies | Lack of automated provisioning/deprovisioning |
| AU-6 | Insufficient log review | No SIEM or alert correlation |
| CM-6 | Configuration deviations | Inconsistent hardening across environments |
| IA-5 | Weak authenticator management | Password policy gaps, no MFA |
| RA-5 | Incomplete vulnerability scanning | Assets outside scan scope |
| SC-7 | Boundary protection gaps | Overly permissive firewall rules |
| SI-2 | Untimely flaw remediation | No patch management process |
| CP-10 | Untested recovery capabilities | DR/BCP tests not conducted |

## SAR Review Process

| Reviewer | Focus | Timeline |
|----------|-------|----------|
| CSP | Accuracy of findings, factual corrections | 2-4 weeks |
| FedRAMP PMO | Completeness, quality, consistency | 2-6 weeks |
| JAB (if JAB path) | Risk adjudication, authorization recommendation | 4-8 weeks | *(Note: JAB dissolved May 2024; replaced by FedRAMP Board)* |
| AO (if Agency path) | Risk acceptance determination | 2-4 weeks |

## Post-Assessment Activities

1. **CSP Response** — CSP reviews SAR, provides factual corrections and remediation plans
2. **POA&M Creation** — All open findings entered into POA&M with milestones and target dates
3. **Risk Adjudication** — AO (or formerly JAB, dissolved May 2024) reviews residual risk and makes authorization determination
4. **Remediation Validation** — 3PAO validates closed findings (may require retesting)
5. **Authorization Decision** — ATO, P-ATO, DATO, or IATT issued

## Remediation and POA&M Entry

Each SAR finding must be tracked in the POA&M with:
- Unique identifier mapped to SAR finding ID
- Affected control(s)
- Description of weakness
- Risk level (from SAR)
- Remediation plan with specific milestones
- Scheduled completion date
- Resources required
- Status and progress updates

### Remediation Timelines

| Risk Level | FedRAMP Remediation Requirement |
|------------|--------------------------------|
| Critical | 30 days (or immediate mitigation) |
| High | 30 days |
| Moderate | 90 days |
| Low | 180 days |

## Assessment Timelines

### Initial Assessment (Moderate Baseline)

| Phase | Duration |
|-------|----------|
| SAP Development and Approval | 2-4 weeks |
| Document Review | 2-3 weeks |
| On-site/Remote Testing | 2-4 weeks |
| Penetration Testing | 1-2 weeks |
| SAR Drafting | 2-4 weeks |
| CSP Review and Response | 2-4 weeks |
| SAR Finalization | 1-2 weeks |
| **Total** | **12-23 weeks** |

### Annual Assessment

| Phase | Duration |
|-------|----------|
| SAP Update and Approval | 1-2 weeks |
| Testing and Evidence Review | 2-3 weeks |
| SAR Update | 1-2 weeks |
| CSP Review | 1-2 weeks |
| **Total** | **5-9 weeks** |

## Key References

- FedRAMP 3PAO Obligations and Performance Guide
- NIST SP 800-53A Rev 5 (Assessment Procedures)
- NIST SP 800-37 Rev 2 (Risk Management Framework)
- FedRAMP SAP Template
- FedRAMP SAR Template
- A2LA R311 (FedRAMP-specific accreditation requirements)
