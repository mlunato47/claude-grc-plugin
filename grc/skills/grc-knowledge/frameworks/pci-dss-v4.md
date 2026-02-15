# PCI DSS v4.0.1 Reference

## Overview

**Full Title**: Payment Card Industry Data Security Standard v4.0.1
**Governing Body**: PCI Security Standards Council (PCI SSC), founded by Visa, Mastercard, American Express, Discover, and JCB
**Current Version**: v4.0.1 (published June 2024; sole active version as of January 1, 2025)
**Predecessor**: v4.0 (March 2022) replaced v3.2.1 (retired March 31, 2024)
**Purpose**: Protect cardholder data (CHD) and sensitive authentication data (SAD) wherever it is stored, processed, or transmitted
**Scope**: All entities that store, process, or transmit CHD/SAD, or that could affect the security of the cardholder data environment (CDE)

| Entity Type | Obligation | Typical Validation |
|-------------|------------|--------------------|
| **Merchants** | Must comply; validation level set by acquirer/payment brand | SAQ or ROC depending on transaction volume |
| **Service Providers** | Must comply; validation required by contracting entities | ROC (Level 1) or SAQ D (Level 2) |
| **Acquirers** | Must comply and enforce merchant compliance | ROC |
| **Issuers** | Must comply for systems handling CHD/SAD | ROC or SAQ per payment brand rules |

| Data Term | Definition |
|-----------|------------|
| **CHD (Cardholder Data)** | PAN, cardholder name, expiration date, service code |
| **SAD (Sensitive Authentication Data)** | Full track data, CAV2/CVC2/CVV2/CID, PINs/PIN blocks -- never stored post-authorization |
| **PAN (Primary Account Number)** | The defining element -- if PAN is present, PCI DSS applies |
| **CDE (Cardholder Data Environment)** | People, processes, and technology that store, process, or transmit CHD/SAD |

---

## The 12 Requirements by Goal

### Goal 1: Build and Maintain a Secure Network and Systems

**Requirement 1 -- Install and Maintain Network Security Controls**

| Sub-Req | Description |
|---------|-------------|
| 1.2.1 | Configuration standards for NSCs defined and implemented |
| 1.2.2 | All changes to network connections and NSC configurations reviewed and approved |
| 1.2.3 | Accurate network diagrams maintained showing all connections to/between CDEs |
| 1.2.4 | Accurate data-flow diagrams maintained showing all account data flows |
| 1.2.5 | All allowed services, protocols, and ports identified, approved, with defined business need |
| 1.2.7 | NSC configurations reviewed at least every six months |
| 1.2.8 | NSC config files secured and synchronized with active running configurations |
| 1.3.x | Network access to/from the CDE restricted (inbound/outbound traffic rules) |
| 1.4.x | Network connections between trusted and untrusted networks controlled |
| 1.5.1 | Security controls on computing devices connecting to both untrusted and trusted networks |

**Requirement 2 -- Apply Secure Configurations to All System Components**

| Sub-Req | Description |
|---------|-------------|
| 2.2.1 | Configuration standards developed, maintained, and applied to all system components |
| 2.2.2 | Vendor default accounts managed (disabled or credentials changed) |
| 2.2.3 | Primary functions requiring different security levels on separate system components |
| 2.2.4 | Only necessary services, protocols, daemons, and functions enabled |
| 2.2.7 | All non-console administrative access encrypted with strong cryptography |
| 2.3.x | Wireless environments configured and managed securely |

### Goal 2: Protect Account Data

**Requirement 3 -- Protect Stored Account Data**

| Sub-Req | Description |
|---------|-------------|
| 3.2.1 | Data retention and disposal policies limit storage amount and retention time |
| 3.3.1 | SAD not retained after authorization (even if encrypted) |
| 3.3.2 | SAD stored before authorization completion encrypted with strong cryptography |
| 3.4.1 | PAN masked when displayed (first 6 and last 4 digits max visible) |
| 3.5.1 | PAN rendered unreadable via one-way hashes, truncation, index tokens, or strong cryptography |
| 3.5.1.1 | Hashes used to render PAN unreadable are keyed cryptographic hashes |
| 3.5.1.2 | Disk/partition-level encryption used only for removable electronic media |
| 3.6.x | Cryptographic keys protecting stored account data managed securely |

**Requirement 4 -- Protect CHD with Strong Cryptography During Transmission**

| Sub-Req | Description |
|---------|-------------|
| 4.2.1 | Strong cryptography and security protocols protect PAN over open/public networks |
| 4.2.1.1 | Inventory of trusted keys and certificates maintained |
| 4.2.1.2 | Certificates confirmed valid and not expired/revoked |
| 4.2.2 | PAN secured with strong cryptography when sent via end-user messaging technologies |

### Goal 3: Maintain a Vulnerability Management Program

**Requirement 5 -- Protect All Systems and Networks from Malicious Software**

| Sub-Req | Description |
|---------|-------------|
| 5.2.1 | Anti-malware deployed on all system components (except per documented evaluation) |
| 5.2.3 | Components not at risk for malware evaluated periodically |
| 5.2.3.1 | Frequency of periodic evaluations defined via targeted risk analysis |
| 5.3.x | Anti-malware mechanisms active, maintained, and monitored |
| 5.3.2.1 | Periodic malware scan frequency defined via TRA |
| 5.4.1 | Mechanisms to detect and protect personnel against phishing attacks |

**Requirement 6 -- Develop and Maintain Secure Systems and Software**

| Sub-Req | Description |
|---------|-------------|
| 6.2.1 | Bespoke/custom software developed securely per industry standards |
| 6.2.2 | Developers trained on secure coding at least every 12 months |
| 6.2.3 | Bespoke/custom software reviewed prior to release for vulnerabilities |
| 6.2.4 | Software engineering techniques prevent/mitigate common attacks |
| 6.3.1 | Security vulnerabilities identified and managed (intelligence sources monitored) |
| 6.3.2 | Inventory of bespoke/custom software and third-party components maintained |
| 6.3.3 | Critical security patches installed within one month of release |
| 6.4.1 | Public-facing web applications protected (WAF or code review) |
| 6.4.2 | Automated technical solution for web application attack detection/prevention |
| 6.4.3 | All payment page scripts managed, authorized, integrity-assured (e-commerce skimming) |
| 6.5.x | Changes managed securely via change control processes |

### Goal 4: Implement Strong Access Control Measures

**Requirement 7 -- Restrict Access by Business Need to Know**

| Sub-Req | Description |
|---------|-------------|
| 7.2.1 | Access control model defined covering all system components |
| 7.2.2 | Access assigned based on job classification and function (RBAC/ABAC) |
| 7.2.3 | Required privileges approved by authorized personnel |
| 7.2.4 | User accounts and access privileges reviewed at least every six months |
| 7.2.5 | Application and system accounts managed based on least privilege |
| 7.2.5.1 | Application/system account access reviewed periodically |
| 7.2.6 | User access to query repositories of stored CHD restricted |

**Requirement 8 -- Identify Users and Authenticate Access**

| Sub-Req | Description |
|---------|-------------|
| 8.2.x | User identification and accounts managed throughout lifecycle |
| 8.2.8 | Sessions inactive > 15 minutes require re-authentication |
| 8.3.4 | Invalid authentication attempts limited (lockout after max 10 attempts) |
| 8.3.6 | Passwords minimum 12 characters (8 if system limit); numeric + alphabetic required |
| 8.3.7 | New password cannot match any of last 4 passwords |
| 8.3.9 | Passwords changed every 90 days if sole auth factor, or dynamic analysis performed |
| 8.4.1 | MFA for all non-console administrative access into the CDE |
| 8.4.2 | MFA for all access into the CDE |
| 8.4.3 | MFA for all remote network access from outside the entity's network |
| 8.5.1 | MFA systems properly configured (not susceptible to replay attacks) |
| 8.6.x | Application/system accounts and authentication factors managed |

> **v4.0.1 clarification**: MFA (8.4.2) does not apply to accounts authenticated exclusively with phishing-resistant factors.

**Requirement 9 -- Restrict Physical Access to Cardholder Data**

| Sub-Req | Description |
|---------|-------------|
| 9.2.x | Physical access controls manage entry into facilities containing CHD |
| 9.3.x | Physical access for personnel and visitors authorized and managed |
| 9.4.x | Media with CHD securely stored, accessed, distributed, and destroyed |
| 9.5.x | POI devices protected from tampering and unauthorized substitution |
| 9.5.1.2.1 | POI device inspection frequency defined via TRA |

### Goal 5: Regularly Monitor and Test Networks

**Requirement 10 -- Log and Monitor All Access**

| Sub-Req | Description |
|---------|-------------|
| 10.2.1 | Audit logs enabled and active for all in-scope system components |
| 10.2.1.x | Logs capture: user access, admin actions, log access, invalid attempts, ID changes, object creation/deletion |
| 10.2.2 | Logs record: user ID, event type, date/time, success/failure, origination, affected component |
| 10.3.x | Audit logs protected from destruction and unauthorized modification |
| 10.4.1 | Audit logs reviewed at least daily |
| 10.4.1.1 | Automated mechanisms perform audit log reviews |
| 10.4.2.1 | Periodic log review frequency for other components defined via TRA |
| 10.5.1 | Log history retained 12 months; last 3 months immediately available |
| 10.6.x | Time-synchronization technology configured and active |
| 10.7.x | Failures of critical security control systems detected, reported, and responded to promptly |

**Requirement 11 -- Test Security of Systems and Networks Regularly**

| Sub-Req | Description |
|---------|-------------|
| 11.2.x | Wireless access points identified/monitored; unauthorized APs addressed |
| 11.3.1 | Internal vulnerability scans at least quarterly |
| 11.3.1.1 | Non-critical/non-high vulnerabilities managed per TRA |
| 11.3.1.3 | Internal scans after significant changes; rescans until resolved |
| 11.3.2 | External vulnerability scans quarterly by ASV |
| 11.4.1 | Penetration testing at least every 12 months and after significant changes |
| 11.5.x | Network intrusions and unexpected file changes detected and responded to |
| 11.5.1.1 | IDS/IPS detects covert malware communication channels |
| 11.6.1 | Change/tamper-detection on payment pages to alert unauthorized modification |

### Goal 6: Maintain an Information Security Policy

**Requirement 12 -- Support Information Security with Organizational Policies and Programs**

| Sub-Req | Description |
|---------|-------------|
| 12.1.x | Information security policy established, published, maintained, and disseminated |
| 12.2.1 | Acceptable use policies for end-user technologies defined |
| 12.3.1 | TRA for each requirement providing frequency flexibility |
| 12.3.2 | TRA for each requirement met with the customized approach |
| 12.3.3 | Cryptographic cipher suites and protocols documented and reviewed annually |
| 12.3.4 | Hardware/software technologies reviewed annually (end-of-life management) |
| 12.4.x | Service providers: compliance managed, quarterly exec confirmation |
| 12.5.2 | PCI DSS scope documented and confirmed annually and upon significant change |
| 12.5.2.1 | Service providers: scope confirmed every six months |
| 12.5.3 | Significant organizational changes trigger scope impact analysis |
| 12.6.2 | Awareness program updated annually (phishing, social engineering) |
| 12.8.x | Risk from TPSPs managed |
| 12.10.x | Incident response plan and procedures maintained |
| 12.10.4.1 | IR training frequency defined via TRA |
| 12.10.7 | IR procedures for detected payment page script modifications |

---

## v3.2.1 to v4.0 Key Changes

| Change Area | Description |
|-------------|-------------|
| **Customized Approach** | New validation option: meet requirement objectives via alternative controls, justified by TRA (12.3.2) |
| **Targeted Risk Analysis** | Two types: (1) entity-defined frequency for periodic controls; (2) customized approach justification |
| **Expanded MFA** | MFA required for all CDE access (8.4.2), not just remote/admin |
| **E-Commerce Skimming** | Payment page script management (6.4.3) and tamper-detection (11.6.1) |
| **Authentication Updates** | 12-character minimum passwords (8.3.6); dynamic analysis option vs. 90-day rotation (8.3.9) |
| **Roles & Responsibilities** | Every requirement section now mandates documented roles/responsibilities (X.1.2) |
| **Automated Log Review** | Automated mechanisms for audit log review (10.4.1.1) |
| **Phishing Protection** | Detection/protection mechanisms required (5.4.1) |
| **Disk Encryption** | No longer acceptable for PAN except on removable media (3.5.1.2) |
| **Cryptographic Inventory** | Keys, certificates, cipher suites, protocols inventoried and reviewed (4.2.1.1, 12.3.3) |
| **Scope Validation** | Annual scope confirmation (12.5.2); semi-annual for service providers (12.5.2.1) |

**v4.0 to v4.0.1 Clarifications** (limited revision, no new/deleted requirements):
- **6.3.3**: 30-day patching applies only to critical vulnerabilities (reverted to v3.2.1 language)
- **6.4.3 / 11.6.1**: Clarified applicability for payment page scripts and tamper-detection
- **8.4.2**: MFA exemption for phishing-resistant-only authentication
- **Appendix G**: Added definitions for Legal Exception, Phishing-Resistant Authentication, Visitor

---

## Future-Dated Requirements (Effective After March 31, 2025)

Of the 64 new requirements in v4.0, 51 were best practice until March 31, 2025, after which they are mandatory. Key examples:

| Requirement | Topic |
|-------------|-------|
| 3.5.1.2 | Disk-level encryption restricted to removable media |
| 4.2.1.1, 4.2.1.2 | Certificate/key inventory; validity confirmation |
| 5.2.3.1, 5.3.2.1 | Malware evaluation and scan frequency via TRA |
| 5.4.1 | Phishing detection and protection |
| 6.3.2 | Software/component inventory |
| 6.4.2, 6.4.3 | Automated web app protection; payment page script controls |
| 7.2.4, 7.2.5.1 | Access reviews every six months; system account review |
| 8.3.6, 8.4.2, 8.6.1 | 12-char passwords; MFA for all CDE access; system account login management |
| 10.4.1.1, 10.4.2.1, 10.7.2 | Automated log review; periodic review frequency via TRA; control failure alerting |
| 11.3.1.1, 11.5.1.1, 11.6.1 | Vulnerability management per TRA; covert channel detection; payment page tamper-detection |
| 12.3.3, 12.3.4 | Crypto review; hardware/software EOL review |
| 12.6.2, 12.10.4.1, 12.10.7 | Awareness updates; IR training frequency; payment page IR procedures |

---

## Scoping and Segmentation

**In scope**: All systems that store, process, or transmit CHD/SAD, plus systems providing security services to the CDE (auth servers, firewalls, logging), segmentation boundary devices, systems in the same network segment as CDE, and TPSPs with CHD access.

**Segmentation** is not required but strongly recommended to reduce scope. Inadequate segmentation places the entire network in scope. Segmentation controls must be tested annually via penetration testing (11.4.1); semi-annually for service providers (11.4.6).

| Category | Scope Status |
|----------|--------------|
| **CDE systems** | Always in scope |
| **Connected-to / security-impacting** | In scope |
| **Out-of-scope** | Must be validated via scoping exercise; no connectivity to or impact on CDE |

---

## Assessment, Reporting, and Roles

| Path | Assessor | Output | Used By |
|------|----------|--------|---------|
| **ROC** | QSA or ISA | ROC + AOC | Level 1 merchants/service providers; acquirer-mandated |
| **SAQ** | Self-assessment (may involve QSA/ISA) | SAQ + AOC | Level 2-4 merchants; Level 2 service providers |

| Document | Purpose |
|----------|---------|
| **ROC** | Detailed assessment report with findings for each requirement |
| **AOC** | Executive summary confirming compliance status; accompanies ROC or SAQ |
| **SAQ** | Self-validation with yes/no/N-A per applicable requirement |

| Role | Description |
|------|-------------|
| **QSA** | Independent assessor certified by PCI SSC; employed by QSAC; issues ROCs |
| **ISA** | Internal employee certified by PCI SSC; performs internal assessments, contributes to ROCs |
| **ASV** | Approved by PCI SSC for quarterly external vulnerability scans (11.3.2) |

---

## SAQ Types

| SAQ | Eligible Environment | ~Questions |
|-----|----------------------|------------|
| **A** | Card-not-present; all CHD functions outsourced to validated third parties; no electronic CHD on merchant systems | 26 |
| **A-EP** | E-commerce; merchant site affects payment security (redirect/iFrame) but does not receive CHD | 191 |
| **B** | Imprint machines and/or standalone dial-out terminals only; no electronic CHD storage | 41 |
| **B-IP** | Standalone PTS-approved IP-connected terminals only; no electronic CHD storage | 82 |
| **C** | Payment application systems connected to Internet; no electronic CHD storage | 160 |
| **C-VT** | Single transactions manually entered into Internet-based virtual terminal from validated TPSP; no electronic CHD storage | 79 |
| **D (Merchant)** | Merchants not qualifying for other SAQ types | 329 |
| **D (Service Provider)** | Service providers eligible for SAQ validation | 347 |
| **P2PE** | Hardware terminals in validated PCI-listed P2PE solution only; no electronic CHD storage | 33 |

> v4.0.1 clarified SAQ A eligibility for Requirements 6.4.3 and 11.6.1 in redirect/iFrame implementations.

---

## Compensating Controls vs. Customized Approach

| Dimension | Compensating Controls | Customized Approach |
|-----------|-----------------------|---------------------|
| **When Used** | Documented constraint prevents meeting defined requirement | Entity chooses alternative means (no constraint required) |
| **Validation** | Appendix B/C of ROC/SAQ; QSA assessment | TRA (12.3.2); controls matrix; QSA independent testing |
| **Standard** | Must meet intent/rigor of original requirement | Must meet Customized Approach Objective |
| **Maturity** | Available since v1.0 | New in v4.0; intended for risk-mature organizations |
| **Combined Use** | Mutually exclusive with customized approach per component per requirement | Same |

---

## Merchant Levels (Visa/Mastercard Typical)

| Level | Annual Transactions | Validation |
|-------|---------------------|------------|
| **1** | > 6 million | Annual ROC by QSA/ISA; quarterly ASV scans |
| **2** | 1-6 million | Annual SAQ; quarterly ASV scans |
| **3** | 20K-1M e-commerce | Annual SAQ; quarterly ASV scans |
| **4** | < 20K e-commerce or up to 1M other | Annual SAQ; quarterly ASV scans (if applicable) |

> Thresholds vary by payment brand. Acquirers may escalate merchants at their discretion.

---

## Key Terminology

| Term | Definition |
|------|------------|
| **NSC** | Network Security Controls -- replaces "firewall" from v3.2.1 for modern architectures |
| **TRA** | Targeted Risk Analysis -- entity-specific analysis for control frequency or customized approach justification |
| **POI** | Point of Interaction -- initial point of account data capture (card reader, terminal) |
| **TPSP** | Third-Party Service Provider -- entity handling account data or impacting CDE security |
| **P2PE** | Point-to-Point Encryption -- PCI SSC-validated solution encrypting data from POI to decryption environment |
| **DESV** | Designated Entities Supplemental Validation -- additional validation for payment-brand-designated entities |
