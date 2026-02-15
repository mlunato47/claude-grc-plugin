# /grc:score-maturity

Score control implementation maturity on a 0–5 scale with actionable guidance to reach the next level.

## Usage

```
/grc:score-maturity [framework] [family-or-control] [baseline?]
```

The user optionally provides implementation descriptions or narrative text. If no content is provided, the command asks structured questions.

## Arguments

- **framework**: The compliance framework. Accepts: `nist`, `fedramp`, `fisma`, `cmmc`, `soc2`, `iso27001`, `pci`, `hipaa`, `cis`, `cobit`
- **family-or-control**: A control family (e.g., `ac`, `ia`) or specific control ID (e.g., `ac-2`, `ia-2`)
- **baseline** (optional): `low`, `moderate`, `high`. Defaults to `moderate` for NIST/FedRAMP.

## Examples

```
/grc:score-maturity fedramp ac-2
/grc:score-maturity fedramp ac moderate
/grc:score-maturity nist ia
/grc:score-maturity cmmc 3.5
/grc:score-maturity soc2 CC6
/grc:score-maturity cobit DSS02
```

## Behavior

When invoked:

1. **Display the Data Sensitivity Notice** at the top of every response if the user provides content. If no content is provided and the command enters interactive/question mode, the notice is not needed.

2. **Read the appropriate reference files**:
   - `skills/grc-knowledge/audits/narrative-quality-criteria.md` for the 0–5 maturity scale
   - Framework file from `skills/grc-knowledge/frameworks/` for control details

3. **Determine mode based on user input**:

   **Mode A: Content-based scoring** (user provides narrative or implementation description)
   - Score each control directly using the 0–5 maturity scale
   - Apply the same criteria as `/grc:review-narrative` but focus on the score and "next level" guidance
   - For a family, score each control individually and compute an overall family score

   **Mode B: Question-based scoring** (no content provided)
   - Ask structured questions about the implementation for each control or the family
   - Questions organized around the Five W's and maturity indicators:

   For each control, ask about:
   1. **Documentation**: Is there a written narrative? How detailed?
   2. **Implementation**: Is the control technically implemented? Fully or partially?
   3. **Automation**: Is the control automated, manual, or hybrid?
   4. **Repeatability**: Is the process consistent and repeatable? Documented procedures?
   5. **Measurement**: Are there metrics? How is effectiveness tracked?
   6. **Review**: When was the last review? How often?
   7. **Evidence**: What evidence exists? Could you produce it for an auditor today?

   Score based on responses:
   - 0 (Absent): Not documented, not implemented
   - 1 (Stub): Documented at a high level only, minimal implementation
   - 2 (Vague): Partially implemented, inconsistent, minimal documentation
   - 3 (Adequate): Implemented with documentation, repeatable, basic evidence
   - 4 (Strong): Fully implemented, automated where possible, metrics tracked, evidence ready
   - 5 (Exemplary): Continuously optimized, comprehensive metrics, proactive improvement

4. **Generate "To Reach Next Level" guidance** for each control:
   - Specific actions to move from current level to next level
   - Prioritized by impact
   - Actionable and concrete (not generic advice)

5. **For family-level scoring**, provide:
   - Individual control scores
   - Overall family score (weighted average or mode)
   - Maturity distribution chart (how many controls at each level)
   - Priority recommendations (which controls to improve first)

6. **CRITICAL**: Maturity scoring is about the quality of documentation, implementation consistency, and operational maturity — not about whether the security measures are "good enough." A maturity score of 3 means "adequately documented and implemented" not "adequately secure."

7. **If no arguments provided**, ask the user which framework and control family or control ID to score.

## Output Format

### For individual control (content-based):

```
> **Before sharing GRC artifacts**: Consider replacing real system names, IP addresses, personnel names, agency names, and CVE IDs with generic placeholders. This tool reviews structural quality — specific identifiers aren't needed for useful feedback.

## Maturity Score: [Framework] [Control-ID] — [Title]

**Baseline**: [Baseline]
**Current Maturity**: [Score] / 5 — [Level Name]

### Score Rationale
[2-3 sentences explaining why this score was assigned, referencing specific elements present or missing]

### To Reach Level [Current + 1] — [Next Level Name]

1. [Specific action]
2. [Specific action]
3. [Specific action]

### Detailed Assessment
[Brief Five W's and quality assessment — condensed version of review-narrative output]
```

### For family-level scoring:

```
> [Redaction reminder if content was provided]

## Maturity Assessment: [Framework] [Family] Family

**Baseline**: [Baseline]
**Overall Family Maturity**: [Score] / 5 — [Level Name]

### Control Scores

| Control | Title | Score | Level |
|---------|-------|-------|-------|
| [ID] | [Title] | [0-5] | [Name] |

### Maturity Distribution

| Level | Count | Controls |
|-------|-------|----------|
| 5 — Exemplary | [N] | [IDs] |
| 4 — Strong | [N] | [IDs] |
| 3 — Adequate | [N] | [IDs] |
| 2 — Vague | [N] | [IDs] |
| 1 — Stub | [N] | [IDs] |
| 0 — Absent | [N] | [IDs] |

### Priority Improvements

1. **[Control-ID]** (currently [score]): [Action to reach next level]
2. **[Control-ID]** (currently [score]): [Action]
3. **[Control-ID]** (currently [score]): [Action]

### Overall Recommendations
[2-3 family-level recommendations for systematic maturity improvement]
```

### For question-based mode:

```
## Maturity Assessment: [Framework] [Family/Control]

I'll ask you a few questions about your implementation to score maturity. Answer what you can — you can skip any question.

### [Control-ID]: [Title]

1. **Documentation**: Is there a written implementation narrative for [Control-ID] in your SSP? (None / Brief / Detailed)
2. **Implementation**: Is [brief control description] currently in place? (No / Partially / Fully)
3. **Automation**: Is this automated, manual, or a mix?
4. **Evidence**: If an auditor asked today, could you produce evidence? (No / With effort / Readily available)
5. **Last review**: When was this last reviewed or tested?

[Continue for each control in scope, or group similar controls]
```

## Notes

- Question-based mode should ask concise questions — don't overwhelm with 7 questions per control for a full family. Group where possible.
- For large families (AC, SC, SI), focus questions on the most impactful controls at the baseline level.
- Maturity scoring is relative to the framework's expectations, not an absolute security measure.
- The 0–5 scale aligns with common maturity models (similar to CMMI, COBIT capability levels) but is adapted for control implementation quality.
