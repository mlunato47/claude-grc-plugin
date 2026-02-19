#!/usr/bin/env python3
"""GRC Knowledge Graph Viewer — development server.

Serves the KG visualization UI and provides a JSON API for the graph data.

Usage:
    python tools/visualize/serve.py          # http://localhost:8765
    python tools/visualize/serve.py 9000     # custom port
"""

from __future__ import annotations

import json
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
GRAPH_DIR = REPO_ROOT / "grc" / "skills" / "grc-knowledge" / "graph"
HTML_PATH = Path(__file__).resolve().parent / "kg_viewer.html"


def load_json(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def flatten_nodes(raw: dict) -> list[dict]:
    """Convert nested nodes.json into flat array of {id, type, label, props}."""
    result: list[dict] = []

    for fw in raw.get("frameworks", []):
        result.append({
            "id": fw["id"], "type": fw["type"], "label": fw["label"],
            "props": {k: v for k, v in fw.items() if k not in ("id", "type", "label")},
        })

    for section in raw.get("control_families", {}).values():
        if isinstance(section, list):
            for cf in section:
                result.append({
                    "id": cf["id"], "type": cf["type"], "label": cf["label"],
                    "props": {k: v for k, v in cf.items() if k not in ("id", "type", "label")},
                })

    for section in raw.get("controls", {}).values():
        if isinstance(section, list):
            for ctrl in section:
                result.append({
                    "id": ctrl["id"], "type": ctrl["type"], "label": ctrl["label"],
                    "props": {k: v for k, v in ctrl.items() if k not in ("id", "type", "label")},
                })

    for bl in raw.get("baselines", []):
        result.append({
            "id": bl["id"], "type": bl["type"], "label": bl["label"],
            "props": {k: v for k, v in bl.items() if k not in ("id", "type", "label")},
        })

    for sm in raw.get("service_models", []):
        result.append({
            "id": sm["id"], "type": sm["type"], "label": sm["label"],
            "props": {k: v for k, v in sm.items() if k not in ("id", "type", "label")},
        })

    for ev in raw.get("evidence_types", []):
        result.append({
            "id": ev["id"], "type": ev["type"], "label": ev["label"],
            "props": {k: v for k, v in ev.items() if k not in ("id", "type", "label")},
        })

    for dt in raw.get("document_types", []):
        result.append({
            "id": dt["id"], "type": dt["type"], "label": dt["label"],
            "props": {k: v for k, v in dt.items() if k not in ("id", "type", "label")},
        })

    return result


PLANE_NAME_MAP = {
    "plane_compliance": "COMPLIANCE",
    "plane_mapping": "MAPPING",
    "plane_responsibility": "RESPONSIBILITY",
    "plane_evidence": "EVIDENCE",
}


def flatten_edges(raw: dict) -> list[dict]:
    """Convert nested edges.json into flat array of {source, target, predicate, plane, confidence, meta}."""
    result: list[dict] = []

    for plane_key, plane_data in raw.items():
        if plane_key.startswith("_") or not isinstance(plane_data, dict):
            continue
        plane_name = PLANE_NAME_MAP.get(plane_key, plane_key.upper())
        for section_key, section_data in plane_data.items():
            if section_key.startswith("_") or not isinstance(section_data, list):
                continue
            for edge in section_data:
                result.append({
                    "source": edge["s"],
                    "target": edge["o"],
                    "predicate": edge["p"],
                    "plane": plane_name,
                    "confidence": edge.get("confidence", 1.0),
                    "meta": edge.get("meta", {}),
                })

    return result


_graph_cache: bytes | None = None


def build_graph_payload() -> bytes:
    global _graph_cache
    if _graph_cache is not None:
        return _graph_cache

    nodes_raw = load_json(GRAPH_DIR / "nodes.json")
    edges_raw = load_json(GRAPH_DIR / "edges.json")
    schema = load_json(GRAPH_DIR / "schema.json")

    payload = {
        "nodes": flatten_nodes(nodes_raw),
        "edges": flatten_edges(edges_raw),
        "planes": schema.get("planes", {}),
        "predicates": schema.get("predicates", {}),
        "scoring": schema.get("scoring", {}),
    }
    _graph_cache = json.dumps(payload).encode()
    return _graph_cache


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/api/graph":
            data = build_graph_payload()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        elif self.path in ("/", "/index.html"):
            content = HTML_PATH.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_error(404)

    def log_message(self, format: str, *args) -> None:
        # Quieter logging
        pass


def main() -> None:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    server = HTTPServer(("", port), Handler)
    print(f"GRC Knowledge Graph Viewer")
    print(f"  http://localhost:{port}")
    print(f"  {len(flatten_nodes(load_json(GRAPH_DIR / 'nodes.json')))} nodes, "
          f"{len(flatten_edges(load_json(GRAPH_DIR / 'edges.json')))} edges")
    print(f"\nPress Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
