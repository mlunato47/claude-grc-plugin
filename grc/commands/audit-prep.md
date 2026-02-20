---
description: "Audit preparation checklists and guidance by audit type"
---

# /grc:audit-prep

Audit preparation checklists and guidance by audit type.

## Usage

```
/grc:audit-prep [audit-type]
```

## Arguments

- **audit-type**: The type of audit to prepare for. Accepts:
  - `3pao` / `fedramp` — FedRAMP 3PAO assessment (initial or annual)
  - `soc2` — SOC 2 Type I or Type II audit
  - `iso` / `iso27001` — ISO 27001 certification (Stage 1/2 or surveillance)
  - `pci` / `pcidss` — PCI DSS QSA assessment
  - `internal` — Internal audit
  - `gap` — Readiness / gap analysis (redirects to `/grc:gap-analysis`)

## Examples

```
/grc:audit-prep 3pao
/grc:audit-prep soc2
/grc:audit-prep iso
/grc:audit-prep pci
/grc:audit-prep internal
```

## Behavior

When invoked:

1. **Identify the audit type** from the argument.

2. **Read the appropriate audit reference file** from `audits/`:
   - `3pao` → `audits/3pao-assessment.md`
   - `soc2` → `audits/soc2-audit.md`
   - `iso` → `audits/iso-certification.md`
   - `pci` → `audits/pci-qsa.md`
   - `internal` → `audits/internal-audit.md`

3. **Present a structured preparation guide** with:
   - Audit overview and timeline
   - Pre-audit checklist (documents, evidence, systems)
   - Phase-by-phase walkthrough
   - Evidence requirements organized by control area
   - Common findings and how to avoid them
   - Day-of logistics (who needs to be available, war room setup)
   - Post-audit activities (remediation, POA&M entry)

4. **If no audit type provided**, show a comparison table of audit types and ask which to prepare for.

## Output Format

```
## Audit Preparation: [Audit Type]

### Overview
- **Assessor**: [Who performs the audit]
- **Duration**: [Typical timeline]
- **Output**: [Deliverables]
- **Frequency**: [How often]

### Pre-Audit Checklist

#### Documents Required
- [ ] [Document 1]
- [ ] [Document 2]

#### Evidence to Prepare
- [ ] [Evidence category 1]
- [ ] [Evidence category 2]

#### Systems/Access
- [ ] [System access needed]

### Phase Walkthrough
1. **[Phase 1]**: [Description, duration, activities]
2. **[Phase 2]**: [Description, duration, activities]

### Common Findings to Address Proactively
| Finding | Control Area | Prevention |
|---------|-------------|------------|

### Day-Of Logistics
- [Logistics item 1]
- [Logistics item 2]

### Post-Audit
- [Post-audit activity 1]
- [Post-audit activity 2]
```
