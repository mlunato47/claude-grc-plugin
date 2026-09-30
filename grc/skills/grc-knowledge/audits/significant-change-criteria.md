# Significant Change Criteria

> **CR26 note (updated Sept 30, 2026):** the FedRAMP Significant Change Request (SCR) pre-approval process described below is the legacy Rev5 model (in force until CR26 becomes mandatory Jan 1, 2027; SCN Rev5 grace to June 1, 2027). Under CR26, the **SCN** (Significant Change Notification) ruleset uses notification — not advance approval — with three categories: **routine recurring** changes need no notification; **adaptive** changes are notified within 10 business days after completion; **transformative** changes require initial plans 30 business days before, final plans 10 business days before, notice within 5 business days after completion and 5 business days after verification, with service documentation updated within 30 business days. Providers keep a 12-month notification history in human-readable and JSON form; advance approval applies only under a Corrective Action Plan. Also note "SCR" now additionally names the CR26 Supply Chain Risk KSI theme. See `frameworks/fedramp-20x.md`.

Criteria for determining whether a system change qualifies as "significant" under FedRAMP, FISMA, and NIST RMF — and what actions are triggered when it does.

## What Is a Significant Change?

A significant change is any modification to a system, its environment, or its operation that could affect the security posture and therefore requires reassessment of affected controls. Per NIST 800-37 and FedRAMP guidance, significant changes trigger updates to the authorization package and may require a new or supplemental assessment.

## FedRAMP Significant Change Categories

FedRAMP defines the following categories of significant change (per the legacy Rev5 FedRAMP Continuous Monitoring Strategy Guide; under CR26 each change is instead classified as routine recurring, adaptive, or transformative for SCN purposes):

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
- Change of 3PAO (CR26: FedRAMP Recognized independent assessor)
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
| FedRAMP notification (if FedRAMP) | System Owner/ISSO | Significant Change Request (SCR) — *legacy Rev5; under CR26 the SCN ruleset uses notification (not pre-approval): transformative changes need initial plans 30 business days before and final plans 10 business days before; adaptive changes are notified only after completion. Note "SCR" now also names the CR26 Supply Chain Risk KSI theme. See `frameworks/fedramp-20x.md`* |

### After the Change

| Action | Responsible | Deliverable |
|--------|-------------|-------------|
| Update SSP with actual implementation | ISSO | Updated SSP |
| Update diagrams (boundary, network, data flow) | Security team | Updated diagrams |
| Assess affected controls | 3PAO (CR26: FedRAMP Recognized independent assessor) or internal assessor | Assessment results |
| Update POA&M if new findings | ISSO | Updated POA&M (legacy Rev5; CR26 tracks Accepted Vulnerabilities in the quarterly OCR) |
| Update CRM/CIS if responsibility changes | ISSO | Updated CRM (legacy Rev5 SSP Appendix J; no CR26 CIS/CRM template) |
| Update inventory (hardware/software) | System Admin | Updated inventory |
| Notify AO of completed change and assessment | System Owner | Status report |
| Submit updated artifacts to FedRAMP | ISSO | Package update (legacy Rev5; CR26: adaptive notice within 10 business days after completion; transformative notice within 5 business days after completion and after verification, documentation updated within 30 business days) |

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

## FedRAMP Significant Change Request (SCR) Process — Legacy Rev5

Legacy Rev5 model (in force until CR26 becomes mandatory Jan 1, 2027):

1. CSP identifies significant change
2. CSP completes Security Impact Analysis
3. CSP submits SCR to FedRAMP (and agency AOs)
4. FedRAMP reviews and determines assessment scope
5. CSP implements change
6. 3PAO assesses affected controls (may be subset assessment)
7. CSP updates authorization package (SSP, POA&M, etc.)
8. CSP submits updated package
9. AO reviews and re-affirms or updates authorization decision

## CR26 Significant Change Notification (SCN) Process

Under CR26 (SCN ruleset; Rev5 grace to June 1, 2027) there is no default advance approval — only notification, with timing by category:

| Category | Notification timing | Independent assessor |
|----------|--------------------|----------------------|
| Routine recurring | No notification required | Not required |
| Adaptive | Within 10 business days after completion | Optional |
| Transformative | Initial plans at least 30 business days before; final plans at least 10 business days before; notice within 5 business days after completion and within 5 business days after verification/assessment; service documentation updated within 30 business days | Should engage |

Providers maintain 12 months of historical notifications in both human-readable and JSON formats. Advance approval applies only when the provider is operating under a Corrective Action Plan.

## Common Mistakes

- **Not recognizing a significant change** — Adding "just one more service" without SIA
- **Implementing before notifying** — Change goes live before the AO/FedRAMP is informed (legacy SCR); under CR26, a transformative change implemented without the 30/10-business-day advance plan notices
- **Incomplete SIA** — Missing affected controls or risk assessment
- **Not updating the SSP** — Change is implemented but SSP still describes the old state
- **Skipping assessment** — Assuming the change is low-risk without verification
- **Not updating diagrams** — Boundary or network diagrams become stale
- **Treating all changes as significant** — Overwhelming the process with routine patches
