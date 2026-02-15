# NIST 800-53 Rev 4 to Rev 5 Transition Guide

Mapping of changes between NIST 800-53 Revision 4 and Revision 5. Use this reference to help organizations transitioning their SSPs, control implementations, and assessments.

## High-Level Changes

| Aspect | Rev 4 | Rev 5 |
|--------|-------|-------|
| Total controls | ~965 (controls + enhancements) | ~1189 (controls + enhancements) |
| Control families | 18 | 20 (added PT and SR) |
| Structure | Controls are specific to federal systems | Controls are outcome-based, applicable to any system type |
| Privacy | Appendix J (privacy overlay) | Integrated into control families + new PT family |
| Supply chain | SA-12 (limited) | New SR family (12 base controls, plus enhancements) |
| Control baselines | In 800-53 itself | Moved to 800-53B (separate publication) |
| Assessment procedures | In 800-53A | Updated 800-53A Rev 5 |

## New Control Families in Rev 5

### PT — PII Processing and Transparency (New)
Privacy controls moved from Appendix J and expanded.

| Control | Title | Baseline |
|---------|-------|----------|
| PT-1 | Policy and Procedures | Privacy |
| PT-2 | Authority to Process PII | Privacy |
| PT-3 | PII Processing Purposes | Privacy |
| PT-4 | Consent | Privacy |
| PT-5 | Privacy Notice | Privacy |
| PT-6 | System of Records Notice | Privacy |
| PT-7 | Specific Categories of PII | Privacy |
| PT-8 | Computer Matching Requirements | Privacy |

**Note**: PT controls are allocated to the **Privacy baseline** in SP 800-53B, not to the Low/Moderate/High security baselines. FedRAMP includes selected PT controls in its security baselines as additional requirements.

**Impact**: Organizations must now explicitly address PII processing in their SSPs. Previously handled via privacy overlay or appendix.

### SR — Supply Chain Risk Management (New)
Expanded from SA-12 into a full family.

| Control | Title | Baselines (L/M/H) |
|---------|-------|--------------------|
| SR-1 | Policy and Procedures | L/M/H |
| SR-2 | Supply Chain Risk Management Plan | L/M/H |
| SR-3 | Supply Chain Controls and Processes | L/M/H |
| SR-4 | Provenance | — |
| SR-5 | Acquisition Strategies | L/M/H |
| SR-6 | Supplier Assessments and Reviews | M/H |
| SR-7 | Supply Chain Operations Security | — |
| SR-8 | Notification Agreements | L/M/H |
| SR-9 | Tamper Resistance and Detection | — |
| SR-10 | Inspection of Systems or Components | L/M/H |
| SR-11 | Component Authenticity | L/M/H |
| SR-12 | Component Disposal | L/M/H |

**Impact**: Supply chain risk management now requires formal SCRM plans, supplier assessments, and component authenticity verification. This is a significant new burden for many organizations.

## Withdrawn Controls

Controls below were withdrawn and their requirements incorporated into other controls. Note: AC-13, AC-15, SC-14, and SC-33 were already withdrawn in Rev 4; they are included here for completeness since Rev 4 SSPs may still reference them. SA-18 through SA-21 were newly withdrawn in Rev 5.

| Rev 4 Control | Title | Disposition | Withdrawn In |
|---------------|-------|-------------|-------------|
| AC-13 | Supervision and Review — Access Control | Incorporated into AC-2 and AU-6 | Rev 4 |
| AC-15 | Automated Marking | Incorporated into MP-3 | Rev 4 |
| SC-14 | Public Access Protections | Incorporated into AC-2, AC-3, SC-7 | Rev 4 |
| SC-33 | Transmission Preparation Integrity | Incorporated into SC-8 | Rev 4 |
| SA-18 | Tamper Resistance and Detection | Incorporated into SR-9 | Rev 5 |
| SA-19 | Component Authenticity | Incorporated into SR-11 | Rev 5 |
| SA-20 | Customized Development | Incorporated into SA-8 | Rev 5 |
| SA-21 | Developer Screening | Incorporated into SA-4, PS-7 | Rev 5 |

**Note**: AU-13, PM-1, SC-34, and SI-8 are sometimes listed as withdrawn but they still exist in the Rev 5 catalog. AU-13 and SI-8 remain as controls (not in standard baselines). PM-1 remains active. SC-34 exists but SC-34(3) was moved to SC-51.

**Migration note**: If your Rev 4 SSP has narratives for withdrawn controls, those narratives must be migrated to the incorporating controls in Rev 5.

## Significant Control Changes

### AC Family Changes
| Control | Change | Migration Action |
|---------|--------|-----------------|
| AC-2 | New enhancements: AC-2(12) Account monitoring for atypical usage; AC-2(13) Disable accounts for high-risk individuals | Add narrative for organizations at Moderate+ |
| AC-4 | Added emphasis on cross-domain and data flow enforcement | Review and update narrative |
| AC-6 | AC-6(10) updated: Prohibit non-privileged users from executing privileged functions (existed in Rev 4; language refined in Rev 5) | Review and update narrative |
| AC-17 | Restructured remote access requirements | Review and align with new structure |
| AC-20 | Expanded to address personally owned devices more explicitly | Update BYOD-related narrative |

### AU Family Changes
| Control | Change | Migration Action |
|---------|--------|-----------------|
| AU-2 | Simplified — no longer requires event types by control | Review and simplify narrative |
| AU-6 | Enhanced correlation requirements | Update analysis/review narrative |
| AU-12 | Added session audit requirements | Verify implementation covers sessions |

### CA Family Changes
| Control | Change | Migration Action |
|---------|--------|-----------------|
| CA-2 | Added continuous assessment emphasis | Update assessment approach |
| CA-7 | Significantly expanded continuous monitoring requirements | Review and align with new sub-parts |
| CA-8 | Penetration testing — restructured | Review scope and methodology |
| CA-9 | Internal system connections (new scope) | Document internal connections |

### CM Family Changes
| Control | Change | Migration Action |
|---------|--------|-----------------|
| CM-2 | Baseline configuration — expanded to include development | Extend coverage |
| CM-8 | Inventory now explicitly includes IoT and OT | Update inventory scope |
| CM-12 | Information location (new) | Document where CUI/PII resides |
| CM-13 | Data action mapping (new) | Map data processing activities |
| CM-14 | Signed components (new) | Document component signing |

### IA Family Changes
| Control | Change | Migration Action |
|---------|--------|-----------------|
| IA-2 | MFA enhancements restructured | Map old enhancements to new structure |
| IA-8 | Non-organizational user identification expanded | Update for modern federation patterns |
| IA-12 | Identity proofing (new) | Add identity proofing narrative |
| IA-13 | Identity providers (new) | Document IdP relationships |

### IR Family Changes
| Control | Change | Migration Action |
|---------|--------|-----------------|
| IR-4 | Added automation and correlation emphasis | Update incident handling narrative |
| IR-8 | IR plan now requires more specific elements | Verify IRP completeness |

### RA Family Changes
| Control | Change | Migration Action |
|---------|--------|-----------------|
| RA-3 | Expanded risk assessment scope | Update risk assessment methodology |
| RA-5 | Vulnerability monitoring (continuous emphasis) | Update scanning narrative |
| RA-7 | Risk response (new) | Document risk response process |
| RA-9 | Criticality analysis (new) | Document critical asset analysis |
| RA-10 | Threat hunting (new) | Document hunting activities if applicable |

### SA Family Changes
| Control | Change | Migration Action |
|---------|--------|-----------------|
| SA-8 | Significantly expanded security engineering | Review development practices |
| SA-12 | Withdrawn — moved to SR family | Migrate narrative to SR controls |
| SA-15 | Development process/standards expanded | Update SDLC documentation |
| SA-17 | Developer security and privacy architecture (expanded) | Review and update architecture practices |

### SC Family Changes
| Control | Change | Migration Action |
|---------|--------|-----------------|
| SC-7 | Boundary protection — added zero trust concepts | Update boundary narrative |
| SC-8 | Transmission confidentiality expanded | Review encryption coverage |
| SC-28 | Protection at rest — separated from confidentiality | Update encryption narrative |
| SC-45 through SC-51 | Multiple new controls | Assess applicability |

### SI Family Changes
| Control | Change | Migration Action |
|---------|--------|-----------------|
| SI-4 | Monitoring significantly expanded | Update monitoring narrative |
| SI-7 | Software integrity expanded | Update integrity verification |
| SI-19 | De-identification (new, privacy) | Document de-identification if PII processed |
| SI-20 | Tainting (new) | Assess applicability |
| SI-21 through SI-23 | New controls | Assess applicability |

## Baseline Changes (Rev 4 → Rev 5)

### Controls Added to Low Baseline
These controls were NOT in Rev 4 (SR family did not exist) but ARE in Rev 5 Low:

| Control | Title | Family |
|---------|-------|--------|
| SR-1 | Supply Chain RM Policy | SR (new family) |
| SR-2 | SCRM Plan | SR |
| SR-3 | Supply Chain Controls | SR |
| SR-5 | Acquisition Strategies | SR |
| SR-8 | Notification Agreements | SR |
| SR-10 | Inspection of Systems or Components | SR |
| SR-11 | Component Authenticity | SR |
| SR-12 | Component Disposal | SR |
| RA-7 | Risk Response | RA |

### Controls Added to Moderate Baseline
These controls were NOT in Rev 4 Moderate but ARE in Rev 5 Moderate (in addition to all Low baseline controls above):

| Control | Title | Family |
|---------|-------|--------|
| SR-6 | Supplier Assessments | SR |
| RA-9 | Criticality Analysis | RA |

**Note**: PT-1 through PT-8 are allocated to the **Privacy baseline** in SP 800-53B, not to the Low/Moderate/High security baselines (see the PT family section above). FedRAMP may include selected PT controls in its security baselines as additional requirements.

### Controls Removed from Moderate Baseline
Some controls were removed from Moderate but remain available as tailoring options:

| Control | Title | Reason |
|---------|-------|--------|
| Various PM controls | Program Management | Restructured; some moved to non-baseline |

## FedRAMP Rev 5 Transition

### FedRAMP-Specific Considerations
- FedRAMP baselines were updated to align with Rev 5
- FedRAMP Rev 5 baselines include additional FedRAMP-specific parameters
- Existing CSPs must transition to Rev 5 (timeline set by FedRAMP PMO)
- New authorizations must use Rev 5

### Transition Timeline
- FedRAMP published Rev 5 baselines
- Existing CSPs given transition period (typically 1 year from announcement)
- Annual assessments during transition should note Rev 4 → Rev 5 mapping
- All new SSPs must be authored to Rev 5

### Transition Steps
1. **Gap analysis**: Compare current Rev 4 SSP to Rev 5 requirements
2. **Identify new controls**: PT and SR families, plus new controls in existing families
3. **Map withdrawn controls**: Migrate narratives to incorporating controls
4. **Update ODPs**: Rev 5 may have different parameter requirements
5. **Update SSP structure**: Align sections with Rev 5 template
6. **Implement new controls**: SR and PT may require new processes
7. **Update assessment procedures**: Align with 800-53A Rev 5
8. **Submit updated package**: SSP, SAP, POA&M per FedRAMP guidance

## Quick Lookup: Rev 4 Control → Rev 5 Equivalent

For controls that were renumbered, restructured, or moved:

| Rev 4 | Rev 5 | Change Type |
|-------|-------|-------------|
| SA-12 | SR-1 through SR-12 | Expanded to full family |
| SA-18 | SR-9 | Moved |
| SA-19 | SR-11 | Moved |
| SA-20 | SA-8 | Incorporated |
| SA-21 | SA-4, PS-7 | Split |
| AC-13 | AC-2, AU-6 | Incorporated |
| AC-15 | MP-3 | Incorporated |
| SC-14 | AC-2, AC-3, SC-7 | Distributed |
| Appendix J (privacy) | PT-1 through PT-8 | New family |

**For all other controls**: The control ID remains the same between Rev 4 and Rev 5, but the control text, parameters, and enhancements may have changed. Always compare the specific control text.
