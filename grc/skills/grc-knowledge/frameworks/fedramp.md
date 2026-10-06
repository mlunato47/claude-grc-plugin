# FedRAMP (Federal Risk and Authorization Management Program)

> **This file covers the legacy Rev5 path.** As of the June 2026 Consolidated Rules (CR26), FedRAMP runs two non-interchangeable paths: legacy **Rev5** (active until at least December 31, 2028; last new certifications June 11, 2027) and **FedRAMP 20x** (KSI-based, generally available). CR26 also renamed "FedRAMP Authorized" → **"FedRAMP Certified"** and impact levels → **Certification Classes A–D**, and its VDR/VER vulnerability standards apply to Rev5 providers too (required December 7, 2026). For 20x, CR26, KSIs, VDR/VER, and the class system → `fedramp-20x.md`.

## Overview

FedRAMP is a U.S. government-wide program that provides a standardized approach to security authorizations for Cloud Service Offerings (CSOs). Established in 2011 and codified by the FedRAMP Authorization Act (part of the FY2023 NDAA), FedRAMP ensures that cloud products and services used by federal agencies meet consistent security requirements based on NIST SP 800-53.

**Governing Body**: General Services Administration (GSA) — FedRAMP (current program documents say "FedRAMP," not "FedRAMP PMO"; the PMO still exists within GSA)

**Legal Authority**: FedRAMP Authorization Act (44 U.S.C. 3607-3616), OMB Memoranda (A-130, M-24-15 "Modernizing FedRAMP"), FISMA

**Core Principle**: "Do once, use many" -- a CSP achieves authorization once and that authorization package can be reused by any federal agency, eliminating redundant assessments.

### Key Organizational Roles

| Entity | Role |
|--------|------|
| **GSA / FedRAMP** | Program governance, baseline maintenance, marketplace management, process oversight (legacy documents call this the "FedRAMP PMO") |
| **FedRAMP Board** | Replaced the JAB per OMB M-24-15 (July 2024); program governance body |
| **JAB** | Joint Authorization Board (CIOs of DoD, DHS, GSA); issued P-ATOs for high-visibility CSOs. **Dissolved May 2024**; replaced by the FedRAMP Board (M-24-15). Legacy P-ATOs remain valid (53 legacy-JAB certifications on the Marketplace as of Sept 30, 2026). |
| **Authorizing Official (AO)** | Senior agency official who accepts risk and grants an Agency ATO |
| **3PAO** | Third Party Assessment Organization; conducts independent security assessments. **CR26 note:** the "3PAO" term is retired in favor of **"FedRAMP Recognized independent assessor"** (REC ruleset, in force July 4, 2026: A2LA accreditation REC-IAS-ACC, full reassessment every 2 years REC-IAS-RAS, at least 2 Class B/C/D assessments every 2 years REC-IAS-ADA, no restoration after 2 revocations REC-FRP-DRD) |
| **CSP** | Cloud Service Provider; implements controls and maintains authorization/certification |
| **A2LA** | American Association for Laboratory Accreditation; accredits 3PAOs / independent assessors (accreditation remains the prerequisite for FedRAMP Recognized status under CR26) |

## FedRAMP Rev 5 Transition

FedRAMP transitioned from NIST 800-53 Rev 4 to Rev 5 baselines. Key changes:

- Adoption of NIST SP 800-53 Rev 5 and SP 800-53B as the control catalog and baseline source
- Introduction of the PT (PII Processing and Transparency) and SR (Supply Chain Risk Management) families
- Consolidation of some control enhancements and withdrawal of others
- Revised parameter values aligned with current threat landscape
- Updated SSP, SAR, and POA&M templates to reflect Rev 5 structure
- CSPs with existing authorizations must transition to Rev 5 baselines per FedRAMP-published timelines
- **CR26 note (NTC-0013):** FedRAMP removed most FedRAMP-assigned control parameters and nearly all FedRAMP-specific control guidance from the Rev5 baselines (now the CTL ruleset), effective with mandatory CR26 adoption (Jan 1, 2027). The parameter values in this file are therefore labeled as legacy Rev5 values.

## Baselines

FedRAMP defines four baselines derived from NIST SP 800-53B, with additional FedRAMP-specific controls and parameter constraints layered on top.

### Baseline Summary

| Baseline | FIPS 199 Impact | Total Controls (FedRAMP) | Use Case |
|----------|----------------|--------------------------|----------|
| **Low** | Low (C, I, A) | ~156 | Low-risk data; publicly available information |
| **Moderate** | Moderate (C, I, A) | 323 (181 base + 142 enhancements) | Controlled unclassified information (CUI); most federal workloads |
| **High** | High (C, I, A) | 410 (191 base + 219 enhancements; 87 net-new controls and 36 parameter changes vs. Moderate) | Law enforcement, emergency services, financial, health data |
| **LI-SaaS** | Low Impact SaaS | Tailored Low | Low-impact SaaS not storing PII beyond login credentials |

**CR26 mapping:** Low → Class B, Moderate → Class C, High → Class D (Class A is new, with no legacy equivalent). Marketplace impact mix as of Sept 30, 2026: Moderate 359 / High 94 / LI-SaaS 44 / Low 8.

### Baseline Selection Guidance

- **Moderate** is by far the most common baseline; roughly two-thirds of FedRAMP certified services are Moderate (359 of 533 as of Sept 30, 2026).
- **High** applies to systems processing high-impact data (FIPS 199 High for any of C, I, or A). Typical for law enforcement, healthcare, and financial systems.
- **Low** is appropriate for systems handling only publicly releasable data with minimal confidentiality needs.
- **LI-SaaS** (Low Impact SaaS) is a tailored Low baseline for SaaS products that store no PII beyond that needed for login. It uses the FedRAMP Low baseline with additional tailoring and has a streamlined authorization process.

### Control Family Distribution by Baseline

Counts include base controls plus enhancements. The **Moderate** column is enumerated from the bundled FedRAMP Moderate Rev5 OSCAL profile (`oscal/fedramp-moderate-rev5/`, total 323). The Low and High columns are approximate legacy figures that have not been re-verified against the FedRAMP profiles; use the FedRAMP baseline workbooks for authoritative Low/High membership. **PM and PT families are not in any FedRAMP baseline** (they are organization-level / Privacy-baseline families in SP 800-53B).

| Family | Low (approx.) | Moderate | High (approx.) |
|--------|-----|----------|------|
| AC (Access Control) | 17 | 43 | 52 |
| AT (Awareness & Training) | 4 | 6 | 6 |
| AU (Audit & Accountability) | 10 | 16 | 20 |
| CA (Assessment & Authorization) | 7 | 14 | 11 |
| CM (Configuration Management) | 7 | 27 | 18 |
| CP (Contingency Planning) | 6 | 23 | 16 |
| IA (Identification & Authentication) | 9 | 27 | 19 |
| IR (Incident Response) | 7 | 17 | 15 |
| MA (Maintenance) | 4 | 10 | 9 |
| MP (Media Protection) | 4 | 7 | 9 |
| PE (Physical & Environmental) | 12 | 19 | 22 |
| PL (Planning) | 4 | 7 | 6 |
| PS (Personnel Security) | 7 | 10 | 8 |
| RA (Risk Assessment) | 5 | 11 | 8 |
| SA (System & Services Acquisition) | 11 | 21 | 25 |
| SC (System & Communications) | 12 | 29 | 40 |
| SI (System & Information Integrity) | 9 | 24 | 19 |
| SR (Supply Chain Risk Mgmt) | 7 | 12 | 14 |

## FedRAMP-Specific Controls and Parameters

FedRAMP baselines are **not** identical to NIST SP 800-53B baselines. FedRAMP adds controls, control enhancements, and prescriptive parameter values beyond what NIST specifies. These additions reflect federal cloud-specific risk considerations.

### FedRAMP Additional Requirements Beyond NIST

| Area | FedRAMP Addition | Notes |
|------|------------------|-------|
| Integrated Inventory (CM-8) | CSP must maintain automated, real-time asset inventory (legacy: SSP Appendix M, Integrated Inventory Workbook) | Includes virtual assets, containers, serverless components |
| FIPS 140 Validation (SC-13) | Legacy Rev5: cryptographic modules must be **FIPS 140-3 validated (active CMVP validation; all FIPS 140-2 certificates have been Historical since Sept 22, 2026)**. **CR26 (CMU ruleset):** SC-13 guidance reads "Follow the FedRAMP Cryptographic Module Use rules" — providers MUST document every module and whether it is validated or an update stream (CMU-CSO-CMD); Class D MUST, Class C SHOULD, Classes A/B MAY use actively validated modules or their update streams (CMU-CSO-UVM); FIPS-140 encryption is expected only to protect sensitive data | FIPS 140-2 sunset: on Sept 22, 2026 NIST moved every 140-2 certificate to the CMVP Historical List (no extension or grandfathering). FedRAMP options (help.fedramp.gov, July 22, 2026): (1) move to an Active 140-3 module via Significant Change, (2) stay on the Historical module until its 140-3 successor validates, or (3) move early to an in-process 140-3 module; options 2 and 3 must be tracked as an open vulnerability (POA&M / Accepted Vulnerability) |
| US-Person Personnel (PS-6) | Personnel with access to federal data must be US persons or have equivalent background checks | Applies to privileged and non-privileged access |
| Data Location (SA-9(5)) | Legacy Rev5 value: information processing, information/data, and system services restricted to the U.S./U.S. territories or geographic locations where there is U.S. jurisdiction | Including backups, replicas, and DR sites |
| Incident Reporting (IR-6) | Legacy Rev5: report within 1 hour to CISA (formerly US-CERT, merged into CISA in 2023), FedRAMP, and affected agencies. **CR26 (IEC ruleset, grace to June 1, 2027):** initial report clocks scale by PAIN rating and class — Class D PAIN-3/4/5 15 minutes, PAIN-1/2 1 hour; Class C PAIN-3/4/5 1 hour, PAIN-2 24 hours, PAIN-1 1 business day; Class B 6 hours (PAIN-3–5) or 1 business day (PAIN-1–2); default PAIN-5 if not estimated. Providers report to FedRAMP (fedramp_security@fedramp.gov) and agency customers and publish to a trust center; agencies report to CISA | Stricter than most agency-specific policies |
| Penetration Testing (CA-8) | Legacy Rev5: annual penetration test by 3PAO or qualified independent entity (Pen Test Guidance v3.0, June 30, 2022, is the last final version; v4.0 was only a March 2024 draft). **CR26:** penetration testing is part of vulnerability detection and is subject to the VDR rules (no fixed frequency); CA-8(1)/(2) remain on the annual independent-assessment control list | CA-8 is in all FedRAMP baselines (NIST places it only in High) |
| Continuous Monitoring (CA-7) | Legacy Rev5: monthly OS/infrastructure, web application (incl. APIs), and database scans; annual independent-assessor scans and assessment. **CR26:** VDR/VER detection cadences (Rev5 MUST verify machine-based resources at least monthly; Class C SHOULD drift-prone 14 days / stable monthly / sample every 3 days; Class D 7 days / monthly / daily; non-machine resources every 3 months) | More prescriptive cadence than base NIST |
| CIS/CRM (SA-9) | Customer Responsibility Matrix required for all shared/inherited controls (legacy: SSP Appendix J, CIS and CRM Workbook) | Not in base NIST; FedRAMP-specific artifact. **CR26:** no CIS/CRM template — customer-facing guidance moves to the Secure Configuration Guide (SCG) ruleset |

### FedRAMP Parameter Values for Key Controls

FedRAMP prescribed specific values where NIST leaves organization-defined parameters (ODPs). The values below are **Legacy FedRAMP Rev5 values (in force until CR26 becomes mandatory Jan 1, 2027)**. **CR26 status:** per NTC-0013, FedRAMP removed most FedRAMP-assigned parameters from the Rev5 baselines; unless a CR26 ruleset pointer is given, the CR26 status is "no FedRAMP-assigned value" (the CSP defines and documents the value in its Security Decision Record). Authoritative legacy values: `oscal/fedramp-moderate-rev5/{family}.json`.

| Control | Parameter | Legacy FedRAMP Rev5 value (Moderate unless noted) | CR26 status |
|---------|-----------|---------------|-------------|
| **AC-2(2)** | Auto-disable of temporary/emergency accounts | No more than 96 hours from last use (Moderate); 24 hours (High) | No FedRAMP-assigned value |
| **AC-2(3)** | Disable accounts after inactivity | 90 days (Moderate); 35 days (High); 24 hours for user accounts under (a)–(c) | No FedRAMP-assigned value |
| **AC-7** | Consecutive invalid login attempts / lockout | **No FedRAMP-assigned value** — CSP defines limit, window, and lockout action "in alignment with NIST SP 800-63B". (The "3 attempts in 15 minutes / 30-minute lock" figures are Rev 4 leftovers and are not Rev5 values.) | No FedRAMP-assigned value |
| **AC-11** | Session lock after inactivity | 15 minutes of inactivity | No FedRAMP-assigned value |
| **AC-12** | Session termination | **No FedRAMP-assigned value** (the 30-minute non-privileged / 15-minute privileged figures come from IA-11 re-authentication guidance, AAL2/AAL3) | No FedRAMP-assigned value |
| **AU-4** | Audit storage capacity | Sufficient to retain per AU-11 requirements | No FedRAMP-assigned value |
| **AU-6** | Audit review frequency | At least weekly (both baselines) | No FedRAMP-assigned value |
| **AU-11** | Audit record retention | 90 days online plus retention in compliance with OMB M-21-31 and NARA (not "12 months / 18 months"). OMB M-26-14 (May 22, 2026) rescinded M-21-31; the new federal minimum is logs actively searchable for 6 months and retrievable for 12 months; the legacy FedRAMP text still names M-21-31 | No FedRAMP-assigned value |
| **CM-6** | Configuration baseline standard | DoD/DISA STIGs; CIS Benchmarks Level 2 where STIGs unavailable; custom baselines where CIS unavailable | "Follow the FedRAMP Secure Configuration Guide rules" (SCG ruleset) |
| **IA-4** | Identifier reuse prevention | At least 2 years before reuse (Moderate/High) | No FedRAMP-assigned value |
| **IA-5(1)** | Password minimum length / complexity / lifetime / history | **No FedRAMP-assigned minimum length or composition rules** — passwords per NIST SP 800-63B-4 (final July 31, 2025); legacy 14-character minimum applies only to non-MFA and emergency-use accounts. (The "12/15 characters, 60-day rotation, 24-password history" figures are Rev 4 leftovers.) | No FedRAMP-assigned value; phishing-resistant MFA required at all classes (IA-2/(1)/(2); TOTP/push/SMS do not qualify) |
| **RA-5** | Vulnerability scanning frequency | Monthly OS/infrastructure; monthly web applications (including APIs) and databases; container images scanned at build/deploy and monthly | VDR/VER detection cadences (required Dec 7, 2026; grace Mar 7, 2027) |
| **RA-5(d)** | Remediation timeline | High 30 / Moderate 90 / Low 180 days from date of discovery ("Critical" is not a FedRAMP category) | VDR-TFR-PVR: remediation by PAIN rating x reachability (e.g., Class D PAIN-5 internet-reachable 12 hours; ranges up to 192 days); KEVs per CISA due dates (VDR-TFR-KEV) |
| **SI-2** | Flaw remediation timeline | Within 30 days of release of updates (flat, not severity-tiered) | Subject to VDR/VER |
| **CP-9** | Backup frequency (user-level, system-level, documentation) | Daily incremental; weekly full (both baselines); backup testing annually (Moderate) / monthly (High) | No FedRAMP-assigned value |
| **CP-10** | Recovery time objective (RTO) | Defined by CSP per FIPS 199 impact (FedRAMP mandates no fixed RTO/RPO) | No FedRAMP-assigned value |
| **PS-4** | Termination — disable access | Within 4 hours (Moderate); 1 hour (High) | No FedRAMP-assigned value |
| **SC-10** | Network disconnect | 10 minutes privileged sessions; 15 minutes user sessions | No FedRAMP-assigned value |
| **X-1 policies** | Policy / procedure review | Policies every 3 years (Moderate) / annually (High); procedures annually | No FedRAMP-assigned value |

## Authorization Paths

### JAB Provisional Authorization (P-ATO)

The JAB P-ATO path was historically for high-visibility, cross-government CSOs expected to be used by multiple agencies. The JAB (CIOs of DoD, DHS, GSA) served as the AO and issued Provisional ATOs. **Note: The JAB was dissolved in May 2024 and replaced by the FedRAMP Board under OMB M-24-15. Existing P-ATOs remain valid (53 legacy-JAB certifications listed as of Sept 30, 2026). The process below describes the historical JAB path for reference only; the CR26 successor for sponsor-less certification is the 20x "Program" path (`fedramp-20x.md`).**

**Historical process steps (legacy):**

| Step | Activity | Typical Duration |
|------|----------|------------------|
| 1 | **FedRAMP Connect** -- CSP submits business case; FedRAMP prioritizes | 1-3 months |
| 2 | **Readiness Assessment** -- 3PAO conducts FedRAMP Ready assessment (FedRAMP Ready is legacy since July 28, 2026) | 4-6 weeks |
| 3 | **Full Security Assessment** -- 3PAO conducts comprehensive assessment per SAP | 3-6 months |
| 4 | **Authorization Package Submission** -- CSP submits SSP, SAR, POA&M to FedRAMP | 2-4 weeks |
| 5 | **FedRAMP Review** -- FedRAMP reviews package, issues review comments | 4-8 weeks |
| 6 | **JAB Review** -- JAB reviews risk posture and makes P-ATO decision | 2-4 weeks |
| 7 | **P-ATO Issuance** -- JAB issues P-ATO letter; CSO listed on Marketplace | 1 week |
| 8 | **Continuous Monitoring** -- Monthly ConMon deliverables to FedRAMP and leveraging agencies | Ongoing |

**Total typical timeline: 6-18 months**

### Agency Authorization (Agency ATO)

An individual agency sponsors the CSP and the agency AO issues the ATO. This is the more common path (452 of 533 certifications as of Sept 30, 2026). Under CR26 the Agency path exists only for the Rev5 certification type; FedRAMP stops accepting new Rev5 certifications June 11, 2027. Any certification application must first pass through the **Initial Implementation Phase** ("Implementing" marketplace listing, opened July 6, 2026).

**Process Steps (legacy Rev5):**

| Step | Activity | Typical Duration |
|------|----------|------------------|
| 1 | **Agency Sponsorship** -- Agency identifies need and agrees to sponsor CSP | 1-2 months |
| 2 | **Readiness Assessment** -- Optional FedRAMP Ready assessment by 3PAO (legacy since July 28, 2026 — see statuses below) | 4-6 weeks |
| 3 | **Full Security Assessment** -- 3PAO / FedRAMP Recognized independent assessor conducts assessment | 3-6 months |
| 4 | **Authorization Package** -- CSP prepares and submits package to agency | 2-4 weeks |
| 5 | **Agency Review** -- Agency security team reviews, may request remediation | 4-12 weeks |
| 6 | **ATO Decision** -- Agency AO issues ATO letter | 1-2 weeks |
| 7 | **FedRAMP Review** -- FedRAMP reviews package for listing on Marketplace | 4-8 weeks |
| 8 | **Marketplace Listing** -- CSO listed as **FedRAMP Certified** (CR26 term; formerly "Authorized") | 1 week |
| 9 | **Continuous Monitoring** -- Monthly ConMon to sponsoring agency and FedRAMP (legacy); under CR26, Ongoing Certification Reports every 3 months with quarterly reviews (CCM ruleset) | Ongoing |

**Total typical timeline: 6-14 months**

**Temporary Rev5 pipelines (opened Aug 10, 2026):** "Ready Conversion" (for FedRAMP Ready holders, who must convert by the later of annual-assessment expiry or Nov 17, 2026 per FRC-CSF-RDY) and "Lost Sponsor".

### JAB P-ATO vs. Agency ATO Comparison (historical)

| Factor | JAB P-ATO (dissolved May 2024) | Agency ATO |
|--------|-----------|------------|
| Authorizing Official | JAB (DoD, DHS, GSA CIOs) | Individual Agency AO |
| Scope of Authorization | Government-wide provisional | Single agency (reusable by others) |
| Selection Criteria | FedRAMP Connect prioritization | Agency sponsorship required |
| FedRAMP Review | Before authorization | After authorization |
| ConMon Reporting | To FedRAMP | To sponsoring agency + FedRAMP |
| Best For | High-demand, multi-agency CSOs | Agency-specific or niche CSOs |
| Rigor | Generally higher bar | Varies by agency |

Under CR26 the sponsor-less route is the 20x **Program** path (direct from FedRAMP); 28 Program certifications were listed as of Sept 30, 2026.

### DoD/DoW Path (Impact Levels)

Selling cloud to the Department of Defense/War is a distinct authorization path layered **on top of** FedRAMP: DISA grants a **DoW Provisional Authorization** per CSO at an Impact Level (IL2/IL4/IL5/IL6), composed of a FedRAMP baseline plus FedRAMP+ controls and CNSSI 1253 overlays. A FedRAMP Moderate authorization gets full reciprocity at IL2; IL4+ requires additional DISA assessment. → Full reference: `dod-impact-levels.md` and `mappings/nist-to-dod-il.md`.

## FedRAMP Marketplace, Connect, and Authorization Statuses

**FedRAMP Marketplace** (marketplace.fedramp.gov; machine-readable data at github.com/FedRAMP/marketplace-fedramp-gov-data) is the authoritative public registry of CSOs, their certification status, baseline/class, certification type, and assessor directory. As of Sept 30, 2026: **533 certified services** (452 Agency, 53 legacy JAB, 28 Program), of which 28 are 20x certified (14 Class B + 14 Class C); 68 FedRAMP Ready, 13 FedRAMP In Process, 48 Agency In Process.

**FedRAMP Connect** was the intake and prioritization process for CSPs seeking a JAB P-ATO (historical — the JAB was dissolved May 2024). CSPs submitted a business case demonstrating federal agency demand, FedRAMP Ready status, and unique government-wide applicability.

| Status | Meaning |
|--------|---------|
| **Implementing** (Initial Implementation Phase) | CR26 precursor to any certification application (opened July 6, 2026); Class B/C/D assessment must be scheduled within 2 years of the listing (MKT-IIP-DLA) |
| **FedRAMP Ready** (legacy) | 3PAO completed Readiness Assessment Report (RAR). **Legacy since July 28, 2026** — no new submissions; Ready holders must convert by the later of annual-assessment expiry or Nov 17, 2026 (FRC-CSF-RDY); legacy Ready listings removed Dec 31, 2027 |
| **In Process** | CSP is actively working toward certification with an agency sponsor (Rev5) or through the Program path (20x) |
| **FedRAMP Certified** (formerly "Authorized") | ATO/P-ATO granted or 20x certification issued; CSO is approved for federal use and listed on Marketplace. CR26 term is "Certified"; FedRAMP certifies the service, agencies still issue their own ATO/risk acceptance |
| **Revoked** | Certification withdrawn due to non-compliance or unacceptable risk |

**FedRAMP Ready** (legacy) required a 3PAO Readiness Assessment validating: well-defined system boundary, key controls implemented (not just planned), substantially complete SSP, manageable vulnerability scan posture, IR/CP plans in place, and FIPS 140-3 validated cryptographic modules (active CMVP validation; 140-2 certificates Historical since Sept 22, 2026).

## Key FedRAMP Documents and Artifacts

> **Legacy notice:** every legacy Rev5 template carries a June 23, 2026 LEGACY NOTICE and now lives at github.com/FedRAMP/docs-legacy. Under CR26 the SSP is replaced by the **FedRAMP Certification Package** (FRC-CSO-PKG/JSN: Certification Package Overview + Security Decision Record + KSI/rule artifacts in FedRAMP JSON schemas); Rev5 control documentation moves to Security Decision Records with statuses Implemented, Partially Implemented, Planned, Alternative Implementation, Not Applicable (SDR-CSF-CTF). The legacy SSP template structure is: 1 Introduction; 2 Purpose; 3 System Information; 4 System Owner; 5 Assignment of Security Responsibility; 6 Leveraged FedRAMP-Authorized Services; 7 External Systems and Services Not Having FedRAMP Authorization; 8 Illustrated Architecture and Narratives; 9 Services, Ports, and Protocols; 10 Cryptographic Modules Implemented for DAR and DIT; 11 Separation of Duties; 12 SSP Appendices List; controls in Appendix A; appendices A–Q (J = CIS and CRM Workbook, K = FIPS 199, M = Integrated Inventory Workbook, O = POA&M, P = SCRMP, Q = Cryptographic Modules Table).

| Document | Description | Owner |
|----------|-------------|-------|
| **System Security Plan (SSP)** | Comprehensive control implementation narratives, system architecture, data flows, boundary diagram, interconnections (legacy; CR26: Certification Package / SDR) | CSP |
| **Security Assessment Plan (SAP)** | Assessment scope, methodology, rules of engagement, test procedures | 3PAO |
| **Security Assessment Report (SAR)** | Assessment findings, risk ratings, risk exposure tables, recommendations | 3PAO |
| **Plan of Action & Milestones (POA&M)** | Open findings tracker with severity, remediation milestones, status, due dates (legacy SSP Appendix O; not a CR26 construct on the CSP side — CR26 uses **Accepted Vulnerability** (FRD-ACV) lists in each OCR; agencies still keep POA&Ms, VER-AGM-MAP) | CSP |
| **Customer Implementation Summary (CIS)** | Summary of customer-responsible controls for agency review (legacy Appendix J) | CSP |
| **Customer Responsibility Matrix (CRM)** | Detailed matrix showing CSP vs. customer responsibility for each control (legacy Appendix J; CR26 has no CIS/CRM template — SCG ruleset instead) | CSP |
| **Readiness Assessment Report (RAR)** | 3PAO assessment of CSP readiness for full assessment (legacy; FedRAMP Ready retired July 28, 2026) | 3PAO |
| **Significant Change Request (SCR)** | Formal request to modify authorized system boundary or architecture (legacy; CR26 replaces it with **Significant Change Notification (SCN)** — notification, not pre-approval) | CSP |
| **Deviation Request (DR)** | Request to accept risk for a finding that cannot be remediated within SLA (legacy; CR26: Accepted Vulnerability with written justification, VER-TFR-MAV) | CSP |
| **Continuous Monitoring Monthly Report** | Monthly executive summary with scan results, POA&M status, inventory changes (legacy; CR26: Ongoing Certification Report every 3 months, CCM-OCR-AVL, plus monthly human-readable vulnerability reporting, VER-TFR-MHR) | CSP |
| **Policies & Procedures (per family)** | Policy and procedure documents for each NIST 800-53 control family (AC, AT, AU, etc.) | CSP |
| **Digital Identity Worksheet** | Legacy SSP Appendix E; per NIST SP 800-63-3 (SP 800-63-4 series is now final, July 31, 2025); documents authentication assurance level selection | CSP |
| **Laws and Regulations Template** | Identifies applicable laws, regulations, and standards for the CSO (legacy Appendix L) | CSP |
| **OSCAL-formatted SSP** | Machine-readable SSP in NIST OSCAL format — **optional**; the OSCAL mandate was dropped (NTC-0009). FedRAMP JSON schemas (github.com/FedRAMP/schemas) are the required machine-readable format under CR26 (FRC-CSO-JSN): Classes A–C submit semi-structured text, Class D comprehensive machine-readable data | CSP |

## 3PAO / Independent Assessor Requirements

> **CR26 note:** the term "3PAO" is retired in CR26 in favor of **"FedRAMP Recognized independent assessor"** (REC ruleset, in force July 4, 2026). Recognition is layered on top of continuing A2LA accreditation (REC-IAS-ACC); assessors undergo a full reassessment every 2 years (REC-IAS-RAS), must perform at least 2 Class B/C/D assessments every 2 years (REC-IAS-ADA), and cannot be restored after 2 revocations (REC-FRP-DRD). "3PAO" is retained below because the legacy Rev5 documents use it.

### Accreditation

- 3PAOs must be accredited by the **American Association for Laboratory Accreditation (A2LA)** under the FedRAMP 3PAO program (CR26: A2LA accreditation remains the prerequisite for FedRAMP Recognized status).
- Accreditation is based on **ISO/IEC 17020:2012** (Conformity Assessment -- Requirements for Bodies Performing Inspection).
- A2LA conducts initial assessments and periodic surveillance assessments to maintain accreditation.
- 3PAOs must demonstrate competency in NIST SP 800-53, FedRAMP requirements, cloud architecture, and penetration testing.

### 3PAO Responsibilities

| Activity | Frequency | Deliverable |
|----------|-----------|-------------|
| Initial Full Assessment | Once (pre-authorization) | SAP, SAR, POA&M review |
| Annual Assessment | Annually (legacy: core controls + rotating subset; CR26 IVV: fixed list of ~80 Rev5 controls every year (IVV-CSF-AIA), all controls at least every 3 years as a ceiling (IVV-CSF-MCA), SHOULD assess all annually (IVV-CSF-PCA), negative-finding controls reassessed; 20x B/C/D: all KSIs annually (IVV-CSX-AIA)) | Updated SAR, POA&M validation |
| Readiness Assessment | Legacy (FedRAMP Ready retired July 28, 2026) | Readiness Assessment Report (RAR) |
| Significant Change Assessment | As needed (legacy SCR; CR26 SCN — transformative changes) | Focused SAR addendum |
| Penetration Testing | Annually (legacy, included in assessment); CR26: part of vulnerability detection under VDR | Penetration test report (within SAR) |

### 3PAO Independence

- The 3PAO must be organizationally independent from the CSP.
- The same 3PAO can perform consecutive annual assessments, but agencies may require rotation.
- 3PAO assessors must not have consulting relationships with the CSP they assess.

## Significant Change Request (SCR) Process (legacy) and CR26 Significant Change Notification (SCN)

> **CR26 (SCN ruleset; Rev5 required Jan 1, 2027, grace to June 1, 2027):** the SCR is replaced by **Significant Change Notification** — notification, not pre-approval (no default advance approval; only under a Corrective Action Plan). Routine recurring changes need no notification; **adaptive** changes are notified within 10 business days after completion; **transformative** changes require initial plans 30 business days before, final plans 10 business days before, notice 5 business days after completion and 5 business days after verification, with documentation updated within 30 business days; providers keep a 12-month change history in human-readable and JSON form.

A Significant Change Request (legacy Rev5) is required when a CSP makes material changes to an authorized CSO. Significant changes include:

- Changes to system boundary (adding/removing components, services, or interconnections)
- Changes to data flows or data types processed
- Migration to a new infrastructure provider or data center
- Major architecture changes (e.g., monolith to microservices)
- Changes to cryptographic implementations
- Changes to authentication mechanisms
- Addition of new external services or APIs

### SCR Process Steps

1. **CSP submits SCR** to the sponsoring agency (Agency ATO) or FedRAMP (legacy JAB P-ATO)
2. **AO/FedRAMP reviews** the SCR and determines assessment scope
3. **3PAO assesses** impacted controls (focused assessment, not full reassessment)
4. **CSP updates SSP** to reflect changes
5. **AO/FedRAMP approves** the change and updates authorization documentation

Changes that are **not** significant (routine patching, minor configuration changes, staff changes) require documentation in the SSP and monthly ConMon reports but do not require an SCR.

## Continuous Monitoring Requirements

FedRAMP continuous monitoring is more prescriptive than general NIST ISCM guidance. The cadence below is the **legacy Rev5 model**. **CR26:** vulnerability management follows the VDR/VER rulesets (Rev5 required Dec 7, 2026, grace to Mar 7, 2027; mandated by CISA BOD 26-04 per NTC-0014) and reporting moves to **Ongoing Certification Reports (OCR)** every 3 months (CCM-OCR-AVL) with a **Quarterly Review** 3–10 business days after each OCR (CCM-QTR-SAR; MUST for Class C/D, SHOULD Class B, MAY Class A per CCM-QTR-MTG); Rev5 CCM rules must be obtained by Jan 1, 2027, maintained by Apr 2, 2027, grace to Oct 1, 2027. Legacy Rev5 CSPs must adhere to the following cadence until then:

### Monthly Requirements

| Deliverable | Details |
|-------------|---------|
| Vulnerability Scans (OS/Infrastructure) | Authenticated scans of all OS-level assets; scan results in POA&M |
| Vulnerability Scans (Web Application) | DAST scans of all web applications, including APIs |
| Vulnerability Scans (Database) | Authenticated scans of all database instances |
| Vulnerability Scans (Container) | Scan container images at build/deploy and monthly in runtime |
| POA&M Update | Refresh all open items; add new findings; update milestones and statuses |
| Inventory Update | Hardware, software, and virtual asset inventory reconciliation |
| ConMon Summary Report | Executive summary of security posture, scan trends, POA&M aging |

### Quarterly Requirements

| Deliverable | Details |
|-------------|---------|
| Privileged User Access Review | Validate all privileged accounts remain appropriate |
| Network Scan / Architecture Review | Confirm no unauthorized changes to network topology |
| Hardware/Software Inventory Reconciliation | Full reconciliation against CM-8 inventory |

### Annual Requirements

| Deliverable | Details |
|-------------|---------|
| 3PAO Security Assessment | Independent assessment of a subset of controls (legacy: core controls plus a rotating ~1/3 subset — the 3-year full-coverage cycle is a ceiling, not a floor; CR26 IVV: fixed ~80-control annual list, all controls at least every 3 years, SHOULD assess all annually) |
| Penetration Test | Full-scope penetration test by 3PAO (legacy annual; CR26: part of vulnerability detection under VDR) |
| Contingency Plan Test | CP test and after-action report |
| Incident Response Plan Test | Tabletop or functional IR exercise |
| Security Awareness Training | All personnel with system access |
| SSP Update | Full refresh of SSP to reflect current state |
| Privacy Impact Assessment | Reassessment if PII processing has changed |

### POA&M Remediation Timelines

**Legacy FedRAMP Rev5 values (in force until CR26 becomes mandatory Jan 1, 2027; VDR/VER required for Rev5 from Dec 7, 2026):**

| Severity | Remediation SLA (RA-5(d), from date of discovery) | Deviation Request Required If Exceeded |
|----------|----------------|----------------------------------------|
| High | 30 days | Yes |
| Moderate | 90 days | Yes |
| Low | 180 days | Yes |

"Critical" is not a FedRAMP severity category (scanner "Critical" findings are treated as High). SI-2 flaw remediation is a flat 30 days from release of updates. Legacy POA&M template = SSP Appendix O (columns include POAM ID, Controls, Weakness Name/Description/Detector Source/Source Identifier, Asset Identifier, Point of Contact, Resources Required, Remediation Plan, Original Detection Date, Scheduled Completion Date, Status Date, Vendor Dependency fields, Original/Adjusted Risk Rating, Risk Adjustment, False Positive, Operational Requirement, Deviation Rationale, Supporting Documents, Comments, BOD 22-01 tracking/Due Date, CVE). BOD 22-01 KEV tracking is now under BOD 26-04.

Findings that cannot be remediated within SLA require a **Deviation Request (DR)** with a risk-based justification. The AO (historically the JAB) must approve the DR. Types of DRs include: Risk Adjustment, False Positive, Operational Requirement, and Vendor Dependency.

**CR26 (VDR/VER):** remediation timeframes derive from **PAIN rating x internet reachability** (VDR-TFR-PVR; e.g., Class D PAIN-5 internet-reachable 12 hours; ranges up to 192 days); KEVs per CISA due dates (VDR-TFR-KEV); anything not remediated within 192 days becomes an **Accepted Vulnerability** with written justification (VER-TFR-MAV; fields per VER-RPT-AVI: tracking ID, detection time/source, evaluation time, internet-reachable, likely-exploitable, PAIN rating, rationale), listed in each OCR. "Accepted Weakness" is not a CR26 term, and the POA&M is not a CR26 construct on the CSP side (agencies still keep POA&Ms, VER-AGM-MAP).

## Key Differences from Base NIST SP 800-53

| Dimension | NIST SP 800-53 Rev 5 | FedRAMP Rev 5 |
|-----------|----------------------|---------------|
| **Control Counts** | Low: ~150, Moderate: ~304, High: ~392 | Low: ~156, Moderate: 323, High: 410 |
| **Additional Controls** | Baseline per 800-53B only | Adds controls and enhancements beyond NIST baselines (e.g., CA-8 at all baselines); PM and PT families are in no FedRAMP baseline |
| **Parameters (ODPs)** | Organization-defined (flexible) | Legacy Rev5: prescriptive values mandated by FedRAMP; CR26 (NTC-0013): most FedRAMP-assigned values removed |
| **Assessment** | Organization selects assessor | Must use A2LA-accredited 3PAO (CR26: FedRAMP Recognized independent assessor) |
| **Authorization** | Agency AO per RMF | Legacy: JAB P-ATO or Agency ATO with FedRAMP oversight; CR26: FedRAMP Certification (Program or Agency path) plus agency ATO |
| **ConMon Cadence** | Organization-defined | Legacy: specific monthly/quarterly/annual requirements; CR26: VDR/VER + OCR every 3 months with quarterly reviews |
| **Artifact Templates** | No mandated templates | Legacy: FedRAMP-provided SSP, SAR, POA&M, CIS/CRM templates (LEGACY NOTICE June 23, 2026); CR26: Certification Package in FedRAMP JSON schemas |
| **Remediation SLAs** | Organization-defined | Legacy: 30/90/180 days by severity (High/Moderate/Low; "Critical" is not a FedRAMP category); CR26: PAIN x reachability timeframes (VDR-TFR-PVR) |
| **Data Sovereignty** | No federal requirement | Legacy SA-9(5): U.S./U.S. territories or U.S.-jurisdiction locations |
| **Cryptography** | FIPS 140 "consistent with" | FIPS 140-3 validated modules (active CMVP validation; 140-2 certificates Historical since Sept 22, 2026); CR26 CMU: document all modules, Class D MUST / Class C SHOULD use actively validated modules |
| **Incident Reporting** | Per organizational policy | Legacy: CISA/FedRAMP/agencies within 1 hour; CR26 IEC: PAIN- and class-based clocks (Class D 15 minutes for PAIN-3/4/5), reported to FedRAMP and agency customers |
| **Supply Chain** | SR family selected per baseline | Enhanced supply chain requirements for cloud context |
| **Marketplace/Reuse** | No reuse mechanism | "Do once, use many" via FedRAMP Marketplace |
| **OSCAL** | Encouraged | Optional — mandate dropped (NTC-0009); FedRAMP JSON schemas are the required machine-readable format (FRC-CSO-JSN) |

## References

- NIST SP 800-53 Rev 5: Security and Privacy Controls for Information Systems and Organizations
- NIST SP 800-53B: Control Baselines for Information Systems and Organizations
- NIST SP 800-37 Rev 2: Risk Management Framework for Information Systems and Organizations
- NIST SP 800-63-4 series: Digital Identity Guidelines (final July 31, 2025; supersedes SP 800-63-3)
- NIST SP 800-88 Rev. 2: Media Sanitization (final Sept 26, 2025; Rev 1 withdrawn)
- FedRAMP Authorization Act (44 U.S.C. 3607-3616); OMB M-24-15 (Modernizing FedRAMP, July 2024)
- FedRAMP Consolidated Rules for 2026 (CR26): https://www.fedramp.gov/2026/ (machine-readable rules: github.com/FedRAMP/rules)
- FedRAMP Security Assessment Framework (SAF) (legacy)
- FedRAMP Continuous Monitoring Strategy Guide (legacy)
- FedRAMP Significant Change Request Form and Guidance (legacy; CR26: SCN ruleset)
- FedRAMP Initial Authorization Package Checklist (legacy)
- FedRAMP legacy templates and OSCAL resources: github.com/FedRAMP/docs-legacy (github.com/GSA/fedramp-automation no longer exists); CR26 submission schemas: github.com/FedRAMP/schemas
- FedRAMP FIPS 140-2 sunset guidance: help.fedramp.gov article 53386638354843 (July 22, 2026)
