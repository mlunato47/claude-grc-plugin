---
description: "Continuous monitoring guidance by topic"
---

# /grc:conmon-guide

Continuous monitoring guidance by topic.

## Usage

```
/grc:conmon-guide [topic]
```

## Arguments

- **topic**: The ConMon topic area. Accepts:
  - `monthly` — Monthly deliverables and activities
  - `annual` — Annual deliverables and activities
  - `poam` — POA&M management and lifecycle
  - `scanning` — Vulnerability scanning requirements and processes
  - `metrics` — ConMon metrics and reporting
  - `lifecycle` — Full ISCM lifecycle overview
  - `tooling` — Automated tooling categories and requirements

## Examples

```
/grc:conmon-guide monthly
/grc:conmon-guide poam
/grc:conmon-guide scanning
/grc:conmon-guide lifecycle
```

## Behavior

When invoked:

1. **Identify the topic** from the argument.

2. **Read the appropriate reference file(s)**:
   - `monthly` → `conmon/monthly-deliverables.md`
   - `annual` → `conmon/annual-deliverables.md`
   - `poam` → `conmon/poam-management.md`
   - `scanning` → `conmon/automated-tooling.md` + `conmon/monthly-deliverables.md`
   - `metrics` → `conmon/iscm-lifecycle.md` + `conmon/monthly-deliverables.md`
   - `lifecycle` → `conmon/iscm-lifecycle.md`
   - `tooling` → `tooling/grc-tooling-categories.md` + `conmon/automated-tooling.md`

3. **Present guidance** structured by:
   - What activities are required
   - Who is responsible (roles)
   - When / how frequently
   - What deliverables are produced
   - Framework-specific requirements (FedRAMP, FISMA)
   - Common pitfalls and best practices
   - Automation opportunities

4. **If no topic provided**, show a summary of all ConMon areas with brief descriptions and ask which to dive into.

## Output Format

```
## Continuous Monitoring: [Topic]

### Overview
[Brief description of this ConMon area]

### Activities
| Activity | Frequency | Responsible Role | Deliverable |
|----------|-----------|-----------------|-------------|

### Requirements
[Framework-specific requirements — FedRAMP, FISMA, etc.]

### Best Practices
- [Practice 1]
- [Practice 2]

### Common Pitfalls
- [Pitfall 1]
- [Pitfall 2]

### Automation Opportunities
- [Opportunity 1]
- [Opportunity 2]
```
