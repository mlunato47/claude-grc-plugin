# /grc:sar-response

Help draft structured responses to SAR (Security Assessment Report) findings.

## Usage

```
/grc:sar-response [framework?] [action?]
```

The user pastes a SAR finding after invoking the command.

## Arguments

- **framework** (optional): `fedramp`, `nist`, `fisma`. Defaults to `fedramp`.
- **action** (optional):
  - `respond` (default): Draft a structured response to a finding
  - `disagree`: Draft a response disagreeing with a finding (false positive or risk acceptance)
  - `template`: Show the blank response template structure

## Examples

```
/grc:sar-response fedramp
/grc:sar-response fedramp respond
/grc:sar-response fedramp disagree
/grc:sar-response template
```

## Behavior

When invoked:

1. **Display the Data Sensitivity Notice** at the top of every response (see SKILL.md Data Handling section). SAR findings may contain system-specific vulnerability details.

2. **Read the appropriate reference files**:
   - `skills/grc-knowledge/audits/sar-response-patterns.md` for response templates and quality checklist
   - `skills/grc-knowledge/audits/document-section-requirements.md` for POA&M field requirements
   - `skills/grc-knowledge/conmon/poam-management.md` for severity SLAs

3. **For `respond` action**:

   Analyze the pasted finding and generate a structured response covering:

   **a. Acknowledgment**
   - Confirm understanding of the finding
   - Note agreement or partial agreement

   **b. Root Cause Analysis**
   - Suggest root cause categories based on the finding type (operational, documentation, technical)
   - Provide placeholder language the user can customize
   - Avoid suggesting root causes that evaluate security posture

   **c. Remediation Plan**
   - Suggest specific, actionable remediation steps
   - Include role placeholders for responsible parties
   - Calculate target dates based on severity SLA
   - Suggest granular milestones (not just "remediate")

   **d. Interim Mitigations**
   - Suggest interim mitigations appropriate to the finding type
   - For Critical/High: emphasize urgency of interim controls

   **e. Verification Approach**
   - Suggest evidence that would demonstrate closure
   - Note whether 3PAO re-verification is likely needed

   **f. POA&M Entry Draft**
   - Generate a draft POA&M entry aligned with the response
   - Pre-populate fields based on the finding

4. **For `disagree` action**:

   Generate a structured disagreement response:
   - False positive template with evidence requirements
   - Risk acceptance template with compensating controls and justification structure
   - Deviation request reference

5. **For `template` action**:

   Show the blank response template from the reference file. No user content needed; no redaction reminder.

6. **CRITICAL**: Never evaluate whether the finding is valid or whether the described vulnerability is actually serious. Only help structure the response. Feedback is structural: "your response should include interim mitigations for a High finding" not "this vulnerability could lead to data breach."

7. **If no finding is pasted**, ask the user to provide the SAR finding they want to respond to.

## Output Format

### For `respond`:

```
> **Before sharing GRC artifacts**: Consider replacing real system names, IP addresses, personnel names, agency names, and CVE IDs with generic placeholders (e.g., "[Agency Name]", "[System Name]", "CVE-XXXX-XXXXX"). This tool helps structure responses — specific identifiers aren't needed.

## SAR Finding Response: [Control-ID] — [Finding Title/Summary]

**Finding Type**: [Operational / Documentation / Technical]
**Severity**: [Critical / High / Moderate / Low]
**SLA**: [X] days from detection

---

### Draft Response

**Response to [Finding ID]: [Control-ID] — [Title]**

**Acknowledgment**: [Organization Name] acknowledges this finding. [Agree/Partially agree].

**Root Cause**: [Suggested root cause language — user should customize]

**Remediation Plan**:
1. [Action] — [Role] — Target: [Date based on SLA]
2. [Action] — [Role] — Target: [Date]
3. [Action] — [Role] — Target: [Date]

**Interim Mitigation**: [Suggested interim control appropriate to finding type]

**Verification**: [Evidence that will demonstrate closure]

**POA&M Reference**: [Draft POA&M entry ID]

---

### Draft POA&M Entry

| Field | Value |
|-------|-------|
| POA&M ID | [Suggested ID] |
| Weakness Name | [From finding] |
| Description | [Structured description] |
| Security Control | [Control-ID] |
| Source | Assessment / SAR |
| Risk Rating | [From finding] |
| Scheduled Completion | [Date per SLA] |
| Milestones | [Aligned with remediation plan] |
| Status | Open |

---

### Response Quality Check
- [ ] Root cause identified (not just symptom)
- [ ] Remediation actions are specific
- [ ] Target dates within SLA
- [ ] Responsible roles named
- [ ] Interim mitigations described (Critical/High)
- [ ] Verification approach defined
- [ ] POA&M entry created
```

## Notes

- Response quality is as important as remediation speed — vague responses create follow-up findings.
- Each finding must have its own response — copy-paste across findings is an anti-pattern that auditors flag.
- The draft response is a starting point — the user must customize with their specific context.
- This command pairs with `/grc:review-poam` to validate the resulting POA&M entries.
