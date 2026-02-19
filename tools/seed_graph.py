#!/usr/bin/env python3
"""GRC Knowledge Graph Seeder — Extracts graph nodes and edges from markdown reference files.

Parses the existing mapping tables in grc/skills/grc-knowledge/mappings/*.md
and generates expanded nodes.json / edges.json for the Knowledge Graph.

Usage:
    python tools/seed_graph.py                    # Print stats
    python tools/seed_graph.py --validate         # Validate existing graph data
    python tools/seed_graph.py --expand           # Parse markdown and expand graph
    python tools/seed_graph.py --expand --write   # Write expanded graph to disk

Architecture layers:
    L1 - Deterministic Control Plane (ERD): strict typed nodes + cardinality constraints
    L2 - Typed Multi-Plane KG: PLANE-COMPLIANCE, PLANE-MAPPING, PLANE-RESPONSIBILITY, PLANE-EVIDENCE
    L3 - Path-Constrained Retrieval (PathRAG): ordered predicate templates
    L4 - Temporal Revision Layer: immutable snapshots, draft→published lifecycle
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
GRAPH_DIR = REPO_ROOT / "grc" / "skills" / "grc-knowledge" / "graph"
MAPPINGS_DIR = REPO_ROOT / "grc" / "skills" / "grc-knowledge" / "mappings"
SCHEMA_PATH = GRAPH_DIR / "schema.json"
NODES_PATH = GRAPH_DIR / "nodes.json"
EDGES_PATH = GRAPH_DIR / "edges.json"


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def load_json(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def collect_all_node_ids(nodes: dict) -> set[str]:
    """Collect all node IDs from the nodes.json structure."""
    ids: set[str] = set()

    for fw in nodes.get("frameworks", []):
        ids.add(fw["id"])

    for section in nodes.get("control_families", {}).values():
        if isinstance(section, list):
            for cf in section:
                ids.add(cf["id"])

    for section in nodes.get("controls", {}).values():
        if isinstance(section, list):
            for ctrl in section:
                ids.add(ctrl["id"])

    for bl in nodes.get("baselines", []):
        ids.add(bl["id"])

    for sm in nodes.get("service_models", []):
        ids.add(sm["id"])

    for ev in nodes.get("evidence_types", []):
        ids.add(ev["id"])

    for dt in nodes.get("document_types", []):
        ids.add(dt["id"])

    return ids


def collect_all_edges(edges: dict) -> list[dict]:
    """Flatten all edges from the edges.json structure."""
    all_edges: list[dict] = []

    for plane_key, plane_data in edges.items():
        if plane_key.startswith("_"):
            continue
        if not isinstance(plane_data, dict):
            continue
        for section_key, section_data in plane_data.items():
            if section_key.startswith("_"):
                continue
            if isinstance(section_data, list):
                all_edges.extend(section_data)

    return all_edges


def validate_graph() -> tuple[int, int, list[str]]:
    """Validate graph integrity. Returns (node_count, edge_count, errors)."""
    nodes = load_json(NODES_PATH)
    edges = load_json(EDGES_PATH)
    schema = load_json(SCHEMA_PATH)

    all_ids = collect_all_node_ids(nodes)
    all_edges = collect_all_edges(edges)
    valid_predicates = set(schema.get("predicates", {}).keys())

    errors: list[str] = []

    # Check edge referential integrity
    for i, edge in enumerate(all_edges):
        s = edge.get("s", "")
        p = edge.get("p", "")
        o = edge.get("o", "")

        if s not in all_ids:
            errors.append(f"Edge {i}: subject '{s}' not found in nodes")
        if o not in all_ids:
            errors.append(f"Edge {i}: object '{o}' not found in nodes")
        if p not in valid_predicates:
            errors.append(f"Edge {i}: predicate '{p}' not in schema")

    # Check that all families reference valid frameworks
    for section in nodes.get("control_families", {}).values():
        if isinstance(section, list):
            for cf in section:
                fw_id = cf.get("framework_id", "")
                if fw_id and fw_id not in all_ids:
                    errors.append(
                        f"ControlFamily '{cf['id']}': framework_id '{fw_id}' not found"
                    )

    # Check that all controls reference valid families
    for section in nodes.get("controls", {}).values():
        if isinstance(section, list):
            for ctrl in section:
                fam_id = ctrl.get("family_id", "")
                if fam_id and fam_id not in all_ids:
                    errors.append(
                        f"Control '{ctrl['id']}': family_id '{fam_id}' not found"
                    )

    return len(all_ids), len(all_edges), errors


# ---------------------------------------------------------------------------
# Markdown Parsing — Extract mapping tables
# ---------------------------------------------------------------------------

# Pattern: matches rows like "| AC-2 (Account Management) | CC6.1, CC6.2 | Full | notes |"
TABLE_ROW_RE = re.compile(
    r"^\|\s*(?P<nist>[A-Z]{2}-\d+(?:\([^)]*\))?)\s+"  # NIST control (e.g. AC-2, AC-2(1))
    r"(?:\([^)]*\))?\s*"  # Optional label in parens
    r"\|\s*(?P<target>[^|]+)"  # Target control(s)
    r"\|\s*(?P<coverage>[^|]+)"  # Coverage level
    r"\|\s*(?P<notes>[^|]*)\|",  # Notes
    re.MULTILINE,
)

# Simplified pattern for the mapping tables in the plugin
MAPPING_ROW_RE = re.compile(
    r"^\|\s*(?P<nist>[A-Z]{2,3}-\d+[^|]*?)\s*\|\s*(?P<target>[^|]+?)\s*\|\s*(?P<coverage>\w+)\s*\|\s*(?P<notes>[^|]*?)\s*\|",
    re.MULTILINE,
)


def parse_mapping_file(path: Path) -> list[dict]:
    """Parse a nist-to-*.md mapping file and extract edge data."""
    content = path.read_text()
    edges: list[dict] = []

    # Determine target framework from filename
    filename = path.stem  # e.g., "nist-to-soc2"
    parts = filename.split("-to-")
    if len(parts) != 2:
        return edges
    target_fw = parts[1].upper().replace("-", "_")

    for match in MAPPING_ROW_RE.finditer(content):
        nist_raw = match.group("nist").strip()
        target_raw = match.group("target").strip()
        coverage = match.group("coverage").strip()
        notes = match.group("notes").strip()

        # Clean up NIST control ID
        nist_id = re.match(r"([A-Z]{2,3}-\d+)", nist_raw)
        if not nist_id:
            continue
        nist_control = f"NIST-{nist_id.group(1)}"

        # Parse target control IDs (comma-separated)
        target_ids = [t.strip() for t in target_raw.split(",") if t.strip()]

        for tid in target_ids:
            if not tid or tid == "--" or tid.startswith("("):
                continue
            edges.append(
                {
                    "nist_control": nist_control,
                    "target_control": tid,
                    "target_framework": target_fw,
                    "coverage": coverage,
                    "notes": notes,
                    "source_file": path.name,
                }
            )

    return edges


def expand_graph() -> dict:
    """Parse all mapping files and return expanded edge data."""
    mapping_files = sorted(MAPPINGS_DIR.glob("nist-to-*.md"))
    all_mappings: list[dict] = []

    for mf in mapping_files:
        mappings = parse_mapping_file(mf)
        all_mappings.extend(mappings)
        print(f"  Parsed {mf.name}: {len(mappings)} edges")

    print(f"\nTotal extracted mappings: {len(all_mappings)}")

    # Group by NIST control
    by_nist: dict[str, list[dict]] = defaultdict(list)
    for m in all_mappings:
        by_nist[m["nist_control"]].append(m)

    print(f"Unique NIST controls with mappings: {len(by_nist)}")

    return {
        "total_edges": len(all_mappings),
        "unique_nist_controls": len(by_nist),
        "by_framework": _count_by_framework(all_mappings),
        "mappings": all_mappings,
    }


def _count_by_framework(mappings: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for m in mappings:
        counts[m["target_framework"]] += 1
    return dict(counts)


# ---------------------------------------------------------------------------
# Content hashing (Revision Layer support)
# ---------------------------------------------------------------------------


def compute_content_hash(data: dict) -> str:
    """SHA-256 of canonical JSON for revision integrity."""
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    args = set(sys.argv[1:])

    if "--validate" in args:
        print("Validating GRC Knowledge Graph...\n")
        node_count, edge_count, errors = validate_graph()
        print(f"Nodes: {node_count}")
        print(f"Edges: {edge_count}")

        if errors:
            print(f"\nERRORS ({len(errors)}):")
            for e in errors:
                print(f"  - {e}")
            sys.exit(1)
        else:
            print("\nAll validations passed.")

            # Compute content hashes for revision tracking
            nodes = load_json(NODES_PATH)
            edges = load_json(EDGES_PATH)
            print(f"\nNodes content_hash: {compute_content_hash(nodes)[:16]}...")
            print(f"Edges content_hash: {compute_content_hash(edges)[:16]}...")

    elif "--expand" in args:
        print("Expanding graph from markdown mapping files...\n")
        result = expand_graph()
        print(f"\nBy framework:")
        for fw, count in sorted(result["by_framework"].items()):
            print(f"  {fw}: {count} edges")

        if "--write" in args:
            print("\n--write flag detected. Writing expanded graph...")
            # TODO: Merge expanded edges into edges.json
            print("  (Full write not yet implemented — use extracted data to manually update edges.json)")
        else:
            print("\nDry run. Add --write to persist changes.")

    else:
        print("GRC Knowledge Graph Seeder")
        print("=" * 40)
        print()

        # Print stats
        nodes = load_json(NODES_PATH)
        edges = load_json(EDGES_PATH)

        all_ids = collect_all_node_ids(nodes)
        all_edges = collect_all_edges(edges)

        print(f"Graph Statistics:")
        print(f"  Nodes: {len(all_ids)}")
        print(f"  Edges: {len(all_edges)}")
        print(f"  Frameworks: {len(nodes.get('frameworks', []))}")

        # Count by type
        family_count = sum(
            len(v) for k, v in nodes.get("control_families", {}).items()
            if isinstance(v, list)
        )
        control_count = sum(
            len(v) for k, v in nodes.get("controls", {}).items()
            if isinstance(v, list)
        )
        print(f"  Control Families: {family_count}")
        print(f"  Controls: {control_count}")
        print(f"  Baselines: {len(nodes.get('baselines', []))}")
        print(f"  Service Models: {len(nodes.get('service_models', []))}")
        print(f"  Evidence Types: {len(nodes.get('evidence_types', []))}")
        print(f"  Document Types: {len(nodes.get('document_types', []))}")

        # Edge stats by predicate
        pred_counts: dict[str, int] = defaultdict(int)
        for e in all_edges:
            pred_counts[e.get("p", "?")] += 1
        print(f"\n  Edges by predicate:")
        for pred, count in sorted(pred_counts.items()):
            print(f"    {pred}: {count}")

        print(f"\nUsage:")
        print(f"  python {sys.argv[0]} --validate     # Check referential integrity")
        print(f"  python {sys.argv[0]} --expand       # Extract from markdown (dry run)")
        print(f"  python {sys.argv[0]} --expand --write  # Extract and write to graph")


if __name__ == "__main__":
    main()
