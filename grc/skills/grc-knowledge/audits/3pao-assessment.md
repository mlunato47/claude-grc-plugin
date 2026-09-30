# 3PAO Assessment for FedRAMP

> **CR26 note (updated Sept 30, 2026):** this file describes the legacy Rev5 assessment model. Under the FedRAMP Consolidated Rules for 2026 (CR26; effective July 4, 2026, enforced Jan 1, 2027), "3PAO" is retired in favor of **FedRAMP Recognized independent assessor**, governed by the REC ruleset (in force July 4, 2026): A2LA accreditation (REC-IAS-ACC), a favorable full A2LA reassessment at least every 2 years (REC-IAS-RAS), at least 2 Class B/C/D assessments every 2 years (REC-IAS-ADA), and no restoration after two revocations (REC-FRP-DRD). Annual assessment moves to the IVV ruleset and significant changes to the SCN ruleset (see notes below). This guidance remains valid for Rev5 engagements through the transition (FedRAMP stops accepting new Rev5 certifications June 11, 2027; Rev5 certifications valid through at least Dec 31, 2028). See `frameworks/fedramp-20x.md`.

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
- Must disclose any conflicts of interest to FedRAMP
- Assessment team members must sign independence attestations

## Assessment Types

| Type | Trigger | Scope | Frequency |
|------|---------|-------|-----------|
| Initial Assessment | New authorization | Full baseline | Once |
| Annual Assessment | Ongoing authorization | Full baseline subset + all prior findings (legacy Rev5; see CR26 IVV note below) | Yearly |
| Significant Change Assessment | Major system change | Changed components and affected controls (legacy Rev5 SCR; CR26 SCN model below) | As needed |

### Initial Assessment
- Covers the complete FedRAMP baseline (Low, Moderate, or High)
- Full testing of all applicable controls
- Results in the initial SAR submitted with the authorization package

### Annual Assessment
- Tests a subset of controls per the FedRAMP annual assessment guidance (legacy Rev5: typically one-third of controls per year)
- Must ensure full baseline coverage over the three-year authorization cycle
- Includes validation of POA&M remediation
- Reviews continuous monitoring artifacts from the past year
- **CR26 (IVV ruleset):** a fixed core set of roughly 80 Rev5 controls is assessed every year (IVV-CSF-AIA); all applicable controls at least every 3 years is a ceiling, not a floor (IVV-CSF-MCA); FedRAMP's preferred approach is all controls annually (IVV-CSF-PCA); controls with negative findings are reassessed the next cycle. For 20x Class B/C/D, all KSIs are assessed annually (IVV-CSX-AIA).

### Significant Change Assessment
- Triggered by changes to the authorization boundary, data flows, or architecture
- Scope limited to affected controls and components
- Legacy Rev5: must be completed before the change is implemented in production (or within a FedRAMP-approved timeframe under the Significant Change Request process)
- **CR26 (SCN ruleset, Rev5 grace to June 1, 2027):** notification replaces advance approval. Routine recurring changes need no notification; adaptive changes are notified within 10 business days after completion; transformative changes require initial plans 30 business days before, final plans 10 business days before, notice 5 business days after completion and 5 business days after verification, with documentation updated within 30 business days. Advance approval applies only under a Corrective Action Plan.

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
- Penetration testing (network, web application, social engineering) — legacy Rev5: annual, per FedRAMP Penetration Test Guidance v3.0 (June 30, 2022, the last final version; v4.0 was only a March 2024 draft). CR26 CA-8 guidance: penetration testing is part of vulnerability detection and subject to the VDR rules
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

*Remediation days above are legacy FedRAMP Rev5 values (in force until CR26 becomes mandatory Jan 1, 2027): High 30 / Moderate 90 / Low 180 days from discovery. "Critical" is not a distinct FedRAMP category (treated as High). Under CR26 VDR/VER (required Dec 7, 2026; grace to Mar 7, 2027), deadlines derive from PAIN rating and reachability rather than severity alone.*

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
| FedRAMP | Completeness, quality, consistency | 2-6 weeks |
| JAB (historical; JAB path no longer exists) | Risk adjudication, authorization recommendation *(JAB dissolved May 2024; replaced by FedRAMP Board per M-24-15)* | 4-8 weeks |
| AO (if Agency path) | Risk acceptance determination | 2-4 weeks |

## Post-Assessment Activities

1. **CSP Response** — CSP reviews SAR, provides factual corrections and remediation plans
2. **POA&M Creation** — All open findings entered into POA&M with milestones and target dates
3. **Risk Adjudication** — AO (or formerly JAB, dissolved May 2024) reviews residual risk and makes authorization determination
4. **Remediation Validation** — 3PAO (CR26: FedRAMP Recognized independent assessor) validates closed findings (may require retesting)
5. **Authorization Decision** — ATO, DATO, or IATT issued (P-ATO was the JAB decision; historical). Under CR26 the outcome is "FedRAMP Certified" rather than "FedRAMP Authorized"

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

| Risk Level | FedRAMP Remediation Requirement (Legacy FedRAMP Rev5 value, in force until CR26 becomes mandatory Jan 1, 2027) |
|------------|--------------------------------|
| Critical | 30 days (or immediate mitigation) — not a distinct FedRAMP category; treated as High |
| High | 30 days |
| Moderate | 90 days |
| Low | 180 days |

**CR26 (VDR/VER rulesets, required Dec 7, 2026; grace to Mar 7, 2027):** remediation timeframes are set by PAIN rating and reachability (VDR-TFR-PVR; e.g., Class D PAIN-5 internet-reachable 12 hours, ranges up to 192 days), KEVs per CISA due dates (VDR-TFR-KEV). Anything not remediated within 192 days becomes an Accepted Vulnerability with written justification (VER-TFR-MAV) and is listed in each quarterly Ongoing Certification Report (OCR). The POA&M is not a CR26 construct on the CSP side.

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

- FedRAMP 3PAO Obligations and Performance Guide (legacy Rev5; CR26 REC ruleset governs assessor recognition)
- FedRAMP Penetration Test Guidance v3.0 (June 30, 2022; last final version)
- NIST SP 800-53A Rev 5 (Assessment Procedures)
- NIST SP 800-37 Rev 2 (Risk Management Framework)
- FedRAMP SAP Template
- FedRAMP SAR Template
- A2LA R311 (FedRAMP-specific accreditation requirements)
