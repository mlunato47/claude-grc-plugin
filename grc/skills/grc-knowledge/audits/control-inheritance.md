# Control Inheritance Models

How security controls are inherited, shared, and allocated across cloud service models and provider stacks. Applies to FedRAMP, FISMA, and any NIST-based framework.

## Responsibility Designations

Every control in an SSP gets one of these designations:

| Designation | Meaning | SSP Requirement |
|-------------|---------|-----------------|
| **Fully Implemented** | The system owner implements this control entirely | Full narrative describing implementation |
| **Inherited** | Another authorized system provides this control | Name the provider, their authorization status, and what exactly is inherited |
| **Shared** | Both the system and another provider contribute | Describe both parties' responsibilities explicitly |
| **Not Applicable** | Control does not apply to this system | Document justification for N/A determination |

### The Inheritance Trap

**Common mistake**: Marking a control as "Inherited" and providing no narrative. Even inherited controls require the SSP to:
1. Name the provider system and its authorization (e.g., "AWS GovCloud, FedRAMP High P-ATO")
2. Describe what specifically is inherited (not just "PE controls inherited from CSP")
3. State how the inheritance was verified (e.g., CRM review, SSP review)
4. Note any residual responsibilities not covered by inheritance

## Service Model Inheritance Patterns

### IaaS (Infrastructure as a Service)

The IaaS provider handles physical infrastructure and virtualization. The customer handles everything from the OS up.

**Typically Inherited from IaaS**:
| Family | Controls | What's Inherited |
|--------|----------|-----------------|
| PE | All PE controls | Physical data center security, environmental controls |
| MP | MP-1 through MP-7 | Physical media handling at data center level |
| MA | MA-1 through MA-5 (partial) | Hardware maintenance at data center |

**Typically Shared with IaaS**:
| Family | Controls | Split |
|--------|----------|-------|
| AC | AC-2, AC-3, AC-6, AC-17 | IaaS: hypervisor/network ACLs. Customer: OS/app accounts |
| AU | AU-2 through AU-12 | IaaS: infrastructure logs. Customer: OS/app audit |
| CM | CM-2, CM-6, CM-7, CM-8 | IaaS: hypervisor config. Customer: OS/app config |
| CP | CP-2, CP-6, CP-7, CP-9, CP-10 | IaaS: infrastructure resilience. Customer: app recovery |
| IA | IA-2, IA-5 | IaaS: console auth. Customer: OS/app auth |
| IR | IR-2, IR-4, IR-5, IR-6 | IaaS: infrastructure incidents. Customer: app incidents |
| RA | RA-5 | IaaS: infrastructure scanning. Customer: OS/app scanning |
| SC | SC-7, SC-8, SC-12, SC-28 | IaaS: network perimeter, physical encryption. Customer: app-level crypto |
| SI | SI-2, SI-4, SI-5 | IaaS: hypervisor patching. Customer: OS/app patching |

**Typically Customer-Implemented on IaaS**:
| Family | Controls | Customer Responsibility |
|--------|----------|------------------------|
| AT | All AT controls | Training own personnel |
| PS | All PS controls | Personnel screening and management |
| PL | PL-1, PL-2, PL-4 | Security planning |
| PM | All PM controls | Program management |
| SA | SA-2, SA-3, SA-4, SA-8 | Development and acquisition |
| PT | All PT controls | Privacy for own data handling |

### PaaS (Platform as a Service)

PaaS adds OS, middleware, and runtime to IaaS inheritance. Customer focuses on application code and data.

**Additional controls inherited from PaaS** (beyond IaaS):
| Family | Controls | What's Added |
|--------|----------|-------------|
| CM | CM-2, CM-6, CM-7 (partial) | OS and middleware configuration management |
| SI | SI-2 (partial) | OS and middleware patching |
| SC | SC-2, SC-3, SC-4 | OS-level separation and memory protection |
| AU | AU-2 through AU-12 (more) | OS and platform-level audit logging |
| IA | IA-2 (partial) | Platform-level authentication services |

**Shared responsibilities shift**:
- CM: Customer only manages application-level configuration
- SI: Customer patches application dependencies only
- RA: Customer scans application layer only
- AC: Customer manages application-level access controls only

### SaaS (Software as a Service)

SaaS providers handle everything except user management, data, and organizational policies.

**Most controls inherited or heavily shared**:
| Family | Typical Designation | Customer Responsibility |
|--------|-------------------|------------------------|
| AC | Shared | Configure user accounts, roles, and permissions within the SaaS application |
| AT | Customer | Train own personnel on using the SaaS |
| AU | Shared | Review audit logs provided by SaaS; configure audit settings if available |
| CA | Shared | Include SaaS in own assessment scope; review SaaS authorization |
| CM | Shared | Manage configurable settings within the SaaS |
| CP | Shared | Data backup/export; application-level recovery planning |
| IA | Shared | Manage user credentials; configure MFA if available |
| IR | Shared | Report incidents to SaaS provider; handle user-level incidents |
| MA | Inherited | SaaS provider handles all maintenance |
| MP | Inherited | SaaS provider handles media |
| PE | Inherited | SaaS provider handles physical |
| PL | Customer | Include SaaS in security plan |
| PM | Customer | Program management |
| PS | Customer (mostly) | Screen own personnel; SaaS provider screens theirs |
| PT | Shared | SaaS provider processes data per agreement; customer defines data handling |
| RA | Shared | SaaS provider scans; customer may do application-level testing if allowed |
| SA | Shared | SaaS provider develops; customer reviews security posture |
| SC | Shared | SaaS provides transport/storage encryption; customer manages keys if CMEK available |
| SI | Shared | SaaS provider patches; customer monitors for application-layer issues |
| SR | Shared | Both manage own supply chains |

### Multi-Layer Inheritance (Stacked Providers)

Real-world stacks often have multiple layers:

```
[Customer Application]      ← Customer-Implemented
        ↓
[PaaS Provider]             ← First inheritance layer
        ↓
[IaaS Provider]             ← Second inheritance layer
        ↓
[Data Center Operator]      ← Third inheritance layer (PE, some MA/MP)
```

**Rules for multi-layer inheritance**:
1. Each layer can only inherit from the layer directly below
2. Each provider must have their own authorization (FedRAMP or equivalent)
3. The SSP must trace the full inheritance chain for each control
4. Shared controls at any layer must clearly define the split
5. The top-level customer is ultimately responsible for verifying the entire chain

## Inheritance Verification

### What Auditors Check

| Verification Item | Evidence Expected |
|-------------------|-------------------|
| Provider authorization is current | ATO letter, FedRAMP Marketplace listing |
| CRM/CIS from provider is reviewed | Documented CRM review with date |
| Inherited controls map to provider's actual offerings | Side-by-side SSP comparison |
| Shared controls clearly delineate responsibilities | Both parties' narratives align |
| Provider's authorization level meets customer's needs | Provider's baseline ≥ customer's baseline |
| Changes to provider's authorization are tracked | Process for monitoring provider status |

### Common Inheritance Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| "PE inherited from AWS" with no detail | Doesn't describe what's inherited or verify authorization | Name specific AWS authorization, describe PE controls inherited |
| Inheriting from non-authorized provider | No FedRAMP authorization to inherit from | Verify provider is on FedRAMP Marketplace or implement controls yourself |
| Wrong baseline level | Inheriting High from a Moderate-authorized provider | Provider baseline must be ≥ consumer baseline |
| Missing CRM review | Assuming inheritance without verifying CRM | Obtain and review provider CRM annually |
| "Shared" without split | Says "shared" but only describes one party | Both parties' specific responsibilities must be documented |
| Inheriting logical controls from physical provider | Data center provides PE, not AC/IA/AU | Only inherit what the provider actually implements |
| Not updating when provider changes | Provider updates their SSP/CRM but consumer SSP is stale | Annual CRM review process, track provider significant changes |

## FedRAMP Leveraged Authorization

FedRAMP allows CSPs to leverage another CSP's authorization:

1. **Underlying CSP** has a FedRAMP P-ATO or ATO
2. **Leveraging CSP** builds on top of the underlying CSP
3. **Leveraging CSP's SSP** documents which controls are inherited
4. **3PAO assessment** verifies the inheritance claims
5. **CRM from underlying CSP** must be current and reviewed

### Leveraging Requirements

- The underlying CSP's authorization level must be ≥ the leveraging CSP's target level
- The leveraging CSP must document in their SSP how they verified the inheritance
- Any controls the underlying CSP marks as "Customer Responsibility" in their CRM become the leveraging CSP's responsibility
- The leveraging CSP must monitor the underlying CSP's authorization status (e.g., through FedRAMP Marketplace, ConMon reporting)

## Responsibility Matrix Template Structure

A well-structured CRM/inheritance matrix should include:

| Column | Purpose |
|--------|---------|
| Control ID | NIST 800-53 control identifier |
| Control Title | Human-readable control name |
| Designation | Inherited / Shared / Customer / CSP |
| Provider Role | What the underlying provider does |
| Customer Role | What the customer must do |
| ODP Responsibility | Who defines ODP values |
| Evidence Owner | Who produces evidence for audit |
| Notes | Additional context or caveats |
