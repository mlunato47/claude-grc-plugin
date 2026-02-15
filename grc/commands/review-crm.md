# /grc:review-crm

Review a Customer Responsibility Matrix (CRM) or Customer Implementation Summary (CIS) for coverage, clarity, and completeness.

## Usage

```
/grc:review-crm [framework?] [baseline?]
```

The user pastes their CRM content after invoking the command.

## Arguments

- **framework** (optional): `fedramp`, `nist`, `fisma`. Defaults to `fedramp`.
- **baseline** (optional): `low`, `moderate`, `high`. Defaults to `moderate`.

## Examples

```
/grc:review-crm
/grc:review-crm fedramp moderate
/grc:review-crm fedramp high
/grc:review-crm nist moderate
```

## Behavior

When invoked:

1. **Display the Data Sensitivity Notice** at the top of every response (see SKILL.md Data Handling section).

2. **Read the appropriate reference files**:
   - `skills/grc-knowledge/audits/document-section-requirements.md` for CRM requirements and expected distribution
   - Framework file from `skills/grc-knowledge/frameworks/` for baseline control list
   - `skills/grc-knowledge/audits/narrative-quality-criteria.md` for quality indicators

3. **Evaluate the CRM** against these criteria:

   **a. Coverage Assessment**
   - Count controls/families present in the CRM vs. total baseline controls
   - Calculate overall coverage percentage
   - Identify missing control families entirely
   - Identify individual controls with customer responsibility that are not addressed

   **b. Responsibility Distribution**
   Categorize each control's designation and report the distribution:
   - **CSP-Implemented**: CSP fully handles
   - **Customer-Implemented**: Customer must fully implement
   - **Shared**: Both parties (must specify the split)
   - **Inherited**: From underlying infrastructure provider
   Compare the distribution against expected patterns (see document-section-requirements.md)

   **c. Clarity Assessment**
   For each entry (especially Shared controls):
   - Is the customer's responsibility clearly described?
   - Are specific actions identified (not just "customer is responsible")?
   - Are customer-responsible ODP values called out?
   - Can a customer read this and know exactly what they need to do?

   **d. Common CRM Gaps**
   Check for these frequently problematic areas:
   - **PE family**: Often omitted entirely for cloud — should have explicit "Inherited from CSP" statements
   - **PS family**: Screening for CSP admin access often unclear
   - **CP/IR shared responsibilities**: Which tier does the customer handle?
   - **AU requirements**: Does the customer get raw logs? Processed alerts? What format?
   - **CM configuration**: Which settings are customer-manageable vs. CSP-locked?
   - **IA credentials**: Customer credential management vs. CSP authentication platform
   - **SC encryption**: Who manages keys? Customer-managed encryption keys (CMEK)?
   - **AT training**: Customer training on CSP platform vs. general security awareness

4. **CRITICAL**: Never evaluate whether the responsibility split is appropriate for security. Only assess whether the CRM is complete, clear, and actionable for the customer. Feedback is structural: "the shared responsibility description for AC-2 doesn't specify what the customer must configure" not "customers should have more control over account management."

5. **If no CRM content is provided**, ask the user to paste their CRM content.

## Output Format

```
> **Before sharing GRC artifacts**: Consider replacing real system names, IP addresses, personnel names, agency names, and CVE IDs with generic placeholders (e.g., "[Agency Name]", "[System Name]"). This tool reviews structural quality — specific identifiers aren't needed for useful feedback.

## CRM Review: [Framework] [Baseline]

---

### Coverage Summary

**Overall coverage**: [X] / [Total baseline controls] ([%])

| Family | Expected | Present | Coverage | Notes |
|--------|----------|---------|----------|-------|
| AC | [X] | [Y] | [%] | [Missing controls] |
| AT | [X] | [Y] | [%] | |
| AU | [X] | [Y] | [%] | |
| ... | ... | ... | ... | |

**Missing families**: [List of families with 0% coverage]

### Responsibility Distribution

| Designation | Count | Percentage |
|-------------|-------|------------|
| CSP-Implemented | [X] | [%] |
| Customer-Implemented | [X] | [%] |
| Shared | [X] | [%] |
| Inherited | [X] | [%] |
| Not Specified | [X] | [%] |

**Expected vs. Actual**: [Brief comparison to typical distribution patterns]

### Clarity Assessment

**Clear entries**: [X] / [Total] — customer knows exactly what to do
**Vague entries**: [X] / [Total] — "customer is responsible" without specifics
**Missing customer actions**: [X] / [Total] — shared but no customer-side description

**Vague entries flagged**:
| Control | Designation | Issue |
|---------|-------------|-------|
| [ID] | Shared | [What's unclear] |

### Common Gap Check

| Gap Area | Status | Finding |
|----------|--------|---------|
| PE family explicit inheritance | ✅ / ❌ | [Details] |
| PS shared screening | ✅ / ❌ | [Details] |
| CP/IR tier responsibilities | ✅ / ❌ | [Details] |
| AU log access clarity | ✅ / ❌ | [Details] |
| CM customer-configurable scope | ✅ / ❌ | [Details] |
| IA credential management split | ✅ / ❌ | [Details] |
| SC key management | ✅ / ❌ | [Details] |
| AT platform training | ✅ / ❌ | [Details] |

### Recommendations

1. **Coverage**: [Missing controls or families to add]
2. **Clarity**: [Vague entries that need specific customer actions]
3. **Gaps**: [Common gap areas to address]
4. **Format**: [Structural improvements]
```

## Notes

- CRMs are customer-facing documents — clarity is paramount. An ambiguous CRM creates compliance risk for the customer.
- The expected responsibility distribution varies by service model (IaaS vs. PaaS vs. SaaS). SaaS typically has more CSP-implemented controls.
- For FedRAMP, the CRM is Appendix H of the SSP and is reviewed by 3PAOs during assessment.
- Partial CRMs (e.g., just one family) are fine to review — the coverage assessment will note what's included vs. total.
