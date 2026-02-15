# /grc:poam-help

POA&M (Plan of Action and Milestones) management help and templates.

## Usage

```
/grc:poam-help [action]
```

## Arguments

- **action**: The POA&M action to get help with. Accepts:
  - `create` — Create a new POA&M entry from a finding
  - `update` — Update an existing POA&M entry (milestones, status)
  - `close` — Close/verify a completed POA&M entry
  - `template` — Show POA&M entry template with all required fields
  - `escalate` — Handle overdue or escalated POA&M items
  - `deviation` — Draft a deviation request (redirects to `/grc:deviation-request`)
  - `metrics` — POA&M metrics and reporting guidance

## Examples

```
/grc:poam-help create
/grc:poam-help update
/grc:poam-help close
/grc:poam-help template
/grc:poam-help escalate
/grc:poam-help metrics
```

## Behavior

When invoked:

1. **Identify the action** from the argument.

2. **Read the POA&M management reference** from `conmon/poam-management.md`.

3. **Present action-specific guidance**:

### For `create`:
- Walk through each required field
- Help determine severity based on finding source
- Calculate remediation deadline based on severity (FedRAMP timelines)
- Suggest appropriate milestones
- Show example entry

### For `update`:
- Guidance on milestone updates
- Status transition rules (Open → In Progress → Completed → Closed)
- What constitutes meaningful progress
- Monthly update requirements

### For `close`:
- Verification requirements (re-scan, re-test)
- Evidence needed for closure
- Who approves closure
- Close vs Risk Accepted vs False Positive

### For `template`:
- Full POA&M entry template with all required fields
- Field descriptions and valid values
- FedRAMP-specific fields
- Example completed entry

### For `escalate`:
- When to escalate (approaching deadline, blocked, vendor dependency)
- Escalation path (ISSO → ISSM → CISO → AO)
- Deviation request triggers
- Impact of overdue items on authorization

### For `metrics`:
- Key POA&M metrics: total open, by severity, overdue count, average age, closure rate, reopened rate
- Monthly reporting format
- Trend analysis guidance
- Benchmarks for healthy POA&M posture

4. **If no action provided**, show available actions and a brief POA&M overview.

## Output Format

Varies by action. Always include:
- Step-by-step instructions
- Required fields/evidence
- Framework-specific requirements (especially FedRAMP timelines)
- Examples where helpful
