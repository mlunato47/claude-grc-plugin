---
description: "Validate SSP structure and completeness against FedRAMP template standards"
---

# /grc:review-ssp

Validate SSP structure and completeness against FedRAMP template standards.

## Usage

```
/grc:review-ssp [framework] [baseline?]
```

The user pastes their SSP table of contents, section headers, or section content after invoking the command.

## Arguments

- **framework**: The compliance framework. Accepts: `fedramp`, `nist`, `fisma`. Defaults to `fedramp`.
- **baseline** (optional): `low`, `moderate`, `high`. Defaults to `moderate`.

## Examples

```
/grc:review-ssp fedramp
/grc:review-ssp fedramp high
/grc:review-ssp nist moderate
/grc:review-ssp fedramp moderate
```

## Behavior

When invoked:

1. **Display the Data Sensitivity Notice** at the top of every response (see SKILL.md Data Handling section).

2. **Read the appropriate reference files**:
   - `skills/grc-knowledge/audits/document-section-requirements.md` for SSP section requirements
   - Framework file from `skills/grc-knowledge/frameworks/` for baseline-specific requirements
   - `skills/grc-knowledge/audits/narrative-quality-criteria.md` if reviewing narrative sections

3. **Determine what the user provided**:
   - **Table of contents / section headers**: Validate against required SSP sections
   - **Specific section content**: Review that section for completeness
   - **Full or partial SSP content**: Assess both structure and content

4. **For TOC / structural review**, check against all required SSP sections:

   **a. Section Checklist**
   For each required SSP section (per FedRAMP template):
   - **Present**: Section exists in the TOC/headers
   - **Missing**: Section not found — flag criticality level

   **b. Critical Sections**
   Flag these as critical if missing — each would be a finding:
   - System categorization (FIPS 199)
   - System description and architecture
   - Authorization boundary diagram
   - Network architecture diagram
   - Data flow diagrams
   - Ports, protocols, and services table
   - Control implementation narratives
   - System interconnections
   - Required appendices (CIS/CRM, contingency plan, IRP, CMP)

   **c. Appendix Completeness**
   Check for all FedRAMP-required appendices (A through L)

5. **For content review**, evaluate:
   - Completeness against section requirements
   - Control family coverage (are all baseline families addressed?)
   - Responsibility designations present and consistent
   - ODP values filled in (not TBD)
   - Interconnection details for each external system
   - Diagram references (are diagrams mentioned/included?)

6. **Generate a control family coverage table** if enough content is provided:
   - For each of the 20 NIST control families
   - Count of controls expected at baseline
   - Count addressed in provided content
   - Coverage percentage

7. **CRITICAL**: Never evaluate whether the described system architecture or security controls are actually adequate. Only assess whether the SSP document is structurally complete and covers required elements. Feedback is structural: "Section 6 is missing the authorization boundary diagram" not "your authorization boundary appears too broad."

8. **If no SSP content is provided**, ask the user to paste their TOC, section headers, or content.

## Output Format

```
> **Before sharing GRC artifacts**: Consider replacing real system names, IP addresses, personnel names, agency names, and CVE IDs with generic placeholders (e.g., "[Agency Name]", "[System Name]", "10.x.x.x"). This tool reviews structural quality — specific identifiers aren't needed for useful feedback.

## SSP Structure Review: [Framework] [Baseline]

---

### Section Checklist

| Section | Required | Status | Criticality |
|---------|----------|--------|-------------|
| 1. System Name/Title | Yes | ✅ / ❌ | Critical |
| 2. System Categorization | Yes | ✅ / ❌ | Critical |
| 3. System Owner | Yes | ✅ / ❌ | Critical |
| 4. Key Personnel | Yes | ✅ / ❌ | Critical |
| 5. System Description | Yes | ✅ / ❌ | Critical |
| 6. Architecture | Yes | ✅ / ❌ | Critical |
| 7. Environment | Yes | ✅ / ❌ | High |
| 8. Interconnections | Yes | ✅ / ❌ | Critical |
| 9. Laws & Regulations | Yes | ✅ / ❌ | Medium |
| 10. Control Summary | Yes | ✅ / ❌ | Critical |
| 11. Control Narratives | Yes | ✅ / ❌ | Critical |

**Sections present**: [X] / 11
**Critical sections missing**: [List]

### Required Diagrams

| Diagram | Status | Notes |
|---------|--------|-------|
| Authorization Boundary | ✅ / ❌ | |
| Network Architecture | ✅ / ❌ | |
| Data Flow | ✅ / ❌ | |

### Appendix Checklist (FedRAMP)

| Appendix | Content | Status |
|----------|---------|--------|
| A | Security Controls Matrix | ✅ / ❌ |
| B | Related Documents | ✅ / ❌ |
| C | Acronyms | ✅ / ❌ |
| D | Rules of Behavior | ✅ / ❌ |
| E | Contingency Plan | ✅ / ❌ |
| F | Configuration Management Plan | ✅ / ❌ |
| G | Incident Response Plan | ✅ / ❌ |
| H | CIS/CRM | ✅ / ❌ |
| I | FIPS 199 | ✅ / ❌ |
| J | PTA/PIA | ✅ / ❌ |
| K | Laws & Regulations | ✅ / ❌ |
| L | Integrated Inventory | ✅ / ❌ |

**Appendices present**: [X] / 12

### Control Family Coverage (if content reviewed)

| Family | Expected | Addressed | Coverage |
|--------|----------|-----------|----------|
| AC | [X] | [Y] | [%] |
| AT | [X] | [Y] | [%] |
| ... | ... | ... | ... |

### Recommendations

1. **Critical**: [Missing critical section or element]
2. **High**: [Important missing element]
3. **Medium**: [Improvement suggestion]
```

## Notes

- SSP review is the broadest scope of all review commands — it may cover structure, content, or both.
- For very large SSPs, the user may paste sections incrementally. Each invocation should review what's provided.
- The section checklist is based on the FedRAMP SSP template. For NIST/FISMA without FedRAMP, some appendices may not be required.
- Always mention that diagrams should be current (within the last year) and match the actual system architecture.
