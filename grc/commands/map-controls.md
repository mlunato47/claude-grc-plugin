---
description: "Map controls between compliance frameworks using NIST 800-53 as the universal hub"
---

# /grc:map-controls

Map controls between compliance frameworks using NIST 800-53 as the universal hub.

## Usage

```
/grc:map-controls [source-framework] [control-id] to [target-framework]
```

## Arguments

- **source-framework**: The framework the control belongs to
- **control-id**: The specific control ID to map
- **target-framework**: The framework to map to

## Examples

```
/grc:map-controls nist ac-2 to soc2
/grc:map-controls soc2 CC6.1 to iso27001
/grc:map-controls pci 8.3 to nist
/grc:map-controls hipaa 164.312(a)(1) to nist
/grc:map-controls iso27001 A.8.5 to cmmc
/grc:map-controls cis 5.2 to nist
```

## Behavior

When invoked:

1. **Parse the source framework, control ID, and target framework** from arguments.

2. **Determine the mapping path**:
   - If source is NIST → direct mapping to target (read `mappings/nist-to-{target}.md`)
   - If target is NIST → reverse lookup in `mappings/nist-to-{source}.md`
   - If neither is NIST → chain through NIST:
     a. Map source control → NIST 800-53 (read `mappings/nist-to-{source}.md` reverse)
     b. Map NIST control(s) → target (read `mappings/nist-to-{target}.md`)
   - If source is FedRAMP/FISMA → treat as NIST (same control IDs with parameters)

3. **Read the appropriate mapping file(s)** from `skills/grc-knowledge/mappings/`

4. **Read framework reference files** as needed for control details.

5. **Present the mapping** with full context:
   - Source control with description
   - NIST 800-53 intermediate mapping (if chaining)
   - Target control(s) with descriptions
   - Coverage assessment: Full, Partial, or Gap
   - Notes on nuances (one-to-many, scope differences, intent differences)

6. **If no arguments provided**, ask the user for source framework, control ID, and target framework.

## Output Format

```
## Control Mapping: [Source Framework] [Control-ID] → [Target Framework]

### Source Control
**[Source-ID]**: [Title]
[Brief description]

### NIST 800-53 Bridge (if chaining)
**[NIST-ID(s)]**: [Title(s)]

### Target Mapping

| Target Control | Title | Coverage | Notes |
|---------------|-------|----------|-------|
| [ID] | [Title] | Full/Partial | [Details] |

### Coverage Assessment
[Explanation of how well the mapping covers the intent of the source control]

### Gaps
[Any aspects of the source control not covered by the target framework]
```

## Notes

- Many mappings are one-to-many or many-to-one. Always show all related controls.
- Flag partial mappings clearly — a mapping may cover the intent but not the specific implementation requirement.
- When chaining through NIST, note that some fidelity may be lost in translation.
- For NIST ↔ FedRAMP, the controls are the same — highlight FedRAMP-specific parameters instead.
