# Control Narrative Quality Criteria

Scoring rubric for evaluating control implementation narratives in SSPs and related documents. Applies across all NIST-based frameworks (FedRAMP, FISMA, CMMC) and adapts to commercial frameworks.

## The Five W's Checklist

Every control narrative must answer these five questions. Missing any one reduces the narrative's audit readiness.

### What — Control Objective

- [ ] States what security function is performed
- [ ] Describes the specific mechanism or process
- [ ] Addresses the control requirement (not just the title)
- [ ] Covers all parts of the control statement (a, b, c, etc.)
- [ ] References applicable enhancements

**Common deficiency**: Restating the control requirement instead of describing the actual implementation.

### Who — Responsible Parties

- [ ] Names specific roles (not individuals) responsible for the control
- [ ] Distinguishes between who implements vs. who oversees
- [ ] Identifies shared responsibilities (CSP, customer, third-party)
- [ ] Uses organizational role titles (ISSO, System Admin, Security Engineer)
- [ ] Specifies who authorizes exceptions

**Common deficiency**: Using vague actors ("the organization", "management", "personnel") without naming roles.

### How — Implementation Method

- [ ] Describes the technical or procedural mechanism
- [ ] Names specific tools, technologies, or platforms (or placeholders for them)
- [ ] Details configuration settings where applicable
- [ ] Explains the process flow from trigger to completion
- [ ] Addresses both automated and manual components

**Common deficiency**: Describing intent ("we ensure...") rather than mechanism ("the system enforces via...").

### When — Frequency and Timing

- [ ] States how often the control activity occurs
- [ ] Matches framework-required frequencies (e.g., FedRAMP parameters)
- [ ] Distinguishes between continuous, periodic, and event-driven activities
- [ ] Specifies review/audit cycles
- [ ] Addresses timeliness of response (for incident/event-based controls)

**Common deficiency**: Omitting frequency entirely, or using "periodically" without specifying the period.

### Where — Scope and Boundary

- [ ] Identifies which systems, components, or environments are covered
- [ ] References the authorization boundary
- [ ] Specifies applicability (all users, privileged users, external interfaces, etc.)
- [ ] Addresses remote access and alternative work locations if relevant
- [ ] Notes any exclusions or scoping decisions

**Common deficiency**: Assuming scope is obvious; not specifying which systems or environments.

## Organization-Defined Parameter (ODP) Completeness

ODPs (also called "assignment" or "selection" operations in NIST 800-53) require the organization to fill in specific values.

### Parameter Check Criteria

- [ ] All required ODPs have explicit values (not blank or TBD)
- [ ] Values match framework requirements (FedRAMP-defined values where mandated)
- [ ] Values are specific and measurable (e.g., "90 days" not "regularly")
- [ ] Selection operations choose from allowed options
- [ ] Assignment operations provide concrete values appropriate to the system

### Common ODP Deficiencies by Family

| Family | Common Missing/Vague Parameters |
|--------|-------------------------------|
| AC | Account inactivity period, unsuccessful login attempts, lockout duration, session timeout |
| AU | Audit events to be logged, audit record retention period, audit review frequency |
| CM | Configuration change approval roles, software restriction list, baseline update frequency |
| CP | Recovery time objective (RTO), recovery point objective (RPO), backup frequency |
| IA | Authenticator types, credential lifetime, complexity requirements |
| IR | Incident reporting timeframe, incident categories, response time targets |
| RA | Vulnerability scanning frequency, remediation timelines by severity |
| SC | Cryptographic algorithms, key sizes, certificate validity periods |
| SI | Flaw remediation timelines, monitoring alert thresholds, signature update frequency |

## Enhancement Coverage

For each control at the applicable baseline, all required enhancements must be addressed.

### Enhancement Check Criteria

- [ ] All baseline-applicable enhancements are addressed (not just the base control)
- [ ] Each enhancement has its own narrative or is clearly integrated into the base narrative
- [ ] Enhancement-specific ODPs are filled in
- [ ] Withdrawn enhancements are noted as such (not silently skipped)
- [ ] Additional (above-baseline) enhancements are identified if implemented

### Common Enhancement Gaps

| Control | Often-Missed Enhancements (Moderate) |
|---------|--------------------------------------|
| AC-2 | (3) Disable accounts, (4) Automated audit actions, (12) Account monitoring, (13) Disable accounts for high risk |
| AC-6 | (1) Authorize access, (2) Non-privileged access for non-security functions, (5) Privileged accounts, (9) Log privileged functions, (10) Prohibit non-privileged users from executing privileged functions |
| AU-6 | (1) Automated process integration, (3) Correlate audit repositories |
| CM-6 | (1) Automated management/verification |
| IA-2 | (1) MFA to privileged, (2) MFA to non-privileged, (12) PIV acceptance |
| IA-5 | (1) Password-based authentication |
| SC-7 | (3) Access points, (4) External telecommunications, (5) Deny by default, (7) Split tunneling prevention, (8) Route to authenticated proxy |
| SI-4 | (2) Automated tools for real-time analysis, (4) Inbound/outbound traffic, (5) System-generated alerts |

## Language Quality Indicators

### Strong Narrative Indicators

- **Active voice**: "The system enforces..." not "Enforcement is performed..."
- **Present tense**: "The ISSO reviews..." not "The ISSO will review..." or "The ISSO should review..."
- **Specific mechanisms**: "AWS IAM policies restrict..." not "Access is restricted..."
- **Measurable frequencies**: "Every 30 days" not "periodically" or "regularly"
- **Role-based actors**: "The System Administrator configures..." not "The organization configures..."
- **Definitive language**: "shall", "must", "is configured to" — not "should", "may", "plans to"

### Weak Narrative Red Flags

| Red Flag | Example | Problem |
|----------|---------|---------|
| Aspirational language | "The organization plans to implement..." | Describes future intent, not current state |
| Policy echo | "Access is managed per AC-2" | Restates requirement without describing implementation |
| Vague mechanisms | "Appropriate controls are in place" | No specifics on what controls or how they work |
| Passive responsibility | "Reviews are conducted" | Who conducts them? |
| Undefined frequency | "Regular reviews are performed" | How often? |
| Conditional language | "If necessary, the system may..." | Auditor needs to know what *is* done, not what *might* be |
| Inherited-only claims | "This is inherited from the CSP" | Must explain what the CSP does and how you verified |
| TBD/placeholder values | "The organization defines [TBD]" | Incomplete parameter assignment |
| Wrong scope | Describes corporate policy but not system implementation | SSP describes the *system*, not the *organization* generically |

## Maturity Scoring Scale (0–5)

### Level 0 — Absent
- No narrative exists for the control
- Control is marked as N/A without justification
- **Auditor impact**: Finding — control not implemented

### Level 1 — Stub
- One or two sentences that merely restate the control requirement
- No implementation details, no roles, no frequencies
- Contains mostly placeholder or TBD values
- **Auditor impact**: Finding — implementation not described

### Level 2 — Vague
- Attempts to describe implementation but lacks specifics
- Missing 2+ of the Five W's
- Uses aspirational or conditional language
- ODPs partially filled in
- **Auditor impact**: Likely finding — insufficient detail for assessment

### Level 3 — Adequate
- Addresses all Five W's at minimum
- ODPs are filled in with specific values
- Correct framework-required parameter values
- Some language quality issues (passive voice, minor vagueness)
- Baseline enhancements addressed
- **Auditor impact**: Passes assessment with minor observations

### Level 4 — Strong
- All Five W's addressed with specifics
- All ODPs complete with correct values
- Active voice, present tense, specific mechanisms
- All baseline enhancements addressed individually
- Clear responsibility delineation (CSP/Customer/Shared)
- References supporting artifacts (policy documents, configuration guides)
- **Auditor impact**: Clean pass

### Level 5 — Exemplary
- Everything in Level 4, plus:
- Addresses above-baseline enhancements where implemented
- Includes evidence references (ticket systems, monitoring dashboards)
- Describes exception handling and escalation
- Notes compensating controls where applicable
- Could serve as a template for other organizations
- **Auditor impact**: Clean pass; may be cited as best practice

## Common Deficiencies by Control Family

### AC — Access Control
- Missing account lifecycle details (creation → review → modification → disabling → deletion)
- Vague "least privilege" claims without specifying role-based access model
- No emergency access/break-glass procedures described
- Remote access narrative ignores VPN configuration specifics

### AU — Audit and Accountability
- Not specifying which events are audited (just says "security-relevant events")
- Missing audit review frequency or reviewer role
- No mention of audit log protection/integrity mechanisms
- Retention period stated but not how/where logs are stored

### CA — Assessment, Authorization, and Monitoring
- POA&M management described generically without lifecycle details
- Interconnections (CA-3) missing partner system specifics
- Assessment frequency not aligned with FedRAMP annual requirement

### CM — Configuration Management
- Baseline configurations referenced but not described
- Change management process lacks approval chain details
- Software inventory claimed but update frequency not stated
- Least functionality (CM-7) lists disabled services without specificity

### CP — Contingency Planning
- RTO/RPO values missing or stated as "TBD"
- Backup frequency and retention not specified
- Testing results not referenced (CP-4)
- Alternate site arrangements vague

### IA — Identification and Authentication
- MFA described generically without specifying authenticator types
- Password complexity stated but doesn't match FedRAMP parameters
- Service account/device authentication not addressed
- Credential management lifecycle incomplete

### IR — Incident Response
- Reporting timelines don't match CISA requirements
- Incident categories and severity definitions missing
- Lessons learned process not described
- External reporting requirements (FedRAMP PMO, agency) omitted

### PE — Physical and Environmental Protection
- For cloud: inheritance claim without CSP reference
- Visitor management described at policy level, not implementation
- Environmental controls (fire, HVAC, water) generically stated
- Physical access authorization list management not described

### SC — System and Communications Protection
- Encryption described without algorithm/key size specifics
- Boundary protection doesn't reference network architecture
- Session management controls vague on timeout values
- DNS/DNSSEC, certificate management often missing

### SI — System and Information Integrity
- Flaw remediation timelines not aligned with POA&M SLAs
- Monitoring tools named but alerting thresholds not described
- Anti-malware update frequency not specified
- Information handling/integrity checks not addressed
