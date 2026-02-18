---
description: "Review a control implementation narrative for completeness and quality"
---

# /grc:review-narrative

Review a control implementation narrative for completeness and quality.

## Usage

```
/grc:review-narrative [framework] [control-id] [baseline?]
```

The user pastes their narrative text after invoking the command, or includes it as part of the prompt.

## Arguments

- **framework**: The compliance framework. Accepts: `nist`, `fedramp`, `fisma`, `cmmc`, `soc2`, `iso27001`, `pci`, `hipaa`, `cis`
- **control-id**: The specific control ID (e.g., `ac-2`, `ia-2`, `sc-7`)
- **baseline** (optional): `low`, `moderate`, `high`. Defaults to `moderate` for NIST/FedRAMP.

## Examples

```
/grc:review-narrative fedramp ac-2
/grc:review-narrative fedramp ac-2 high
/grc:review-narrative nist ia-2 moderate
/grc:review-narrative cmmc 3.5.3
```

## Behavior

When invoked:

1. **Display the Data Sensitivity Notice** at the top of every response (see SKILL.md Data Handling section).

2. **Read the appropriate reference files**:
   - Framework file from `skills/grc-knowledge/frameworks/` for control details and ODP values
   - `skills/grc-knowledge/audits/narrative-quality-criteria.md` for scoring rubric
   - Mapping files if cross-framework context is helpful

3. **Evaluate the narrative** against these criteria:

   **a. Five W's Completeness**
   For each element (What, Who, How, When, Where), determine if it is:
   - **Present**: Clearly addressed with specifics
   - **Partial**: Mentioned but vague or incomplete
   - **Missing**: Not addressed at all

   **b. ODP/Parameter Check**
   For each organization-defined parameter required by the control:
   - State what the parameter requires
   - Note the FedRAMP-required value (if FedRAMP framework and value is mandated)
   - State what value was found in the narrative (or "Not specified")
   - Flag mismatches with framework-required values

   **c. Enhancement Coverage**
   For each enhancement applicable at the stated baseline:
   - State whether it is Addressed, Partially Addressed, or Not Addressed in the narrative
   - Note what's missing for partially addressed enhancements

   **d. Language Quality**
   Identify specific instances of:
   - Aspirational/future-tense language
   - Passive voice without identified actors
   - Vague mechanisms
   - Policy echoing (restating the requirement)
   - Conditional/hedging language
   - TBD or placeholder values

   **e. Maturity Score**
   Assign a score from 0–5 per the maturity scale in `narrative-quality-criteria.md`:
   - 0: Absent — no narrative
   - 1: Stub — restates requirement only
   - 2: Vague — attempts implementation but missing specifics
   - 3: Adequate — all Five W's present, ODPs filled, some quality issues
   - 4: Strong — specific, active voice, all enhancements, clear responsibility
   - 5: Exemplary — everything in 4 plus evidence references, exception handling, above-baseline coverage

4. **Generate actionable recommendations** — each recommendation should be specific and include suggested phrasing where possible. Focus on structural completeness, not on the security posture of the described system.

5. **CRITICAL**: Never evaluate whether the described system is actually secure. Only assess whether the narrative adequately describes the implementation. Feedback must be structural ("the narrative doesn't state who reviews accounts") not evaluative ("your account management process is insecure").

6. **If no narrative text is provided**, ask the user to paste their control implementation narrative.

## Output Format

```
> **Before sharing GRC artifacts**: Consider replacing real system names, IP addresses, personnel names, agency names, and CVE IDs with generic placeholders (e.g., "[Agency Name]", "[System Name]", "10.x.x.x"). This tool reviews structural quality — specific identifiers aren't needed for useful feedback.

## Narrative Review: [Framework] [Control-ID] — [Title]

**Baseline**: [Low/Moderate/High]
**Maturity Score**: [0-5] — [Level Name]

---

### Five W's Assessment

| Element | Status | Finding |
|---------|--------|---------|
| **What** (Control objective) | ✅ Present / ⚠️ Partial / ❌ Missing | [Details] |
| **Who** (Responsible parties) | ✅ / ⚠️ / ❌ | [Details] |
| **How** (Implementation method) | ✅ / ⚠️ / ❌ | [Details] |
| **When** (Frequency/timing) | ✅ / ⚠️ / ❌ | [Details] |
| **Where** (Scope/boundary) | ✅ / ⚠️ / ❌ | [Details] |

### Parameter Check

| Parameter | Required Value | Found Value | Status |
|-----------|---------------|-------------|--------|
| [ODP description] | [FedRAMP value or "Org-defined"] | [Value from narrative] | ✅ / ❌ |

### Enhancement Coverage ([Baseline])

| Enhancement | Status | Notes |
|-------------|--------|-------|
| [Control-ID(Enhancement #)] | ✅ Addressed / ⚠️ Partial / ❌ Not Addressed | [What's missing] |

### Language Quality Findings

- [Finding 1 — e.g., "Line X uses future tense: 'will implement' — should describe current state"]
- [Finding 2]

### Recommendations

1. **[Category]**: [Specific recommendation with suggested phrasing]
2. **[Category]**: [Next recommendation]
```

## Notes

- The redaction reminder is displayed at the top of every review response, before any analysis.
- Feedback is always structural and about narrative quality, never about the security posture.
- When the user's narrative contains specific system details (IPs, agency names, etc.), the review should reference them only to note "the narrative includes [element]" — never to evaluate whether the system configuration is appropriate.
- Score should be calibrated: most real-world SSP narratives land at 2-3. A score of 4-5 is genuinely excellent.
