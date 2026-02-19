# /grc:graph-traverse

## Usage

```
/grc:graph-traverse <source-control-id> [--to <target-framework>] [--plane <plane>] [--depth <max-depth>]
```

## Arguments

- `<source-control-id>` — The starting control, family, or framework ID (e.g., `AC-2`, `CC6.1`, `NIST-AC`, `SOC2`)
- `--to <target-framework>` — Target framework to map to (e.g., `ISO-27001`, `SOC2`, `PCI-DSS`, `HIPAA`)
- `--plane <plane>` — Which graph plane to traverse: `compliance`, `mapping`, `responsibility`, `evidence`, or `all` (default: auto-detect)
- `--depth <max-depth>` — Maximum traversal depth (default: 6)

## Behavior

1. **Read** the graph data files:
   - `graph/schema.json` — for predicate definitions, templates, scoring weights
   - `graph/nodes.json` — for node lookups
   - `graph/edges.json` — for edge traversal
   - `graph/pathrag.md` — for traversal rules

2. **Resolve the seed node**: Normalize the input control ID to the canonical graph node ID.
   - `AC-2` → `NIST-AC-2`
   - `CC6.1` → `SOC2-CC6.1`
   - `A.5.18` → `ISO-A.5.18`
   - `164.312(a)(1)` → `HIPAA-312-a1`
   - If ambiguous, list matching nodes and ask the user.

3. **Select traversal template** based on the query:
   - If `--to` is specified → use `cross_framework_mapping_v1` (PLANE-MAPPING)
   - If `--plane compliance` → use `compliance_chain_v1` (PLANE-COMPLIANCE)
   - If `--plane evidence` → use neighborhood BFS on PLANE-EVIDENCE
   - If `--plane responsibility` → use neighborhood BFS on PLANE-RESPONSIBILITY
   - If `--plane all` or auto-detect → run all applicable planes

4. **Execute PathRAG traversal** following the rules in `pathrag.md`:
   - Template-ordered BFS for PLANE-COMPLIANCE and PLANE-MAPPING
   - Neighborhood BFS for PLANE-RESPONSIBILITY and PLANE-EVIDENCE
   - Score paths using: `score = avg(confidence) × geo_mean(edge_weights)`
   - Apply evidence gate: discard paths with unsupported normative edges
   - Apply diversity filter: Jaccard dedup at threshold 0.8

5. **Present results** in Vector PathRAG format:
   ```
   ## MAPPING PATHS (3 path(s), template: cross_framework_mapping_v1)

   ### Path 1 (score: 0.95)
     SOC2-CC6.1 --[MAPS_TO]--> NIST-AC-2 (Account Management)  [coverage: Full]
     NIST-AC-2 --[MAPS_TO]--> ISO-A.5.18 (Access Rights)  [coverage: Full]
   ```

6. **For multi-plane queries**, present each plane's results in separate sections, sorted by score.

## Examples

### Cross-framework mapping
```
/grc:graph-traverse CC6.1 --to ISO-27001
```
Traverses: SOC2-CC6.1 → NIST hub → ISO 27001 controls

### Full graph exploration
```
/grc:graph-traverse AC-2 --plane all
```
Shows: compliance chain + all cross-framework mappings + responsibility + evidence requirements

### Evidence trail
```
/grc:graph-traverse IR-8 --plane evidence
```
Shows: what evidence artifacts IR-8 (Incident Response Plan) requires for audit

### Responsibility check
```
/grc:graph-traverse PE-3 --plane responsibility
```
Shows: which service model layer owns PE-3 (Physical Access Control) and inheritance chain

## Output Format

Always use the PathRAG path notation with scores. Include:
- Path number and score
- Each triple: `subject --[PREDICATE]--> object (label)`
- Evidence/coverage annotations in square brackets
- A summary after all paths explaining the key takeaway

## Notes

- All cross-framework mappings route through NIST 800-53 as the hub (no direct non-NIST-to-non-NIST paths)
- If the source or target control is not in the graph, fall back to the detailed mapping files in `mappings/` for prose-based lookup
- When the graph has a gap (control not seeded), note it and suggest using `/grc:map-controls` for the full prose mapping
