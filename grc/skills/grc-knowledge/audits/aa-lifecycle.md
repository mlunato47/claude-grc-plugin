# Authorization and Assessment (A&A) Lifecycle

## Overview

The A&A lifecycle follows the NIST Risk Management Framework (RMF) defined in NIST SP 800-37 Rev 2. The RMF integrates security and risk management into the system development lifecycle through seven steps: Prepare, Categorize, Select, Implement, Assess, Authorize, and Monitor. It is mandatory for federal systems including FedRAMP cloud authorizations.

### RMF Prepare Step
*Note: NIST SP 800-37 Rev 2 added Prepare as the first formal RMF step. The sections below number Categorize through Monitor as Steps 1-6, following the convention used by many federal organizations. In strict 800-37 Rev 2 numbering, Prepare=Step 1 and Monitor=Step 7.*

Before the Categorize step, organizations assign key roles (AO, System Owner, ISSO, ISSM), identify the authorization boundary, characterize the system, establish a risk management strategy, and register the system in inventory.

---

## Step 1 — Categorize

Determine the security impact level based on information types the system processes, stores, and transmits.

### FIPS 199 Impact Levels

| Impact Level | Definition |
|-------------|-----------|
| Low | Limited adverse effect on operations, assets, or individuals |
| Moderate | Serious adverse effect on operations, assets, or individuals |
| High | Severe or catastrophic adverse effect on operations, assets, or individuals |

### NIST SP 800-60 Information Types
- 800-60 Vol 2 catalogs information types with recommended C/I/A impact levels
- Types grouped by mission-based and management/support categories
- Organizations identify all information types processed and assign provisional impacts

### High Water Mark (HWM)
The system categorization uses: `SC = {(C, HWM-C), (I, HWM-I), (A, HWM-A)}`. The highest impact for each objective across all information types determines the system level. The overall category is the highest of C, I, and A.

### FedRAMP Impact Levels

| Level | Description | Controls (Approx.) |
|-------|-------------|-------------------|
| Low | Publicly available data | ~158 |
| Moderate | Controlled unclassified information, PII | ~322 |
| High | Law enforcement, healthcare, financial data | ~410 |
| LI-SaaS | Low Impact SaaS (limited functionality) | ~158 |

**Output:** Security Categorization Document (system ID, information types, impact levels, adjustments with justification, AO approval).

---

## Step 2 — Select

Select the appropriate security control baseline and tailor it to the system's needs.

### Baseline Selection (NIST SP 800-53B)

| System Category | Approximate Controls |
|----------------|---------------------|
| Low | ~150 |
| Moderate | ~304 |
| High | ~392 |

### Tailoring Activities

| Activity | Description |
|----------|-------------|
| Scoping | Remove non-applicable controls based on technology/environment |
| Compensating Controls | Substitute equivalent controls when baseline controls cannot be implemented |
| Organization-Defined Parameters | Specify values for discretionary parameters (e.g., session timeout = 15 min) |
| Supplementation | Add controls beyond the baseline based on risk assessment |

### FedRAMP Baseline Overlays
FedRAMP publishes overlays augmenting NIST baselines with cloud-specific requirements (FIPS 140 encryption, US-based personnel). ODPs are pre-defined by FedRAMP where applicable.

**Output:** SSP with selected baseline, tailoring decisions, ODP values, control applicability, and allocation (common, system-specific, hybrid).

---

## Step 3 — Implement

Implement selected controls and document implementation in the SSP.

### SSP Narrative Elements
Each control description must address: **What** (control function), **Who** (responsible parties), **How** (technology/process), **When** (frequency), **Where** (boundary/segment/facility).

### Control Types

| Type | Definition | Example |
|------|-----------|---------|
| Common | Inherited from organizational capability or shared service | Org-wide security awareness training (AT-2) |
| System-Specific | Implemented within the system boundary | System access control configuration (AC-2) |
| Hybrid | Partially inherited, partially system-specific | Audit policy (common) + log config (system-specific) |

### Inherited Controls
CSPs inherit controls from IaaS/PaaS providers. The Customer Responsibility Matrix (CRM) defines which controls are fully inherited, shared, or fully the CSP's responsibility. FedRAMP requires explicit inheritance documentation in the SSP.

**Output:** Updated SSP with complete implementation narratives, configuration docs, architecture and data flow diagrams.

---

## Step 4 — Assess

Assess controls to determine if they are implemented correctly, operating as intended, and producing the desired outcome.

### Security Assessment Plan (SAP)
Defines scope, methodology, schedule, team qualifications, rules of engagement, and sampling methodology. Must be approved by the AO.

### Independent Assessor

| Context | Assessor |
|---------|----------|
| FedRAMP | 3PAO (A2LA accredited) |
| DoD | DISA or authorized SCA |
| Federal agency | Independent internal or contracted assessor |
| Non-federal | Internal audit team or third-party assessor |

### Assessment Methods (NIST SP 800-53A)

| Method | Description |
|--------|-------------|
| Examine | Review documents, records, mechanisms, activities |
| Interview | Discuss controls with responsible personnel |
| Test | Exercise controls to verify expected behavior |

FedRAMP requires **comprehensive** depth and coverage for initial assessments (thorough testing of all aspects; full population coverage).

**Output:** SAR with executive summary, methodology, risk exposure table, detailed findings with severity ratings, recommendations, and evidence appendices.

---

## Step 5 — Authorize

The AO reviews assessment results, determines if residual risk is acceptable, and makes an authorization decision.

### Authorization Package

| Document | Purpose |
|----------|---------|
| SSP | Complete system and control description |
| SAR | Assessment findings and risk exposure |
| POA&M | Remediation plan for open findings |
| Boundary Diagram | Visual scope of what is authorized |
| Supporting Artifacts | Policies, scans, test results, diagrams |

### Risk Determination
The AO reviews residual risk in the SAR, considers organizational risk tolerance and mission needs, evaluates POA&M timelines, and makes a formal, documented risk acceptance decision.

### Authorization Decisions

| Decision | Meaning | Duration |
|----------|---------|----------|
| ATO | System authorized; risk accepted | Ongoing authorization maintained through ConMon (some agencies still issue 3-year terms) |
| P-ATO | JAB-issued (JAB dissolved May 2024; replaced by FedRAMP Board); agencies leverage for their own ATO | Requires agency ATO for operation |
| DATO | Risk not acceptable; system cannot operate | Must remediate and resubmit |
| IATT | Limited authorization for testing only | Typically 90-180 days |

### Authorization Boundary
Defines all authorized components (hardware, software, network, data, people). Must align with the SSP. Changes may require reassessment. FedRAMP requires detailed boundary diagrams with data flows.

**Output:** Authorization Decision Letter (decision, system ID, scope, risk acceptance, conditions, termination date).

---

## Step 6 — Monitor

Maintain ongoing awareness of security posture and ensure continued authorization.

### Continuous Monitoring Strategy
Defines: monitoring objectives, assessment frequency per control family, automated and manual activities, roles, reporting requirements, escalation procedures, and tooling.

### Ongoing Assessments

| Activity | Frequency |
|----------|-----------|
| Vulnerability scanning | Monthly (OS/infra, web app, database) |
| Control assessment | Annual (rotating subset; 3PAO for FedRAMP) |
| Penetration testing | Annual |
| Configuration compliance | Continuous or monthly |
| Contingency plan testing | Annual |

### Configuration and Change Management
All changes require security impact analysis. Significant changes may trigger 3PAO reassessment (FedRAMP). Configuration baselines must be maintained with deviations tracked.

### POA&M Management

| Field | Description |
|-------|-------------|
| POA&M ID | Unique identifier |
| Finding Source | SAR, scan, incident, internal audit |
| Weakness | Description of vulnerability or deficiency |
| Risk Level | Critical, High, Moderate, Low |
| Affected Controls | NIST 800-53 control IDs |
| Remediation Plan | Steps to address the weakness |
| Milestones | Checkpoints with dates |
| Scheduled Completion | Target remediation date |
| Status | Open, In Progress, Completed, Closed, Risk Accepted |

**FedRAMP Remediation Timelines:** Critical = 30 days, High = 30 days, Moderate = 90 days, Low = 180 days.

### Reauthorization Triggers
Authorization expiration, significant system change, major incident, mission change, risk tolerance change, new threats fundamentally altering risk. FedRAMP continuous authorization replaces periodic reauthorization when ConMon requirements are met.

### FedRAMP Monthly/Annual Deliverables

| Deliverable | Frequency |
|-------------|-----------|
| Vulnerability scan results | Monthly |
| POA&M updates | Monthly |
| Inventory updates | Monthly |
| ConMon summary report | Monthly |
| Significant change requests | As needed |
| Annual 3PAO assessment | Annual |
| Incident reports | As needed (per CISA reporting timelines — 1 hour for CAT 1-3) |

**Output:** Ongoing authorization evidence demonstrating continuous compliance, active POA&M management, timely vulnerability response, proper change handling, and regular AO reporting.

---

## End-to-End Timeline Estimates

| Path | Duration |
|------|----------|
| Federal ATO (Moderate) — Steps 1-5 | 12-24 months |
| FedRAMP JAB P-ATO *(historical; JAB dissolved May 2024)* | 12-21 months |
| FedRAMP Agency ATO | 9-18 months |

## Key References

- NIST SP 800-37 Rev 2 — Risk Management Framework
- NIST SP 800-53 Rev 5 — Security and Privacy Controls
- NIST SP 800-53A Rev 5 — Assessing Security and Privacy Controls
- NIST SP 800-53B — Control Baselines
- NIST SP 800-60 Vol 1/2 — Mapping Information Types to Security Categories
- FIPS 199 — Standards for Security Categorization
- FedRAMP Authorization Boundary and Continuous Monitoring Guidance
