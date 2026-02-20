#!/usr/bin/env python3
"""GRC Knowledge Graph Viewer — development server.

Serves the KG visualization UI and provides a JSON API for the graph data.

Usage:
    python tools/visualize/serve.py          # http://localhost:8765
    python tools/visualize/serve.py 9000     # custom port
"""

from __future__ import annotations

import json
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
GRAPH_DIR = REPO_ROOT / "grc" / "skills" / "grc-knowledge" / "graph"
DIST_DIR = Path(__file__).resolve().parent / "app" / "dist"

MIME_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".js": "application/javascript",
    ".css": "text/css",
    ".json": "application/json",
    ".png": "image/png",
    ".svg": "image/svg+xml",
    ".ico": "image/x-icon",
    ".woff": "font/woff",
    ".woff2": "font/woff2",
}


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

    nodes = flatten_nodes(nodes_raw)
    edges = flatten_edges(edges_raw)

    # Compute stats breakdown
    type_counts = {}
    for n in nodes:
        type_counts[n["type"]] = type_counts.get(n["type"], 0) + 1
    pred_counts = {}
    for e in edges:
        pred_counts[e["predicate"]] = pred_counts.get(e["predicate"], 0) + 1

    payload = {
        "nodes": nodes,
        "edges": edges,
        "planes": schema.get("planes", {}),
        "predicates": schema.get("predicates", {}),
        "scoring": schema.get("scoring", {}),
        "stats": {
            "node_types": type_counts,
            "edge_predicates": pred_counts,
        },
    }
    _graph_cache = json.dumps(payload).encode()
    return _graph_cache


def build_system_prompt() -> str:
    """Build a system prompt containing the full graph schema and data."""
    schema = load_json(GRAPH_DIR / "schema.json")
    nodes_raw = load_json(GRAPH_DIR / "nodes.json")
    edges_raw = load_json(GRAPH_DIR / "edges.json")

    nodes = flatten_nodes(nodes_raw)
    edges = flatten_edges(edges_raw)

    # Compact representations to save tokens
    compact_nodes = [
        {"id": n["id"], "type": n["type"], "label": n["label"]}
        for n in nodes
    ]
    compact_edges = [
        {"s": e["source"], "o": e["target"], "p": e["predicate"], "plane": e["plane"]}
        for e in edges
    ]

    return f"""You are the GRC Knowledge Graph assistant. You answer questions about governance, risk, and compliance (GRC) frameworks, controls, mappings, baselines, evidence requirements, and responsibility models — all based on the knowledge graph loaded in this viewer.

## Graph Schema

Node types: {json.dumps(list(schema["node_types"].keys()))}
Predicates: {json.dumps(list(schema["predicates"].keys()))}
Planes: {json.dumps({k: v["description"] for k, v in schema["planes"].items()})}

## Graph Data ({len(nodes)} nodes, {len(edges)} edges)

Nodes:
{json.dumps(compact_nodes, separators=(",", ":"))}

Edges:
{json.dumps(compact_edges, separators=(",", ":"))}

## Instructions

- When referencing node IDs, always use the exact ID from the graph (e.g., NIST-AC-2, SOC2-CC6.1). Users can click these to navigate the graph.
- Be concise and factual. Ground every answer in the graph data above.
- If asked about cross-framework mappings, trace through MAPS_TO edges.
- If asked about baselines (e.g., "FedRAMP Moderate controls"), use ASSIGNED_TO edges.
- If asked about evidence requirements, use REQUIRES_EVIDENCE edges.
- If asked about responsibility/shared responsibility, use RESPONSIBILITY_OF edges.
- If asked where controls are documented, use DOCUMENTED_IN edges.
- If a question cannot be answered from the graph, say so clearly.
- Format responses in markdown. Use bullet lists and tables when helpful."""


_anthropic_client = None


def get_anthropic_client():
    """Lazy-init the Anthropic client. Returns None if no API key."""
    global _anthropic_client
    if _anthropic_client is not None:
        return _anthropic_client
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None
    try:
        import anthropic
        _anthropic_client = anthropic.Anthropic(api_key=api_key)
        return _anthropic_client
    except ImportError:
        return None


_system_prompt_cache: str | None = None


def get_system_prompt() -> str:
    global _system_prompt_cache
    if _system_prompt_cache is None:
        _system_prompt_cache = build_system_prompt()
    return _system_prompt_cache


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/api/graph":
            data = build_graph_payload()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        else:
            self._serve_static()

    def _serve_static(self) -> None:
        """Serve files from dist/, with SPA fallback to index.html."""
        # Strip query string
        path = self.path.split("?")[0]
        if path == "/":
            path = "/index.html"

        file_path = DIST_DIR / path.lstrip("/")

        # If file doesn't exist, SPA fallback
        if not file_path.is_file():
            file_path = DIST_DIR / "index.html"

        if not file_path.is_file():
            self.send_error(404, f"dist/ not found — run 'npm run build' in tools/visualize/app/")
            return

        content = file_path.read_bytes()
        content_type = MIME_TYPES.get(file_path.suffix, "application/octet-stream")
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self) -> None:
        if self.path == "/api/chat":
            self._handle_chat()
        else:
            self.send_error(404)

    def _handle_chat(self) -> None:
        # Read request body
        content_length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(content_length))

        messages = body.get("messages", [])
        selected_node = body.get("selectedNode")

        if not messages:
            self.send_error(400, "No messages provided")
            return

        client = get_anthropic_client()
        if client is None:
            self.send_response(503)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            error_msg = "anthropic package not installed" if os.environ.get("ANTHROPIC_API_KEY") else "ANTHROPIC_API_KEY not set"
            self.wfile.write(json.dumps({"error": error_msg}).encode())
            return

        # Build system prompt with optional selected node context
        system = get_system_prompt()
        if selected_node:
            system += f"\n\n## Currently Selected Node\nThe user has selected node **{selected_node}** in the graph viewer. Use this context when relevant."

        # Stream from Claude via SSE
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.end_headers()

        try:
            with client.messages.stream(
                model="claude-sonnet-4-20250514",
                max_tokens=2048,
                system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
                messages=messages,
            ) as stream:
                for text in stream.text_stream:
                    # SSE format: data: <json>\n\n
                    chunk = json.dumps({"type": "delta", "text": text})
                    self.wfile.write(f"data: {chunk}\n\n".encode())
                    self.wfile.flush()

            # Send done event
            self.wfile.write(b"data: {\"type\":\"done\"}\n\n")
            self.wfile.flush()
        except Exception as e:
            error_chunk = json.dumps({"type": "error", "text": str(e)})
            self.wfile.write(f"data: {error_chunk}\n\n".encode())
            self.wfile.flush()

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
