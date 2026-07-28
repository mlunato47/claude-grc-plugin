# FedRAMP 20x & Consolidated Rules for 2026 (CR26)

## Overview

**FedRAMP 20x** is the modernized, automation-first FedRAMP authorization model announced March 24, 2025: machine-readable evidence and continuous validation of **Key Security Indicators (KSIs)** replace narrative SSPs and point-in-time annual assessments. As of the **June 2026 Consolidated Rules release, 20x is generally available** — no longer a pilot — and operates alongside the legacy Rev5 path during a transition running until at least December 31, 2028.

**CR26 = the FedRAMP Consolidated Rules for 2026** — the program's first consolidated ruleset, merging the 2025-era "25.x" standards releases and the outcomes of RFC-0019–0031 into a single declarative rule system.

| CR26 fact | Value |
|-----------|-------|
| Launched | **June 24, 2026** (announcement blog June 25; public preview May 4, 2026) |
| Optional early adoption | July 4, 2026 |
| **Mandatory for all stakeholders** | **January 1, 2027** (including existing Rev5 certification holders) |
| Valid through | December 31, 2028 (stable planning window) |
| Structure | ~246 rules across 17 rulesets + 46 KSIs + 75 definitions (FRD) + rebuilt Rev5 control guidance (CTL) — counts per dataset 2026.07.14.01 |
| Rule format | Plain-language RFC-2119 statements (MUST/SHOULD/MAY) with stable IDs `SET-SUBSET-KEY` (e.g., `VDR-CSO-DET`), published as machine-readable JSON |
| Versioning | Date-based dataset releases (e.g., 2026.07.14.01); check the changelog — CR26 saw multiple revisions in its first weeks |

**Legal basis:** FedRAMP Authorization Act (44 USC 3607–3616, FY2023 NDAA) + OMB Memorandum M-24-15 ("Modernizing FedRAMP," July 2024). CR26's vulnerability standards also implement **CISA BOD 26-04**.

## Terminology Changes (know these — they invalidate older vocabulary)

| Old term | CR26 term |
|----------|-----------|
| FedRAMP Authorized / Authorization | **FedRAMP Certified / Certification** (FedRAMP certifies the *service*; agencies still issue their own ATO/risk acceptance) |
| Impact levels (Low/Moderate/High) as labels | **Certification Classes A–D** |
| 3PAO | **Independent Assessor** with **FedRAMP Recognized** status (REC ruleset — recognition layered on top of continuing A2LA accreditation, with biennial reassessment) |
| SSP | **Security Decision Record (SDR)** + **Certification Package Overview (CPO)** |
| Monthly ConMon deliverables | **VDR/VER** vulnerability standards + **Ongoing Certification Reports (OCR)** with quarterly reviews (CCM ruleset) |
| SSAD / Authorization Data Sharing | **Certification Data Sharing (CDS)** via provider **Trust Centers** |
| FedRAMP Ready | Legacy as of **July 28, 2026** (no new submissions; Ready-conversion pipeline opens Aug 10, 2026) |

## The Certification Model: Type + Path + Class

A **Certification Profile** = **Type** (20x or Rev5) + **Path** (Program — direct from FedRAMP, no agency sponsor — or Agency, Rev5-legacy only) + **Class** (A–D, per definition FRD-CCL: "minimal assurance at Class A to significant assurance at Class D").

| Class | Legacy mapping | Available under | Notes |
|-------|----------------|-----------------|-------|
| **A** | **New — no legacy equivalent** (minimal assurance) | 20x only | Entry tier leveraging **Approved Alternative Security Frameworks** (FRC-CLA-ASF): SOC 2 Type II, GovRAMP (any impact level), or FedRAMP Rev5 incl. FedRAMP Ready (any historical impact level), completed within the past 12 months — plus a reduced mandatory rule set incl. **7 named KSIs**, VDR detection, incident and trust-center rules; ongoing assessment cadence is carried primarily by the underlying framework (the FedRAMP-side annual IVV is a MAY for Class A). **2 years** to obtain a Class B/C/D certification (NTC-0007). Applications open Aug 3, 2026. |
| **B** | LI-SaaS / Low | 20x ("20x Low") and Rev5 | Full ruleset + full KSI set under 20x |
| **C** | Moderate | 20x ("20x Moderate") and Rev5 | Largest tier — Moderate ≈ two-thirds of currently certified services |
| **D** | High | **Rev5 only today** | 20x Class D pilot planned FY27 Q1–Q2 (Phase 4) |

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
- Machine verification/validation cadence scales by class (VDR-TFR-MVX: 20x Class B every 7 days and Class C every 3 days as MUSTs, Class A monthly as SHOULD; Rev5 monthly per VDR-TFR-MVF).

**Dates:** optional from July 4, 2026; **required to obtain/maintain certification by December 7, 2026**; corrective-action grace to **March 7, 2027**, then loss of certification.

## VER — Vulnerability Evaluation and Reporting

Companion CR26 ruleset (23 rules; classes B/C/D) split out of VDR: it governs *evaluating federal-customer impact and reporting it*.

- Evaluate exploitability and internet reachability; **assume exploits are automatable by default** (VER-EVA-AIA).
- Rate every vulnerability's **Potential Agency Impact N-rating (PAIN): N1 (minimal) → N5 (debilitating effect on multiple agencies)** (VER-EVA-EPA). Internet-reachable, likely-exploitable N4/N5 findings are handled as security incidents.
- Persistent reporting to all necessary parties, monthly activity reports, accepted-vulnerability marking, responsible public disclosure.
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
| FRD | Definitions (`/2026/definitions/`) | 75 controlled terms (PAIN, IRV, KEV, LEV, OCR, SDR, Trust Center, …) |

Class/type bundles: `reference/20x/{a,b,c}/` and `reference/rev5/{b,c,d}/`; full index at `reference/complete-rulesets/`. Note: there is no document named SSAD or CRS in CR26 (2025-era names people may still search for) — that content became CDS and CCM/OCR.

## Frequently Asked Details (and where the authoritative answers live)

- **Submission formats — OSCAL vs FedRAMP JSON schemas.** The 20x certification package (CPO + SDR + KSI evidence + rule artifacts) is machine-readable per **FedRAMP's own JSON schemas** (github.com/FedRAMP/schemas) — not OSCAL. The RFC-0024 OSCAL-mandate idea was dropped (NTC-0009): under CR26, Rev5 packages likewise move to FedRAMP's simplified JSON formats with OSCAL merely optional in some cases (comprehensive machine-readable data is required only for Rev5 Class D/High). Do not tell any CR26 applicant they need OSCAL.
- **Cryptography / FIPS (CMU).** The CMU ruleset takes a **risk-based approach to cryptographic module selection, preferring validated modules** — a posture shift from legacy hard FIPS-validation gating (CMU-CSO-UVM: validated modules MAY at Class A/B, SHOULD at Class C, still **MUST at Class D**; documenting the modules in use is a MUST for all). Fetch the CMU ruleset for the exact current rules before advising on FIPS obligations under 20x.
- **Penetration testing and assessment specifics.** Penetration testing is treated as **part of vulnerability detection under VDR** (FedRAMP's CTL guidance for CA-8 states this explicitly); assessment scope lives in **MAS** and independent-assessment expectations in **IVV** — fetch those rather than assuming the legacy annual-3PAO-pen-test model carries over.
- **Incident reporting clocks.** The **IEC** ruleset defines Initial/Ongoing/Final Incident Report obligations and their timelines — fetch it for the current clocks.
- **SDR contents.** The **SDR** ruleset defines what the Security Decision Record must contain and how it is maintained/verified — fetch it before drafting one.
- **VDR/VER timeframes.** The authoritative per-class detection/evaluation/remediation clocks are the **VDR-TFR-\*** and **VER-TFR-\*** rules in the machine-readable dataset; the examples in this file are industry summaries, not the rule text.

## For Agencies

- Certification ≠ ATO: agencies still perform their own risk acceptance. Industry analyses report CR26 restricts agencies from layering duplicate requirements on certified offerings.
- Agencies consume certification data through the provider's **Trust Center** (CDS ruleset — public info plus agency-access provisions) and **Ongoing Certification Reports** with quarterly reviews (CCM ruleset).
- Formal agency obligations live in the **AGU** ruleset — placeholder status at CR26 launch, so check it live before citing agency-side rules.

## Rev5 Coexistence and Sunset

- Rev5 continues as a legacy Certification Type (classes B/C/D; the Agency/sponsor path is Rev5-only) under CR26's Rev5 rulesets.
- **NTC-0013**: FedRAMP removed most FedRAMP-assigned control parameters and nearly all FedRAMP-specific control guidance from the Rev5 baselines (now the CTL ruleset), effective with mandatory adoption.
- **VDR and VER apply to Rev5 providers too** (required Dec 7, 2026).
- Timeline: **Jan 1, 2027** CR26 mandatory for everyone. Rev5 adoption is **per ruleset**: some rules carry fixed calendar dates (SCG grace already ended Jul 1, 2026; IEC/CMU/SCN grace to Jun 1, 2027; CCM ConMon rules mandatory to maintain certification **Apr 2, 2027**, grace to Oct 1, 2027; CDS grace to Feb 1, 2028), others tie their grace to the next completed independent assessment (e.g., CPO/FRC/IVV/MAS), and NTC-0013's Rev5 control-guidance changes adopt at the first independent assessment after Jan 1, 2027. **Jun 11, 2027** last new Rev5 certifications; **all CR26 grace periods expire Feb 1, 2028**; existing Rev5 certifications remain active until **at least December 31, 2028** ("unless FedRAMP is otherwise directed").
- Temporary Rev5 Class B/C pipelines (Ready Conversion + Lost Sponsor only) open Aug 10, 2026.

**Transitioning from Rev5 to 20x:** there is no automatic conversion — a Rev5 provider files a new 20x application (Program path). Two hooks ease the move: a FedRAMP Rev5 certification completed within the past 12 months qualifies as an **Approved Alternative Security Framework for Class A** (a fast onramp while building full KSI automation), and each KSI's official `controls` array is the sanctioned crosswalk from Rev5 control implementations to KSI evidence. Rev5 providers continue their existing monthly ConMon deliverables until the Rev5 CCM rules take hold (mandatory to maintain certification April 2, 2027; grace to October 1, 2027) — with VDR/VER layering on from December 7, 2026 regardless.

## Program Status (as of July 2026)

| Phase | Scope | Status |
|-------|-------|--------|
| 1 | Low pilot (Apr–Sep 2025) | Complete — 26 submissions, first certifications July 2025 |
| 2 | Moderate pilot (Nov 2025–Mar 2026) | Complete — first cohort certified Mar 6, 2026 |
| 3 | **General availability** | **Current** — "no longer just a pilot" (June 2026); Class A pipeline Aug 3, Class B/C Aug 31, 2026 |
| 4 | 20x Class D (High) pilot | Estimated FY27 Q1–Q2 |
| 5 | Rev5 sunset activities | Estimated FY27 Q3–Q4 |

Marketplace data (July 28, 2026): **28 FedRAMP 20x certified services** — 14 at 20x Low (Class B) + 14 at 20x Moderate (Class C) — out of ~530 total FedRAMP certified/authorized services.

## Practitioner Watch Items (industry analysis, mid-2026)

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
| Notices (NTC-0001–0014) | https://www.fedramp.gov/notices/ — key: 0004 (classes/CR26), 0007 (Class A / alternative frameworks, 2-year window), 0012 (incident comms), 0013 (Rev5 baselines), 0014 (BOD 26-04 → VDR/VER) |
| RFCs | https://www.fedramp.gov/rfcs/00XX/ |
| Submission JSON schemas | https://github.com/FedRAMP/schemas |
| Marketplace data (counts) | https://github.com/FedRAMP/marketplace-fedramp-gov-data (`data.json`) |
| 20x program page | https://www.fedramp.gov/20x/ |
| Community discussions | https://github.com/FedRAMP/community/discussions |
| Legacy 25.x standards (archived) | https://github.com/FedRAMP/docs-alpha ; legacy Rev5: https://www.fedramp.gov/legacy/ |

## References

| Reference | Detail |
|-----------|--------|
| CR26 launch | June 24, 2026 (dataset); announcement June 25, 2026 — "Propelling Change" blog |
| NTC-0004 | Feb 25, 2026 — certification designations, class scheme, CR26 commitment |
| NTC-0013 | Rev5 baseline parameter/guidance removal (CTL ruleset) |
| NTC-0014 | CISA BOD 26-04 implementation → VDR/VER mandate |
| OMB M-24-15 | July 2024 — Modernizing FedRAMP |
| FedRAMP Authorization Act | 44 USC 3607–3616 (FY2023 NDAA) |
| FedRAMP 20x announcement | March 24, 2025 |
