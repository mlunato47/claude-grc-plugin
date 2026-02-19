# /grc:graph-query

## Usage

```
/grc:graph-query <natural-language-question>
```

## Arguments

- `<natural-language-question>` — A compliance question to answer using Knowledge Graph traversal

## Behavior

1. **Read** the graph data files:
   - `graph/schema.json` — for schema and template definitions
   - `graph/nodes.json` — for node lookups
   - `graph/edges.json` — for edge traversal
   - `graph/pathrag.md` — for traversal rules and output format

2. **Parse the question** to identify:
   - **Seed entities**: Control IDs, framework names, family names mentioned in the question
   - **Target entities**: If the question asks about mapping, identify the target framework
   - **Query type**: Determine which template(s) apply:
     - "What controls..." → `compliance_chain_v1`
     - "How does X map to Y..." → `cross_framework_mapping_v1`
     - "What evidence..." → `obligation_to_evidence_v1`
     - "Who is responsible..." → `inheritance_chain_v1`
     - "What baseline..." → `baseline_coverage_v1`
     - Complex questions → multi-plane query

3. **Execute PathRAG traversal** for each identified template:
   - Follow the predicate ordering defined in the template
   - Score and deduplicate paths per `pathrag.md` rules
   - Apply evidence gate on normative edges

4. **Synthesize an answer** that:
   - Cites specific paths from the graph traversal
   - Uses PathRAG notation for traceability
   - Provides the natural language answer grounded in graph evidence
   - Notes any gaps where the graph doesn't cover the query (and falls back to prose reference files)

5. **Cross-reference with reference files** when the graph provides a partial answer:
   - Use `frameworks/<framework>.md` for control details
   - Use `mappings/<mapping>.md` for coverage nuances
   - Use `audits/` for assessment context

## Example Questions and Template Routing

| Question | Template(s) | Planes |
|----------|------------|--------|
| "Map SOC 2 CC6.1 to ISO 27001" | `cross_framework_mapping_v1` | MAPPING |
| "What evidence do I need for AU-6?" | `obligation_to_evidence_v1` | EVIDENCE |
| "Is AC-2 in the FedRAMP Low baseline?" | `baseline_coverage_v1` | COMPLIANCE |
| "Who owns PE-3 in a SaaS model?" | `inheritance_chain_v1` | RESPONSIBILITY |
| "Map CC6.1 to HIPAA and list evidence" | `cross_framework_mapping_v1` + neighborhood BFS | MAPPING + EVIDENCE |
| "What's the full compliance chain for NIST IR?" | `compliance_chain_v1` | COMPLIANCE |
| "Compare access control requirements across SOC2, ISO, and PCI" | `cross_framework_mapping_v1` × 3 | MAPPING (multi-target) |

## Output Format

### Simple query (single plane)
```
## Answer

[Natural language answer grounded in graph paths]

## Graph Evidence

### MAPPING PATHS (2 path(s), template: cross_framework_mapping_v1)

### Path 1 (score: 0.95)
  SOC2-CC6.1 --[MAPS_TO]--> NIST-AC-2 (Account Management)  [coverage: Full]
  NIST-AC-2 --[MAPS_TO]--> ISO-A.5.18 (Access Rights)  [coverage: Full]

### Path 2 (score: 0.90)
  SOC2-CC6.1 --[MAPS_TO]--> NIST-AC-3 (Access Enforcement)  [coverage: Full]
  NIST-AC-3 --[MAPS_TO]--> ISO-A.5.15 (Access Control)  [coverage: Full]
```

### Complex query (multi-plane)
```
## Answer

[Natural language answer combining insights from multiple planes]

## Graph Evidence

### MAPPING PATHS (N path(s), template: cross_framework_mapping_v1)
[paths...]

### EVIDENCE PATHS (M path(s), template: obligation_to_evidence_v1)
[paths...]
```

## Notes

- When the graph does not contain a node for the queried control, say so explicitly and fall back to the prose reference files
- Always present the graph evidence — never answer a graph-query without showing the traversal paths
- For questions about specific control implementation details (ODPs, parameter values), defer to `frameworks/<framework>.md` — the graph captures relationships, not prose content
- Combine graph traversal with framework prose for the most complete answer
