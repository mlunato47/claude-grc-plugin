# GRC Plugin Usage Guide

This guide walks through everything the GRC plugin can do, organized by use case. Each section includes the relevant commands, what to expect, and tips for getting the best results.

## How the Plugin Works

Once installed, the plugin gives Claude deep expertise in 15 compliance frameworks, cross-framework mapping, document review, and operational GRC workflows. It works two ways:

1. **Slash commands** (`/grc:command-name`) — Structured workflows with specific inputs and formatted outputs
2. **Conversational GRC knowledge** — Ask any GRC question naturally and Claude responds with specific control IDs, baselines, and framework-native terminology

All 27 slash commands are listed when you type `/grc:` in your session.

---

## DoD ATO Acceleration Engine

The `/grc:ato` command is an intelligent reasoning engine for DoD Authorization to Operate. It doesn't ask you questions — it reads whatever context is available, infers your situation, and outputs a specific plan.

### How It Works

Drop any context into the conversation — architecture description, stack mentions, a config file, a system description — and run:

```
/grc:ato
```

The engine will:
1. Scan your context for platform signals (P1, AWS GovCloud, Azure, DISA, K8s, Windows)
2. Infer your Impact Level (IL2/IL4/IL5/IL6) and DoD branch
3. Determine what controls your platform already covers (inheritance)
4. Calculate the critical path to AO signature
5. Output a day-by-day sprint with specific tools and commands

### Example Usage

**Drop your architecture description and run the engine:**
```
We're deploying a containerized Python app on Platform One Cloud One at IL4.
Army program. No existing ATO. Uses PostgreSQL on RDS and authenticates via Keycloak.

/grc:ato
```

**Focus modes:**
```
/grc:ato --gap      # Just show me what P1 covers vs. what I own
/grc:ato --path     # Just show me what the AO needs before signing
/grc:ato --brief    # What do I put in the AO briefing deck?
/grc:ato --conmon   # What does ConMon look like post-ATO at IL4 for Army?
```

### Supported Platforms

| Platform | Coverage |
|----------|----------|
| Platform One / Cloud One / Big Bang / Iron Bank | Full — process, required conditions, Big Bang component → NIST mapping |
| AWS GovCloud | Full — CRM usage, IL4/IL5 specifics, tool chain (Security Hub, Config, Inspector, GuardDuty) |
| Azure Government | Full — MDfC, Azure Policy, CAC/PIV in Entra ID, IL5 dedicated host |
| DISA MilCloud 2.0 | Full — ACAS, ESS, STIG application, STOREFRONT process |
| Windows Server / Active Directory | Full — PowerSTIG, DISA GPOs, AD tiering, CAC enforcement |
| Kubernetes (non-P1) | Full — K8s STIG, etcd encryption, image signing, Falco, Trivy |
| On-premises DoD enclave | Full — facility inheritance, STIG compliance, ACAS, ESS |

### Supported ILs and Branches

**Impact Levels**: IL2 (non-CUI), IL4 (CUI), IL5 (CUI + NSS), IL6 (SECRET — high-level process only)

**DoD Branches**: Army (ARCYBER), Navy (NAVWAR), Air Force (AFCYBER), Marine Corps (MARFORCYBER), Space Force (SpOC), SOCOM (J62), DISA

### What Makes It Fast

The engine knows:
- What each platform's ATO already covers (you don't write those control narratives)
- Which controls AOs read first (write those first)
- What takes weeks to generate (start on Day 1)
- What can run in parallel (three-track sprint model)
- Branch-specific quirks (Navy PPSM, Army eMASS routing, P1 system intake process)

### Assumptions and Corrections

The engine always starts with an assumptions table:

```
| Dimension | Assumed | Confidence | What would confirm |
| Platform  | P1/IL4  | High       | Iron Bank image refs seen |
| Branch    | Air Force | Medium   | P1 is AF-managed |
```

If an assumption is wrong, say "re-run with [correction]" and the engine will regenerate with the corrected context.

---

## Framework & Control Lookup

### Look Up Any Control

```
/grc:control-lookup <framework> <control-id-or-keyword>
```

**Frameworks supported**: `nist`, `fedramp`, `fisma`, `cmmc`, `soc2`, `iso27001`, `pci`, `hipaa`, `cis`, `cobit`, `csa`, `gdpr`

**Examples**:
```
/grc:control-lookup nist ac-2           # NIST AC-2 Account Management
/grc:control-lookup soc2 CC6.1          # SOC 2 Logical Access
/grc:control-lookup iso27001 A.8.5      # ISO Secure Authentication
/grc:control-lookup cis 5.2             # CIS Safeguard 5.2
/grc:control-lookup nist encryption     # Keyword search — returns all matching controls
```

**What you get**: Control ID, title, description, baseline assignment, expected evidence, and related controls.

### Map Controls Between Frameworks

```
/grc:map-controls <source-framework> <control-id> to <target-framework>
```

All mappings route through NIST 800-53 as the universal hub. This means you can map between any two frameworks, even if no direct mapping exists.

**Examples**:
```
/grc:map-controls nist ac-2 to soc2             # NIST → SOC 2
/grc:map-controls soc2 CC6.1 to iso27001        # SOC 2 → ISO (chains through NIST)
/grc:map-controls pci 8.3 to nist               # PCI MFA → NIST IA
/grc:map-controls hipaa 164.312(a)(1) to nist    # HIPAA → NIST
```

**What you get**: Source control, NIST mapping, target control(s), coverage assessment (full, partial, gap), and nuance notes.

---

## Document Review & Analysis

These commands review GRC documents for structural completeness and quality. They assess whether your document says *enough* — not whether your system is *secure*.

### Review SSP Narratives

```
/grc:review-narrative <framework> <control-id> [baseline]
```

Paste your control narrative after invoking the command. You get:
- **Five W's assessment** — What, Who, How, When, Where coverage
- **Maturity score** (0-5) with detailed rationale
- **ODP completeness** — Are all FedRAMP parameter values filled in?
- **Enhancement coverage** — Are required enhancements at your baseline addressed?
- **Specific recommendations** with suggested replacement phrasing

**Example**:
```
/grc:review-narrative fedramp ac-2 moderate
```
Then paste your AC-2 narrative.

**Tip**: You can use placeholders like `[System Name]`, `[IAM Tool]`, `[Agency Name]` instead of real names — the review focuses on structure, not specific details.

### Review Full SSP Structure

```
/grc:review-ssp <framework> [baseline]
```

Paste your SSP table of contents or section headers. The review checks for:
- Missing required sections
- Missing appendices (A through L for FedRAMP)
- Missing diagram requirements (boundary, network, data flow)

### Review POA&M Entries

```
/grc:review-poam <framework> <entry|structure>
```

**For individual entries**: Paste a POA&M entry and get field completeness, SLA compliance, milestone quality, and specificity feedback.

**For structure**: Paste your column headers and get a gap analysis of missing required fields.

### Review Policies

```
/grc:review-policy <framework> <family>
```

Paste policy text to get feedback on:
- Language quality — flags advisory language ("should", "may") vs mandatory ("shall", "must")
- Structural completeness — purpose, scope, roles, enforcement, review frequency
- Control coverage against the specified family
- Specificity — flags vague frequencies like "periodically"

### Review CRMs

```
/grc:review-crm <framework> [baseline]
```

Paste your Customer Responsibility Matrix entries to get:
- Coverage percentage (controls documented vs baseline total)
- Responsibility distribution (CSP, Customer, Shared, Inherited)
- Vague description flags
- Missing control families

### Score Control Maturity

```
/grc:score-maturity <framework> <control-id-or-family> [baseline]
```

Two modes:
- **With content**: Paste a narrative and get a 0-5 maturity score with "to reach next level" guidance
- **Without content**: Enter question-based assessment mode — answer structured questions about documentation, implementation, automation, and evidence

---

## Operational Workflows

### Significant Change Analysis

```
/grc:significant-change <framework> <description of the change>
```

Describe a planned system change and get:
- **Classification**: Significant or not significant (per FedRAMP criteria)
- Affected control families
- Before/after action checklists
- SSP sections and diagrams that need updating
- 3PAO assessment likelihood

**Examples**:
```
/grc:significant-change fedramp Migrating database from EC2 to RDS
/grc:significant-change fedramp Applying routine security patches to RHEL 8
```

### Control Inheritance Modeling

```
/grc:inheritance <framework> <service-model> [baseline]
```

Get a complete inheritance model showing which controls are Inherited, Shared, or Customer responsibility for your service model (IaaS, PaaS, SaaS).

**Example**:
```
/grc:inheritance fedramp saas moderate
```

### SAR Finding Responses

```
/grc:sar-response <framework> [respond|template]
```

- **respond**: Paste a SAR finding and get a structured response with acknowledgment, root cause, remediation plan, interim mitigation, verification approach, and a draft POA&M entry
- **template**: Get a blank response template

### Compliance Calendar

```
/grc:compliance-calendar <framework(s)> [frequency]
```

Generate a 12-month recurring activity calendar with control IDs for each activity.

**Examples**:
```
/grc:compliance-calendar fedramp                # Single framework
/grc:compliance-calendar fedramp,soc2 frequency # Multi-framework, grouped by frequency
```

### Authorization Boundary Guidance

```
/grc:boundary-guidance <framework> [service-model]
```

Two modes:
- **Generic**: Specify a service model (SaaS, PaaS, IaaS) for pattern-based guidance
- **Specific**: Describe your architecture for tailored boundary recommendations, including what goes inside/outside and common decision points

### Tabletop Exercise Scenarios

```
/grc:tabletop-scenario <ir|cp> <scenario-type> [context]
```

Generate complete tabletop exercise packages with scenario narrative, injects, discussion questions, controls exercised, and a report template.

**Examples**:
```
/grc:tabletop-scenario ir credentials saas    # IR exercise: credential compromise in SaaS
/grc:tabletop-scenario cp outage              # CP exercise: system outage
```

### Multi-Framework Overlap Analysis

```
/grc:multi-framework <framework1,framework2,...> [baseline]
```

Compare two or three frameworks to see:
- Coverage overlap matrix
- Shared compliance activities
- Incremental work to add each framework
- Requirements unique to each framework

**Example**:
```
/grc:multi-framework fedramp,soc2,pci moderate
```

---

## Audit Preparation

### Audit Prep Checklists

```
/grc:audit-prep <audit-type>
```

**Audit types**: `3pao`, `soc2`, `iso`, `pci`, `internal`

Get phases, timelines, evidence requirements, and common pitfalls for each audit type.

### Evidence Checklists

```
/grc:evidence-checklist <framework> <control-ids> [audit-type]
```

Generate a checklist of documents, technical evidence, interview subjects, and common gaps for specific controls. Uses markdown checkboxes for easy tracking.

**Example**:
```
/grc:evidence-checklist fedramp ac-2,ia-2 3pao
```

### Gap Analysis Worksheets

```
/grc:gap-analysis <framework> [baseline] <system-description>
```

Generate a structured assessment worksheet organized by control families or criteria.

**Examples**:
```
/grc:gap-analysis fedramp moderate SaaS platform
/grc:gap-analysis soc2 security+availability cloud service
```

---

## SSP & Documentation Drafting

### Draft SSP Narratives

```
/grc:ssp-section <framework> <control-family>
```

Draft SSP narrative language for an entire control family at the specified baseline. Output follows the standard What/Who/How/When/Where structure with FedRAMP parameter values.

**Example**:
```
/grc:ssp-section fedramp ac    # All AC family controls at Moderate
/grc:ssp-section fedramp ia    # All IA family controls
```

### Draft Deviation Requests

```
/grc:deviation-request <framework> <control-id> <justification-type>
```

Generate deviation/risk acceptance documentation with finding details, justification, compensating controls, and approval chain.

**Example**:
```
/grc:deviation-request fedramp si-2 vendor-dependency
```

### POA&M Assistance

```
/grc:poam-help <create|template|metrics>
```

- **create**: Walk through required fields, severity determination, deadline calculation
- **template**: Full POA&M entry template with all required fields
- **metrics**: Key metrics (total open, overdue, average age, closure rate)

---

## Continuous Monitoring

```
/grc:conmon-guide <topic>
```

**Topics**: `monthly`, `annual`, `poam`, `lifecycle`, `tooling`

Get detailed guidance on continuous monitoring activities, deliverables, and frequencies.

---

## NIST Transition & OSCAL

### Rev 4 to Rev 5 Transition

```
/grc:rev5-transition <lookup|gaps|withdrawn|checklist>
```

- **lookup `<control>`**: See how a Rev 4 control maps to Rev 5 (e.g., SA-12 → SR family)
- **gaps**: List all new Rev 5 controls with baseline assignments
- **withdrawn**: List all withdrawn controls with dispositions
- **checklist**: Phased transition checklist

### OSCAL Guidance

```
/grc:oscal-guide <overview|ssp|readiness>
```

- **overview**: OSCAL models, layers, current version, FedRAMP status
- **ssp**: OSCAL SSP structure with key components
- **readiness**: Readiness checklist and common conversion challenges

---

## Data Sensitivity

GRC artifacts often contain CUI, PII, and system architecture details. The plugin handles this carefully:

- **Document review commands** display a redaction reminder before every response
- **All feedback is structural** — it assesses document quality, not system security
- **No security posture judgment** — "your narrative is missing the frequency component" not "your system is insecure"
- **Placeholders work great** — replace real names/IPs/agencies with `[Agency Name]`, `[System Name]`, `10.x.x.x`

**Reference-only commands** (evidence-checklist, compliance-calendar, tabletop-scenario, oscal-guide, rev5-transition, multi-framework) don't process user content and skip the reminder.

---

## Tips

1. **Be specific with baselines** — For NIST/FedRAMP, always specify the baseline (Low, Moderate, High). The plugin defaults to Moderate if unspecified.

2. **Use NIST as your rosetta stone** — When mapping between non-NIST frameworks, the plugin chains through NIST automatically, but understanding this helps you interpret partial mappings.

3. **Paste real document sections** — The review commands work best with actual document content. Even with placeholders substituted for sensitive details, the structural feedback is highly specific.

4. **Chain commands** — Start with `/grc:gap-analysis` to identify gaps, then use `/grc:ssp-section` to draft narratives for the gaps, then `/grc:review-narrative` to verify quality.

5. **Ask conversationally too** — You don't always need slash commands. Questions like "What evidence does a 3PAO need for IA-2?" or "Compare SOC 2 and ISO 27001 access control coverage" work naturally.

6. **Multi-framework planning** — If you're working toward multiple certifications, start with `/grc:multi-framework` to understand overlap before diving into individual framework work.

---

## Frameworks Covered

| Framework | Version | Type |
|-----------|---------|------|
| NIST 800-53 | Rev 5 | Federal (anchor framework) |
| FedRAMP | Rev 5 | Federal |
| FISMA | Current | Federal |
| CMMC | 2.0 | Federal (DoD) |
| SOC 2 | Current | Commercial |
| ISO 27001 | 2022 | International |
| PCI DSS | v4.0.1 | Industry |
| HIPAA | Current | Industry |
| CIS Controls | v8.1 | Industry |
| COBIT | 2019 | Governance |
| CSA CCM | v4 | Cloud |
| GDPR | Current | Privacy/International |
| SLSA | v1.2 | Supply Chain |
| OSCAL | 1.1.2 | Standards/Automation |
| NIST Rev 4-5 | Transition | Migration |
