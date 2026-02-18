---
description: "Look up controls by framework and ID or keyword"
---

# /grc:control-lookup

Look up controls by framework and ID or keyword.

## Usage

```
/grc:control-lookup [framework] [id-or-keyword]
```

## Arguments

- **framework**: The compliance framework to search. Accepts: `nist`, `fedramp`, `fisma`, `cmmc`, `soc2`, `iso27001`, `pci`, `hipaa`, `cis`, `cobit`, `ccm`, `gdpr`
- **id-or-keyword**: A control ID (e.g., `ac-2`, `CC6.1`, `A.8.1`) or a keyword (e.g., `multi-factor`, `encryption`, `logging`)

## Examples

```
/grc:control-lookup nist ac-2
/grc:control-lookup soc2 CC6.1
/grc:control-lookup pci 8.3
/grc:control-lookup nist encryption
/grc:control-lookup iso27001 A.8.5
/grc:control-lookup cis 5.2
```

## Behavior

When invoked:

1. **Identify the framework** from the first argument. Normalize aliases:
   - `nist` / `800-53` → NIST 800-53 Rev 5
   - `fedramp` → FedRAMP (NIST 800-53 + FedRAMP parameters)
   - `cmmc` / `800-171` → CMMC 2.0 / NIST 800-171
   - `soc2` / `soc` → SOC 2 Trust Services Criteria
   - `iso` / `iso27001` / `27001` → ISO 27001:2022
   - `pci` / `pcidss` → PCI DSS v4.0.1
   - `hipaa` → HIPAA Security Rule
   - `cis` → CIS Controls v8.1
   - `cobit` → COBIT 2019
   - `ccm` / `csa` → CSA CCM v4
   - `gdpr` → GDPR

2. **Read the appropriate framework reference file** from `skills/grc-knowledge/frameworks/`

3. **If a control ID is provided**, locate the specific control and return:
   - Control ID and full title
   - Framework and version
   - Description of what the control requires
   - Baseline assignment (if applicable — Low/Moderate/High for NIST/FedRAMP, IG level for CIS, CMMC level)
   - FedRAMP parameter values (if FedRAMP and parameters exist)
   - Expected evidence/artifacts for audit
   - Related controls within the same framework
   - Cross-framework equivalents (reference the appropriate mapping file)

4. **If a keyword is provided**, search for matching controls and return:
   - A table of matching controls with ID, title, and brief description
   - Organized by relevance
   - Limit to top 10-15 most relevant matches
   - Offer to dive deeper into any specific control

5. **If no arguments provided**, ask the user which framework and control/keyword to look up.

## Output Format

### For specific control ID:
```
## [Framework] [Control-ID]: [Title]

**Framework**: [Name] [Version]
**Baseline**: [Low/Moderate/High or equivalent]
**Family/Category**: [Parent family or category]

### Description
[What the control requires]

### FedRAMP Parameters (if applicable)
[Organization-defined parameter values]

### Expected Evidence
- [Evidence item 1]
- [Evidence item 2]

### Related Controls
- [Related-ID]: [Brief description of relationship]

### Cross-Framework Equivalents
| Framework | Control(s) | Notes |
|-----------|-----------|-------|
```

### For keyword search:
```
## Controls matching "[keyword]" in [Framework]

| ID | Title | Baseline | Description |
|----|-------|----------|-------------|
```
