# Critical Path Rules: ATO Timeline Compression Engine

Reference for the ATO acceleration engine. Defines what blocks AO signature, how to order work, what to parallelize, and how to compress a standard 30-60 day ATO into 3-10 days for the right combination of platform, IL, and team size.

---

## The AO Signature Model

An AO signs an ATO when the risk of operating the system is documented, understood, and acceptable. The AO is not looking for perfection — they are looking for:

1. **I know what I'm authorizing** (boundary, categorization, system description)
2. **I know what risks exist** (vulnerability scan results + POA&M)
3. **I know those risks are managed** (ConMon plan, remediation timelines)
4. **The documentation says enough** (SSP covers all required sections; POA&M is current)
5. **The people are accountable** (ISSO/ISSM named, contact info correct)

Everything else is detail. Know the AO's mental model and work backwards from it.

---

## Hard Blockers: What an AO Will Not Sign Without

These items must exist before an AO review meeting. Missing any one of them stops the clock.

**1. Authorization Boundary Diagram**
- Must show: every system component (servers, containers, databases, load balancers, identity providers, external services), the boundary line, data flows across the boundary, trust zones
- Must be numbered: each component in the diagram must have a corresponding row in the system inventory
- Format: Visio, Lucidchart, or draw.io — exported to PDF for upload to eMASS
- Time to produce: 2-6 hours for a well-understood system; up to 2 days if you're reverse-engineering from a live environment
- AO failure mode: "Your boundary includes an external API but your SSP doesn't describe the interconnection" → ATO delayed

**2. FIPS 199 / CNSSI 1253 Categorization**
- Three values: Confidentiality impact (L/M/H), Integrity impact (L/M/H), Availability impact (L/M/H)
- Each must have a 2-3 sentence rationale explaining WHY that impact level was chosen
- Mission owner must agree/sign off — this is not a unilateral ISSO decision
- Common mistake: choosing Moderate because it "feels right" without written rationale → AO sends it back
- Time to produce: 1-2 hours if mission owner is available; 1-2 days if you're chasing approvals

**3. SSP with All Required Sections Populated**
- Every section must have content — no "TBD" or blank fields
- Control narratives must cover the applicable controls (at minimum, key controls per family)
- System description, data flows, interconnections, user types, and authorization boundary must be described
- Inherited controls must be marked as inherited with CRM reference
- Time to produce: This is the long pole in most ATOs. Allocate 6-16 hours depending on control count and writer experience.

**4. Current Vulnerability Scan Results**
- Scan results must be less than 30 days old at time of package submission
- Must include: OS/host scans (ACAS/Nessus), web application scan (if web-facing), container image scans (if containerized)
- Scans must be credentialed (authenticated) for OS-level findings — uncredentialed scans are not accepted
- All Criticals and Highs must have a POA&M entry (or an accepted deviation request)
- Time to produce: 2-24 hours to run scans; 1-4 hours to process and enter results into POA&M

**5. POA&M — Even If Empty**
- A blank POA&M (no findings) is acceptable only if scan results support it
- Every Critical/High/Moderate finding from scans must have a corresponding POA&M entry
- POA&M must include: Finding description, severity, source, responsible party, scheduled completion date, milestones
- No "TBD" for scheduled completion dates — AOs reject POA&Ms with vague timelines
- Time to produce: 1-3 hours for a clean system; 2-8 hours for a system with extensive findings

**6. CRM (Customer Responsibility Matrix)**
- Required if you leverage ANY inherited controls from a platform
- Shows: each inherited/shared control, which platform covers it, your obligations for shared controls
- Available as a template from platform owner (P1 CTSO, AWS Artifact, Azure Service Trust Portal, DISA STOREFRONT)
- You fill in your portion of shared controls
- Time to produce: 1-3 hours once you have the base CRM from the platform

**7. ConMon Plan (at minimum, an outline)**
- Most AOs will not sign without knowing how the system will be monitored post-authorization
- Minimum required: scanning frequency, POA&M update schedule, responsible party for each activity, escalation procedure
- Full ConMon Plan can come post-ATO, but AO needs to see a credible outline
- Time to produce: 1-2 hours for a basic ConMon overview table

**8. For IL5 and IL6: Penetration Test Results or Approved Waiver**
- IL5 systems should have a pen test before ATO; many AOs require it
- Pen testing requires scheduling 2-4 weeks in advance with an approved assessor
- If no pen test exists: risk acceptance memo with AO signature required; AO may refuse
- **Critical: start pen test scheduling on Day 1 if this is IL5 — it's the longest lead item**

---

## Lead-Time Items: Start on Day 1 Regardless of Everything Else

These items cannot be rushed once started. They set the minimum timeline. Kick them off immediately on Day 1, even if other work is incomplete.

| Item | Why Lead Time | Day 1 Action |
|------|--------------|-------------|
| Vulnerability scanning (credentialed) | Scans take 2-8 hours to run; analysis + POA&M entry takes another 4-8 hours. Must run AFTER system is in its final state (changes after scan = stale results). | Configure and launch ACAS/Nessus scans with credentials. |
| Penetration testing | Must schedule 2-4 weeks ahead; engagement takes 5-10 days | Contact approved assessor and schedule immediately if IL5/IL6 |
| Policy documents (if none exist) | Writing AC policy, CM policy, IR plan from scratch takes 1-3 days | Identify which policies exist; gap list; assign writers |
| Personnel security (clearance verification) | If clearances need to be adjudicated or updated, this takes weeks | Identify all system users requiring access; verify clearances are current |
| eMASS system registration | Must complete before you can upload any package components | Register system in correct eMASS tenant on Day 1 |
| Mission owner FIPS 199 sign-off | Chasing approvals is the silent killer of ATO timelines | Get FIPS 199 rationale approved by mission owner on Day 1 |

---

## AO-Blocking Control Families: Prioritize These in SSP

Not all controls are equal. AOs focus on certain families when reviewing packages. Write these first.

**Tier 1: AO Reads These First (will open these sections before anything else)**

1. **PL-2 / PL-7 (System Security Plans, Security Concepts)**: The SSP overview and system description. AO forms their mental model of what they're authorizing here.
2. **RA-2 (Security Categorization)**: FIPS 199 rationale. AO validates the scope is right.
3. **CA-6 (Authorization)**: The actual authorization section — defines ATO conditions, duration, residual risk statement.
4. **CA-7 (Continuous Monitoring)**: AO checks you have a credible monitoring plan.
5. **SC-7 (Boundary Protection)**: AO verifies boundary diagram matches SSP narrative.

**Tier 2: Technical Controls AOs Commonly Ask About**

6. **IA-2 / IA-2(1)/(2) (Multi-Factor Authentication)**: "How do users authenticate?" is almost always asked.
7. **AC-2 (Account Management)**: How are accounts created, modified, reviewed, and removed.
8. **AU-6 (Audit Review)**: "Who watches the logs and how fast do they respond?"
9. **CM-6 (Configuration Settings)**: STIG compliance score, how you manage configuration drift.
10. **SI-2 (Flaw Remediation)**: POA&M — how current is it, what's your patching timeline.
11. **IR-6 (Incident Reporting)**: Do you have a process to report incidents up the chain.

**Tier 3: Supporting Controls (need to be present; AO may not read deeply)**

All other controls — write these adequately but don't over-invest if time is short. An SSP with strong Tier 1 and Tier 2 narratives and thin Tier 3 narratives passes faster than an SSP that's mediocre across all tiers.

---

## Parallelization Map: Three-Track Sprint

The 3-day ATO sprint runs three parallel tracks:

```
TRACK A: Documentation          TRACK B: Technical Evidence       TRACK C: Package Admin
━━━━━━━━━━━━━━━━━━━━━━━━         ━━━━━━━━━━━━━━━━━━━━━━━━━━━        ━━━━━━━━━━━━━━━━━━━━━━
Day 1:                           Day 1:                             Day 1:
- FIPS 199 (with mission owner)  - Launch ACAS/Nessus scans        - Register system in eMASS
- Boundary diagram               - Launch SCAP/SCC (OS STIG)       - Get CRM from platform
- System description             - Launch container scans (if K8s)  - Assign ISSO/ISSM/AO in eMASS
- SSP overview section           - Identify all data flows          - Prep schedule for pen test (IL5)

Day 2:                           Day 2:                             Day 2:
- SSP control narratives         - Process scan results             - Enter FIPS 199 in eMASS
  (Tier 1 + 2 first)             - Begin POA&M population           - Upload boundary diagram
- ConMon plan outline            - Remediate Critical findings      - Link CRM to eMASS controls
- CMP, IRP, ACP drafts             where possible (< 4hr fixes)     - Mark inherited controls

Day 3:                           Day 3:                             Day 3:
- Complete SSP narratives        - Finalize POA&M with             - Upload all documents
  (Tier 3 controls)                milestone dates                  - Final eMASS review pass
- Residual risk statement        - Final scan run (confirm          - Submit for AO review
- AO briefing deck               changes are captured)              - Schedule AO meeting
```

**Track dependencies:**
- Track B scan results inform Track A POA&M section and Track C POA&M upload
- Track C eMASS must be registered before Track A SSP can be uploaded
- Track A boundary diagram must be complete before Track B data flow analysis

---

## Timeline Compression Techniques

### Technique 1: Inheritance First
Before writing a single SSP narrative, identify your full inheritance. Controls you inherit = controls you don't write. On P1 at IL4, this eliminates 120-140 controls from your writing queue immediately.

### Technique 2: Scan While You Write
Launch scans at 0800 Day 1 and let them run in the background while you write SSP narratives. By the time your Tier 1+2 narratives are done, scans are complete and you can immediately populate the POA&M.

### Technique 3: Use Existing Policies
Never write a policy from scratch if you can reference an existing policy. Most organizations have ISO-aligned or NIST-aligned policies. Cite them by title and version. The SSP narrative says "See [Policy Name] v[X.X] for implementation details" — that satisfies the policy requirement.

### Technique 4: IATT to Bridge Scan-to-POA&M Gap
If scans reveal Moderate/Low findings that will take 30-90 days to remediate, get an IATT (Interim Authority to Test) while remediating. IATT allows operation during the remediation window. AO signs IATT with conditions; conditions become your POA&M milestones.

### Technique 5: AO Briefing Before Package Submission
For programs where the AO is accessible: brief the AO informally before submitting the formal package. "Here's what we have, here are the 3 open findings, here's the plan." An AO who already understands the system and the risks signs faster once the formal package arrives.

### Technique 6: Modular SSP — Write Prioritized
In eMASS, controls are individually tracked. Write narratives in priority order, not family order. Finish Tier 1 controls completely before starting Tier 2. If time runs out, a complete Tier 1+2 with partial Tier 3 is better than mediocre coverage across all families.

### Technique 7: Scope Reduction via Boundaries
The tightest reasonable boundary = fewest controls = fastest ATO. If your application connects to 15 external systems, document those as interconnections (ISA/MOU), not as part of your boundary. Inherited external systems reduce your scope significantly.

### Technique 8: Accept Risk vs. Delay
For findings that cannot be remediated in the ATO sprint timeframe, document a risk acceptance rationale in the POA&M. A written, acknowledged risk with a remediation timeline is better than delaying the ATO. AOs are authorized to accept risk — use that mechanism.

---

## Scenario-Based Timelines

**Scenario 1: Modern app on Platform One, IL4, Air Force, no prior ATO**
- Inheritance: P1 covers ~50% of controls
- Technical complexity: Low (P1 handles infra)
- Timeline: 3-5 days
- Key accelerators: P1 CRM available same day; Twistlock scans automated by P1; AF eMASS familiar to P1 CTSO
- Common delays: CAC/PIV Keycloak configuration not complete; Iron Bank images have open CVEs

**Scenario 2: Kubernetes app on AWS GovCloud, IL4, Army, no prior ATO**
- Inheritance: AWS covers ~35-40% of controls
- Technical complexity: Medium (you own K8s STIG + OS STIG)
- Timeline: 5-10 days
- Key accelerators: AWS Security Hub gives instant compliance posture; AWS Config shows drift in real-time
- Common delays: STIG compliance below 95%; open High/Critical scan findings; ARCYBER connection approval process

**Scenario 3: Windows Server app, on-prem DoD enclave, IL4, Navy**
- Inheritance: Facility PE only (~15% of controls)
- Technical complexity: High (Windows STIG, AD STIG, IIS STIG, database STIG)
- Timeline: 15-30 days
- Key accelerators: DISA GPO packages applied; PowerSTIG automation; SCC scan automation
- Common delays: PPSM registration (Navy-specific); legacy software can't meet STIG requirements; AD group policy conflicts with STIG

**Scenario 4: Containerized app on AWS GovCloud, IL5, SOCOM**
- Inheritance: AWS IL5 PA covers ~35% of controls; additional verification needed
- Technical complexity: High (dedicated instances, HSM, US-persons-only enforcement)
- Timeline: 10-20 days
- Key accelerators: SOCOM can expedite for operational urgency; SOCOM J62 familiar with fast-track process
- Common delays: Dedicated instance tenancy not configured; HSM setup takes 2-3 days; pen test scheduling

**Scenario 5: New ATO leveraging existing FedRAMP P-ATO (reciprocity path to IL4)**
- Inheritance: FedRAMP High covers baseline; add IL4 delta controls
- Technical complexity: Low-Medium (delta is manageable)
- Timeline: 3-7 days
- Key accelerators: FedRAMP package already documents most controls; CSP CRM already exists
- Common delays: DISA-specific IL4 requirements not in original FedRAMP package; finding the right AO for reciprocity acceptance

---

## IATT / IATO / ATO Decision Matrix

| Situation | Right Choice | Why |
|-----------|-------------|-----|
| System not yet deployed; testing needed | IATT (Interim Authority to Test) | Limits scope to testing; doesn't authorize production data |
| System deployed; minor open findings; remediation in progress | IATO (Interim ATO) | Authorizes production with conditions; typically 6-month window |
| System deployed; clean scan; complete package | Full ATO | Maximum authorization; typically 1-3 years |
| Open High/Critical findings that can't be quickly fixed | IATO with POA&M milestones | AO accepts risk with documented remediation plan |
| System urgently needed for operations | IATT first → full ATO within 90 days | Operational need drives urgency; document residual risk |
| System has existing ATO but major change | Significant Change → updated ATO or addendum | See significant-change-criteria.md |

**IATT specifics:**
- Duration: Typically 90 days, renewable
- Conditions: Must document what data types are prohibited during test phase
- Allows: Testing with non-production data; functional validation
- Does not allow: Production data; live operations

**IATO specifics:**
- Duration: Typically 6 months; some AOs grant up to 12 months
- Conditions: Specific POA&M milestones must be met; periodic check-ins required
- Allows: Production operation with documented residual risk
- AO can revoke: If POA&M milestones are missed or new critical findings emerge

---

## ConMon Minimum Requirements Before ATO

An AO will want to see at least a ConMon outline. Minimum content:

| Activity | Frequency | Tool | Owner |
|----------|-----------|------|-------|
| Vulnerability scanning (OS/infra) | Monthly | ACAS/Nessus | ISSO |
| Container image scanning | Per deployment / weekly | Twistlock/Trivy | DevSecOps team |
| Web application scanning | Monthly | [tool] | ISSO |
| POA&M review and update | Monthly | eMASS | ISSO/ISSM |
| Log review and anomaly investigation | Continuous / daily | [SIEM tool] | ISSO |
| Privileged user access review | Quarterly | AD/IAM reports | ISSO |
| Hardware/software inventory reconciliation | Quarterly | CMDB/eMASS | CM team |
| Annual security assessment (subset of controls) | Annual | [SCA team] | ISSM |
| Contingency plan test | Annual | Tabletop/functional test | PM/ISSO |
| Security awareness training completion | Annual | [LMS] | PM |
| Authorization package review | Annual | eMASS | ISSO/ISSM/AO |

This table, presented in the SSP ConMon section and/or a separate ConMon Plan document, satisfies the AO's need to know the system will be maintained post-authorization.
