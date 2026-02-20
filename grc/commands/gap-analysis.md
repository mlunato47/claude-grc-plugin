---
description: "Perform a structured gap analysis against a compliance framework"
---

# /grc:gap-analysis

Perform a structured gap analysis against a compliance framework.

## Usage

```
/grc:gap-analysis [framework] [scope-description]
```

## Arguments

- **framework**: The target compliance framework. Accepts same aliases as `control-lookup`.
- **scope-description**: Brief description of what's in scope (system, organization, service).

## Examples

```
/grc:gap-analysis fedramp moderate SaaS platform
/grc:gap-analysis soc2 security+availability cloud service
/grc:gap-analysis iso27001 entire organization
/grc:gap-analysis pci e-commerce payment processing
/grc:gap-analysis cmmc level2 CUI handling system
/grc:gap-analysis hipaa patient portal
```

## Behavior

When invoked:

1. **Identify the framework and scope** from arguments.

2. **Read the framework reference file** and the **readiness/gap analysis reference** (`audits/readiness-gap-analysis.md`).

3. **Present a structured gap analysis template** organized by:

   a. **Control families/categories** for the target framework
   b. **Assessment criteria** per control area:
      - Implemented (control fully in place with evidence)
      - Partially Implemented (some aspects in place)
      - Planned (not yet implemented but on roadmap)
      - Not Implemented (no plans currently)
      - Not Applicable (with justification)
   c. **Maturity assessment** (optional):
      - Level 0: Non-existent
      - Level 1: Ad-hoc
      - Level 2: Repeatable
      - Level 3: Defined
      - Level 4: Managed
      - Level 5: Optimizing

4. **For each control family**, provide:
   - Key controls to assess
   - Questions to ask during assessment
   - Evidence to look for
   - Common gaps in that area
   - Remediation complexity estimate (Low/Medium/High)

5. **Generate a gap analysis worksheet** the user can work through interactively:
   - Walk through each control family
   - Ask about current state
   - Record gaps
   - Build prioritized remediation roadmap

6. **If the user provides current-state information**, assess gaps and produce:
   - Gap summary heat map (by family)
   - Prioritized findings
   - Remediation roadmap with effort estimates
   - Quick wins vs long-term items

7. **If no arguments provided**, ask for target framework, baseline/level, and scope.

## Output Format

```
## Gap Analysis: [Framework] [Baseline/Level] — [Scope]

### Scope
[System/organization description]

### Assessment Summary
| Control Area | Total Controls | Implemented | Partial | Planned | Not Impl. | N/A |
|-------------|---------------|-------------|---------|---------|-----------|-----|

### Detailed Assessment

#### [Control Family 1]
**Key Controls**: [IDs]
**Current State**: [Assessment]
**Gaps Identified**:
- [Gap 1]
- [Gap 2]
**Remediation Priority**: [High/Medium/Low]
**Estimated Effort**: [Low/Medium/High]

### Remediation Roadmap
| Priority | Gap | Control(s) | Effort | Dependencies | Target Date |
|----------|-----|-----------|--------|-------------|-------------|

### Quick Wins
- [Quick win 1]
- [Quick win 2]
```
