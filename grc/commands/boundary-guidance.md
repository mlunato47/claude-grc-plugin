# /grc:boundary-guidance

Provide guidance on authorization boundary definition based on system architecture.

## Usage

```
/grc:boundary-guidance [framework?] [service-model?]
```

The user can optionally describe their architecture for tailored guidance.

## Arguments

- **framework** (optional): `fedramp`, `nist`, `fisma`. Defaults to `fedramp`.
- **service-model** (optional): `iaas`, `paas`, `saas`. Helps tailor boundary patterns.

## Examples

```
/grc:boundary-guidance fedramp saas
/grc:boundary-guidance fedramp iaas
/grc:boundary-guidance fedramp
/grc:boundary-guidance We have a SaaS app on AWS with RDS, ECS, S3, CloudFront, and a VPN connection to an agency
```

## Behavior

When invoked:

1. **Display the Data Sensitivity Notice** if the user describes their specific architecture (see SKILL.md Data Handling section). If only a generic service model is specified, the notice is not needed.

2. **Read the appropriate reference files**:
   - `skills/grc-knowledge/audits/boundary-guidance.md` for boundary patterns, common mistakes, and diagram requirements
   - `skills/grc-knowledge/audits/control-inheritance.md` for inheritance context
   - Framework file if framework-specific requirements apply

3. **If the user describes their architecture**, provide tailored guidance:

   **a. Boundary Recommendation**
   - Which components should be inside the boundary
   - Which components should be outside (with interconnection documentation)
   - Gray areas that need a decision, with pros/cons of each option

   **b. Diagram Requirements**
   - What the authorization boundary diagram must show
   - What the network architecture diagram must show
   - What the data flow diagram must show

   **c. Interconnection Inventory**
   - External connections that cross the boundary
   - What each interconnection needs (ISA, ports/protocols, security measures)

   **d. Common Mistakes for This Architecture**
   - Specific boundary mistakes relevant to the described architecture
   - How the 3PAO is likely to challenge the boundary

4. **If no architecture is described**, provide general guidance:
   - Boundary definition principles
   - Service-model-specific patterns (if service model provided)
   - Must-include and typically-excluded component lists
   - Diagram requirements checklist
   - Common mistakes overview

5. **CRITICAL**: Never evaluate whether the architecture is secure or whether specific components should be included for security reasons. Only advise on what the boundary should encompass for compliance purposes and what documentation is required. Feedback is procedural: "CI/CD pipelines that deploy to production are typically inside the boundary" not "excluding CI/CD from the boundary creates a security risk."

6. **If no arguments provided**, ask the user about their framework and service model, or invite them to describe their architecture.

## Output Format

### For architecture-specific guidance:

```
> **Before sharing GRC artifacts**: Consider replacing real system names, IP addresses, personnel names, agency names, and CVE IDs with generic placeholders. This tool provides boundary guidance — specific identifiers aren't needed.

## Authorization Boundary Guidance: [Service Model] — [Framework]

---

### Recommended Boundary

**Inside the boundary**:
| Component | Reason |
|-----------|--------|
| [Component] | [Why it belongs inside] |

**Outside the boundary (document as interconnection)**:
| Component | Reason | Interconnection Required |
|-----------|--------|------------------------|
| [Component] | [Why it's outside] | [ISA/MOU/API docs needed] |

**Decision points** (could go either way):
| Component | Inside? | Outside? | Recommendation |
|-----------|---------|----------|----------------|
| [Component] | [Pros] | [Pros] | [Recommendation with rationale] |

### Diagram Checklist

**Authorization Boundary Diagram**:
- [ ] [Required element]
- [ ] [Required element]

**Network Architecture Diagram**:
- [ ] [Required element]

**Data Flow Diagram**:
- [ ] [Required element]

### Interconnections to Document (CA-3)

| Connection | Remote System | Direction | Ports/Protocols | Security |
|------------|--------------|-----------|-----------------|----------|
| [Name] | [System] | [In/Out/Both] | [Ports] | [Encryption, auth] |

### Watch Out For
- [Architecture-specific boundary mistake]
- [Common 3PAO challenge for this pattern]
```

### For general guidance:

```
## Authorization Boundary Guidance: [Service Model] — [Framework]

### Boundary Principles
[Key principles for boundary definition]

### What Goes Inside
[Component categories that must be in the boundary]

### What Stays Outside
[Components typically outside with interconnection requirements]

### Diagram Requirements
[Checklist of required diagram elements]

### Common Mistakes
[Service-model-specific boundary mistakes]
```

## Notes

- The authorization boundary is the single most consequential decision in an SSP — everything flows from it.
- When in doubt, include the component inside the boundary. Excluding something that should be inside creates a finding; including something extra just increases scope.
- This command pairs with `/grc:inheritance` to understand how inherited controls interact with the boundary.
- Boundary decisions should be reviewed annually and after any significant change.
