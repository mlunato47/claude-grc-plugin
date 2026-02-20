# Blowing Up RMF — Implementation Plan

> Mapping the "Blowing Up RMF" workshop vision to concrete engineering work in the claude-grc-plugin. Every section traces back to a specific pain point or future-state goal from the workshop board.

---

## Workshop Themes → Engineering Translation

### Pain Points Identified

| # | Pain Point | Root Cause | Plugin Response |
|---|-----------|------------|-----------------|
| 1 | RMF results are not even valuable | Compliance artifacts exist for auditors, not operators | **Risk Dashboard** — surface risk posture, not control counts |
| 2 | Too many controls, not another POAM | Flat control lists with no prioritization | **Threat-Aligned Scoring** — rank controls by mission impact, not alphabetically |
| 3 | 100% compliance ≠ secure system | Checklist mentality, no threat modeling | **Risk Quantification Engine** — score residual risk independent of compliance % |
| 4 | No consistent way to evaluate risk | Every team invents their own risk math | **Standardized Risk Model** — FAIR-lite scoring baked into the knowledge graph |
| 5 | Stop separating systems when discussing risk | Authorization boundaries silo risk view | **Enterprise Risk Aggregation** — cross-system risk roll-up |
| 6 | Not well aligned to threats | Controls selected by baseline, not by threat landscape | **Threat-to-Control Mapping Plane** — ATT&CK ↔ NIST control mapping |
| 7 | Assessors do not understand mission | Assessors check boxes without operational context | **Mission Context Layer** — encode mission criticality, data sensitivity, operational tempo |
| 8 | Lacking culture, workforce, skillset context | RMF ignores organizational readiness | **Maturity & Readiness Scoring** — organizational capability overlay |
| 9 | No new money for cyber | Budget constraints demand efficiency | **Inheritance Maximizer** — automatically identify every inheritable control to reduce work |
| 10 | RMF may not require our old RMF work | Framework versions evolve, old work may carry over | **Delta Analyzer** — diff framework versions, identify carry-forward vs. new work |

### Future State Goals

| # | Goal | Plugin Feature |
|---|------|---------------|
| F1 | Automated decision-making | **Decision Engine** — given system context, auto-recommend baseline, controls, inheritance |
| F2 | No need to push paper | **OSCAL-Native Pipeline** — machine-readable artifacts, no more Word/Excel |
| F3 | Use what we already have | **Evidence Reuse Engine** — map existing evidence to new framework requirements |
| F4 | Less money spent | **Cost-to-Compliance Calculator** — estimate effort per control, optimize ordering |
| F5 | Everything in one dashboard | **Unified Risk Dashboard** — single-pane view across systems, frameworks, threats |
| F6 | Data feeds, not checklists | **Live Data Connectors** — ingest scan results, SIEM alerts, CMDB data |
| F7 | Risk is measured and informs operations | **Operational Risk Score** — real-time risk metric that operators (not just auditors) use |
| F8 | Real-time behavioral analysis | **Behavioral Telemetry Plane** — model people/computer/network behavior patterns |
| F9 | Traceability: capability → cost → mission risk | **Mission Risk Traceability Chain** — full path from capability to cost to risk impact |
| F10 | Prediction of failures | **Predictive Analytics** — identify controls likely to fail based on patterns |

---

## Architecture Evolution

### Current State (v1.0)

```
┌─────────────────────────────────────────────────────┐
│  SKILL.md (system prompt)                           │
│  ├── frameworks/ (15 framework reference docs)      │
│  ├── mappings/ (9 cross-framework crosswalks)       │
│  ├── audits/ (14 audit procedure docs)              │
│  ├── conmon/ (6 continuous monitoring docs)          │
│  ├── dod/ (ATO engine + 6 tech playbooks)           │
│  ├── tooling/ (1 tooling reference)                 │
│  └── graph/ (KG: 1114 nodes, ~5000 edges)           │
│      ├── schema.json (4-layer architecture)         │
│      ├── nodes.json                                 │
│      ├── edges.json                                 │
│      └── pathrag.md                                 │
├─────────────────────────────────────────────────────┤
│  tools/visualize/ (React+Vite KG viewer + chat)     │
└─────────────────────────────────────────────────────┘
```

**Strengths**: Deep framework knowledge, typed KG with PathRAG, cross-framework mapping, DoD ATO engine, interactive graph viewer with AI chat.

**Gaps (per workshop)**: No threat alignment, no risk quantification, no mission context, no live data ingestion, no dashboard, no OSCAL pipeline, no evidence reuse, no predictive analytics.

### Target State (v2.0)

```
┌──────────────────────────────────────────────────────────────────┐
│  KNOWLEDGE LAYER (enhanced SKILL.md + expanded graph)            │
│  ├── Existing: frameworks, mappings, audits, conmon, dod         │
│  ├── NEW: threat-intelligence/ (ATT&CK integration)              │
│  ├── NEW: risk-models/ (FAIR-lite, mission risk)                 │
│  └── graph/ (expanded KG)                                        │
│      ├── NEW node types: Threat, ThreatGroup, Technique,         │
│      │   MissionCapability, System, Organization, DataFeed       │
│      ├── NEW planes: PLANE-THREAT, PLANE-MISSION, PLANE-RISK    │
│      └── NEW predicates: MITIGATES, EXPLOITS, TARGETS,           │
│          SUPPORTS_MISSION, HAS_RISK_SCORE, FEEDS_DATA            │
├──────────────────────────────────────────────────────────────────┤
│  DECISION ENGINE (new)                                           │
│  ├── risk-scorer/ (quantitative risk calculation)                │
│  ├── inheritance-optimizer/ (maximize control reuse)             │
│  ├── delta-analyzer/ (framework version diff)                    │
│  └── cost-estimator/ (effort per control family)                 │
├──────────────────────────────────────────────────────────────────┤
│  DATA INTEGRATION LAYER (new)                                    │
│  ├── oscal/ (OSCAL read/write/validate)                          │
│  ├── connectors/ (scan ingest, SIEM, CMDB schemas)              │
│  └── evidence-mapper/ (reuse existing evidence across frameworks)│
├──────────────────────────────────────────────────────────────────┤
│  DASHBOARD (enhanced visualize/)                                 │
│  ├── Existing: KG viewer, AI chat                                │
│  ├── NEW: Risk heatmap (system × control family)                 │
│  ├── NEW: Threat coverage view (ATT&CK overlay)                  │
│  ├── NEW: Mission traceability tree                              │
│  ├── NEW: Compliance vs. Risk scatter plot                       │
│  └── NEW: Evidence coverage & gap analysis                       │
└──────────────────────────────────────────────────────────────────┘
```

---

## Implementation Phases

### Phase 1: Threat-Aligned Knowledge Graph (Pain Points 3, 6, 7 | Goals F7)

**The single biggest workshop complaint: compliance ≠ security because controls aren't aligned to threats.**

#### 1A. MITRE ATT&CK Integration into the Knowledge Graph

Add new node types and a PLANE-THREAT to the graph schema:

**New node types:**
```json
{
  "Technique": {
    "description": "A MITRE ATT&CK technique or sub-technique",
    "id_pattern": "ATT-{TACTIC}-{TECHNIQUE-ID}",
    "required_properties": ["label", "tactic", "platform", "data_sources"]
  },
  "ThreatGroup": {
    "description": "A known threat actor group (APT, cybercrime, hacktivist)",
    "id_pattern": "THREAT-{GROUP-ID}",
    "required_properties": ["label", "aliases", "target_sectors"]
  },
  "Tactic": {
    "description": "A MITRE ATT&CK tactic (the adversary's goal)",
    "id_pattern": "TACTIC-{ID}",
    "required_properties": ["label", "kill_chain_phase"]
  }
}
```

**New predicates:**
```json
{
  "MITIGATES": {
    "description": "Control mitigates a specific ATT&CK technique",
    "valid_pairs": [{"subject": "Control", "object": "Technique"}],
    "meta_fields": ["effectiveness", "coverage_type"]
  },
  "USES_TECHNIQUE": {
    "description": "Threat group uses a specific technique",
    "valid_pairs": [{"subject": "ThreatGroup", "object": "Technique"}]
  },
  "PART_OF_TACTIC": {
    "description": "Technique belongs to a tactic",
    "valid_pairs": [{"subject": "Technique", "object": "Tactic"}]
  }
}
```

**New plane:**
```json
{
  "PLANE-THREAT": {
    "description": "Threat landscape overlay — ATT&CK techniques mapped to controls",
    "predicates_allowed": ["MITIGATES", "USES_TECHNIQUE", "PART_OF_TACTIC"],
    "traversal_strategy": "neighborhood_bfs"
  }
}
```

**New PathRAG templates:**
- `threat_coverage_v1`: Control → MITIGATES → Technique → USES_TECHNIQUE → ThreatGroup — "Which threat groups does AC-2 help defend against?"
- `gap_analysis_v1`: ThreatGroup → USES_TECHNIQUE → Technique → (missing MITIGATES) → "What techniques used by APT29 have no control coverage?"

**Data source:** MITRE ATT&CK STIX bundles (enterprise-attack.json). Seed ~200 techniques, ~14 tactics, ~130 threat groups. NIST provides an official ATT&CK-to-800-53 mapping (NIST SP 800-53 Rev 5 → ATT&CK mapping project).

**Files to create/modify:**
- `graph/schema.json` — add node types, predicates, plane, templates
- `graph/nodes.json` — add Technique, Tactic, ThreatGroup nodes
- `graph/edges.json` — add MITIGATES, USES_TECHNIQUE, PART_OF_TACTIC edges
- `tools/seed_attack.py` — new seeder script to parse ATT&CK STIX → graph nodes/edges
- `grc/skills/grc-knowledge/threat-intelligence/attack-overview.md` — ATT&CK reference doc
- `grc/skills/grc-knowledge/threat-intelligence/control-to-attack-mapping.md` — mapping methodology doc

#### 1B. Threat-Prioritized Control Scoring

Add a `threat_relevance_score` to each Control node:

```
threat_relevance = (# of techniques mitigated × avg technique prevalence) / total_techniques_in_baseline
```

This lets the plugin answer: "Which 20 controls in FedRAMP Moderate would stop the most ATT&CK techniques?" — replacing the alphabetical control list with a **threat-ranked priority list**.

**Files to modify:**
- `graph/schema.json` — add scoring model
- `graph/pathrag.md` — add threat-weighted path scoring
- `grc/skills/grc-knowledge/SKILL.md` — add threat-alignment section and commands

**Estimated graph growth:** ~350 new nodes, ~2,500 new edges.

---

### Phase 2: Risk Quantification Engine (Pain Points 1, 3, 4, 5 | Goals F5, F7, F9)

**Workshop demand: "Risk is measured and informs operations." Replace subjective L/M/H with quantified scores.**

#### 2A. FAIR-Lite Risk Model in the Graph

Add a risk scoring layer that computes quantitative risk per control, per system:

**New node types:**
```json
{
  "RiskScenario": {
    "description": "A specific risk scenario combining threat, vulnerability, and asset",
    "id_pattern": "RISK-{ID}",
    "required_properties": ["label", "threat_event_frequency", "loss_magnitude", "risk_score"]
  },
  "MissionCapability": {
    "description": "A mission function that depends on systems and controls",
    "id_pattern": "MISSION-{ID}",
    "required_properties": ["label", "criticality", "owner"]
  }
}
```

**New predicates:**
```json
{
  "HAS_RISK": {
    "description": "Control or system has a quantified risk scenario",
    "valid_pairs": [
      {"subject": "Control", "object": "RiskScenario"},
      {"subject": "MissionCapability", "object": "RiskScenario"}
    ]
  },
  "SUPPORTS_MISSION": {
    "description": "Control or system supports a mission capability",
    "valid_pairs": [
      {"subject": "Control", "object": "MissionCapability"}
    ]
  }
}
```

**New plane:**
```json
{
  "PLANE-MISSION": {
    "description": "Mission traceability — capabilities, systems, controls, risk",
    "predicates_allowed": ["SUPPORTS_MISSION", "HAS_RISK"],
    "traversal_strategy": "neighborhood_bfs"
  }
}
```

**Risk calculation model (FAIR-lite):**
```
Risk = Threat Event Frequency × Vulnerability × Loss Magnitude
     = TEF × (1 - Control Effectiveness) × (Mission Criticality × Data Sensitivity × Exposure)
```

- **TEF**: Derived from ATT&CK technique prevalence (Phase 1 data)
- **Control Effectiveness**: Derived from implementation status + evidence freshness
- **Loss Magnitude**: Derived from mission criticality × data sensitivity
- **Output**: Numerical risk score (0-100) per RiskScenario, aggregatable up to system and enterprise level

**New PathRAG template:**
- `mission_risk_chain_v1`: MissionCapability → SUPPORTS_MISSION ← Control → MITIGATES → Technique — "What is the mission risk if AC-2 is not implemented?"

**Files to create/modify:**
- `graph/schema.json` — add risk model, new node types, predicates, plane
- `grc/skills/grc-knowledge/risk-models/fair-lite.md` — FAIR-lite methodology reference
- `grc/skills/grc-knowledge/risk-models/mission-risk-scoring.md` — mission risk scoring guide
- `tools/risk_calculator.py` — compute risk scores from graph data

#### 2B. "Compliance ≠ Security" Visualization

Add a scatter plot to the dashboard: X-axis = compliance % (controls implemented), Y-axis = residual risk score. Systems that are 100% compliant but high-risk are **immediately visible** in the upper-right quadrant.

**Files to create/modify:**
- `tools/visualize/app/src/components/RiskDashboard.tsx` — new dashboard component
- `tools/visualize/app/src/components/ComplianceVsRiskChart.tsx` — scatter plot
- `tools/visualize/app/src/hooks/useRiskData.ts` — risk data hook

---

### Phase 3: Inheritance Maximizer & Evidence Reuse (Pain Points 2, 9 | Goals F3, F4)

**Workshop demand: "Use what we already have." "Less money spent." "No new money for cyber."**

#### 3A. Inheritance Optimizer

Build an engine that, given a system's hosting platform and Impact Level, automatically identifies every control that can be inherited or shared — maximizing reuse and minimizing original work.

**How it works:**
1. User provides: platform (e.g., AWS GovCloud), IL (e.g., IL4), baseline (e.g., FedRAMP Moderate)
2. Engine traverses PLANE-RESPONSIBILITY to resolve inheritance chains
3. Engine cross-references the `dod/ato-engine/inheritance-matrix.md` data
4. Output: Three lists — **Inherited** (no work needed), **Shared** (partial work), **Residual** (full work)
5. Each list includes estimated effort (hours) and evidence requirements

**Files to create/modify:**
- `grc/skills/grc-knowledge/SKILL.md` — add inheritance optimizer section and commands
- `tools/inheritance_optimizer.py` — computation engine
- Enhance existing `dod/ato-engine/inheritance-matrix.md` data with per-control granularity

#### 3B. Evidence Reuse Engine

Build an engine that maps existing evidence artifacts to requirements across multiple frameworks:

**How it works:**
1. User provides: list of existing evidence artifacts (or framework already achieved)
2. Engine traverses PLANE-EVIDENCE + PLANE-MAPPING to find all controls satisfied by that evidence
3. Output: For each target framework, a list of controls already covered by existing evidence and what gaps remain

**Example:** "We have SOC 2 Type II. What FedRAMP Moderate controls does our existing evidence already cover?"

**Files to create/modify:**
- `grc/skills/grc-knowledge/SKILL.md` — add evidence reuse section
- `tools/evidence_reuse.py` — cross-framework evidence mapping
- `graph/edges.json` — ensure evidence edges are comprehensive across frameworks

#### 3C. Cost-to-Compliance Estimator

Add `estimated_effort_hours` metadata to control nodes, broken down by implementation type (inherited/shared/system-specific). This enables:
- "How many hours to achieve FedRAMP Moderate on AWS GovCloud?" → sum of residual control efforts
- "We already have SOC 2 — how much additional work for ISO 27001?" → delta effort after evidence reuse

**Files to modify:**
- `graph/nodes.json` — add effort metadata to Control nodes
- `graph/schema.json` — document effort metadata fields
- `grc/skills/grc-knowledge/SKILL.md` — add cost estimation section

---

### Phase 4: Framework Delta Analyzer (Pain Point 10 | Goal F3)

**Workshop insight: "RMF may not require our old RMF work" — versions evolve, carry-forward matters.**

#### 4A. Version Diff Engine

Build a tool that diffs two versions of a framework and produces:
- **Carried forward**: Controls that exist in both versions (no rework)
- **Modified**: Controls that changed (review and update needed)
- **Withdrawn**: Controls removed in new version (can archive)
- **New**: Controls added in new version (net new work)

**Priority diffs:**
- NIST 800-53 Rev 4 → Rev 5 (already have prose doc, now formalize in graph)
- FedRAMP Rev 4 → Rev 5
- PCI DSS v3.2.1 → v4.0.1
- ISO 27001:2013 → 2022

**Implementation:**
Add `SUPERSEDES` edges between framework versions (schema already supports this predicate). Build a traversal template that walks SUPERSEDES + MAPS_TO to identify carry-forward.

**Files to create/modify:**
- `tools/delta_analyzer.py` — version diff engine
- `graph/nodes.json` — add version-pair nodes where needed
- `graph/edges.json` — add SUPERSEDES edges between control versions
- `grc/skills/grc-knowledge/SKILL.md` — add delta analysis section

---

### Phase 5: OSCAL-Native Pipeline (Goal F2)

**Workshop demand: "No need to push paper." "Admin by the bot, not by the person."**

#### 5A. OSCAL Document Generation

Build OSCAL SSP/POA&M/Component Definition generation from the knowledge graph:

**How it works:**
1. User describes system (platform, IL, boundary, services)
2. Engine selects baseline, resolves inheritance, maps controls
3. Generates OSCAL JSON artifacts (SSP skeleton, component definitions, POA&M template)
4. Output is machine-readable, importable to eMASS/RegScale/Telos

**OSCAL models to support:**
- `oscal-ssp` — System Security Plan
- `oscal-poam` — Plan of Action & Milestones
- `oscal-component-definition` — Reusable component control implementations
- `oscal-assessment-results` — For ingesting scan/assessment data

**Files to create/modify:**
- `grc/skills/grc-knowledge/oscal/` — new directory
- `grc/skills/grc-knowledge/oscal/ssp-generator.md` — SSP generation guide
- `grc/skills/grc-knowledge/oscal/oscal-schemas.md` — schema reference
- `tools/oscal_generator.py` — OSCAL document builder
- `grc/skills/grc-knowledge/SKILL.md` — add OSCAL section

#### 5B. OSCAL Validation & Import

Build OSCAL validation that checks generated documents against FedRAMP OSCAL constraints and validates schema compliance.

**Files to create/modify:**
- `tools/oscal_validator.py` — schema + FedRAMP constraint validation

---

### Phase 6: Live Data Connectors & Continuous Monitoring Dashboard (Goals F5, F6, F8)

**Workshop demand: "Data feeds, not checklists." "Everything in one dashboard." "Real-time behavioral analysis."**

#### 6A. Connector Schema Definitions

Define standardized ingest schemas for common security tool outputs:

| Connector | Data Source | Graph Impact |
|-----------|-----------|--------------|
| Vulnerability Scanner | Nessus/Qualys CSV/JSON | Creates Finding nodes → HAS_FINDING edges to Controls |
| SIEM Alerts | Splunk/Sentinel JSON | Creates Alert nodes → DETECTED_BY edges to Techniques |
| CMDB/Asset Inventory | ServiceNow/Axonius | Creates Asset nodes → RUNS_ON edges to Systems |
| SCAP Compliance | XCCDF results XML | Updates Control implementation status |
| Patch Status | WSUS/Automox | Updates SI-2 related risk scores |

**New node types:**
```json
{
  "Finding": {
    "description": "A vulnerability finding from a scanner",
    "id_pattern": "FINDING-{CVE-or-ID}",
    "required_properties": ["label", "severity", "cvss", "source", "timestamp"]
  },
  "Asset": {
    "description": "A system component within an authorization boundary",
    "id_pattern": "ASSET-{ID}",
    "required_properties": ["label", "asset_type", "boundary"]
  }
}
```

**Files to create/modify:**
- `grc/skills/grc-knowledge/connectors/` — new directory
- `grc/skills/grc-knowledge/connectors/ingest-schemas.md` — connector schema reference
- `grc/skills/grc-knowledge/connectors/vuln-scanner.md` — vulnerability scanner integration
- `grc/skills/grc-knowledge/connectors/siem-alerts.md` — SIEM alert integration
- `tools/ingest_scan.py` — vulnerability scan ingest tool
- `graph/schema.json` — add Finding, Asset node types and predicates

#### 6B. Unified Risk Dashboard

Extend the existing React visualizer into a full risk dashboard with multiple views:

**View 1 — Risk Heatmap:**
Matrix of systems (rows) × control families (columns), cells colored by risk score. Immediately shows where risk concentrates.

**View 2 — ATT&CK Coverage Map:**
ATT&CK matrix overlay showing which techniques are mitigated (green), partially mitigated (yellow), or uncovered (red) by the current control set.

**View 3 — Mission Traceability Tree:**
Tree visualization: Mission Capability → Supporting Systems → Controls → Evidence → Findings. Full traceability from "why we care" to "what we found."

**View 4 — Compliance Timeline:**
Gantt-style view of ConMon deliverables, upcoming milestones, POA&M due dates, and assessment schedules.

**View 5 — Evidence Freshness:**
Grid showing each control's evidence age. Stale evidence (>90 days) highlighted red. Enables "continuous authorization" monitoring.

**Files to create/modify:**
- `tools/visualize/app/src/components/RiskHeatmap.tsx`
- `tools/visualize/app/src/components/AttackCoverageMap.tsx`
- `tools/visualize/app/src/components/MissionTraceTree.tsx`
- `tools/visualize/app/src/components/ComplianceTimeline.tsx`
- `tools/visualize/app/src/components/EvidenceFreshness.tsx`
- `tools/visualize/app/src/components/DashboardLayout.tsx` — tab/view switcher
- `tools/visualize/app/src/hooks/useRiskData.ts`
- `tools/visualize/app/src/hooks/useThreatData.ts`
- `tools/visualize/app/src/App.tsx` — integrate dashboard views

---

### Phase 7: Predictive Analytics & Organizational Readiness (Pain Points 7, 8 | Goals F8, F10)

**Workshop demand: "Prediction of failures." "Lacking culture, workforce, operational context."**

#### 7A. Control Failure Predictor

Build a scoring model that predicts which controls are most likely to fail at next assessment:

**Signals:**
- Evidence age (stale evidence → likely failure)
- POA&M history (repeated open findings on same control → systemic issue)
- Scan trend (vulnerability count increasing in control's domain → degradation)
- Implementation type (manual controls fail more than automated)
- Personnel turnover (controls owned by departed staff → risk)

**Output:** Ranked list of "controls at risk of failure" with contributing factors and recommended actions.

**Files to create/modify:**
- `grc/skills/grc-knowledge/risk-models/failure-prediction.md` — prediction methodology
- `tools/failure_predictor.py` — prediction engine
- `tools/visualize/app/src/components/FailurePrediction.tsx` — dashboard widget

#### 7B. Organizational Readiness Scorer

Score an organization's readiness across dimensions that RMF ignores:

| Dimension | Indicators | Score Range |
|-----------|-----------|-------------|
| **Culture** | Security awareness training completion, phishing test results, incident reporting rate | 0-100 |
| **Workforce** | ISSO/ISSM staffing ratio, certifications held, turnover rate | 0-100 |
| **Process Maturity** | POA&M closure rate, evidence automation %, policy review currency | 0-100 |
| **Tooling** | Scanner coverage %, SIEM coverage %, automation level | 0-100 |
| **Operational Tempo** | Change frequency, deployment cadence, incident response time | 0-100 |

**Composite Readiness Score** = weighted average across dimensions.

This directly addresses "assessors don't understand mission" — by giving assessors a readiness profile alongside the compliance package.

**Files to create/modify:**
- `grc/skills/grc-knowledge/risk-models/readiness-scoring.md` — methodology
- `grc/skills/grc-knowledge/SKILL.md` — add readiness scoring section

---

## New Plugin Commands Summary

| Command | Phase | Description |
|---------|-------|-------------|
| `/grc:threat-map <control>` | 1 | Show ATT&CK techniques mitigated by a control |
| `/grc:threat-gap <threat-group>` | 1 | Identify control gaps for a specific threat group |
| `/grc:threat-rank <baseline>` | 1 | Rank controls by threat relevance score |
| `/grc:risk-score <control-or-system>` | 2 | Compute quantitative risk score |
| `/grc:mission-trace <capability>` | 2 | Trace mission capability → controls → risk |
| `/grc:inherit <platform> <IL> <baseline>` | 3 | Compute inherited/shared/residual control breakdown |
| `/grc:evidence-reuse <source-framework> <target-framework>` | 3 | Map evidence coverage across frameworks |
| `/grc:estimate-effort <target-framework> [--from <existing>]` | 3 | Estimate hours to achieve compliance |
| `/grc:delta <framework> <old-version> <new-version>` | 4 | Diff framework versions |
| `/grc:oscal-gen <type> [--system <context>]` | 5 | Generate OSCAL SSP/POA&M/Component artifacts |
| `/grc:oscal-validate <file>` | 5 | Validate OSCAL document against schema + FedRAMP |
| `/grc:ingest <scan-type> <file>` | 6 | Ingest scan results into the graph |
| `/grc:predict-failures [--system <name>]` | 7 | Predict controls likely to fail |
| `/grc:readiness-score` | 7 | Compute organizational readiness score |

---

## Graph Schema Evolution Summary

### New Node Types (Phases 1-6)

| Node Type | Phase | Count Estimate | Source |
|-----------|-------|---------------|--------|
| Technique | 1 | ~200 | MITRE ATT&CK Enterprise |
| Tactic | 1 | 14 | MITRE ATT&CK Enterprise |
| ThreatGroup | 1 | ~130 | MITRE ATT&CK Enterprise |
| RiskScenario | 2 | ~500 | Generated from TEF × Control × Mission |
| MissionCapability | 2 | ~20 | User-defined per organization |
| Finding | 6 | Variable | Ingested from scan tools |
| Asset | 6 | Variable | Ingested from CMDB |

### New Predicates (Phases 1-6)

| Predicate | Phase | Plane | Est. Edges |
|-----------|-------|-------|------------|
| MITIGATES | 1 | PLANE-THREAT | ~1,500 |
| USES_TECHNIQUE | 1 | PLANE-THREAT | ~3,000 |
| PART_OF_TACTIC | 1 | PLANE-THREAT | ~200 |
| HAS_RISK | 2 | PLANE-MISSION | ~500 |
| SUPPORTS_MISSION | 2 | PLANE-MISSION | ~200 |
| HAS_FINDING | 6 | PLANE-EVIDENCE | Variable |
| RUNS_ON | 6 | PLANE-RESPONSIBILITY | Variable |

### New Planes

| Plane | Phase | Purpose |
|-------|-------|---------|
| PLANE-THREAT | 1 | ATT&CK techniques ↔ controls ↔ threat groups |
| PLANE-MISSION | 2 | Mission capabilities ↔ controls ↔ risk scenarios |

---

## Priority Order & Dependencies

```
Phase 1 ──→ Phase 2 ──→ Phase 3 ──→ Phase 4
  │              │                       │
  │              └───────→ Phase 6 ──────┘
  │                            │
  └──────────────→ Phase 5     └──→ Phase 7
```

- **Phase 1** (Threat Alignment) is foundational — Phase 2 risk scoring depends on threat data
- **Phase 2** (Risk Quantification) depends on Phase 1 for TEF data
- **Phase 3** (Inheritance/Evidence Reuse) can start after Phase 2 risk model exists
- **Phase 4** (Delta Analyzer) is independent, can be parallelized with Phase 3
- **Phase 5** (OSCAL) is independent, can be parallelized with any phase
- **Phase 6** (Dashboard/Connectors) depends on Phase 2 risk data + Phase 1 threat data
- **Phase 7** (Predictive/Readiness) requires Phase 6 live data + Phase 2 risk model

---

## Key Design Principles (From the Workshop)

1. **"Same data across tools"** — Single knowledge graph is the source of truth. All tools read from and write to the graph. No data silos.

2. **"Admin by the bot, not by the person"** — Every feature should automate what an ISSO currently does manually. The plugin recommends, the human approves.

3. **"Data feeds, not checklists"** — Replace static checklist mentality with live data ingestion. Controls are validated by evidence streams, not annual checkbox exercises.

4. **"100% compliance ≠ secure system"** — Every dashboard view shows BOTH compliance status AND risk score side by side. Never show compliance alone.

5. **"Traceability of capability, cost to mission risk"** — Full path from mission capability through controls through evidence to actual findings. Every decision is traceable.

6. **"No new money for cyber"** — Maximize inheritance, reuse evidence, automate generation. Every feature should reduce cost, not add it.

7. **"Compliance intent meets practice — prediction of failures"** — Don't just document what should happen; predict where it will break and focus attention there.
