---
description: "Review POA&M entries or structure for completeness"
---

# /grc:review-poam

Review POA&M entries or structure for completeness against FedRAMP and NIST requirements.

## Usage

```
/grc:review-poam [framework?] [action?]
```

The user pastes their POA&M entry/entries or structure after invoking the command.

## Arguments

- **framework** (optional): `fedramp`, `nist`, `fisma`, `cmmc`. Defaults to `fedramp`.
- **action** (optional): `entry` or `structure`. Defaults to `entry`.
  - `entry`: Reviews individual POA&M entries for field completeness and quality
  - `structure`: Reviews column headers, status values, and lifecycle model

## Examples

```
/grc:review-poam
/grc:review-poam fedramp entry
/grc:review-poam fedramp structure
/grc:review-poam nist entry
```

## Behavior

When invoked:

1. **Display the Data Sensitivity Notice** at the top of every response (see SKILL.md Data Handling section).

2. **Read the appropriate reference files**:
   - `skills/grc-knowledge/audits/document-section-requirements.md` for POA&M field requirements
   - `skills/grc-knowledge/conmon/poam-management.md` for lifecycle and SLA details
   - Framework file if framework-specific parameters are needed

3. **For `entry` action** — review each POA&M entry against:

   **a. Required Fields Check (16+ fields)**
   For each required field, check:
   - Present or Missing
   - If present, quality assessment (specific vs. vague)

   **b. Description Quality**
   - Is the weakness description specific enough to understand without additional context?
   - Does it identify the root cause or just the symptom?
   - Flag vague descriptions: "improve security", "address finding", "update configuration"

   **c. Milestone Quality**
   - Are milestones granular (multiple steps) or just "remediate finding"?
   - Do milestone dates progress logically between detection and completion?
   - Is each milestone an actionable step?

   **d. SLA Compliance**
   - Calculate days between detection date and scheduled completion
   - Compare to severity-based SLA (Critical: 30, High: 30, Moderate: 90, Low: 180)
   - Flag overdue items or items exceeding SLA without deviation request

   **e. Status Consistency**
   - Does the status match the milestones and dates?
   - Are completed items missing completion dates or evidence?
   - Are open items past their scheduled completion missing a DR?

4. **For `structure` action** — review the POA&M template/spreadsheet structure:
   - Required column check against the 16+ fields
   - Missing columns identified
   - Status value set (does it include all required statuses?)
   - Lifecycle model (Open → In Progress → Completed → Closed or equivalent)
   - ID numbering scheme assessment
   - Recommendations for missing structural elements

5. **CRITICAL**: Never evaluate whether the described vulnerabilities are actually serious or whether the system is insecure. Only assess whether the POA&M entry adequately documents the weakness, plan, and progress. Feedback is structural: "the description doesn't identify the root cause" not "this vulnerability is critical and should be prioritized."

6. **If no POA&M content is provided**, ask the user to paste their POA&M entry or structure.

## Output Format

### For `entry` review:

```
> **Before sharing GRC artifacts**: Consider replacing real system names, IP addresses, personnel names, agency names, and CVE IDs with generic placeholders (e.g., "[Agency Name]", "[System Name]", "CVE-XXXX-XXXXX"). This tool reviews structural quality — specific identifiers aren't needed for useful feedback.

## POA&M Entry Review: [POA&M ID or "Entry"]

### Required Fields

| # | Field | Status | Finding |
|---|-------|--------|---------|
| 1 | POA&M ID | ✅ / ❌ | [Details] |
| 2 | Weakness Name | ✅ / ❌ | [Details] |
| 3 | Description | ✅ / ⚠️ / ❌ | [Quality note] |
| 4 | Point of Contact | ✅ / ❌ | |
| 5 | Security Control | ✅ / ❌ | |
| 6 | Source | ✅ / ❌ | |
| 7 | Detection Date | ✅ / ❌ | |
| 8 | Risk Rating | ✅ / ❌ | |
| 9 | Vendor Dependency | ✅ / ❌ | |
| 10 | Scheduled Completion | ✅ / ❌ | |
| 11 | Milestones | ✅ / ⚠️ / ❌ | [Quality note] |
| 12 | Status | ✅ / ❌ | |
| ... | ... | ... | ... |

**Fields present**: [X] / [Total required]

### Description Quality
[Assessment of specificity, root cause identification, actionability]

### Milestone Quality
[Assessment of granularity, logical progression, actionable steps]

### SLA Compliance
- **Severity**: [Rating]
- **SLA**: [X] days
- **Days elapsed**: [X] days (detection to scheduled completion)
- **Status**: ✅ Within SLA / ⚠️ Approaching SLA / ❌ Exceeds SLA [needs DR]

### Recommendations
1. [Specific recommendation]
2. [Specific recommendation]
```

### For `structure` review:

```
> [Redaction reminder]

## POA&M Structure Review

### Column Assessment

| Required Column | Present | Notes |
|----------------|---------|-------|
| [Column name] | ✅ / ❌ | [Match quality or suggestion] |

**Columns present**: [X] / [Total required]
**Missing critical columns**: [List]

### Status Values
[Assessment of status lifecycle model]

### ID Scheme
[Assessment of numbering convention]

### Recommendations
1. [Add missing columns]
2. [Structure improvements]
```

## Notes

- Multiple POA&M entries can be reviewed in a single invocation — each gets its own assessment section.
- SLA calculations are based on FedRAMP timelines by default. Adjust if the user specifies a different framework.
- For structure reviews, common issues include missing vendor dependency column, no deviation request tracking, and incomplete status lifecycle.
