---
description: "Draft SSP control family descriptions"
---

# /grc:ssp-section

Draft SSP (System Security Plan) control family descriptions.

## Usage

```
/grc:ssp-section [framework] [control-family]
```

## Arguments

- **framework**: The compliance framework. Primarily `nist`, `fedramp`, or `fisma` (SSP is an RMF artifact). Also supports `cmmc` for NIST 800-171 security plans.
- **control-family**: The control family ID or name (e.g., `ac`, `access-control`, `ir`, `incident-response`).

## Examples

```
/grc:ssp-section fedramp ac
/grc:ssp-section nist ir
/grc:ssp-section fedramp ia
/grc:ssp-section cmmc access-control
/grc:ssp-section fedramp sc
```

## Behavior

When invoked:

1. **Identify the framework, baseline, and control family** from arguments. Default to FedRAMP Moderate if no baseline specified.

2. **Read the framework reference file** to get the control list for the specified family and baseline.

3. **For each control in the family** (at the appropriate baseline), draft SSP narrative language following the standard format:

   **SSP Narrative Structure** (per control):
   - **What**: The control objective and what is being implemented
   - **Who**: Responsible roles and teams
   - **How**: Implementation details — mechanisms, tools, processes
   - **When**: Frequency of the activity (if applicable)
   - **Where**: System boundary applicability

4. **Include for each control**:
   - Control ID and title
   - Responsibility designation: Common, System-Specific, or Hybrid
   - Inherited controls notation (if from underlying CSP/infrastructure)
   - FedRAMP parameter values (if FedRAMP)
   - Implementation status: Implemented, Partially Implemented, Planned, Alternative, N/A
   - Control enhancements included at the baseline level

5. **Use professional SSP language**:
   - Third person ("The organization...", "The system...")
   - Present tense for implemented controls
   - Specific and auditable (not vague or aspirational)
   - Reference specific tools/mechanisms generically (e.g., "the organization's SIEM" not a product name)

6. **If no arguments provided**, ask for framework, baseline, and control family.

## Output Format

```
## [Framework] SSP — [Family Name] ([Family ID]) Family

**Baseline**: [Low/Moderate/High]
**Total Controls in Family (at baseline)**: [Count]

---

### [Control-ID]: [Title]

**Responsibility**: [Common / System-Specific / Hybrid]
**Implementation Status**: [Implemented / Partially Implemented / Planned / N/A]

#### Implementation Narrative

[The organization/system implements [control] by...]

**What**: [Control objective]
**Who**: [Responsible roles]
**How**: [Implementation details]
**When**: [Frequency, if applicable]
**Where**: [System boundary scope]

#### FedRAMP Parameters (if applicable)
- [Parameter]: [Value]

#### Control Enhancements
- **[ID](enhancement#)**: [Enhancement narrative]

---
```

## Notes

- SSP language should be specific enough to pass 3PAO testing but generic enough to not require updates for every minor change.
- Flag controls that are commonly written poorly or frequently found deficient.
- Include common inherited controls from IaaS/PaaS providers where applicable.
- For CMMC, adapt the format for NIST 800-171 security requirement descriptions.
