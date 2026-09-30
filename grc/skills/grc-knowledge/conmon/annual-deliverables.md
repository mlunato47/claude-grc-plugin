# Annual Continuous Monitoring Deliverables

> **CR26 note (updated Sept 30, 2026):** FedRAMP-specific annual-assessment framing below is the legacy Rev5 model. Under CR26, independent assessment expectations live in the IVV ruleset (required Jan 1, 2027): a fixed core set of ~80 Rev5 controls is assessed every year (IVV-CSF-AIA), every control at least every 3 years as a ceiling (IVV-CSF-MCA), all controls SHOULD be assessed annually (IVV-CSF-PCA), controls with negative findings are reassessed, and for 20x Class B/C/D all KSIs are assessed annually (IVV-CSX-AIA). CR26 also retires the term "3PAO" in favor of "FedRAMP Recognized independent assessor" (REC ruleset) — "3PAO" below is the legacy term. See `frameworks/fedramp-20x.md`.

## Overview

Annual deliverables complement monthly ConMon activities by providing deeper assessments, comprehensive testing, and programmatic reviews that are impractical to perform monthly. These activities ensure that the full control set is evaluated over time, contingency and incident response capabilities are validated, and organizational policies remain current. For FedRAMP systems, many annual deliverables are mandatory for maintaining authorization.

---

## Annual Security Assessment

### Purpose

Each year, a subset of security controls is assessed to ensure they remain effective. Under the legacy Rev5 model, over a three-year authorization cycle all controls should be assessed at least once, meaning approximately one-third of controls are assessed annually. **CR26 (IVV):** the three-year rotation is a ceiling, not a floor — a fixed core set of ~80 Rev5 controls is assessed every year (IVV-CSF-AIA), all controls at least every 3 years (IVV-CSF-MCA), and FedRAMP's preferred approach is all controls every year (IVV-CSF-PCA).

### Control Selection Methodology

Controls are selected for annual assessment based on:

| Selection Criteria | Description |
|-------------------|-------------|
| **Rotation schedule** | Controls not assessed in the prior two years are prioritized to ensure complete coverage over three years |
| **Risk-based prioritization** | Controls associated with higher risk or those that address known weaknesses are assessed more frequently |
| **Change-driven selection** | Controls affected by significant system changes since the last assessment |
| **AO-directed** | The Authorizing Official may request assessment of specific controls based on threat intelligence or organizational concerns |
| **Incident-driven** | Controls related to a recent security incident may be selected for reassessment |

FedRAMP provides a core set of controls that must be assessed annually regardless of rotation (under CR26, the fixed IVV-CSF-AIA list of ~80 controls). These typically include access control, audit, configuration management, incident response, and vulnerability management families.

### Assessment Scope and Sampling

- **Sampling methodology:** When a control applies to multiple system components, a representative sample may be assessed rather than every instance. Sampling must follow a documented methodology with sufficient coverage to provide confidence (e.g., NIST 800-53A guidance).
- **Assessment methods:** Interview, examine, and test (per NIST 800-53A). Automated testing preferred where possible.
- **Common controls:** Controls inherited from a shared or common control provider must be assessed by that provider. The inheriting system must verify the inheritance relationship remains valid.
- **Hybrid controls:** Both the common portion and the system-specific implementation must be assessed.

### SAR Update Process

Following the annual assessment:

1. The assessor produces findings for each assessed control (Satisfied or Other Than Satisfied)
2. New findings are documented with risk rating and recommended remediation
3. The Security Assessment Report (SAR) is updated to reflect current assessment results
4. New findings are added to the POA&M with appropriate severity and timelines
5. The updated SAR is submitted to the AO and (for FedRAMP) to the FedRAMP repository
6. Previous year findings are reconciled — verify closure or update status

---

## Contingency Plan Test

| Attribute | Requirement |
|-----------|------------|
| **Frequency** | Annually |
| **Governing control** | CP-4 (Contingency Plan Testing) |
| **Scope** | Full contingency plan or functional components (backup restoration, failover, communication procedures) |
| **Test types** | Tabletop exercise, functional test, full-scale exercise (type depends on system impact level) |
| **Documentation** | Test plan, test results, lessons learned, corrective actions |
| **Deliverable** | Contingency Plan Test Report |

The test must validate that:
- Backup and restoration procedures work as documented
- Recovery time objectives (RTO) and recovery point objectives (RPO) are achievable
- Personnel understand their roles and responsibilities
- Communication procedures function correctly
- Alternate processing sites (if applicable) can support operations

Lessons learned and corrective actions must be incorporated into an updated contingency plan.

---

## Incident Response Plan Test

| Attribute | Requirement |
|-----------|------------|
| **Frequency** | Annually |
| **Governing control** | IR-3 (Incident Response Testing) |
| **Scope** | Full incident response plan or specific incident scenarios |
| **Test types** | Tabletop exercise, simulation, or functional drill |
| **Documentation** | Test plan, scenario description, test results, lessons learned, corrective actions |
| **Deliverable** | Incident Response Test Report |

Testing should exercise:
- Incident detection and classification procedures
- Escalation and notification chains
- Evidence collection and preservation
- Containment and eradication procedures
- Recovery and post-incident review processes
- External reporting obligations (CISA, law enforcement, affected parties)

---

## Security Training Completion Records

| Attribute | Requirement |
|-----------|------------|
| **Frequency** | Annually (and upon hire, role change) |
| **Governing controls** | AT-2 (Literacy Training and Awareness), AT-3 (Role-Based Training) |
| **Scope** | All personnel with access to the information system |
| **Documentation** | Training completion records, training content/curriculum, attendance rosters |
| **Deliverable** | Training completion report showing percentage compliance |

Training must cover:
- General security awareness (phishing, password hygiene, social engineering, insider threats)
- Role-based training for privileged users, developers, administrators, and security personnel
- Privacy awareness training (if PII is processed)
- Specialized training for incident response, contingency operations, and security assessment personnel

---

## Penetration Test

| Attribute | Requirement |
|-----------|------------|
| **Frequency** | Annually (legacy Rev5; FedRAMP Penetration Test Guidance v3.0, June 30, 2022, is the last final version — v4.0 was only a March 2024 draft). CA-8 is in all FedRAMP baselines. CR26 CA-8 guidance: penetration testing is part of vulnerability detection and is subject to the VDR rules |
| **Governing control** | CA-8 (Penetration Testing) |
| **Scope** | External, internal, and (for High) social engineering |
| **Deliverable** | Penetration Test Report, Remediation Plan |

### Scope Details

| Test Component | Description |
|----------------|-------------|
| **External testing** | Attacks against internet-facing assets from outside the authorization boundary (web applications, APIs, network services) |
| **Internal testing** | Attacks simulating an insider threat or compromised internal host (lateral movement, privilege escalation, data exfiltration) |
| **Social engineering** | Phishing campaigns, pretexting, physical access attempts (required for FedRAMP High) |
| **Web application** | Manual and automated testing beyond automated scanning (business logic flaws, authentication bypass, authorization issues) |

### Rules of Engagement

The penetration test must be governed by a formal Rules of Engagement (ROE) document that specifies:

- Authorized testing targets (IP ranges, URLs, personnel for social engineering)
- Prohibited activities (denial of service, production data modification, testing of out-of-scope systems)
- Testing window (dates and times)
- Emergency contacts and stop conditions
- Data handling requirements for any sensitive data encountered
- Communication protocols during testing
- Legal authorization and liability

### Remediation of Findings

- All penetration test findings must be added to the POA&M with appropriate severity ratings
- High findings (including scanner-"Critical" — FedRAMP has no Critical category) follow the legacy FedRAMP Rev5 RA-5(d) timeline of 30 days from discovery (Moderate 90, Low 180); under CR26 the VDR/VER PAIN-and-reachability timeframes apply (12 hours to 192 days; Accepted Vulnerability at 192 days)
- Re-testing of remediated findings is recommended to verify effectiveness
- The penetration test report and remediation status must be submitted to the AO

---

## Privacy Impact Assessment Review

| Attribute | Requirement |
|-----------|------------|
| **Frequency** | Annually, or when system changes affect PII processing |
| **Governing controls** | RA-8 (Privacy Impact Assessments), PT family |
| **Scope** | All PII collection, processing, storage, and sharing activities |
| **Deliverable** | Updated Privacy Impact Assessment (PIA) or review memo confirming no changes |

The review must confirm:
- PII data types collected remain as documented
- Purpose of collection and use has not changed
- Data retention periods are being followed
- Privacy controls remain effective
- Third-party data sharing agreements are current

---

## Access Reviews and Recertification

| Attribute | Requirement |
|-----------|------------|
| **Frequency** | At least annually (quarterly for privileged accounts is recommended) |
| **Governing controls** | AC-2 (Account Management), PS-5 (Personnel Transfer) |
| **Scope** | All user accounts, service accounts, and privileged accounts |
| **Deliverable** | Access review report with recertification evidence |

The review must validate:
- All accounts are associated with active, authorized personnel
- Privilege levels are appropriate for current roles (least privilege)
- Shared and group accounts are documented and justified
- Service accounts have documented owners and appropriate restrictions
- Separated personnel have had access revoked
- Temporary and emergency accounts have been removed or disabled

---

## Policy and Procedure Reviews

| Attribute | Requirement |
|-----------|------------|
| **Frequency** | Annually (Legacy FedRAMP Rev5 value, in force until CR26 becomes mandatory Jan 1, 2027: policies reviewed every 3 years at Moderate / annually at High; procedures annually at both. CR26: no FedRAMP-assigned value) |
| **Governing controls** | All "-1" controls (e.g., AC-1, AU-1, CM-1) — Policy and Procedures |
| **Scope** | All security and privacy policies and procedures within the SSP |
| **Deliverable** | Updated policies with revision history, or review memo confirming no changes |

The review must assess:
- Alignment with current NIST 800-53 requirements and organizational directives
- Accuracy of roles, responsibilities, and contact information
- Consistency with actual operational practices
- Incorporation of lessons learned from incidents and assessments
- Currency of referenced standards, tools, and technologies

---

## Configuration Baseline Reviews

| Attribute | Requirement |
|-----------|------------|
| **Frequency** | Annually |
| **Governing controls** | CM-2 (Baseline Configuration), CM-6 (Configuration Settings) |
| **Scope** | Approved configuration baselines for all system component types |
| **Deliverable** | Updated baseline documentation, deviation justifications |

The review must evaluate:
- Whether baselines reflect current CIS Benchmark or DISA STIG versions
- Whether approved deviations remain justified and documented
- Whether new system component types have been added without baseline documentation
- Alignment between documented baselines and actual system configurations (informed by monthly compliance scans)

---

## Supply Chain Risk Reassessment

| Attribute | Requirement |
|-----------|------------|
| **Frequency** | Annually |
| **Governing controls** | SR-2 (Supply Chain Risk Management Plan), SR-3 (Supply Chain Controls and Processes) |
| **Scope** | All third-party vendors, service providers, and supply chain partners |
| **Deliverable** | Updated supply chain risk assessment, vendor inventory |

The reassessment must address:
- Changes in vendor risk profiles (financial stability, security incidents, acquisition)
- Currency of vendor security certifications (SOC 2, ISO 27001, FedRAMP)
- Compliance with contractual security requirements
- New vendors or services added during the year
- Discontinued vendor relationships and transition plans
- Software bill of materials (SBOM) updates for critical components

---

## Annual SAR and POA&M Reconciliation

At the end of each annual cycle, the SAR and POA&M must be fully reconciled:

1. **SAR reconciliation:** All findings from the annual assessment are reflected in the SAR with accurate status (open, closed, risk accepted)
2. **POA&M reconciliation:** Every open SAR finding has a corresponding POA&M entry; every closed POA&M item has verification evidence
3. **Cross-reference validation:** POA&M weakness IDs map to SAR finding IDs; no orphaned entries in either document
4. **Historical closure:** POA&M items marked Completed are verified through re-assessment or re-scanning and moved to Closed status
5. **Deviation reconciliation:** All active deviation requests are reviewed for continued validity
6. **Submission:** Reconciled SAR and POA&M are submitted to the AO and (for FedRAMP) to the FedRAMP repository

---

## Annual Deliverable Summary Calendar

| Deliverable | Typical Due Date | Responsible Party |
|------------|-----------------|-------------------|
| Annual security assessment (legacy 1/3 rotation; CR26 IVV: core set annually, all controls within 3 years) | Per assessment schedule (often Q4 or anniversary of ATO) | SCA / 3PAO (CR26: FedRAMP Recognized independent assessor) |
| Updated SAR | Within 30 days of assessment completion | SCA / 3PAO |
| Contingency plan test | Annually (coordinate with system owner) | ISSO / System Owner |
| Incident response plan test | Annually | ISSO / IR Team |
| Security training completion | By anniversary date or fiscal year end | ISSO / Training Coordinator |
| Penetration test | Annually (legacy Rev5; CA-8 is in all baselines; CR26: subject to VDR) | 3PAO (independent assessor) or authorized pen test team |
| Privacy impact assessment review | Annually or upon PII-related changes | Privacy Officer / ISSO |
| Access review and recertification | At least annually | ISSO / System Owner |
| Policy and procedure reviews | Annually | ISSO / System Owner |
| Configuration baseline reviews | Annually | ISSO / System Administrator |
| Supply chain risk reassessment | Annually | ISSO / Procurement |
| SAR and POA&M reconciliation | Annually (after assessment) | ISSO / SCA |

---

## References

- NIST SP 800-53 Rev. 5: CA-2, CA-5, CA-8, CP-4, IR-3, AT-2, AT-3, AC-2, CM-2, CM-6, SR-2
- NIST SP 800-53A Rev. 5: Assessing Security and Privacy Controls
- NIST SP 800-137: Information Security Continuous Monitoring
- FedRAMP Annual Assessment Guidance (legacy Rev5; CR26: IVV ruleset)
- FedRAMP Penetration Test Guidance v3.0 (June 30, 2022 — last final version; v4.0 March 2024 draft only)
- OMB Circular A-130
