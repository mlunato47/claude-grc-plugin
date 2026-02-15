# Supply Chain Risk Management (SCRM) Deep Dive

Comprehensive reference for the NIST 800-53 Rev 5 SR (Supply Chain Risk Management) family, NIST 800-161 Rev 1, and practical implementation guidance.

## Why SCRM Matters Now

Supply chain attacks (SolarWinds, Log4j, 3CX, xz-utils) have moved SCRM from a theoretical concern to an operational priority. Rev 5 elevated supply chain from a handful of SA-12 enhancements to a dedicated 12-control family (SR-1 through SR-12, with additional enhancements). NIST 800-53B includes most SR controls in all three baselines (Low, Moderate, High).

## SR Family Controls

### SR-1: Policy and Procedures
**Baselines**: Low, Moderate, High

Requires a documented SCRM policy that addresses purpose, scope, roles, management commitment, coordination, and compliance. Plus procedures to facilitate implementation.

**Key ODP**: Review frequency for policy and procedures (FedRAMP: at least annually).

**What auditors look for**:
- A formal SCRM policy document (not just a paragraph in the general security policy)
- Defined roles and responsibilities for supply chain risk decisions
- Integration with acquisition and procurement processes
- Regular review and update cycle

### SR-2: Supply Chain Risk Management Plan
**Baselines**: Low, Moderate, High

Requires a formal SCRM plan that includes:
- Threats and vulnerabilities to the supply chain
- Organizational strategies for managing supply chain risks
- Implementation of controls to mitigate identified risks
- Processes for monitoring and continuous improvement

**What auditors look for**:
- Documented SCRM plan (standalone or integrated into broader risk management)
- Threat assessment specific to the organization's supply chain
- Clear strategy (avoid, mitigate, accept, transfer) for each identified risk
- Integration with the overall risk management framework

### SR-3: Supply Chain Controls and Processes
**Baselines**: Low, Moderate, High

Requires implementation of specific processes and controls to protect against supply chain risks:
- Establishing provenance for critical components
- Employing contract language requiring supplier security practices
- Using trusted delivery channels
- Maintaining traceability of components

**What auditors look for**:
- Evidence of supplier security requirements in contracts
- Component provenance documentation
- Trusted delivery verification processes
- Software Bill of Materials (SBOM) practices

### SR-4: Provenance
**Baselines**: Not in standard baselines

Requires documenting, monitoring, and maintaining valid provenance of systems, components, and associated data:
- Tracking the origin of system components
- Documenting chain of custody for critical components
- Verifying the integrity of delivered components against provenance records

**What auditors look for**:
- Provenance documentation for critical components
- Chain of custody records
- Verification processes for component origin claims
- Integration with SBOM and inventory management

### SR-5: Acquisition Strategies, Tools, and Methods
**Baselines**: Low, Moderate, High

Requires employing acquisition strategies, tools, and methods to limit supply chain risk:
- Diversity of suppliers
- Vendor lock-in avoidance where feasible
- Trusted procurement channels
- Security-focused acquisition criteria

**What auditors look for**:
- Security criteria in vendor selection/evaluation
- Documented acquisition procedures that include security assessment
- Evidence of alternative supplier identification
- RFP/RFQ templates with security requirements

### SR-6: Supplier Assessments and Reviews
**Baselines**: Moderate, High

Requires assessing and reviewing suppliers for risk, including:
- Pre-contract security assessment
- Ongoing supplier monitoring
- Review of supplier security incidents
- Assessment of supplier sub-tier suppliers (where critical)

**What auditors look for**:
- Supplier risk assessment methodology
- Completed supplier assessments
- Ongoing monitoring process and evidence
- Supplier incident notification requirements

### SR-7: Supply Chain Operations Security
**Baselines**: Not in standard baselines

Requires employing operations security (OPSEC) measures to protect supply chain-related information:
- Limiting disclosure of supply chain security practices to authorized personnel
- Protecting information about supply chain security measures from adversaries
- Using OPSEC principles in supply chain communications

### SR-8: Notification Agreements
**Baselines**: Low, Moderate, High

Requires establishing agreements with suppliers for notification of:
- Supply chain compromises
- Security vulnerabilities in delivered products
- Changes in supplier ownership or control
- End-of-life/end-of-support announcements

**What auditors look for**:
- Contract clauses requiring notification
- Defined notification timelines
- Process for receiving and acting on notifications
- Evidence of notifications received and processed

### SR-9: Tamper Resistance and Detection
**Baselines**: High

Requires implementing tamper protection for systems and components:
- Anti-tamper technologies and techniques
- Tamper detection mechanisms (seals, sensors, inspection)
- Response procedures when tampering is detected

**What auditors look for**:
- Tamper-evident packaging or seals for hardware components
- Inspection procedures upon receipt of components
- Tamper detection and response procedures
- Documentation of tamper events and responses

### SR-10: Inspection of Systems or Components
**Baselines**: Low, Moderate, High

Requires inspection of delivered systems and components (spot checks or comprehensive):
- Verifying components match specifications
- Checking for tampering indicators
- Validating software integrity (hashes, signatures)
- Testing for unauthorized functionality

### SR-11: Component Authenticity
**Baselines**: Low, Moderate, High

Requires processes to detect and prevent counterfeit or compromised components:
- Anti-counterfeit policies and procedures
- Source verification for critical components
- Software integrity verification (code signing, hash verification)
- Hardware authenticity validation

**What auditors look for**:
- SBOM or equivalent component inventory
- Code signing verification processes
- Trusted source documentation
- Counterfeit detection procedures

### SR-12: Component Disposal
**Baselines**: Low, Moderate, High

Requires secure disposal of system components to prevent information leakage and unauthorized reuse.

## Building an SCRM Program

### Tier 1: Foundational (Minimum for Compliance)

1. **Write the SCRM policy** (SR-1)
   - Define scope: which suppliers and components are covered
   - Assign SCRM roles (who makes supply chain risk decisions)
   - Set review cadence (annual minimum)

2. **Create the SCRM plan** (SR-2)
   - Inventory critical suppliers and components
   - Identify supply chain threats relevant to your system
   - Define risk tolerance for supply chain risks
   - Document risk treatment decisions

3. **Establish supplier requirements** (SR-3, SR-8)
   - Add security clauses to standard contracts/agreements
   - Require incident notification from suppliers
   - Require vulnerability disclosure from software suppliers
   - Require SBOM delivery for software components

### Tier 2: Operational (Effective Risk Management)

4. **Implement supplier assessments** (SR-6)
   - Create a supplier risk assessment questionnaire
   - Categorize suppliers by criticality (critical, important, routine)
   - Assess critical suppliers before contract and annually thereafter
   - Monitor supplier security posture (news, advisories, breach reports)

5. **Secure acquisition processes** (SR-5)
   - Include security in vendor evaluation criteria
   - Verify component authenticity on delivery (SR-11)
   - Use trusted distribution channels
   - Maintain an approved supplier list

6. **Monitor and respond**
   - Process supplier notifications (SR-8)
   - Track supplier vulnerabilities
   - Include supply chain scenarios in incident response
   - Update SCRM plan based on lessons learned

### Tier 3: Advanced (Mature Program)

7. **Deep supply chain visibility**
   - Map sub-tier suppliers for critical components
   - SBOM analysis with automated vulnerability tracking
   - Integrate supply chain risk into enterprise risk management
   - Conduct supply chain threat hunting

## Software Supply Chain Specifics

### Software Bill of Materials (SBOM)

An SBOM lists all components in a software product — direct dependencies, transitive dependencies, and their versions.

**Why it matters**: You can't manage risk for components you don't know about. Log4j demonstrated that most organizations couldn't quickly determine if they were affected.

**SBOM formats**:
| Format | Maintained By | Notes |
|--------|--------------|-------|
| SPDX | Linux Foundation | ISO standard (ISO/IEC 5962:2021) |
| CycloneDX | OWASP | Security-focused, lightweight |
| SWID | ISO/IEC | Software identification tags |

**SBOM requirements**:
- Generate SBOM for every production release
- Include direct and transitive dependencies
- Include version numbers and package sources
- Monitor SBOM components against CVE databases
- Update SBOM when dependencies change

### Software Composition Analysis (SCA)

Automated tools that scan code and binaries for known vulnerabilities in dependencies:

**Integration points**:
- CI/CD pipeline (scan on every build)
- Container image scanning (scan base images and layers)
- Runtime monitoring (detect vulnerable libraries in production)
- Scheduled rescanning (new CVEs against existing SBOMs)

### Code Signing and Integrity

| Practice | Purpose | Implementation |
|----------|---------|---------------|
| Code signing | Verify code authenticity | Sign all release artifacts |
| Hash verification | Detect tampering | Verify SHA-256/512 hashes on download |
| Dependency pinning | Prevent supply chain substitution | Pin exact versions in lock files |
| Registry mirroring | Control package sources | Mirror public registries internally |
| Reproducible builds | Verify build integrity | Build from source produces identical artifacts |

## Supplier Risk Assessment Framework

### Criticality Categories

| Category | Criteria | Assessment Frequency | Depth |
|----------|----------|---------------------|-------|
| **Critical** | Single point of failure, handles sensitive data, core platform component | Pre-contract + annual | Full assessment |
| **Important** | Significant functionality, difficult to replace, handles some data | Pre-contract + biennial | Standard questionnaire |
| **Routine** | Commodity service, easily replaceable, no data access | Pre-contract only | Basic verification |

### Assessment Criteria

| Area | What to Assess |
|------|---------------|
| Security program | Does the supplier have a formal security program? Certifications? |
| Incident response | How will the supplier notify you of incidents? What is their SLA? |
| Data protection | How does the supplier protect your data? Encryption? Access controls? |
| Business continuity | Will the supplier survive disruption? What are their DR capabilities? |
| Compliance | Does the supplier hold relevant certifications (SOC 2, ISO 27001, FedRAMP)? |
| Sub-suppliers | Does the supplier rely on sub-tier suppliers? Who are they? |
| Financial health | Is the supplier financially stable? Risk of sudden closure? |
| Vulnerability management | How does the supplier handle vulnerabilities in their products? |
| Change management | How are changes to the supplier's product communicated? |
| End of life | What is the product roadmap? EOL/EOS timeline? |

### Supplier Contract Security Clauses

Essential clauses for supplier agreements:

1. **Security requirements**: Minimum security controls the supplier must maintain
2. **Incident notification**: Timeline and process for reporting security incidents
3. **Vulnerability disclosure**: Process for reporting vulnerabilities in delivered products
4. **Audit rights**: Right to audit or request third-party audit reports
5. **Data handling**: How supplier handles, stores, and disposes of your data
6. **Subcontractor flow-down**: Requirements flow to sub-tier suppliers
7. **Change notification**: Advance notice of significant changes to the product/service
8. **Termination and transition**: Data return/destruction on contract termination
9. **Compliance requirements**: Maintain specific certifications or standards
10. **SBOM delivery**: Provide SBOM with each release (for software suppliers)

## SLSA Integration

SLSA (Supply-chain Levels for Software Artifacts) is a complementary maturity model that provides concrete, technical implementation guidance for several SR controls — particularly SR-3 (provenance and traceability), SR-4 (provenance), and SR-11 (component authenticity). Where the SR family defines *what* supply chain controls are required, SLSA defines *how* to implement artifact integrity and provenance at progressive maturity levels through its Build track (L0–L3) and Source track (L1–L4).

Organizations building an SCRM program should consider SLSA levels as measurable implementation targets for their SR control narratives. For example, achieving SLSA Build L2 provides concrete evidence for SR-3 and SR-4 implementations (signed provenance from a hosted build platform).

> Full reference: `frameworks/slsa.md`

## Common SCRM Deficiencies (Audit Findings)

| Finding | Description | Fix |
|---------|-------------|-----|
| No SCRM policy | SR-1 not satisfied | Write formal SCRM policy |
| No SCRM plan | SR-2 not satisfied | Create SCRM plan with threat assessment |
| No supplier inventory | Can't assess what you don't know | Catalog all suppliers and categorize by criticality |
| Contracts lack security clauses | SR-3, SR-8 gap | Update contract templates and renegotiate where possible |
| No supplier assessments | SR-6 gap | Implement assessment program for critical suppliers |
| No SBOM | SR-11 gap for software | Generate SBOM from build process |
| No incident notification clause | SR-8 gap | Add to contracts; verify supplier has process |
| No component verification | SR-11 gap | Implement hash verification, code signing checks |
| SCRM not in risk management | SR-2 gap | Integrate supply chain risks into enterprise risk register |
| No ongoing monitoring | SR-6 gap | Establish supplier monitoring cadence |
