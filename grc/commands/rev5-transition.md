# /grc:rev5-transition

Provide NIST 800-53 Rev 4 to Rev 5 transition guidance — control mapping, gap analysis, and migration steps.

## Usage

```
/grc:rev5-transition [action] [control-or-family?]
```

## Arguments

- **action**: What to do. Accepts:
  - `lookup` (default): Look up what changed for a specific Rev 4 control in Rev 5
  - `gaps`: Show new controls added in Rev 5 that need implementation
  - `withdrawn`: Show controls withdrawn in Rev 5 and where they went
  - `baseline-changes`: Show what was added/removed from baselines between revisions
  - `checklist`: Full transition checklist with steps and sequence

- **control-or-family** (optional): A Rev 4 control ID (e.g., `ac-2`, `sa-12`) or family (e.g., `ac`, `sa`) to look up

## Examples

```
/grc:rev5-transition lookup sa-12
/grc:rev5-transition lookup ac-2
/grc:rev5-transition gaps
/grc:rev5-transition gaps sr
/grc:rev5-transition withdrawn
/grc:rev5-transition baseline-changes moderate
/grc:rev5-transition checklist
```

## Behavior

When invoked:

1. **No redaction reminder needed** — this is a pure reference command comparing framework revisions. No user content is processed.

2. **Read the appropriate reference files**:
   - `skills/grc-knowledge/frameworks/nist-rev4-to-rev5.md` for the transition mapping
   - `skills/grc-knowledge/frameworks/nist-800-53.md` for Rev 5 control details
   - `skills/grc-knowledge/frameworks/fedramp.md` for FedRAMP-specific transition context

3. **For `lookup` action**:
   Given a Rev 4 control or family:
   - Show what changed between Rev 4 and Rev 5
   - If the control was withdrawn, show where the requirements moved
   - If the control was modified, highlight the key differences
   - If new enhancements were added, list them
   - Provide migration action for the SSP narrative

4. **For `gaps` action**:
   Show all controls that are new in Rev 5 (didn't exist in Rev 4):
   - New PT family controls
   - New SR family controls
   - New controls added to existing families
   - For each: baseline assignment, brief description, implementation effort estimate

   If a specific family is provided, show only new controls in that family.

5. **For `withdrawn` action**:
   Show all controls that were withdrawn in Rev 5:
   - Rev 4 control ID and title
   - Where the requirements were incorporated (Rev 5 control(s))
   - Migration action (move narrative, merge, or delete)

6. **For `baseline-changes` action**:
   Show what was added to and removed from a specific baseline:
   - Controls newly added to the baseline
   - Controls removed from the baseline
   - Enhancement changes (new required enhancements)

7. **For `checklist` action**:
   Generate a full transition checklist:
   - Pre-transition assessment steps
   - Gap analysis steps
   - SSP migration steps (control by control)
   - New control implementation steps
   - Assessment alignment steps
   - Package update and submission steps

8. **If no arguments provided**, show the overview of changes and ask what the user wants to dive into.

## Output Format

### For `lookup`:

```
## Rev 4 → Rev 5: [Control-ID] — [Title]

### Change Summary
[Brief description of what changed]

### Rev 4 → Rev 5 Mapping
| Aspect | Rev 4 | Rev 5 |
|--------|-------|-------|
| Control ID | [Same or new] | [ID] |
| Title | [Rev 4 title] | [Rev 5 title if different] |
| Baselines | [Rev 4 assignment] | [Rev 5 assignment] |
| Key Changes | — | [List of changes] |

### New Enhancements in Rev 5
| Enhancement | Title | Baseline |
|-------------|-------|----------|
| [Control-ID(X)] | [Title] | [L/M/H] |

### Migration Action
[What to do with the SSP narrative — update, merge, or move]
```

### For `gaps`:

```
## Rev 5 New Controls: [Family or "All"]

| Control | Title | Family | Baselines | Effort |
|---------|-------|--------|-----------|--------|
| [ID] | [Title] | [Family] | [L/M/H] | [Low/Medium/High] |

### By Priority
**Must implement (in your baseline)**: [List]
**Optional (above baseline)**: [List]
```

### For `withdrawn`:

```
## Withdrawn Controls (Rev 4 → Rev 5)

| Rev 4 Control | Title | Incorporated Into | Migration Action |
|---------------|-------|-------------------|-----------------|
| [ID] | [Title] | [Rev 5 control(s)] | [Move/Merge/Delete] |
```

### For `checklist`:

```
## Rev 4 → Rev 5 Transition Checklist

### Phase 1: Assessment
- [ ] [Step]

### Phase 2: Gap Analysis
- [ ] [Step]

### Phase 3: SSP Migration
- [ ] [Step]

### Phase 4: Implementation
- [ ] [Step]

### Phase 5: Assessment Alignment
- [ ] [Step]

### Phase 6: Package Update
- [ ] [Step]
```

## Notes

- The Rev 4 → Rev 5 transition is a significant effort, especially for the new PT and SR families.
- Most controls kept the same ID but the text, parameters, and enhancements may have changed. Don't assume "same ID = no change."
- FedRAMP has published Rev 5 baselines with their own transition timeline — check FedRAMP.gov for the latest.
- This command pairs with `/grc:gap-analysis` to assess Rev 5 readiness in detail.
