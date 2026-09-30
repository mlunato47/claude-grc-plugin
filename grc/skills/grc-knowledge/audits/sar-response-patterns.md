# SAR Finding Response Patterns

Templates and guidance for responding to Security Assessment Report (SAR) findings from 3PAO assessments (CR26 term: FedRAMP Recognized independent assessor), internal audits, and other security evaluations. Severity SLAs cited below are legacy FedRAMP Rev5 values (in force until CR26 becomes mandatory Jan 1, 2027); see the CR26 note under "Response Patterns by Risk Rating".

## SAR Finding Structure

A 3PAO SAR finding typically contains:

| Field | Description |
|-------|-------------|
| Finding ID | Unique identifier (e.g., SAR-2024-001) |
| Control ID | NIST 800-53 control that has a deficiency |
| Risk Rating | Critical, High, Moderate, Low |
| Finding Type | Operational, Documentation, Technical |
| Description | What the assessor found deficient |
| Recommendation | Assessor's suggested remediation |
| Evidence Reviewed | What the assessor examined |
| Assessment Method | Test, Interview, Examine (from 800-53A) |

## Response Structure

Every SAR finding response should address these elements:

### 1. Acknowledgment
- Confirm understanding of the finding
- Agree, partially agree, or disagree (with justification)
- If disagreeing: provide evidence that contradicts the finding

### 2. Root Cause Analysis
- Why the deficiency exists (not just what it is)
- Contributing factors (resource, process, technology, awareness)
- Whether this is an isolated issue or systemic

### 3. Remediation Plan
- Specific corrective actions (not "we will fix it")
- Responsible party for each action (role, not individual name)
- Target completion dates per action
- Resources required
- Dependencies or blockers

### 4. Interim Mitigations
- What's in place right now to reduce risk while full remediation is underway
- Compensating controls (if any)
- Monitoring enhancements during remediation period

### 5. Verification Approach
- How the CSP will verify remediation is effective
- Evidence that will demonstrate closure
- Whether re-assessment by 3PAO is needed

### 6. POA&M Entry
- Maps directly to a POA&M entry (or references existing one)
- Milestones align with remediation plan
- Scheduled completion within severity SLA

## Response Templates by Finding Type

### Operational Finding
When a control is implemented but operating ineffectively (e.g., reviews not happening on schedule, scans not meeting frequency requirements).

```
**Response to [Finding ID]: [Control ID] — [Brief Title]**

**Acknowledgment**: [CSP Name] acknowledges this finding. [Agree/Partially agree with rationale].

**Root Cause**: [Describe why the operational gap exists — e.g., "The quarterly access review process was implemented in [date] but the review scheduled for Q3 was delayed due to [reason]. The review cadence was not tracked in the centralized compliance calendar."]

**Remediation Plan**:
1. [Action 1] — [Role] — Target: [Date]
2. [Action 2] — [Role] — Target: [Date]
3. [Action 3] — [Role] — Target: [Date]

**Interim Mitigation**: [What's in place now — e.g., "An ad-hoc review was conducted on [date] covering the missed period. Results documented in [evidence reference]."]

**Verification**: [How remediation will be confirmed — e.g., "Compliance calendar alerts configured. Next scheduled review will serve as verification. Evidence: calendar configuration + completed review artifact."]

**POA&M Reference**: [POA&M-ID]
```

### Documentation Finding
When control implementation exists but SSP narrative, policy, or procedure documentation is missing or deficient.

```
**Response to [Finding ID]: [Control ID] — [Brief Title]**

**Acknowledgment**: [CSP Name] acknowledges this documentation deficiency.

**Root Cause**: [Describe why documentation is deficient — e.g., "The SSP narrative for [Control-ID] was drafted during the initial authorization and was not updated to reflect the migration from [old tool] to [new tool] in [date]."]

**Remediation Plan**:
1. Update SSP Section [X] narrative for [Control-ID] to reflect current implementation — [Role] — Target: [Date]
2. Review all [Family] narratives for similar staleness — [Role] — Target: [Date]
3. Implement SSP review trigger in change management process — [Role] — Target: [Date]

**Interim Mitigation**: [Description — e.g., "The control IS implemented as described in the updated draft narrative provided to the 3PAO on [date]. Only the SSP documentation was stale."]

**Verification**: Updated SSP section submitted for review. Evidence: SSP revision history showing update.

**POA&M Reference**: [POA&M-ID]
```

### Technical Finding
When a control is not technically implemented as required (e.g., phishing-resistant MFA not enforced, encryption not using a FIPS 140-3 module with active CMVP validation — 140-2 certificates have been Historical since Sept 22, 2026 — configurations not matching baselines).

```
**Response to [Finding ID]: [Control ID] — [Brief Title]**

**Acknowledgment**: [CSP Name] acknowledges this technical deficiency.

**Root Cause**: [Describe why the technical gap exists — e.g., "The device lock (AC-11) inactivity timeout was configured to 30 minutes, which exceeds the legacy FedRAMP Rev5 value of 15 minutes (in force until CR26 becomes mandatory Jan 1, 2027; CR26 assigns no FedRAMP value). The configuration was set during initial deployment and was not updated when FedRAMP parameter guidance changed." Note: AC-12 session termination has no FedRAMP-assigned value in either the legacy baseline or CR26.]

**Remediation Plan**:
1. [Technical action] — [Role] — Target: [Date]
2. Update configuration baseline documentation — [Role] — Target: [Date]
3. Add configuration check to automated compliance scanning — [Role] — Target: [Date]

**Interim Mitigation**: [Compensating control — e.g., "Enhanced session monitoring is in place. All active sessions are logged and reviewed daily. The current 30-minute timeout still provides meaningful protection against session hijacking."]

**Verification**: [Evidence — e.g., "Screenshot of updated configuration. Automated scan results confirming compliant setting. Evidence provided to 3PAO for verification."]

**POA&M Reference**: [POA&M-ID]
```

## Response Patterns by Risk Rating

SLAs below are the Legacy FedRAMP Rev5 values (in force until CR26 becomes mandatory Jan 1, 2027): High 30 / Moderate 90 / Low 180 days from discovery; "Critical" is not a distinct FedRAMP category and is treated as High. **CR26 (VDR/VER, required Dec 7, 2026; grace to Mar 7, 2027):** deadlines derive from PAIN rating and reachability (e.g., Class D PAIN-5 internet-reachable 12 hours, ranges up to 192 days), KEVs per CISA due dates; anything not remediated within 192 days becomes an Accepted Vulnerability with written justification, listed in each quarterly OCR.

### Critical Findings (30-day SLA)
- Response must demonstrate urgency
- Interim mitigations are mandatory (not optional)
- Daily or weekly progress updates expected
- AO notification required immediately
- Consider whether system should operate during remediation

### High Findings (30-day SLA)
- Response should include phased remediation if complex
- Interim mitigations strongly recommended
- Weekly progress updates typical
- Remediation milestones should be granular

### Moderate Findings (90-day SLA)
- Response can include longer-term process improvements
- Milestones can be monthly
- May be batched with related findings for efficiency

### Low Findings (180-day SLA)
- Often documentation or minor configuration issues
- Can be addressed as part of regular maintenance cycles
- May be combined with annual SSP updates

## Disagreement Responses

When the CSP disagrees with a finding:

### False Positive Response
```
**Response to [Finding ID]: [Control ID]**

**Disagreement**: [CSP Name] respectfully disagrees with this finding. The identified item is a false positive based on the following evidence:

**Evidence**:
1. [Evidence item 1 — e.g., "The scan flagged OpenSSL 1.1.1 as vulnerable (CVE-XXXX-XXXXX). However, the installed version is 1.1.1w which includes the patch. Scanner signature was outdated."]
2. [Evidence item 2 — e.g., "Attached: vendor advisory confirming fix in version 1.1.1w"]

**Requested Action**: Mark as false positive in POA&M. Updated scan signatures will resolve future false positive detections.
```

### Risk Acceptance Response
```
**Response to [Finding ID]: [Control ID]**

**Acknowledgment**: [CSP Name] acknowledges this finding. We request risk acceptance based on the following justification:

**Business Justification**: [Why the current state is operationally necessary]

**Compensating Controls**:
1. [Compensating control 1]
2. [Compensating control 2]

**Residual Risk Assessment**: [Risk with compensating controls in place]

**Requested Action**: Deviation request [DR-ID] submitted. POA&M entry [POA&M-ID] reflects accepted risk status pending AO approval.
```

*Legacy Rev5 deviation-request model. Under CR26 the equivalent is an **Accepted Vulnerability** (FRD-ACV) with written justification, reported in each quarterly OCR with the VER-RPT-AVI fields (tracking ID, detection time/source, evaluation time, internet-reachable, likely-exploitable, PAIN rating, rationale); "Accepted Weakness" is not a CR26 term.*

## SAR Response Quality Checklist

| Criteria | Check |
|----------|-------|
| Every finding has a response | ☐ |
| Root cause identified (not just symptom) | ☐ |
| Remediation actions are specific and actionable | ☐ |
| Target dates are within SLA | ☐ |
| Responsible roles are named | ☐ |
| Interim mitigations described for High/Critical | ☐ |
| Verification approach defined | ☐ |
| POA&M entry created/referenced | ☐ |
| Evidence commitments are realistic | ☐ |
| Disagreements supported with evidence | ☐ |
| No "we will look into this" without action plan | ☐ |
| No commitments that can't be met within SLA | ☐ |

## Common Response Anti-Patterns

| Anti-Pattern | Example | Problem |
|-------------|---------|---------|
| Vague commitment | "We will address this finding" | No specific action, timeline, or owner |
| Blame shifting | "The 3PAO misunderstood our implementation" | Without evidence, appears defensive |
| Over-promising | "All 47 findings will be resolved in 30 days" | Unrealistic; sets up for SLA failure |
| Missing interim mitigation | Critical finding with 90-day remediation, no interim controls | Unmitigated critical risk for 90 days |
| Copy-paste responses | Same response for different findings | Each finding has unique context |
| Ignoring the root cause | "We will update the configuration" | Without addressing why it was wrong, it will recur |
| Future-tense hedging | "We plan to evaluate options for..." | Doesn't commit to specific remediation |
| Missing POA&M linkage | Response doesn't reference a POA&M entry | Finding isn't tracked for closure |
