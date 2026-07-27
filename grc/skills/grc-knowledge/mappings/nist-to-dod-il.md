# NIST 800-53 ↔ DoD/DoW Impact Levels Mapping

## How This Mapping Works

DoD/DoW Impact Levels are **not a parallel control catalog** — they are *compositions of NIST 800-53 Rev 5 selections*. Unlike SOC 2 or ISO 27001, there is no IL-native control ID to crosswalk. Mapping between NIST and an Impact Level means answering two questions:

1. **Forward (IL → NIST):** which NIST baseline + which added controls/parameters does this IL require?
2. **Reverse (NIST control → IL):** at which Impact Levels is this control required, and does the DoW change its parameter values?

The composition stack for every IL is:

```
FedRAMP baseline (NIST 800-53 Rev 5 selection + FedRAMP parameters)
  + DoW FedRAMP+ controls & parameter adjustments   (IL4/5/6 only)
  + CNSSI 1253 baseline mapping & overlays          (MMx or HHx)
  + CNSSI 1253 Appendix D NSS controls              (IL5/6)
  + CNSSI 1253 Classified Information Overlay       (IL6 — values take precedence)
  + SRG operational requirements (separation, personnel, connectivity, IR)
```

Authority: DISA **Cloud Service Provider SRG V1R7** (30 June 2026), Table 3-1 and Appendix D Table D-1. Framework detail: `frameworks/dod-impact-levels.md`.

## Forward Mapping: Impact Level → NIST 800-53 Composition

| Impact Level | NIST/FedRAMP baseline | CNSSI 1253 | Added control sets |
|--------------|----------------------|------------|--------------------|
| **IL2** | FedRAMP Moderate (≈322 controls) | n/a (reciprocity accepted) | None — FedRAMP Moderate PA accepted as-is |
| **IL4** (Moderate path) | FedRAMP Moderate | Table D-1, CIA MMx | FedRAMP+ (Table D-1 below) + data-driven overlays |
| **IL4** (High path) | FedRAMP High (≈410 controls) | Table D-1, CIA HHx | FedRAMP+ + data-driven overlays |
| **IL5** | FedRAMP High | Table D-1 "+", CIA HHx | FedRAMP+ + **Appendix D NSS controls** + overlays |
| **IL6** | FedRAMP High | Table D-1 "+" + Classified Overlay, CIA HHx | FedRAMP+ + NSS controls + **Classified Information Overlay** (precedence) |

## Control-Level Deltas: DoW FedRAMP+ (Appendix D, Table D-1)

These NIST 800-53 Rev 5 controls/enhancements are added to, or have parameters adjusted from, the FedRAMP baseline. "DSPAV" = the DoW Specific Assignment Value from the DoW RMF TAG must be used.

| NIST control | Delta vs FedRAMP | IL4 | IL5 | IL6 |
|--------------|------------------|-----|-----|-----|
| AC-7 | Adjusted: privileged lock after 3 attempts (ILs 2/4/5 per SRG; 5 for SIPR token), admin unlock; non-privileged 10/30-min if rate-limited, otherwise normal DSPAV | ✓ | ✓ | ✓ |
| AU-5(1) | FedRAMP value acceptable (listed for completeness) | ✓ | ✓ | ✓ |
| CM-7(5) | DSPAV | ✓ | ✓ | ✓ |
| IA-5(1) | DSPAV | ✓ | ✓ | ✓ |
| MA-5(1) | DSPAV | ✓ | — | — |
| MA-5(2), MA-5(3), MA-5(4) | Added at IL6 (no parameter adjustment specified) | — | — | ✓ |
| MA-5(5) | Added | ✓ | ✓ | ✓ |
| MA-6 | FedRAMP value acceptable | ✓ | ✓ | ✓ |
| PE-15 | DSPAV | ✓ | ✓ | ✓ |
| PS-3(4) | Adjusted: citizenship-based screening — users U.S. citizens/nationals/persons (plus foreign personnel per DoW policy with AO approval); admins U.S. citizens/nationals/persons only | ✓ | ✓ | ✓ |
| PS-4 | FedRAMP value acceptable | ✓ | ✓ | ✓ |
| SA-4(5) | DSPAV | ✓ | ✓ | ✓ |
| SA-9(1), SA-9(3) | DSPAV | ✓ | ✓ | ✓ |
| SA-9(5) | Adjusted: processing/data/services restricted to U.S./U.S.-jurisdiction locations | ✓ | ✓ | ✓ |
| SA-9(6), SA-9(7), SA-9(8) | Added | ✓ | ✓ | ✓ |
| SC-12(6) | Added | ✓ | ✓ | ✓ |
| SC-17 | Adjusted: PKI per DODI 8520.02 | ✓ | ✓ | ✓ |
| SC-18, SC-18(2) | Added/DSPAV (mobile code) | ✓ | ✓ | ✓ |
| SC-18(3), SC-18(4) | Added: no unacceptable mobile-code download; permission prompting | — | ✓ | ✓ |
| SC-24 | DSPAV | ✓ | ✓ | ✓ |
| SC-46 | DSPAV — only when a cross-domain solution is used | (CDS) | (CDS) | (CDS) |

At IL6 the CNSSI 1253 Classified Information Overlay modifies some of these values and adds further controls; overlay values take precedence.

## SRG Requirements Anchored to NIST Controls

Beyond Table D-1, the SRG's operational sections attach to specific NIST controls:

| NIST control | SRG requirement | IL |
|--------------|-----------------|-----|
| SC-4 | Impact Level separation model (§5.2.2): virtual separation at IL4; physical **or** NSA-approved cryptographic separation at IL5; dedicated infrastructure at IL6 | 4/5/6 |
| PS-3, PS-3(3) | Investigation tiers: Tier 1 (IL2), Tier 3 (IL4/5), Tier 3-classified (IL6), Tier 5 for key IL6 cyber personnel | all |
| MA-5 | Digital-escort remote maintenance for sensitive systems (§5.17) | 4/5/6 |
| IR family | DoW-specific incident categories, timelines, reporting mechanisms (§6.2) | all |
| SC-7, SC-7(3), SC-7(4) | CAP-mediated DISN connectivity; approved boundaries only (§5.9.1) | 4/5/6 |
| MP-6 / media | Data retrieval and destruction at CSO termination; media reuse/disposal (§5.7–5.8) | 4/5/6 |
| SR family | Supply chain risk management assessment (§5.12); subcontracted CSO disclosure is required at PA assessment (§3.6) | 4/5/6 |

## Reverse Lookup: "Is NIST control X required at IL Y?"

Decision order:

1. **Is it in the FedRAMP baseline for that IL's floor?** (Moderate for IL2/IL4-Moderate-path; High for IL4-High-path/IL5/IL6.) If yes → required, with FedRAMP parameters.
2. **Is it in Table D-1 above?** If yes → required at the listed ILs with the DoW parameter (DSPAV or the stated adjustment), which **overrides** the FedRAMP value — unless the table notes the FedRAMP value is acceptable (AU-5(1), MA-6, PS-4).
3. **IL5/6 only:** is it a CNSSI 1253 Appendix D NSS control or (IL6) Classified Overlay control? If yes → required even if absent from the FedRAMP baseline.
4. Otherwise → not required by the IL composition (though a Mission Owner/AO may still add it via tailoring).

For FedRAMP-baseline membership and parameter values, use the OSCAL data: `oscal/fedramp-moderate-rev5/{family}.json` (Moderate) and `oscal/nist-800-53-rev5/{family}.json` (full catalog).

## Mapping ILs to Other Frameworks

To relate an Impact Level to a non-NIST framework (SOC 2, ISO 27001, etc.), chain through NIST as usual:

1. Resolve the IL to its NIST composition (this file).
2. Map the relevant NIST controls to the target framework via `mappings/nist-to-<target>.md`.

Note the reverse direction is weaker: no commercial framework certification (SOC 2, ISO 27001) provides any reciprocity toward a DoW PA — only FedRAMP authorizations enter the IL reciprocity chain.

## Related References

- `frameworks/dod-impact-levels.md` — full Impact Level framework reference (SRG V1R7)
- `frameworks/fedramp.md` — FedRAMP program and baselines
- `frameworks/nist-800-53.md` — NIST 800-53 Rev 5 anchor reference
- `oscal/fedramp-moderate-rev5/` — authoritative FedRAMP Moderate control data
- CNSSI 1253 and the DoW RMF Knowledge Service (https://rmfks.osd.mil) for DSPAV values
