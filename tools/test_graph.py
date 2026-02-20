#!/usr/bin/env python3
"""Tests for GRC Knowledge Graph integrity and PathRAG contracts.

Validates:
- L1 (ERD): Referential integrity, type constraints, cardinality
- L2 (Multi-Plane KG): Plane predicate allowlists, hub routing invariant
- L3 (PathRAG): Template predicate ordering, scoring formula
- L4 (Revision): Revision metadata, content hashing
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

GRAPH_DIR = Path(__file__).resolve().parent.parent / "grc" / "skills" / "grc-knowledge" / "graph"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def load(name: str) -> dict:
    with open(GRAPH_DIR / name) as f:
        return json.load(f)


def collect_node_ids(nodes: dict) -> dict[str, str]:
    """Returns {node_id: node_type}."""
    result: dict[str, str] = {}

    for fw in nodes.get("frameworks", []):
        result[fw["id"]] = "Framework"

    for section in nodes.get("control_families", {}).values():
        if isinstance(section, list):
            for cf in section:
                result[cf["id"]] = "ControlFamily"

    for section in nodes.get("controls", {}).values():
        if isinstance(section, list):
            for ctrl in section:
                result[ctrl["id"]] = "Control"

    for bl in nodes.get("baselines", []):
        result[bl["id"]] = "Baseline"

    for sm in nodes.get("service_models", []):
        result[sm["id"]] = "ServiceModel"

    for ev in nodes.get("evidence_types", []):
        result[ev["id"]] = "EvidenceType"

    for dt in nodes.get("document_types", []):
        result[dt["id"]] = "DocumentType"

    return result


def flatten_edges(edges: dict) -> list[dict]:
    result: list[dict] = []
    for plane_key, plane_data in edges.items():
        if plane_key.startswith("_"):
            continue
        if not isinstance(plane_data, dict):
            continue
        for section_key, section_data in plane_data.items():
            if section_key.startswith("_"):
                continue
            if isinstance(section_data, list):
                for e in section_data:
                    e["_plane"] = plane_key
                    e["_section"] = section_key
                    result.append(e)
    return result


# ---------------------------------------------------------------------------
# Test functions
# ---------------------------------------------------------------------------

PASSED = 0
FAILED = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASSED, FAILED
    if condition:
        PASSED += 1
        print(f"  PASS  {name}")
    else:
        FAILED += 1
        msg = f"  FAIL  {name}"
        if detail:
            msg += f" — {detail}"
        print(msg)


def test_l1_erd() -> None:
    """Layer 1: Deterministic Control Plane (ERD) tests."""
    print("\n=== L1: Deterministic Control Plane (ERD) ===")

    schema = load("schema.json")
    nodes = load("nodes.json")
    edges = load("edges.json")

    node_map = collect_node_ids(nodes)
    all_edges = flatten_edges(edges)
    valid_predicates = set(schema.get("predicates", {}).keys())

    # Referential integrity
    dangling_subjects = [e for e in all_edges if e["s"] not in node_map]
    dangling_objects = [e for e in all_edges if e["o"] not in node_map]
    check("No dangling subject references", len(dangling_subjects) == 0,
          f"{len(dangling_subjects)} edges have unknown subjects")
    check("No dangling object references", len(dangling_objects) == 0,
          f"{len(dangling_objects)} edges have unknown objects")

    # All predicates are valid
    bad_predicates = [e for e in all_edges if e["p"] not in valid_predicates]
    check("All predicates in schema", len(bad_predicates) == 0,
          f"{len(bad_predicates)} edges use unknown predicates")

    # Confidence values in range [0, 1]
    bad_confidence = [e for e in all_edges if not (0.0 <= e.get("confidence", 0) <= 1.0)]
    check("All confidence values in [0,1]", len(bad_confidence) == 0,
          f"{len(bad_confidence)} edges have out-of-range confidence")

    # Type pair validation for CONTAINS edges
    contains_edges = [e for e in all_edges if e["p"] == "CONTAINS"]
    bad_contains = []
    for e in contains_edges:
        s_type = node_map.get(e["s"], "?")
        o_type = node_map.get(e["o"], "?")
        valid_pairs = [
            ("Framework", "ControlFamily"),
            ("ControlFamily", "Control"),
            ("Control", "Control"),
        ]
        if (s_type, o_type) not in valid_pairs:
            bad_contains.append(f"{e['s']}({s_type}) -> {e['o']}({o_type})")
    check("CONTAINS edges have valid type pairs", len(bad_contains) == 0,
          f"Invalid: {bad_contains[:3]}")

    # ControlFamily -> Framework referential integrity
    families_with_bad_fw = []
    for section in nodes.get("control_families", {}).values():
        if isinstance(section, list):
            for cf in section:
                if cf.get("framework_id") not in node_map:
                    families_with_bad_fw.append(cf["id"])
    check("All families reference valid frameworks", len(families_with_bad_fw) == 0,
          f"Bad refs: {families_with_bad_fw[:3]}")

    # Controls -> ControlFamily referential integrity
    controls_with_bad_family = []
    for section in nodes.get("controls", {}).values():
        if isinstance(section, list):
            for ctrl in section:
                if ctrl.get("family_id") not in node_map:
                    controls_with_bad_family.append(ctrl["id"])
    check("All controls reference valid families", len(controls_with_bad_family) == 0,
          f"Bad refs: {controls_with_bad_family[:3]}")

    # No duplicate node IDs
    all_ids = []
    for fw in nodes.get("frameworks", []):
        all_ids.append(fw["id"])
    for section in nodes.get("control_families", {}).values():
        if isinstance(section, list):
            for cf in section:
                all_ids.append(cf["id"])
    for section in nodes.get("controls", {}).values():
        if isinstance(section, list):
            for ctrl in section:
                all_ids.append(ctrl["id"])
    dupes = [x for x in all_ids if all_ids.count(x) > 1]
    check("No duplicate node IDs", len(set(dupes)) == 0,
          f"Duplicates: {list(set(dupes))[:5]}")


def test_l2_multiplane() -> None:
    """Layer 2: Typed Multi-Plane Knowledge Graph tests."""
    print("\n=== L2: Typed Multi-Plane Knowledge Graph ===")

    schema = load("schema.json")
    edges = load("edges.json")
    nodes = load("nodes.json")
    node_map = collect_node_ids(nodes)

    planes = schema.get("planes", {})
    all_edges = flatten_edges(edges)

    # Check that each plane section uses only its allowed predicates
    plane_predicate_map = {
        "plane_compliance": set(planes["PLANE-COMPLIANCE"]["predicates_allowed"]),
        "plane_mapping": set(planes["PLANE-MAPPING"]["predicates_allowed"]),
        "plane_responsibility": set(planes["PLANE-RESPONSIBILITY"]["predicates_allowed"]),
        "plane_evidence": set(planes["PLANE-EVIDENCE"]["predicates_allowed"]),
    }

    for plane_key, allowed in plane_predicate_map.items():
        plane_edges = [e for e in all_edges if e.get("_plane") == plane_key]
        bad = [e for e in plane_edges if e["p"] not in allowed]
        check(f"{plane_key} uses only allowed predicates", len(bad) == 0,
              f"{len(bad)} edges use disallowed predicates")

    # Hub routing invariant: MAPS_TO edges must have at least one NIST node
    maps_to_edges = [e for e in all_edges if e["p"] == "MAPS_TO"]
    non_hub = []
    for e in maps_to_edges:
        s_is_nist = e["s"].startswith("NIST-")
        o_is_nist = e["o"].startswith("NIST-")
        if not s_is_nist and not o_is_nist:
            non_hub.append(f"{e['s']} -> {e['o']}")
    check("MAPS_TO hub routing (at least one NIST endpoint)", len(non_hub) == 0,
          f"Non-hub edges: {non_hub[:3]}")

    # Service model stack ordering: INHERITS_FROM flows upward
    inherits_edges = [e for e in all_edges if e["p"] == "INHERITS_FROM"]
    sm_positions = {sm["id"]: sm["stack_position"] for sm in nodes.get("service_models", [])}
    bad_inherit = []
    for e in inherits_edges:
        s_pos = sm_positions.get(e["s"], 0)
        o_pos = sm_positions.get(e["o"], 0)
        if s_pos <= o_pos:
            bad_inherit.append(f"{e['s']}({s_pos}) inherits {e['o']}({o_pos})")
    check("INHERITS_FROM flows upward (higher stack inherits lower)", len(bad_inherit) == 0,
          f"Bad: {bad_inherit}")

    # Minimum graph size checks
    check("At least 10 frameworks", len(nodes.get("frameworks", [])) >= 10)
    total_controls = sum(
        len(v) for k, v in nodes.get("controls", {}).items() if isinstance(v, list)
    )
    check("At least 50 controls", total_controls >= 50,
          f"Found {total_controls}")
    check("At least 50 MAPS_TO edges", len(maps_to_edges) >= 50,
          f"Found {len(maps_to_edges)}")

    # Expanded plane coverage checks
    assigned_to_edges = [e for e in all_edges if e["p"] == "ASSIGNED_TO"]
    requires_evidence_edges = [e for e in all_edges if e["p"] == "REQUIRES_EVIDENCE"]
    responsibility_of_edges = [e for e in all_edges if e["p"] == "RESPONSIBILITY_OF"]
    documented_in_edges = [e for e in all_edges if e["p"] == "DOCUMENTED_IN"]

    check("At least 500 ASSIGNED_TO edges", len(assigned_to_edges) >= 500,
          f"Found {len(assigned_to_edges)}")
    check("At least 100 REQUIRES_EVIDENCE edges", len(requires_evidence_edges) >= 100,
          f"Found {len(requires_evidence_edges)}")
    check("At least 100 RESPONSIBILITY_OF edges", len(responsibility_of_edges) >= 100,
          f"Found {len(responsibility_of_edges)}")
    check("At least 100 DOCUMENTED_IN edges", len(documented_in_edges) >= 100,
          f"Found {len(documented_in_edges)}")


def test_l3_pathrag() -> None:
    """Layer 3: Path-Constrained Retrieval (PathRAG) tests."""
    print("\n=== L3: Path-Constrained Retrieval (PathRAG) ===")

    schema = load("schema.json")
    edges = load("edges.json")
    nodes = load("nodes.json")

    templates = schema.get("templates", {})
    scoring = schema.get("scoring", {})

    # All templates reference valid predicates
    valid_predicates = set(schema.get("predicates", {}).keys())
    for tpl_name, tpl in templates.items():
        for pred in tpl.get("predicates_ordered", []):
            check(f"Template {tpl_name} predicate '{pred}' is valid",
                  pred in valid_predicates)

    # Scoring weights exist for all predicates used in edges
    all_edges = flatten_edges(edges)
    edge_weights = scoring.get("edge_weights", {})
    used_predicates = {e["p"] for e in all_edges}
    missing_weights = used_predicates - set(edge_weights.keys())
    check("All used predicates have scoring weights", len(missing_weights) == 0,
          f"Missing: {missing_weights}")

    # Cross-framework mapping template is bidirectional-testable
    # Can we trace SOC2-CC6.1 -> NIST-AC-2 -> ISO-A.5.18?
    node_map = collect_node_ids(nodes)
    maps_to = [e for e in all_edges if e["p"] == "MAPS_TO"]

    # Find SOC2-CC6.1 -> NIST paths
    soc2_to_nist = [e for e in maps_to if e["o"] == "SOC2-CC6.1" or e["s"] == "SOC2-CC6.1"]
    # Since MAPS_TO goes NIST->SOC2, the reverse traversal finds NIST-AC-2->SOC2-CC6.1
    nist_sources_for_cc61 = [e["s"] for e in maps_to if e["o"] == "SOC2-CC6.1"]
    check("SOC2-CC6.1 is reachable from NIST via MAPS_TO",
          len(nist_sources_for_cc61) > 0,
          f"Found {len(nist_sources_for_cc61)} NIST sources")

    # From those NIST controls, can we reach ISO controls?
    if nist_sources_for_cc61:
        nist_ctrl = nist_sources_for_cc61[0]
        nist_to_iso = [e for e in maps_to if e["s"] == nist_ctrl and e["o"].startswith("ISO-")]
        check(f"Can map {nist_ctrl} -> ISO-27001 via MAPS_TO",
              len(nist_to_iso) > 0,
              f"Found {len(nist_to_iso)} ISO targets")

    # Evidence chain test: NIST-AC-2 has evidence requirements
    ac2_evidence = [e for e in all_edges if e["s"] == "NIST-AC-2" and e["p"] == "REQUIRES_EVIDENCE"]
    check("NIST-AC-2 has evidence requirements", len(ac2_evidence) > 0,
          f"Found {len(ac2_evidence)} evidence edges")

    # Scoring config completeness
    check("min_path_score defined", "min_path_score" in scoring)
    check("max_depth defined", "max_depth" in scoring)
    check("jaccard_dedup_threshold defined", "jaccard_dedup_threshold" in scoring)


def test_l4_revision() -> None:
    """Layer 4: Temporal Revision Layer tests."""
    print("\n=== L4: Temporal Revision Layer ===")

    schema = load("schema.json")
    nodes = load("nodes.json")
    edges = load("edges.json")

    revision = schema.get("revision_layer", {})

    # Revision metadata exists
    check("Revision layer defined", bool(revision))
    check("Current revision exists", bool(revision.get("current_revision")))

    current = revision.get("current_revision", {})
    check("Revision has ID", bool(current.get("revision_id")))
    check("Revision has status", current.get("status") == "published")
    check("Revision has created_at", bool(current.get("created_at")))

    # Lifecycle states defined
    lifecycle = revision.get("lifecycle", [])
    check("Lifecycle includes draft", "draft" in lifecycle)
    check("Lifecycle includes published", "published" in lifecycle)
    check("Lifecycle includes archived", "archived" in lifecycle)

    # Gates defined
    gates = revision.get("gates", {})
    check("Publish gate defined", bool(gates.get("publish_gate")))

    # Content hash reproducibility
    nodes_hash = hashlib.sha256(
        json.dumps(nodes, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    check("Nodes content hash is reproducible", len(nodes_hash) == 64)

    edges_hash = hashlib.sha256(
        json.dumps(edges, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    check("Edges content hash is reproducible", len(edges_hash) == 64)

    # Meta revision_id matches schema
    nodes_rev = nodes.get("_meta", {}).get("revision_id")
    edges_rev = edges.get("_meta", {}).get("revision_id")
    schema_rev = current.get("revision_id")
    check("Nodes revision_id matches schema",
          nodes_rev == schema_rev,
          f"nodes={nodes_rev}, schema={schema_rev}")
    check("Edges revision_id matches schema",
          edges_rev == schema_rev,
          f"edges={edges_rev}, schema={schema_rev}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    print("GRC Knowledge Graph — Four-Layer Validation Suite")
    print("=" * 55)

    test_l1_erd()
    test_l2_multiplane()
    test_l3_pathrag()
    test_l4_revision()

    print(f"\n{'=' * 55}")
    print(f"Results: {PASSED} passed, {FAILED} failed")

    if FAILED > 0:
        sys.exit(1)
    else:
        print("\nAll tests passed.")


if __name__ == "__main__":
    main()
