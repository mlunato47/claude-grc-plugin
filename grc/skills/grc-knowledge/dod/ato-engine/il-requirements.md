# DoD Impact Level Requirements: IL2 / IL4 / IL5 / IL6

Reference for the ATO acceleration engine. Maps each Impact Level to its regulatory foundation, baseline controls, hosting restrictions, encryption requirements, and what changes moving between levels.

---

## IL2 — Unclassified, Non-CUI

**Authority**: DoD Cloud Computing Security Requirements Guide (CC SRG) v1.4, Section 5.2
**NIST baseline**: Moderate (~304 controls, NIST 800-53 Rev 5)
**FedRAMP equivalent**: FedRAMP Moderate P-ATO is sufficient for IL2 (CSP must be FedRAMP-authorized)
**eMASS categorization**: (C-Low, I-Low, A-Low) or (C-Moderate, I-Moderate, A-Moderate)

### What data belongs at IL2
- Non-CUI, publicly releasable DoD information
- Administrative data: travel orders, non-sensitive HR data (non-FOUO)
- Open-source development and collaboration tools
- Public-facing DoD websites and portals
- Training content with no CUI
- General DoD IT productivity tools (no sensitive data)

**Does NOT belong at IL2**: Any CUI, PII, acquisition-sensitive data, personnel records, law enforcement sensitive, export-controlled information

### Hosting requirements
- Any FedRAMP Moderate (or higher) authorized commercial cloud provider
- No physical isolation requirement beyond being in the authorized FedRAMP service boundary
- Multi-tenant OK
- No DoD-specific network access control requirement (internet-accessible OK)

### Encryption requirements
- Data at rest: AES-128 or higher (FIPS 140-2 validated module preferred but not required)
- Data in transit: TLS 1.2 minimum
- Key management: CSP-managed keys acceptable

### Authentication requirements
- MFA required for privileged users
- CAC/PIV not required (but acceptable if available)
- Username/password + MFA acceptable

### ATO process notes
- Fastest path in the DoD: leverage existing FedRAMP Moderate or High package via reciprocity
- Reciprocity language: "This system leverages [CSP Name]'s FedRAMP [Moderate/High] P-ATO package. See CRM for inherited controls."
- Typical timeline: 5-15 days with FedRAMP inheritance in place
- Still requires: FIPS 199 categorization, SSP with residual controls, POA&M

---

## IL4 — Controlled Unclassified Information (CUI)

**Authority**: DoD CC SRG v1.4, Section 5.3; DFARS 252.204-7012; 32 CFR Part 2002
**NIST baseline**: High (~392 controls, NIST 800-53 Rev 5)
**FedRAMP equivalent**: FedRAMP High is minimum; DoD CC SRG IL4 Provisional Authorization also required from DISA
**eMASS categorization**: Typically (C-Moderate, I-High, A-High) or (C-High, I-High, A-High)

### What data belongs at IL4
- Controlled Unclassified Information (CUI) as defined in 32 CFR Part 2002 and CUI Registry
- For Official Use Only (FOUO)
- Personally Identifiable Information (PII) including medical, financial, personnel records
- Acquisition-sensitive information, contract data, budget data
- Law Enforcement Sensitive (LES)
- Export Controlled (EAR/ITAR) — at this level only if unclassified
- Privacy Act-protected records
- Most DoD mission support systems (logistics, HR, finance, acquisition)
- Systems containing any CUI sub-categories (see CUI Registry at archives.gov)

### Hosting requirements
- Must be a DoD CC SRG IL4-authorized cloud provider (DISA Provisional Authorization at IL4 or higher)
- Current IL4-authorized CSPs include: AWS GovCloud, Azure Government, Google Government, Oracle Government Cloud, others (check DISA Cloud Service Catalog)
- Logical separation is sufficient (multi-tenant OK with proper controls)
- US-only region required (no data in foreign AWS/Azure regions)
- Must use the provider's authorized service boundary (not all services in GovCloud are IL4-authorized; check DISA's list)

### Encryption requirements
- Data at rest: AES-256 with FIPS 140-2 validated cryptographic module (non-negotiable)
- Data in transit: TLS 1.2 minimum; TLS 1.3 preferred; FIPS-validated endpoints required
- Cipher suite restriction: No export-grade ciphers; no SSLv3/TLS 1.0/1.1; no RC4
- Key management: Customer-managed keys (CMK) strongly preferred; CSP-managed keys require documented risk acceptance
- AWS: Use AWS FIPS endpoints (*.fips.amazonaws.com / *.fips.govcloud.amazonaws.com)
- Azure: Use Azure Government with FIPS-compliant settings enabled
- Database encryption: Transparent Data Encryption (TDE) or equivalent required

### Authentication requirements
- MFA required for ALL users (not just privileged) — this is a hard requirement at IL4
- CAC/PIV strongly preferred; software-based MFA (authenticator app, FIDO2) acceptable with risk acceptance
- Privileged Access Management (PAM) required for privileged accounts
- No shared accounts; no generic service accounts with human-usable passwords
- Session timeout: 15-minute idle timeout (AC-11), re-authentication required

### Key differences from IL2
- Entire NIST High baseline (~88 additional controls over Moderate)
- FIPS 140-2 validated crypto becomes mandatory (vs. preferred)
- MFA required for all users (not just privileged)
- CSP must have DoD CC SRG IL4 PA (not just FedRAMP Moderate)
- Data residency must be US-only (federal regions)
- Customer-managed keys expected
- CUI handling policy required (marking, storage, transmission, destruction)

### ATO process notes
- Dominant use case: most non-classified DoD programs, ERP systems, HR systems, logistics, acquisition
- Inheritance: Leverage CSP's FedRAMP High package + DISA IL4 PA CRM
- Typical timeline with Platform One: 3-7 days
- Typical timeline with AWS GovCloud (standalone): 7-14 days
- Typical timeline with on-prem: 20-45 days

---

## IL5 — CUI + National Security Systems (NSS)

**Authority**: DoD CC SRG v1.4, Section 5.4; CNSSP 11; DoDI 8510.01
**NIST baseline**: High (~392 controls) + NSS-specific overlays from CNSSI 1253
**FedRAMP equivalent**: FedRAMP High is necessary but not sufficient; DoD CC SRG IL5 PA required
**eMASS categorization**: (C-High, I-High, A-High) with NSS designation flag

### What data belongs at IL5
- CUI that is also designated as National Security System (NSS) data
- Missions systems that are NSS-designated under DoDI 8500.01
- Controlled personnel data with clearance/sensitive duty information
- Mission-critical C2 (command and control) systems — unclassified tier
- Intelligence support systems (unclassified portions)
- Weapons system support systems with mission-critical availability requirements
- Systems where a compromise would directly impact national security
- Systems designated by DoD CIO as NSS

**Note**: NSS designation must come from the program/mission owner in coordination with AO. Not all systems with sensitive data are NSS.

### Hosting requirements
- CSP must have DoD CC SRG IL5 Provisional Authorization from DISA
- Current IL5-authorized CSPs: AWS GovCloud (IL5 PA for specific services), Azure Government (select regions/services), DISA MilCloud 2.0
- **Dedicated tenancy required for compute**: No shared hypervisors with non-DoD workloads — this rules out standard shared instance types
- AWS: Must use Dedicated Hosts or Dedicated Instances; no default multi-tenant EC2
- Logical isolation must be hardware-enforced (not just software-enforced)
- US persons only: Foreign nationals (including FN employees of DoD contractors) cannot access IL5 systems; must be documented and enforced
- Network separation from IL2/IL4 workloads (different VPCs, separate tenancy)

### Encryption requirements
- All IL4 requirements apply, plus:
- Type 1 encryption may be required depending on data sensitivity and NSS designation
- Always use customer-managed keys (no CSP-managed keys); HSM-backed preferred
- AWS CloudHSM or Azure Dedicated HSM required if handling certain NSS data categories
- Key custodian must be cleared US person
- Cryptographic module must be NSA-approved (in addition to FIPS 140-2 validated)

### Authentication requirements
- All IL4 requirements apply, plus:
- CAC/PIV authentication mandatory (not just preferred) — software MFA not acceptable without specific waiver
- No foreign national access to authentication systems
- Privileged accounts: PAM required with session recording
- Network access: Typically requires connection from DoD network (NIPRnet) or IL5-approved VPN
- Zero Trust Architecture components strongly expected at IL5

### Key differences from IL4
- NSS designation required (formal determination by mission owner + AO)
- Dedicated compute tenancy (no shared hypervisors)
- US persons only (access control extends to citizenship)
- CAC/PIV mandatory (no software MFA)
- Customer-managed HSM-backed keys required
- Higher likelihood of pen test requirement before ATO
- ConMon frequency may increase (some programs require bi-weekly scanning)

### ATO process notes
- Typical timeline: 10-25 days (fewer inheritance shortcuts, more verification)
- Platform One supports IL5 (Cloud One on dedicated AWS GovCloud infrastructure)
- DISA MilCloud 2.0 is common choice for IL5 without going to commercial cloud
- NSS designation must be formally documented before ATO package is complete
- Expect AO to ask specifically about US-persons-only enforcement and dedicated tenancy evidence

---

## IL6 — Classified (SECRET and Below)

**Authority**: DoD CC SRG v1.4, Section 5.5; EO 13526; CNSSI 1253; DoDI 5200.01
**NIST baseline**: CNSSI 1253 (not just NIST 800-53) — High baseline + classified information overlays
**FedRAMP equivalent**: N/A — FedRAMP does not cover classified systems
**eMASS categorization**: Classified system registration (separate from unclassified eMASS; SIMS or equivalent)

### What data belongs at IL6
- Classified National Security Information at SECRET and below
- SIPRNET-connected systems
- C2 systems handling classified mission data
- Intelligence systems (SECRET-level and below)
- Classified procurement and acquisition data
- Classified personnel records (clearance information above FOUO)

### Hosting requirements
- **Must reside in a SECRET-capable accredited enclave** — cannot be in commercial cloud at this time
- Approved environments: DISA Joint Regional Security Stack (JRSS), C2S (Commercial Cloud Services by AWS/Microsoft — IC-specific, not standard GovCloud), DISA data centers, accredited facility data centers
- Physical security: ICS 705 or equivalent SCIF-level controls required
- TEMPEST: NSA TEMPEST requirements apply for processing equipment
- No connection to unclassified networks (physical air gap or approved CDS for cross-domain)
- Cross Domain Solutions (CDS): Must use NSA-approved CDS for any data moving between classification levels

### Encryption requirements
- Type 1 encryption mandatory for data at rest and in transit (NSA-approved crypto)
- NSA-approved cryptographic equipment (e.g., Type 1 encryptors from NSA-certified vendors)
- Key management through NSA Key Management Infrastructure (KMI) or equivalent
- No COTS encryption — only NSA-certified Type 1 products
- Classified key material handling: Must follow COMSEC procedures, Two-Person Integrity (TPI) for key material

### Authentication requirements
- Security clearance required for all users (SECRET minimum)
- CAC/PIV with additional clearance verification
- Physical security factors (must be in an accredited area)
- Privileged users: Additional background investigation (TS/SCI or higher for some)
- System administrators: Minimum SECRET clearance; TS common

### ATO process notes
- **This guidance covers the unclassified process only — operational specifics require cleared personnel**
- Typical timeline: 30-120 days depending on facility accreditation status
- Facility accreditation (ICD 705 or SCIF) is often the long pole — must be done first
- DCSA (Defense Counterintelligence and Security Agency) involved for facility
- SAP (Special Access Program) systems — separate category not covered here; requires SAP-specific authorization
- eMASS equivalent for classified: Varies by component — SIMS, classified eMASS instances
- Reciprocity: Much harder at IL6 — requires reviewing the classified package; rarely accepted without review

---

## IL Comparison Summary

| Dimension | IL2 | IL4 | IL5 | IL6 |
|-----------|-----|-----|-----|-----|
| Data type | Non-CUI | CUI | CUI + NSS | SECRET |
| NIST baseline | Moderate | High | High + NSS overlay | CNSSI 1253 High |
| FedRAMP basis | Moderate sufficient | High required | High + IL5 PA | Not applicable |
| Hosting | Any FedRAMP-authorized | IL4 PA CSP | IL5 PA CSP only | Accredited SECRET enclave |
| Tenancy | Multi-tenant OK | Multi-tenant OK | Dedicated compute | Physical isolation |
| Encryption (rest) | AES-128+ | AES-256, FIPS 140-2 | AES-256, HSM-backed | Type 1 (NSA) |
| MFA | Privileged users | All users | All users, CAC required | CAC + clearance |
| US persons only | No | No | Yes | Yes (cleared) |
| Typical new ATO | 5-15 days | 7-45 days (platform dependent) | 10-30 days | 30-120+ days |
| eMASS instance | Standard | Standard | Standard | Classified equivalent |

---

## IL Determination Checklist

Use this to help the mission owner determine the correct IL before starting ATO work (wrong IL = complete rework):

**Is any data SECRET or above?**
→ YES: IL6. Stop here. This document covers high-level process only.
→ NO: Continue.

**Is the system designated as a National Security System (NSS) by the mission owner / DoD CIO?**
→ YES: IL5 minimum.
→ NO: Continue.

**Does the system process, store, or transmit CUI as defined in 32 CFR Part 2002?**
→ YES: IL4 minimum. Check if NSS designation applies for IL5.
→ NO: IL2 is likely sufficient.

**Does the CUI include categories marked sensitive enough to require dedicated compute, CAC-only authentication, or US-persons-only access?**
→ YES: IL5.
→ NO: IL4.

**Cross-check with DISA CUI Registry** (archives.gov/cui) — specific CUI categories (e.g., Controlled Technical Information, Export Controlled) may mandate higher handling.

---

## Common IL Mistakes That Cause ATO Rework

1. **Starting at IL2 when system has CUI** — Data classification review was skipped. All CUI = IL4 minimum.
2. **Choosing IL4 when mission owner designates NSS** — AO will require re-categorization to IL5.
3. **Using FedRAMP Moderate CSP for IL4 data** — CSP must have DISA IL4 PA, not just FedRAMP Moderate.
4. **IL5 on shared-tenancy cloud** — Dedicated instances are mandatory; standard multi-tenant violates IL5 requirements.
5. **Assuming all AWS GovCloud services are IL5-authorized** — Only specific services in the DISA Cloud Service Catalog are IL5 PA'd. Run your architecture against the DISA list before starting.
6. **Treating FOUO as IL2** — FOUO = CUI = IL4 minimum. This is a common confusion.
