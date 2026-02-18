---
description: "Generate a recurring compliance activity calendar by framework"
---

# /grc:compliance-calendar

Generate a recurring compliance activity calendar by framework.

## Usage

```
/grc:compliance-calendar [frameworks] [format?]
```

## Arguments

- **frameworks**: One or more frameworks, comma-separated. Accepts: `fedramp`, `nist`, `fisma`, `soc2`, `iso27001`, `pci`, `hipaa`, `cmmc`, `all`
- **format** (optional):
  - `monthly` (default): Month-by-month calendar view
  - `frequency`: Grouped by frequency (daily, weekly, monthly, quarterly, annual)
  - `controls`: Activities mapped to control IDs

## Examples

```
/grc:compliance-calendar fedramp
/grc:compliance-calendar fedramp,soc2
/grc:compliance-calendar fedramp monthly
/grc:compliance-calendar pci frequency
/grc:compliance-calendar fedramp,soc2,pci controls
```

## Behavior

When invoked:

1. **No redaction reminder needed** — this is a pure reference command generating calendars from framework knowledge. No user content is processed.

2. **Read the appropriate reference files**:
   - `skills/grc-knowledge/conmon/compliance-calendar.md` for consolidated calendar data
   - `skills/grc-knowledge/conmon/monthly-deliverables.md` for monthly detail
   - `skills/grc-knowledge/conmon/annual-deliverables.md` for annual detail
   - `skills/grc-knowledge/conmon/iscm-lifecycle.md` for lifecycle context

3. **Generate the calendar**:

   **For `monthly` format**:
   - Present a 12-month calendar template
   - Monthly recurring activities appear every month
   - Quarterly activities placed in Q1-Q4 months
   - Annual activities distributed across the year with recommended scheduling
   - If multiple frameworks: consolidate overlapping activities, note the strictest frequency

   **For `frequency` format**:
   - Group all activities by frequency: Daily, Weekly, Monthly, Quarterly, Semi-Annual, Annual, Event-Driven
   - Include responsible role, deliverable, and control reference for each
   - If multiple frameworks: show which framework(s) require each activity

   **For `controls` format**:
   - Map each recurring activity to its control ID(s)
   - Include frequency, responsible role, and deliverable
   - Useful for verifying control implementation completeness

4. **If multiple frameworks are specified**, harmonize activities:
   - Identify activities required by multiple frameworks (e.g., vulnerability scanning)
   - Use the most frequent requirement (e.g., FedRAMP monthly scanning satisfies PCI quarterly)
   - Note framework-specific activities that don't overlap
   - Flag where one activity can satisfy multiple framework requirements

5. **If no arguments provided**, ask the user which framework(s) to generate a calendar for.

## Output Format

### Monthly format:

```
## Compliance Calendar: [Framework(s)]

### Recurring Monthly Activities
[Activities that repeat every month]

| Activity | Frequency | Role | Deliverable | Control |
|----------|-----------|------|-------------|---------|

---

### Month-by-Month Schedule

#### January
**Monthly**: [Standard monthly activities]
**Quarterly (Q1)**: [Q1 activities]
**Annual**: [Annual activities suggested for January]

#### February
**Monthly**: [Standard monthly activities]
...

[Continue for all 12 months]

---

### Event-Driven Activities
| Trigger | Activity | Timeline | Control |
|---------|----------|----------|---------|
```

### Frequency format:

```
## Compliance Calendar: [Framework(s)] — By Frequency

### Daily / Continuous
| Activity | Role | Control | Framework |
|----------|------|---------|-----------|

### Weekly
| Activity | Role | Control | Framework |
|----------|------|---------|-----------|

### Monthly
| Activity | Role | Deliverable | Control | Framework |
|----------|------|-------------|---------|-----------|

[Continue through all frequencies]
```

### Controls format:

```
## Compliance Calendar: [Framework(s)] — By Control

| Control | Activity | Frequency | Role | Deliverable |
|---------|----------|-----------|------|-------------|
| AU-6 | Log review | Daily | SOC Analyst | Review records |
| RA-5 | Vulnerability scan | Monthly | Security Engineer | Scan report |
...
```

## Notes

- The calendar is a template — organizations should adjust annual activity placement based on their ATO anniversary date and assessment cycle.
- When multiple frameworks overlap, doing the most frequent activity once satisfies all frameworks (e.g., monthly scans for FedRAMP also satisfy PCI quarterly requirement).
- Event-driven activities (incident response, significant changes) cannot be calendared but should be documented in the compliance program.
- This command pairs with `/grc:conmon-guide` for detailed guidance on specific activities.
