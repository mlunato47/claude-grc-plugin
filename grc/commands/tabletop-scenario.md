---
description: "Generate IR or CP tabletop exercise scenarios"
---

# /grc:tabletop-scenario

Generate incident response or contingency plan tabletop exercise scenarios.

## Usage

```
/grc:tabletop-scenario [type] [scenario?] [system-type?]
```

## Arguments

- **type**: `ir` (incident response) or `cp` (contingency plan)
- **scenario** (optional): Scenario theme — `credentials`, `ransomware`, `breach`, `supply-chain`, `insider`, `ddos`, `outage`, `corruption`, `custom`
- **system-type** (optional): System context — `saas`, `paas`, `iaas`, `web-app`, `api`, `data-platform`

## Examples

```
/grc:tabletop-scenario ir credentials
/grc:tabletop-scenario ir ransomware saas
/grc:tabletop-scenario cp outage
/grc:tabletop-scenario ir supply-chain api
/grc:tabletop-scenario cp corruption data-platform
/grc:tabletop-scenario ir custom
```

## Behavior

When invoked:

1. **No redaction reminder needed** — this is a pure reference command generating generic exercise scenarios. No user content is processed.

2. **Read the appropriate reference files**:
   - `skills/grc-knowledge/audits/tabletop-scenarios.md` for scenario templates, exercise structure, and report requirements
   - `skills/grc-knowledge/audits/document-section-requirements.md` for IRP/CP section requirements (to ensure the exercise tests relevant procedures)

3. **Generate a complete tabletop exercise package**:

   **a. Scenario Narrative**
   A realistic scenario appropriate to the type and system context. Written in present tense, progressively revealing information through injects.

   **b. Injects**
   4-6 progressive injects that escalate the scenario and force new decisions. Each inject should:
   - Introduce new information
   - Require a decision or action
   - Test a different aspect of the IRP/CP

   **c. Discussion Questions**
   8-12 questions that probe:
   - Detection and initial response
   - Escalation and communication
   - Containment/recovery decisions
   - External reporting obligations (CISA, FedRAMP PMO, agencies)
   - Evidence preservation
   - Lessons learned

   **d. Controls Exercised**
   List of NIST 800-53 controls that the scenario tests.

   **e. Exercise Planning Checklist**
   Pre-exercise, during, and post-exercise checklists from the reference file.

   **f. Report Template**
   Structure for the exercise report that serves as evidence for IR-3 or CP-4.

4. **If `custom` scenario is specified**, ask the user what type of incident or contingency they want to simulate and generate a tailored scenario.

5. **If system-type is provided**, tailor the scenario details:
   - SaaS: multi-tenant impacts, customer notification, API disruption
   - IaaS: infrastructure-level attacks, hypervisor concerns, region failures
   - Web app: application-layer attacks, XSS/SQLi, session hijacking
   - API: API abuse, rate limiting failures, authentication bypass
   - Data platform: data corruption, ETL failures, reporting accuracy

6. **If no arguments provided**, ask what type of exercise (IR or CP) and offer scenario options.

## Output Format

```
## Tabletop Exercise: [Type] — [Scenario Title]

**Exercise Type**: [Incident Response / Contingency Plan]
**Scenario Theme**: [Theme]
**Estimated Duration**: [1-3 hours]
**Controls Exercised**: [List of control IDs]

---

### Pre-Exercise Checklist
- [ ] Participants identified and notified
- [ ] Facilitator briefed on scenario and injects
- [ ] Current IRP/CP available for reference
- [ ] Note-taker assigned
- [ ] Confirm: THIS IS AN EXERCISE (not a real incident)

---

### Scenario

**Background**:
[1-2 paragraphs setting the scene]

**Initial Alert**:
> [The triggering event — what participants first learn]

---

### Inject 1 — [Title] (reveal at ~15 minutes)
> [New information that changes the picture]

**Questions**:
1. [Question testing detection/initial response]
2. [Question testing a specific decision]

### Inject 2 — [Title] (reveal at ~30 minutes)
> [Escalation or complication]

**Questions**:
3. [Question testing escalation]
4. [Question testing communication]

### Inject 3 — [Title] (reveal at ~45 minutes)
> [Further escalation]

**Questions**:
5. [Question testing containment/recovery]
6. [Question testing external reporting]

### Inject 4 — [Title] (reveal at ~60 minutes)
> [Resolution phase complication or new dimension]

**Questions**:
7. [Question testing evidence/forensics]
8. [Question testing lessons learned]

---

### Additional Discussion Questions
9. [Broader question about process improvement]
10. [Question about plan adequacy]
11. [Question about training needs]
12. [Question about tool/automation gaps]

---

### Exercise Wrap-Up

**Hot Wash Questions**:
1. What went well?
2. What gaps did we identify in our [IRP/CP]?
3. What would we do differently in a real incident?
4. What training or resources do we need?

---

### Exercise Report Template

1. **Summary**: Date, duration, scenario, participants
2. **Objectives**: What was tested
3. **Findings**: Gaps and strengths identified
4. **Action Items**: Improvements with owners and due dates
5. **Plan Updates**: Changes to make to the [IRP/CP]
6. **Next Exercise**: Recommended scenario and timeframe

*This report satisfies evidence requirements for [IR-3 / CP-4].*
```

## Notes

- Scenarios are intentionally generic — they do not reference specific systems, agencies, or vulnerabilities.
- The exercise should test the actual procedures in the organization's IRP or CP, not generic incident response knowledge.
- FedRAMP requires annual testing of both the IRP (IR-3) and contingency plan (CP-4).
- A good tabletop makes participants uncomfortable — if every question has an obvious answer, the scenario isn't challenging enough.
- This command pairs with `/grc:evidence-checklist` to prepare the documentation evidence for IR-3 or CP-4.
