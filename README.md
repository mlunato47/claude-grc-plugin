# GRC Knowledge Plugin for Claude Code

A Claude Code plugin that turns Claude into a senior GRC (Governance, Risk, and Compliance) analyst with a built-in DoD ATO acceleration engine. 87+ reference files covering 15 frameworks, 27 slash commands, a multi-plane Knowledge Graph with PathRAG traversal, and deep domain knowledge for federal, DoD, and commercial compliance work.

## What It Does

Load this plugin and Claude gains expertise in:

- **15 compliance frameworks** — NIST 800-53, FedRAMP, FISMA, CMMC, SOC 2, ISO 27001, PCI DSS, HIPAA, CIS Controls, COBIT, CSA CCM, GDPR, SLSA, OSCAL, and NIST Rev 4→5 transition
- **Cross-framework mapping** — Map any control to any other framework through NIST 800-53 as the hub
- **Knowledge Graph with PathRAG** — 284-node, 295-edge typed graph across four semantic planes (compliance, mapping, responsibility, evidence) with path-constrained retrieval and scored traversal
- **Document review** — Feed it SSP narratives, POA&Ms, policies, CRMs and get structural quality feedback with 0-5 maturity scoring
- **Operational workflows** — Significant change analysis, inheritance modeling, SAR responses, compliance calendars, tabletop exercises

It cites specific control IDs, knows baseline assignments, understands assessment procedures, and speaks the language of auditors, ISSOs, and compliance engineers.

## Install

### From a Plugin Marketplace (Recommended)

Add the marketplace and install:

```
/plugin marketplace add mlunato47/claude-grc-plugin
/plugin install grc@mlunato47
```

Or from the CLI:

```bash
claude plugin install grc@mlunato47
```

You can install at different scopes:

```bash
claude plugin install grc@mlunato47                  # User scope (all projects)
claude plugin install grc@mlunato47 --scope project  # Project scope (shared via git)
claude plugin install grc@mlunato47 --scope local    # Local only
```

### From a Local Directory

Clone the repo and load directly:

```bash
git clone https://github.com/mlunato47/claude-grc-plugin.git
claude --plugin-dir ./grc-plugin/grc
```

Or load alongside other plugins:

```bash
claude --plugin-dir ./grc-plugin/grc --plugin-dir ./other-plugin
```

Once loaded, type `/grc:` to see all available commands.

## Commands

### Framework & Controls

| Command | Purpose |
|---------|---------|
| `/grc:control-lookup` | Look up controls by framework and ID or keyword |
| `/grc:map-controls` | Map controls between any two frameworks |
| `/grc:conmon-guide` | Continuous monitoring guidance by topic |
| `/grc:audit-prep` | Audit preparation checklists by audit type |
| `/grc:poam-help` | POA&M creation, templates, and metrics |
| `/grc:gap-analysis` | Structured gap analysis worksheets |
| `/grc:ssp-section` | Draft SSP narrative language by control family |
| `/grc:deviation-request` | Draft deviation/risk acceptance documentation |

### Document Review & Analysis

| Command | Purpose |
|---------|---------|
| `/grc:review-narrative` | Review SSP control narratives — Five W's, ODPs, 0-5 maturity score |
| `/grc:review-ssp` | Validate SSP structure against FedRAMP template |
| `/grc:review-poam` | Check POA&M entries for field completeness and SLA compliance |
| `/grc:review-policy` | Review policy structure, control coverage, and language quality |
| `/grc:review-crm` | Review CRM coverage, responsibility clarity, and common gaps |
| `/grc:score-maturity` | Score control implementation maturity 0-5 with next-level guidance |
| `/grc:evidence-checklist` | Generate audit evidence prep checklists (no user content needed) |

### Knowledge Graph

| Command | Purpose |
|---------|---------|
| `/grc:graph-query` | Natural language compliance questions answered via Knowledge Graph traversal |
| `/grc:graph-traverse` | PathRAG traversal from a control across planes — mapping, evidence, responsibility |

### DoD ATO Engine

| Command | Purpose |
|---------|---------|
| `/grc:ato` | ATO acceleration engine — reads context, infers platform/IL/branch, outputs technology-specific sprint plan |
| `/grc:ato --gap` | Inheritance gap analysis only — what platform covers vs. what you own |
| `/grc:ato --path` | Critical path only — AO gate requirements and parallelization map |
| `/grc:ato --brief` | AO briefing structure for your branch and IL |
| `/grc:ato --conmon` | ConMon plan for post-ATO at your IL and branch |

Supports all DoD components (Army, Navy, Air Force, Marines, Space Force, SOCOM, DISA) and IL2 through IL6 across Platform One, AWS GovCloud, Azure Government, DISA MilCloud, Windows enclaves, and generic Kubernetes.

### Operational Workflows

| Command | Purpose |
|---------|---------|
| `/grc:significant-change` | Analyze if a system change is "significant" per FedRAMP |
| `/grc:inheritance` | Model control inheritance by service model (IaaS/PaaS/SaaS) |
| `/grc:sar-response` | Draft structured responses to SAR findings |
| `/grc:compliance-calendar` | Generate recurring compliance activity calendar |
| `/grc:boundary-guidance` | Authorization boundary definition guidance |
| `/grc:tabletop-scenario` | Generate IR/CP tabletop exercise scenarios |
| `/grc:multi-framework` | Analyze overlap and gaps across multiple frameworks |
| `/grc:oscal-guide` | OSCAL structure, readiness, and conversion guidance |
| `/grc:rev5-transition` | NIST 800-53 Rev 4 to Rev 5 transition mapping |

For detailed usage, examples, and tips for every command, see the [Usage Guide](GUIDE.md).

## Quick Examples

**Look up a control:**
```
/grc:control-lookup fedramp ac-2
```

**Map between frameworks:**
```
/grc:map-controls soc2 CC6.1 to iso27001
```

**Review a control narrative** (paste your narrative after the command):
```
/grc:review-narrative fedramp ac-2 moderate
```

**Check if a change is significant:**
```
/grc:significant-change fedramp Migrating database from EC2 to RDS
```

**Generate a compliance calendar:**
```
/grc:compliance-calendar fedramp,soc2
```

**Generate a tabletop exercise:**
```
/grc:tabletop-scenario ir ransomware saas
```

**Query the Knowledge Graph:**
```
/grc:graph-query What evidence do I need for AU-6?
```

**Traverse cross-framework mappings:**
```
/grc:graph-traverse CC6.1 --to ISO-27001
```

**Explore all planes for a control:**
```
/grc:graph-traverse AC-2 --plane all
```

## Data Sensitivity

GRC artifacts often contain CUI, PII, system architecture, and vulnerability data. This plugin is designed to be useful **without requiring sensitive specifics**:

- **Document review commands** display a redaction reminder before every response
- **All feedback is structural** — "your narrative is missing the frequency component" not "your system is insecure"
- **No security posture judgment** — the plugin assesses document quality, never system security
- **Safe to use with placeholders** — replace real names/IPs/agencies with `[Agency Name]`, `[System Name]`, `10.x.x.x`

Reference-only commands (`evidence-checklist`, `compliance-calendar`, `tabletop-scenario`, `oscal-guide`, `rev5-transition`, `multi-framework`, `graph-query`, `graph-traverse`) don't process user content and skip the reminder.

## Architecture

```
grc/
├── .claude-plugin/
│   └── plugin.json              # Plugin metadata
├── agents/
│   └── grc-researcher.md        # Read-only research agent
├── commands/                    # 26 slash commands
│   ├── control-lookup.md
│   ├── graph-query.md
│   ├── graph-traverse.md
│   ├── map-controls.md
│   ├── review-narrative.md
│   ├── significant-change.md
│   └── ...
├── skills/
│   └── grc-knowledge/
│       ├── SKILL.md             # Core skill definition (loaded into context)
│       ├── audits/              # 14 reference files
│       ├── conmon/              # 6 reference files
│       ├── frameworks/          # 16 reference files
│       ├── graph/               # Knowledge Graph (PathRAG)
│       │   ├── schema.json      # ERD, predicates, planes, templates, scoring
│       │   ├── nodes.json       # 284 nodes (frameworks, families, controls, ...)
│       │   ├── edges.json       # 295 edges across four semantic planes
│       │   └── pathrag.md       # Traversal rules, scoring formula, output format
│       ├── mappings/            # 9 reference files
│       └── tooling/             # 1 reference file
├── GUIDE.md                     # Usage guide
└── LICENSE                      # MIT
```

**How it works:**

- `SKILL.md` is loaded into Claude's context and provides the core GRC analyst persona, framework quick reference, and response guidelines
- Slash commands in `commands/` define the behavior, arguments, and output format for each command
- Reference files in `skills/grc-knowledge/` contain deep domain knowledge that commands read on demand
- The `grc-researcher` agent provides a read-only research interface for complex cross-reference queries
- NIST 800-53 serves as the universal mapping hub — any framework maps to any other through NIST
- The Knowledge Graph in `graph/` provides structured traversal across four semantic planes using PathRAG, with scored paths and evidence gating

## Frameworks Covered

| Framework | Version | Reference File |
|-----------|---------|---------------|
| NIST 800-53 | Rev 5 | `frameworks/nist-800-53.md` |
| FedRAMP | Rev 5 | `frameworks/fedramp.md` |
| FISMA | Current | `frameworks/fisma.md` |
| CMMC | 2.0 | `frameworks/cmmc.md` |
| SOC 2 | Current | `frameworks/soc2.md` |
| ISO 27001 | 2022 | `frameworks/iso-27001-27002.md` |
| PCI DSS | v4.0.1 | `frameworks/pci-dss-v4.md` |
| HIPAA | Current | `frameworks/hipaa.md` |
| CIS Controls | v8.1 | `frameworks/cis-controls-v8.md` |
| COBIT | 2019 | `frameworks/cobit-2019.md` |
| CSA CCM | v4 | `frameworks/csa-ccm-v4.md` |
| GDPR | Current | `frameworks/gdpr.md` |
| SLSA | v1.2 | `frameworks/slsa.md` |
| OSCAL | 1.1.2 | `frameworks/oscal-reference.md` |
| NIST Rev 4→5 | Transition | `frameworks/nist-rev4-to-rev5.md` |
| Supply Chain (SR) | Rev 5 | `frameworks/supply-chain-srm.md` |

## Knowledge Graph

The plugin includes a typed multi-plane Knowledge Graph with path-constrained retrieval (PathRAG). Instead of flat keyword search, compliance queries follow relational paths through a structured graph with scored results.

### Four-Layer Architecture

1. **Deterministic Control Plane (ERD)** — 284 nodes with strict entity types (Framework, ControlFamily, Control, Baseline, ServiceModel, EvidenceType) and cardinality constraints.
2. **Typed Multi-Plane KG** — 295 edges across four semantic planes:
   - **PLANE-COMPLIANCE** — Framework → Family → Control hierarchy
   - **PLANE-MAPPING** — Cross-framework equivalences via NIST 800-53 hub
   - **PLANE-RESPONSIBILITY** — IaaS/PaaS/SaaS control ownership chains
   - **PLANE-EVIDENCE** — Evidence and documentation requirements
3. **Path-Constrained Retrieval (PathRAG)** — Ordered predicate templates enforce traversal discipline with scoring: `score = avg(confidence) × geo_mean(edge_weights)`.
4. **Temporal Revision Layer** — Immutable graph snapshots with draft → published → archived lifecycle and content hash integrity.

### PathRAG Templates

| Template | Use Case |
|----------|----------|
| `compliance_chain_v1` | "What controls are in the AC family?" |
| `cross_framework_mapping_v1` | "Map SOC 2 CC6.1 to ISO 27001" |
| `obligation_to_evidence_v1` | "What evidence do I need for AU-6?" |
| `inheritance_chain_v1` | "Who owns PE-3 in a SaaS model?" |
| `baseline_coverage_v1` | "Is AC-2 in the FedRAMP Low baseline?" |

### Graph Data

| File | Contents |
|------|----------|
| `graph/schema.json` | ERD, predicates, planes, templates, scoring config |
| `graph/nodes.json` | 284 nodes: 14 frameworks, 92 families, 137 controls, baselines, service models, evidence types |
| `graph/edges.json` | 295 edges across all four planes |
| `graph/pathrag.md` | Traversal rules, scoring formula, output format |

## Roadmap

Planned enhancements and next priorities for the plugin:

### Graph Expansion

The current graph covers families and top-level controls. Next steps include adding sub-control nodes, richer NIST-to-framework edges extracted from existing mapping files, and conditional or baseline-specific predicates (e.g., "applies only at FedRAMP High").

### Framework Content Depth

Many framework reference files are concise summaries today. Enriching them with more detailed control descriptions, assessment objectives, and ODP (Organization-Defined Parameter) guidance would improve the quality of control lookups, narrative reviews, and gap analyses.

### OSCAL Integration

The plugin has an `/grc:oscal-guide` command but no actual OSCAL import/export capability. Adding OSCAL JSON/XML parsing would let users feed real System Security Plans, component definitions, and assessment results into the Knowledge Graph — bridging structured compliance data with graph-based reasoning.

### Automated Graph Seeding

`tools/seed_graph.py` can parse the mapping markdown files and expand the graph, but this capability is not fully utilized yet. Running the seeder in `--expand --write` mode and integrating it into a build step could significantly grow edge coverage without manual curation.

### Additional Test Coverage

The current 47-test suite validates graph integrity across all four layers. Next steps include integration tests for the slash commands themselves, edge-case graph traversals (e.g., orphan nodes, circular paths), fuzz testing on command inputs, and performance benchmarks for large graph queries.

### Plugin Packaging and Distribution

Polishing the `marketplace.json` metadata, adding install verification checks, documenting version compatibility, and streamlining the plugin install experience for both marketplace and local directory workflows.

## Contributing

Contributions welcome. The main areas where help is needed:

- **Framework updates** — Control catalogs change. If a framework publishes a new version, the corresponding reference file needs updating.
- **New framework mappings** — Adding mappings for frameworks not yet covered.
- **Command improvements** — Better output formats, additional review criteria, new operational workflows.
- **Reference accuracy** — If you spot an incorrect control ID, wrong baseline assignment, or outdated parameter value, please open an issue or PR.

### Adding a new command

1. Create `commands/your-command.md` following the pattern of existing commands
2. If the command needs reference data, create a file in the appropriate `skills/grc-knowledge/` subdirectory
3. Update `skills/grc-knowledge/SKILL.md` — add reference navigation entry
4. Update `agents/grc-researcher.md` — add new reference files to the available list

### Adding a new framework

1. Create `skills/grc-knowledge/frameworks/your-framework.md`
2. Create `skills/grc-knowledge/mappings/nist-to-your-framework.md` (map through NIST hub)
3. Update the Framework Quick Reference table in `SKILL.md`
4. Update framework aliases in `commands/control-lookup.md` and `commands/map-controls.md`

## License

MIT — see [LICENSE](LICENSE).

## Disclaimer

This plugin provides GRC domain knowledge for documentation and compliance workflow assistance. It does not constitute legal, security, or compliance advice. The plugin assesses document structure and completeness — it does not evaluate whether a system is actually secure or compliant. Always consult qualified GRC professionals and your authorizing official for authorization decisions.
