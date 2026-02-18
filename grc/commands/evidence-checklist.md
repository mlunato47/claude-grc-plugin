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

2. **Read the appropriate reference files**:
   - Framework file from `skills/grc-knowledge/frameworks/`
   - Audit file from `skills/grc-knowledge/audits/` (if audit-type specified)
   - Narrative quality criteria from `skills/grc-knowledge/audits/narrative-quality-criteria.md` (for evidence expectations)

3. **For each control**, generate:
   - **Documents to prepare**: Policies, plans, procedures, and SSP narratives the auditor will request
   - **Technical evidence**: Screenshots, configuration exports, log samples, scan results
   - **Interview subjects**: Roles the auditor will want to speak with
   - **Common gaps**: Evidence that is frequently missing or insufficient for this control
   - **Preparation tips**: Practical advice for gathering this evidence

4. **If audit-type is specified**, tailor the checklist:
   - `3pao`: Focus on FedRAMP SAR evidence requirements, emphasize technical testing artifacts
   - `annual`: Focus on changes since last assessment, ConMon evidence
   - `soc2`: Focus on operating effectiveness evidence over the observation period
   - `iso`: Focus on documented procedures and management review records
   - `pci`: Focus on scoping documentation and technical validation
   - `internal`: Focus on self-assessment evidence and improvement tracking

5. **If a family is provided** instead of specific controls, expand to all controls in that family at the applicable baseline (default: Moderate for NIST/FedRAMP).

6. **If no arguments provided**, ask the user which framework and controls to generate a checklist for.

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
