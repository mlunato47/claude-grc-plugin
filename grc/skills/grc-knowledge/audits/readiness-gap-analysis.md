# Readiness and Gap Analysis Methodology

## Overview

A readiness or gap analysis evaluates an organization's current security posture against a target framework's requirements, identifying gaps and producing a prioritized remediation roadmap. It is a planning tool, not a formal assessment or certification, and is typically conducted 6-12 months before a planned audit or authorization effort.

## Purpose

- Assess current state of controls, policies, and processes against target requirements
- Identify gaps between current state and desired compliance or certification
- Quantify the effort and resources required to achieve compliance
- Prioritize remediation activities by risk and feasibility
- Set realistic timelines for audit or authorization readiness
- Provide executive visibility into compliance posture and investment needs

## Gap Analysis Types

| Type | Target | Typical Timing |
|------|--------|---------------|
| Pre-certification | ISO 27001, ISO 27701 | 6-12 months before Stage 1 audit |
| Pre-authorization | FedRAMP, StateRAMP | 6-18 months before 3PAO assessment |
| Pre-audit | SOC 2, PCI DSS | 3-6 months before Type II period or QSA engagement |
| Framework adoption | NIST CSF, CIS Controls | When adopting a new framework |
| Regulation readiness | HIPAA, GDPR, CMMC | When subject to a new regulatory requirement |
| Post-incident | Any applicable framework | After a breach or significant security event |

## Methodology

### Step 1: Define Scope and Target

- Select the target framework, standard, or regulation
- Define the baseline or profile (e.g., FedRAMP Moderate, CMMC Level 2, NIST CSF Tier 3)
- Identify the organizational scope (business units, systems, locations)
- Determine assessment boundaries (what is included and excluded)
- Identify stakeholders and assign roles

### Step 2: Inventory Existing Controls

- Catalog existing policies, procedures, and standards
- Document current technical controls and configurations
- Identify existing certifications and prior audit results
- Map existing controls to an internal control framework or catalog
- Note recent changes or planned initiatives that affect the control environment

### Step 3: Map Controls to Framework Requirements

- Create a mapping matrix: existing controls vs. target framework requirements
- Identify where existing controls satisfy framework requirements (full or partial)
- Identify requirements with no corresponding controls
- Leverage existing cross-framework mappings (e.g., NIST CSF to 800-53, CIS Controls to ISO 27001)
- Document assumptions and mapping rationale

### Step 4: Assess Each Requirement

Evaluate each framework requirement against the current state:

| Status | Definition | Color Code |
|--------|-----------|------------|
| Implemented | Control fully meets the requirement with evidence | Green |
| Partially Implemented | Control exists but does not fully meet the requirement | Yellow |
| Planned | Control is in development or budgeted but not yet implemented | Orange |
| Not Implemented | No control exists to address the requirement | Red |
| Not Applicable | Requirement does not apply (with documented justification) | Gray |

### Step 5: Identify and Prioritize Gaps

- List all Partially Implemented and Not Implemented requirements
- Assess each gap's risk impact (What is the exposure if not addressed?)
- Categorize gaps by effort required (Quick Win, Moderate, Significant)
- Identify dependencies between remediation activities
- Rank gaps by a combination of risk severity and remediation feasibility

### Step 6: Develop Remediation Roadmap

- Group remediation activities into phases (immediate, short-term, long-term)
- Assign ownership for each remediation activity
- Estimate resource requirements (personnel, budget, tools)
- Set target completion dates aligned with the audit or authorization timeline
- Identify milestones and checkpoints for progress tracking

## Maturity Model Assessment

A maturity assessment complements the binary gap analysis by evaluating how well controls are implemented:

### CMM-Style Maturity Levels

| Level | Name | Description |
|-------|------|-------------|
| 0 | Non-existent | No awareness of the need; no processes or controls |
| 1 | Initial / Ad-hoc | Processes are unpredictable, reactive, and poorly controlled |
| 2 | Repeatable | Basic processes are established and can be repeated; limited documentation |
| 3 | Defined | Processes are documented, standardized, and integrated into the organization |
| 4 | Managed / Measured | Processes are monitored and measured; data-driven management |
| 5 | Optimizing | Continuous improvement through quantitative feedback and innovation |

### Maturity Assessment Application

- Assess each control domain or requirement area at a maturity level
- Most organizations target Level 3 (Defined) for initial certification
- Level 4-5 represent advanced maturity and are aspirational for most programs
- Maturity scores can be visualized as a spider/radar chart for executive communication
- Track maturity improvements over time to demonstrate program growth

### Maturity by Domain Example

| Domain | Current Level | Target Level | Gap |
|--------|--------------|-------------|-----|
| Access Control | 3 — Defined | 3 — Defined | None |
| Incident Response | 1 — Ad-hoc | 3 — Defined | 2 levels |
| Risk Management | 2 — Repeatable | 3 — Defined | 1 level |
| Change Management | 3 — Defined | 4 — Managed | 1 level |
| Asset Management | 1 — Ad-hoc | 3 — Defined | 2 levels |
| Logging/Monitoring | 2 — Repeatable | 4 — Managed | 2 levels |

## Gap Analysis Deliverables

| Deliverable | Description |
|-------------|-------------|
| Findings Matrix | Spreadsheet mapping each requirement to current status, gap description, and evidence |
| Heat Map | Visual summary of compliance posture by domain or control family |
| Maturity Assessment | Spider chart or scorecard showing maturity by domain |
| Remediation Roadmap | Phased plan with activities, owners, timelines, and resource estimates |
| Resource Estimate | Budget and staffing requirements for remediation |
| Executive Summary | High-level findings, risk exposure, and recommended investment |

## Prioritization Framework

### Risk-Based Prioritization Matrix

| Priority | Risk Level | Effort | Action |
|----------|-----------|--------|--------|
| P1 — Critical | High risk | Any | Address immediately; blocks certification/authorization |
| P2 — High | High risk | High effort | Begin planning now; long lead time |
| P3 — Medium | Moderate risk | Moderate effort | Schedule in current phase |
| P4 — Low | Low risk | Low effort | Quick wins; address opportunistically |
| P5 — Deferred | Low risk | High effort | Plan for future phases |

### Prioritization Factors

- **Risk severity**: What is the potential impact if the gap is exploited?
- **Likelihood**: How probable is exploitation given the current threat landscape?
- **Effort**: Resources, time, and complexity required to remediate
- **Dependencies**: Does remediation depend on other activities completing first?
- **Quick wins**: Can the gap be closed with minimal effort for outsized benefit?
- **Audit timeline**: Does the gap block certification or create a major nonconformity?

## Quick Wins vs Long-Term Improvements

### Quick Wins (typically completed in 1-4 weeks)
- Documenting existing but undocumented processes
- Enabling security features already available in existing tools
- Updating outdated policies and procedures
- Configuring logging and alerting for existing systems
- Implementing MFA where infrastructure already supports it
- Formalizing existing informal processes (e.g., change management)

### Long-Term Improvements (typically 3-12 months)
- Implementing a new SIEM or security monitoring platform
- Deploying a GRC tool for risk and compliance management
- Building a formal vendor risk management program
- Establishing a security operations center (SOC)
- Redesigning network architecture for segmentation
- Implementing identity governance and administration (IGA)

## Stakeholder Communication

### Reporting Cadence

| Audience | Content | Frequency |
|----------|---------|-----------|
| Executive leadership | Summary findings, risk exposure, investment asks | At gap analysis completion; quarterly updates |
| CISO / Security leadership | Detailed findings, remediation progress, blockers | Bi-weekly during remediation |
| Control owners | Assigned gaps, remediation guidance, deadlines | Weekly during active remediation |
| Audit committee / Board | High-level posture, key risks, certification timeline | Quarterly or as needed |

### Communication Best Practices
- Lead with risk, not compliance checkboxes
- Use visual aids (heat maps, maturity charts, trend lines)
- Be specific about resource and budget requirements
- Highlight quick wins to demonstrate early progress
- Set realistic expectations for certification timelines

## Common Gaps by Framework

| Framework | Common Gaps |
|-----------|------------|
| ISO 27001 | Missing risk assessment, incomplete SoA, no internal audit, objectives not measurable |
| FedRAMP | Incomplete SSP narratives, missing FIPS 140 encryption, POA&M process immaturity |
| SOC 2 | No formal change management, access reviews not periodic, missing vendor assessments |
| PCI DSS | Scope creep, missing network segmentation, insufficient logging, key management gaps |
| NIST CSF | No formal risk management process, inconsistent asset inventory, weak detection capabilities |
| CMMC | Inadequate CUI identification, missing NIST 800-171 controls, no SSP for CUI systems |
| HIPAA | Missing risk analysis, BAA gaps, insufficient access controls, no breach notification process |

## Gap Analysis vs Formal Assessment

| Attribute | Gap Analysis | Formal Assessment |
|-----------|-------------|-------------------|
| Purpose | Planning and readiness | Certification or attestation |
| Authority | Internal or advisory | Accredited assessor (3PAO, CB, QSA, CPA) |
| Output | Roadmap and recommendations | SAR, ROC, SOC report, certificate |
| Regulatory value | None (internal planning tool) | Satisfies regulatory or contractual requirements |
| Independence | Not required (but recommended) | Required |
| Scope | Flexible, can be partial | Must cover full baseline/scope |

A gap analysis is not a substitute for a formal assessment. It is a preparatory activity that identifies what must be done before a formal assessment can succeed.

## Key References

- NIST Cybersecurity Framework (CSF) 2.0
- ISO/IEC 27001:2022
- CMMI Institute — Capability Maturity Model
- ISACA COBIT — Maturity Assessment
- FedRAMP Authorization Boundary Guidance
