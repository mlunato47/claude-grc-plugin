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
# Content hashing (Revision Layer support)
# ---------------------------------------------------------------------------


def compute_content_hash(data: dict) -> str:
    """SHA-256 of canonical JSON for revision integrity."""
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# ID patterns and normalization
# ---------------------------------------------------------------------------

NIST_CTRL_RE = re.compile(r"([A-Z]{2})-(\d+)")
ISO_CTRL_RE = re.compile(r"A\.(\d+)\.(\d+)")
CIS_SAFEGUARD_RE = re.compile(r"^(\d+)\.(\d+)$")
PCI_REQ_RE = re.compile(r"^(\d+)\.(\d+)(?:\.(\d+))?(?:\.(\d+))?$")
COBIT_OBJ_RE = re.compile(r"(APO|BAI|DSS|EDM|MEA)(\d+)")
CCM_CTRL_RE = re.compile(r"([A-Z][A-Z&]+)-(\d+)")
CMMC_PRACTICE_RE = re.compile(r"L(\d+)-(\d+\.\d+\.\d+)")


def normalize_nist_id(raw: str) -> str | None:
    """Normalize a raw NIST control reference to graph ID format.

    'AC-2' -> 'NIST-AC-2'.  Enhancements like 'AC-2(1)' collapse to base 'NIST-AC-2'.
    """
    raw = raw.strip()
    base = raw.split("(")[0].strip()
    m = NIST_CTRL_RE.match(base)
    if m:
        return f"NIST-{m.group(1)}-{m.group(2)}"
    return None


def extract_nist_ids(raw: str) -> list[str]:
    """Extract all NIST control IDs from a comma/space separated string."""
    ids: list[str] = []
    for chunk in re.split(r"[,;]", raw):
        chunk = chunk.strip()
        if not chunk or chunk == "--":
            continue
        nid = normalize_nist_id(chunk)
        if nid:
            ids.append(nid)
    return list(dict.fromkeys(ids))  # dedupe preserving order


def normalize_iso_id(raw: str) -> str | None:
    """'A.5.18' -> 'ISO-A.5.18'"""
    m = ISO_CTRL_RE.search(raw.strip())
    if m:
        return f"ISO-A.{m.group(1)}.{m.group(2)}"
    return None


def normalize_pci_id(raw: str) -> str | None:
    """'7.2.1' -> 'PCI-7.2.1', 'N/A' -> None"""
    raw = raw.strip()
    if raw.upper() == "N/A":
        return None
    m = PCI_REQ_RE.match(raw)
    if m:
        parts = [m.group(1), m.group(2)]
        if m.group(3):
            parts.append(m.group(3))
        if m.group(4):
            parts.append(m.group(4))
        return f"PCI-{'.'.join(parts)}"
    return None


def normalize_cis_safeguard_id(raw: str) -> str | None:
    """'5.1' -> 'CIS-5.1'"""
    m = CIS_SAFEGUARD_RE.match(raw.strip())
    if m:
        return f"CIS-{m.group(1)}.{m.group(2)}"
    return None


def normalize_cobit_id(raw: str) -> str | None:
    """'APO01' -> 'COBIT-APO01', 'DSS05' -> 'COBIT-DSS05'"""
    m = COBIT_OBJ_RE.search(raw.strip())
    if m:
        return f"COBIT-{m.group(1)}{m.group(2)}"
    return None


def normalize_ccm_id(raw: str) -> str | None:
    """'IAM-04' -> 'CSA-IAM-04', 'A&A-02' -> 'CSA-AA-02'"""
    m = CCM_CTRL_RE.match(raw.strip())
    if m:
        domain = m.group(1).replace("&", "")  # A&A -> AA
        return f"CSA-{domain}-{m.group(2)}"
    return None


def normalize_cmmc_id(raw: str) -> str | None:
    """'L2-3.1.1' -> 'CMMC-L2-3.1.1'"""
    m = CMMC_PRACTICE_RE.match(raw.strip())
    if m:
        return f"CMMC-L{m.group(1)}-{m.group(2)}"
    return None


def coverage_to_confidence(coverage: str) -> float:
    """Map coverage level string to confidence value."""
    c = coverage.strip().lower()
    if c in ("full", "strong", "direct"):
        return 0.95
    if c in ("partial",):
        return 0.80
    if c in ("implicit",):
        return 0.70
    if c in ("weak", "minimal", "limited"):
        return 0.55
    if c in ("none", "--", ""):
        return 0.0
    return 0.85  # default for unlabeled


def confidence_to_coverage(conf: float) -> str:
    """Reverse map confidence to coverage label."""
    if conf >= 0.90:
        return "Full"
    if conf >= 0.75:
        return "Partial"
    if conf >= 0.60:
        return "Implicit"
    return "Weak"


def infer_family_id(node_id: str) -> str | None:
    """Infer the ControlFamily ID for a control based on its node ID."""
    if node_id.startswith("NIST-"):
        parts = node_id.split("-")
        if len(parts) >= 3:
            return f"{parts[0]}-{parts[1]}"
    elif node_id.startswith("ISO-A."):
        m = re.match(r"ISO-A\.(\d+)\.\d+", node_id)
        if m:
            return f"ISO-THEME{m.group(1)}"
    elif node_id.startswith("SOC2-"):
        base = node_id.split(".")[0]
        return base
    elif node_id.startswith("PCI-"):
        m = re.match(r"PCI-(\d+)", node_id)
        if m:
            return f"PCI-REQ{m.group(1)}"
    elif node_id.startswith("CIS-"):
        m = re.match(r"CIS-(\d+)\.\d+", node_id)
        if m:
            return f"CIS-{int(m.group(1)):02d}"
    elif node_id.startswith("COBIT-"):
        m = re.match(r"COBIT-([A-Z]+)\d+", node_id)
        if m:
            return f"COBIT-{m.group(1)}"
    elif node_id.startswith("CSA-"):
        parts = node_id.split("-")
        if len(parts) >= 3:
            return f"{parts[0]}-{parts[1]}"
    elif node_id.startswith("CMMC-"):
        m = re.match(r"CMMC-L\d+-(\d+)\.(\d+)\.\d+", node_id)
        if m:
            return f"CMMC-{m.group(1)}{m.group(2)}"
    elif node_id.startswith("HIPAA-"):
        if "308" in node_id:
            return "HIPAA-ADMIN"
        if "310" in node_id:
            return "HIPAA-PHYSICAL"
        if "312" in node_id:
            return "HIPAA-TECHNICAL"
        if "314" in node_id:
            return "HIPAA-ORG"
        if "316" in node_id:
            return "HIPAA-ORG"
        # Breach Notification Rule (164.400-414)
        m = re.match(r"HIPAA-(\d+)", node_id)
        if m:
            sec = int(m.group(1))
            if 400 <= sec <= 414:
                return "HIPAA-BREACH"
    return None


def infer_framework_id(node_id: str) -> str:
    """Infer the Framework ID for a node based on its ID prefix."""
    prefixes = {
        "NIST-": "NIST-800-53",
        "ISO-": "ISO-27001",
        "SOC2-": "SOC2",
        "PCI-": "PCI-DSS",
        "CIS-": "CIS",
        "COBIT-": "COBIT",
        "CSA-": "CSA-CCM",
        "CMMC-": "CMMC",
        "HIPAA-": "HIPAA",
    }
    for prefix, fw_id in prefixes.items():
        if node_id.startswith(prefix):
            return fw_id
    return "UNKNOWN"


# ---------------------------------------------------------------------------
# Generic table parsing
# ---------------------------------------------------------------------------


def extract_table_rows(content: str) -> list[list[str]]:
    """Extract data rows from ALL markdown tables in content.

    Returns list of cell lists. Skips header rows and separator rows.
    A table is detected as: header row -> separator row -> data rows.
    """
    rows: list[list[str]] = []
    header_seen = False
    sep_seen = False

    for line in content.split("\n"):
        stripped = line.strip()
        if not stripped.startswith("|"):
            header_seen = False
            sep_seen = False
            continue

        cells = [c.strip() for c in stripped.split("|")]
        if cells and cells[0] == "":
            cells = cells[1:]
        if cells and cells[-1] == "":
            cells = cells[:-1]

        if not cells:
            continue

        is_sep = all(re.match(r"^[\s\-:]+$", c) for c in cells)

        if not header_seen:
            header_seen = True
            if is_sep:
                sep_seen = True
            continue

        if is_sep:
            sep_seen = True
            continue

        if header_seen and sep_seen:
            rows.append(cells)

    return rows


# ---------------------------------------------------------------------------
# Format-specific parsers
# ---------------------------------------------------------------------------
# Each returns list[dict] with keys: nist_id, target_id, confidence, source_file


def _is_header_row(cells: list[str], *keywords: str) -> bool:
    """Check if a table row looks like a header (contains keywords)."""
    text = " ".join(cells).lower()
    return any(kw.lower() in text for kw in keywords)


def parse_soc2(path: Path) -> list[dict]:
    """| Key NIST Controls | SOC 2 Criteria | Coverage | Notes |"""
    content = path.read_text()
    mappings: list[dict] = []

    for cells in extract_table_rows(content):
        if len(cells) < 3:
            continue
        if _is_header_row(cells, "NIST", "SOC 2", "Criteria", "Dimension"):
            continue

        nist_raw = cells[0]
        target_raw = cells[1]
        coverage = cells[2] if len(cells) > 2 else "Full"

        nist_ids = extract_nist_ids(nist_raw)
        if not nist_ids:
            continue

        targets: list[str] = []
        for chunk in re.split(r"[,;]", target_raw):
            chunk = chunk.strip()
            m = re.match(r"(CC\d+\.\d+|A\d+\.\d+|PI\d+\.\d+|C\d+\.\d+|P\d+\.\d+)", chunk)
            if m:
                targets.append(f"SOC2-{m.group(1)}")

        if not targets:
            continue

        conf = coverage_to_confidence(coverage)
        if conf == 0.0:
            continue

        for nid in nist_ids:
            for tid in targets:
                mappings.append({"nist_id": nid, "target_id": tid, "confidence": conf, "source_file": path.name})

    return mappings


def parse_iso27001(path: Path) -> list[dict]:
    """| NIST Control | NIST Title | ISO Control | ISO Title | Coverage |"""
    content = path.read_text()
    mappings: list[dict] = []

    for cells in extract_table_rows(content):
        if len(cells) < 5:
            continue
        if _is_header_row(cells, "NIST Control", "NIST Title", "ISO Control", "Dimension"):
            continue

        nist_raw = cells[0]
        iso_raw = cells[2]
        coverage_raw = cells[4]

        nist_ids = extract_nist_ids(nist_raw)
        if not nist_ids:
            continue

        targets: list[str] = []
        for chunk in re.split(r"[,;]", iso_raw):
            tid = normalize_iso_id(chunk)
            if tid:
                targets.append(tid)

        if not targets:
            continue

        conf = coverage_to_confidence(coverage_raw)
        if conf == 0.0:
            continue

        for nid in nist_ids:
            for tid in targets:
                mappings.append({"nist_id": nid, "target_id": tid, "confidence": conf, "source_file": path.name})

    return mappings


def parse_cis(path: Path) -> list[dict]:
    """| Key NIST Controls | CIS Control | CIS Safeguards | Coverage Notes |"""
    content = path.read_text()
    mappings: list[dict] = []

    for cells in extract_table_rows(content):
        if len(cells) < 3:
            continue
        if _is_header_row(cells, "Key NIST", "CIS Control", "CIS Safeguard", "IG Level", "Attribute"):
            continue

        nist_raw = cells[0]
        cis_ctrl_raw = cells[1]
        safeguards_raw = cells[2] if len(cells) > 2 else ""

        nist_ids = extract_nist_ids(nist_raw)
        if not nist_ids:
            continue

        if cis_ctrl_raw.strip() == "--":
            continue

        targets: list[str] = []
        for chunk in safeguards_raw.split(","):
            tid = normalize_cis_safeguard_id(chunk.strip())
            if tid:
                targets.append(tid)

        if not targets:
            continue

        notes = cells[3] if len(cells) > 3 else ""
        if "strong" in notes.lower():
            conf = 0.95
        elif "partial" in notes.lower() or "limited" in notes.lower():
            conf = 0.80
        else:
            conf = 0.85

        for nid in nist_ids:
            for tid in targets:
                mappings.append({"nist_id": nid, "target_id": tid, "confidence": conf, "source_file": path.name})

    return mappings


def parse_cmmc(path: Path) -> list[dict]:
    """| 800-171 Req | Description | 800-53 Control(s) | CMMC Practice |"""
    content = path.read_text()
    mappings: list[dict] = []

    for cells in extract_table_rows(content):
        if len(cells) < 4:
            continue
        if _is_header_row(cells, "800-171", "800-53", "CMMC Practice", "Requirement", "Aspect"):
            continue

        nist_raw = cells[2]
        cmmc_raw = cells[3]

        nist_ids = extract_nist_ids(nist_raw)
        if not nist_ids:
            continue

        cmmc_id = normalize_cmmc_id(cmmc_raw.strip())
        if not cmmc_id:
            continue

        for nid in nist_ids:
            mappings.append({"nist_id": nid, "target_id": cmmc_id, "confidence": 0.95, "source_file": path.name})

    return mappings


def parse_cobit(path: Path) -> list[dict]:
    """| Key NIST Controls | COBIT 2019 Objectives | Coverage Notes |"""
    content = path.read_text()
    mappings: list[dict] = []

    for cells in extract_table_rows(content):
        if len(cells) < 2:
            continue
        if _is_header_row(cells, "NIST", "COBIT", "Objective", "Dimension", "Attribute"):
            continue

        nist_raw = cells[0]
        cobit_raw = cells[1]

        nist_ids = extract_nist_ids(nist_raw)
        if not nist_ids:
            continue

        targets: list[str] = []
        for chunk in re.split(r"[,;]", cobit_raw):
            tid = normalize_cobit_id(chunk)
            if tid:
                targets.append(tid)

        targets = list(dict.fromkeys(targets))
        if not targets:
            continue

        for nid in nist_ids:
            for tid in targets:
                mappings.append({"nist_id": nid, "target_id": tid, "confidence": 0.85, "source_file": path.name})

    return mappings


def parse_csa_ccm(path: Path) -> list[dict]:
    """| NIST Controls | CSA CCM v4 Controls | Coverage Notes |"""
    content = path.read_text()
    mappings: list[dict] = []

    for cells in extract_table_rows(content):
        if len(cells) < 2:
            continue
        if _is_header_row(cells, "NIST", "CSA CCM", "CCM Domain", "Family", "Layer"):
            continue

        nist_raw = cells[0]
        ccm_raw = cells[1]

        nist_ids = extract_nist_ids(nist_raw)
        if not nist_ids:
            continue

        targets: list[str] = []

        # Handle "through" ranges like "UEM-01 through UEM-14"
        through_match = re.search(
            r"([A-Z][A-Z&]+)-(\d+)\s+through\s+([A-Z][A-Z&]+)-(\d+)", ccm_raw, re.IGNORECASE
        )
        if through_match:
            domain = through_match.group(1).replace("&", "")
            start = int(through_match.group(2))
            end = int(through_match.group(4))
            for n in range(start, end + 1):
                targets.append(f"CSA-{domain}-{n:02d}")
        else:
            for chunk in re.split(r"[,;]", ccm_raw):
                chunk = chunk.strip()
                tid = normalize_ccm_id(chunk)
                if tid:
                    targets.append(tid)
                else:
                    for m in CCM_CTRL_RE.finditer(chunk):
                        domain = m.group(1).replace("&", "")
                        targets.append(f"CSA-{domain}-{m.group(2)}")

        targets = list(dict.fromkeys(targets))
        if not targets:
            continue

        for nid in nist_ids:
            for tid in targets:
                mappings.append({"nist_id": nid, "target_id": tid, "confidence": 0.90, "source_file": path.name})

    return mappings


def parse_hipaa(path: Path) -> list[dict]:
    """| HIPAA Specification | Type | Description | NIST 800-53 Controls |

    Direction is HIPAA->NIST in the file. We reverse for NIST->HIPAA edges.
    Track section context from markdown headers to determine HIPAA node IDs.
    """
    content = path.read_text()
    mappings: list[dict] = []

    current_cfr: str | None = None
    current_standard: str | None = None
    in_table_header = False
    in_table_sep = False

    for line in content.split("\n"):
        stripped = line.strip()

        # Track CFR section from headers
        if stripped.startswith("#"):
            cfr_match = re.search(r"164\.(\d{3})", stripped)
            if cfr_match:
                current_cfr = cfr_match.group(1)
                std_match = re.search(r"164\.\d{3}\(([a-z])\)(?:\((\d+)\))?", stripped)
                if std_match:
                    letter = std_match.group(1)
                    num = std_match.group(2)
                    current_standard = f"{letter}{num}" if num else letter
                else:
                    current_standard = None
            in_table_header = False
            in_table_sep = False
            continue

        # Parse table rows
        if not stripped.startswith("|"):
            in_table_header = False
            in_table_sep = False
            continue

        cells = [c.strip() for c in stripped.split("|")]
        if cells and cells[0] == "":
            cells = cells[1:]
        if cells and cells[-1] == "":
            cells = cells[:-1]
        if not cells:
            continue

        is_sep = all(re.match(r"^[\s\-:]+$", c) for c in cells)

        if not in_table_header:
            in_table_header = True
            if is_sep:
                in_table_sep = True
            continue
        if is_sep:
            in_table_sep = True
            continue
        if not in_table_sep:
            continue

        # Data row
        if len(cells) < 3:
            continue
        if _is_header_row(cells, "HIPAA", "Specification", "Provision", "Safeguard"):
            continue

        nist_raw = cells[-1]
        nist_ids = extract_nist_ids(nist_raw)
        if not nist_ids:
            continue

        if not current_cfr:
            continue

        hipaa_spec = cells[0].strip()
        hipaa_id = _build_hipaa_id(current_cfr, current_standard, hipaa_spec)
        if not hipaa_id:
            continue

        for nid in nist_ids:
            mappings.append({"nist_id": nid, "target_id": hipaa_id, "confidence": 0.90, "source_file": path.name})

    return mappings


def _build_hipaa_id(cfr_section: str, current_standard: str | None, spec: str) -> str | None:
    """Build a HIPAA node ID from CFR section context and specification reference."""
    m = re.match(r"\(([a-z])\)(?:\((\d+)\))?", spec)
    if m:
        letter = m.group(1)
        num = m.group(2)
        if num:
            return f"HIPAA-{cfr_section}-{letter}{num}"
        else:
            return f"HIPAA-{cfr_section}-{letter}"

    m = re.search(r"164\.(\d{3})", spec)
    if m:
        return f"HIPAA-{m.group(1)}"

    if current_standard:
        return f"HIPAA-{cfr_section}-{current_standard}"

    return None


def parse_pci_dss(path: Path) -> list[dict]:
    """| NIST Control | Title | PCI DSS v4 Requirement | Coverage Notes |"""
    content = path.read_text()
    mappings: list[dict] = []

    for cells in extract_table_rows(content):
        if len(cells) < 3:
            continue
        if _is_header_row(cells, "NIST Control", "PCI DSS", "Dimension", "Req ", "Coverage Gap"):
            continue

        nist_raw = cells[0]
        pci_raw = cells[2]

        nist_ids = extract_nist_ids(nist_raw)
        if not nist_ids:
            continue

        targets: list[str] = []
        for chunk in pci_raw.split(","):
            tid = normalize_pci_id(chunk.strip())
            if tid:
                targets.append(tid)

        targets = list(dict.fromkeys(targets))
        if not targets:
            continue

        for nid in nist_ids:
            for tid in targets:
                mappings.append({"nist_id": nid, "target_id": tid, "confidence": 0.90, "source_file": path.name})

    return mappings


# Parser dispatch map
PARSERS: dict[str, callable] = {
    "nist-to-soc2.md": parse_soc2,
    "nist-to-iso27001.md": parse_iso27001,
    "nist-to-cis.md": parse_cis,
    "nist-to-cmmc.md": parse_cmmc,
    "nist-to-cobit.md": parse_cobit,
    "nist-to-csa-ccm.md": parse_csa_ccm,
    "nist-to-hipaa.md": parse_hipaa,
    "nist-to-pci-dss.md": parse_pci_dss,
}


# ---------------------------------------------------------------------------
# Graph expansion
# ---------------------------------------------------------------------------


def expand_graph() -> dict:
    """Parse all mapping files and return expanded mapping data."""
    mapping_files = sorted(MAPPINGS_DIR.glob("nist-to-*.md"))
    all_mappings: list[dict] = []

    for mf in mapping_files:
        parser = PARSERS.get(mf.name)
        if parser:
            mappings = parser(mf)
            all_mappings.extend(mappings)
            print(f"  {mf.name}: {len(mappings)} edges")
        else:
            print(f"  {mf.name}: skipped (no parser)")

    print(f"\nTotal raw mappings: {len(all_mappings)}")

    # Deduplicate
    seen: set[tuple[str, str]] = set()
    deduped: list[dict] = []
    for m in all_mappings:
        key = (m["nist_id"], m["target_id"])
        if key not in seen:
            seen.add(key)
            deduped.append(m)

    print(f"After dedup: {len(deduped)} unique edges")

    by_framework: dict[str, int] = defaultdict(int)
    for m in deduped:
        by_framework[infer_framework_id(m["target_id"])] += 1

    return {
        "total_edges": len(deduped),
        "by_framework": dict(by_framework),
        "mappings": deduped,
    }


# ---------------------------------------------------------------------------
# Node generation
# ---------------------------------------------------------------------------

CMMC_FAMILY_LABELS: dict[str, str] = {
    "CMMC-31": "3.1 Access Control",
    "CMMC-32": "3.2 Awareness and Training",
    "CMMC-33": "3.3 Audit and Accountability",
    "CMMC-34": "3.4 Configuration Management",
    "CMMC-35": "3.5 Identification and Authentication",
    "CMMC-36": "3.6 Incident Response",
    "CMMC-37": "3.7 Maintenance",
    "CMMC-38": "3.8 Media Protection",
    "CMMC-39": "3.9 Personnel Security",
    "CMMC-310": "3.10 Physical Protection",
    "CMMC-311": "3.11 Risk Assessment",
    "CMMC-312": "3.12 Security Assessment",
    "CMMC-313": "3.13 System and Communications Protection",
    "CMMC-314": "3.14 System and Information Integrity",
}

NIST_CONTROL_LABELS: dict[str, str] = {
    "AC-8": "System Use Notification",
    "AC-11": "Device Lock",
    "AC-12": "Session Termination",
    "AC-14": "Permitted Actions Without ID",
    "AC-18": "Wireless Access",
    "AC-19": "Access Control for Mobile Devices",
    "AC-21": "Information Sharing",
    "AC-22": "Publicly Accessible Content",
    "AT-4": "Training Records",
    "AU-4": "Audit Log Storage Capacity",
    "AU-5": "Response to Audit Logging Process Failures",
    "AU-7": "Audit Record Reduction and Report Generation",
    "AU-8": "Time Stamps",
    "AU-11": "Audit Record Retention",
    "CA-3": "Information Exchange",
    "CA-6": "Authorization",
    "CA-8": "Penetration Testing",
    "CA-9": "Internal System Connections",
    "CM-4": "Impact Analyses",
    "CM-5": "Access Restrictions for Change",
    "CM-9": "Configuration Management Plan",
    "CM-10": "Software Usage Restrictions",
    "CM-11": "User-Installed Software",
    "CP-3": "Contingency Training",
    "CP-6": "Alternate Storage Site",
    "CP-7": "Alternate Processing Site",
    "CP-8": "Telecommunications Services",
    "IA-3": "Device Identification and Authentication",
    "IA-4": "Identifier Management",
    "IA-6": "Authentication Feedback",
    "IA-11": "Re-authentication",
    "IR-3": "Incident Response Testing",
    "IR-7": "Incident Response Assistance",
    "MA-2": "Controlled Maintenance",
    "MA-3": "Maintenance Tools",
    "MA-4": "Nonlocal Maintenance",
    "MA-5": "Maintenance Personnel",
    "MP-1": "Media Protection Policy and Procedures",
    "MP-2": "Media Access",
    "MP-3": "Media Marking",
    "MP-4": "Media Storage",
    "MP-5": "Media Transport",
    "MP-6": "Media Sanitization",
    "MP-7": "Media Use",
    "PE-4": "Access Control for Transmission",
    "PE-5": "Access Control for Output Devices",
    "PE-8": "Visitor Access Records",
    "PE-9": "Power Equipment and Cabling",
    "PE-10": "Emergency Shutoff",
    "PE-11": "Emergency Power",
    "PE-12": "Emergency Lighting",
    "PE-13": "Fire Protection",
    "PE-14": "Environmental Controls",
    "PE-15": "Water Damage Protection",
    "PE-16": "Delivery and Removal",
    "PE-17": "Alternate Work Site",
    "PE-18": "Location of System Components",
    "PL-4": "Rules of Behavior",
    "PM-2": "Information Security Program Leadership Role",
    "PM-4": "Plan of Action and Milestones Process",
    "PM-5": "System Inventory",
    "PM-10": "Authorization Process",
    "PM-11": "Mission and Business Process Definition",
    "PM-14": "Testing, Training, and Monitoring",
    "PM-28": "Risk Framing",
    "PM-30": "Supply Chain Risk Management Strategy",
    "PM-31": "Continuous Monitoring Strategy",
    "PS-2": "Position Risk Designation",
    "PS-5": "Personnel Transfer",
    "PS-6": "Access Agreements",
    "PS-7": "External Personnel Security",
    "PS-8": "Personnel Sanctions",
    "PT-1": "Policy and Procedures",
    "PT-2": "Authority to Process PII",
    "PT-3": "PII Processing Purposes",
    "PT-4": "Consent",
    "PT-5": "Privacy Notice",
    "RA-2": "Security Categorization",
    "RA-7": "Risk Response",
    "RA-9": "Criticality Analysis",
    "RA-10": "Threat Hunting",
    "SA-3": "System Development Life Cycle",
    "SA-9": "External System Services",
    "SA-10": "Developer Configuration Management",
    "SA-11": "Developer Testing and Evaluation",
    "SA-15": "Development Process, Standards, and Tools",
    "SA-17": "Developer Security and Privacy Architecture",
    "SA-22": "Unsupported System Components",
    "SC-2": "Separation of User and System Functionality",
    "SC-4": "Information in Shared Resources",
    "SC-5": "Denial-of-Service Protection",
    "SC-10": "Network Disconnect",
    "SC-15": "Collaborative Computing Devices and Applications",
    "SC-17": "PKI Certificates",
    "SC-23": "Session Authenticity",
    "SC-39": "Process Isolation",
    "SI-7": "Software, Firmware, and Information Integrity",
    "SI-10": "Information Input Validation",
    "SI-11": "Error Handling",
    "SI-12": "Information Management and Retention",
    "SI-16": "Memory Protection",
    "SR-5": "Acquisition Strategies, Tools, and Methods",
    "SR-6": "Supplier Assessments and Reviews",
    "SR-8": "Notification Agreements",
    "SR-10": "Inspection of Systems or Components",
    "SR-11": "Component Authenticity",
}


def _id_to_label(ctrl_id: str) -> str:
    """Generate a human-readable label from a control ID."""
    if ctrl_id.startswith("NIST-"):
        base = ctrl_id.replace("NIST-", "")
        extra = NIST_CONTROL_LABELS.get(base, "")
        return f"{base} {extra}".strip()
    if ctrl_id.startswith("ISO-"):
        return ctrl_id.replace("ISO-", "")
    if ctrl_id.startswith("SOC2-"):
        return ctrl_id.replace("SOC2-", "")
    if ctrl_id.startswith("PCI-"):
        return f"Requirement {ctrl_id.replace('PCI-', '')}"
    if ctrl_id.startswith("CIS-"):
        return f"Safeguard {ctrl_id.replace('CIS-', '')}"
    if ctrl_id.startswith("COBIT-"):
        return ctrl_id.replace("COBIT-", "")
    if ctrl_id.startswith("CSA-"):
        return ctrl_id.replace("CSA-", "")
    if ctrl_id.startswith("CMMC-"):
        return ctrl_id.replace("CMMC-", "")
    if ctrl_id.startswith("HIPAA-"):
        return ctrl_id.replace("HIPAA-", "")
    return ctrl_id


def generate_missing_nodes(
    mappings: list[dict], existing_ids: set[str]
) -> dict[str, list[dict]]:
    """Generate new node definitions for controls found in mappings but missing from graph."""
    new_controls: list[dict] = []
    new_families: list[dict] = []

    all_control_ids: set[str] = set()
    for m in mappings:
        all_control_ids.add(m["nist_id"])
        all_control_ids.add(m["target_id"])

    missing = all_control_ids - existing_ids
    needed_family_ids: set[str] = set()

    for ctrl_id in sorted(missing):
        family_id = infer_family_id(ctrl_id)
        framework_id = infer_framework_id(ctrl_id)

        if not family_id:
            continue

        label = _id_to_label(ctrl_id)

        new_controls.append({
            "id": ctrl_id,
            "type": "Control",
            "label": label,
            "family_id": family_id,
            "framework_id": framework_id,
        })

        if family_id not in existing_ids:
            needed_family_ids.add(family_id)

    for fam_id in sorted(needed_family_ids):
        if fam_id.startswith("CMMC-"):
            framework_id = "CMMC"
        else:
            framework_id = infer_framework_id(fam_id)
        label = CMMC_FAMILY_LABELS.get(fam_id, fam_id)

        new_families.append({
            "id": fam_id,
            "type": "ControlFamily",
            "label": label,
            "framework_id": framework_id,
        })

    return {"controls": new_controls, "families": new_families}


# ---------------------------------------------------------------------------
# Merge and write
# ---------------------------------------------------------------------------

FW_TO_FAMILY_SECTION: dict[str, str] = {
    "CMMC": "cmmc", "COBIT": "cobit", "CSA-CCM": "csa_ccm",
    "HIPAA": "hipaa", "PCI-DSS": "pci_dss", "CIS": "cis",
    "ISO-27001": "iso27001", "SOC2": "soc2", "NIST-800-53": "nist",
}

FW_TO_CTRL_SECTION: dict[str, str] = {
    "NIST-800-53": "nist_controls", "SOC2": "soc2_controls",
    "ISO-27001": "iso_controls", "PCI-DSS": "pci_controls",
    "HIPAA": "hipaa_controls", "CIS": "cis_controls",
    "COBIT": "cobit_controls", "CSA-CCM": "csa_ccm_controls",
    "CMMC": "cmmc_controls",
}

FW_TO_EDGE_SECTION: dict[str, str] = {
    "SOC2": "nist_to_soc2", "ISO-27001": "nist_to_iso27001",
    "HIPAA": "nist_to_hipaa", "PCI-DSS": "nist_to_pci",
    "CIS": "nist_to_cis", "COBIT": "nist_to_cobit",
    "CSA-CCM": "nist_to_csa_ccm", "CMMC": "nist_to_cmmc",
}


def write_expanded_graph(result: dict) -> None:
    """Merge expanded data into nodes.json and edges.json and write to disk."""
    nodes = load_json(NODES_PATH)
    edges = load_json(EDGES_PATH)

    existing_ids = collect_all_node_ids(nodes)
    mappings = result["mappings"]

    new_data = generate_missing_nodes(mappings, existing_ids)
    new_controls = new_data["controls"]
    new_families = new_data["families"]

    print(f"\n  New control nodes: {len(new_controls)}")
    print(f"  New family nodes:  {len(new_families)}")

    # --- Merge new families ---
    families_section = nodes.setdefault("control_families", {})
    for fam in new_families:
        section_key = FW_TO_FAMILY_SECTION.get(fam["framework_id"], fam["framework_id"].lower())
        if section_key not in families_section:
            families_section[section_key] = []
        if not isinstance(families_section[section_key], list):
            continue
        existing = {f["id"] for f in families_section[section_key]}
        if fam["id"] not in existing:
            families_section[section_key].append(fam)

    # --- Merge new controls ---
    controls_section = nodes.setdefault("controls", {})
    for ctrl in new_controls:
        section_key = FW_TO_CTRL_SECTION.get(
            ctrl["framework_id"], f"{ctrl['framework_id'].lower()}_controls"
        )
        if section_key not in controls_section:
            controls_section[section_key] = []
        if not isinstance(controls_section[section_key], list):
            continue
        existing = {c["id"] for c in controls_section[section_key]}
        if ctrl["id"] not in existing:
            controls_section[section_key].append(ctrl)

    # --- Build MAPS_TO edges ---
    plane_mapping = edges.setdefault("plane_mapping", {})
    existing_mapping_edges: set[tuple[str, str]] = set()
    for section_key, section_data in plane_mapping.items():
        if section_key.startswith("_"):
            continue
        if isinstance(section_data, list):
            for e in section_data:
                existing_mapping_edges.add((e["s"], e["o"]))

    new_edge_count = 0
    for m in mappings:
        key = (m["nist_id"], m["target_id"])
        if key in existing_mapping_edges:
            continue

        fw = infer_framework_id(m["target_id"])
        section_key = FW_TO_EDGE_SECTION.get(fw, f"nist_to_{fw.lower()}")

        if section_key not in plane_mapping:
            plane_mapping[section_key] = []

        edge = {
            "s": m["nist_id"],
            "p": "MAPS_TO",
            "o": m["target_id"],
            "confidence": m["confidence"],
            "meta": {
                "coverage": confidence_to_coverage(m["confidence"]),
                "source": m["source_file"],
            },
        }
        plane_mapping[section_key].append(edge)
        existing_mapping_edges.add(key)
        new_edge_count += 1

    print(f"  New MAPS_TO edges: {new_edge_count}")

    # --- Add CONTAINS edges for new nodes ---
    all_ids_after = collect_all_node_ids(nodes)
    compliance = edges.setdefault("plane_compliance", {})
    family_to_ctrl = compliance.setdefault("family_to_control", [])
    fw_to_family = compliance.setdefault("framework_to_family", [])

    existing_contains = {(e["s"], e["o"]) for e in family_to_ctrl}
    existing_fw_contains = {(e["s"], e["o"]) for e in fw_to_family}

    new_contains = 0
    for ctrl in new_controls:
        fam_id = ctrl["family_id"]
        if fam_id in all_ids_after:
            key = (fam_id, ctrl["id"])
            if key not in existing_contains:
                family_to_ctrl.append(
                    {"s": fam_id, "p": "CONTAINS", "o": ctrl["id"], "confidence": 1.0}
                )
                existing_contains.add(key)
                new_contains += 1

    for fam in new_families:
        fw_id = fam["framework_id"]
        key = (fw_id, fam["id"])
        if key not in existing_fw_contains:
            fw_to_family.append(
                {"s": fw_id, "p": "CONTAINS", "o": fam["id"], "confidence": 1.0}
            )
            existing_fw_contains.add(key)
            new_contains += 1

    print(f"  New CONTAINS edges: {new_contains}")

    # --- Update metadata ---
    all_ids_final = collect_all_node_ids(nodes)
    all_edges_final = collect_all_edges(edges)
    nodes["_meta"]["node_count"] = len(all_ids_final)

    # --- Write files ---
    with open(NODES_PATH, "w") as f:
        json.dump(nodes, f, indent=2, ensure_ascii=False)
        f.write("\n")

    with open(EDGES_PATH, "w") as f:
        json.dump(edges, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\n  Written {NODES_PATH.name}: {len(all_ids_final)} nodes")
    print(f"  Written {EDGES_PATH.name}: {len(all_edges_final)} edges")


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
            print("\nWriting expanded graph...")
            write_expanded_graph(result)

            print("\nPost-write validation...")
            node_count, edge_count, errors = validate_graph()
            print(f"  Nodes: {node_count}, Edges: {edge_count}")
            if errors:
                print(f"\n  WARNINGS ({len(errors)}):")
                for e in errors[:20]:
                    print(f"    - {e}")
                if len(errors) > 20:
                    print(f"    ... and {len(errors) - 20} more")
            else:
                print("  All validations passed.")
        else:
            print("\nDry run. Add --write to persist changes.")

    else:
        print("GRC Knowledge Graph Seeder")
        print("=" * 40)
        print()

        nodes = load_json(NODES_PATH)
        edges = load_json(EDGES_PATH)

        all_ids = collect_all_node_ids(nodes)
        all_edges = collect_all_edges(edges)

        print(f"Graph Statistics:")
        print(f"  Nodes: {len(all_ids)}")
        print(f"  Edges: {len(all_edges)}")
        print(f"  Frameworks: {len(nodes.get('frameworks', []))}")

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
