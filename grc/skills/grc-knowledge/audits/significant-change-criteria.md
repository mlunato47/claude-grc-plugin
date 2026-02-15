# Significant Change Criteria

Criteria for determining whether a system change qualifies as "significant" under FedRAMP, FISMA, and NIST RMF — and what actions are triggered when it does.

## What Is a Significant Change?

A significant change is any modification to a system, its environment, or its operation that could affect the security posture and therefore requires reassessment of affected controls. Per NIST 800-37 and FedRAMP guidance, significant changes trigger updates to the authorization package and may require a new or supplemental assessment.

## FedRAMP Significant Change Categories

FedRAMP defines the following categories of significant change (per FedRAMP Continuous Monitoring Strategy Guide):

### Category 1 — Changes to the Authorization Boundary

- Adding or removing components within the boundary
- Adding new services or capabilities
- Moving to a new data center or cloud region
- Adding new external system interconnections
- Changes to the cloud service model (IaaS/PaaS/SaaS scope shift)
- Adding new data types (especially higher-impact data)

### Category 2 — Changes to the Security Architecture

- Modifying the network architecture (subnets, segmentation, firewalls)
- Changing the authentication/authorization infrastructure
- Adding or changing encryption implementations
- Modifying logging/monitoring infrastructure
- Changing the vulnerability scanning architecture
- Adding or modifying API gateways or load balancers

### Category 3 — Changes to Security Controls

- Changing how a control is implemented (new tool, new process)
- Changing responsibility designation (CSP→Shared, Shared→Customer)
- Modifying ODP values (e.g., changing session timeout from 15 to 30 minutes)
- Adding or removing control enhancements
- Changing compensating controls
- Removing a control with a risk acceptance

### Category 4 — Changes to the Operating Environment

- Operating system major version upgrades
- Database platform changes
- Middleware or application framework changes
- Changing the CI/CD pipeline security tooling
- Major changes to the operational support model (new MSSP, new SOC)
- Changes to key management infrastructure

### Category 5 — Personnel and Process Changes

- Change of ISSO, ISSM, or System Owner
- Change of 3PAO
- Significant organizational restructuring affecting security roles
- Changes to incident response or contingency planning procedures
- Changes to the change management process itself

## Significant Change Decision Tree

```
1. Does the change affect the authorization boundary?
   → YES → Significant change (Category 1)

2. Does the change modify the network architecture or data flow?
   → YES → Significant change (Category 2)

3. Does the change affect how a security control is implemented?
   → YES → Significant change (Category 3)

4. Does the change involve a major platform/OS/infrastructure upgrade?
   → YES → Significant change (Category 4)

5. Does the change affect key security personnel or processes?
   → YES → Significant change (Category 5)

6. Could the change introduce new attack vectors or vulnerabilities?
   → YES → Likely significant change — assess further

7. Does the change affect only cosmetic/UI elements with no security impact?
   → YES → Not significant — document in change log only

8. Is the change a routine patch/update within existing baselines?
   → YES → Not significant — handle via standard ConMon
```

## Changes That Are NOT Typically Significant

- Routine security patches within the same major version
- Minor configuration adjustments within approved baselines
- Adding users within existing role definitions
- Content updates (documentation, help text)
- Hardware replacement with identical specifications
- Scaling within existing architecture (adding identical nodes)
- Routine certificate renewal (same CA, same key parameters)

## Actions Required for Significant Changes

### Before the Change

| Action | Responsible | Deliverable |
|--------|-------------|-------------|
| Security Impact Analysis (SIA) | ISSO/Security team | SIA document |
| Identify affected controls | ISSO | Affected controls list |
| Update SSP draft with planned changes | ISSO | Updated SSP sections |
| Notify AO of planned significant change | System Owner | Notification (email/ticket) |
| FedRAMP PMO notification (if FedRAMP) | System Owner/ISSO | Significant Change Request (SCR) |

### After the Change

| Action | Responsible | Deliverable |
|--------|-------------|-------------|
| Update SSP with actual implementation | ISSO | Updated SSP |
| Update diagrams (boundary, network, data flow) | Security team | Updated diagrams |
| Assess affected controls | 3PAO or internal assessor | Assessment results |
| Update POA&M if new findings | ISSO | Updated POA&M |
| Update CRM/CIS if responsibility changes | ISSO | Updated CRM |
| Update inventory (hardware/software) | System Admin | Updated inventory |
| Notify AO of completed change and assessment | System Owner | Status report |
| Submit updated artifacts to FedRAMP PMO | ISSO | Package update |

## Control Families Commonly Affected by Change Type

| Change Type | Primary Families Affected | Secondary Families |
|-------------|--------------------------|-------------------|
| New component in boundary | CM, RA, CA, SA | AC, SC, SI, AU |
| Network architecture change | SC, AC, CA | AU, SI, CM |
| Authentication change | IA, AC | AU, SC |
| Encryption change | SC, IA | CM, SA |
| New interconnection | CA, AC, SC | SA, CM |
| Platform/OS upgrade | CM, SI, RA | SC, AC, AU |
| Data center move | PE, CP, SC | AC, CM, CA |
| Personnel change | PS, PL | CA, AT, PM |
| New data type | RA, PL, PT | AC, SC, MP, AU |
| Monitoring tool change | SI, AU | CA, CM |
| Incident response change | IR | CA, AT |
| Backup/recovery change | CP | CM, SC |

## Security Impact Analysis (SIA) Template

An SIA should address:

1. **Change description** — What specifically is changing
2. **Change justification** — Why the change is needed
3. **Scope** — Components, systems, and data affected
4. **Affected controls** — Which controls are impacted and how
5. **Risk assessment** — New risks introduced by the change
6. **Mitigation** — How new risks are mitigated
7. **Rollback plan** — How to revert if the change causes issues
8. **Assessment needs** — What testing/assessment is required post-change
9. **Documentation updates** — Which documents need updating
10. **Timeline** — Implementation and assessment schedule

## FedRAMP Significant Change Request (SCR) Process

1. CSP identifies significant change
2. CSP completes Security Impact Analysis
3. CSP submits SCR to FedRAMP PMO (and agency AOs)
4. FedRAMP PMO reviews and determines assessment scope
5. CSP implements change
6. 3PAO assesses affected controls (may be subset assessment)
7. CSP updates authorization package (SSP, POA&M, etc.)
8. CSP submits updated package
9. AO reviews and re-affirms or updates authorization decision

## Common Mistakes

- **Not recognizing a significant change** — Adding "just one more service" without SIA
- **Implementing before notifying** — Change goes live before AO/PMO is informed
- **Incomplete SIA** — Missing affected controls or risk assessment
- **Not updating the SSP** — Change is implemented but SSP still describes the old state
- **Skipping assessment** — Assuming the change is low-risk without verification
- **Not updating diagrams** — Boundary or network diagrams become stale
- **Treating all changes as significant** — Overwhelming the process with routine patches
