# Internal Audit Program

## Overview

An internal audit program provides independent, objective assurance that an organization's information security controls are designed and operating effectively. Internal audits are required by multiple frameworks including ISO 27001 (Clause 9.2), NIST SP 800-53 (CA-2, CA-7), SOC 2 (CC4.1), and PCI DSS (Req 12.4). A well-structured internal audit program supports external audit readiness, drives continuous improvement, and provides management with visibility into the organization's risk posture.

## Purpose and Authority

### Purpose
- Evaluate the effectiveness of controls, policies, and procedures
- Identify deficiencies and recommend improvements
- Verify compliance with internal policies and external requirements
- Support management decision-making with objective evidence
- Prepare the organization for external audits and assessments

### Framework Requirements

| Framework | Requirement | Reference |
|-----------|------------|-----------|
| ISO 27001 | Conduct internal audits at planned intervals | Clause 9.2 |
| NIST 800-53 | Assess security controls periodically | CA-2 (Assessments), CA-7 (Continuous Monitoring) |
| SOC 2 | Select, develop, and perform ongoing evaluations | CC4.1 |
| PCI DSS | Perform reviews at least once every 12 months | Req 12.4 |
| FedRAMP | Annual assessment of a subset of controls | Continuous Monitoring Strategy Guide |

### Internal Audit Charter
The charter is the foundational document establishing:
- Authority and organizational placement of the internal audit function
- Scope of audit activities
- Reporting lines (ideally to executive management or board/audit committee)
- Independence and objectivity requirements
- Access rights to systems, records, and personnel
- Responsibility for follow-up and remediation tracking

## Internal Audit Program Structure

### Components

| Component | Description |
|-----------|-------------|
| Charter | Authorizing document defining mandate and authority |
| Audit Universe | Complete inventory of auditable areas |
| Annual Plan | Risk-ranked schedule of audits for the year |
| Procedures | Standardized methodology and working paper templates |
| Reporting | Defined formats for findings, reports, and dashboards |
| Follow-up | Process for tracking remediation and verifying closure |

## Audit Universe and Risk-Based Prioritization

The audit universe is the complete inventory of auditable entities, processes, and controls:

- Information security policy domains (access control, cryptography, operations, etc.)
- Technology environments (cloud, on-premises, hybrid)
- Business processes that handle sensitive data
- Third-party and vendor relationships
- Regulatory and compliance obligations
- Previous audit findings and open items

### Risk-Based Prioritization

| Risk Factor | Consideration |
|-------------|---------------|
| Data sensitivity | Classification level of data processed |
| Regulatory requirements | Mandatory audit frequencies per framework |
| Prior findings | History of deficiencies and repeat findings |
| System criticality | Business impact of system failure |
| Change volume | Recent or significant system/process changes |
| Time since last audit | Ensure full coverage over the audit cycle |
| Threat landscape | Emerging threats relevant to the area |

## Audit Cycle Planning

- Annual audit plan should cover all ISMS requirements over a defined cycle (typically 1-3 years)
- ISO 27001 requires all clauses and Annex A controls to be audited within the cycle
- High-risk areas should be audited annually; lower-risk areas can be less frequent
- Plan should be flexible enough to accommodate unplanned audits triggered by incidents or changes
- Management approval of the audit plan should be documented

## Audit Execution

### Phase 1: Planning
- Define audit objectives and scope
- Identify applicable criteria (framework requirements, policies)
- Review prior audit findings and current risk context
- Develop audit program (procedures, test steps, evidence requests)
- Notify auditees and schedule interviews
- Prepare evidence request list

### Phase 2: Fieldwork
- Conduct opening meeting with auditees
- Execute audit procedures using defined testing methods
- Collect and evaluate evidence
- Document findings in working papers
- Conduct closing meeting to discuss preliminary findings

### Phase 3: Reporting
- Draft audit report with findings, risk ratings, and recommendations
- Share draft with auditees for factual accuracy review
- Obtain management responses and corrective action plans
- Finalize and distribute the audit report
- Present executive summary to leadership

### Phase 4: Follow-Up
- Track remediation progress against agreed timelines
- Verify effectiveness of corrective actions
- Retest controls where necessary
- Escalate overdue or inadequate responses
- Close findings when evidence of remediation is confirmed

## Sampling Methodologies

| Method | Description | Use Case |
|--------|-------------|----------|
| Statistical | Random sampling with mathematically determined sample size | Large populations with uniform characteristics |
| Judgmental | Auditor selects samples based on risk and experience | Targeted testing of high-risk items |
| Attribute | Tests for presence/absence of a specific attribute | Access reviews, approval checks |
| Discovery | Designed to detect at least one occurrence of a condition | Fraud detection, policy violations |

### Sample Size Guidance

| Population Size | Suggested Minimum Sample (Attribute) |
|-----------------|--------------------------------------|
| 1-5 | All items |
| 6-50 | 5-10 items |
| 51-250 | 10-25 items |
| 251-1000 | 25-40 items |
| 1000+ | 40-60 items (or statistically calculated) |

Sample sizes should be adjusted based on risk level, control criticality, and confidence requirements.

## Testing Types

| Type | Description | Examples |
|------|-------------|---------|
| Inquiry | Asking personnel about processes and controls | Interviews, questionnaires |
| Observation | Watching a process being performed | Observing access review meetings, backup procedures |
| Inspection | Examining records, documents, and configurations | Reviewing policies, screenshots, system configs |
| Reperformance | Independently executing a control to verify results | Re-running access reviews, recalculating metrics |

## Working Papers and Documentation

Working papers must:
- Clearly state the audit objective and scope
- Document the procedures performed
- Record evidence obtained (or reference to evidence repository)
- Support the auditor's conclusions
- Be reviewed and approved by the audit lead
- Be retained per the organization's record retention policy

### Working Paper Contents
- Audit program with completed test steps
- Evidence collected (screenshots, exports, documents)
- Interview notes with interviewee identification
- Sample selection methodology and rationale
- Test results and exceptions identified
- Cross-references to findings

## Finding Classification

| Classification | Definition | Response Timeline |
|---------------|-----------|-------------------|
| Critical | Fundamental control failure with immediate risk of significant harm | Immediate corrective action (within 30 days) |
| Major | Significant control weakness that could lead to material impact | Corrective action within 60-90 days |
| Minor | Limited control weakness with low probability of significant impact | Corrective action within 90-180 days |
| Observation | Opportunity for improvement; no compliance failure | Tracked for consideration; no mandatory action |

## Audit Report Structure

| Section | Content |
|---------|---------|
| Executive Summary | High-level overview, overall assessment, key findings |
| Scope and Objectives | What was audited, criteria used, period covered |
| Methodology | Testing approach, sampling methods, limitations |
| Findings and Recommendations | Detailed findings with risk ratings and recommended actions |
| Management Response | Auditee's response, corrective action plan, target dates |
| Appendices | Evidence references, distribution list, glossary |

## Management Response and Corrective Action Plans

- Management must respond to each finding with:
  - Agreement or disagreement (with justification if disagreeing)
  - Root cause analysis
  - Corrective action plan with specific steps
  - Responsible owner
  - Target completion date
- Responses should be documented within 2-4 weeks of report issuance
- Disagreements should be escalated to appropriate management level

## Follow-Up and Verification

- Maintain a centralized finding tracker (spreadsheet, GRC tool, or ticketing system)
- Conduct follow-up reviews at defined intervals (30, 60, 90 days)
- Request evidence of corrective action completion
- Retest controls to confirm effective remediation
- Escalate overdue items to senior management
- Report remediation status in regular management reports

## Internal Auditor Independence and Competence

### Independence
- Auditors must not audit their own work or areas of responsibility
- Organizational placement should ensure objectivity (report to CISO, CRO, or audit committee)
- In small organizations, cross-functional auditing or outsourced/co-sourced models can provide independence
- Independence must be documented and attested

### Competence
- Auditors should have training in audit methodology (ISO 19011 or IIA standards)
- Technical competence in the areas being audited
- Knowledge of applicable frameworks and standards
- Continuing education to maintain skills
- Relevant certifications (CISA, ISO 27001 Lead Auditor, CIA)

## Relationship to External Audits

- Internal audit results are reviewed by external auditors (3PAOs, SOC 2 auditors, CBs)
- Strong internal audit programs can reduce external audit scope and cost
- External auditors assess the quality and coverage of the internal audit program
- Internal audits should not duplicate external audit testing but should complement it
- Findings from external audits should be incorporated into internal audit planning

## Metrics and Reporting

| Metric | Purpose |
|--------|---------|
| Findings open vs closed | Track remediation progress |
| Findings by severity | Identify risk trends |
| Audit coverage percentage | Ensure all areas audited per cycle |
| Overdue corrective actions | Highlight remediation delays |
| Average time to remediate | Measure organizational responsiveness |
| Repeat findings | Identify systemic issues |
| Audit plan completion rate | Measure program execution |

## Key References

- ISO 19011:2018 — Guidelines for auditing management systems
- ISO/IEC 27001:2022 Clause 9.2 — Internal audit
- NIST SP 800-53A Rev 5 — Assessing Security and Privacy Controls
- IIA International Standards for the Professional Practice of Internal Auditing
- ISACA IT Audit Framework (ITAF)
