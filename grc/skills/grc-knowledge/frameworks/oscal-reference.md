# OSCAL Reference

OSCAL (Open Security Controls Assessment Language) is a set of standardized, machine-readable formats for security documentation. Developed by NIST, OSCAL is becoming mandatory for FedRAMP submissions.

## What Is OSCAL?

OSCAL provides standardized data formats (JSON, XML, YAML) for GRC artifacts that are traditionally authored in Word documents and spreadsheets. The goal is to enable automation, consistency, and interoperability across the authorization ecosystem.

**Key value**: Instead of hundreds of pages of Word documents reviewed manually, OSCAL enables machine validation, automated comparison, and programmatic analysis of security documentation.

## OSCAL Models (Layer Architecture)

OSCAL is organized into three layers, each with specific models:

### Layer 1 — Controls Layer

| Model | Purpose | Replaces |
|-------|---------|----------|
| **Catalog** | Defines a set of controls (e.g., NIST 800-53 Rev 5 catalog) | NIST SP 800-53 publication |
| **Profile** | Selects and tailors controls from catalogs (e.g., FedRAMP Moderate baseline) | FedRAMP baseline spreadsheets |

### Layer 2 — Implementation Layer

| Model | Purpose | Replaces |
|-------|---------|----------|
| **Component Definition** | Describes security capabilities of a component (software, hardware, service) | Vendor security documentation |
| **System Security Plan (SSP)** | Documents how controls are implemented in a system | Word/PDF SSP documents |

### Layer 3 — Assessment Layer

| Model | Purpose | Replaces |
|-------|---------|----------|
| **Assessment Plan (SAP)** | Defines assessment methodology and scope | Word SAP documents |
| **Assessment Results (SAR)** | Documents assessment findings | Word SAR documents |
| **Plan of Action and Milestones (POA&M)** | Tracks findings and remediation | POA&M spreadsheets |

## OSCAL SSP Structure

The OSCAL SSP model is the most critical for CSPs. Key components:

### Metadata
```
metadata:
  title: System Security Plan
  last-modified: [timestamp]
  version: [version]
  oscal-version: 1.1.2
  roles: [role definitions]
  parties: [organization/person definitions]
  responsible-parties: [role-to-party mappings]
```

### Import Profile
References the control baseline (profile) the SSP is built against:
```
import-profile:
  href: [URI to FedRAMP profile, e.g., Moderate baseline]
```

### System Characteristics
Replaces SSP Sections 1-9:
```
system-characteristics:
  system-id: [FedRAMP ID]
  system-name: [System name]
  description: [System description]
  security-sensitivity-level: moderate
  system-information:
    information-types: [NIST 800-60 types]
  security-impact-level:
    security-objective-confidentiality: moderate
    security-objective-integrity: moderate
    security-objective-availability: moderate
  status:
    state: operational
  authorization-boundary:
    description: [Boundary description]
    diagrams: [diagram references]
  network-architecture:
    description: [Network description]
    diagrams: [diagram references]
  data-flow:
    description: [Data flow description]
    diagrams: [diagram references]
```

### System Implementation
Components, users, inventory:
```
system-implementation:
  users: [user types and roles]
  components: [system components]
  inventory-items: [hardware/software inventory]
  leveraged-authorizations: [inherited systems]
```

### Control Implementation
The core — replaces SSP Section 11 (narratives):
```
control-implementation:
  description: [Overall approach]
  implemented-requirements:
    - control-id: ac-2
      statements:
        - statement-id: ac-2_smt.a
          by-components:
            - component-uuid: [component reference]
              description: [Implementation narrative for this part]
              implementation-status:
                state: implemented
              responsible-roles:
                - role-id: isso
```

### Back Matter
References, attachments, resources:
```
back-matter:
  resources:
    - uuid: [unique ID]
      title: [Resource title]
      description: [Resource description]
      rlinks:
        - href: [URI to document]
```

## OSCAL SSP Key Concepts

### Components
Instead of writing one monolithic narrative per control, OSCAL breaks implementation into **components** — each component describes its contribution to the control.

Example for AC-2:
- Component "AWS IAM" → describes IAM's role in account management
- Component "Okta" → describes Okta's role in authentication
- Component "Custom App" → describes application-level account logic

This enables **component reuse** — a CSP can define an "AWS IAM" component once and reference it across multiple controls.

### Responsibility and Implementation Status

Each implemented requirement has:

| Field | Values |
|-------|--------|
| `implementation-status` | `implemented`, `partial`, `planned`, `alternative`, `not-applicable` |
| `responsible-roles` | References to defined roles |
| Provider vs. customer | `by-components` links to specific components with `provided` or `inherited` markers |

### Leveraged Authorizations
OSCAL explicitly models inheritance:
```
leveraged-authorizations:
  - uuid: [unique ID]
    title: "AWS GovCloud"
    party-uuid: [AWS party reference]
    date-authorized: 2024-01-15
    links:
      - href: [FedRAMP Marketplace URL]
```

### Parameters (ODPs)
OSCAL handles organization-defined parameters as first-class objects:
```
set-parameters:
  - param-id: ac-2_prm_1
    values: ["ISSO, System Owner"]
  - param-id: ac-2_prm_4
    values: ["upon account creation or modification"]
```

## FedRAMP OSCAL Requirements

### Current Status
- FedRAMP has published OSCAL versions of their baselines (Low, Moderate, High, LI-SaaS)
- OSCAL SSP submissions are accepted and encouraged
- FedRAMP is moving toward requiring OSCAL for new authorizations
- FedRAMP provides OSCAL-based templates and validation tools

### FedRAMP OSCAL Resources
- FedRAMP Automation GitHub repository: OSCAL templates and examples
- FedRAMP OSCAL Registry: FedRAMP-specific extensions and constraints
- GovReady, Trestle, and other tools support FedRAMP OSCAL generation

### FedRAMP Extensions
FedRAMP adds extensions (properties) to standard OSCAL:
- `fedramp:authorization-type` — JAB or Agency
- `fedramp:authorization-date`
- `fedramp:system-service-model` — IaaS, PaaS, SaaS
- `fedramp:deployment-model` — Public, Private, Hybrid, Community
- `fedramp:leveraged-authorization-type`

## OSCAL Validation

### Structural Validation
- Schema validation (JSON Schema or XML Schema)
- OSCAL model version compatibility
- Required field presence
- Reference integrity (all UUIDs resolve)

### Content Validation
- All baseline controls are addressed
- All required parameters have values
- Component references are valid
- Responsible roles are defined
- Implementation status is set for every control
- Diagrams are referenced and linked

### FedRAMP-Specific Validation
- FedRAMP extensions are present
- Leveraged authorizations reference valid FedRAMP packages
- Baseline profile matches the target authorization level
- FedRAMP-required parameter values match expectations

## OSCAL Conversion Readiness

### What Your SSP Needs for OSCAL Conversion

| SSP Element | OSCAL Requirement | Readiness Check |
|-------------|-------------------|-----------------|
| System components | Each component must be uniquely identifiable | Do you have a component inventory? |
| Control narratives | Must be decomposable by component and statement part | Are narratives structured by control part (a, b, c)? |
| Roles | Must be formally defined | Are roles consistently named throughout the SSP? |
| Parameters | Must be explicit, not embedded in prose | Are ODP values called out separately? |
| Inheritance | Must reference specific leveraged authorizations | Are inherited systems formally identified? |
| Diagrams | Must be linkable resources | Are diagrams stored as separate files with stable URIs? |
| Inventory | Must be itemized | Is inventory in a structured format? |
| Interconnections | Must be individually documented | Are interconnections in a table/list format? |

### Common Conversion Challenges

| Challenge | Impact | Mitigation |
|-----------|--------|-----------|
| Monolithic narratives | Hard to decompose by component | Restructure narratives by component before converting |
| Embedded parameters | Can't extract ODP values | Separate parameter values into their own section |
| Inconsistent role names | Role references break | Standardize role names across the SSP |
| Missing UUIDs | Components can't be cross-referenced | Assign UUIDs during conversion |
| Prose-heavy sections | Difficult to structure | Extract structured data, keep prose as descriptions |
| Diagrams in Word | Can't link as resources | Export diagrams as standalone image files |

## OSCAL Tools Ecosystem

| Tool | Type | Purpose |
|------|------|---------|
| NIST OSCAL CLI | Validation | Validate OSCAL documents against schemas |
| Trestle / compliance-trestle (IBM) | Authoring/Automation | Author, manage, and CI/CD integrate OSCAL documents |
| GovReady-Q | Assessment | GRC platform with OSCAL export |
| OSCAL Deep Diff | Comparison | Compare two OSCAL documents |
| FedRAMP Automation | Validation | FedRAMP-specific OSCAL validation rules |
| Lula | Assessment | Automated evidence collection to OSCAL |

## OSCAL Versions

| Version | Status | Key Changes |
|---------|--------|-------------|
| 1.0.0 | Released June 2021 | First stable release |
| 1.0.4 | Released 2023 | Bug fixes, clarifications |
| 1.1.0 | Released July 2023 | New features, enhanced assessment layer |
| 1.1.3 | Released November 2024 | Bug fixes, stability improvements |
| 1.2.0 | Released December 2025 | Latest stable |

Always use the latest stable OSCAL version unless a specific version is required by the consuming organization (e.g., FedRAMP may specify a version).
