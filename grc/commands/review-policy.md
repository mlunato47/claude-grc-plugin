# /grc:review-policy

Review a policy document against framework requirements for structure, coverage, and language quality.

## Usage

```
/grc:review-policy [framework] [family]
```

The user pastes their policy text or outline after invoking the command.

## Arguments

- **framework**: The compliance framework. Accepts: `nist`, `fedramp`, `fisma`, `cmmc`, `soc2`, `iso27001`, `pci`, `hipaa`, `cis`
- **family**: The control family the policy covers (e.g., `ac`, `ia`, `ir`, `cm`, `cp`). For non-NIST frameworks, use the equivalent domain (e.g., `CC6` for SOC 2 logical access).

## Examples

```
/grc:review-policy fedramp ac
/grc:review-policy nist ir
/grc:review-policy fedramp cm
/grc:review-policy iso27001 A.8
/grc:review-policy pci 8
```

## Behavior

When invoked:

1. **Display the Data Sensitivity Notice** at the top of every response (see SKILL.md Data Handling section).

2. **Read the appropriate reference files**:
   - `skills/grc-knowledge/audits/document-section-requirements.md` for policy structural requirements
   - `skills/grc-knowledge/audits/narrative-quality-criteria.md` for language quality indicators
   - Framework file from `skills/grc-knowledge/frameworks/` for control family requirements

3. **Evaluate the policy** against these criteria:

   **a. Structural Elements Check**
   Verify presence of each required policy element:
   - Purpose statement
   - Scope definition
   - Roles and responsibilities
   - Policy statements (mandatory requirements)
   - Procedures reference
   - Definitions (recommended)
   - Compliance/enforcement section
   - Exceptions process (recommended)
   - Review frequency
   - Approval authority
   - Effective date
   - Version/revision history
   - Related documents (recommended)

   **b. Control Coverage**
   For the specified family at the applicable baseline:
   - Which controls in the family are addressed by the policy?
   - Which controls are partially addressed?
   - Which controls are not addressed at all?
   - Are enhancements covered where applicable?

   **c. Parameter Alignment**
   - Do policy-stated values align with framework ODP requirements?
   - Are timeframes, thresholds, and frequencies specific and measurable?
   - Do stated values match what should appear in the SSP?

   **d. Language Quality**
   - **Enforceable**: "shall", "must", "is required to" — for mandatory requirements
   - **Advisory**: "should", "may" — acceptable for guidance only
   - **Unenforceable**: "try to", "best effort", "as appropriate", "as feasible" — flag these
   - Count of SHALL/MUST vs SHOULD/MAY in policy statements
   - Flag any requirement statements using advisory language

4. **CRITICAL**: Never evaluate whether the policy's requirements are sufficient for actual security. Only assess whether the policy document is structurally complete, covers the applicable controls, and uses enforceable language. Feedback is structural: "the policy uses 'should' for the password complexity requirement — use 'shall' or 'must' for enforceability" not "your password requirements are too weak."

5. **If no policy text is provided**, ask the user to paste their policy content or outline.

## Output Format

```
> **Before sharing GRC artifacts**: Consider replacing real system names, IP addresses, personnel names, agency names, and CVE IDs with generic placeholders (e.g., "[Agency Name]", "[System Name]"). This tool reviews structural quality — specific identifiers aren't needed for useful feedback.

## Policy Review: [Family] Policy — [Framework]

---

### Structural Elements

| Element | Status | Finding |
|---------|--------|---------|
| Purpose | ✅ / ❌ | [Details] |
| Scope | ✅ / ⚠️ / ❌ | [Details] |
| Roles & Responsibilities | ✅ / ⚠️ / ❌ | [Details] |
| Policy Statements | ✅ / ⚠️ / ❌ | [Details] |
| Procedures Reference | ✅ / ❌ | [Details] |
| Definitions | ✅ / ❌ | |
| Compliance/Enforcement | ✅ / ❌ | [Details] |
| Exceptions Process | ✅ / ❌ | |
| Review Frequency | ✅ / ❌ | [Details] |
| Approval Authority | ✅ / ❌ | |
| Effective Date | ✅ / ❌ | |
| Revision History | ✅ / ❌ | |
| Related Documents | ✅ / ❌ | |

**Present**: [X] / 13

### Control Coverage ([Family] at [Baseline])

| Control | Addressed | Notes |
|---------|-----------|-------|
| [Control-ID] | ✅ / ⚠️ / ❌ | [What's covered or missing] |

**Coverage**: [X] / [Total family controls at baseline]

### Parameter Alignment

| Parameter | Policy Value | Framework Requirement | Status |
|-----------|-------------|----------------------|--------|
| [Parameter] | [Value from policy] | [Required value] | ✅ / ❌ |

### Language Quality

**Enforcement language distribution**:
- SHALL/MUST statements: [count]
- SHOULD/MAY statements: [count]
- Unenforceable phrasing: [count]

**Findings**:
- [Specific language finding with quote and recommendation]

### Recommendations

1. **[Category]**: [Specific recommendation]
2. **[Category]**: [Next recommendation]
```

## Notes

- Policies are reviewed for structural completeness and language quality, not for whether the requirements are good enough for security.
- The distinction between policy (what must be done) and procedure (how to do it) should be clear — policies should not contain step-by-step procedures.
- Review frequency should be at least annual for most frameworks (FedRAMP requires annual review of all policies).
