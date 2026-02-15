# FISMA — Federal Information Security Modernization Act

## Overview

FISMA is the primary federal statute governing information security for executive branch agencies and their contractors. The original **Federal Information Security Management Act of 2002** (P.L. 107-347, Title III) established the framework; the **Federal Information Security Modernization Act of 2014** (P.L. 113-283) updated it to reflect modern threats, strengthen DHS's operational role, and shift from compliance-oriented reporting toward continuous monitoring and risk management.

FISMA requires every federal agency to develop, implement, and maintain an agency-wide information security program. It also mandates annual independent evaluations (Inspector General audits) and reporting to OMB, Congress, and DHS.

### Key Statutory Changes: 2002 vs. 2014

| Aspect | FISMA 2002 | FISMA 2014 |
|--------|-----------|-----------|
| Full title | Federal Information Security Management Act | Federal Information Security Modernization Act |
| Public law | P.L. 107-347, Title III | P.L. 113-283 |
| Reporting focus | Annual paper-based compliance | Continuous diagnostics and risk-based metrics |
| DHS role | Advisory only | Operational authority for federal civilian cybersecurity |
| OMB role | Policy oversight | Policy oversight + binding directives |
| Breach notification | Not addressed | Required notification to Congress for major incidents |
| Continuous monitoring | Not emphasized | Explicitly required |

## Legislative Authority and Oversight Structure

FISMA establishes a multi-layered governance model for federal cybersecurity.

| Entity | FISMA Role |
|--------|-----------|
| **Congress** | Enacts FISMA legislation; receives annual reports from OMB |
| **OMB** | Issues annual FISMA guidance (A-130, FISMA metrics memoranda); sets policy; oversees agency compliance |
| **DHS/CISA** | Operational cybersecurity authority for FCEB agencies; administers CDM program; operates CyberScope/FISMA reporting; issues Binding Operational Directives (BODs) |
| **NIST** | Develops security standards (FIPS) and guidelines (SP 800-series) that agencies must follow |
| **Agency heads** | Ultimately responsible for agency information security program |
| **Inspectors General** | Conduct annual independent FISMA evaluations |
| **GAO** | Government-wide audits and FISMA compliance reviews |

### Key Policy Documents

- **OMB Circular A-130** — Managing Information as a Strategic Resource; establishes agency responsibilities for information security and privacy
- **Annual OMB FISMA Guidance Memoranda** — E.g., M-22-09 (Zero Trust), M-23-03 (FY23 FISMA metrics); set yearly reporting requirements and strategic priorities
- **DHS Binding Operational Directives (BODs)** — Compulsory directives to FCEB agencies (e.g., BOD 22-01 for Known Exploited Vulnerabilities)

## FIPS 199 — Security Categorization

FIPS 199 defines the methodology for categorizing federal information systems based on potential impact across three security objectives.

### Impact Levels

| Impact Level | Definition |
|-------------|-----------|
| **Low** | Loss would have a limited adverse effect on operations, assets, or individuals |
| **Moderate** | Loss would have a serious adverse effect on operations, assets, or individuals |
| **High** | Loss would have a severe or catastrophic adverse effect on operations, assets, or individuals |

### Categorization Formula

The system categorization is expressed as:

```
SC information system = {(confidentiality, impact), (integrity, impact), (availability, impact)}
```

The **overall system categorization** is the high-water mark — the highest impact level across all three objectives. For example:

```
SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Low)}
→ Overall categorization: Moderate
```

### Information Types and NIST SP 800-60

NIST SP 800-60 (Vol. 1 & 2) provides guidance for mapping information types to provisional impact levels. It catalogs information types by mission areas (e.g., defense, health, law enforcement) and management areas (e.g., HR, financial, IT management). Agencies use 800-60 as the starting point and adjust based on agency-specific context.

## FIPS 200 — Minimum Security Requirements

FIPS 200 specifies 17 minimum security requirement areas that federal information systems must address. The specific controls satisfying these requirements are selected from NIST SP 800-53.

| # | Security Area | NIST 800-53 Family |
|---|-------------|-------------------|
| 1 | Access Control | AC |
| 2 | Awareness and Training | AT |
| 3 | Audit and Accountability | AU |
| 4 | Certification, Accreditation, and Security Assessments | CA |
| 5 | Configuration Management | CM |
| 6 | Contingency Planning | CP |
| 7 | Identification and Authentication | IA |
| 8 | Incident Response | IR |
| 9 | Maintenance | MA |
| 10 | Media Protection | MP |
| 11 | Physical and Environmental Protection | PE |
| 12 | Planning | PL |
| 13 | Personnel Security | PS |
| 14 | Risk Assessment | RA |
| 15 | System and Services Acquisition | SA |
| 16 | System and Communications Protection | SC |
| 17 | System and Information Integrity | SI |

FIPS 200 mandates that agencies apply the baseline controls from NIST 800-53B corresponding to the system's FIPS 199 categorization level. Tailoring (scoping and compensating controls) is permitted per NIST 800-53B guidance.

## Relationship to NIST Publications

FISMA relies on a constellation of NIST publications. These are not optional guidelines for federal agencies — FISMA gives NIST standards the force of law for executive branch systems.

| Publication | Title | FISMA Role |
|------------|-------|-----------|
| **FIPS 199** | Standards for Security Categorization | Mandatory categorization methodology |
| **FIPS 200** | Minimum Security Requirements | Mandatory minimum security areas |
| **SP 800-37 Rev 2** | Risk Management Framework | Mandatory RMF process (Categorize through Monitor) |
| **SP 800-53 Rev 5** | Security and Privacy Controls | Control catalog; basis for baseline selection |
| **SP 800-53A Rev 5** | Assessing Security and Privacy Controls | Assessment procedures for each control |
| **SP 800-53B** | Control Baselines | Low, Moderate, High baseline assignments |
| **SP 800-60 Vol 1&2** | Mapping Information Types to Categories | Guidance for FIPS 199 categorization |
| **SP 800-137** | ISCM for Federal Systems | Continuous monitoring strategy and program design |
| **SP 800-137A** | Assessing ISCM Programs | Maturity assessment for ConMon programs |
| **SP 800-128** | Configuration Management for Security | CM processes supporting FISMA requirements |
| **SP 800-30 Rev 1** | Risk Assessment Guide | Risk assessment methodology |
| **SP 800-39** | Managing Information Security Risk | Enterprise risk management framework |

## Agency Roles and Responsibilities

FISMA defines specific roles within federal agencies. These roles carry explicit statutory or regulatory responsibilities.

| Role | Abbreviation | Key Responsibilities |
|------|-------------|---------------------|
| **Agency Head** | — | Ultimate accountability for agency information security program; ensures adequate resources |
| **Chief Information Officer** | CIO | Designates CISO; ensures compliance with FISMA, OMB, and NIST requirements; reports to agency head |
| **Chief Information Security Officer** | CISO | Manages agency-wide infosec program; develops policies; trains personnel; oversees incident response; reports to CIO |
| **Authorizing Official** | AO | Accepts risk and grants ATO/DATO; accountable for system operation at accepted risk level |
| **System Owner** | SO | Responsible for system procurement, development, operation, and maintenance; ensures controls are implemented |
| **Information System Security Officer** | ISSO | Day-to-day security operations for assigned system(s); monitors compliance; manages POA&Ms |
| **Information System Security Manager** | ISSM | Oversees multiple ISSOs; ensures consistency across systems; reports to CISO |
| **Senior Agency Official for Privacy** | SAOP | Manages agency privacy program; PIA oversight; coordinates with CISO on overlapping concerns |

## FISMA Reporting Requirements

### CyberScope and FISMA Reporting

CyberScope is the DHS-operated reporting platform through which agencies submit FISMA metrics data. Key reporting characteristics:

- **Quarterly data feeds** — Agencies submit automated data on vulnerability management, configuration management, and other operational metrics
- **Annual CIO metrics** — CIO-reported metrics covering all FISMA metric domains
- **Annual IG metrics** — Independent IG-reported assessment of agency security posture
- **Ad hoc reporting** — Major incident reports within prescribed timelines

### Annual FISMA Report to Congress

OMB compiles agency-reported data and IG assessments into an annual FISMA report to Congress. This report includes:

- Agency-level FISMA scores and maturity ratings
- Government-wide trends in cybersecurity posture
- Status of key cybersecurity initiatives (CDM, Zero Trust, identity management)
- Incident statistics across the federal enterprise

### OMB Annual FISMA Guidance and Metrics

Each fiscal year, OMB issues guidance defining FISMA metrics and reporting requirements. These memoranda establish:

- Specific metrics agencies must report against
- Maturity model levels for each metric domain
- Alignment with the NIST Cybersecurity Framework (CSF) functions
- Cross-Agency Priority (CAP) goal targets
- Deadlines for submissions

## FISMA Metrics Categories

FISMA metrics are aligned to the five NIST Cybersecurity Framework functions. Each function contains specific metric areas with maturity levels ranging from Ad Hoc to Optimized.

### Maturity Model Levels

| Level | Name | Description |
|-------|------|-------------|
| 1 | Ad Hoc | Policies/processes not formalized; reactive |
| 2 | Defined | Policies defined but inconsistently implemented |
| 3 | Consistently Implemented | Policies implemented across the organization |
| 4 | Managed and Measurable | Metrics collected; quantitative performance data |
| 5 | Optimized | Continuous improvement based on metrics and lessons learned |

### Metric Domains by CSF Function

| CSF Function | FISMA Metric Areas |
|-------------|-------------------|
| **Identify** | Risk management, asset management, governance, supply chain risk management |
| **Protect** | Configuration management, identity and access management, data protection, security training |
| **Detect** | Intrusion detection, network/endpoint monitoring, security event logging, threat intelligence |
| **Respond** | Incident response, incident reporting, information sharing, mitigation activities |
| **Recover** | Recovery planning, contingency plan testing, lessons learned, communications |

## DHS CDM Program

The **Continuous Diagnostics and Mitigation (CDM)** program is a DHS/CISA initiative that provides federal agencies with tools and integration services to strengthen cybersecurity.

### CDM Capability Areas

| Phase | Capability | Focus |
|-------|-----------|-------|
| Phase 1 | HWAM / SWAM | Hardware Asset Management, Software Asset Management — what is on the network |
| Phase 2 | TRUST / BEHAVE | Credential and access management — who is on the network |
| Phase 3 | BOUND / MNGEVT | Network security, event management — what is happening on the network |
| Phase 4 | DATA | Data protection — how is data protected |

### CDM Architecture Components

- **CDM Agency Dashboard** — Agency-level visibility into cybersecurity posture
- **CDM Federal Dashboard** — DHS-operated cross-agency visibility
- **CDM Tools** — Vulnerability scanning, asset discovery, configuration assessment, privilege management tools provided to agencies
- **CDM Integration Layer** — Aggregates data from agency tools into standardized feeds

CDM data directly supports FISMA reporting by providing automated, near-real-time data on vulnerability management, asset inventory, and configuration compliance.

## Inspector General Audits and FISMA Scorecards

### IG FISMA Evaluations

Each agency's IG (or contracted independent assessor) conducts an annual FISMA evaluation that:

- Assesses the effectiveness of the agency information security program
- Evaluates a sample of agency systems against NIST controls
- Tests the maturity of security practices across all CSF function areas
- Reports findings using the IG FISMA Reporting Metrics defined by CIGIE and DHS
- Issues maturity ratings (Levels 1-5) for each metric domain

### FISMA Scorecards

OMB and congressional committees use FISMA scorecards to grade agency performance:

| Rating | Description |
|--------|-------------|
| **Managing Risk** | Agency demonstrates effective, organization-wide risk management |
| **At Risk** | Deficiencies exist in one or more function areas; remediation needed |
| **High Risk** | Critical or widespread deficiencies; immediate attention required |

Scorecards are published publicly and factor into agency budget and oversight discussions. Poor FISMA scores can trigger GAO reviews, congressional hearings, or additional OMB oversight.

## RMF Integration — How FISMA Drives RMF Adoption

FISMA mandates that agencies follow the NIST Risk Management Framework (SP 800-37). The RMF operationalizes FISMA requirements into a repeatable lifecycle.

| RMF Step | FISMA Requirement Addressed |
|----------|---------------------------|
| **Prepare** | Agency-wide information security program establishment |
| **Categorize** | FIPS 199 impact determination (statutory requirement) |
| **Select** | FIPS 200 baseline selection from 800-53 (statutory requirement) |
| **Implement** | Security control deployment per agency security program |
| **Assess** | Annual assessment requirement; IG evaluation |
| **Authorize** | AO risk acceptance; system authorization |
| **Monitor** | FISMA 2014 continuous monitoring mandate; CDM integration |

FISMA 2014 specifically strengthened the Monitor step by making continuous monitoring a statutory requirement rather than a best practice. This shifted agencies away from three-year reauthorization cycles toward ongoing authorization supported by automated monitoring.

## FISMA vs. FedRAMP

FISMA and FedRAMP are complementary but distinct. Understanding their relationship is critical for agencies consuming cloud services and CSPs seeking federal customers.

| Dimension | FISMA | FedRAMP |
|-----------|-------|---------|
| **Scope** | All federal information systems | Cloud Service Offerings (CSOs) used by federal agencies |
| **Authority** | Statute (P.L. 113-283) | OMB policy (codified in FedRAMP Authorization Act, P.L. 117-263, Title LIX) |
| **Applies to** | Federal agencies | Cloud Service Providers serving federal agencies |
| **Categorization** | FIPS 199 | FIPS 199 (same methodology) |
| **Control baselines** | NIST 800-53 (agency-selected) | NIST 800-53 + FedRAMP-specific parameters and additional controls |
| **Assessment** | Agency or IG assessment | 3PAO assessment |
| **Authorization** | Agency AO grants ATO | Agency ATO or FedRAMP P-ATO (via PMO review) |
| **Continuous monitoring** | Agency-managed ConMon | FedRAMP ConMon program with monthly deliverables to PMO |
| **Reciprocity** | Between agencies (limited) | "Do once, use many" — one authorization, multiple agencies |

A FedRAMP-authorized CSO satisfies the FISMA requirements for the cloud portion of an agency's system boundary. The agency remains responsible for FISMA compliance for agency-managed components, interconnections, and inherited control responsibilities that fall to the agency (documented in the CRM).

## Key Compliance Considerations for Analysts

### Common FISMA Findings

1. **Incomplete system inventory** — Agencies fail to maintain accurate HWAM/SWAM inventories
2. **Overdue POA&Ms** — Findings exceed remediation timelines without documented risk acceptance
3. **Inconsistent access reviews** — Privileged access reviews not performed at required frequency
4. **Inadequate contingency plan testing** — Plans exist but are not tested or test results are not documented
5. **Configuration management gaps** — Baselines not established or deviation tracking is absent
6. **Weak identity management** — MFA not fully deployed; shared/generic accounts persist
7. **Insufficient continuous monitoring** — Manual, periodic assessments instead of automated monitoring

### FISMA Compliance Checklist (High-Level)

- [ ] System categorized per FIPS 199 with supporting rationale (SP 800-60)
- [ ] Security control baseline selected per FIPS 200 and SP 800-53B
- [ ] System Security Plan documents all control implementations
- [ ] Independent assessment completed (SAR with findings)
- [ ] AO has granted current authorization (ATO with date)
- [ ] POA&M tracks all open findings with milestones
- [ ] Continuous monitoring strategy documented and operational
- [ ] Annual security training completed for all users
- [ ] Incident response plan tested within last 12 months
- [ ] Contingency plan tested within last 12 months
- [ ] FISMA metrics data submitted to CyberScope per OMB guidance

## References

| Document | Identifier |
|----------|-----------|
| FISMA 2014 | P.L. 113-283 |
| FISMA 2002 | P.L. 107-347, Title III |
| FedRAMP Authorization Act | P.L. 117-263, Title LIX |
| OMB Circular A-130 | Revised July 2016 |
| FIPS 199 | February 2004 |
| FIPS 200 | March 2006 |
| NIST SP 800-37 Rev 2 | December 2018 |
| NIST SP 800-53 Rev 5 | September 2020 (updated December 2020) |
| NIST SP 800-53A Rev 5 | January 2022 |
| NIST SP 800-53B | October 2020 |
| NIST SP 800-60 Vol 1 Rev 1 | August 2008 |
| NIST SP 800-137 | September 2011 |
| NIST CSF 2.0 | February 2024 |
