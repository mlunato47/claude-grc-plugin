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

2. **Read the OSCAL family JSON for the complete control list and parameter definitions** (use the Read tool — do NOT use Bash, Python, or jq to extract data):
   - For `nist`: read `skills/grc-knowledge/oscal/nist-800-53-rev5/{family}.json`
   - For `fedramp`: read `skills/grc-knowledge/oscal/fedramp-moderate-rev5/{family}.json`
   - Extract all controls, enhancements, parameters (ODPs), and statement parts from the OSCAL data
   - Use parameter values from the OSCAL data to populate FedRAMP-specific ODP values in narratives
   - Read `.parts[] | select(.name == "assessment-objective")` to ensure the narrative addresses every testable objective — each leaf objective's `.prose` describes what an assessor will verify, so the narrative must cover it
   - **ID normalization**: `AC-2` → `ac-2`, `AC-2(1)` → `ac-2.1`

3. **Read the framework reference file** from `skills/grc-knowledge/frameworks/` for additional narrative context, audit expectations, and cross-framework guidance.

4. **For each control in the family** (at the appropriate baseline), draft SSP narrative language following the standard format:

   **SSP Narrative Structure** (per control):
   - **What**: The control objective and what is being implemented
   - **Who**: Responsible roles and teams
   - **How**: Implementation details — mechanisms, tools, processes
   - **When**: Frequency of the activity (if applicable)
   - **Where**: System boundary applicability

5. **Include for each control**:
   - Control ID and title
   - Responsibility designation: Common, System-Specific, or Hybrid
   - Inherited controls notation (if from underlying CSP/infrastructure)
   - FedRAMP parameter values (if FedRAMP)
   - Implementation status: Implemented, Partially Implemented, Planned, Alternative, N/A
   - Control enhancements included at the baseline level

6. **Use professional SSP language**:
   - Third person ("The organization...", "The system...")
   - Present tense for implemented controls
   - Specific and auditable (not vague or aspirational)
   - Reference specific tools/mechanisms generically (e.g., "the organization's SIEM" not a product name)

7. **If no arguments provided**, ask for framework, baseline, and control family.

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
