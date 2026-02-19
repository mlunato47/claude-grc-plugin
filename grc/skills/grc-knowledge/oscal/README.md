# OSCAL Structured Data

Per-family JSON files extracted from official OSCAL catalogs published by NIST and FedRAMP.

## Sources

| Dataset | Source Repository | License |
|---------|-------------------|---------|
| **NIST 800-53 Rev 5** | [usnistgov/oscal-content](https://github.com/usnistgov/oscal-content) | Public domain (NIST) |
| **FedRAMP Moderate Rev 5** | [GSA/fedramp-automation](https://github.com/GSA/fedramp-automation) | CC0 1.0 / Public domain |

### Source URLs

- NIST: `nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json`
- FedRAMP: `dist/content/rev5/baselines/json/FedRAMP_rev5_MODERATE-baseline-resolved-profile_catalog.json`

## Directory Structure

```
oscal/
├── nist-800-53-rev5/       # Full NIST 800-53 Rev 5 catalog (all controls)
│   ├── metadata.json       # Catalog metadata (title, version, last-modified)
│   ├── ac.json             # Access Control family
│   ├── at.json             # Awareness and Training family
│   ├── ...                 # One file per family (20 families)
│   └── sr.json             # Supply Chain Risk Management family
├── fedramp-moderate-rev5/  # FedRAMP Moderate baseline only
│   ├── metadata.json
│   ├── ac.json
│   ├── ...                 # 18 families (PM and PT not in Moderate baseline)
│   └── sr.json
└── README.md
```

## What Each File Contains

Each family JSON file is the complete OSCAL group object:

- **controls**: All controls in the family with enhancements nested under parent controls
- **params**: Organization-defined parameters (ODPs) with labels, guidelines, and constraints
- **parts**: Control statement parts (requirements text), guidance, assessment objectives
- **links**: Related control references
- **props**: Properties like baseline assignment labels

## ID Normalization

OSCAL uses lowercase hyphenated IDs with dots for enhancements:

| Human ID | OSCAL ID |
|----------|----------|
| AC-2 | `ac-2` |
| AC-2(1) | `ac-2.1` |
| AC-2(1)(a) | Part `ac-2.1_smt.a` |