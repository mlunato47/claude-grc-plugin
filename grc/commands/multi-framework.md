---
description: "Analyze overlap and gaps across multiple compliance frameworks"
---

# /grc:multi-framework

Analyze overlap and gaps across multiple compliance frameworks to identify shared coverage and incremental work.

## Usage

```
/grc:multi-framework [frameworks] [baseline?]
```

## Arguments

- **frameworks**: Two or more frameworks, comma-separated. Accepts: `fedramp`, `nist`, `soc2`, `iso27001`, `pci`, `hipaa`, `cmmc`, `cis`, `cobit`, `ccm`
- **baseline** (optional): For NIST-based frameworks: `low`, `moderate`, `high`. Defaults to `moderate`.

## Examples

```
/grc:multi-framework fedramp,soc2
/grc:multi-framework fedramp,soc2,pci moderate
/grc:multi-framework fedramp,iso27001
/grc:multi-framework soc2,iso27001,pci
/grc:multi-framework fedramp,soc2,iso27001,pci high
/grc:multi-framework cmmc,fedramp
```

## Behavior

When invoked:

1. **No redaction reminder needed** — this is a pure reference/analysis command using framework knowledge only. No user content is processed.

2. **Read the appropriate reference files**:
   - Framework files for each specified framework from `skills/grc-knowledge/frameworks/`
   - Mapping files from `skills/grc-knowledge/mappings/` for each framework pair (chaining through NIST)
   - `skills/grc-knowledge/mappings/cross-framework-matrix.md` for high-level family mapping

3. **Generate a multi-framework analysis**:

   **a. Coverage Overlap Matrix**
   For each major control domain/family, show which frameworks cover it:
   - Full coverage: the framework explicitly addresses this domain
   - Partial coverage: some aspects addressed but not all
   - Gap: the framework doesn't address this domain

   **b. Shared Requirements**
   Activities and controls that satisfy multiple frameworks simultaneously:
   - Access control reviews → FedRAMP AC-2, SOC 2 CC6.1, ISO A.5.15, PCI 8.6
   - Vulnerability scanning → FedRAMP RA-5, SOC 2 CC7.1, ISO A.8.8, PCI 11.3
   - Security training → FedRAMP AT-2, SOC 2 CC1.4, ISO 7.2, PCI 12.6
   - Incident response → FedRAMP IR-4, SOC 2 CC7.3, ISO A.5.24, PCI 12.10

   **c. Incremental Work**
   When adding each new framework, what's net-new:
   - Start from the framework with the broadest coverage
   - For each additional framework, list only the unique requirements
   - Prioritize by effort and impact

   **d. Compliance Activity Harmonization**
   Recurring activities that can serve multiple frameworks:
   - Which scans satisfy multiple requirements
   - Which reviews cover multiple framework needs
   - Where the strictest frequency satisfies all
   - Which evidence artifacts serve multiple audits

   **e. Framework-Specific Unique Requirements**
   Controls or requirements unique to each framework that don't map to others:
   - FedRAMP: FedRAMP-specific parameters, ConMon deliverables, 3PAO assessment
   - SOC 2: Trust Service Criteria not covered by NIST, SOC 2 report format
   - PCI DSS: Cardholder-specific controls, network segmentation, ASV scanning
   - ISO 27001: ISMS process requirements (Clauses 4-10), management review
   - HIPAA: PHI-specific requirements, breach notification rules

4. **Provide a recommended implementation approach**:
   - Which framework to implement first (usually the broadest — NIST/FedRAMP)
   - How to layer additional frameworks efficiently
   - Where to create unified policies vs. framework-specific addenda

5. **If only one framework is specified**, ask the user which additional framework(s) to compare against.

## Output Format

```
## Multi-Framework Analysis: [Framework 1] + [Framework 2] [+ ...]

---

### Coverage Matrix

| Domain | [Framework 1] | [Framework 2] | [Framework 3] | Overlap |
|--------|--------------|--------------|--------------|---------|
| Access Control | [Control IDs] | [Control IDs] | [Control IDs] | Full |
| Audit & Logging | [Control IDs] | [Control IDs] | [Control IDs] | Full |
| Change Management | [Control IDs] | [Control IDs] | — | Partial |
| Physical Security | [Control IDs] | — | — | [F1] only |
| ... | ... | ... | ... | ... |

### Shared Requirements (Do Once, Satisfy Many)

| Activity | [F1] Control | [F2] Control | [F3] Control | Strictest Frequency |
|----------|-------------|-------------|-------------|-------------------|
| Access reviews | AC-2 | CC6.1 | 8.6 | Monthly (FedRAMP) |
| Vuln scanning | RA-5 | CC7.1 | 11.3 | Monthly (FedRAMP) |
| Security training | AT-2 | CC1.4 | 12.6 | Annual |
| ... | ... | ... | ... | ... |

### Incremental Work by Framework

#### Starting with [Broadest Framework]
**Baseline effort**: [X] controls/requirements

#### Adding [Framework 2]
**Already covered**: [X]% by [Framework 1]
**Net-new requirements**:
| Requirement | Category | Effort |
|-------------|----------|--------|
| [Requirement] | [Domain] | [Low/Medium/High] |

#### Adding [Framework 3]
**Already covered**: [X]% by [F1] + [F2]
**Net-new requirements**:
| Requirement | Category | Effort |
|-------------|----------|--------|

### Unique to Each Framework

#### [Framework 1] — Unique Requirements
- [Requirement not covered by others]

#### [Framework 2] — Unique Requirements
- [Requirement not covered by others]

### Recommended Approach

1. **Implement first**: [Framework] — broadest coverage, [X]% overlap with others
2. **Add second**: [Framework] — [X]% already covered, adds [key capability]
3. **Add third**: [Framework] — [X]% already covered, primarily adds [specific area]

### Unified Activities
[List of activities that can be done once to satisfy all frameworks]
```

## Notes

- NIST 800-53 / FedRAMP is almost always the broadest framework and the best starting point.
- Cross-framework mapping loses some fidelity — a "mapped" control covers the intent but may not satisfy the specific language.
- For audit purposes, each framework's audit is independent — having "equivalent" controls doesn't mean you skip evidence for a specific framework.
- This command pairs with `/grc:compliance-calendar` to build a unified calendar across frameworks.
