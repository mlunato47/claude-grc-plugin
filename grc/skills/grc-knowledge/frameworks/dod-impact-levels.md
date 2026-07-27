# DoD/DoW Cloud Impact Levels — DISA Cloud Service Provider SRG V1R7

## Overview

The Department of Defense — now formally the **Department of War (DoW)** — authorizes commercial and government cloud services through a system of **Information Impact Levels (IL2, IL4, IL5, IL6)** defined by DISA. Impact Levels segregate information into buckets by sensitivity and audience, and each level composes a **FedRAMP baseline** with **DoW-specific additions**: FedRAMP+ controls, CNSSI 1253 overlays, and SRG operational requirements.

The source of record is the **DISA Cloud Service Provider (CSP) Security Requirements Guide (SRG), Version 1 Release 7 (V1R7), 30 June 2026**. Key facts about the current document generation:

- **Renamed and split — with restarted numbering.** On 14 June 2024 the monolithic *DoD Cloud Computing SRG* (last release V1R4, 2022, now retired) was replaced by two documents: the **Cloud Service Provider SRG** (requirements a CSP must meet to earn a DoW Provisional Authorization) and the separate **Cloud Computing Mission Owner SRG** (technical requirements for the DoW customer hosting workloads in the cloud). The CSP SRG restarted its own release numbering at V1R1 and iterated rapidly — V1R2 (Jan 2025), V1R3 (Jul 2025; made IL5 NSS-focused and added ~170 CNSSI 1253 controls), V1R4 (Aug 2025), V1R5 (Sep 2025), V1R6, and now **V1R7 (30 Jun 2026)**. Beware: "SRG V1R4" is therefore ambiguous — it can mean the retired 2022 CC SRG or the Aug 2025 CSP SRG release. When someone says "the CC SRG," they almost always mean this material.
- **DoD → DoW terminology.** Following Executive Order 14347 (5 Sep 2025), which authorized "Department of War" as a secondary name, V1R7 uses "DoW" throughout while still citing legacy DoD instruction numbers (DODI 8500.01, 8510.01, 8520.02). DoD remains the statutory name pending congressional action. Treat DoD and DoW as the same department; mirror the user's terminology.
- **Impact Levels are a DoW construct, not a FedRAMP construct.** The SRG states explicitly that it is inaccurate to call a DoW PA a "FedRAMP Impact Level." FedRAMP does not address National Security Systems (NSS), National Security Information (NSI), or classified information — those fall under CNSS policy (CNSSI 1253, CNSSP-32).
- **There is no IL1 or IL3.** The SRG's 2014 predecessor (the DoD Cloud Security Model) defined six levels; when the CC SRG replaced it in 2015, Level 1 (public information) was folded into IL2 and Level 3 (low-impact CUI) into IL4, deliberately keeping the original numbering. Anything above SECRET (TS/TS-SCI) is out of scope for the SRG.

## Authority and Key Documents

| Document | Role |
|----------|------|
| Cloud Service Provider SRG V1R7 (DISA, 30 Jun 2026) | CSP requirements for DoW Provisional Authorization; defines IL2–IL6 |
| Cloud Computing Mission Owner SRG | Mission Owner (customer-side) technical requirements |
| DODI 8500.01 | Cybersecurity policy; authority for DISA SRGs/STIGs |
| DODI 8510.01 | DoW Risk Management Framework (RMF) |
| CNSSI 1253 | NSS categorization and control selection (baselines, overlays, Appendix D NSS controls, Classified Information Overlay) |
| CNSSP-32 | Requires unclassified NSS at minimum FedRAMP High baseline |
| DODI 8520.02 | PKI and Public Key Enabling (drives SC-17 at IL4+) |
| CNSSAM TEMPEST/1-13 | RED/BLACK requirements (IL6) |
| ICD 705 / ICD 503 | Classified facility and IC accreditation standards (IL6 physical separation from TS/SCI) |
| JWCC memo (31 Jul 2023) | Mandates the JWCC contract vehicle for new IL6/Top Secret cloud capabilities |

## Key Terminology

| Term | Meaning |
|------|---------|
| **DoW PA** | DoW Provisional Authorization — DISA AO's acknowledgment of risk for a specific CSO at a specific Impact Level. Foundation that Mission Owner AOs leverage for their ATOs. |
| **CSO** | Cloud Service Offering. PAs attach to CSOs, **not** to the CSP as a company. |
| **Mission Owner** | The DoW customer (program/component) hosting a workload in a CSO. |
| **FedRAMP+** | DoW concept of leveraging the FedRAMP assessment and layering added NIST 800-53 controls / adjusted parameter values on top (applies to IL4/5/6 only). |
| **DSPAV** | DoW Specific Assignment Value — the DoW-mandated parameter value for a control (from the DoW RMF TAG). |
| **CAP** | Cloud Access Point — boundary protection between the DISN (NIPRNet/SIPRNet) and a CSO. |
| **DoW Cloud Service Catalog** | Listing of CSOs holding a DoW PA. |
| **NIPRNet / SIPRNet** | DISN unclassified / SECRET network services. |

## The Impact Levels at a Glance

| IL | Information | CNSSI 1253 categorization | Access / network | FedRAMP floor |
|----|-------------|---------------------------|------------------|---------------|
| **IL2** | Noncontrolled unclassified — publicly releasable or low-confidentiality non-CUI | MMx (moderate C/I) | Internet | Moderate or High (full reciprocity) |
| **IL4** | Controlled Unclassified Information (CUI), mission data incl. direct support of military/contingency operations | MMx or HHx | NIPRNet via approved boundaries, or private connectivity | Moderate or High |
| **IL5** | Unclassified **NSS/NSI**; CUI needing protection above IL4 | HHx (high C/I) | NIPRNet / private | **High** (mandatory per CNSSP-32) |
| **IL6** | Classified up to **SECRET** (NSS/NSI) | HHx, classified | **SIPRNet** or approved CNSSP-11 circuits | High + Classified Overlay |

Categorization flow: the Mission Owner categorizes the system per DODI 8510.01 + CNSSI 1253, then selects the Impact Level that aligns with that categorization. Availability is assessed only to the FedRAMP baseline — specific availability needs go in the contract/SLA.

### IL2 — Noncontrolled Unclassified Information

- Publicly releasable data, or nonpublic unclassified data with limited adverse effect from disclosure; **not** CUI. May still need minimal access control (user ID/password).
- CSP may serve any customer mix (government, commercial, public) in the same environment. Access via internet.
- DoW accepts the FedRAMP Moderate PA risk as-is — **no additional DoW requirements beyond personnel-security screening are assessed** for an IL2 PA (Tier 1 investigation still applies; see the personnel table below).

### IL4 — Controlled Unclassified Information

- Nonpublic unclassified data where disclosure has a **serious** adverse effect: CUI and mission data, including direct support of military/contingency operations. Designating data as CUI is the owning organization's responsibility; selecting the IL is the mission AO's.
- Some CUI categories (e.g., certain privacy data) may need assessment beyond the DoW PA.
- Customer community: all U.S. government customers (federal/state/local/tribal) and commercial entities supporting them; DoW contractors operating systems for the DoW or storing/processing DoW CUI/CDI under contract (contract fulfillment, not general corporate use).
- Connectivity: NIPRNet-based components connect via DoW CIO-approved NIPRNet boundaries; non-NIPRNet components via component-provided approved boundaries; others establish their own.

### IL5 — Unclassified NSS / National Security Information

- Nonpublic unclassified **NSS/NSI**, plus CUI/mission data the owner deems in need of protection above IL4.
- Per CNSSP-32: minimum = **FedRAMP High baseline + CNSSI 1253 Appendix D NSS controls + overlays**. NSS data must sit at IL5 or higher; unclassified NSS must be at IL5.
- Deployment: DoW private/community clouds or Federal Government Community Clouds; on- or off-premises.
- A non-NSS system **may** elect IL5 for added protection.

### IL6 — Classified up to SECRET

- Classified NSS/NSI up to SECRET only (above SECRET is out of SRG scope).
- **Dedicated infrastructure** in facilities accredited for classified processing at/above the data's classification; the CSO is a self-contained SECRET enclave.
- Because the infrastructure must be dedicated, IL6 CSOs exist only under contract to DoW or another federal agency — not "commercially available," even when cloned from the CSP's commercial offering.
- Access via SIPRNet; customers are SIPRNet-based DoW components, National Secret Fabric agencies, and contractors operating SECRET NSS under contract.
- New SECRET/Top Secret cloud capability acquisitions must use the **JWCC** contract vehicle (31 Jul 2023 memo).

## Baseline Composition per Impact Level (SRG Table 3-1)

Every DoW PA is a **composition**: FedRAMP baseline + FedRAMP+ + CNSSI 1253 overlays + other SRG requirements. There is no single fixed per-IL control list.

| IL | Baseline | Additions based on data/mission |
|----|----------|-------------------------------|
| IL2 | FedRAMP Moderate | None |
| IL4 (Moderate path) | FedRAMP Moderate + CNSSI 1253 Table D-1, CIA MMx | Additional CNSSI 1253 overlays |
| IL4 (High path) | FedRAMP High + CNSSI 1253 Table D-1, CIA HHx | Additional CNSSI 1253 overlays |
| IL5 (NSS) | FedRAMP High + CNSSI 1253 Table D-1 "+", CIA HHx | CNSSI 1253 overlays + Table D-1 "+" NSS controls (HHx) |
| IL6 (NSS) | FedRAMP High + CNSSI 1253 Table D-1 "+" + Classified Overlay, CIA HHx | CNSSI 1253 overlays + Table D-1 "+" controls; **Classified Information Overlay values take precedence** |

→ For the NIST 800-53 control-level view of these compositions, see `mappings/nist-to-dod-il.md`.

## FedRAMP Reciprocity and the Two-Step Authorization

DoW uses a **two-step** model for commercial cloud: (1) DISA assesses the CSO and grants a **DoW PA** at one or more Impact Levels; (2) the Mission Owner's AO leverages the PA plus their own assessment package to issue an **ATO** for the mission system in that CSO.

| FedRAMP status | DoW reciprocity | What is layered on top |
|----------------|-----------------|------------------------|
| FedRAMP Moderate P-ATO/Agency ATO | **Full reciprocity → IL2** | Personnel security + integration requirements; Mission Owner ATO still required |
| FedRAMP Moderate or High | Floor for **IL4** | IL4 FedRAMP+ + CNSSI 1253 overlays + SRG requirements → DoW PA assessment |
| FedRAMP High | Mandatory floor for **IL5** | IL5 FedRAMP+ + CNSSI 1253 Appendix D NSS controls + overlays → DoW PA |
| — | **IL6** | Separate DoW authorization: FedRAMP High baseline + Classified Overlay; SIPRNet; classified facility |

PA mechanics worth knowing:

- **Granted per-CSO.** A SaaS built on an authorized IaaS/PaaS **inherits** the underlying CSO's compliance but still needs **its own** DoW PA (and usually its own FedRAMP P-ATO) — the application layer must be assessed itself.
- **Inheritance chains flow down.** If CSP A's CSO leverages CSPs B/C/D, A inherits their posture (good or bad), must disclose all subcontracted CSOs, and is contractually accountable for them. Leveraged CSOs without their own PA get assessed as part of the primary CSO but earn no independent PA.
- **Revocable.** Losing the FedRAMP PA, falling out of SRG compliance, or a leveraged CSO losing its PA can all revoke a DoW PA. The DISA AO approves and revokes.
- **PAs are not granted to physical facilities** — data centers are assessed under the CSP's CSO PE controls.
- **"FedRAMP Moderate equivalency"** (a DFARS 252.204-7012 construct per the 21 Dec 2023 DoD CIO memo) requires **3PAO-validated 100% compliance** with the FedRAMP Moderate baseline, with the contractor responsible for verifying and maintaining the CSP's status. It is **not** a FedRAMP authorization and has zero crossover value toward actual FedRAMP certification (no P-ATO, no Marketplace listing).
- **SRG update transition (§4.4):** assessments already active when a new SRG releases finish under the old one; CSOs in ConMon must provide a POA&M for new-requirement gaps within 30 days and reach compliance no later than the next annual assessment. A PA based on the prior SRG remains in effect (unless revoked) **so long as those transition timelines are met**.

## FedRAMP+ Key Parameter Values (SRG Appendix D, Table D-1)

FedRAMP+ controls and adjusted parameters apply at IL4/5/6. Parameter precedence (stated in the SRG for IL5 NSS parameters, generally applied): **DSPAV** (DoW RMF TAG value) → CNSSI 1253 value → AO-tailored. This table is a benchmark, not the complete control set.

| Control | DoW requirement | IL |
|---------|-----------------|-----|
| AC-7 | Privileged accounts: lock after **3** failed attempts (per the SRG, for ILs 2/4/5; **5** attempts for SIPR-token accounts); **administrator unlock** required at all levels. Non-privileged with rate limiting: 10 attempts, 30-min auto-unlock; otherwise DSPAV. | 4/5/6 |
| PS-3(4) | Users: U.S. citizens/nationals/persons (foreign personnel only per DoW policy + AO approval). Administrators: U.S. citizens/nationals/persons. | 4/5/6 |
| SA-9(5) | Information processing, data, and services restricted to **U.S./U.S. territories or U.S.-jurisdiction locations** — all data, systems, services. | 4/5/6 |
| SC-17 | PKI per DODI 8520.02. | 4/5/6 |
| SC-18, SC-18(2) | Mobile code restrictions — SC-18 added (no parameter specified); SC-18(2) DSPAV. | 4/5/6 |
| SC-18(3), SC-18(4) | CSO must not support downloading mobile code unacceptable to DoW; user-permission prompting for embedded-code documents. | 5/6 |
| CM-7(5), IA-5(1), PE-15, SA-4(5), SA-9(1), SA-9(3), SC-24 | DSPAV must be used. | 4/5/6 |
| SC-12(6) | Added (no parameter adjustment specified). | 4/5/6 |
| MA-5(1) | DSPAV. | 4 |
| MA-5(2), MA-5(3), MA-5(4) | Required. | 6 |
| MA-5(5) | Required. | 4/5/6 |
| SA-9(6), SA-9(7), SA-9(8) | Required. | 4/5/6 |
| AU-5(1), MA-6, PS-4 | FedRAMP value acceptable. | 4/5/6 |
| SC-46 | DSPAV — only if a cross-domain solution is used. | CDS |

At IL6, the CNSSI 1253 **Classified Information Overlay** modifies some of these values and adds controls not listed — overlay values take precedence.

## Separation Requirements per Impact Level (SRG §5.2.2)

Anchoring control: **SC-4**. The SRG enables *logical* separation of unclassified services from non-DoW infrastructure at IL2/4/5; physical separation enters at specific points below.

| IL | Separation requirement |
|----|------------------------|
| IL2 | None beyond FedRAMP Moderate — DoW accepts that risk as adequately covered. |
| IL4 | **Strong virtual separation** (encryption and/or access-control policy) + monitoring. Must support law-enforcement "search and seizure" of non-DoW data without exposing DoW data (and vice versa), and prevent cross-tenant access on shared hardware. Monitoring must detect unauthorized access. |
| IL5 | Strong isolation via **either** (a) physical separation from all nonfederal tenant systems, **or** (b) **NSA-validated/approved cryptographic (virtual) separation** preventing cross-tenant access even on shared hardware. The Mission Owner/AO may still mandate physical separation from non-DoW/nonfederal tenants. PaaS/SaaS at IL5 must be built on an authorized IL5 environment. |
| IL6 | **Dedicated infrastructure** in a classified-rated facility; self-contained SECRET enclave. Virtual/logical separation is sufficient between DoW and federal tenants and (minimally) between missions; **physical separation required** from non-DoW/nonfederal tenants and from TS/SCI (ICD 705/503). CNSSAM TEMPEST/1-13 Level 1 RED/BLACK compliance. |

> **Recent change to know (V1R6/V1R7):** IL5 previously read as "physical separation required" from nonfederal tenants — as of V1R5 (Sep 2025) that was still the text. The current SRG makes NSA-approved cryptographic separation an accepted **alternative**, codifying what DISA had already approved case-by-case for years (e.g., HSM-backed key-isolation architectures in existing IL5 PAs).

**E-discovery separation (all ILs):** the CSP must be able to segregate federal from nonfederal data at the **individual Mission Owner** granularity, isolate a Mission Owner's data for forensic review without CSP involvement (or produce a forensic image), and flow this requirement down to all subcontracted CSOs.

## CSP Personnel Security (SRG §5.5.2, Table 5-1)

Screening under PS-3/PS-3(3); personnel accessing multiple systems meet the highest applicable requirement.

| IL | Minimum investigation (privileged personnel) | Citizenship |
|----|----------------------------------------------|-------------|
| IL2 | Tier 1 | No restrictions |
| IL4 | Tier 3 | U.S. citizens / nationals / persons |
| IL5 | Tier 3 | U.S. citizens / nationals / persons |
| IL6 | Tier 3 with access to classified | **U.S. citizens only** |

- Non-privileged staff (janitorial, physical maintenance) at IL4/5/6: Tier 3 **or always escorted**.
- IL6 extras: **Tier 5** investigation for key cyber individuals with knowledge of key risks/vulnerabilities; contracts carry classified-safeguarding clauses (48 CFR Subpart 4.4, FAR 52.204-2) under the **NISP**.
- Shared facilities: CSP personnel requirements match the facility's unescorted-access requirement (a TS building means TS-cleared support staff).
- Remote maintenance on sensitive systems uses qualified **digital escorts** with defined restrictions (SRG §5.17).
- Tier 1/3/5 are the legacy Federal Investigative Standards tiers, which the SRG still uses; Trusted Workforce 2.0 is migrating federal vetting toward a low/moderate/high model.

## Architecture and Connectivity Notes

- **Cloud Access Point (CAP)** — boundary protection between the DISN and CSOs, required in general to mitigate risk to the DISN (limited exceptions exist; SRG §5.9.1). IL4/5 traffic from NIPRNet-based components flows through DoW CIO-approved NIPRNet boundaries; IL6 connects via SIPRNet. Alternate connectivity requires DoW CIO approval.
- **Network planes** — the SRG distinguishes user/data-plane and management-plane connectivity, each with its own requirements (SRG Tables 5-3/5-4).
- **Data location** — IL4+ data stays in the U.S./U.S. jurisdiction (SA-9(5)); this protects against foreign seizure and non-U.S.-person access.
- **Ongoing assessment** — continuous monitoring, change control (per the FedRAMP Significant Change Policies and Procedures Guide), and support for financial audits (SOC 1 Type II) are CSP obligations post-PA (SRG §5.3).
- **Incident response** — DoW-specific reporting categories, timelines, and mechanisms apply (SRG §6.2), plus support for law-enforcement investigations and the DoW insider-threat/UAM program.

## Common Pitfalls

1. **Calling an IL a FedRAMP level.** "FedRAMP IL5" is not a thing — Impact Levels are DoW-only. State the FedRAMP baseline and the IL separately.
2. **Assuming a FedRAMP High ATO ≈ IL5.** High is only the floor; FedRAMP+ controls, CNSSI 1253 NSS controls, personnel/citizenship requirements, U.S.-jurisdiction hosting, and connectivity architecture all still apply.
3. **Treating the PA as company-wide.** PAs are per-CSO. Each offering — including a SaaS on an already-authorized IaaS — needs its own.
4. **Citing the retired CC SRG — or the wrong "V1R4."** The 2022 CC SRG V1R4 is retired; use the CSP SRG V1R7 (CSP-side) and the Mission Owner SRG (customer-side). Note "V1R4" is ambiguous: the CSP SRG series restarted numbering in 2024, so CSP SRG V1R4 (Aug 2025) is a different document from CC SRG V1R4 (2022).
5. **Confusing "FedRAMP Moderate equivalency" with FedRAMP authorization.** Equivalency (DoD CIO memo, 21 Dec 2023) is 3PAO-validated 100% Moderate-baseline compliance for DFARS purposes — rigorous, but it carries no weight toward a FedRAMP P-ATO/ATO or Marketplace listing.
6. **Forgetting the Mission Owner's half.** A PA never authorizes a mission system by itself — the Mission Owner AO's ATO (leveraging the PA) is always the second step.

## References

| Reference | Detail |
|-----------|--------|
| Cloud Service Provider SRG | V1R7, 30 June 2026 (DISA; series began V1R1 on 14 Jun 2024, replacing the retired CC SRG V1R4 of 2022) |
| Cloud Computing Mission Owner SRG | Companion document for Mission Owner requirements |
| DODI 8500.01 / 8510.01 | Cybersecurity policy / DoW RMF |
| CNSSI 1253 | NSS categorization, overlays, Appendix D, Classified Information Overlay |
| CNSSP-32 | Unclassified NSS minimum baseline (FedRAMP High) |
| DODI 8520.02 | PKI/PKE |
| CNSSAM TEMPEST/1-13 | RED/BLACK (IL6) |
| ICD 705 / ICD 503 | Classified facilities / IC accreditation |
| JWCC memo | 31 July 2023 — JWCC vehicle for IL6/TS cloud (still operative; the JWCC follow-on "Unified Cloud Marketplace" was in solicitation as of mid-2026, awards expected 2027) |
| DISA Cyber Exchange | https://cyber.mil / https://public.cyber.mil (SRG/STIG distribution) |
| DoW RMF Knowledge Service | https://rmfks.osd.mil (DSPAV parameter values) |
