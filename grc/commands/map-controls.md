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
/grc:map-controls il5 to nist
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
   - If source or target is a DoD/DoW Impact Level (`dod`, `dow`, `il2`/`il4`/`il5`/`il6`) → read `mappings/nist-to-dod-il.md`. ILs are baseline *compositions*, not a control catalog: resolve the IL to its NIST composition (FedRAMP baseline + FedRAMP+ + CNSSI 1253 additions), then chain to the other framework as normal. When the source is an IL and no control-id is given (e.g., `il5 to nist`), report the IL's full baseline composition rather than a single control. Note that no commercial certification provides reciprocity toward an IL — only FedRAMP authorizations do.
   - If source or target is a FedRAMP 20x KSI (`ksi`, `20x`) → read `frameworks/fedramp-20x.md`. Each CR26 KSI carries an official NIST 800-53 control mapping (a `controls` array in FedRAMP's machine-readable rules); map KSI → NIST via that mapping (fetch the rules JSON from the doc index in that file for the authoritative list), then chain to other frameworks through NIST as normal.
   - If source or target is ITAR (`itar`) → read `frameworks/itar.md`. ITAR is a conduct regulation, not a control catalog: there is no official DDTC↔NIST crosswalk. Use that file's "NIST 800-53 families" practitioner mapping (AC/PS/PE/AU/SC/MP/IR/SA-SR) and clearly label it as convention, not authority.

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
