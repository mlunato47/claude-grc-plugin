---
description: "OSCAL structure, readiness, and conversion guidance"
---

# /grc:oscal-guide

Provide OSCAL guidance — structure, readiness assessment, and conversion considerations.

## Usage

```
/grc:oscal-guide [topic]
```

## Arguments

- **topic**: The OSCAL topic to address. Accepts:
  - `overview` (default): What OSCAL is, models, and architecture
  - `ssp`: OSCAL SSP model structure and components
  - `readiness`: Assess whether your current SSP is ready for OSCAL conversion
  - `components`: How OSCAL component definitions work
  - `parameters`: How OSCAL handles ODPs/parameters
  - `inheritance`: How OSCAL models leveraged authorizations and inheritance
  - `tools`: OSCAL tooling ecosystem
  - `validation`: OSCAL validation approaches

## Examples

```
/grc:oscal-guide
/grc:oscal-guide overview
/grc:oscal-guide ssp
/grc:oscal-guide readiness
/grc:oscal-guide components
/grc:oscal-guide tools
```

## Behavior

When invoked:

1. **No redaction reminder needed for most topics** — OSCAL guidance is reference material. If the user pastes their SSP content for readiness assessment, display the Data Sensitivity Notice.

2. **Read the appropriate reference files**:
   - `skills/grc-knowledge/frameworks/oscal-reference.md` for OSCAL structure and concepts
   - `skills/grc-knowledge/audits/document-section-requirements.md` for SSP section requirements (for readiness topic)
   - `skills/grc-knowledge/oscal/nist-800-53-rev5/{family}.json` and `skills/grc-knowledge/oscal/fedramp-moderate-rev5/{family}.json` for live OSCAL data examples — when showing structure examples, read a real family file (e.g., `at.json` for a small example) instead of fabricating sample JSON

3. **For each topic**:

   **`overview`**: Present OSCAL models, layer architecture, current status, and FedRAMP OSCAL requirements. Explain why OSCAL matters and how it changes the GRC workflow.

   **`ssp`**: Deep dive into the OSCAL SSP model — metadata, system characteristics, system implementation, control implementation, back matter. Show the structure with examples.

   **`readiness`**: If the user provides SSP details, assess readiness for OSCAL conversion:
   - Are control narratives structured by component?
   - Are ODPs separated from prose?
   - Are roles consistently named?
   - Is inventory itemized?
   - Are diagrams separate, linkable files?
   - Score readiness and list conversion prerequisites.

   If no SSP details provided, present the readiness checklist from the reference file.

   **`components`**: Explain how OSCAL component definitions work — reusable security capability descriptions that can be referenced across controls. Show how to decompose monolithic narratives into component-based narratives.

   **`parameters`**: How OSCAL handles ODPs as first-class objects with `set-parameters`. Show the difference between catalog parameters, profile parameters, and SSP parameters.

   **`inheritance`**: How OSCAL models leveraged authorizations — `leveraged-authorizations` section, `provided` and `inherited` markers on by-components, and how to trace the inheritance chain.

   **`tools`**: Overview of OSCAL tooling ecosystem — authoring, validation, comparison, FedRAMP-specific tools.

   **`validation`**: What OSCAL validation checks (structural, content, FedRAMP-specific) and how to run them.

4. **If no arguments provided**, show the overview topic.

## Output Format

```
## OSCAL Guide: [Topic]

[Content organized with clear sections, code examples where relevant, and practical guidance]

### Key Concepts
[Core concepts for this topic]

### Structure
[Relevant OSCAL structure with annotated examples]

### Practical Guidance
[Actionable steps or considerations]

### Common Pitfalls
[Mistakes to avoid]

### Resources
[Relevant tools, documentation, templates]
```

## Notes

- OSCAL is evolving — always reference the current stable version (1.1.2 as of this writing).
- FedRAMP OSCAL requirements are separate from NIST OSCAL — FedRAMP adds extensions and constraints.
- OSCAL conversion is a significant effort — recommend starting with new SSPs rather than converting existing ones when possible.
- This command is informational and educational — it doesn't generate OSCAL output.
