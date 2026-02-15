# Cross-Framework Mapping Matrix

## NIST 800-53 as the Universal Mapping Hub

NIST SP 800-53 Rev 5 serves as the canonical reference taxonomy for security and privacy controls. Rather than maintaining direct mappings between every pair of frameworks (an N-by-N problem), the industry-standard approach maps each framework to and from NIST 800-53, reducing the problem to N-by-2 lookups.

This matrix provides a **family-level** index. Each row represents one of the 20 NIST 800-53 control families. Each column shows the corresponding domain, category, requirement, or control area from the target framework. Use this table to quickly identify where a NIST family's concerns are addressed in another framework, then consult the detailed mapping files for control-level precision.

## How to Use This Matrix

1. **Find the NIST 800-53 family** in the left column (e.g., AC for Access Control)
2. **Read across the row** to the target framework column
3. **Note the identifiers** listed in that cell -- these are the domains, criteria, requirements, or control areas that address the same concerns
4. **Consult the detailed mapping file** (e.g., `nist-to-soc2.md`) for control-by-control mappings within that family

### Example: Forward Lookup (NIST to Target)

To find the ISO 27001 equivalent of NIST IR (Incident Response): locate the IR row, read across to the ISO 27001 column, and find A.5.24 through A.5.28 and A.6.8. These are the Annex A controls addressing incident management, reporting, and learning from incidents.

### Example: Reverse Lookup (Target to NIST)

To find what NIST family covers PCI DSS Requirement 10 (Log and Monitor All Access): scan the PCI DSS column for "Req 10" and find it in the AU (Audit & Accountability) row. This tells you the NIST AU family contains the controls most relevant to PCI DSS logging requirements.

### Example: Cross-Framework Bridge (Non-NIST to Non-NIST)

To map SOC 2 CC6.1 to ISO 27001: first find CC6.1 in the SOC 2 column (it appears in the AC, IA, MA, MP, PE, and SC rows), then read across those rows to the ISO 27001 column. This reveals that CC6.1's broad logical and physical access concerns span multiple ISO 27001 Annex A controls across organizational (5.x), physical (7.x), and technological (8.x) themes.

## Mapping Matrix

| NIST 800-53 Family | SOC 2 TSC | ISO 27001:2022 Annex A | PCI DSS v4.0.1 | HIPAA Security Rule | CIS Controls v8 | CMMC 2.0 / 800-171 | CSA CCM v4 | COBIT 2019 | GDPR |
|---|---|---|---|---|---|---|---|---|---|
| **AC** - Access Control | CC6.1, CC6.2, CC6.3 | A.5.15, A.5.18, A.8.2, A.8.3, A.8.4, A.8.5 | Req 7, Req 8 | 164.312(a)(1), 164.312(d) | CIS 3, CIS 5, CIS 6 | 3.1 (AC) | IAM-01 to IAM-16, IVS-03 | DSS05.04, DSS05.05 | Art. 5(1)(f), Art. 32 |
| **AT** - Awareness & Training | CC1.4, CC2.2 | A.6.3 | Req 12.6 | 164.308(a)(5) | CIS 14 | 3.2 (AT) | HRS-09, HRS-10, HRS-11 | APO07.03, APO07.04 | Art. 39, Art. 47 |
| **AU** - Audit & Accountability | CC7.1, CC7.2, CC7.3 | A.8.15, A.8.16, A.8.17 | Req 10 | 164.312(b) | CIS 8 | 3.3 (AU) | LOG-01 to LOG-13 | DSS05.07, MEA01, MEA02 | Art. 5(2), Art. 30 |
| **CA** - Assessment, Authorization & Monitoring | CC4.1, CC4.2, CC3.2 | A.5.35, A.5.36 | Req 11, Req 12.4 | 164.308(a)(8) | CIS 18 | 3.12 (CA) | A&A-01 to A&A-03, GRC-01 to GRC-05 | MEA01, MEA02, MEA03 | Art. 35, Art. 36 |
| **CM** - Configuration Management | CC7.1, CC8.1 | A.8.9, A.8.19, A.8.32 | Req 1, Req 2 | 164.310(d)(2)(iii) | CIS 4 | 3.4 (CM) | CCC-01 to CCC-09, IVS-04 | BAI10.01 to BAI10.05 | Art. 25, Art. 32 |
| **CP** - Contingency Planning | A1.1, A1.2, A1.3 | A.5.29, A.5.30, A.8.13, A.8.14 | Req 12.10.2 | 164.308(a)(7) | CIS 11, CIS 17 | -- | BCR-01 to BCR-11 | DSS04.01 to DSS04.08 | Art. 32(1)(b), Art. 32(1)(c) |
| **IA** - Identification & Authentication | CC6.1, CC6.2 | A.5.16, A.5.17, A.8.5 | Req 8 | 164.312(d) | CIS 5, CIS 6 | 3.5 (IA) | IAM-01 to IAM-16 | DSS05.04 | Art. 32 |
| **IR** - Incident Response | CC7.3, CC7.4, CC7.5 | A.5.24, A.5.25, A.5.26, A.5.27, A.5.28, A.6.8 | Req 12.10 | 164.308(a)(6) | CIS 17 | 3.6 (IR) | SEF-01 to SEF-08 | DSS02.01 to DSS02.07 | Art. 33, Art. 34 |
| **MA** - Maintenance | CC6.1, CC6.2, CC7.1 | A.7.13, A.8.9 | Req 6.3, Req 9.5 | 164.310(a)(2)(iv) | CIS 4, CIS 7 | 3.7 (MA) | IVS-04, IVS-05 | DSS01.04, BAI03 | Art. 32 |
| **MP** - Media Protection | CC6.1, CC6.5, CC6.7 | A.7.9, A.7.10, A.7.14, A.8.10 | Req 3.5, Req 9.4 | 164.310(d)(1), 164.312(c)(1) | CIS 3 | 3.8 (MP) | DSP-01, DSP-04, DSP-18 | DSS05.06, BAI09 | Art. 5(1)(f), Art. 17 |
| **PE** - Physical & Environmental | CC6.4, CC6.5 | A.7.1, A.7.2, A.7.3, A.7.4, A.7.5, A.7.6, A.7.8, A.7.11, A.7.12 | Req 9 | 164.310(a), 164.310(b), 164.310(c) | -- | 3.10 (PE) | DCS-01 to DCS-09 | DSS01.04, DSS01.05, DSS05.05 | Art. 32 |
| **PL** - Planning | CC3.1, CC5.1 | A.5.1, A.5.2, A.5.4 | Req 12.1, Req 12.3 | 164.308(a)(1)(i) | CIS 18 | -- | GRC-01 to GRC-05 | APO02, APO12 | Art. 24, Art. 35 |
| **PM** - Program Management | CC1.1, CC1.2, CC1.3, CC5.3 | A.5.1, A.5.2, A.5.3, A.5.4, A.5.31 | Req 12.1, Req 12.4, Req 12.5 | 164.308(a)(1)(i), 164.308(a)(2) | CIS 18 | -- | GRC-01 to GRC-08, STA-01 to STA-14 | EDM01, EDM03, APO01, APO13 | Art. 24, Art. 37, Art. 38, Art. 39 |
| **PS** - Personnel Security | CC1.4, CC6.1 | A.6.1, A.6.2, A.6.4, A.6.5, A.6.6 | Req 12.7 | 164.308(a)(3) | CIS 14 | 3.9 (PS) | HRS-01 to HRS-08 | APO07.01, APO07.06 | Art. 32, Art. 39 |
| **PT** - PII Processing & Transparency | P6.1, P6.2, P6.5, P7.1, P8.1 | A.5.34 | Req 3.1, Req 3.2 | 164.520, 164.522, 164.524, 164.526, 164.528 *(Privacy Rule)* | -- | -- | DSP-01 to DSP-19 | APO01.08, EDM01 | Art. 5, Art. 6, Art. 12-22, Art. 30 |
| **RA** - Risk Assessment | CC3.1, CC3.2, CC3.3, CC3.4 | A.5.7, A.8.8, A.8.34 | Req 6.1, Req 11 | 164.308(a)(1)(ii)(A), 164.308(a)(1)(ii)(B) | CIS 7, CIS 16 | 3.11 (RA) | GRC-02, TVM-01 to TVM-10 | APO12.01 to APO12.06 | Art. 35, Art. 36 |
| **SA** - System & Services Acquisition | CC3.2, CC9.2 | A.5.8, A.5.19, A.5.20, A.5.21, A.5.22, A.5.23, A.8.25, A.8.26, A.8.27, A.8.30, A.8.31 | Req 6, Req 12.8 | 164.308(b)(1), 164.314(a) | CIS 15, CIS 16, CIS 18 | -- | STA-01 to STA-14, AIS-01 to AIS-07 | BAI02, BAI03, APO10 | Art. 28, Art. 35 |
| **SC** - System & Communications Protection | CC6.1, CC6.6, CC6.7, CC6.8 | A.5.14, A.8.20, A.8.21, A.8.22, A.8.23, A.8.24, A.8.26 | Req 1, Req 4 | 164.312(a)(2)(iv), 164.312(e)(1) | CIS 3, CIS 12, CIS 13 | 3.13 (SC) | IVS-01 to IVS-13, CEK-01 to CEK-21, UEM-01 to UEM-14 | DSS05.02, DSS05.03 | Art. 5(1)(f), Art. 32 |
| **SI** - System & Information Integrity | CC7.1, CC7.2, CC7.4 | A.5.7, A.8.7, A.8.8, A.8.16 | Req 5, Req 6.2, Req 11.3, Req 11.5 | 164.308(a)(1)(ii)(D), 164.308(a)(5)(ii)(B) | CIS 7, CIS 10, CIS 13 | 3.14 (SI) | TVM-01 to TVM-10, IVS-07 | DSS05.01, DSS05.03 | Art. 5(1)(f), Art. 32 |
| **SR** - Supply Chain Risk Management | CC9.2 | A.5.19, A.5.20, A.5.21, A.5.22, A.5.23 | Req 12.8, Req 12.9 | 164.308(b)(1), 164.314(a) | CIS 15, CIS 16 | -- | STA-01 to STA-14 | APO10.01 to APO10.05, EDM03 | Art. 28, Art. 44-49 |

## Framework Column Key

**SOC 2 TSC** -- Trust Services Criteria per the AICPA 2017 framework. CC = Common Criteria (maps to Security). A1 = Availability. P-series = Privacy. Criteria are shared across all five categories (Security, Availability, Processing Integrity, Confidentiality, Privacy).

**ISO 27001:2022 Annex A** -- 93 controls organized into four themes: 5.x (Organizational, 37 controls), 6.x (People, 8 controls), 7.x (Physical, 14 controls), 8.x (Technological, 34 controls).

**PCI DSS v4.0.1** -- 12 top-level requirements. "Req" numbers refer to the requirement group; sub-requirement numbers indicate more specific sections.

**HIPAA Security Rule** -- References are to 45 CFR Part 164, Subparts C and E. Format: 164.3xx denotes Administrative (308), Physical (310), Technical (312), and Organizational (314) safeguard standards.

**CIS Controls v8** -- 18 control groups containing 153 individual safeguards. Numbers reference the top-level control group (e.g., CIS 5 = Account Management). Implementation Groups (IG1/IG2/IG3) determine which safeguards apply.

**CMMC 2.0 / 800-171** -- The "3.x" references map to NIST SP 800-171 Rev 2 security requirement families. CMMC Level 2 directly adopts all 110 requirements from 800-171. Cells marked "--" indicate NIST 800-53 families excluded from 800-171 (CP, PL, PM, SA, PT, SR). For CIS Controls, PE has no CIS equivalent (CIS does not address physical security). See `nist-to-cmmc.md` for the complete exclusion list.

**CSA CCM v4** -- Cloud Controls Matrix with 17 domains. Short prefixes identify the domain (e.g., IAM = Identity & Access Management, LOG = Logging and Monitoring).

**COBIT 2019** -- ISACA's IT governance framework with 40 management and governance objectives across five domains: EDM (Evaluate, Direct, Monitor), APO (Align, Plan, Organize), BAI (Build, Acquire, Implement), DSS (Deliver, Service, Support), MEA (Monitor, Evaluate, Assess).

**GDPR** -- References to Articles of Regulation (EU) 2016/679. GDPR is a regulation with legal force, not a control framework, so mappings are to legal obligations rather than prescriptive controls.

## HIPAA Security Rule Safeguard Categories

For reference when reading the HIPAA column in the matrix above:

| CFR Section | Safeguard Type | Scope |
|---|---|---|
| 164.308 | Administrative | Security management, workforce security, information access, training, contingency, evaluation, BAA requirements |
| 164.310 | Physical | Facility access, workstation use/security, device and media controls |
| 164.312 | Technical | Access control, audit controls, integrity, authentication, transmission security |
| 164.314 | Organizational | Business associate contracts, group health plan requirements |
| 164.316 | Policies & Documentation | Policy requirements, documentation retention |
| 164.520-528 | Privacy Rule (Subpart E) | Notice of privacy practices, individual rights, accounting of disclosures |

## PCI DSS v4.0.1 Requirement Groups

For reference when reading the PCI DSS column in the matrix above:

| Req | Title |
|---|---|
| 1 | Install and Maintain Network Security Controls |
| 2 | Apply Secure Configurations to All System Components |
| 3 | Protect Stored Account Data |
| 4 | Protect Cardholder Data with Strong Cryptography During Transmission |
| 5 | Protect All Systems and Networks from Malicious Software |
| 6 | Develop and Maintain Secure Systems and Software |
| 7 | Restrict Access to System Components and Cardholder Data by Business Need to Know |
| 8 | Identify Users and Authenticate Access to System Components |
| 9 | Restrict Physical Access to Cardholder Data |
| 10 | Log and Monitor All Access to System Components and Cardholder Data |
| 11 | Test Security of Systems and Networks Regularly |
| 12 | Support Information Security with Organizational Policies and Programs |

## CIS Controls v8 Quick Reference

For reference when reading the CIS Controls column in the matrix above:

| CIS # | Control Title |
|---|---|
| 1 | Inventory and Control of Enterprise Assets |
| 2 | Inventory and Control of Software Assets |
| 3 | Data Protection |
| 4 | Secure Configuration of Enterprise Assets and Software |
| 5 | Account Management |
| 6 | Access Control Management |
| 7 | Continuous Vulnerability Management |
| 8 | Audit Log Management |
| 9 | Email and Web Browser Protections |
| 10 | Malware Defenses |
| 11 | Data Recovery |
| 12 | Network Infrastructure Management |
| 13 | Network Monitoring and Defense |
| 14 | Security Awareness and Skills Training |
| 15 | Service Provider Management |
| 16 | Application Software Security |
| 17 | Incident Response Management |
| 18 | Penetration Testing |

## CSA CCM v4 Domain Reference

| Prefix | Domain |
|---|---|
| A&A | Audit & Assurance |
| AIS | Application & Interface Security |
| BCR | Business Continuity Management & Operational Resilience |
| CCC | Change Control & Configuration Management |
| CEK | Cryptography, Encryption & Key Management |
| DCS | Datacenter Security |
| DSP | Data Security & Privacy Lifecycle Management |
| GRC | Governance, Risk & Compliance |
| HRS | Human Resources |
| IAM | Identity & Access Management |
| IPY | Interoperability & Portability |
| IVS | Infrastructure & Virtualization Security |
| LOG | Logging & Monitoring |
| SEF | Security Incident Management, E-Discovery & Cloud Forensics |
| STA | Supply Chain Management, Transparency & Accountability |
| TVM | Threat & Vulnerability Management |
| UEM | Universal Endpoint Management |

## Caveats and Limitations

**Many-to-many relationships.** The matrix shows family-to-domain mappings, but at the individual control level, relationships are frequently many-to-many. A single NIST control may map to multiple controls in another framework, and vice versa. For example, NIST AC-2 (Account Management) maps to SOC 2 CC6.1 and CC6.2, ISO 27001 A.5.18, PCI DSS Req 7.1 and 8.6, CIS 5.1 through 5.4, and HIPAA 164.312(a)(1) simultaneously.

**Partial mappings.** Not all frameworks cover the same scope. A cell entry indicates that the target framework addresses the same general concern, not that it provides equivalent depth or specificity. NIST 800-53 is the most granular framework in this matrix, so most target frameworks provide less prescriptive coverage.

**Privacy-specific gaps.** The PT (PII Processing and Transparency) family, added in NIST 800-53 Rev 5, has limited coverage in older or security-focused frameworks. CIS Controls do not address privacy directly. GDPR covers privacy extensively but from a legal obligations perspective rather than as technical controls.

**Framework version sensitivity.** This matrix is current as of NIST 800-53 Rev 5, SOC 2 (2017 criteria), ISO 27001:2022, PCI DSS v4.0.1, HIPAA (as amended through the HITECH Act), CIS Controls v8.1, CMMC 2.0, CSA CCM v4, COBIT 2019, and GDPR (Regulation EU 2016/679). Framework updates will alter these mappings.

**Inherited and shared responsibilities.** In cloud environments, a single NIST control may be partially addressed by the CSP and partially by the customer. The matrix does not distinguish responsibility splits. Consult the CSP's Customer Responsibility Matrix (CRM) for inherited vs. customer-implemented controls.

**Scope differences.** Some frameworks address only a subset of the security domain. PCI DSS focuses on cardholder data environments. HIPAA applies only to protected health information. GDPR addresses personal data of EU residents. CMMC/800-171 targets Controlled Unclassified Information (CUI). When a framework's scope does not cover a particular concern, the mapping may be sparse or absent -- this does not indicate a deficiency in the framework, only a scope boundary.

**Regulatory vs. control frameworks.** GDPR and HIPAA are legal/regulatory instruments, not prescriptive control frameworks. Their "controls" are legal obligations that organizations must interpret and implement using technical controls from frameworks like NIST or ISO. The mappings in this matrix show which NIST families address the same concerns as the regulatory requirements, not that implementing the NIST controls automatically satisfies the legal obligation.

## Detailed Mapping Files

For control-level mappings within each family, consult the following files:

| File | Scope |
|---|---|
| `nist-to-soc2.md` | NIST 800-53 controls mapped to SOC 2 Trust Services Criteria |
| `nist-to-iso27001.md` | NIST 800-53 controls mapped to ISO 27001:2022 Annex A controls |
| `nist-to-pci-dss.md` | NIST 800-53 controls mapped to PCI DSS v4.0.1 requirements |
| `nist-to-hipaa.md` | NIST 800-53 controls mapped to HIPAA Security Rule standards |
| `nist-to-cis.md` | NIST 800-53 controls mapped to CIS Controls v8 safeguards |
| `nist-to-cmmc.md` | NIST 800-53 controls mapped to NIST 800-171 / CMMC 2.0 practices |
| `nist-to-csa-ccm.md` | NIST 800-53 controls mapped to CSA CCM v4 controls |
| `nist-to-cobit.md` | NIST 800-53 controls mapped to COBIT 2019 management objectives |
