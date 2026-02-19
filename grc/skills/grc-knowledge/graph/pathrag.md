# GRC PathRAG — Path-Constrained Retrieval over the Knowledge Graph

## Architecture

This Knowledge Graph implements a four-layer architecture modeled after Vector StrategyEngine:

1. **Deterministic Control Plane (ERD)** — Strict entity types with cardinality constraints. Every node has a typed ID; every edge validates subject/object type pairs.
2. **Typed Multi-Plane Knowledge Graph** — Four semantic planes, each with its own predicate allowlist and traversal strategy.
3. **Path-Constrained Retrieval (PathRAG)** — Ordered predicate templates that enforce traversal discipline. No flat retrieval; all reasoning follows relational paths.
4. **Temporal Revision Layer** — Immutable graph snapshots with draft→published lifecycle and evidence gating.

## Four Graph Planes

### PLANE-COMPLIANCE (Template-Ordered BFS)
**Purpose**: Framework hierarchy traversal.
**Predicate chain**: `CONTAINS → CONTAINS → ASSIGNED_TO`
**Use case**: "What controls are in the AC family at the Moderate baseline?"

```
NIST-800-53 --[CONTAINS]--> NIST-AC --[CONTAINS]--> NIST-AC-2 --[ASSIGNED_TO]--> FEDRAMP-MODERATE
```

### PLANE-MAPPING (Template-Ordered BFS)
**Purpose**: Cross-framework control equivalence. All paths route through NIST 800-53 as the universal hub.
**Predicate chain**: `MAPS_TO → MAPS_TO`
**Use case**: "What is the ISO 27001 equivalent of SOC 2 CC6.1?"

```
SOC2-CC6.1 --[MAPS_TO]--> NIST-AC-2 --[MAPS_TO]--> ISO-A.5.18
                                      --[MAPS_TO]--> ISO-A.5.15
```

**Hub routing invariant**: No direct non-NIST-to-non-NIST edges. To map SOC2→ISO, always transit through NIST.

### PLANE-RESPONSIBILITY (Neighborhood BFS)
**Purpose**: Control responsibility across IaaS/PaaS/SaaS layers.
**Predicates**: `RESPONSIBILITY_OF`, `INHERITS_FROM`
**Use case**: "Who is responsible for PE-3 (Physical Access Control) in a SaaS deployment?"

```
NIST-PE-3 --[RESPONSIBILITY_OF]--> IAAS (provider)
IAAS --[INHERITS_FROM]-- PAAS --[INHERITS_FROM]-- SAAS
→ Answer: IaaS provider owns PE-3; PaaS and SaaS inherit.
```

### PLANE-EVIDENCE (Neighborhood BFS)
**Purpose**: Evidence and documentation requirements for controls.
**Predicates**: `REQUIRES_EVIDENCE`, `DOCUMENTED_IN`
**Use case**: "What evidence does an auditor expect for AC-2?"

```
NIST-AC-2 --[REQUIRES_EVIDENCE]--> EVIDENCE-ACCESS-REVIEW-LOG
NIST-AC-2 --[REQUIRES_EVIDENCE]--> EVIDENCE-CONFIG-SCREENSHOT
NIST-AC-2 --[DOCUMENTED_IN]--> DOC-SSP
```

## PathRAG Traversal Rules

### Rule 1: Template-Ordered BFS (PLANE-COMPLIANCE, PLANE-MAPPING)
When traversing template-ordered planes, follow predicates **in order**. Do not skip or reorder.

**Compliance chain template**:
```
Step 1: Start at seed node (Framework or ControlFamily)
Step 2: Follow CONTAINS edge to next level
Step 3: Follow CONTAINS edge to control level
Step 4: (Optional) Follow ASSIGNED_TO to baseline
```

**Cross-framework mapping template**:
```
Step 1: Start at source control (any framework)
Step 2: Follow MAPS_TO to reach NIST 800-53 control (hub)
Step 3: Follow MAPS_TO from NIST control to target framework control(s)
```

If the source is already a NIST control, skip step 2 and go directly to step 3 (fan-out from hub).

### Rule 2: Neighborhood BFS (PLANE-RESPONSIBILITY, PLANE-EVIDENCE)
When traversing neighborhood planes, follow edges in any order, bidirectionally.

- Walk outgoing edges from the seed node
- Walk incoming edges to the seed node (reverse adjacency)
- Collect all reachable nodes within max_depth
- Do not revisit nodes (cycle prevention)

### Rule 3: Scoring
Score each path using Vector's formula:
```
score = avg(confidence_per_edge) × geo_mean(edge_weights)
```

Edge weights from schema:
- MAPS_TO: 1.3 (highest — cross-framework mappings are the core value)
- RESPONSIBILITY_OF: 1.2
- REQUIRES_EVIDENCE: 1.2
- INHERITS_FROM: 1.1
- CONTAINS: 1.0
- ASSIGNED_TO: 1.0
- PART_OF: 0.9
- DOCUMENTED_IN: 0.9
- SUPERSEDES: 0.7

### Rule 4: Evidence Gate
For normative predicates (MAPS_TO, RESPONSIBILITY_OF, REQUIRES_EVIDENCE), the edge must have a source citation (the `meta.source` field or `meta.coverage` field). Paths with unsupported normative edges are discarded.

### Rule 5: Diversity Filter
When multiple paths cover the same ground (Jaccard similarity > 0.8 on edge signatures), keep only the highest-scoring path.

## Output Format

When presenting PathRAG results, use the Vector-style path notation:

```
## COMPLIANCE PATHS (N path(s), template: compliance_chain_v1)

### Path 1 (score: 0.95)
  NIST-800-53 --[CONTAINS]--> NIST-AC (Access Control)
  NIST-AC --[CONTAINS]--> NIST-AC-2 (Account Management)
  NIST-AC-2 --[ASSIGNED_TO]--> FEDRAMP-MODERATE  [evidence: NIST SP 800-53B]

### Path 2 (score: 0.90)
  ...
```

For cross-framework mapping results:
```
## MAPPING PATHS (N path(s), template: cross_framework_mapping_v1)

### Path 1 (score: 0.95)
  SOC2-CC6.1 --[MAPS_TO]--> NIST-AC-2 (Account Management)  [coverage: Full]
  NIST-AC-2 --[MAPS_TO]--> ISO-A.5.18 (Access Rights)  [coverage: Full]
```

## Multi-Plane Queries

When a question spans multiple planes, run each plane's PathRAG independently and merge results. Sort by score descending.

Example: "Map SOC 2 CC6.1 to ISO 27001 and tell me what evidence I need"
1. **PLANE-MAPPING**: SOC2-CC6.1 → NIST-AC-2 → ISO-A.5.18
2. **PLANE-EVIDENCE**: NIST-AC-2 → EVIDENCE-ACCESS-REVIEW-LOG, EVIDENCE-CONFIG-SCREENSHOT

Present both plane results in sequence.

## Graph Data Files

| File | Contents |
|------|----------|
| `schema.json` | Node types, predicates, planes, templates, revision layer, scoring config |
| `nodes.json` | All graph nodes: frameworks, families, controls, baselines, service models, evidence types |
| `edges.json` | All graph edges organized by plane: compliance, mapping, responsibility, evidence |
| `pathrag.md` | This file — traversal rules, output format, scoring |

## Revision Management

The graph uses immutable revisions:
- **Current revision**: `grc-kg-rev-001` (status: published)
- **Lifecycle**: draft → published → archived
- **Publish gate**: All normative edges must have source citations
- **Content integrity**: Each revision has a content_hash (SHA-256) for verification

To propose graph changes:
1. Create a new revision in draft status
2. Add/modify/remove nodes and edges
3. Validate all normative edges have evidence
4. Publish the revision (gates must pass)
5. Archive the previous revision
