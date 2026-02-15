# CMMC 2.0 — Cybersecurity Maturity Model Certification

## Overview

CMMC (Cybersecurity Maturity Model Certification) is the DoD's verification mechanism ensuring defense contractors implement adequate cybersecurity practices to protect Federal Contract Information (FCI) and Controlled Unclassified Information (CUI). CMMC 2.0 codified in 32 CFR Part 170 (final rule effective December 16, 2024) replaces the self-attestation model under DFARS 252.204-7012 with a tiered certification requirement.

**Governing authority**: DoD CIO, administered by the Cyber AB (formerly CMMC Accreditation Body)
**Primary standards**: NIST SP 800-171 Rev 2, NIST SP 800-172, FAR 52.204-21
**Applicability**: All companies in the Defense Industrial Base (DIB) handling FCI or CUI

## CMMC 2.0 vs 1.0 Changes

| Aspect | CMMC 1.0 (2020) | CMMC 2.0 (2024) |
|--------|-----------------|-----------------|
| Maturity levels | 5 levels | 3 levels |
| Total unique practices | 171 | 110+ (aligned to NIST standards) |
| Delta practices (CMMC-unique) | 20 practices beyond NIST | Eliminated — pure NIST alignment |
| Process maturity | Required (ML 2-5) | Removed |
| Self-assessment | Not allowed | Allowed for Level 1 and select Level 2 |
| POA&Ms | Not allowed | Conditionally allowed (limited) |
| Waivers | Not available | Available (mission-critical, senior DoD approval) |
| Cost model | All third-party assessed | Reduced third-party burden |

Key simplification: the five levels (Basic, Intermediate, Good, Proactive, Advanced) collapsed to three (Foundational, Advanced, Expert), eliminating CMMC-unique practices and aligning entirely to existing NIST publications.

## Three CMMC 2.0 Levels

| Attribute | Level 1 — Foundational | Level 2 — Advanced | Level 3 — Expert |
|-----------|----------------------|-------------------|-----------------|
| **Data protected** | FCI | CUI | CUI in highest-priority programs |
| **Practice source** | FAR 52.204-21 | NIST SP 800-171 Rev 2 | NIST SP 800-172 (selected) |
| **Practice count** | 17 | 110 | 110 + 24 selected from 800-172 |
| **Assessment type** | Annual self-assessment | C3PAO or self-assessment (select programs) | Government-led (DIBCAC) |
| **Assessment frequency** | Annual | Triennial | Triennial |
| **Affirmation** | Senior official affirms annually | Senior official affirms annually | Senior official affirms annually |
| **POA&M allowed** | Not applicable | Yes, with conditions | Yes, with conditions |
| **SPRS score entry** | Required | Required | Required |

## Level 1 — Foundational (17 Practices)

Level 1 maps to 17 practices derived from the 15 safeguarding requirements in FAR 52.204-21 "Basic Safeguarding of Covered Contractor Information Systems" per 32 CFR Part 170 Table 1. The 17 practices span 6 domains.

| Domain | Practice ID(s) | Practice Description |
|--------|---------------|---------------------|
| **Access Control (AC)** | L1-3.1.1 | Limit system access to authorized users, processes, or devices |
| | L1-3.1.2 | Limit system access to authorized transaction and function types |
| | L1-3.1.20 | Verify and control connections to external systems |
| | L1-3.1.22 | Control information posted on publicly accessible systems |
| **Identification & Authentication (IA)** | L1-3.5.1 | Identify system users, processes, or devices |
| | L1-3.5.2 | Authenticate identities of users, processes, or devices |
| **Media Protection (MP)** | L1-3.8.3 | Sanitize or destroy media containing FCI before disposal or reuse |
| **Physical Protection (PE)** | L1-3.10.1 | Limit physical access to authorized individuals |
| | L1-3.10.3 | Escort visitors and monitor visitor activity |
| | L1-3.10.4 | Maintain audit logs of physical access |
| | L1-3.10.5 | Control and manage physical access devices |
| **System & Communications Protection (SC)** | L1-3.13.1 | Monitor, control, and protect communications at system boundaries |
| | L1-3.13.5 | Implement subnetworks for publicly accessible components |
| **System & Information Integrity (SI)** | L1-3.14.1 | Identify, report, and correct system flaws in a timely manner |
| | L1-3.14.2 | Provide protection from malicious code |
| | L1-3.14.4 | Update malicious code protection mechanisms |
| | L1-3.14.5 | Perform periodic and real-time scans for malicious code |

## Level 2 — Advanced (110 Practices)

Level 2 requires implementation of all 110 security requirements from NIST SP 800-171 Rev 2 across 14 families. These 110 requirements map directly to a subset of the NIST 800-53 Moderate baseline.

### NIST 800-171 Rev 2 Requirements by Family

| Family | ID Range | Count | Description |
|--------|----------|-------|-------------|
| **3.1 Access Control** | 3.1.1 – 3.1.22 | 22 | Account management, access enforcement, flow control, separation of duties, least privilege, session control, remote access, wireless, mobile, CUI on external systems, publicly accessible content |
| **3.2 Awareness & Training** | 3.2.1 – 3.2.3 | 3 | Security awareness, role-based training, insider threat awareness |
| **3.3 Audit & Accountability** | 3.3.1 – 3.3.9 | 9 | Event logging, audit content, audit capacity, audit review/reporting, audit reduction, time stamps, protection of audit info, audit process failure alerts, correlation of review/analysis/reporting |
| **3.4 Configuration Management** | 3.4.1 – 3.4.9 | 9 | System baselines, security configuration settings, change tracking, security impact analysis, access restrictions for change, least functionality, non-essential component restrictions, application execution policies, user-installed software |
| **3.5 Identification & Authentication** | 3.5.1 – 3.5.11 | 11 | User identification, device authentication, multi-factor authentication, replay-resistant authentication, identifier management, authenticator management, obscuring feedback, cryptographic module authentication, non-privileged account use for privileged functions, authenticator feedback, password requirements |
| **3.6 Incident Response** | 3.6.1 – 3.6.3 | 3 | IR capabilities (planning, detection, analysis, containment, recovery), IR tracking/documenting/reporting, IR plan testing |
| **3.7 Maintenance** | 3.7.1 – 3.7.6 | 6 | System maintenance, maintenance tools, remote maintenance, maintenance personnel oversight and media inspection |
| **3.8 Media Protection** | 3.8.1 – 3.8.9 | 9 | Media protection policies, CUI access restrictions on media, media sanitization, media marking, media access control, media transport cryptography, media accountability, removable media usage control, media storage cryptography |
| **3.9 Personnel Security** | 3.9.1 – 3.9.2 | 2 | Personnel screening, CUI protection during personnel actions (termination/transfer) |
| **3.10 Physical Protection** | 3.10.1 – 3.10.6 | 6 | Physical access authorization, facility protection/monitoring, visitor escorts, physical access logs, physical access devices, alternate work sites |
| **3.11 Risk Assessment** | 3.11.1 – 3.11.3 | 3 | Risk assessments, vulnerability scanning, vulnerability remediation |
| **3.12 Security Assessment** | 3.12.1 – 3.12.4 | 4 | Control assessments, plans of action, continuous monitoring, system security plans |
| **3.13 System & Comms Protection** | 3.13.1 – 3.13.16 | 16 | Boundary protection, architectural designs, role separation, shared resource control, boundary deny-by-default, split tunneling prohibition, cryptographic protection for CUI in transit, session termination, cryptographic key management, FIPS-validated cryptography, CUI confidentiality at rest, collaborative device control, mobile code, VoIP, authenticity of communications sessions, CUI at rest on mobile |
| **3.14 System & Info Integrity** | 3.14.1 – 3.14.7 | 7 | Flaw remediation, malicious code protection, security alerts/advisories, system monitoring, unauthorized use identification, inbound/outbound communications monitoring, unauthorized connections identification |
| | | **110** | **Total** |

## Level 3 — Expert (110 + Selected 800-172 Requirements)

Level 3 builds on Level 2 (all 110 NIST 800-171 practices) and adds 24 selected requirements from NIST SP 800-172 "Enhanced Security Requirements for Protecting CUI." These address APT-level threats targeting critical defense programs.

800-172 enhanced requirements focus on:
- Dual authorization for critical operations
- Advanced threat hunting and analytics
- Supply chain risk management controls
- Penetration testing (red team exercises)
- Automated incident response orchestration
- Hardware-enforced protections and isolation
- Network segmentation and microsegmentation
- Specialized security engineering principles

Assessment is government-led by DIBCAC (Defense Industrial Base Cybersecurity Assessment Center).

## CUI Scope and Marking

**Controlled Unclassified Information (CUI)** is information the government creates or possesses, or that an entity creates or possesses for or on behalf of the government, that requires safeguarding or dissemination controls per law, regulation, or government-wide policy.

| Attribute | Detail |
|-----------|--------|
| **Governing order** | Executive Order 13556, 32 CFR Part 2002 |
| **Registry** | CUI Registry (archives.gov/cui) — lists approved categories and subcategories |
| **Marking format** | `CUI` banner, category marking (e.g., `CUI//SP-CTI`), dissemination controls (e.g., `CUI//NOFORN`) |
| **Categories** | 20 CUI categories (e.g., Defense, Export Control, Privacy, Critical Infrastructure, Procurement/Acquisition) |
| **Dissemination controls** | NOFORN, FEDCON, DL ONLY, REL TO [country] |
| **Decontrolling** | Originator or designee can decontrol; follows agency-specific procedures |
| **Distinction from classified** | CUI is NOT classified — it sits below Confidential/Secret/Top Secret |

**CMMC scope determination**: Only systems that process, store, or transmit CUI (or FCI for Level 1) fall within the CMMC assessment boundary. Proper CUI identification and data flow mapping is the critical first step.

## DFARS Clauses

| Clause | Title | Purpose |
|--------|-------|---------|
| **DFARS 252.204-7012** | Safeguarding Covered Defense Information | Requires adequate security per NIST 800-171, mandates 72-hour cyber incident reporting to DC3, requires medium assurance PKI certificate for incident reporting, flow-down to subcontractors |
| **DFARS 252.204-7019** | Notice of NIST SP 800-171 DoD Assessment Requirements | Requires current NIST 800-171 assessment score posted to SPRS as a condition of award |
| **DFARS 252.204-7020** | NIST SP 800-171 DoD Assessment Requirements | Provides for DoD Medium or High assessments (government-conducted), right of access for assessment, three-year validity |
| **DFARS 252.204-7021** | Cybersecurity Maturity Model Certification Requirements | Requires specified CMMC level as condition of contract award, mandatory flow-down to subcontractors handling CUI/FCI |

**Flow-down requirement**: Prime contractors must flow down DFARS 7012 and 7021 to all subcontractors that handle FCI or CUI. The required CMMC level matches the data type the subcontractor handles.

## POA&M Allowance Under CMMC 2.0

CMMC 2.0 permits POA&Ms under strict conditions, unlike CMMC 1.0 which required 100% implementation at assessment.

| Condition | Requirement |
|-----------|-------------|
| **Eligibility** | Only Level 2 and Level 3 assessments |
| **Maximum open POA&Ms** | Cannot have NOT MET findings on more than a limited subset of requirements |
| **SPRS score threshold** | Must achieve a minimum score of 80% (SPRS score >= 88 out of 110 for Level 2) |
| **Closeout timeline** | All POA&Ms must be closed within 180 days of conditional certification |
| **Prohibited POA&M items** | Certain critical requirements cannot be placed on POA&M (e.g., FIPS-validated cryptography 3.13.11, MFA 3.5.3, flaw remediation 3.14.1) |
| **Verification** | Closeout requires senior official affirmation; C3PAO may verify |

If POA&M items are not closed within 180 days, the conditional CMMC certification status is revoked.

## Assessment Process

### Level 1 — Self-Assessment

1. Identify all systems processing, storing, or transmitting FCI
2. Evaluate 17 practices against FAR 52.204-21
3. Document results in the Basic Assessment format
4. Enter results into SPRS (Supplier Performance Risk System)
5. Senior company official submits annual affirmation letter
6. Repeat annually

### Level 2 — C3PAO Assessment

1. **Scoping**: Define assessment boundary (CUI assets, security protection assets, contractor risk-managed assets, specialized assets, out-of-scope assets)
2. **Readiness**: Conduct gap assessment against all 110 NIST 800-171 requirements, remediate gaps, prepare SSP and POA&M
3. **Pre-assessment**: Optional — engage C3PAO for a readiness review
4. **Assessment**: C3PAO conducts formal assessment — document review, interviews, testing (typically 1-2 weeks onsite)
5. **Scoring**: C3PAO calculates SPRS score, identifies MET/NOT MET per requirement
6. **Reporting**: C3PAO submits results to Cyber AB; CMMC certification issued if passing
7. **Affirmation**: Senior official affirms annually during 3-year certification period
8. **POA&M closeout**: If conditional, close all items within 180 days

For select Level 2 programs (non-critical CUI), self-assessment may be permitted per contract language.

### Level 3 — DIBCAC Assessment

1. Must first achieve Level 2 certification from a C3PAO
2. DIBCAC (government assessors) conduct additional assessment of selected 800-172 requirements
3. Government-led, no cost to contractor for assessment itself
4. Results determine Level 3 certification eligibility
5. Triennial reassessment required

## SPRS Scoring Methodology

SPRS (Supplier Performance Risk System) scores reflect a contractor's implementation status against NIST 800-171 Rev 2.

| Score Element | Detail |
|---------------|--------|
| **Maximum score** | 110 (all 110 requirements fully implemented) |
| **Minimum possible** | -203 (all weighted requirements NOT MET) |
| **Scoring method** | Each of the 110 requirements has a point value of 1, 3, or 5 based on its security weight |
| **5-point requirements** | The most critical requirements (e.g., MFA, FIPS crypto, flaw remediation) — 43 requirements |
| **3-point requirements** | Moderate criticality — 42 requirements |
| **1-point requirements** | Lower criticality — 25 requirements |
| **Deduction** | NOT MET requirement = deduct its point value from 110 |
| **Passing for CMMC L2** | Minimum 88 to qualify for conditional certification with POA&M |

**Assessment confidence levels**:

| Assessment Type | Confidence | Conducted By |
|-----------------|------------|--------------|
| Basic (self) | Low | Contractor |
| Medium | Medium | DoD (DCMA DIBCAC) |
| High | High | DoD (DCMA DIBCAC, onsite) |

SPRS scores and assessment dates are visible to DoD contracting officers. A current assessment (within 3 years) is a condition for contract award under DFARS 7019.

## Relationship to NIST 800-53

NIST 800-171 derives from the NIST 800-53 Moderate baseline. Understanding this lineage is essential for organizations that maintain both DoD (CMMC) and federal civilian (FedRAMP/FISMA) compliance programs.

| Aspect | NIST 800-53 (Moderate) | NIST 800-171 Rev 2 |
|--------|----------------------|-------------------|
| **Intended environment** | Federal information systems | Non-federal systems handling CUI |
| **Total controls** | ~304 controls (incl. enhancements) | 110 requirements |
| **Derivation** | Standalone catalog | Selected and tailored from 800-53 Moderate |
| **Control numbering** | Family-based (e.g., AC-2) | Section-based (e.g., 3.1.1) |
| **Non-applicable controls removed** | N/A | Removed controls primarily satisfied by the federal government (e.g., PM family, certain PE/PS) |
| **NFO requirements** | N/A | 61 "Non-Federal Organization" controls (Appendix E) — expected but not assessed |

**Mapping example**: NIST 800-171 requirement 3.1.1 (Limit system access to authorized users) maps to NIST 800-53 AC-2, AC-3, AC-17. The 800-171 requirement is a condensed expression of the intent across multiple 800-53 controls.

For organizations with both FedRAMP and CMMC obligations, achieving FedRAMP Moderate authorization substantially covers CMMC Level 2 requirements, though the assessment processes and reporting formats differ.

## Key Timelines and Dates

| Milestone | Date |
|-----------|------|
| CMMC 1.0 published | January 2020 |
| CMMC 2.0 announced | November 2021 |
| 32 CFR Part 170 final rule | October 15, 2024 (effective December 16, 2024) |
| 48 CFR CMMC rule (DFARS) | Phased rollout beginning 2025 |
| Phase 1 | CMMC Level 1 and Level 2 self-assessment in solicitations |
| Phase 2 (+1 year) | CMMC Level 2 C3PAO assessment in solicitations |
| Phase 3 (+1 year) | CMMC Level 3 in solicitations |
| Phase 4 (full) | CMMC required in all applicable DoD contracts with option exercise |

## Common Pitfalls

1. **Scope creep** — Failing to properly define and minimize the CUI boundary increases cost and complexity
2. **Encryption gaps** — FIPS 140-2/140-3 validated cryptography (3.13.11) is non-negotiable and cannot be placed on POA&M
3. **SSP deficiency** — Many organizations lack a current, detailed System Security Plan; this is an assessable requirement (3.12.4)
4. **MFA gaps** — Multi-factor authentication for local and network access (3.5.3) is a high-value control; often missed on legacy systems
5. **Subcontractor flow-down** — Primes are responsible for ensuring subcontractor compliance; DFARS 7012/7021 must flow down
6. **SPRS entry** — Forgetting to post assessment scores to SPRS blocks contract award
7. **CUI identification** — Not all data from DoD is CUI; only properly marked or contractually identified data triggers CMMC requirements
8. **Shared responsibility confusion** — Cloud service provider (CSP) responsibilities vs. contractor responsibilities must be documented in a CRM/shared responsibility matrix
9. **Incident reporting** — 72-hour reporting to DC3 (Defense Cyber Crime Center) is a DFARS 7012 requirement, not optional
10. **POA&M over-reliance** — POA&Ms are allowed but limited; failing to close within 180 days revokes certification
