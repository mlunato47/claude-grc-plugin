# DoD Authority Chains, AO Roles, and eMASS Routing

Reference for the ATO acceleration engine. Maps each DoD component to its authorization authority chain, typical AO role, eMASS tenant, and process nuances. Use this to tailor the ATO plan to the correct organizational chain.

---

## How DoD Authorization Authority Works

Every DoD system must have an **Authorizing Official (AO)** — the senior official who accepts residual risk on behalf of the organization and signs the ATO letter. The AO cannot be the ISSO or ISSM. The AO is typically an SES or General/Flag Officer, or a designated civilian equivalent.

**The Chain:**
```
Mission Owner / Program Manager (PM)
      ↓ (sponsors the system)
ISSO (Information System Security Officer)
      ↓ (owns day-to-day security, builds the package)
ISSM (Information System Security Manager)
      ↓ (reviews and endorses package)
SCA (Security Control Assessor)
      ↓ (independently assesses controls)
AO (Authorizing Official)
      ↓ (reviews risk, signs ATO letter or delegates DATO/IATT/IATO)
SISO (Senior Information Security Officer)
      ↓ (organizational oversight, policy)
DoD CIO
      ↓ (policy and oversight at DoD level)
```

**Key roles:**
- **ISSO**: The person who builds and maintains the ATO package, runs eMASS, coordinates evidence
- **ISSM**: Oversees ISSOs; has broader scope (may manage multiple systems)
- **SCA (or SCA-R)**: Independent assessor — may be internal or external (third party)
- **AO**: Signs the ATO. Cannot be waived away. Every system needs one.

---

## Army

**Senior Authority**: Army CIO/G-6 (Chief Information Officer / G-6)
**Operational oversight**: ARCYBER — Army Cyber Command (manages Army RMF/ATO at enterprise level)
**Program-level AO**: Designated by Program Executive Officer (PEO) or Program Manager (PM); typically a Colonel (O-6) or SES equivalent

**Typical chain for a program:**
```
PM / Mission Owner
↓
ISSO (contractor or government)
↓
ISSM (organic to program office or RCERT)
↓
SCA (Army Authorizing Official Support Environment — AOSE, or third party)
↓
AO (designated by PEO — typically PM or Deputy PM with delegated authority)
↓
ARCYBER oversight (reviews Army-wide)
```

**eMASS tenant**: Army eMASS — accessed at `rcm.army.mil/emass` (NIPRNet access required)
- Army eMASS is a separate instance from Air Force/Navy/other components
- Contractors must use Army VPN or be on .mil network to access
- System must be registered in correct Army eMASS tenant (by organization/PEO)

**eMASS registration for Army:**
1. Access Army eMASS (requires Army-issued PKI certificate or sponsor)
2. Create new system record: System name, Mission owner, Criticality (Mission Critical / Mission Essential / Administrative)
3. Enter system categorization (FIPS 199 values)
4. Assign ISSO and AO roles
5. Generate Control Implementation Summary (CIS)
6. Upload SSP, SAP, SAR, POA&M in required format

**Package components (Army-specific):**
- Standard package: SSP, SAR, POA&M, CRM (if leveraging inheritance)
- Army-specific: Interconnection Security Agreements (ISAs) for any Army network connections
- For ARCYBER-connected systems: network connection approval required separately
- Army Accreditation Package review by ARCYBER staff before AO signs for high-value systems

**ConMon for Army:**
- Monthly vulnerability scans (ACAS/Nessus) reported to ARCYBER
- Quarterly POA&M updates in eMASS
- Annual eMASS review and authorization renewal

**Reciprocity stance**: Army will consider reciprocity from other DoD components but typically requires ISSO/ISSM review of the original package. Not rubber-stamp; expect 2-5 days review.

**Typical ATO timeline (complete package to signature)**: 15-45 days depending on AO availability and system complexity. Simple apps with clean scan results: 15-20 days. Complex systems with open findings: 30-45 days.

---

## Navy (includes NAVSEA, NAVAIR, NAVWAR, NAVSUP, ONR)

**Senior Authority**: DON CIO (Department of the Navy Chief Information Officer)
**Navy CISO**: Reports to DON CIO
**Operational oversight**: NAVWAR (Naval Information Warfare Systems Command) — manages Navy eMASS and RMF process
**Program-level AO**: Designated per Program; major commands (NAVSEA, NAVAIR) have their own AO structures

**Typical chain for a Navy program:**
```
PM / Mission Owner
↓
ISSO
↓
ISSM (at command level)
↓
SCA (third party or internal NAVWAR team)
↓
AO (Program Executive Office designation — e.g., PEO C4I, PEO IWS)
↓
NAVWAR / DON CIO oversight
```

**eMASS tenant**: Navy eMASS — managed by NAVWAR
- Accessed through NAVWAR IT services (NIPRNet)
- Different instance from Army eMASS — do not confuse tenants
- USMC uses a separate MARFORCYBER-managed eMASS instance (but same underlying platform)

**Package components (Navy-specific):**
- Standard package plus: System-specific Privacy Impact Assessment (PIA) if PII involved
- Navy requires signed Memorandum of Agreement (MOA) for any cross-command system connections
- Ports, Protocols, and Services Management (PPSM) registration required for any network-accessible ports
- Waivers for non-standard ports submitted through NAVWAR PPSM process

**PPSM (Ports, Protocols, Services Management):**
- Every open port on a Navy system must be registered in PPSM database
- Standard ports (443, 80, 22, etc.) are pre-approved; non-standard require waiver
- PPSM registration is separate from the eMASS package but required before ATO
- This is a common surprise for teams new to Navy — start PPSM early

**ConMon for Navy:**
- Scan results submitted to NAVWAR Security Operations
- POA&M management in Navy eMASS
- Annual authorization renewal

**Reciprocity**: Navy will accept Navy-internal ATOs readily. Cross-component ATOs (from Army, AF, etc.) require review and approval from NAVWAR — expect 5-10 business days.

**USMC specifics:**
- Authority: HQMC C4/DIRSSCAM (Director, Security, Service and Cybersecurity)
- Oversight: MARFORCYBER
- eMASS: USMC eMASS instance managed by MARFORCYBER
- Process mirrors Navy RMF but with USMC-specific policy overlays

**Typical timeline**: 20-40 days from complete package to AO signature. PPSM adds 1-2 weeks if not started early.

---

## Air Force (includes AFMC, AFLCMC, AFSPC programs)

**Senior Authority**: SAF/CN (Secretary of the Air Force, Chief of Information Dominance and Chief Information Officer)
**Operational oversight**: AFCYBER (Air Forces Cyber, subordinate to ACC) — manages AF cyberspace operations and ATO enterprise
**Program-level AO**: Typically at Wing, Center, or Product Center level; AFLCMC programs have PEO-designated AOs

**Typical chain for an AF program:**
```
PM / Mission Owner
↓
ISSO
↓
ISSM (at unit or program office level)
↓
SCA (Wing/Center IA team or contracted 3PAO)
↓
AO (Designated by Product Center or Wing Commander — O-7/O-8 or SES equivalent)
↓
AFCYBER oversight
```

**eMASS tenant**: Air Force eMASS
- Accessed through AF network (NIPRNet or AFNET VPN)
- AF uses JAFAN-compliant eMASS instance for classified systems (separate)
- Platform One (P1) systems are typically registered in AF eMASS (AFLCMC oversight)

**Platform One specific (AF):**
- P1 is managed by AFLCMC/HNA (Hanscomb Air Force Base)
- P1 CTSO holds the Cloud One / Platform One ATO under AF authority
- Mission apps on P1: Register in AF eMASS; reference P1's ATO as parent; leverage P1 CRM
- P1 has a streamlined ATO process: P1 CTSO reviews app intake → approves → mission ISSO completes residual controls

**Package components (AF-specific):**
- Standard package plus: Mission System Criticality designation (MSCL 1-5)
- Critical Program Information (CPI) designation if applicable (acquisition-sensitive)
- For AFNET-connected systems: Connection Approval Package (CAP) required through AFCYBER
- CONOP approval for any cloud deployment (Cloud First policy documentation)

**AF ConMon:**
- Scan results via ACAS to AFCYBER SOC
- Monthly POA&M updates
- Annual authorization renewal in AF eMASS

**Space Force (USSF):**
- Authority: USSF CIO / S6
- Operational oversight: SpOC (Space Operations Command) Cyber Ops
- eMASS: USSF is still maturing its own eMASS instance; many USSF programs currently use AF eMASS
- Space system ATOs may require additional CSfC (Commercial Solutions for Classified) reviews for ground systems
- Space Force is building out its own RMF process — expect policy evolution in 2024-2026

**Typical timeline**: 15-30 days for simple apps on P1. 30-60 days for complex programs. AF is generally faster than Navy for cloud-native apps due to P1 maturity.

---

## Marine Corps

**Senior Authority**: HQMC C4/DIRSSCAM (Commandant's office C4 Director)
**Operational oversight**: MARFORCYBER (Marine Forces Cyber Command)
**Program-level AO**: Marine Corps program AOs designated by I MEF, II MEF, III MEF, or TECOM as applicable

**eMASS**: USMC eMASS (separate instance, managed by MARFORCYBER)

**Process notes:**
- Marine Corps follows DoD RMF aligned with Navy (same DON CIO umbrella)
- MARFORCYBER reviews packages and coordinates with NAVWAR for enterprise awareness
- Ground-tactical systems may go through MARCENT/MARFORPAC instead of MARFORCYBER
- Marines tend to have faster ATO timelines for smaller tactical systems vs. large enterprise IT

**Typical timeline**: 15-35 days.

---

## SOCOM (United States Special Operations Command)

**Senior Authority**: USSOCOM J6 (Director, Command, Control, Communications and Computers)
**Operational oversight**: SOCOM J62 (Cybersecurity branch under J6)
**AO designation**: USSOCOM AO for SOCOM-owned systems; component commands (JSOC, AFSOC, MARSOC, NAVSPECWARCOM, USASOC, SWCS) have sub-AO structures

**eMASS**: SOCOM has its own eMASS tenant, managed by J62

**Process notes:**
- SOCOM operates with more speed and flexibility than conventional force, but ATO process is still RMF-compliant
- SOCOM frequently deploys unique tactical technologies — expect non-standard deployment environments
- Classified (IL6) systems common at SOCOM; these go through a separate classified ATO process
- SOCOM will often accept reciprocity from other DoD components after abbreviated review
- Operational urgency: SOCOM can execute IATT (Interim Authority to Test) faster than most components for operationally urgent systems

**Typical timeline**: 10-25 days for systems with strong sponsorship. Operational urgency can compress to 5-10 days for IATT.

---

## DISA (Defense Information Systems Agency)

**Senior Authority**: DISA Director (civilian SES or General Officer)
**Operational oversight**: DISA IASE (Information Assurance Support Environment) and DISA Cybersecurity
**AO**: DISA Designated Authorizing Official (DAO) for DISA-operated systems

**Dual role**: DISA is both a system owner/AO for its own systems AND the authorizing body for Cloud Service Providers under the DoD CC SRG. Two different processes:

**DISA-owned system ATO:**
- Register in DISA eMASS
- DISA IASE manages the process
- Typical timeline: 20-45 days

**Cloud Service Provider seeking DoD-wide authorization (DISA PA):**
- CSP submits to DISA Cloud Security Review (DCSR) process
- Requires FedRAMP P-ATO as prerequisite
- DISA performs additional DoD CC SRG assessment
- Results in Provisional Authorization (PA) at specific IL (IL2, IL4, or IL5)
- PA is listed on DISA Cloud Service Catalog (publicly searchable)
- This is what gives CSPs like AWS GovCloud and Azure Government their IL4/IL5 status
- Timeline: 6-12 months (not relevant for mission apps; relevant only for CSPs)

**For mission apps using DISA-hosted services (MilCloud 2.0):**
- DISA MilCloud 2.0 has its own ATO held by DISA
- Mission app teams inherit DISA's infrastructure ATO
- Mission app registers in their own component's eMASS (Army/AF/Navy) — NOT DISA eMASS
- Reference DISA MilCloud CRM in SSP for inherited controls
- Download MilCloud CRM from DISA STOREFRONT

---

## DIA (Defense Intelligence Agency)

**Authority**: DIA Information Systems Security Manager (ISSM at enterprise level)
**Oversight**: DIA CISO, DIARMF process
**ATO process**: DIARMF (DIA Risk Management Framework) — based on NIST 800-37 but with IC overlay

**Notes:**
- DIA systems often carry intelligence information — higher classification common
- DIARMF has additional requirements vs. standard DoD RMF for IC-connected systems
- IC Technical Specifications (ICS) may apply in addition to DoD policy
- DIA will typically not accept DoD-side ATOs without full review

---

## eMASS General Reference

**What is eMASS**: Enterprise Mission Assurance Support Service — DoD-wide platform for managing RMF package lifecycle. Every ATO package lives in eMASS (unclassified systems).

**eMASS data entry requirements (all components):**

*System Registration:*
- System name and abbreviation
- Mission/function description (50-200 words)
- System owner organization (down to branch/directorate)
- System criticality level (Mission Critical / Mission Essential / Administrative & Support)
- System type (Major IS / Minor IS / Platform IT / DoD IT)
- Operational status (Operational / Under Development / Major Modification)
- Deployment environment (Cloud / On-Premises / Hybrid / Tactical)

*Categorization (FIPS 199 / CNSSI 1253):*
- Confidentiality impact: Low / Moderate / High
- Integrity impact: Low / Moderate / High
- Availability impact: Low / Moderate / High
- Overall categorization: High-water mark of all three
- Rationale for each (1-2 sentences per dimension)

*Controls:*
- Apply baseline (eMASS auto-populates based on categorization)
- Tailor controls: scoping, overlays, compensating controls
- Enter control implementation for each applicable control
- Mark controls Inherited / Hybrid / System-Specific
- Link evidence artifacts to controls

*Package:*
- Upload: SSP (or link to eMASS-native fields), SAP, SAR, POA&M, CRM, Contingency Plan
- Attach scan results (ACAS/Nessus .nessus files or HTML reports)
- Enter system interconnections
- List personnel (ISSO, ISSM, AO, SCA)

*Authorization:*
- AO reviews package in eMASS
- AO submits authorization decision (ATO / IATO / IATT / DATO)
- Authorization letter generated in eMASS
- ATO expiration date set (typically 1-3 years depending on component policy)

**Common eMASS mistakes that delay ATO:**
1. Registering in the wrong component's eMASS tenant (Army ISSO registers in AF eMASS by mistake)
2. Incomplete FIPS 199 rationale — every dimension needs a sentence
3. Leaving control narratives blank ("see SSP" without uploading SSP)
4. Not marking which controls are inherited vs. system-specific (eMASS requires this)
5. Uploading scans as password-protected PDFs (eMASS requires parseable format)
6. AO not assigned in eMASS before package is "submitted" — AO can't see it to sign

---

## Reciprocity Quick Reference

DoD reciprocity policy (DoDI 8510.01): DoD components should accept ATOs from other components without requiring a complete reassessment, as long as the operational environment is equivalent.

**In practice:**

| From → To | Typical Reciprocity |
|-----------|---------------------|
| AF → AF | Automatic (same AO chain) |
| Army → Army | Automatic |
| Navy → Navy | Automatic |
| AF → Army | Usually accepted after brief review (2-5 days) |
| AF → Navy | Usually accepted after review (5-10 days) |
| Army → SOCOM | Usually accepted; SOCOM J62 reviews |
| FedRAMP P-ATO → DoD IL2 | Straightforward; need to add DoD-specific controls |
| FedRAMP High P-ATO → DoD IL4 | Accepted as baseline; add IL4 delta controls |
| FedRAMP High → IL5 | Must add IL5-specific requirements on top; not automatic |
| Commercial ATO → DoD | Not accepted; DoD uses NIST/RMF; commercial ATOs don't satisfy DoD requirements |

**How to leverage reciprocity:**
1. Obtain the existing ATO letter and package summary from the originating component
2. Identify delta controls (what the new environment adds that the old ATO didn't cover)
3. Document the delta in a Reciprocity Acceptance Memorandum
4. AO reviews delta and signs acceptance
5. Register in your eMASS tenant referencing the original ATO
