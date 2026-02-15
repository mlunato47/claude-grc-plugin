# NIST 800-53 to HIPAA Security Rule Mapping

## Overview

The **HIPAA Security Rule** (45 CFR Part 164, Subparts A and C) establishes national standards for protecting electronic protected health information (ePHI). NIST published the authoritative crosswalk between NIST 800-53 and the HIPAA Security Rule in **SP 800-66 Revision 2** (_Implementing the Health Insurance Portability and Accountability Act Security Rule: A Cybersecurity Resource Guide_, February 2024). SP 800-66 Rev 2 maps each HIPAA Security Rule standard and implementation specification to the corresponding NIST 800-53 Rev 5 controls, providing covered entities and business associates with a structured approach to satisfying HIPAA requirements using the NIST Risk Management Framework.

**Key references**:
- **45 CFR Part 164** -- HIPAA Security Rule (HHS/OCR)
- **NIST SP 800-66 Rev 2** -- HIPAA-to-NIST crosswalk
- **NIST SP 800-53 Rev 5** -- Security and Privacy Controls
- **NIST Cybersecurity Framework (CSF) 2.0** -- Alternative high-level mapping published by HHS

---

## Key Differences Between HIPAA and NIST 800-53

| Dimension | HIPAA Security Rule | NIST 800-53 Rev 5 |
|-----------|--------------------|--------------------|
| **Nature** | Federal regulation (law) | Voluntary framework (mandatory for federal systems under FISMA) |
| **Approach** | Outcome-based and scalable; specifies *what* must be achieved | Prescriptive; specifies *what* and often *how* with control enhancements |
| **Flexibility** | "Required" vs. "Addressable" implementation specifications allow risk-based tailoring | Baselines (Low/Moderate/High) with tailoring guidance and compensating controls |
| **Scope** | ePHI held by covered entities and business associates | All federal information systems; adoptable by any organization |
| **Granularity** | ~42 implementation specifications across 3 safeguard categories | 1,189 controls and enhancements across 20 families |
| **Enforcement** | HHS Office for Civil Rights (OCR); civil and criminal penalties | Agency-specific; OMB oversight for federal systems |
| **Updates** | Rarely updated (original 2003; NPRM for update published Dec 2023) | Periodically revised (Rev 5 released Sept 2020) |

### The "Addressable" Concept

HIPAA implementation specifications are designated as either **Required (R)** or **Addressable (A)**. "Addressable" does not mean "optional." A covered entity must assess whether the specification is reasonable and appropriate. If it is, implement it. If not, document why and implement an equivalent alternative measure, or document why the specification is not applicable. This risk-based approach has no direct parallel in NIST 800-53, where controls are either selected (in the baseline) or not.

---

## Comprehensive Mapping by HIPAA Security Rule Standard

### Administrative Safeguards -- 45 CFR SS 164.308

#### SS 164.308(a)(1) -- Security Management Process

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (a)(1)(i) | Standard | Implement policies and procedures to prevent, detect, contain, and correct security violations | PM-1, PL-1 |
| (a)(1)(ii)(A) | R | Risk Analysis | RA-1, RA-2, RA-3, RA-9 |
| (a)(1)(ii)(B) | R | Risk Management | PM-9, RA-3, PM-4 |
| (a)(1)(ii)(C) | R | Sanction Policy | PS-8, PL-4 |
| (a)(1)(ii)(D) | R | Information System Activity Review | AU-2, AU-3, AU-6, AU-12 |

#### SS 164.308(a)(2) -- Assigned Security Responsibility

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (a)(2) | R | Identify the security official responsible for developing and implementing security policies | PM-2, PS-2 |

#### SS 164.308(a)(3) -- Workforce Security

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (a)(3)(i) | Standard | Implement policies to ensure workforce members have appropriate access to ePHI | AC-1, AC-2 |
| (a)(3)(ii)(A) | A | Authorization and/or Supervision | AC-2, PS-2, AC-6 |
| (a)(3)(ii)(B) | A | Workforce Clearance Procedure | PS-3, PS-2 |
| (a)(3)(ii)(C) | A | Termination Procedures | PS-4, PS-5 |

#### SS 164.308(a)(4) -- Information Access Management

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (a)(4)(i) | Standard | Implement policies for authorizing access to ePHI | AC-1 |
| (a)(4)(ii)(A) | A | Isolating Healthcare Clearinghouse Functions | AC-4, SC-7 |
| (a)(4)(ii)(B) | R | Access Authorization | AC-2, AC-3, AC-6 |
| (a)(4)(ii)(C) | R | Access Establishment and Modification | AC-2, AC-3, AC-5, AC-6 |

#### SS 164.308(a)(5) -- Security Awareness and Training

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (a)(5)(i) | Standard | Implement a security awareness and training program | AT-1 |
| (a)(5)(ii)(A) | A | Security Reminders | AT-2 |
| (a)(5)(ii)(B) | A | Protection from Malicious Software | AT-2, SI-3 |
| (a)(5)(ii)(C) | A | Log-in Monitoring | AT-2, AC-7 |
| (a)(5)(ii)(D) | A | Password Management | AT-2, AT-3, IA-5 |

#### SS 164.308(a)(6) -- Security Incident Procedures

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (a)(6)(i) | Standard | Implement policies and procedures to address security incidents | IR-1 |
| (a)(6)(ii) | R | Response and Reporting | IR-2, IR-4, IR-5, IR-6, IR-8 |

#### SS 164.308(a)(7) -- Contingency Plan

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (a)(7)(i) | Standard | Establish policies for responding to an emergency or occurrence that damages systems containing ePHI | CP-1 |
| (a)(7)(ii)(A) | R | Data Backup Plan | CP-2, CP-9 |
| (a)(7)(ii)(B) | R | Disaster Recovery Plan | CP-2, CP-7, CP-10 |
| (a)(7)(ii)(C) | R | Emergency Mode Operation Plan | CP-2, CP-6, CP-7 |
| (a)(7)(ii)(D) | A | Testing and Revision Procedures | CP-3, CP-4 |
| (a)(7)(ii)(E) | A | Applications and Data Criticality Analysis | CP-2, RA-3, CP-8 |

#### SS 164.308(a)(8) -- Evaluation

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (a)(8) | R | Perform periodic technical and nontechnical evaluations of security policies and procedures | CA-2, CA-5, CA-7 |

#### SS 164.308(b)(1) -- Business Associate Contracts and Other Arrangements

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (b)(1) | R | Obtain satisfactory assurances from business associates that they will safeguard ePHI | SA-4, SA-9 |
| (b)(4) | R | Written Contract or Other Arrangement | SA-4, SA-9, PS-7 |

---

### Physical Safeguards -- 45 CFR SS 164.310

#### SS 164.310(a)(1) -- Facility Access Controls

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (a)(1) | Standard | Implement policies to limit physical access to electronic information systems | PE-1 |
| (a)(2)(i) | A | Contingency Operations | PE-1, CP-2, CP-7 |
| (a)(2)(ii) | A | Facility Security Plan | PE-2, PE-3, PE-4, PE-5 |
| (a)(2)(iii) | A | Access Control and Validation Procedures | PE-2, PE-3, PE-6, PE-8 |
| (a)(2)(iv) | A | Maintenance Records | MA-2, MA-5 |

#### SS 164.310(b) -- Workstation Use

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (b) | R | Implement policies specifying physical attributes of workstation surroundings and proper use | PE-5, PL-4, AC-11 |

#### SS 164.310(c) -- Workstation Security

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (c) | R | Implement physical safeguards that restrict access to workstations accessing ePHI | PE-5, SC-15, PE-18 |

#### SS 164.310(d)(1) -- Device and Media Controls

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (d)(1) | Standard | Implement policies governing the receipt and removal of hardware and electronic media containing ePHI | MP-1 |
| (d)(2)(i) | R | Disposal | MP-6, MP-7 |
| (d)(2)(ii) | R | Media Re-use | MP-6 |
| (d)(2)(iii) | A | Accountability | MP-4, MP-5 |
| (d)(2)(iv) | A | Data Backup and Storage | CP-9, MP-4, MP-2, MP-3 |

---

### Technical Safeguards -- 45 CFR SS 164.312

#### SS 164.312(a)(1) -- Access Control

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (a)(1) | Standard | Implement technical policies to allow access only to authorized persons or software | AC-1, AC-2 |
| (a)(2)(i) | R | Unique User Identification | AC-2, IA-2, IA-4 |
| (a)(2)(ii) | R | Emergency Access Procedure | AC-2, AC-14, CP-2 |
| (a)(2)(iii) | A | Automatic Logoff | AC-11, AC-12 |
| (a)(2)(iv) | A | Encryption and Decryption | SC-13, SC-28 |

#### SS 164.312(b) -- Audit Controls

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (b) | R | Implement mechanisms to record and examine activity in systems containing ePHI | AU-1, AU-2, AU-3, AU-6, AU-7, AU-8, AU-9, AU-11, AU-12 |

#### SS 164.312(c)(1) -- Integrity

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (c)(1) | Standard | Implement policies to protect ePHI from improper alteration or destruction | SI-1 |
| (c)(2) | A | Mechanism to Authenticate Electronic PHI | SI-7, SI-10 |

#### SS 164.312(d) -- Person or Entity Authentication

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (d) | R | Implement procedures to verify that a person or entity seeking access to ePHI is who they claim to be | IA-1, IA-2, IA-3, IA-4, IA-5 |

#### SS 164.312(e)(1) -- Transmission Security

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (e)(1) | Standard | Implement technical security measures to guard against unauthorized access to ePHI transmitted over a network | SC-8 |
| (e)(2)(i) | A | Integrity Controls | SC-8, SC-13 |
| (e)(2)(ii) | A | Encryption | SC-8, SC-12, SC-13 |

---

## Organizational Requirements -- 45 CFR SS 164.314

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (a)(1) | R | Business Associate Contracts or Other Arrangements | SA-4, SA-9 |
| (a)(2) | R | Requirements for Group Health Plans | SA-9, PM-1 |
| (b)(1) | R | Requirements for Policies, Procedures, and Documentation | PL-1, PL-2 |

---

## Policies, Procedures, and Documentation -- 45 CFR SS 164.316

| HIPAA Specification | Type | Description | NIST 800-53 Controls |
|---------------------|------|-------------|---------------------|
| (a) | R | Implement reasonable and appropriate policies and procedures | PL-1, PM-1 |
| (b)(1) | R | Documentation | PL-2, all "-1" policy controls (AC-1, AT-1, etc.) |
| (b)(2)(i) | R | Time Limit (retain documentation 6 years) | AU-11, all "-1" policy controls |
| (b)(2)(ii) | R | Availability | PL-2 |
| (b)(2)(iii) | R | Updates | All "-1" policy controls, PL-2 |

---

## Breach Notification Rule Mapping -- 45 CFR SS 164.400-414

The HIPAA Breach Notification Rule (Subpart D) is technically separate from the Security Rule but is operationally linked through incident response processes.

| HIPAA Provision | Description | NIST 800-53 Controls |
|----------------|-------------|---------------------|
| SS 164.404 | Notification to individuals following a breach of unsecured PHI | IR-6, IR-8 |
| SS 164.406 | Notification to media for breaches affecting 500+ individuals in a state | IR-6, IR-8 |
| SS 164.408 | Notification to the HHS Secretary | IR-6 |
| SS 164.410 | Business associate notification obligations to covered entity | IR-6, SA-9 |
| SS 164.414 | Administrative requirements and burden of proof | IR-1, IR-5 |

---

## NIST 800-53 Families With No Direct HIPAA Equivalent

The following NIST 800-53 control families have no direct HIPAA Security Rule counterpart, though some may be partially relevant depending on the organization's risk analysis:

| NIST Family | ID | Reason for No Direct Mapping |
|-------------|-----|------------------------------|
| Configuration Management | CM | HIPAA does not prescribe configuration baselines or change control procedures; however, CM practices support multiple HIPAA standards indirectly |
| System and Communications Protection (partial) | SC | SC-7 maps partially to 164.308(a)(4)(ii)(A) (isolating clearinghouse functions); SC-8, SC-12, SC-13, SC-15, SC-28 are also mapped; broader SC controls have no direct HIPAA specification |
| Supply Chain Risk Management | SR | HIPAA addresses business associates (SA-4, SA-9) but does not cover broader supply chain risk management |
| PII Processing and Transparency | PT | HIPAA Privacy Rule (Subpart E) covers PII concepts but the Security Rule does not directly address PT controls |
| Program Management (partial) | PM | Only PM-1, PM-2, PM-4, PM-9 are mapped; broader governance controls (PM-3, PM-5 through PM-8, PM-10 through PM-32) are not addressed |
| System Development Lifecycle | SA (partial) | Only SA-4 and SA-9 map to BAA requirements; HIPAA does not prescribe SDLC controls |

---

## Summary: Required vs. Addressable Specification Counts

| Safeguard Category | Required Specs | Addressable Specs | Total |
|--------------------|---------------|-------------------|-------|
| Administrative (SS 164.308) | 12 | 9 | 21 |
| Physical (SS 164.310) | 4 | 6 | 10 |
| Technical (SS 164.312) | 5 | 4 | 9 |
| Organizational (SS 164.314) | 3 | 0 | 3 |
| Documentation (SS 164.316) | 5 | 0 | 5 |
| **Total** | **29** | **19** | **48** |

When mapping NIST 800-53 controls to HIPAA, organizations should note that a single NIST control often satisfies multiple HIPAA specifications (many-to-many relationship), and that "Addressable" specifications still require documented risk-based decisions even if the specific implementation is not adopted.

---

## Practical Guidance

**For organizations already NIST-compliant seeking HIPAA alignment**:
1. Start with the SP 800-66 Rev 2 crosswalk as the authoritative reference
2. Map your existing SSP control implementations to HIPAA standards
3. Pay special attention to Addressable specifications -- document risk-based decisions for any not implemented
4. Address HIPAA-specific requirements not fully covered by NIST controls (e.g., BAA contracts, 6-year documentation retention, breach notification timelines of 60 days)
5. Ensure the HIPAA Security Officer role (SS 164.308(a)(2)) is explicitly assigned

**For organizations already HIPAA-compliant seeking NIST alignment**:
1. Perform a gap analysis against the NIST 800-53 Moderate baseline
2. Expect significant gaps in CM (Configuration Management), SI (System Integrity beyond ePHI), and SC (System and Communications Protection) families
3. HIPAA's outcome-based standards will need to be supplemented with prescriptive NIST implementation details
4. Consider FedRAMP or FISMA requirements if serving federal healthcare agencies
