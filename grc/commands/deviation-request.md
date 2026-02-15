# /grc:deviation-request

Draft deviation requests, risk acceptances, or false positive justifications.

## Usage

```
/grc:deviation-request [framework] [control-id] [reason-type]
```

## Arguments

- **framework**: The compliance framework
- **control-id**: The specific control ID requiring deviation
- **reason-type**: The type of deviation. Accepts:
  - `operational` — Operational requirement prevents full implementation
  - `false-positive` — Scanner finding is a false positive
  - `risk-adjustment` — Risk is mitigated by compensating controls
  - `vendor-dependency` — Remediation depends on vendor action
  - `technology-constraint` — Technical limitation prevents implementation
  - `temporary` — Temporary deviation with planned remediation

## Examples

```
/grc:deviation-request fedramp si-2 vendor-dependency
/grc:deviation-request fedramp ac-7 operational
/grc:deviation-request pci 6.3.3 false-positive
/grc:deviation-request nist sc-28 technology-constraint
/grc:deviation-request fedramp ra-5 temporary
```

## Behavior

When invoked:

1. **Identify the framework, control, and reason type** from arguments.

2. **Read the relevant framework reference** and **POA&M management reference** (`conmon/poam-management.md`).

3. **Draft a deviation request** that includes all required elements:

   a. **Finding identification**:
      - POA&M ID / Weakness ID
      - Control ID and title
      - Finding source (scan tool, assessment, etc.)
      - Original severity and risk rating

   b. **Deviation justification** (varies by reason type):
      - **Operational**: Why the control cannot be fully implemented, what business process depends on the exception, impact of full implementation
      - **False positive**: Technical evidence that the finding is not a true vulnerability, scanner configuration details, manual verification results
      - **Risk adjustment**: Compensating controls in place, residual risk calculation, why compensating controls adequately mitigate the risk
      - **Vendor dependency**: Vendor ticket/case number, vendor acknowledgment, expected vendor timeline, interim mitigations
      - **Technology constraint**: Technical limitation details, alternatives evaluated, compensating controls
      - **Temporary**: Planned remediation date, milestones, interim mitigations

   c. **Risk assessment**:
      - Adjusted risk rating with justification
      - Impact if deviation is not approved
      - Compensating controls (if any)
      - Residual risk statement

   d. **Approval chain**:
      - ISSO recommendation
      - ISSM review
      - AO approval (for FedRAMP)
      - Expiration date for deviation

4. **If no arguments provided**, ask for framework, control ID, and reason type.

## Output Format

```
## Deviation Request

### Finding Information
- **POA&M ID**: [To be assigned]
- **Control**: [Framework] [Control-ID] — [Title]
- **Source**: [Scan/Assessment/Incident]
- **Original Severity**: [Critical/High/Moderate/Low]
- **Detection Date**: [Date]

### Deviation Type
[Operational Requirement / False Positive / Risk Adjustment / Vendor Dependency / Technology Constraint / Temporary]

### Justification
[Detailed justification based on deviation type]

### Compensating Controls
| Control | Description | Risk Reduction |
|---------|-------------|---------------|

### Risk Assessment
- **Original Risk**: [Rating]
- **Adjusted Risk**: [Rating]
- **Residual Risk**: [Statement]
- **Risk Acceptance Rationale**: [Why this residual risk is acceptable]

### Remediation Plan (if temporary/vendor)
| Milestone | Target Date | Owner |
|-----------|-------------|-------|

### Approval
- **Requested by**: [Name, Role]
- **ISSO Recommendation**: [Approve/Deny]
- **ISSM Review**: [Approve/Deny]
- **AO Decision**: [Approve/Deny]
- **Expiration Date**: [Date — typically 1 year max]

### Supporting Evidence
- [Attachment 1: Description]
- [Attachment 2: Description]
```

## Notes

- FedRAMP deviation requests have specific submission requirements through the PMO.
- False positive deviation requests require technical evidence (not just an assertion).
- Operational requirement deviations should be rare and well-justified — auditors scrutinize these heavily.
- All deviations should have an expiration date and be reviewed at least annually.
- Compensating controls must demonstrably reduce the risk to an acceptable level.
