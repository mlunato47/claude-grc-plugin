# FedRAMP 20x & Consolidated Rules for 2026 (CR26)

## Overview

**FedRAMP 20x** is the modernized, automation-first FedRAMP authorization model announced March 24, 2025: machine-readable evidence and continuous validation of **Key Security Indicators (KSIs)** replace narrative SSPs and point-in-time annual assessments. As of the **June 2026 Consolidated Rules release, 20x is generally available** — no longer a pilot — and operates alongside the legacy Rev5 path during a transition running until at least December 31, 2028.

**CR26 = the FedRAMP Consolidated Rules for 2026** — the program's first consolidated ruleset, merging the 2025-era "25.x" standards releases and the outcomes of RFC-0019–0031 into a single declarative rule system.

| CR26 fact | Value |
|-----------|-------|
| Launched | **June 24, 2026** (announcement blog June 25; public preview May 4, 2026) |
| Effective / optional early adoption | July 4, 2026 |
| **Mandatory (enforced) for all stakeholders** | **January 1, 2027** (including existing Rev5 certification holders) |
| Valid through | December 31, 2028 (stable planning window) |
| Structure | 246 rules across 17 rulesets + 46 KSIs (10 themes) + 80 definitions (FRD) + rebuilt Rev5 control guidance (CTL) — counts per dataset **2026.10.05.01 (Oct 5, 2026 release: PAIN N0 added; CMU-CSO-UVM note that new algorithms in update streams are outside validated scope; FRC-CSO-JSN web-compatibility clarification)** (site changelog 2026.09.22.01) |
| Rule format | Plain-language RFC-2119 statements (MUST/SHOULD/MAY) with stable IDs `SET-SUBSET-KEY` (e.g., `VDR-CSO-DET`), published as machine-readable JSON |
| Versioning | Date-based dataset releases (e.g., 2026.10.05.01 (Oct 5, 2026 release: PAIN N0 added; CMU-CSO-UVM note that new algorithms in update streams are outside validated scope; FRC-CSO-JSN web-compatibility clarification)); check the changelog — CR26 has been revised several times since launch |

**Legal basis:** FedRAMP Authorization Act (44 USC 3607–3616, FY2023 NDAA) + OMB Memorandum M-24-15 ("Modernizing FedRAMP," July 2024). CR26's vulnerability standards also implement **CISA BOD 26-04**.

## Terminology Changes (know these — they invalidate older vocabulary)

| Old term | CR26 term |
|----------|-----------|
| FedRAMP Authorized / Authorization | **FedRAMP Certified / Certification** (FedRAMP certifies the *service*; agencies still issue their own ATO/risk acceptance) |
| Impact levels (Low/Moderate/High) as labels | **Certification Classes A–D** |
| 3PAO | **FedRAMP Recognized independent assessor** (REC ruleset, in force July 4, 2026 — recognition layered on top of continuing A2LA accreditation (REC-IAS-ACC), full reassessment every 2 years (REC-IAS-RAS), at least 2 Class B/C/D assessments every 2 years (REC-IAS-ADA), no restoration after 2 revocations (REC-FRP-DRD)) |
| SSP | **FedRAMP Certification Package** (FRC-CSO-PKG/JSN) = **Security Decision Record (SDR)** + **Certification Package Overview (CPO)** + KSI/rule artifacts; Rev5 control statuses in the SDR: Implemented, Partially Implemented, Planned, Alternative Implementation, Not Applicable (SDR-CSF-CTF) |
| Monthly ConMon deliverables / POA&M | **VDR/VER** vulnerability standards + **Ongoing Certification Reports (OCR)** every 3 months (CCM-OCR-AVL) with Quarterly Reviews (MUST Class C/D, SHOULD B, MAY A — CCM-QTR-MTG; 3–10 business days after the OCR — CCM-QTR-SAR). The POA&M is not a CR26 construct on the CSP side (agencies still keep POA&Ms, VER-AGM-MAP) |
| Accepted Weakness / Deviation Request | **Accepted Vulnerability** (FRD-ACV: not remediated within the VDR maximum period; listed in each OCR). "OAR" is likewise not a CR26 term — it is OCR |
| Significant Change Request | **Significant Change Notification (SCN)** — notification, not pre-approval |
| SSAD / Authorization Data Sharing | **Certification Data Sharing (CDS)** via provider **Trust Centers** |
| FedRAMP PMO | **FedRAMP** (the PMO still exists in GSA, but the documents say "FedRAMP") |
| FedRAMP Ready | Legacy as of **July 28, 2026** (no new submissions; Ready holders must convert by the later of annual-assessment expiry or Nov 17, 2026 (FRC-CSF-RDY); legacy Ready removed Dec 31, 2027; Ready Conversion and Lost Sponsor pipelines opened Aug 10, 2026) |
| (pre-application) | **Initial Implementation Phase** — "Implementing" marketplace listing (opened July 6, 2026), a required precursor to any certification application; B/C/D assessment must be scheduled within 2 years of listing (MKT-IIP-DLA) |

## The Certification Model: Type + Path + Class

A **Certification Profile** = **Type** (20x or Rev5) + **Path** (Program — direct from FedRAMP, no agency sponsor — or Agency, Rev5-legacy only) + **Class** (A–D, per definition FRD-CCL: "minimal assurance at Class A to significant assurance at Class D").

| Class | Legacy mapping | Available under | Notes |
|-------|----------------|-----------------|-------|
| **A** | **New — no legacy equivalent** (minimal assurance) | 20x only | Entry tier leveraging **Approved Alternative Security Frameworks** (FRC-CLA-ASF): SOC 2 Type II, GovRAMP (any impact level), or FedRAMP Rev5 incl. FedRAMP Ready (any historical impact level), completed within the past 12 months — plus a reduced mandatory rule set incl. **7 named KSIs**, VDR detection, incident and trust-center rules; ongoing assessment cadence is carried primarily by the underlying framework (the FedRAMP-side annual IVV is a MAY for Class A). Agencies SHOULD NOT use a Class A service for more than 12 months unless it is pursuing B/C/D (AGU-USE-CLA); a B/C/D assessment must be scheduled within 2 years of the Initial Implementation listing (MKT-IIP-DLA). Pipeline opened Aug 3, 2026. |
| **B** | LI-SaaS / Low | 20x ("20x Low") and Rev5 | Full ruleset + full KSI set under 20x; pipeline opened Aug 31, 2026 |
| **C** | Moderate | 20x ("20x Moderate") and Rev5 | Largest tier — Moderate ≈ two-thirds of currently certified services (359 of 533); pipeline opened Aug 31, 2026 |
| **D** | High | **Rev5 only today** | 20x Class D is **pilot only**: RFC-0033/0034 open Sept 9–Oct 9, 2026; pilot FY27 Q1–Q2 (Phase 4); gate = CR26-compliant 20x Class C certification before Dec 1, 2026; applications Dec 1–4, 2026; max 10 participants; final submissions Mar 17, 2027 |

Classes reflect **assessment scope and assurance level, not product quality**; higher classes primarily demand faster response and tighter reporting cadence. The letter scheme was chosen partly to end the collision between FedRAMP Low/Moderate/High and DoD Impact Level numbering.

**Class A's 7 required KSIs:** KSI-CMT-LMC, KSI-CNA-RNT, KSI-CED-RAT, KSI-IAM-AAM, KSI-IAM-APM, KSI-INR-RIR, KSI-SVC-SIN.

## Key Security Indicators (KSIs) — 46 across 10 themes

KSIs are measurable security outcomes that CSPs prove continuously through automated verification/validation, replacing control-narrative documentation. Under CR26 each KSI uses a mnemonic ID (`KSI-THEME-KEY`, e.g., KSI-IAM-APM "Adopting Passwordless Methods"), carries an **explicit NIST 800-53 control mapping** (a `controls` array in the machine-readable rules), and defines 5 standard artifact expectations (explanation, cycle, verification, automation verification, validation).

| Theme | Name | KSIs |
|-------|------|------|
| CED | Cybersecurity Education | 1 |
| CMT | Change Management | 4 |
| CNA | Cloud Native Architecture | 8 |
| IAM | Identity and Access Management | 6 |
| INR | Incident Response | 3 |
| MLA | Monitoring, Logging, and Auditing | 5 |
| PIY | Policy and Inventory | 5 |
| RPL | Recovery Planning | 4 |
| SCR | Supply Chain Risk | 2 |
| SVC | Service Configuration | 8 |

**Evolution:** initial standard (25.05A, May 30, 2025) = **51** KSIs in 10 themes; the Phase 2 release (25.11A, Nov 18, 2025) listed **72** IDs in 11 themes (adding the 11-KSI AFR process theme while retiring 7 superseded CSP KSIs → 65 active); 25.12A (Dec 29, 2025) rewrote for clarity and retired 4 more (→ 61 active); **CR26 cut the set to 46 in 10 themes** — the AFR theme (Authorization by FedRAMP) was dropped with its process subject matter absorbed into the FRR rulesets, and TPR (Third-Party Information Resources) gave way to the SCR theme plus MAS third-party rules (FedRAMP published no formal crosswalk; destinations per analysis). IDs changed from numbers to mnemonics — pre-CR26 KSI IDs do not resolve against the current set.

**Validation in practice:** continuous pipelines emit structured evidence (cloud control-plane APIs, IaC state, scanner output) into a machine-readable certification package; agencies and assessors consume it via the provider's Trust Center; assessors subscribe to validation events rather than re-creating evidence annually.

## VDR — Vulnerability Detection and Response

CR26 ruleset (18 rules; applies fully at classes B/C/D across both 20x and Rev5 — Class A carries a detection subset) governing *finding and fixing* vulnerabilities. Implements CISA BOD 26-04.

- Systematic, persistent, prompt detection → evaluation → prioritization → mitigation → remediation; security-control failures are treated as vulnerabilities; detection re-run after changes; persistent drift detection.
- **KEV** (CISA Known Exploited Vulnerabilities) avoidance and remediation duties.
- Risk triage concepts: **LEV/NLEV** (likely exploitable or not), **IRV/NIRV** (internet-reachable or not — broader than "internet-facing": relay/chained paths count).
- **Mitigation ≠ remediation** — a mitigated vulnerability still exists until remediated; the standard measures how fast *potential adverse impact* shrinks rather than imposing only fixed CVSS-based clocks. Timeframes scale by class (higher class = faster; industry summaries cite, e.g., likely-exploitable catastrophic findings at Class D in hours, Class B in days).
- Machine verification/validation cadence scales by class (VDR-TFR-MVX: 20x Class B every 7 days and Class C every 3 days as MUSTs, Class A monthly as SHOULD; Rev5 MUST verify machine-based resources at least monthly per VDR-TFR-MVF). Detection cadences: Class C SHOULD detect on drift-prone resources every 14 days / stable resources monthly / sample every 3 days; Class D 7 days / monthly / daily; non-machine resources every 3 months.
- **Remediation timeframes** derive from PAIN rating x reachability (VDR-TFR-PVR; e.g., Class D PAIN-5 internet-reachable 12 hours; ranges up to 192 days); KEVs per CISA due dates (VDR-TFR-KEV). Anything not remediated within 192 days becomes an **Accepted Vulnerability** with written justification (VER-TFR-MAV).
- Penetration testing is part of vulnerability detection and subject to VDR (CR26 CA-8 guidance).

**Dates:** optional from July 4, 2026; **required to obtain/maintain certification by December 7, 2026** (mandated by CISA BOD 26-04, NTC-0014); corrective-action grace to **March 7, 2027**, then loss of certification. Legacy Rev5 values these replace: RA-5(d) high 30 / moderate 90 / low 180 days from discovery; SI-2 flat 30 days from release; monthly OS/infra, web app (incl. APIs), and database scans; annual independent-assessor scans; "Critical" is not a FedRAMP category.

## VER — Vulnerability Evaluation and Reporting

Companion CR26 ruleset (23 rules; classes B/C/D) split out of VDR: it governs *evaluating federal-customer impact and reporting it*.

- Evaluate exploitability and internet reachability; **assume exploits are automatable by default** (VER-EVA-AIA).
- Rate every vulnerability's **Potential Agency Impact N-rating (PAIN): N0 → N5** (VER-EVA-EPA; N0, added in dataset 2026.10.05.01 on Oct 5, 2026, means exploitation is extremely unlikely to have any adverse agency effect; N1 minimal; N5 debilitating effect on multiple agencies). Internet-reachable, likely-exploitable N4/N5 findings are handled as security incidents.
- Persistent reporting to all necessary parties, monthly human-readable activity reports (VER-TFR-MHR), accepted-vulnerability marking (fields per VER-RPT-AVI: tracking ID, detection time/source, evaluation time, internet-reachable, likely-exploitable, PAIN rating, rationale), responsible public disclosure.
- Same effective dates as VDR (required Dec 7, 2026; grace to Mar 7, 2027). Together VDR + VER replace the legacy monthly-scan-plus-POA&M ConMon model.

## The Full CR26 Ruleset Catalog

All at `https://www.fedramp.gov/2026/reference/<slug>/`. Legacy 25.x predecessor in parentheses.

| ID | Name (slug) | One-liner |
|----|-------------|-----------|
| AFC | Addressing FedRAMP Communication (`addressing-fedramp-communication`; was FSI) | Security-contact inbox, response-time tests |
| AGU | Agency Use (`agency-use`) | Agency obligations — placeholder status |
| CCM | Collaborative Continuous Monitoring (`collaborative-continuous-monitoring`) | Ongoing Certification Reports (OCR), quarterly reviews |
| CDS | Certification Data Sharing (`certification-data-sharing`; was ADS/SSAD) | Trust Centers, public info, agency access |
| CMU | Cryptographic Module Use (`cryptographic-module-use`; was UCM) | Risk-based (preferably validated) crypto module selection |
| CPO | Certification Package Overview (`certification-package-overview`) | Concise offering overview replacing the base SSP |
| FRC | FedRAMP Certification (`fedramp-certification`) | How offerings obtain/maintain certification; Class A rules; class changes |
| IEC | Incident Evaluation and Communication (`incident-evaluation-and-communication`; was ICP) | Reportability evaluation; Initial/Ongoing/Final Incident Reports |
| IVV | Independent Verification and Validation (`independent-verification-and-validation`; was PVA) | Independent assessment expectations, annual cadence |
| MAS | Minimum Assessment Scope (`minimum-assessment-scope`) | Boundary/scope definition, third-party resources |
| MKT | Marketplace Listing (`marketplace-listing`) | Listing eligibility and machine-readable listing data |
| REC | FedRAMP Recognition (`fedramp-recognition`) | FedRAMP Recognized status for assessors (on top of continuing A2LA accreditation) |
| SCG | Secure Configuration Guide (`secure-configuration-guide`; was RSC) | Customer-facing secure-config guidance |
| SCN | Significant Change Notification (`significant-change-notification`) | Adaptive/transformative/routine-recurring change categories; notification not pre-approval |
| SDR | Security Decision Record (`security-decision-record`) | Persistently maintained record of security decisions — the SSP's replacement |
| VDR | Vulnerability Detection and Response (`vulnerability-detection-and-response`) | See above |
| VER | Vulnerability Evaluation and Reporting (`vulnerability-evaluation-and-reporting`) | See above |
| KSI | Key Security Indicators (`key-security-indicators`) | See above |
| CTL | Rev5 Control Guidance (`rev5-control-guidance`) | Rebuilt Rev5 guidance per NTC-0013 |
| FRD | Definitions (`/2026/definitions/`) | 80 controlled terms as of dataset 2026.10.05.01 (Oct 5, 2026 release: PAIN N0 added; CMU-CSO-UVM note that new algorithms in update streams are outside validated scope; FRC-CSO-JSN web-compatibility clarification) (PAIN, IRV, KEV, LEV, OCR, SDR, Accepted Vulnerability, Trust Center, …) |

Class/type bundles: `reference/20x/{a,b,c}/` and `reference/rev5/{b,c,d}/`; full index at `reference/complete-rulesets/`. Note: there is no document named SSAD or CRS in CR26 (2025-era names people may still search for) — that content became CDS and CCM/OCR.

## Frequently Asked Details (and where the authoritative answers live)

- **Submission formats — OSCAL vs FedRAMP JSON schemas.** The 20x certification package (CPO + SDR + KSI evidence + rule artifacts) is machine-readable per **FedRAMP's own JSON schemas** (github.com/FedRAMP/schemas; FRC-CSO-JSN) — not OSCAL. The RFC-0024 OSCAL-mandate idea was dropped (NTC-0009): Classes A–C submit semi-structured text, Class D comprehensive machine-readable data; OSCAL is optional. Agency tooling must be able to ingest both OSCAL and JSON (AGU). Legacy templates and OSCAL resources live at github.com/FedRAMP/docs-legacy (github.com/GSA/fedramp-automation no longer exists). Do not tell any CR26 applicant they need OSCAL.
- **Cryptography / FIPS (CMU).** The CMU ruleset (optional July 4, 2026; required Jan 1, 2027; Rev5 grace to June 1, 2027) takes a **risk-based approach to cryptographic module selection, preferring validated modules** — a posture shift from legacy hard FIPS-validation gating: providers MUST document every module and whether it is validated or an update stream (CMU-CSO-CMD); Class D MUST, Class C SHOULD, Classes A/B MAY use actively validated modules or their update streams (CMU-CSO-UVM). CR26 SC-13 guidance reads "Follow the FedRAMP Cryptographic Module Use rules," and CR26 states FIPS-140 encryption is only expected to protect sensitive data. **FIPS 140-2 sunset (passed):** on Sept 22, 2026 NIST moved every FIPS 140-2 certificate to the CMVP Historical List (sunset date Sept 21, 2026); no extension or grandfathering. Historical modules may keep running in existing systems under documented risk acceptance but must not be cited for new procurements. FedRAMP's options (help.fedramp.gov article 53386638354843, July 22, 2026): (1) move to an Active FIPS 140-3 module via the Significant Change process, (2) stay on the Historical module until its 140-3 successor is validated, or (3) move early to a 140-3 module still in CMVP process — options 2 and 3 must be tracked as an open vulnerability (POA&M / Accepted Vulnerability). Fetch the CMU ruleset for the exact current rules before advising.
- **Penetration testing and assessment specifics.** Penetration testing is treated as **part of vulnerability detection under VDR** (FedRAMP's CTL guidance for CA-8 states this explicitly; legacy Pen Test Guidance v3.0, June 30, 2022, was the last final version). Assessment scope lives in **MAS** (rescinds all previous boundary guidance: scope = all information resources likely to handle federal customer data or impact its CIA, MAS-CSO-IIR; metadata in scope only if IIR applies, MAS-CSO-MDI; document information flows, MAS-CSO-FLO; third-party resources in scope only if they handle/affect federal data and must be documented with usage, justification, mitigations, and compensating controls, MAS-CSO-TPR — no prohibition and no FedRAMP approval step; no explicit diagram requirement). Independent-assessment expectations live in **IVV** (Rev5: fixed list of ~80 controls assessed every year, IVV-CSF-AIA; all controls at least every 3 years as a ceiling, IVV-CSF-MCA; SHOULD assess all annually, IVV-CSF-PCA; negative-finding controls reassessed; 20x B/C/D: all KSIs annually, IVV-CSX-AIA). Do not assume the legacy annual-3PAO-pen-test or one-third-rotation model carries over.
- **Incident reporting clocks (IEC; finalized in CR26, replacing the RFC-0031 draft; Rev5 grace to June 1, 2027).** PAIN = Potential Agency Impact N-rating (N1 minimal effect on 1+ agencies … N5 debilitating effect on more than one agency; default PAIN-5 if not estimated). Initial report: Class D — PAIN-3/4/5 within 15 minutes, PAIN-2 and PAIN-1 within 1 hour (ongoing every 3h/6h/24h; final 3h/6h/24h after recovery); Class C — PAIN-3/4/5 1 hour, PAIN-2 24 hours, PAIN-1 1 business day; Class B — 6 hours (PAIN-3–5) or 1 business day (PAIN-1–2). Providers report to FedRAMP (fedramp_security@fedramp.gov) and agency customers and publish to a trust center; agencies report to CISA. Legacy Rev5: one hour to CISA (formerly US-CERT), FedRAMP, and agencies. Fetch the ruleset for the current clocks.
- **Significant changes (SCN; Rev5 grace to June 1, 2027).** Routine recurring changes need no notification; adaptive changes are notified within 10 business days after completion; transformative changes require initial plans 30 business days before, final plans 10 business days before, notice 5 business days after completion and 5 business days after verification, docs updated within 30 business days; keep a 12-month history in human-readable and JSON form; no default advance approval (only under a Corrective Action Plan).
- **SDR contents.** The **SDR** ruleset defines what the Security Decision Record must contain and how it is maintained/verified (Rev5 control statuses: Implemented, Partially Implemented, Planned, Alternative Implementation, Not Applicable — SDR-CSF-CTF) — fetch it before drafting one.
- **VDR/VER timeframes.** The authoritative per-class detection/evaluation/remediation clocks are the **VDR-TFR-\*** and **VER-TFR-\*** rules in the machine-readable dataset; the examples in this file are industry summaries, not the rule text.

## For Agencies

- Certification ≠ ATO: agencies still perform their own risk acceptance. Industry analyses report CR26 restricts agencies from layering duplicate requirements on certified offerings.
- Agencies consume certification data through the provider's **Trust Center** (CDS ruleset — public info plus agency-access provisions) and **Ongoing Certification Reports** with quarterly reviews (CCM ruleset).
- Formal agency obligations live in the **AGU** ruleset — placeholder status at CR26 launch, so check it live before citing agency-side rules.

## Rev5 Coexistence and Sunset

- Rev5 continues as a legacy Certification Type (classes B/C/D; the Agency/sponsor path is Rev5-only) under CR26's Rev5 rulesets.
- **NTC-0013**: FedRAMP removed most FedRAMP-assigned control parameters and nearly all FedRAMP-specific control guidance from the Rev5 baselines (now the CTL ruleset), effective with mandatory adoption.
- **VDR and VER apply to Rev5 providers too** (required Dec 7, 2026).
- Timeline: **Jan 1, 2027** CR26 mandatory for everyone. Rev5 adoption is **per ruleset**: VDR/VER required Dec 7, 2026 (grace to Mar 7, 2027); MAS/SCN/FRC/IVV/CMU/IEC required Jan 1, 2027 (IEC/CMU/SCN grace to Jun 1, 2027); CCM ConMon rules obtain Jan 1, 2027 / maintain **Apr 2, 2027** / grace to Oct 1, 2027; CPO Rev5 grace to Jul 1, 2027; SDR Rev5 maintain Aug 1, 2027; CDS grace to Feb 1, 2028; SCG in force since Mar 1, 2026; AFC Security Inbox mandatory since Jan 5, 2026 (grace ended Jul 1, 2026). NTC-0013's Rev5 control-guidance changes adopt at the first independent assessment after Jan 1, 2027. **Jun 11, 2027** last new Rev5 certifications; **all CR26 grace periods expire Feb 1, 2028**; existing Rev5 certifications remain active until **at least December 31, 2028** ("unless FedRAMP is otherwise directed").
- Temporary Rev5 Class B/C pipelines (Ready Conversion + Lost Sponsor only) opened Aug 10, 2026; Ready holders must convert by the later of annual-assessment expiry or Nov 17, 2026 (FRC-CSF-RDY).

**Transitioning from Rev5 to 20x:** there is no automatic conversion — a Rev5 provider files a new 20x application (Program path). Two hooks ease the move: a FedRAMP Rev5 certification completed within the past 12 months qualifies as an **Approved Alternative Security Framework for Class A** (a fast onramp while building full KSI automation), and each KSI's official `controls` array is the sanctioned crosswalk from Rev5 control implementations to KSI evidence. Rev5 providers continue their existing monthly ConMon deliverables until the Rev5 CCM rules take hold (mandatory to maintain certification April 2, 2027; grace to October 1, 2027) — with VDR/VER layering on from December 7, 2026 regardless.

## Program Status (as of September 30, 2026)

| Phase | Scope | Status |
|-------|-------|--------|
| 1 | Low pilot (Apr–Sep 2025) | Complete — 26 submissions, first certifications July 2025 |
| 2 | Moderate pilot (Nov 2025–Mar 2026) | Complete — first cohort certified Mar 6, 2026 |
| 3 | **General availability** | **Current** — "no longer just a pilot" (June 2026); Initial Implementation Phase opened July 6; Class A pipeline opened Aug 3, Class B/C Aug 31, 2026 |
| 4 | 20x Class D (High) pilot | **Started** — RFC-0033/0034 open Sept 9–Oct 9, 2026; pilot FY27 Q1–Q2; gate = CR26-compliant 20x Class C certification before Dec 1, 2026; applications Dec 1–4, 2026; max 10; final submissions Mar 17, 2027 |
| 5 | Rev5 sunset activities | Estimated FY27 Q3–Q4 (last new Rev5 certifications Jun 11, 2027) |

Marketplace data (Sept 30, 2026): **28 FedRAMP 20x certified services** — 14 at 20x Low (Class B) + 14 at 20x Moderate (Class C); 14 still flagged "pilot" pending CR26 adoption by Mar 7, 2027 — out of **533** FedRAMP certified services (452 Agency, 53 legacy JAB, 28 Program; impact mix Moderate 359 / High 94 / LI-SaaS 44 / Low 8). Also listed: 68 FedRAMP Ready, 13 FedRAMP In Process, 48 Agency In Process.

Program events: FedRAMP Director Pete Waterman was placed on leave July 31, 2026 and reinstated the week of Aug 26, 2026; FedRAMP Day was held Sept 30, 2026. Post-CR26 RFCs: 0032 (Offerings By Government, Aug 6–Sept 8, 2026), 0033/0034 (Phase 4 / Class D, TAG). Notices run through NTC-0016.

## Practitioner Watch Items (industry analysis, as of September 2026)

1. **MAS scope judgment calls** — what counts as in-scope (scanners, IdPs) is less prescriptive than the old boundary; cautious scoping can be expensive.
2. **Dec 7, 2026 VDR/VER deadline** is realistic for automated cloud-native shops and aggressive for everyone else — it hits Rev5 providers as well.
3. **SDR bloat risk** — the community's worry is the SSP replacement re-growing into a 300-page artifact.
4. **Agency acceptance is the execution risk** — CR26 reportedly restricts agencies from layering duplicate requirements, but certification ≠ ATO; agencies still make their own risk decisions.
5. **Rule churn** — CR26 was revised several times within weeks of launch; always check the changelog/dataset version before citing a rule verbatim.
6. **DoD/DoW reciprocity** — the DISA CSP SRG (see `dod-impact-levels.md`) keys reciprocity to FedRAMP baselines and P-ATOs; check current DISA guidance for how 20x certifications and classes map to DoW PA reciprocity before advising on it.

## Public CR26 Documentation Index (for live lookups)

When a question needs authoritative, current detail (exact rule text, KSI wording, dates), fetch these rather than relying on this summary. **FedRAMP explicitly directs automated agents to the machine-readable repos below instead of parsing the website HTML.**

| Resource | URL |
|----------|-----|
| **Machine-readable rules (source of truth)** | https://raw.githubusercontent.com/FedRAMP/rules/main/fedramp-consolidated-rules.json (repo: https://github.com/FedRAMP/rules) |
| **LLM-optimized markdown mirror** | https://github.com/FedRAMP/2026-markdown |
| CR26 home | https://www.fedramp.gov/2026/ |
| Rules structure guide | https://www.fedramp.gov/2026/rules/ |
| Definitions (FRD) | https://www.fedramp.gov/2026/definitions/ |
| Timeline | https://www.fedramp.gov/2026/timeline/ |
| Changelog / dataset versions | https://www.fedramp.gov/2026/changelog/ |
| Ruleset reference index | https://www.fedramp.gov/2026/reference/ (individual: `/2026/reference/<slug>/`; bundles: `/2026/reference/20x/{a,b,c}/`, `/2026/reference/rev5/{b,c,d}/`) |
| Responsibilities by role | https://www.fedramp.gov/2026/responsibilities/{fedramp,agencies,providers,assessors,advisors}/ |
| Notices (NTC-0001–0016) | https://www.fedramp.gov/notices/ — key: 0004 (classes/CR26), 0007 (Class A / alternative frameworks, 2-year window), 0009 (OSCAL mandate dropped), 0012 (incident comms), 0013 (Rev5 baselines), 0014 (BOD 26-04 → VDR/VER), 0015/0016 (Security Inbox test and outcome) |
| RFCs | https://www.fedramp.gov/rfcs/00XX/ — post-CR26: 0032 (Offerings By Government), 0033/0034 (Phase 4 / Class D pilot, open Sept 9–Oct 9, 2026) |
| Submission JSON schemas | https://github.com/FedRAMP/schemas |
| Marketplace data (counts) | https://github.com/FedRAMP/marketplace-fedramp-gov-data (`data.json`) |
| 20x program page | https://www.fedramp.gov/20x/ |
| Community discussions | https://github.com/FedRAMP/community/discussions |
| Legacy 25.x standards (archived) | https://github.com/FedRAMP/docs-alpha ; legacy Rev5: https://www.fedramp.gov/legacy/ ; legacy templates (June 23, 2026 LEGACY NOTICE): https://github.com/FedRAMP/docs-legacy (github.com/GSA/fedramp-automation no longer exists) |
| FIPS 140-2 sunset guidance | help.fedramp.gov article 53386638354843 (July 22, 2026) |

## References

| Reference | Detail |
|-----------|--------|
| CR26 launch | June 24, 2026 (dataset); announcement June 25, 2026 — "Propelling Change" blog |
| NTC-0004 | Feb 25, 2026 — certification designations, class scheme, CR26 commitment |
| NTC-0009 | RFC-0024 outcome — OSCAL mandate dropped; FedRAMP JSON schemas required (FRC-CSO-JSN) |
| NTC-0013 | Rev5 baseline parameter/guidance removal (CTL ruleset) |
| NTC-0014 | CISA BOD 26-04 implementation → VDR/VER mandate (Rev5 required Dec 7, 2026) |
| RFC-0033 / RFC-0034 | Phase 4 — 20x Class D (High) pilot; open Sept 9–Oct 9, 2026 |
| OMB M-24-15 | July 2024 — Modernizing FedRAMP |
| FedRAMP Authorization Act | 44 USC 3607–3616 (FY2023 NDAA) |
| FedRAMP 20x announcement | March 24, 2025 |
