# ITAR — International Traffic in Arms Regulations (22 CFR 120–130)

## Overview

ITAR controls the export of **defense articles, defense services, and technical data** on the U.S. Munitions List (USML). Administered by the State Department's **Directorate of Defense Trade Controls (DDTC)** under the Arms Export Control Act (AECA, 22 U.S.C. 2778), it regulates *conduct* — manufacturing, exporting, brokering, and disclosing controlled data — not products or platforms.

Four framing facts every GRC conversation needs:

1. **There is no ITAR certification.** DDTC certifies nothing; a company *registers* with DDTC and self-manages compliance. No cloud, product, or vendor is "ITAR certified" — an environment can only *support* a customer's compliance (AWS and Microsoft both state this verbatim in their docs).
2. **The exporter owns the obligation.** Shared-responsibility applies operationally, but the legal export-compliance duty stays 100% with the registered company, never the CSP.
3. **An "export" includes disclosure to a foreign person inside the U.S.** (deemed export, §120.50(a)(2)) — even visual access counts, and a release is attributed to all countries of the person's **current and former citizenship, and current permanent residency** (§120.50(b)).
4. **Data location is an export event.** Storing technical data on a server abroad is an export to that country unless the §120.54 encryption carve-out applies (see the 3D Systems enforcement case: German file server = violation).

## Regulatory Structure (22 CFR Subchapter M)

| Part | Covers |
|------|--------|
| 120 | Purpose, policies, and **all definitions** (Subpart C, §§120.30–120.69) |
| 121 | The USML (§121.1 — 21 categories) |
| 122 | Registration of manufacturers and exporters |
| 123 | Licenses for defense articles (DSP-5/-61/-73) |
| 124 | Agreements: TAA, MLA, WDA; offshore procurement |
| 125 | Technical data & classified exports (DSP-85) |
| 126 | General policies: §126.1 proscribed countries; exemptions (Canada §126.5, AUKUS §126.7, UUV §126.9); ETL (Supp. No. 2) |
| 127 | Violations and penalties |
| 128 | Administrative procedures (consent agreements §128.11) |
| 129 | Brokering |
| 130 | Political contributions, fees, and commissions |

**2022 reorganization trap (effective Sept 6, 2022):** definitions were consolidated into Part 120 Subpart C, and many old section numbers were **reused for different concepts**. Pre-2022 citations are unreliable: defense article is now §120.31 (was §120.6), technical data §120.33 (was §120.10), public domain §120.34 (was §120.11 — and **§120.11 now means "Order of review"**), export §120.50 (was §120.17), U.S. person §120.62 (was §120.15), foreign person §120.63 (was §120.16). Stable anchors: §120.54 (activities-not-exports) and §120.55 (access information) kept their numbers.

## Key Definitions (current section numbers)

| Term | § | Essence |
|------|---|---------|
| Defense article | 120.31 | Items/technical data designated on the USML, incl. models/mockups revealing technical data and unfinished products (forgings, castings) clearly identifiable as defense articles |
| Defense service | 120.32 | Assisting foreign persons (anywhere) in design→use of defense articles; furnishing controlled technical data; military training |
| Technical data | 120.33 | Information required for design/development/production/operation/repair/testing/modification of defense articles + directly related software. Excludes public domain, general scientific principles, basic marketing info |
| Public domain | 120.34 | Published, generally accessible information (incl. §120.34(a)(8) **fundamental research** at accredited U.S. universities — lost if publication restrictions accepted) |
| Export | 120.50 | Shipment/transmission abroad; **deemed export** — release to a foreign person in the U.S. (a)(2); performing a defense service; attributed to all citizenship/residency countries (b) |
| Reexport / Retransfer | 120.51 / 120.52 | Movement between foreign countries (incl. deemed reexport) / change of end-use or end-user within one |
| Release | 120.56 | Visual or other inspection revealing technical data; oral/written exchange; **use of access information to reach unencrypted data** |
| Access information | 120.55 | Decryption keys, passwords, network access codes — providing these to a foreign person requires the same authorization as releasing the data (§120.56(b)) |
| U.S. person | 120.62 | Citizens/nationals and other protected individuals (incl. asylees/refugees), lawful permanent residents, U.S.-incorporated entities, U.S. governmental entities |
| Foreign person | 120.63 | Everyone/everything else, incl. foreign governments and international organizations |
| Empowered Official | 120.67 | Senior U.S. person with authority to sign — and refuse to sign — license applications |

## The USML (§121.1) — 21 Categories

I Firearms · II Guns & Armament · III Ammunition/Ordnance · IV Launch Vehicles, Missiles, Rockets, Torpedoes, Bombs, Mines · V Explosives/Energetics/Propellants · VI Surface Vessels of War · VII Ground Vehicles · VIII Aircraft · IX Military Training Equipment · X Personal Protective Equipment · XI Military Electronics · XII Fire Control/Laser/Imaging/Guidance · XIII Materials & Miscellaneous · XIV Toxicological/Chemical/Biological Agents · XV Spacecraft · XVI Nuclear Weapons Related · XVII Classified Articles Not Otherwise Enumerated · XVIII Directed Energy Weapons · XIX Gas Turbine Engines · XX Submersible Vessels · XXI Articles Not Otherwise Enumerated

**Classification churn — re-run jurisdiction analyses:** the **"USML Targeted Revisions" rules (IFR Jan 17, 2025; final Aug 27, 2025 — both effective Sept 15, 2025)** amended 16 of 21 categories, the largest restructure in a decade: e.g., body-armor ITAR threshold reset at NIJ RF3+ (lower levels → EAR), Novichok-family agents added to XIV, large-UUV entries in XX with a new §126.9(u) exemption, and finalized Cat VIII "foreign advanced military aircraft" coverage. A July 23, 2026 IFR removes **suppressors for non/semi-automatic firearms** from Cat I effective **Nov 20, 2026** (still ITAR until then). Space Cats IV/XV modernization and the defense-services (§120.32) overhaul remain **pending NPRMs** — no final rules yet.

## §120.54 — The End-to-End Encryption Carve-Out (the cloud provision)

Sending, taking, or **storing** technical data is **not an export/reexport/retransfer** when ALL of §120.54(a)(5) holds:

1. **Unclassified**;
2. **End-to-end encrypted** (§120.54(b)): never unencrypted between the originator's and recipient's in-country security boundaries, and **the means of decryption are not provided to any third party** (the intended recipient must be the originator, a U.S. person in the U.S., or an otherwise-authorized person);
3. **FIPS 140-2-compliant modules (or successors)** with NIST-conformant implementation and key management, **or** other means of at least AES-128-comparable strength; *(regulatory wording — practitioner note: FIPS 140-3 is the successor; on September 22, 2026 NIST moved every FIPS 140-2 certificate to the CMVP Historical List, so new deployments should use an actively validated FIPS 140-3 module, and Historical modules run only under documented risk acceptance)*
4. **Not intentionally sent to a person in, or stored in, a §126.1 proscribed country** (internet transit through a country is not "storage" there — Note 1). *The former separate "or Russia" wording was removed from both conditions 4 and 5 as duplicative on July 7, 2025 — Russia is itself a §126.1 country; the prohibition is unchanged*;
5. **Not sent from** a §126.1 country.

§120.54(c): a foreign person's mere *ability to access* properly encrypted data is not a release — this is what lawfully permits ITAR data on commercial cloud infrastructure with foreign-person administrators. But **giving a foreign person the access information is itself a controlled release** requiring prior authorization (§120.56(b); reinforced by DDTC's encryption-rule FAQ): sloppy IAM or password sharing can be a violation with zero data movement.

**Practitioner gotchas (why gov clouds still dominate):**
- **Provider-managed keys break condition 2.** Default server-side encryption (S3/Azure Storage SSE, TDE with service-managed keys) means the CSP holds the keys — the carve-out fails. Customer-held keys are the load-bearing control: client-side encryption, HSM-backed non-exportable keys, external key managers.
- **TLS terminated at the provider's load balancer** = plaintext on third-party infrastructure mid-path.
- **Metadata leaks**: filenames, error messages, console output, and config can themselves be technical data.
- Endpoint sync/caching abroad defeats the carve-out at the edges.

## DDTC Registration (Part 122)

- **Who (§122.1):** anyone in the U.S. engaged in manufacturing, exporting, temporarily importing defense articles, or furnishing defense services — one occasion suffices, and **manufacturers must register even if they never export**. Brokers register separately (Part 129).
- **Mechanics:** Form DS-2032 via DECCS, signed by a U.S.-person senior officer; annual renewal; **§122.4 material-change notification is an enforced obligation** (a count in the 2026 GE consent agreement), with 60-day advance notice of any sale or transfer of ownership/control of the registrant to a foreign person; 5-year records (§122.5).
- **Fees (effective Jan 9, 2025):** Tier 1 **$3,000**/yr (new registrants / no recent favorable determinations); Tier 2 **$4,000** (1–5 favorable determinations); Tier 3 **$4,000 + $1,100 per determination above five**.
- Registration confers no export rights — it is the precondition for licenses.

## Licensing, Agreements, Exemptions

| Vehicle | Use |
|---------|-----|
| DSP-5 | Permanent export of unclassified articles/technical data (also the deemed-export license for foreign-person employees) |
| DSP-61 / DSP-73 | Temporary import / temporary export (unclassified) |
| DSP-85 | Classified articles or technical data |
| TAA / MLA / WDA (Part 124) | Technical assistance, manufacturing licenses, warehouse/distribution abroad |
| Brokering (Part 129) | Separate registration + prior approval for certain articles |

**Exemptions:**
- **Canada (§126.5):** license-free export of most unclassified articles/services to Canadian-registered persons and authorities (exceptions in Supp. No. 1).
- **AUKUS (§126.7):** license-free trade among DDTC-registered U.S. persons, UK/Australian government bodies, and enrolled **Authorized Users** (700+ enrolled), within AUS/UK/US territory, for items **not** on the Excluded Technology List (Supp. No. 2 — MT-designated items, anti-tamper, F-22, MANPADS, certain Cat XI electronics, etc.). Created Sept 1, 2024 (IFR); **final rule Dec 30, 2025** added §126.7(c) (reexports/retransfers by contractors supporting AUKUS armed forces) and broadened Authorized Users. ETL reviewed annually for the first five years. For SaaS vendors: entity-gated on both sides — it eases sharing with enrolled UK/AU entities but does not relax U.S.-persons assumptions in gov-cloud environments (practitioner inference; no DDTC SaaS guidance exists).
- **§126.9(u):** large-UUV activities (new, Sept 2025).

## §126.1 Proscribed Countries

- **Table 1 (policy of denial):** Belarus, Burma, China, Cuba, Iran, North Korea, Syria, Venezuela.
- **Table 2 (denial with carve-outs):** Afghanistan, CAR, Cyprus, DR Congo, Eritrea, Ethiopia, Haiti, Iraq, Lebanon, Libya, Nicaragua, **Russia**, Somalia, South Sudan, Sudan, Zimbabwe. (**Cambodia removed Nov 7, 2025.**)
- Exemptions are generally unavailable for §126.1 destinations, and §126.1(e)(2) imposes an affirmative **duty to notify DDTC immediately** of any proposed or actual transfer involving one.

## ITAR in the Cloud

**The correct answer to "is your cloud ITAR compliant?":** no cloud is or can be — the environment can only support the customer's own compliance. What the big three actually commit to:

| Provider | Commitment |
|----------|-----------|
| **AWS GovCloud (US)** | US-soil regions "managed solely by **U.S. citizens** in U.S. locations"; account holders must be U.S. persons; all customer data treated as ITAR data. Customer must be DDTC-registered and control its own IAM population — AWS does not restrict who *you* let in. |
| **Azure Government** | Contractual CONUS residency + screened-U.S.-persons access commitments — **via EA amendment only** (you must formally notify Microsoft of ITAR intent); Customer Lockbox for support access; HSM-backed key custody. |
| **GCP Assured Workloads (ITAR package)** | Policy-enforced folder: US-only resource locations, **mandatory CMEK**, restricted service list, US-persons support routing (Enhanced/Premium Care), regional endpoints. |

Two lawful architectures: (a) a gov-cloud environment whose contractual US-persons + residency commitments hold even when encryption is imperfect, or (b) a strict §120.54 end-to-end-encryption architecture on commercial cloud. Most defense customers land on (a) because DFARS/CMMC/IL4-5 requirements push them there anyway and it removes carve-out fragility. Note the provider commitments cover *provider* personnel only — the customer's own admins, MSPs, SIEM vendors, and follow-the-sun support remain the customer's deemed-export problem.

**AI/LLM caution (no DDTC guidance exists yet — practitioner analysis only):** ITAR technical data sent to commercial LLM APIs creates deemed-export surface at every layer — training-data retention, non-US inference infrastructure, foreign-national model-ops staff, vector DB/logging pipelines. Recommended practice: full pipeline deemed-export analysis and US-persons-only AI infrastructure (e.g., Bedrock in GovCloud, Azure OpenAI in Azure Government, Vertex under Assured Workloads).

## ITAR × Federal Frameworks

| Framework | Relationship |
|-----------|-------------|
| **CUI** | Export-controlled technical data on federal contracts is CUI Specified — banner **CUI//SP-EXPT** (NARA registry, Export Controlled category) |
| **DFARS 252.204-7012** | Safeguarding per NIST 800-171 + 72-hr incident reporting; cloud must be FedRAMP Moderate or "equivalent" (3PAO-validated 100% compliance per the Dec 21, 2023 DoD CIO memo) |
| **NIST 800-171 / CMMC** | The *safeguarding* baseline for export-controlled CUI. **CMMC L2 certification ≠ ITAR compliance** — CMMC assesses 800-171, not US-persons gating, licensing, or DDTC registration |
| **FedRAMP** | **FedRAMP High ≠ ITAR.** FedRAMP authorizes cloud security; it says nothing about export control. A FedRAMP High service in a commercial region with global support staff satisfies FedRAMP and fails ITAR. What helps: FIPS-validated crypto, audit trails, and — in gov-cloud instantiations — the US-persons operations that come from the *gov-cloud contract*, not the FedRAMP certification |
| **DoD/DoW IL4/IL5** | ITAR technical data as CUI typically rides IL4+; the FedRAMP+ parameters operationalize ITAR-adjacent needs — **PS-3(4)** (US citizens/nationals/persons) and **SA-9(5)** (US-jurisdiction-only data/services). See `dod-impact-levels.md` |
| **NIST 800-53 families** | Practitioner mapping (no official DDTC crosswalk exists): **AC** (need-to-know limited to authorized US persons), **PS** (PS-3 screening = the nationality gate), **PE** (TCP physical controls), **AU** (access logs as export-recordkeeping evidence), **SC** (SC-8/12/13/28 = the §120.54 machinery), **MP** (marking/sanitization), **IR** (violation response/VSD), **SA/SR** (flow-down to vendors) |

## Penalties & Enforcement

- **Civil (§127.10):** up to **$1,271,078 per violation** or twice the transaction value (2025-adjusted figures — still operative in 2026: no government-wide 2026 inflation adjustment occurred because the FY2026 shutdown blocked the underlying CPI-U publication).
- **Criminal:** willful violations up to $1,000,000 and/or 20 years per violation. **Debarment** (§127.7): generally 3 years, reinstatement never automatic.
- **Voluntary disclosure (§127.12)** is a consistently honored mitigating factor — not immunity.

| Case | Penalty | Lesson |
|------|---------|--------|
| Boeing (Feb 2024) | $51M ($24M suspended), 199 violations | Deemed exports to foreign-person employees/contractors (incl. in Russia/China) — FPE access to engineering data is DDTC's core concern |
| **RTX (Aug 2024)** | **Record $200M ($100M suspended)**, 750 violations | All voluntarily disclosed — half the penalty suspended for remediation; M&A/legacy-entity hygiene |
| Precision Castparts (Oct 2024) | $3M ($1M suspended), 24 violations | Mid-market trap: tooling technical data released to 46 foreign-person employees without deemed-export licenses |
| GE Aerospace (Apr 2026) | $36M ($18M suspended), 116 violations | Proviso management inside approved agreements + **§122.4 registration-change reporting are enforced obligations** |
| 3D Systems (Feb 2023) | $20M DDTC (+BIS/DOJ) | Technical data emailed to Chinese subsidiary and **stored on a German server** — infrastructure location is an export decision |

Cloud-specific latent liability: a public bucket of technical data is an uncontrolled worldwide export (cf. the 2017 Booz Allen/INSCOM S3 exposures); no DDTC consent agreement squarely addresses a cloud misconfig yet — treat as contain → scope access → strongly consider VSD.

## Compliance Program (DDTC Compliance Program Guidelines + TCP)

DDTC's published CPG elements: management commitment · registration maintenance · jurisdiction/classification (CJ where unclear) · authorization administration incl. proviso tracking and screening · 5-year recordkeeping · violation detection/disclosure (VSD path) · role-based training · risk assessment · independent audits.

The core artifact is the **Technology Control Plan (TCP)**: inventory of controlled technology and locations; **Empowered Official** designation; physical security (controlled areas, clean desk, visitor/escort rules); IT segregation (the "ITAR enclave" pattern — gov-cloud folder, US-persons-only IAM groups, customer-managed keys, DLP labeling); foreign-national and visitor procedures; CUI//SP-EXPT + ITAR notice marking; training cadence and records; restricted-party screening (Debarred/Denied/SDN lists, at hire and continuously); a pre-written VSD decision path.

## ITAR vs. EAR

- **Order of review (§120.11 — the new meaning of that number):** USML first (enumerated entries before "specially designed" catch-alls); if not described there, the item may be **subject to the EAR** (§120.58) — the EAR's own order of review (Supp. No. 4 to 15 CFR part 774) then starts with the **600-series** ECCNs (USML migrants under Commerce jurisdiction — still controlled, not "free").
- **Commodity Jurisdiction (§120.4, procedure §120.12, Form DS-4076):** the only definitive resolution of USML-vs-CCL doubt.
- **The "ITAR-free" fallacy:** ITAR has **no de minimis** — any ITAR content or U.S.-person defense service keeps the item/activity under ITAR indefinitely (see-through rule; §123.9 consent for reexports). Marketing a supply chain as "ITAR-free" does not remove AECA jurisdiction.
- ITAR deemed-export attribution covers all current and former citizenships plus current permanent residency — broader than the EAR's approach; don't apply EAR logic to ITAR data.

## Customer FAQ (the questions that actually come up)

1. **"Is your cloud ITAR certified?"** No certification exists — we provide an environment that supports *your* obligations; you remain the exporter and must be DDTC-registered.
2. **"Do I need GovCloud for ITAR?"** Not legally — you need either a US-persons/US-residency environment (which gov clouds deliver contractually) or a strict §120.54 architecture. Most defense customers choose gov cloud; DoD contract requirements push them there anyway.
3. **"Is FedRAMP High enough?"** No — FedRAMP is security authorization, not export control.
4. **"Does encryption alone fix it?"** Only true end-to-end with keys exclusively held by authorized persons, FIPS 140-compliant, no plaintext on third-party infrastructure, and no §126.1 endpoints. Provider-managed keys or TLS terminated at the provider break it — and handing a foreign person the keys is itself a release.
5. **"Can foreign-national devs touch the codebase?"** If they can *see* ITAR technical data, that's a deemed export requiring prior authorization. License them (DSP-5/TAA), architect them out (segregated enclave, sanitized repos), or ensure they can't decrypt. Repo ACLs are export controls.
6. **"What about follow-the-sun support?"** Provider side is covered by gov-cloud commitments; your own MSPs, SaaS admins, and 24/7 vendors are your deemed-export responsibility.
7. **"How does this relate to CUI/CMMC?"** Export-controlled data is CUI//SP-EXPT; 800-171/CMMC give safeguarding; ITAR adds nationality gating, licensing, and registration on top.
8. **"We exposed data — now what?"** Contain, scope who could have accessed it, and strongly consider a voluntary self-disclosure — RTX's fully-disclosed 750 violations got half the record penalty suspended.

## References

| Reference | Detail |
|-----------|--------|
| 22 CFR 120–130 | ecfr.gov current edition (structure verified July 2026) |
| AECA | 22 U.S.C. 2778 |
| §120.54 encryption rule | 84 FR 70887 (effective Mar 25, 2020); Russia-reference cleanup 90 FR 29720 (Jul 7, 2025) |
| USML Targeted Revisions | 90 FR 5594 (IFR) / 90 FR 41778 (final, effective Sept 15, 2025) |
| AUKUS exemption | 89 FR 67270 (IFR, effective Sept 1, 2024); final rule 90 FR 61053 (Dec 30, 2025) |
| Registration fees | 89 FR 99081 (effective Jan 9, 2025) |
| Suppressors IFR | 91 FR 46279 (Jul 23, 2026; effective Nov 20, 2026) |
| DDTC Compliance Program Guidelines | pmddtc.state.gov compliance portal (Dec 2022; check portal for later revisions) |
| CUI Export Control category | archives.gov/cui/registry (CUI//SP-EXPT) |
| Consent agreements | state.gov press releases (Boeing, RTX, Precision Castparts, GE) |
