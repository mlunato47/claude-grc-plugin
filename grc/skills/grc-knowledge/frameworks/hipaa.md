# HIPAA — Health Insurance Portability and Accountability Act

## Overview

HIPAA (Public Law 104-191, 1996) is a federal law governing the privacy, security, and electronic exchange of health information. It is codified primarily at **45 CFR Parts 160 and 164**. The **Department of Health and Human Services (HHS)** administers HIPAA, with the **Office for Civil Rights (OCR)** serving as the primary enforcement body for the Privacy, Security, and Breach Notification Rules.

HIPAA applies to **Covered Entities** and their **Business Associates** that create, receive, maintain, or transmit **Protected Health Information (PHI)**. Unlike frameworks such as SOC 2 or ISO 27001, HIPAA is a legal mandate — non-compliance carries civil and criminal penalties.

**Key legislation and amendments**:
- **HIPAA (1996)** — Original statute establishing portability, privacy, and security requirements
- **HITECH Act (2009)** — Expanded enforcement, introduced breach notification, extended rules to Business Associates
- **Omnibus Rule (2013)** — Final rule implementing HITECH modifications, strengthened BA liability and breach definition

## HIPAA Rules

| Rule | CFR Citation | Purpose |
|------|-------------|---------|
| **Privacy Rule** | 45 CFR Part 164, Subpart E (§164.500–§164.534) | Establishes standards for the use and disclosure of PHI; grants patient rights (access, amendment, accounting of disclosures) |
| **Security Rule** | 45 CFR Part 164, Subpart C (§164.302–§164.318) | Requires administrative, physical, and technical safeguards for electronic PHI (ePHI) |
| **Breach Notification Rule** | 45 CFR Part 164, Subpart D (§164.400–§164.414) | Mandates notification to individuals, HHS, and media following a breach of unsecured PHI |
| **Enforcement Rule** | 45 CFR Part 160, Subparts C–E (§160.300–§160.552) | Defines investigation procedures, penalty determinations, and hearing processes |
| **Omnibus Rule (2013)** | 78 FR 5566 | Implements HITECH provisions: BA direct liability, modified breach standard, strengthened enforcement |

## Covered Entities vs. Business Associates

| Category | Definition | Examples |
|----------|-----------|----------|
| **Covered Entity (CE)** | Entity that conducts standard electronic health care transactions (45 CFR §160.103) | Health plans, health care clearinghouses, health care providers who transmit any health information electronically |
| **Business Associate (BA)** | Person or entity that performs functions or activities on behalf of (or provides services to) a CE involving PHI (45 CFR §160.103) | Cloud hosting providers, EHR vendors, billing companies, shredding services, consultants with PHI access |
| **Business Associate Subcontractor** | Entity that creates, receives, maintains, or transmits PHI on behalf of a BA | Downstream cloud providers, data analytics subcontractors |

Post-HITECH, Business Associates are **directly liable** for compliance with applicable Security Rule provisions, Breach Notification requirements, and certain Privacy Rule restrictions.

## Business Associate Agreements (BAAs)

A BAA is required under **§164.314(a)(2)** whenever a CE engages a BA, or when a BA engages a subcontractor, that will create, receive, maintain, or transmit PHI.

**Required BAA elements** (§164.314(a)(2)(i)):

| Element | Description |
|---------|-------------|
| Permitted uses/disclosures | Specify the uses and disclosures of PHI the BA is authorized to make |
| Safeguards assurance | BA must use appropriate safeguards to prevent unauthorized use or disclosure |
| Reporting obligations | BA must report breaches of unsecured PHI, security incidents, and unauthorized uses/disclosures |
| Subcontractor flow-down | BA must ensure subcontractors agree to the same restrictions and conditions |
| Individual access | BA must make PHI available to satisfy CE's obligations under §164.524 (right of access) |
| Amendment support | BA must make PHI available for amendment per §164.526 |
| Accounting of disclosures | BA must provide information required for accounting of disclosures under §164.528 |
| HHS access | BA must make internal practices, books, and records available to HHS for compliance determination |
| Return/destruction | BA must return or destroy all PHI at termination (where feasible) |
| Termination authority | CE must have the right to terminate the agreement if BA violates a material term |

## Security Rule Safeguards (45 CFR Part 164, Subpart C)

### Administrative Safeguards — §164.308

| Standard | CFR Citation | Implementation Specifications | R/A |
|----------|-------------|-------------------------------|-----|
| **Security Management Process** | §164.308(a)(1) | Risk analysis | R |
| | | Risk management | R |
| | | Sanction policy | R |
| | | Information system activity review | R |
| **Assigned Security Responsibility** | §164.308(a)(2) | Designate a security official | R |
| **Workforce Security** | §164.308(a)(3) | Authorization and/or supervision | A |
| | | Workforce clearance procedure | A |
| | | Termination procedures | A |
| **Information Access Management** | §164.308(a)(4) | Isolating healthcare clearinghouse functions | R |
| | | Access authorization | A |
| | | Access establishment and modification | A |
| **Security Awareness and Training** | §164.308(a)(5) | Security reminders | A |
| | | Protection from malicious software | A |
| | | Log-in monitoring | A |
| | | Password management | A |
| **Security Incident Procedures** | §164.308(a)(6) | Response and reporting | R |
| **Contingency Plan** | §164.308(a)(7) | Data backup plan | R |
| | | Disaster recovery plan | R |
| | | Emergency mode operation plan | R |
| | | Testing and revision procedures | A |
| | | Applications and data criticality analysis | A |
| **Evaluation** | §164.308(a)(8) | Periodic technical and nontechnical evaluation | R |
| **BAA Contracts and Other Arrangements** | §164.308(b)(1) | Written contract or other arrangement | R |

### Physical Safeguards — §164.310

| Standard | CFR Citation | Implementation Specifications | R/A |
|----------|-------------|-------------------------------|-----|
| **Facility Access Controls** | §164.310(a)(1) | Contingency operations | A |
| | | Facility security plan | A |
| | | Access control and validation procedures | A |
| | | Maintenance records | A |
| **Workstation Use** | §164.310(b) | (Standard only — no separate specifications) | R |
| **Workstation Security** | §164.310(c) | (Standard only — no separate specifications) | R |
| **Device and Media Controls** | §164.310(d)(1) | Disposal | R |
| | | Media re-use | R |
| | | Accountability | A |
| | | Data backup and storage | A |

### Technical Safeguards — §164.312

| Standard | CFR Citation | Implementation Specifications | R/A |
|----------|-------------|-------------------------------|-----|
| **Access Control** | §164.312(a)(1) | Unique user identification | R |
| | | Emergency access procedure | R |
| | | Automatic logoff | A |
| | | Encryption and decryption | A |
| **Audit Controls** | §164.312(b) | (Standard only — no separate specifications) | R |
| **Integrity** | §164.312(c)(1) | Mechanism to authenticate ePHI | A |
| **Person or Entity Authentication** | §164.312(d) | (Standard only — no separate specifications) | R |
| **Transmission Security** | §164.312(e)(1) | Integrity controls | A |
| | | Encryption | A |

### Organizational Requirements — §164.314

| Standard | CFR Citation | Description |
|----------|-------------|-------------|
| **Business Associate Contracts or Other Arrangements** | §164.314(a) | CE must obtain satisfactory assurances from BAs via written contract (see BAA section above) |
| **Requirements for Group Health Plans** | §164.314(b) | Group health plan documents must incorporate safeguards for ePHI disclosed to plan sponsors |

### Policies, Procedures, and Documentation Requirements — §164.316

| Standard | CFR Citation | Description |
|----------|-------------|-------------|
| **Policies and Procedures** | §164.316(a) | Implement reasonable and appropriate policies and procedures to comply with the Security Rule |
| **Documentation** | §164.316(b)(1) | Maintain written (electronic or paper) policies, procedures, actions, activities, and assessments required by the Security Rule |
| **Retention** | §164.316(b)(2) | Retain documentation for **6 years** from the date of creation or the date it was last in effect, whichever is later |

## Required vs. Addressable Implementation Specifications

| Designation | Obligation | CFR Reference |
|-------------|-----------|---------------|
| **Required (R)** | Must be implemented exactly as specified — no discretion | §164.306(d)(2) |
| **Addressable (A)** | Entity must assess whether the specification is reasonable and appropriate. Three outcomes: (1) implement as written, (2) implement an equivalent alternative measure, or (3) document why neither is reasonable and appropriate. **Addressable does not mean optional.** | §164.306(d)(3) |

All decisions regarding addressable specifications must be documented, including the rationale for the chosen approach. This documentation must be retained per §164.316(b)(2).

## Protected Health Information (PHI) — 18 Identifiers

PHI is **individually identifiable health information** (§160.103) held or transmitted by a CE or BA. The Privacy Rule identifies **18 identifiers** that make health information individually identifiable (per the Safe Harbor de-identification method, §164.514(b)(2)):

| # | Identifier | # | Identifier |
|---|-----------|---|-----------|
| 1 | Names | 10 | Account numbers |
| 2 | Geographic data smaller than a state | 11 | Certificate/license numbers |
| 3 | Dates (except year) related to an individual | 12 | Vehicle identifiers and serial numbers |
| 4 | Telephone numbers | 13 | Device identifiers and serial numbers |
| 5 | Fax numbers | 14 | Web URLs |
| 6 | Email addresses | 15 | IP addresses |
| 7 | Social Security numbers | 16 | Biometric identifiers |
| 8 | Medical record numbers | 17 | Full-face photographs and comparable images |
| 9 | Health plan beneficiary numbers | 18 | Any other unique identifying number, characteristic, or code |

**ePHI** (electronic PHI) is PHI that is created, received, maintained, or transmitted in electronic form. The Security Rule applies specifically to ePHI.

## Minimum Necessary Standard

Under **§164.502(b)** and **§164.514(d)**, CEs and BAs must make reasonable efforts to limit PHI to the **minimum necessary** to accomplish the intended purpose of the use, disclosure, or request.

**Exceptions** (minimum necessary does not apply to):
- Disclosures to or requests by a health care provider for treatment purposes
- Disclosures to the individual who is the subject of the PHI
- Uses or disclosures authorized by the individual
- Disclosures to HHS for enforcement purposes
- Uses or disclosures required by law
- Uses or disclosures required for HIPAA compliance

## Breach Notification Requirements (§164.400–§164.414)

A **breach** is the acquisition, access, use, or disclosure of unsecured PHI in a manner not permitted by the Privacy Rule that compromises the security or privacy of the PHI (§164.402).

### Presumption and Risk Assessment

Post-Omnibus Rule, an impermissible use or disclosure of PHI is **presumed to be a breach** unless the CE or BA demonstrates a low probability that the PHI was compromised, based on a risk assessment considering at least four factors (§164.402(2)):

| Factor | Description |
|--------|-------------|
| 1 | Nature and extent of the PHI involved (types of identifiers, likelihood of re-identification) |
| 2 | The unauthorized person who used the PHI or to whom the disclosure was made |
| 3 | Whether the PHI was actually acquired or viewed |
| 4 | Extent to which the risk to the PHI has been mitigated |

### Notification Requirements

| Notification Target | Trigger | Timeline | Method | CFR Citation |
|---------------------|---------|----------|--------|-------------|
| **Affected individuals** | Any breach of unsecured PHI | Without unreasonable delay, no later than **60 days** after discovery | Written notice by first-class mail (or email if individual agreed); substitute notice if contact info insufficient | §164.404 |
| **HHS (Secretary)** | Breach affecting **fewer than 500** individuals | Annual log submitted no later than **60 days after the end of the calendar year** | Via HHS breach reporting portal | §164.408 |
| **HHS (Secretary)** | Breach affecting **500 or more** individuals | Without unreasonable delay, no later than **60 days** after discovery | Via HHS breach reporting portal | §164.408 |
| **Prominent media** | Breach affecting **500 or more** residents of a state or jurisdiction | Without unreasonable delay, no later than **60 days** after discovery | Press release or equivalent to prominent media outlets in the affected jurisdiction | §164.406 |

### Breach Exceptions (§164.402(1))

| Exception | Description |
|-----------|-------------|
| Unintentional acquisition | Good-faith, unintentional acquisition, access, or use by a workforce member acting under the CE or BA's authority |
| Inadvertent disclosure | Inadvertent disclosure between authorized persons at the same CE, BA, or OHCA |
| Good-faith belief | Recipient could not reasonably retain the information |

## HITECH Act Enhancements (2009)

The **Health Information Technology for Economic and Clinical Health (HITECH) Act** (Title XIII of ARRA, Public Law 111-5) significantly expanded HIPAA:

| Enhancement | Description |
|-------------|-------------|
| **BA direct liability** | BAs are directly subject to Security Rule standards and certain Privacy Rule requirements; subject to civil and criminal penalties |
| **Breach notification** | Established the Breach Notification Rule (§164.400–§164.414) |
| **Increased penalties** | Established tiered penalty structure with substantially higher maximums |
| **State AG enforcement** | Authorized state Attorneys General to bring civil actions for HIPAA violations on behalf of state residents |
| **Willful neglect** | HHS required to investigate complaints involving willful neglect; mandatory penalties for uncorrected willful neglect |
| **Accounting of disclosures for EHRs** | Extended accounting-of-disclosures rights to treatment, payment, and health care operations disclosures from EHRs |
| **Marketing/fundraising restrictions** | Strengthened consent requirements for marketing and fundraising communications |
| **Sale of PHI** | Prohibited the sale of PHI without individual authorization |
| **Audit program** | Required HHS to perform periodic audits of CE and BA compliance |

## Penalty Tiers

Civil monetary penalties under HIPAA are structured in four tiers based on the level of knowledge and culpability (§160.404).

| Tier | Level of Culpability | Minimum per Violation | Maximum per Violation | Annual Cap |
|------|---------------------|----------------------|----------------------|------------|
| **1** | Did not know (and, by exercising reasonable diligence, would not have known) | $100 | $50,000 | $25,000 |
| **2** | Reasonable cause (not willful neglect) | $1,000 | $50,000 | $100,000 |
| **3** | Willful neglect — corrected within required time period | $10,000 | $50,000 | $250,000 |
| **4** | Willful neglect — not corrected within required time period | $50,000 | $50,000 | $1,500,000 |

*Base statutory amounts per 42 U.S.C. §1320d-5 as amended by HITECH. HHS adjusts these amounts annually for inflation per 45 CFR §160.404 — check the latest Federal Register notice for current inflation-adjusted figures. Criminal penalties (§1177 of the Social Security Act) can reach up to $250,000 and 10 years imprisonment for offenses committed with intent to sell, transfer, or use PHI for commercial advantage, personal gain, or malicious harm.*

## Risk Analysis Requirements — §164.308(a)(1)(ii)(A)

The risk analysis is the foundational requirement of the HIPAA Security Rule. OCR has cited failure to conduct an adequate risk analysis as the most common finding in enforcement actions and audits.

**Required elements** (per HHS guidance and OCR enforcement expectations):

| Element | Description |
|---------|-------------|
| **Scope** | Encompasses all ePHI the entity creates, receives, maintains, or transmits — all electronic media, systems, and locations |
| **Data collection** | Identify where ePHI is stored, received, maintained, and transmitted |
| **Threat identification** | Identify and document reasonably anticipated threats to ePHI (natural, human, environmental) |
| **Vulnerability identification** | Identify and document vulnerabilities that could be exploited by identified threats |
| **Current controls assessment** | Evaluate existing security measures protecting ePHI |
| **Likelihood determination** | Assess the probability that each identified threat will exploit a given vulnerability |
| **Impact analysis** | Determine the potential impact if a threat exploits a vulnerability (on confidentiality, integrity, availability) |
| **Risk level determination** | Assign risk levels based on the combination of likelihood and impact |
| **Documentation** | Document the risk analysis methodology, findings, and resulting risk levels |
| **Review cycle** | Periodic review and updates — particularly when there are environmental or operational changes |

**Common deficiencies cited by OCR**:
- Conducting only a gap assessment instead of a full risk analysis
- Failing to include all ePHI environments (overlooking mobile devices, legacy systems, cloud services)
- Not documenting the analysis or its methodology
- Treating risk analysis as a one-time activity rather than an ongoing process
- Failing to address identified risks through the risk management process (§164.308(a)(1)(ii)(B))

## Common HIPAA Violations and Enforcement Trends

| Violation Category | Description | Typical Enforcement Outcome |
|-------------------|-------------|---------------------------|
| **Failure to perform risk analysis** | No documented risk analysis or incomplete scope | Most frequently cited; settlement amounts range from $100K to $6.85M |
| **Lack of BAAs** | Engaging vendors with PHI access without executed BAAs | Resolution agreements with corrective action plans |
| **Insufficient access controls** | Excessive user privileges, shared credentials, lack of MFA | Settlements + mandated corrective action |
| **Missing encryption** | Unencrypted ePHI on portable devices (laptops, USB drives) | Common trigger for breach investigations; significant settlement amounts |
| **Improper disposal** | PHI found in dumpsters, on resold devices, or in accessible locations | Resolution agreements, civil monetary penalties |
| **Lack of audit controls/log review** | No audit logging or failure to review access logs for unauthorized activity | Corrective action plans with monitoring |
| **Denial of patient access** | Failing to provide individuals access to their PHI within 30 days (§164.524) | OCR Right of Access Initiative; penalties from $3,500 to $240,000 |
| **Insufficient training** | No security awareness training program or failure to document training | Corrective action plans |
| **Impermissible disclosures** | Unauthorized sharing of PHI (social media, unencrypted email, verbal) | Varies by scope; significant penalties for large-scale disclosures |
| **Failure to mitigate** | No action taken after a known breach or security incident | Aggravating factor in settlement negotiations |

## Key NIST Crosswalk

NIST published **SP 800-66 Rev 2** (February 2024) as the primary mapping between HIPAA Security Rule and NIST Cybersecurity Framework / 800-53 Rev 5. Key mappings:

| HIPAA Security Rule Standard | Primary NIST 800-53 Rev 5 Controls |
|-----------------------------|-------------------------------------|
| §164.308(a)(1) Security Management Process | RA-3, RA-5, PM-4, PL-2, SI-2, SI-5 |
| §164.308(a)(2) Assigned Security Responsibility | PM-2, PS-2 |
| §164.308(a)(3) Workforce Security | PS-2, PS-4, PS-5, PS-7 |
| §164.308(a)(4) Information Access Management | AC-1, AC-2, AC-3, AC-6 |
| §164.308(a)(5) Security Awareness and Training | AT-1, AT-2, AT-3, AT-4 |
| §164.308(a)(6) Security Incident Procedures | IR-1, IR-2, IR-4, IR-5, IR-6 |
| §164.308(a)(7) Contingency Plan | CP-1 through CP-10 |
| §164.308(a)(8) Evaluation | CA-2, CA-7 |
| §164.310(a)(1) Facility Access Controls | PE-1 through PE-6, PE-8 |
| §164.310(d)(1) Device and Media Controls | MP-2, MP-4, MP-5, MP-6, MP-7 |
| §164.312(a)(1) Access Control | AC-2, AC-3, AC-7, AC-11, SC-13 |
| §164.312(b) Audit Controls | AU-2, AU-3, AU-6, AU-11, AU-12 |
| §164.312(c)(1) Integrity | SI-7, SI-10 |
| §164.312(d) Person or Entity Authentication | IA-1 through IA-5, IA-8 |
| §164.312(e)(1) Transmission Security | SC-8, SC-13, SC-23 |

> Deep dive: `mappings/nist-to-hipaa.md` for full control-level mapping

## Abbreviations

| Abbreviation | Meaning |
|-------------|---------|
| BA | Business Associate |
| BAA | Business Associate Agreement |
| CE | Covered Entity |
| ePHI | Electronic Protected Health Information |
| HHS | Department of Health and Human Services |
| HITECH | Health Information Technology for Economic and Clinical Health Act |
| OCR | Office for Civil Rights |
| PHI | Protected Health Information |
