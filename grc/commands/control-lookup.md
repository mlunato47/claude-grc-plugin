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

2. **For NIST or FedRAMP lookups, read the OSCAL family JSON first** for authoritative control data:
   - Determine the family ID from the control ID (e.g., `AC-2` → family `ac`, `IA-5(1)` → family `ia`)
   - For `nist`: read `skills/grc-knowledge/oscal/nist-800-53-rev5/{family}.json`
   - For `fedramp`: read `skills/grc-knowledge/oscal/fedramp-moderate-rev5/{family}.json`
   - **IMPORTANT: Use the Read tool to read the file directly. Do NOT use Bash, Python, jq, or any other scripting tool to extract data from OSCAL files.** The JSON is structured and you can find the target control by scanning for its `"id"` field. For large family files, you may read the file in chunks using offset/limit parameters to locate the control.
   - **ID normalization**: OSCAL uses lowercase with dots for enhancements — `AC-2` → `ac-2`, `AC-2(1)` → `ac-2.1`
   - **Extract from OSCAL** (jq paths shown for reference — extract visually from the JSON, do not run jq):
     - Control statement: `.controls[] | select(.id == "ac-2") | .parts[] | select(.name == "statement")`
     - Parameters: `.controls[].params[]` — look for `id`, `label`, `guidelines`, `select`/`choice` constraints. FedRAMP files include `.constraints[].description` with required values (e.g., "at least every 3 years")
     - Guidance: `.parts[] | select(.name == "guidance")`
     - Assessment objectives: `.parts[] | select(.name == "assessment-objective")` — nested tree of testable objectives with `.prose` for each leaf
     - Assessment methods: `.parts[] | select(.name == "assessment-method")` — three methods per control:
       - EXAMINE (`.props[] | select(.name == "method") | .value == "EXAMINE"`): lists documents/artifacts an assessor reviews
       - INTERVIEW: lists roles an assessor interviews
       - TEST: lists processes/mechanisms an assessor tests
       - Each method's objects are in `.parts[] | select(.name == "assessment-objects") | .prose`
     - Enhancements: `.controls[].controls[]` (nested under parent)
     - Related controls: `.links[] | select(.rel == "related")`
   - Then read the markdown framework file from `skills/grc-knowledge/frameworks/` for cross-framework mapping, audit context, and narrative guidance

3. **For all other frameworks**, read the appropriate framework reference file from `skills/grc-knowledge/frameworks/`

4. **If a control ID is provided**, locate the specific control in the OSCAL JSON by matching `.controls[] | select(.id == "{control-id}")` and return ALL of the following sections in this exact order:
   - Control ID and full title
   - Framework and version
   - Description — from `.parts[] | select(.name == "statement")`
   - Baseline assignment (if applicable — Low/Moderate/High for NIST/FedRAMP, IG level for CIS, CMMC level)
   - FedRAMP parameter values (if FedRAMP and parameters exist)
   - **Assessment Objectives** — **MANDATORY for NIST/FedRAMP**. Find the control's `.parts[] | select(.name == "assessment-objective")` and recursively walk the nested `.parts[]` tree. For each leaf node (a part that has `.prose` but no child `.parts[]`), output its label from `.props[] | select(.name == "label") | .value` and its `.prose`. Output ALL leaf objectives — do not summarize, truncate, or skip any. This MUST be its own separate section in the output.
   - **Assessment Methods** — **MANDATORY for NIST/FedRAMP**. Find the control's `.parts[] | select(.name == "assessment-method")`. There are typically three: EXAMINE, INTERVIEW, and TEST (identified by `.props[] | select(.name == "method") | .value`). For each method, extract `.parts[] | select(.name == "assessment-objects") | .prose` and list each item. This MUST be its own separate section in the output with three subsections.
   - Expected evidence/artifacts — your own practical guidance beyond the raw OSCAL data (tips, common gaps, preparation advice)
   - Related controls within the same framework
   - Cross-framework equivalents (reference the appropriate mapping file)

5. **If a keyword is provided**, search for matching controls and return:
   - A table of matching controls with ID, title, and brief description
   - Organized by relevance
   - Limit to top 10-15 most relevant matches
   - Offer to dive deeper into any specific control

6. **If no arguments provided**, ask the user which framework and control/keyword to look up.

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

### Assessment Objectives (NIST/FedRAMP only)
List every leaf objective from the OSCAL assessment-objective tree as a separate item:
- AC-02a.[01]: an access control policy is developed and documented
- AC-02a.[02]: the access control policy is disseminated to [personnel or roles]
- AC-02a.[03]: ...
- ...
(Show ALL leaf objectives — do not summarize or truncate)

### Assessment Methods (NIST/FedRAMP only)
Present each method type as a separate list. Pull directly from OSCAL assessment-method parts:

**Examine**:
- [Document/artifact 1 from OSCAL EXAMINE assessment-objects]
- [Document/artifact 2]
- ...

**Interview**:
- [Role 1 from OSCAL INTERVIEW assessment-objects]
- [Role 2]
- ...

**Test**:
- [Process/mechanism 1 from OSCAL TEST assessment-objects]
- [Process/mechanism 2]
- ...

### Expected Evidence
Practical evidence guidance beyond the raw OSCAL methods — tips, common gaps, preparation advice:
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
