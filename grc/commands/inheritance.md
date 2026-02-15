# /grc:inheritance

Model control inheritance based on service model and provider stack.

## Usage

```
/grc:inheritance [framework?] [service-model] [baseline?]
```

The user can optionally describe their provider stack or specific controls to analyze.

## Arguments

- **framework** (optional): `fedramp`, `nist`, `fisma`. Defaults to `fedramp`.
- **service-model**: `iaas`, `paas`, `saas`, or a description like "SaaS on AWS" or "PaaS on Azure GovCloud"
- **baseline** (optional): `low`, `moderate`, `high`. Defaults to `moderate`.

## Examples

```
/grc:inheritance fedramp iaas moderate
/grc:inheritance fedramp saas
/grc:inheritance paas on AWS GovCloud
/grc:inheritance fedramp saas high
/grc:inheritance We run a SaaS application on AWS GovCloud (IaaS) using RDS, ECS, and S3
```

## Behavior

When invoked:

1. **Display the Data Sensitivity Notice** at the top of every response if the user describes their specific stack (see SKILL.md Data Handling section). If the user only specifies a generic service model (e.g., "iaas"), the notice is not needed.

2. **Read the appropriate reference files**:
   - `skills/grc-knowledge/audits/control-inheritance.md` for inheritance patterns by service model
   - Framework file from `skills/grc-knowledge/frameworks/` for baseline control list
   - `skills/grc-knowledge/audits/document-section-requirements.md` for CRM structure guidance

3. **Generate an inheritance model** based on the service model:

   **a. Control Family Inheritance Table**
   For each of the 20 NIST control families at the specified baseline:
   - Expected responsibility designation (Inherited, Shared, Customer, CSP)
   - Brief explanation of what's inherited vs. what the customer must implement
   - Key controls to pay attention to in each family

   **b. Detailed Shared Control Breakdown**
   For controls marked as Shared:
   - What the underlying provider typically handles
   - What the leveraging CSP or customer must handle
   - ODP responsibility (who defines parameter values)
   - Evidence responsibility (who produces evidence for audit)

   **c. Multi-Layer Inheritance Chain**
   If the user describes a stacked environment (e.g., "SaaS on PaaS on IaaS"):
   - Show the full inheritance chain per family
   - Identify which layer each control is implemented at
   - Flag any gaps in the chain

   **d. Common Inheritance Mistakes**
   For the specified service model, highlight the most common mistakes from the reference file.

4. **If specific controls are asked about**, provide deep-dive inheritance analysis for those controls:
   - What exactly is inherited and from whom
   - What the SSP narrative must say about the inheritance
   - What evidence the 3PAO will want
   - Common mistakes for that specific control

5. **CRITICAL**: Never evaluate whether the inheritance model is appropriate for security. Only provide the expected inheritance patterns and what the SSP must document. Feedback is informational: "for IaaS, PE controls are typically inherited — your SSP must name the provider and their authorization" not "inheriting PE from this provider is risky."

6. **If insufficient information is provided**, ask the user to describe their service model and provider stack.

## Output Format

```
> [Redaction reminder if user described specific stack details]

## Control Inheritance Model: [Service Model] on [Provider] — [Framework] [Baseline]

---

### Inheritance Summary

| Family | Designation | Notes |
|--------|-------------|-------|
| AC | Shared | [Brief — e.g., "Provider: network ACLs. You: user accounts, roles"] |
| AT | Customer | [Brief] |
| AU | Shared | [Brief] |
| ... | ... | ... |

**Distribution**:
- Inherited: [X] families
- Shared: [X] families
- Customer: [X] families

### Shared Controls — Detailed Split

#### [Family]: [Family Name]

| Control | Provider Does | You Do | ODP Owner | Evidence Owner |
|---------|-------------|--------|-----------|----------------|
| [Control-ID] | [Provider action] | [Your action] | [Who] | [Who] |

[Repeat for each family with Shared controls]

### Inheritance Chain
[If multi-layer stack]
```
[Your Application] — Customer-implemented
       ↓
[PaaS Layer] — First inheritance (name provider + authorization)
       ↓
[IaaS Layer] — Second inheritance (name provider + authorization)
       ↓
[Physical] — Third inheritance (data center operator)
```

### SSP Documentation Requirements

For each inherited or shared control, your SSP must:
1. Name the provider and their authorization status
2. Reference the provider's CRM/CIS
3. Describe specifically what you inherit (not just "inherited from CSP")
4. For shared controls: describe your specific responsibilities
5. State how you verified the inheritance (CRM review date)

### Common Mistakes for [Service Model]

| Mistake | Why It's a Problem | Fix |
|---------|-------------------|-----|
| [Mistake] | [Problem] | [Fix] |
```

## Notes

- Inheritance patterns are guidelines, not rules — the actual split depends on the specific provider and their CRM.
- Always recommend the user obtain and review their provider's actual CRM rather than relying on general patterns.
- For multi-CSP environments, each provider relationship needs its own inheritance documentation.
- This command pairs well with `/grc:review-crm` to validate the actual CRM against expected patterns.
