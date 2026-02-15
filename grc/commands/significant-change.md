# /grc:significant-change

Analyze whether a system change qualifies as "significant" and determine the required actions.

## Usage

```
/grc:significant-change [framework?] [change-description]
```

The user describes the change in the prompt or as an argument.

## Arguments

- **framework** (optional): `fedramp`, `nist`, `fisma`. Defaults to `fedramp`.
- **change-description**: Free-text description of the system change (can be inline or pasted after invoking).

## Examples

```
/grc:significant-change fedramp We are migrating our database from self-managed PostgreSQL to AWS RDS
/grc:significant-change We are adding a new API gateway in front of our application
/grc:significant-change fedramp Upgrading from RHEL 8 to RHEL 9 across all production servers
/grc:significant-change Our ISSO is leaving and we are assigning a new ISSO
/grc:significant-change Adding a new interconnection to an agency's identity provider
```

## Behavior

When invoked:

1. **Display the Data Sensitivity Notice** at the top of every response (see SKILL.md Data Handling section). Users may describe system architecture details.

2. **Read the appropriate reference files**:
   - `skills/grc-knowledge/audits/significant-change-criteria.md` for the decision criteria and category definitions
   - Framework file from `skills/grc-knowledge/frameworks/` if framework-specific parameters are needed

3. **Classify the change**:
   - Walk through the significant change decision tree from the reference file
   - Determine the change category (1-5) or determine it is not significant
   - Explain the rationale for the classification

4. **If significant**, provide:

   **a. Change Category**
   Which of the 5 categories it falls into and why.

   **b. Affected Control Families**
   List the control families impacted by this change, using the control-to-change-type mapping from the reference file.

   **c. Required Actions — Before the Change**
   Specific steps to take before implementing (SIA, notifications, SSP draft updates, etc.).

   **d. Required Actions — After the Change**
   Steps after implementation (SSP update, assessment, POA&M, artifact submission).

   **e. Documentation Updates**
   Specific SSP sections, diagrams, appendices, and other documents that need updating.

   **f. Assessment Impact**
   Whether a 3PAO assessment is likely needed and what scope.

5. **If NOT significant**, explain why and recommend:
   - Document in change management log
   - Standard ConMon reporting
   - Any minor SSP updates that might still be prudent

6. **CRITICAL**: Never evaluate whether the change is a good idea or whether the new architecture is secure. Only assess whether the change qualifies as significant and what compliance actions are required. Feedback is procedural, not architectural.

7. **If no change description is provided**, ask the user to describe the change.

## Output Format

```
> **Before sharing GRC artifacts**: Consider replacing real system names, IP addresses, personnel names, agency names, and CVE IDs with generic placeholders. This tool assesses change significance — specific identifiers aren't needed for useful analysis.

## Significant Change Analysis

**Change**: [Brief summary of the described change]
**Framework**: [Framework]
**Classification**: ✅ Significant Change — Category [X]: [Category Name]
*or* ❌ Not a Significant Change

---

### Classification Rationale
[2-3 sentences explaining why this is/isn't significant, referencing the decision criteria]

### Change Category
**Category [X] — [Name]**: [Description of why this category applies]

### Affected Control Families

| Family | Impact | Reason |
|--------|--------|--------|
| [Family] | Primary / Secondary | [Why this family is affected] |

### Required Actions

**Before Implementation**:
1. [ ] [Action — e.g., Complete Security Impact Analysis]
2. [ ] [Action — e.g., Notify AO of planned change]
3. [ ] [Action — e.g., Submit SCR to FedRAMP PMO]
4. [ ] [Action — e.g., Draft SSP updates for affected sections]

**After Implementation**:
1. [ ] [Action — e.g., Update SSP Section X with actual implementation]
2. [ ] [Action — e.g., Update authorization boundary diagram]
3. [ ] [Action — e.g., Assess affected controls]
4. [ ] [Action — e.g., Submit updated package]

### Documentation Updates

| Document | Section/Element | Update Needed |
|----------|----------------|---------------|
| SSP | [Section] | [What to update] |
| [Diagram] | | [What to update] |

### Assessment Impact
[Whether 3PAO reassessment is likely needed, scope, and timing]
```

## Notes

- The significant change determination is based on FedRAMP Continuous Monitoring Strategy Guide criteria by default.
- When in doubt, classify as significant — the cost of over-reporting is much lower than under-reporting.
- Multiple changes can be analyzed together if they are part of the same initiative.
- This command pairs well with `/grc:evidence-checklist` to prepare for any assessment triggered by the change.
