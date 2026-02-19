---
description: "Generate an evidence preparation checklist for audits or assessments"
---

# /grc:evidence-checklist

Generate an evidence preparation checklist for upcoming audits or assessments.

## Usage

```
/grc:evidence-checklist [framework] [controls] [audit-type?]
```

## Arguments

- **framework**: The compliance framework. Accepts: `nist`, `fedramp`, `fisma`, `cmmc`, `soc2`, `iso27001`, `pci`, `hipaa`, `cis`, `cobit`, `ccm`
- **controls**: Comma-separated control IDs (e.g., `ac-2,ia-2,sc-7`) or a control family (e.g., `ac`, `ia`, `au`)
- **audit-type** (optional): Type of audit — `3pao`, `annual`, `soc2`, `iso`, `pci`, `internal`. Adjusts evidence focus.

## Examples

```
/grc:evidence-checklist fedramp ac-2,ia-2
/grc:evidence-checklist fedramp ac
/grc:evidence-checklist soc2 CC6.1,CC6.2,CC6.3
/grc:evidence-checklist fedramp ia 3pao
/grc:evidence-checklist pci 8.3,8.4 pci
/grc:evidence-checklist nist cp annual
```

## Behavior

When invoked:

1. **This is a pure reference command** — it generates checklists from framework knowledge and does NOT require user content. No redaction reminder is needed.

2. **Read the OSCAL family JSON first** for authoritative assessment procedures (use the Read tool — do NOT use Bash, Python, or jq to extract data):
   - For `nist`: read `skills/grc-knowledge/oscal/nist-800-53-rev5/{family}.json`
   - For `fedramp`: read `skills/grc-knowledge/oscal/fedramp-moderate-rev5/{family}.json`
   - Extract assessment methods from `.controls[].parts[] | select(.name == "assessment-method")`:
     - **EXAMINE** method → use `.parts[] | select(.name == "assessment-objects") | .prose` as the primary source for "Documents to prepare" and "Technical evidence"
     - **INTERVIEW** method → use `.parts[].prose` as the primary source for "Interview subjects"
     - **TEST** method → use `.parts[].prose` to identify processes and mechanisms that need demonstrable evidence
   - **ID normalization**: `AC-2` → `ac-2`, `AC-2(1)` → `ac-2.1`

3. **Read additional reference files**:
   - Framework file from `skills/grc-knowledge/frameworks/`
   - Audit file from `skills/grc-knowledge/audits/` (if audit-type specified)
   - Narrative quality criteria from `skills/grc-knowledge/audits/narrative-quality-criteria.md` (for evidence expectations)

4. **For each control**, generate:
   - **Documents to prepare**: Policies, plans, procedures, and SSP narratives the auditor will request
   - **Technical evidence**: Screenshots, configuration exports, log samples, scan results
   - **Interview subjects**: Roles the auditor will want to speak with
   - **Common gaps**: Evidence that is frequently missing or insufficient for this control
   - **Preparation tips**: Practical advice for gathering this evidence

5. **If audit-type is specified**, tailor the checklist:
   - `3pao`: Focus on FedRAMP SAR evidence requirements, emphasize technical testing artifacts
   - `annual`: Focus on changes since last assessment, ConMon evidence
   - `soc2`: Focus on operating effectiveness evidence over the observation period
   - `iso`: Focus on documented procedures and management review records
   - `pci`: Focus on scoping documentation and technical validation
   - `internal`: Focus on self-assessment evidence and improvement tracking

6. **If a family is provided** instead of specific controls, expand to all controls in that family at the applicable baseline (default: Moderate for NIST/FedRAMP).

7. **If no arguments provided**, ask the user which framework and controls to generate a checklist for.

## Output Format

```
## Evidence Preparation Checklist: [Framework] [Controls]

[Audit type context if specified]

---

### [Control-ID]: [Title]

**Documents**
- [ ] [Document name — e.g., Access Control Policy]
- [ ] [Document name — e.g., SSP Section 11, AC-2 narrative]

**Technical Evidence**
- [ ] [Evidence item — e.g., Screenshot of account provisioning workflow]
- [ ] [Evidence item — e.g., Export of IAM role assignments]

**Interview Subjects**
- [ ] [Role — e.g., System Administrator (account management process)]
- [ ] [Role — e.g., ISSO (account review process)]

**Common Gaps**
- [Gap description — e.g., Missing evidence of periodic account reviews]

**Tips**
- [Preparation advice]

---

### [Next Control-ID]: [Title]
...

---

## Preparation Timeline

| Timeframe | Action |
|-----------|--------|
| 4 weeks before | [Actions] |
| 2 weeks before | [Actions] |
| 1 week before | [Actions] |
| Day of | [Actions] |
```

## Notes

- This command generates reference checklists only — it does not require or process user documents.
- Evidence items are based on what auditors typically request per published assessment procedures (NIST 800-53A, FedRAMP test cases).
- The checklist format uses markdown checkboxes for easy copy-paste into task trackers.
- For large families (AC has 25+ controls at Moderate), prioritize the controls most frequently cited in findings.
