# ISO 27001 Certification Process

## Overview

ISO/IEC 27001 is an international standard for information security management systems (ISMS). Certification is granted by an accredited Certification Body (CB) after a successful two-stage audit. Certificates are valid for three years, with annual surveillance audits and a full recertification audit in Year 3. The current version is ISO/IEC 27001:2022.

## Certification Body (CB) Selection

### Accreditation Requirements
- CBs must be accredited by a national accreditation body (e.g., UKAS, ANAB, DAkkS)
- Accreditation is under ISO/IEC 17021-1 and ISO/IEC 27006
- Look for the IAF (International Accreditation Forum) MLA signatory mark
- Certificates from non-accredited CBs may not be recognized internationally

### Selection Criteria
- Accreditation status and scope
- Industry experience and sector-specific expertise
- Auditor availability and language capabilities
- Geographic coverage (important for multi-site certifications)
- Pricing structure and transparency
- Reputation and recognition by customers and regulators
- Integrated audit capability (if pursuing multiple ISO standards)

## Pre-Certification Activities

### Gap Assessment
- Compare current security posture against ISO 27001 requirements
- Identify missing or inadequate controls, policies, and processes
- Produce a remediation plan with priorities and timelines
- Typically performed 6-12 months before the certification audit

### ISMS Implementation
- Establish the ISMS scope and boundaries
- Develop the information security policy and objectives
- Conduct a risk assessment using a defined methodology (ISO 27005 or equivalent)
- Produce the Statement of Applicability (SoA) with justification for included/excluded controls
- Implement controls from Annex A (or alternative control sets)
- Develop required documented information (policies, procedures, records)
- Train staff on ISMS requirements and their roles

### Internal Audit (Clause 9.2)
- Must cover all ISMS requirements and applicable Annex A controls
- Internal auditors must be independent of the activities being audited
- Produce an internal audit report with findings and nonconformities
- Must be completed before the certification audit

### Management Review (Clause 9.3)
- Top management must review the ISMS at planned intervals
- Inputs: audit results, interested party feedback, risk assessment status, improvement opportunities
- Outputs: decisions on improvement, resource needs, changes to the ISMS
- Must be documented with meeting minutes and action items

## Stage 1 Audit

### Purpose
- Confirm readiness for Stage 2
- Review ISMS documentation
- Confirm scope and boundaries
- Identify any issues that could prevent Stage 2 success

### Required Documents for Stage 1

| Document | ISO 27001 Reference |
|----------|-------------------|
| ISMS Scope Statement | Clause 4.3 |
| Information Security Policy | Clause 5.2 |
| Risk Assessment Methodology | Clause 6.1.2 |
| Risk Assessment Results | Clause 6.1.2 |
| Risk Treatment Plan | Clause 6.1.3 |
| Statement of Applicability (SoA) | Clause 6.1.3 d) |
| Information Security Objectives | Clause 6.2 |
| Evidence of Competence | Clause 7.2 |
| Documented Operational Procedures | Clause 8.1 |
| Internal Audit Results | Clause 9.2 |
| Management Review Minutes | Clause 9.3 |

### Stage 1 Output
- Written report with findings and observations
- Recommendation on readiness for Stage 2
- Identification of areas of concern or potential nonconformities
- Agreement on Stage 2 schedule (typically 1-3 months after Stage 1)

## Stage 2 Audit

### Purpose
- Evaluate the implementation and effectiveness of the ISMS
- Confirm that controls are operating as described
- Determine conformity with ISO 27001 requirements

### Execution
- Conducted on-site and/or remotely (hybrid approach common post-2020)
- Duration based on organization size, scope complexity, and number of sites
- Typical duration: 5-15 auditor-days for medium organizations

### Sampling Methodology
- Auditors select a representative sample of controls, processes, and locations
- Sample size considers risk, control complexity, and prior audit results
- High-risk areas receive more thorough examination
- Auditors may expand sampling if issues are found

### Evidence Requirements by Clause

| Clause | Evidence Types |
|--------|---------------|
| Clause 4 (Context) | Interested party analysis, scope documentation |
| Clause 5 (Leadership) | Policy approvals, management commitment evidence, role assignments |
| Clause 6 (Planning) | Risk register, risk treatment plan, SoA, objectives and plans |
| Clause 7 (Support) | Training records, competence evidence, communication records |
| Clause 8 (Operation) | Operational procedures, risk assessment execution, change records |
| Clause 9 (Performance) | Monitoring results, internal audit reports, management review minutes |
| Clause 10 (Improvement) | Nonconformity records, corrective actions, improvement evidence |

### Evidence for Annex A Controls (2022 — 93 Controls)

| Control Theme | Example Evidence |
|---------------|-----------------|
| Organizational (37 controls) | Policies, roles, agreements, threat intelligence, asset inventory |
| People (8 controls) | Screening records, training, awareness, disciplinary process |
| Physical (14 controls) | Physical access logs, CCTV, environmental controls, secure disposal |
| Technological (34 controls) | Endpoint configs, access logs, encryption, backup, SIEM, vulnerability scans |

### Nonconformities

| Type | Definition | Impact on Certification |
|------|-----------|------------------------|
| Major | Absence or complete failure of a required process or control; systemic issue | Blocks certification until resolved and verified |
| Minor | Isolated lapse or partial implementation; does not undermine the ISMS | Can certify with an accepted Corrective Action Plan (CAP) |
| Observation | Opportunity for improvement; not a nonconformity | Noted in report; no action required for certification |

### Corrective Action Requirements
- Organization must perform root cause analysis for each nonconformity
- Corrective action must address the root cause, not just the symptom
- Major nonconformities require evidence of correction before certification (follow-up audit)
- Minor nonconformities: CAP accepted at Stage 2; evidence reviewed at next surveillance
- Typical timeline for major NC resolution: 90 days maximum

## Certification Decision

- Lead auditor makes recommendation to the CB's certification decision committee
- Decision committee is independent of the audit team
- Committee reviews audit report, nonconformities, and corrective actions
- Decision: Certify, conditionally certify (pending NC closure), or deny
- Certificate issued with defined scope, locations, and version of the standard
- Certificate validity: 3 years from date of issue

## Surveillance Audits

### Year 1 and Year 2 Surveillance

| Attribute | Details |
|-----------|---------|
| Frequency | Annual (approximately 12 months after certification and Stage 2 respectively) |
| Scope | Partial — selected clauses and Annex A controls |
| Duration | Typically 40-60% of Stage 2 duration |
| Mandatory elements | Clause 9.2 (internal audit), Clause 9.3 (management review), Clause 10 (improvement) |
| Focus areas | Previous nonconformities, changes to the ISMS, high-risk areas |

### Surveillance Requirements
- All clauses and controls must be covered across the two surveillance audits
- CB may adjust scope based on risk and findings
- Failure to schedule surveillance within the required window may result in suspension
- New major nonconformities must be resolved before the next surveillance

## Recertification Audit (Year 3)

- Full reassessment of the entire ISMS scope
- Includes both Stage 1 and Stage 2 components (may be combined)
- Must be completed before the certificate expires
- Reviews the ISMS effectiveness over the full certification cycle
- New certificate issued for another 3-year cycle
- Typically 80-100% of the original Stage 2 effort

## Transition from ISO 27001:2013 to 2022

| Aspect | Requirement |
|--------|-------------|
| Transition deadline | October 31, 2025 (all certificates must be transitioned) |
| Key changes | Annex A restructured from 114 controls (14 domains) to 93 controls (4 themes) |
| New controls | 11 new controls including threat intelligence, cloud security, data masking, monitoring |
| SoA update | Must be revised to reflect new Annex A structure |
| Transition audit | Can be combined with surveillance or recertification |
| Risk assessment | Must be reviewed against updated control set |

## Multi-Site Certification

- A single certificate can cover multiple locations under a centralized ISMS
- Central function must manage the ISMS across all sites
- Sampling of sites: auditors visit a representative subset each audit cycle
- Sample size: square root of the number of sites (rounded up), with risk-based adjustments
- All sites must be visited within the 3-year certification cycle
- Non-permanent sites (e.g., remote workers) handled through central management controls

## Integrated Audits

ISO 27001 can be audited alongside other management system standards:

| Standard | Integration Benefit |
|----------|-------------------|
| ISO 9001 (Quality) | Shared document control, management review, internal audit processes |
| ISO 22301 (Business Continuity) | Aligned risk assessment, shared BIA and recovery processes |
| ISO 27701 (Privacy) | Extension of ISMS to cover PIMS (privacy information management) |
| ISO 20000-1 (IT Service Management) | Aligned change management, incident management |

Benefits: reduced audit days, lower costs, streamlined management system, single integrated audit report.

## Common Nonconformities and Prevention

| Common Nonconformity | Prevention |
|---------------------|------------|
| Risk assessment not covering all assets in scope | Maintain complete asset inventory linked to risk register |
| SoA justifications missing or inadequate | Document clear rationale for each included/excluded control |
| Internal audit not covering all ISMS requirements | Create audit program covering all clauses and controls over the cycle |
| Management review missing required inputs/outputs | Use Clause 9.3 as a checklist for agenda items |
| Lack of evidence for Clause 7.2 competence | Maintain training records, certifications, and competence evaluations |
| Objectives not measurable | Define SMART objectives with clear metrics and targets |
| Corrective actions not addressing root cause | Use structured root cause analysis (5 Whys, fishbone) |
| Documented information not controlled | Implement document management with version control and approvals |

## Key References

- ISO/IEC 27001:2022 — Information security management systems — Requirements
- ISO/IEC 27002:2022 — Information security controls — Guidance
- ISO/IEC 27006-1:2024 — Requirements for audit and certification bodies
- ISO 19011:2018 — Guidelines for auditing management systems
- IAF MD 4:2018 — Use of ICT for auditing purposes
