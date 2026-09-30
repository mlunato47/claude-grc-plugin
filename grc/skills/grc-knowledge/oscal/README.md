# OSCAL Structured Data

Per-family JSON files extracted from official OSCAL catalogs published by NIST and FedRAMP.

## Sources

| Dataset | Source Repository | License |
|---------|-------------------|---------|
| **NIST 800-53 Rev 5** | [usnistgov/oscal-content](https://github.com/usnistgov/oscal-content) | Public domain (NIST) |
| **FedRAMP Moderate Rev 5** | Formerly [GSA/fedramp-automation](https://github.com/GSA/fedramp-automation) (repository no longer exists; legacy Rev5 content now lives under [FedRAMP/docs-legacy](https://github.com/FedRAMP/docs-legacy)) | CC0 1.0 / Public domain |

### Source URLs

- NIST: `nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json` (Release 5.2.0, last modified 2025-08-26; still the latest NIST release as of September 2026)
- FedRAMP: `dist/content/rev5/baselines/json/FedRAMP_rev5_MODERATE-baseline-resolved-profile_catalog.json` (profile version `fedramp2.1.0-oscal1.0.4`, published 2024-09-24)

### Currency Note (September 2026)

- The NIST catalog extract is **Release 5.2.0**, which added SA-15(13), SA-24, and SI-2(7) and revised SI-7(12). None of those are in any 800-53B or FedRAMP baseline.
- The FedRAMP Moderate profile is the **legacy Rev5 baseline**. Its FedRAMP-assigned parameter values (e.g., "at least every 3 years") remain in force for Rev5 packages only until the Consolidated Rules for 2026 (CR26) become mandatory on **January 1, 2027**; CR26 removed most FedRAMP-assigned parameter values and points several controls to rulesets instead (VDR/VER, IEC, SCN, CMU, SCG). Treat these values as "legacy Rev5" and check `frameworks/fedramp-20x.md` for the CR26 status.
- Under CR26, OSCAL is optional; FedRAMP's own JSON schemas (github.com/FedRAMP/schemas) are the required machine-readable format (FRC-CSO-JSN). This data remains useful for control text, parameters, and assessment objectives.
- The profile metadata still names the JAB and the FedRAMP PMO as roles; the JAB was dissolved in May 2024 (replaced by the FedRAMP Board) and current FedRAMP documents say "FedRAMP" rather than "FedRAMP PMO".

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