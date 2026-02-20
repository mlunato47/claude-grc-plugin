#!/usr/bin/env python3
"""GRC Knowledge Graph Upgrade — Populates baseline, evidence, responsibility,
and documentation planes plus GDPR/NIST-800-171 framework controls.

Reads existing nodes.json/edges.json, generates ~3,000 new edges and ~170 new
nodes, merges them, validates, and writes.

Usage:
    python tools/upgrade_graph.py --preview    # Dry run — prints summary
    python tools/upgrade_graph.py --write      # Generate + write + validate
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Bootstrap imports from seed_graph.py
# ---------------------------------------------------------------------------

sys.path.insert(0, str(Path(__file__).resolve().parent))
from seed_graph import (  # noqa: E402
    load_json,
    collect_all_node_ids,
    collect_all_edges,
    validate_graph,
    infer_family_id,
    infer_framework_id,
    GRAPH_DIR,
    NODES_PATH,
    EDGES_PATH,
    SCHEMA_PATH,
)

NEW_REVISION = "grc-kg-rev-002"

# ═══════════════════════════════════════════════════════════════════════════
# Phase 1 — NIST SP 800-53B Baselines (Low / Moderate / High)
# ═══════════════════════════════════════════════════════════════════════════


def phase_nist_baselines() -> tuple[list[dict], list[dict]]:
    """Add 3 Baseline nodes: NIST-LOW, NIST-MODERATE, NIST-HIGH."""
    nodes = [
        {
            "id": "NIST-LOW",
            "type": "Baseline",
            "label": "NIST 800-53 Low Baseline",
            "framework_id": "NIST-800-53",
            "level_ordinal": 1,
        },
        {
            "id": "NIST-MODERATE",
            "type": "Baseline",
            "label": "NIST 800-53 Moderate Baseline",
            "framework_id": "NIST-800-53",
            "level_ordinal": 2,
        },
        {
            "id": "NIST-HIGH",
            "type": "Baseline",
            "label": "NIST 800-53 High Baseline",
            "framework_id": "NIST-800-53",
            "level_ordinal": 3,
        },
    ]
    return nodes, []


# ═══════════════════════════════════════════════════════════════════════════
# Phase 2 — GDPR Control Families + Controls
# ═══════════════════════════════════════════════════════════════════════════

# Operationally relevant GDPR articles (Chapters 2–5)
GDPR_FAMILIES: list[dict] = [
    {"id": "GDPR-CH2", "label": "Chapter 2 — Principles", "focus": "Lawfulness, purpose limitation, data minimisation, accuracy, storage limitation, integrity, accountability"},
    {"id": "GDPR-CH3", "label": "Chapter 3 — Data Subject Rights", "focus": "Transparency, access, rectification, erasure, portability, objection"},
    {"id": "GDPR-CH4", "label": "Chapter 4 — Controller and Processor", "focus": "Obligations, DPbD, records, security, breach notification, DPIA, DPO"},
    {"id": "GDPR-CH5", "label": "Chapter 5 — Transfers to Third Countries", "focus": "Adequacy, safeguards, BCRs, derogations"},
    {"id": "GDPR-CH6", "label": "Chapter 6 — Supervisory Authorities", "focus": "Independence, competence, tasks, powers"},
    {"id": "GDPR-CH7", "label": "Chapter 7 — Cooperation and Consistency", "focus": "Lead authority, mutual assistance, consistency mechanism"},
]

GDPR_CONTROLS: list[dict] = [
    # Chapter 2 — Principles
    {"id": "GDPR-ART5",  "label": "Art 5 Principles relating to processing of personal data", "family_id": "GDPR-CH2"},
    {"id": "GDPR-ART6",  "label": "Art 6 Lawfulness of processing",                         "family_id": "GDPR-CH2"},
    {"id": "GDPR-ART7",  "label": "Art 7 Conditions for consent",                            "family_id": "GDPR-CH2"},
    {"id": "GDPR-ART8",  "label": "Art 8 Conditions for child consent",                      "family_id": "GDPR-CH2"},
    {"id": "GDPR-ART9",  "label": "Art 9 Processing of special categories",                  "family_id": "GDPR-CH2"},
    {"id": "GDPR-ART10", "label": "Art 10 Processing of criminal conviction data",            "family_id": "GDPR-CH2"},
    {"id": "GDPR-ART11", "label": "Art 11 Processing not requiring identification",           "family_id": "GDPR-CH2"},
    # Chapter 3 — Data Subject Rights
    {"id": "GDPR-ART12", "label": "Art 12 Transparent information and communication",         "family_id": "GDPR-CH3"},
    {"id": "GDPR-ART13", "label": "Art 13 Information to be provided (direct collection)",    "family_id": "GDPR-CH3"},
    {"id": "GDPR-ART14", "label": "Art 14 Information to be provided (indirect collection)",  "family_id": "GDPR-CH3"},
    {"id": "GDPR-ART15", "label": "Art 15 Right of access",                                   "family_id": "GDPR-CH3"},
    {"id": "GDPR-ART16", "label": "Art 16 Right to rectification",                            "family_id": "GDPR-CH3"},
    {"id": "GDPR-ART17", "label": "Art 17 Right to erasure (right to be forgotten)",          "family_id": "GDPR-CH3"},
    {"id": "GDPR-ART18", "label": "Art 18 Right to restriction of processing",                "family_id": "GDPR-CH3"},
    {"id": "GDPR-ART19", "label": "Art 19 Notification obligation regarding rectification/erasure", "family_id": "GDPR-CH3"},
    {"id": "GDPR-ART20", "label": "Art 20 Right to data portability",                         "family_id": "GDPR-CH3"},
    {"id": "GDPR-ART21", "label": "Art 21 Right to object",                                   "family_id": "GDPR-CH3"},
    {"id": "GDPR-ART22", "label": "Art 22 Automated individual decision-making, including profiling", "family_id": "GDPR-CH3"},
    {"id": "GDPR-ART23", "label": "Art 23 Restrictions",                                      "family_id": "GDPR-CH3"},
    # Chapter 4 — Controller and Processor
    {"id": "GDPR-ART24", "label": "Art 24 Responsibility of the controller",                  "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART25", "label": "Art 25 Data protection by design and by default",          "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART26", "label": "Art 26 Joint controllers",                                 "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART27", "label": "Art 27 Representatives of non-EU controllers/processors",  "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART28", "label": "Art 28 Processor",                                         "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART29", "label": "Art 29 Processing under authority of controller/processor", "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART30", "label": "Art 30 Records of processing activities",                  "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART31", "label": "Art 31 Cooperation with supervisory authority",            "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART32", "label": "Art 32 Security of processing",                            "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART33", "label": "Art 33 Notification of breach to supervisory authority",   "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART34", "label": "Art 34 Communication of breach to data subject",           "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART35", "label": "Art 35 Data protection impact assessment",                 "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART36", "label": "Art 36 Prior consultation",                                "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART37", "label": "Art 37 Designation of the data protection officer",        "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART38", "label": "Art 38 Position of the data protection officer",           "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART39", "label": "Art 39 Tasks of the data protection officer",              "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART40", "label": "Art 40 Codes of conduct",                                  "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART41", "label": "Art 41 Monitoring of approved codes of conduct",           "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART42", "label": "Art 42 Certification",                                     "family_id": "GDPR-CH4"},
    {"id": "GDPR-ART43", "label": "Art 43 Certification bodies",                              "family_id": "GDPR-CH4"},
    # Chapter 5 — Transfers
    {"id": "GDPR-ART44", "label": "Art 44 General principle for transfers",                    "family_id": "GDPR-CH5"},
    {"id": "GDPR-ART45", "label": "Art 45 Transfers on basis of adequacy decision",           "family_id": "GDPR-CH5"},
    {"id": "GDPR-ART46", "label": "Art 46 Transfers subject to appropriate safeguards",       "family_id": "GDPR-CH5"},
    {"id": "GDPR-ART47", "label": "Art 47 Binding corporate rules",                           "family_id": "GDPR-CH5"},
    {"id": "GDPR-ART49", "label": "Art 49 Derogations for specific situations",               "family_id": "GDPR-CH5"},
]


def phase_gdpr_controls() -> tuple[list[dict], list[dict]]:
    """Add GDPR ControlFamily + Control nodes and CONTAINS edges."""
    new_nodes: list[dict] = []
    new_edges: list[dict] = []

    for fam in GDPR_FAMILIES:
        new_nodes.append({
            "id": fam["id"],
            "type": "ControlFamily",
            "label": fam["label"],
            "framework_id": "GDPR",
            "focus": fam["focus"],
        })
        new_edges.append({"s": "GDPR", "p": "CONTAINS", "o": fam["id"], "confidence": 1.0})

    for ctrl in GDPR_CONTROLS:
        new_nodes.append({
            "id": ctrl["id"],
            "type": "Control",
            "label": ctrl["label"],
            "family_id": ctrl["family_id"],
            "framework_id": "GDPR",
        })
        new_edges.append({"s": ctrl["family_id"], "p": "CONTAINS", "o": ctrl["id"], "confidence": 1.0})

    return new_nodes, new_edges


# ═══════════════════════════════════════════════════════════════════════════
# Phase 3 — NIST 800-171 Control Families + Controls + MAPS_TO
# ═══════════════════════════════════════════════════════════════════════════

# 800-171 Rev 2 requirement families and counts
N171_FAMILIES: list[dict] = [
    {"id": "N171-31",  "label": "3.1 Access Control",                         "focus": "Limit access, enforce flow, separation, least privilege, remote access, wireless, mobile, external, PII"},
    {"id": "N171-32",  "label": "3.2 Awareness and Training",                 "focus": "Security awareness, role-based training"},
    {"id": "N171-33",  "label": "3.3 Audit and Accountability",               "focus": "Create/retain/review audit records"},
    {"id": "N171-34",  "label": "3.4 Configuration Management",               "focus": "Baselines, change control, least functionality, software restrictions"},
    {"id": "N171-35",  "label": "3.5 Identification and Authentication",      "focus": "Identify/authenticate users, multi-factor, replay-resistant"},
    {"id": "N171-36",  "label": "3.6 Incident Response",                      "focus": "Establish capability, detect/report/respond"},
    {"id": "N171-37",  "label": "3.7 Maintenance",                            "focus": "Perform/control maintenance, media, personnel"},
    {"id": "N171-38",  "label": "3.8 Media Protection",                       "focus": "Protect, limit access, sanitize, transport, mark"},
    {"id": "N171-39",  "label": "3.9 Personnel Security",                     "focus": "Screen individuals, protect CUI during personnel actions"},
    {"id": "N171-310", "label": "3.10 Physical Protection",                   "focus": "Limit access, protect/monitor facility, escort visitors"},
    {"id": "N171-311", "label": "3.11 Risk Assessment",                       "focus": "Assess risk, scan vulnerabilities, remediate"},
    {"id": "N171-312", "label": "3.12 Security Assessment",                   "focus": "Assess controls, POA&M, monitor continuously"},
    {"id": "N171-313", "label": "3.13 System and Communications Protection",  "focus": "Monitor/control communications, protect boundaries, crypto"},
    {"id": "N171-314", "label": "3.14 System and Information Integrity",      "focus": "Identify/report flaws, protect from malicious code, monitor"},
]

# (requirement_id, label, family_id)
N171_CONTROLS: list[tuple[str, str, str]] = [
    # 3.1 Access Control (22)
    ("N171-3.1.1",  "Limit system access to authorized users",                           "N171-31"),
    ("N171-3.1.2",  "Limit system access to authorized transactions and functions",       "N171-31"),
    ("N171-3.1.3",  "Control CUI flow in accordance with approved authorizations",        "N171-31"),
    ("N171-3.1.4",  "Separate duties of individuals to reduce risk",                      "N171-31"),
    ("N171-3.1.5",  "Employ principle of least privilege",                                "N171-31"),
    ("N171-3.1.6",  "Use non-privileged accounts for non-security functions",             "N171-31"),
    ("N171-3.1.7",  "Prevent non-privileged users from executing privileged functions",   "N171-31"),
    ("N171-3.1.8",  "Limit unsuccessful logon attempts",                                  "N171-31"),
    ("N171-3.1.9",  "Provide privacy and security notices consistent with CUI rules",     "N171-31"),
    ("N171-3.1.10", "Use session lock with pattern-hiding displays",                      "N171-31"),
    ("N171-3.1.11", "Terminate user sessions after defined conditions",                   "N171-31"),
    ("N171-3.1.12", "Monitor and control remote access sessions",                         "N171-31"),
    ("N171-3.1.13", "Employ cryptographic mechanisms for remote access",                  "N171-31"),
    ("N171-3.1.14", "Route remote access via managed access control points",              "N171-31"),
    ("N171-3.1.15", "Authorize remote execution of privileged commands",                  "N171-31"),
    ("N171-3.1.16", "Authorize wireless access prior to allowing connections",            "N171-31"),
    ("N171-3.1.17", "Protect wireless access using authentication and encryption",        "N171-31"),
    ("N171-3.1.18", "Control connection of mobile devices",                               "N171-31"),
    ("N171-3.1.19", "Encrypt CUI on mobile devices",                                     "N171-31"),
    ("N171-3.1.20", "Verify and control external system connections",                     "N171-31"),
    ("N171-3.1.21", "Limit use of portable storage devices on external systems",          "N171-31"),
    ("N171-3.1.22", "Control CUI posted or processed on publicly accessible systems",     "N171-31"),
    # 3.2 Awareness and Training (3)
    ("N171-3.2.1",  "Ensure personnel are aware of security risks",                       "N171-32"),
    ("N171-3.2.2",  "Ensure personnel are trained to carry out responsibilities",         "N171-32"),
    ("N171-3.2.3",  "Provide security awareness training on recognizing social engineering", "N171-32"),
    # 3.3 Audit and Accountability (9)
    ("N171-3.3.1",  "Create and retain audit records",                                    "N171-33"),
    ("N171-3.3.2",  "Ensure actions can be traced to individual users",                   "N171-33"),
    ("N171-3.3.3",  "Review and update audited events",                                   "N171-33"),
    ("N171-3.3.4",  "Alert on audit logging process failure",                             "N171-33"),
    ("N171-3.3.5",  "Correlate audit record review, analysis, and reporting",             "N171-33"),
    ("N171-3.3.6",  "Provide audit record reduction and report generation",               "N171-33"),
    ("N171-3.3.7",  "Provide capability to compare and synchronize clocks",               "N171-33"),
    ("N171-3.3.8",  "Protect audit information and tools from unauthorized access",       "N171-33"),
    ("N171-3.3.9",  "Limit management of audit logging to authorized individuals",        "N171-33"),
    # 3.4 Configuration Management (9)
    ("N171-3.4.1",  "Establish and maintain baseline configurations",                     "N171-34"),
    ("N171-3.4.2",  "Establish and enforce security configuration settings",              "N171-34"),
    ("N171-3.4.3",  "Track, review, approve/disapprove, and log changes",                "N171-34"),
    ("N171-3.4.4",  "Analyze security impact of changes prior to implementation",         "N171-34"),
    ("N171-3.4.5",  "Define, document, approve, and enforce access restrictions",         "N171-34"),
    ("N171-3.4.6",  "Employ principle of least functionality",                            "N171-34"),
    ("N171-3.4.7",  "Restrict, disable, or prevent nonessential programs",                "N171-34"),
    ("N171-3.4.8",  "Apply deny-by-exception (blacklisting) policy for software",         "N171-34"),
    ("N171-3.4.9",  "Control and monitor user-installed software",                        "N171-34"),
    # 3.5 Identification and Authentication (11)
    ("N171-3.5.1",  "Identify system users, processes, or devices",                       "N171-35"),
    ("N171-3.5.2",  "Authenticate users, processes, or devices as prerequisite to access", "N171-35"),
    ("N171-3.5.3",  "Use multifactor authentication for local and network access",        "N171-35"),
    ("N171-3.5.4",  "Employ replay-resistant authentication mechanisms",                  "N171-35"),
    ("N171-3.5.5",  "Prevent reuse of identifiers for a defined period",                  "N171-35"),
    ("N171-3.5.6",  "Disable identifiers after a defined period of inactivity",           "N171-35"),
    ("N171-3.5.7",  "Enforce minimum password complexity",                                "N171-35"),
    ("N171-3.5.8",  "Prohibit password reuse for a specified number of generations",      "N171-35"),
    ("N171-3.5.9",  "Allow temporary password use for system logons with immediate change", "N171-35"),
    ("N171-3.5.10", "Store and transmit only cryptographically-protected passwords",      "N171-35"),
    ("N171-3.5.11", "Obscure feedback of authentication information",                     "N171-35"),
    # 3.6 Incident Response (3)
    ("N171-3.6.1",  "Establish operational incident-handling capability",                  "N171-36"),
    ("N171-3.6.2",  "Track, document, and report incidents",                              "N171-36"),
    ("N171-3.6.3",  "Test organizational incident response capability",                   "N171-36"),
    # 3.7 Maintenance (6)
    ("N171-3.7.1",  "Perform maintenance on organizational systems",                      "N171-37"),
    ("N171-3.7.2",  "Provide controls on tools, techniques, and personnel for maintenance", "N171-37"),
    ("N171-3.7.3",  "Ensure equipment removed for maintenance is sanitized",              "N171-37"),
    ("N171-3.7.4",  "Check media containing diagnostic programs for malicious code",      "N171-37"),
    ("N171-3.7.5",  "Require multifactor authentication for remote maintenance",          "N171-37"),
    ("N171-3.7.6",  "Supervise maintenance activities of personnel without required access", "N171-37"),
    # 3.8 Media Protection (9)
    ("N171-3.8.1",  "Protect system media containing CUI (paper and digital)",            "N171-38"),
    ("N171-3.8.2",  "Limit access to CUI on system media to authorized users",            "N171-38"),
    ("N171-3.8.3",  "Sanitize or destroy system media before disposal or reuse",          "N171-38"),
    ("N171-3.8.4",  "Mark media with CUI distribution and handling caveats",              "N171-38"),
    ("N171-3.8.5",  "Control access to media containing CUI; maintain accountability",    "N171-38"),
    ("N171-3.8.6",  "Implement cryptographic mechanisms to protect CUI on portable media", "N171-38"),
    ("N171-3.8.7",  "Control use of removable media on system components",                "N171-38"),
    ("N171-3.8.8",  "Prohibit use of portable storage when owner/origin is unknown",      "N171-38"),
    ("N171-3.8.9",  "Protect confidentiality of backup CUI at storage locations",         "N171-38"),
    # 3.9 Personnel Security (2)
    ("N171-3.9.1",  "Screen individuals prior to authorizing access to CUI systems",      "N171-39"),
    ("N171-3.9.2",  "Ensure CUI is protected during and after personnel actions",         "N171-39"),
    # 3.10 Physical Protection (6)
    ("N171-3.10.1", "Limit physical access to organizational systems",                    "N171-310"),
    ("N171-3.10.2", "Protect and monitor the physical facility",                          "N171-310"),
    ("N171-3.10.3", "Escort visitors and monitor visitor activity",                       "N171-310"),
    ("N171-3.10.4", "Maintain audit logs of physical access",                             "N171-310"),
    ("N171-3.10.5", "Control and manage physical access devices",                         "N171-310"),
    ("N171-3.10.6", "Enforce safeguarding measures for CUI at alternate work sites",      "N171-310"),
    # 3.11 Risk Assessment (3)
    ("N171-3.11.1", "Periodically assess risk to operations and assets",                  "N171-311"),
    ("N171-3.11.2", "Scan for vulnerabilities periodically and when new vulnerabilities identified", "N171-311"),
    ("N171-3.11.3", "Remediate vulnerabilities in accordance with risk assessments",      "N171-311"),
    # 3.12 Security Assessment (4)
    ("N171-3.12.1", "Periodically assess security controls",                              "N171-312"),
    ("N171-3.12.2", "Develop and implement plans of action to correct deficiencies",      "N171-312"),
    ("N171-3.12.3", "Monitor security controls on an ongoing basis",                      "N171-312"),
    ("N171-3.12.4", "Develop, document, and periodically update system security plans",   "N171-312"),
    # 3.13 System and Communications Protection (16)
    ("N171-3.13.1",  "Monitor, control, and protect communications at boundaries",        "N171-313"),
    ("N171-3.13.2",  "Employ architectural designs that promote effective security",       "N171-313"),
    ("N171-3.13.3",  "Separate user functionality from system management functionality",  "N171-313"),
    ("N171-3.13.4",  "Prevent unauthorized and unintended information transfer",          "N171-313"),
    ("N171-3.13.5",  "Implement subnetworks for publicly accessible system components",   "N171-313"),
    ("N171-3.13.6",  "Deny network communications traffic by default",                    "N171-313"),
    ("N171-3.13.7",  "Prevent remote devices from establishing non-remote connections",   "N171-313"),
    ("N171-3.13.8",  "Implement cryptographic mechanisms to prevent unauthorized disclosure", "N171-313"),
    ("N171-3.13.9",  "Terminate network connections at end of sessions",                  "N171-313"),
    ("N171-3.13.10", "Establish and manage cryptographic keys",                           "N171-313"),
    ("N171-3.13.11", "Employ FIPS-validated cryptography",                                "N171-313"),
    ("N171-3.13.12", "Prohibit remote activation of collaborative computing devices",     "N171-313"),
    ("N171-3.13.13", "Control and monitor use of mobile code",                            "N171-313"),
    ("N171-3.13.14", "Control and monitor use of VoIP technologies",                      "N171-313"),
    ("N171-3.13.15", "Protect authenticity of communications sessions",                   "N171-313"),
    ("N171-3.13.16", "Protect confidentiality of CUI at rest",                            "N171-313"),
    # 3.14 System and Information Integrity (7)
    ("N171-3.14.1", "Identify, report, and correct system flaws in a timely manner",      "N171-314"),
    ("N171-3.14.2", "Provide protection from malicious code",                             "N171-314"),
    ("N171-3.14.3", "Monitor system security alerts and advisories and take action",      "N171-314"),
    ("N171-3.14.4", "Update malicious code protection mechanisms when new releases available", "N171-314"),
    ("N171-3.14.5", "Perform periodic and real-time scans; scan files from external sources", "N171-314"),
    ("N171-3.14.6", "Monitor organizational systems including inbound/outbound traffic",  "N171-314"),
    ("N171-3.14.7", "Identify unauthorized use of organizational systems",                "N171-314"),
]

# NIST 800-171 → NIST 800-53 mappings (from SP 800-171 Rev 2 mapping table)
N171_TO_NIST53: dict[str, list[str]] = {
    "N171-3.1.1":  ["NIST-AC-2", "NIST-AC-3", "NIST-AC-17"],
    "N171-3.1.2":  ["NIST-AC-2", "NIST-AC-3"],
    "N171-3.1.3":  ["NIST-AC-4"],
    "N171-3.1.4":  ["NIST-AC-5"],
    "N171-3.1.5":  ["NIST-AC-6"],
    "N171-3.1.6":  ["NIST-AC-6"],
    "N171-3.1.7":  ["NIST-AC-6"],
    "N171-3.1.8":  ["NIST-AC-7"],
    "N171-3.1.9":  ["NIST-AC-7"],
    "N171-3.1.10": ["NIST-AC-11"],
    "N171-3.1.11": ["NIST-AC-12"],
    "N171-3.1.12": ["NIST-AC-17"],
    "N171-3.1.13": ["NIST-AC-17"],
    "N171-3.1.14": ["NIST-AC-17"],
    "N171-3.1.15": ["NIST-AC-17"],
    "N171-3.1.16": ["NIST-AC-18"],
    "N171-3.1.17": ["NIST-AC-18"],
    "N171-3.1.18": ["NIST-AC-19"],
    "N171-3.1.19": ["NIST-AC-19"],
    "N171-3.1.20": ["NIST-AC-20"],
    "N171-3.1.21": ["NIST-AC-20"],
    "N171-3.1.22": ["NIST-AC-22"],
    "N171-3.2.1":  ["NIST-AT-2"],
    "N171-3.2.2":  ["NIST-AT-3"],
    "N171-3.2.3":  ["NIST-AT-2"],
    "N171-3.3.1":  ["NIST-AU-2", "NIST-AU-3", "NIST-AU-12"],
    "N171-3.3.2":  ["NIST-AU-2", "NIST-AU-3", "NIST-AU-6"],
    "N171-3.3.3":  ["NIST-AU-2"],
    "N171-3.3.4":  ["NIST-AU-5"],
    "N171-3.3.5":  ["NIST-AU-6"],
    "N171-3.3.6":  ["NIST-AU-7"],
    "N171-3.3.7":  ["NIST-AU-8"],
    "N171-3.3.8":  ["NIST-AU-9"],
    "N171-3.3.9":  ["NIST-AU-9"],
    "N171-3.4.1":  ["NIST-CM-2"],
    "N171-3.4.2":  ["NIST-CM-6"],
    "N171-3.4.3":  ["NIST-CM-3"],
    "N171-3.4.4":  ["NIST-CM-4"],
    "N171-3.4.5":  ["NIST-CM-5"],
    "N171-3.4.6":  ["NIST-CM-7"],
    "N171-3.4.7":  ["NIST-CM-7"],
    "N171-3.4.8":  ["NIST-CM-7"],
    "N171-3.4.9":  ["NIST-CM-11"],
    "N171-3.5.1":  ["NIST-IA-2", "NIST-IA-5"],
    "N171-3.5.2":  ["NIST-IA-2", "NIST-IA-5"],
    "N171-3.5.3":  ["NIST-IA-2"],
    "N171-3.5.4":  ["NIST-IA-2"],
    "N171-3.5.5":  ["NIST-IA-4"],
    "N171-3.5.6":  ["NIST-IA-4"],
    "N171-3.5.7":  ["NIST-IA-5"],
    "N171-3.5.8":  ["NIST-IA-5"],
    "N171-3.5.9":  ["NIST-IA-5"],
    "N171-3.5.10": ["NIST-IA-5"],
    "N171-3.5.11": ["NIST-IA-6"],
    "N171-3.6.1":  ["NIST-IR-2", "NIST-IR-4", "NIST-IR-5", "NIST-IR-6"],
    "N171-3.6.2":  ["NIST-IR-6"],
    "N171-3.6.3":  ["NIST-IR-3"],
    "N171-3.7.1":  ["NIST-MA-2"],
    "N171-3.7.2":  ["NIST-MA-3"],
    "N171-3.7.3":  ["NIST-MA-2"],
    "N171-3.7.4":  ["NIST-MA-3"],
    "N171-3.7.5":  ["NIST-MA-4"],
    "N171-3.7.6":  ["NIST-MA-5"],
    "N171-3.8.1":  ["NIST-MP-2", "NIST-MP-4"],
    "N171-3.8.2":  ["NIST-MP-2"],
    "N171-3.8.3":  ["NIST-MP-6"],
    "N171-3.8.4":  ["NIST-MP-3"],
    "N171-3.8.5":  ["NIST-MP-5"],
    "N171-3.8.6":  ["NIST-MP-5"],
    "N171-3.8.7":  ["NIST-MP-7"],
    "N171-3.8.8":  ["NIST-MP-7"],
    "N171-3.8.9":  ["NIST-CP-9"],
    "N171-3.9.1":  ["NIST-PS-3"],
    "N171-3.9.2":  ["NIST-PS-4", "NIST-PS-5"],
    "N171-3.10.1": ["NIST-PE-2", "NIST-PE-3", "NIST-PE-5"],
    "N171-3.10.2": ["NIST-PE-6"],
    "N171-3.10.3": ["NIST-PE-2", "NIST-PE-3"],
    "N171-3.10.4": ["NIST-PE-8"],
    "N171-3.10.5": ["NIST-PE-3"],
    "N171-3.10.6": ["NIST-PE-17"],
    "N171-3.11.1": ["NIST-RA-3"],
    "N171-3.11.2": ["NIST-RA-5"],
    "N171-3.11.3": ["NIST-RA-5"],
    "N171-3.12.1": ["NIST-CA-2"],
    "N171-3.12.2": ["NIST-CA-5"],
    "N171-3.12.3": ["NIST-CA-7"],
    "N171-3.12.4": ["NIST-PL-2"],
    "N171-3.13.1":  ["NIST-SC-7", "NIST-SA-8"],
    "N171-3.13.2":  ["NIST-SA-8"],
    "N171-3.13.3":  ["NIST-SC-2"],
    "N171-3.13.4":  ["NIST-SC-4"],
    "N171-3.13.5":  ["NIST-SC-7"],
    "N171-3.13.6":  ["NIST-SC-7"],
    "N171-3.13.7":  ["NIST-SC-7"],
    "N171-3.13.8":  ["NIST-SC-8"],
    "N171-3.13.9":  ["NIST-SC-10"],
    "N171-3.13.10": ["NIST-SC-12"],
    "N171-3.13.11": ["NIST-SC-13"],
    "N171-3.13.12": ["NIST-SC-15"],
    "N171-3.13.13": ["NIST-SC-18"],
    "N171-3.13.14": ["NIST-SC-19"],
    "N171-3.13.15": ["NIST-SC-23"],
    "N171-3.13.16": ["NIST-SC-28"],
    "N171-3.14.1":  ["NIST-SI-2"],
    "N171-3.14.2":  ["NIST-SI-3"],
    "N171-3.14.3":  ["NIST-SI-5"],
    "N171-3.14.4":  ["NIST-SI-3"],
    "N171-3.14.5":  ["NIST-SI-3"],
    "N171-3.14.6":  ["NIST-SI-4"],
    "N171-3.14.7":  ["NIST-SI-4"],
}


def phase_nist171_controls() -> tuple[list[dict], list[dict]]:
    """Add N171 families, controls, CONTAINS edges, and MAPS_TO edges to NIST 800-53."""
    new_nodes: list[dict] = []
    new_edges: list[dict] = []

    for fam in N171_FAMILIES:
        new_nodes.append({
            "id": fam["id"],
            "type": "ControlFamily",
            "label": fam["label"],
            "framework_id": "NIST-800-171",
            "focus": fam["focus"],
        })
        new_edges.append({"s": "NIST-800-171", "p": "CONTAINS", "o": fam["id"], "confidence": 1.0})

    for ctrl_id, label, family_id in N171_CONTROLS:
        new_nodes.append({
            "id": ctrl_id,
            "type": "Control",
            "label": label,
            "family_id": family_id,
            "framework_id": "NIST-800-171",
        })
        new_edges.append({"s": family_id, "p": "CONTAINS", "o": ctrl_id, "confidence": 1.0})

    # MAPS_TO edges (N171 → NIST 800-53)
    for n171_id, nist_ids in N171_TO_NIST53.items():
        for nist_id in nist_ids:
            new_edges.append({
                "s": nist_id, "p": "MAPS_TO", "o": n171_id,
                "confidence": 0.95,
                "meta": {"coverage": "Full", "source": "nist-171-to-800-53"},
            })

    return new_nodes, new_edges


# ═══════════════════════════════════════════════════════════════════════════
# Phase 4 — ASSIGNED_TO edges (baseline assignments)
# ═══════════════════════════════════════════════════════════════════════════

# NIST 800-53B baseline selections (Low / Moderate / High)
# Only reference control IDs that exist in the current graph.
NIST_LOW_CONTROLS = [
    "NIST-AC-1", "NIST-AC-2", "NIST-AC-3", "NIST-AC-7", "NIST-AC-17",
    "NIST-AC-20", "NIST-AC-22",
    "NIST-AT-1", "NIST-AT-2",
    "NIST-AU-1", "NIST-AU-2", "NIST-AU-3", "NIST-AU-6", "NIST-AU-8", "NIST-AU-12",
    "NIST-CA-1", "NIST-CA-2", "NIST-CA-3", "NIST-CA-5", "NIST-CA-7",
    "NIST-CM-1", "NIST-CM-2", "NIST-CM-6", "NIST-CM-7", "NIST-CM-8",
    "NIST-CP-1", "NIST-CP-2", "NIST-CP-9",
    "NIST-IA-1", "NIST-IA-2", "NIST-IA-4", "NIST-IA-5", "NIST-IA-8",
    "NIST-IR-1", "NIST-IR-2", "NIST-IR-4", "NIST-IR-5", "NIST-IR-6",
    "NIST-IR-7", "NIST-IR-8",
    "NIST-MA-1", "NIST-MA-2", "NIST-MA-5",
    "NIST-MP-1", "NIST-MP-2", "NIST-MP-6", "NIST-MP-7",
    "NIST-PE-1", "NIST-PE-2", "NIST-PE-3", "NIST-PE-6", "NIST-PE-8",
    "NIST-PE-12", "NIST-PE-17",
    "NIST-PL-1", "NIST-PL-2", "NIST-PL-4",
    "NIST-PM-1", "NIST-PM-2", "NIST-PM-3", "NIST-PM-4", "NIST-PM-5",
    "NIST-PM-7", "NIST-PM-8", "NIST-PM-9", "NIST-PM-10", "NIST-PM-11",
    "NIST-PM-14", "NIST-PM-28", "NIST-PM-30", "NIST-PM-31",
    "NIST-PS-1", "NIST-PS-2", "NIST-PS-3", "NIST-PS-4", "NIST-PS-5",
    "NIST-PS-6", "NIST-PS-7", "NIST-PS-8",
    "NIST-PT-1", "NIST-PT-2", "NIST-PT-3", "NIST-PT-4", "NIST-PT-5",
    "NIST-RA-1", "NIST-RA-2", "NIST-RA-3", "NIST-RA-5", "NIST-RA-7",
    "NIST-SA-1", "NIST-SA-2", "NIST-SA-3", "NIST-SA-4", "NIST-SA-8",
    "NIST-SA-9", "NIST-SA-22",
    "NIST-SC-1", "NIST-SC-5", "NIST-SC-7", "NIST-SC-12", "NIST-SC-13",
    "NIST-SC-15", "NIST-SC-39",
    "NIST-SI-1", "NIST-SI-2", "NIST-SI-3", "NIST-SI-4", "NIST-SI-5",
    "NIST-SR-1", "NIST-SR-2", "NIST-SR-3",
]

# Moderate adds these on top of Low
NIST_MODERATE_EXTRA = [
    "NIST-AC-4", "NIST-AC-5", "NIST-AC-6", "NIST-AC-11", "NIST-AC-12",
    "NIST-AC-14", "NIST-AC-18", "NIST-AC-19", "NIST-AC-21",
    "NIST-AT-3", "NIST-AT-4",
    "NIST-AU-4", "NIST-AU-5", "NIST-AU-7", "NIST-AU-9", "NIST-AU-11",
    "NIST-CA-6", "NIST-CA-8", "NIST-CA-9",
    "NIST-CM-3", "NIST-CM-4", "NIST-CM-5", "NIST-CM-9", "NIST-CM-10", "NIST-CM-11",
    "NIST-CP-3", "NIST-CP-4", "NIST-CP-6", "NIST-CP-7", "NIST-CP-8", "NIST-CP-10",
    "NIST-IA-3", "NIST-IA-6", "NIST-IA-12",
    "NIST-IR-3",
    "NIST-MA-3", "NIST-MA-4",
    "NIST-MP-3", "NIST-MP-4", "NIST-MP-5",
    "NIST-PE-4", "NIST-PE-5", "NIST-PE-9", "NIST-PE-10", "NIST-PE-11",
    "NIST-PL-7", "NIST-PL-8",
    "NIST-PT-6",
    "NIST-RA-9", "NIST-RA-10",
    "NIST-SA-10", "NIST-SA-11", "NIST-SA-15", "NIST-SA-17",
    "NIST-SC-2", "NIST-SC-4", "NIST-SC-8", "NIST-SC-10", "NIST-SC-17",
    "NIST-SC-18", "NIST-SC-19", "NIST-SC-23", "NIST-SC-28",
    "NIST-SI-7", "NIST-SI-10", "NIST-SI-12", "NIST-SI-16",
    "NIST-SR-5", "NIST-SR-6", "NIST-SR-8", "NIST-SR-10", "NIST-SR-11",
]

# FedRAMP Low baseline (representative selection of existing controls)
FEDRAMP_LOW_CONTROLS = [
    "NIST-AC-1", "NIST-AC-2", "NIST-AC-3", "NIST-AC-7", "NIST-AC-17",
    "NIST-AC-20", "NIST-AC-22",
    "NIST-AT-1", "NIST-AT-2",
    "NIST-AU-1", "NIST-AU-2", "NIST-AU-3", "NIST-AU-6", "NIST-AU-8", "NIST-AU-12",
    "NIST-CA-1", "NIST-CA-2", "NIST-CA-3", "NIST-CA-5", "NIST-CA-7",
    "NIST-CM-1", "NIST-CM-2", "NIST-CM-6", "NIST-CM-7", "NIST-CM-8",
    "NIST-CP-1", "NIST-CP-2", "NIST-CP-9",
    "NIST-IA-1", "NIST-IA-2", "NIST-IA-4", "NIST-IA-5", "NIST-IA-8",
    "NIST-IR-1", "NIST-IR-2", "NIST-IR-4", "NIST-IR-5", "NIST-IR-6",
    "NIST-IR-7", "NIST-IR-8",
    "NIST-MA-1", "NIST-MA-2", "NIST-MA-5",
    "NIST-MP-1", "NIST-MP-2", "NIST-MP-6", "NIST-MP-7",
    "NIST-PE-1", "NIST-PE-2", "NIST-PE-3", "NIST-PE-6", "NIST-PE-8",
    "NIST-PE-12", "NIST-PE-17",
    "NIST-PL-1", "NIST-PL-2", "NIST-PL-4",
    "NIST-PM-1", "NIST-PM-5", "NIST-PM-9", "NIST-PM-10",
    "NIST-PS-1", "NIST-PS-2", "NIST-PS-3", "NIST-PS-4", "NIST-PS-5",
    "NIST-PS-6", "NIST-PS-7", "NIST-PS-8",
    "NIST-PT-1",
    "NIST-RA-1", "NIST-RA-2", "NIST-RA-3", "NIST-RA-5",
    "NIST-SA-1", "NIST-SA-2", "NIST-SA-3", "NIST-SA-4", "NIST-SA-9",
    "NIST-SC-1", "NIST-SC-5", "NIST-SC-7", "NIST-SC-12", "NIST-SC-13",
    "NIST-SC-15", "NIST-SC-39",
    "NIST-SI-1", "NIST-SI-2", "NIST-SI-3", "NIST-SI-4", "NIST-SI-5",
    "NIST-SR-1", "NIST-SR-2", "NIST-SR-3",
]

FEDRAMP_MODERATE_EXTRA = [
    "NIST-AC-4", "NIST-AC-5", "NIST-AC-6", "NIST-AC-11", "NIST-AC-12",
    "NIST-AC-14", "NIST-AC-18", "NIST-AC-19", "NIST-AC-21",
    "NIST-AT-3", "NIST-AT-4",
    "NIST-AU-4", "NIST-AU-5", "NIST-AU-7", "NIST-AU-9", "NIST-AU-11",
    "NIST-CA-6", "NIST-CA-8", "NIST-CA-9",
    "NIST-CM-3", "NIST-CM-4", "NIST-CM-5", "NIST-CM-9", "NIST-CM-10", "NIST-CM-11",
    "NIST-CP-3", "NIST-CP-4", "NIST-CP-6", "NIST-CP-7", "NIST-CP-8", "NIST-CP-10",
    "NIST-IA-3", "NIST-IA-6", "NIST-IA-12",
    "NIST-IR-3",
    "NIST-MA-3", "NIST-MA-4",
    "NIST-MP-3", "NIST-MP-4", "NIST-MP-5",
    "NIST-PE-4", "NIST-PE-5", "NIST-PE-9", "NIST-PE-10", "NIST-PE-11",
    "NIST-PL-7", "NIST-PL-8",
    "NIST-PM-2", "NIST-PM-3", "NIST-PM-4", "NIST-PM-7", "NIST-PM-8",
    "NIST-PM-11", "NIST-PM-14", "NIST-PM-28", "NIST-PM-30", "NIST-PM-31",
    "NIST-PT-2", "NIST-PT-3", "NIST-PT-4", "NIST-PT-5", "NIST-PT-6",
    "NIST-RA-7", "NIST-RA-9", "NIST-RA-10",
    "NIST-SA-8", "NIST-SA-10", "NIST-SA-11", "NIST-SA-15", "NIST-SA-17", "NIST-SA-22",
    "NIST-SC-2", "NIST-SC-4", "NIST-SC-8", "NIST-SC-10", "NIST-SC-17",
    "NIST-SC-18", "NIST-SC-19", "NIST-SC-23", "NIST-SC-28",
    "NIST-SI-7", "NIST-SI-10", "NIST-SI-12", "NIST-SI-16",
    "NIST-SR-5", "NIST-SR-6", "NIST-SR-8", "NIST-SR-10", "NIST-SR-11",
]

# CIS IG baseline safeguard assignments (CIS Controls v8)
CIS_IG1_SAFEGUARDS = [
    "CIS-1.1", "CIS-1.2",
    "CIS-2.1", "CIS-2.2", "CIS-2.3", "CIS-2.6",
    "CIS-3.1", "CIS-3.5", "CIS-3.7",
    "CIS-4.1", "CIS-4.6", "CIS-4.7",
    "CIS-5.1", "CIS-5.2", "CIS-5.3", "CIS-5.4",
    "CIS-6.1", "CIS-6.2", "CIS-6.3", "CIS-6.4", "CIS-6.5", "CIS-6.7", "CIS-6.8",
    "CIS-7.1", "CIS-7.2", "CIS-7.3", "CIS-7.4", "CIS-7.7",
    "CIS-8.1", "CIS-8.2", "CIS-8.3",
    "CIS-10.1", "CIS-10.2",
    "CIS-11.1", "CIS-11.2", "CIS-11.3", "CIS-11.4",
    "CIS-12.2", "CIS-12.7",
    "CIS-13.1", "CIS-13.6",
    "CIS-14.1", "CIS-14.2", "CIS-14.3", "CIS-14.4",
    "CIS-15.1", "CIS-15.2", "CIS-15.3", "CIS-15.4",
    "CIS-16.1", "CIS-16.8", "CIS-16.9", "CIS-16.11",
    "CIS-17.1", "CIS-17.3",
]

CIS_IG2_EXTRA = [
    "CIS-1.3", "CIS-1.4", "CIS-1.5",
    "CIS-2.4", "CIS-2.5", "CIS-2.7",
    "CIS-3.9", "CIS-3.10", "CIS-3.11",
    "CIS-4.2", "CIS-4.3", "CIS-4.4", "CIS-4.5", "CIS-4.8",
    "CIS-5.5",
    "CIS-8.4", "CIS-8.5", "CIS-8.9", "CIS-8.10", "CIS-8.11", "CIS-8.12",
    "CIS-10.3", "CIS-10.4", "CIS-10.5", "CIS-10.6", "CIS-10.7",
    "CIS-11.5",
    "CIS-12.3", "CIS-12.4", "CIS-12.5", "CIS-12.6",
    "CIS-13.2", "CIS-13.3", "CIS-13.4", "CIS-13.7", "CIS-13.8",
    "CIS-14.5", "CIS-14.6", "CIS-14.7", "CIS-14.8", "CIS-14.9",
    "CIS-15.5",
    "CIS-16.2", "CIS-16.3", "CIS-16.4", "CIS-16.5", "CIS-16.6",
    "CIS-16.7", "CIS-16.10", "CIS-16.12", "CIS-16.13", "CIS-16.14",
    "CIS-17.2", "CIS-17.4", "CIS-17.5", "CIS-17.6", "CIS-17.7",
    "CIS-17.8", "CIS-17.9",
]

# CMMC Level 1 practices (FAR 52.204-21 — 17 practices)
CMMC_L1_PRACTICES = [
    "CMMC-L2-3.1.1", "CMMC-L2-3.1.2", "CMMC-L2-3.1.20", "CMMC-L2-3.1.22",
    "CMMC-L2-3.2.1", "CMMC-L2-3.2.2",
    "CMMC-L2-3.3.1", "CMMC-L2-3.3.2",
    "CMMC-L2-3.4.1", "CMMC-L2-3.4.2",
    "CMMC-L2-3.5.1", "CMMC-L2-3.5.2",
    "CMMC-L2-3.7.1", "CMMC-L2-3.7.2",
    "CMMC-L2-3.8.3",
    "CMMC-L2-3.13.1",
    "CMMC-L2-3.14.1",
]


def phase_assigned_to(existing_node_ids: set[str]) -> tuple[list[dict], list[dict]]:
    """Generate ASSIGNED_TO edges for all baselines."""
    edges: list[dict] = []

    def _assign(controls: list[str], baseline: str) -> None:
        for ctrl in controls:
            if ctrl in existing_node_ids:
                edges.append({"s": ctrl, "p": "ASSIGNED_TO", "o": baseline, "confidence": 1.0})

    # NIST baselines
    _assign(NIST_LOW_CONTROLS, "NIST-LOW")
    nist_mod = NIST_LOW_CONTROLS + NIST_MODERATE_EXTRA
    _assign(nist_mod, "NIST-MODERATE")
    # High = all existing NIST controls
    all_nist = [nid for nid in existing_node_ids if nid.startswith("NIST-") and "-" in nid[5:]]
    # Filter to only Controls (not families/frameworks) — must have numeric part
    nist_ctrls = sorted([nid for nid in all_nist
                         if any(c.isdigit() for c in nid.split("-")[-1])])
    _assign(nist_ctrls, "NIST-HIGH")

    # FedRAMP baselines
    _assign(FEDRAMP_LOW_CONTROLS, "FEDRAMP-LOW")
    fedramp_mod = FEDRAMP_LOW_CONTROLS + FEDRAMP_MODERATE_EXTRA
    _assign(fedramp_mod, "FEDRAMP-MODERATE")
    _assign(nist_ctrls, "FEDRAMP-HIGH")

    # CIS baselines
    _assign(CIS_IG1_SAFEGUARDS, "CIS-IG1")
    cis_ig2 = CIS_IG1_SAFEGUARDS + CIS_IG2_EXTRA
    _assign(cis_ig2, "CIS-IG2")
    # IG3 = all CIS safeguards
    all_cis = sorted([nid for nid in existing_node_ids
                      if nid.startswith("CIS-") and "." in nid])
    _assign(all_cis, "CIS-IG3")

    # CMMC baselines
    _assign(CMMC_L1_PRACTICES, "CMMC-L1")
    # L2 = all CMMC-L2 practices
    all_cmmc = sorted([nid for nid in existing_node_ids
                       if nid.startswith("CMMC-L2-")])
    _assign(all_cmmc, "CMMC-L2")
    # L3 = all CMMC-L2 practices (L3 adds 800-172 extras not in graph yet)
    _assign(all_cmmc, "CMMC-L3")

    # N171 controls assigned to CMMC baselines (N171 = CMMC L2)
    all_n171 = sorted([nid for nid in existing_node_ids if nid.startswith("N171-3.")])
    _assign(all_n171, "CMMC-L2")
    _assign(all_n171, "CMMC-L3")

    return [], edges


# ═══════════════════════════════════════════════════════════════════════════
# Phase 5 — REQUIRES_EVIDENCE edges
# ═══════════════════════════════════════════════════════════════════════════

# Family → evidence types mapping
FAMILY_EVIDENCE_MAP: dict[str, list[tuple[str, float]]] = {
    "NIST-AC": [("EVIDENCE-ACCESS-REVIEW-LOG", 0.95), ("EVIDENCE-CONFIG-SCREENSHOT", 0.90), ("EVIDENCE-POLICY-DOC", 0.90)],
    "NIST-AT": [("EVIDENCE-TRAINING-RECORDS", 0.95), ("EVIDENCE-POLICY-DOC", 0.90)],
    "NIST-AU": [("EVIDENCE-AUDIT-LOG", 0.95), ("EVIDENCE-CONFIG-SCREENSHOT", 0.90)],
    "NIST-CA": [("EVIDENCE-RISK-ASSESSMENT", 0.90), ("EVIDENCE-POAM", 0.95), ("EVIDENCE-POLICY-DOC", 0.90)],
    "NIST-CM": [("EVIDENCE-CONFIG-SCREENSHOT", 0.95), ("EVIDENCE-CHANGE-RECORDS", 0.90), ("EVIDENCE-INVENTORY-REPORT", 0.90)],
    "NIST-CP": [("EVIDENCE-BCP-TEST-RESULTS", 0.95), ("EVIDENCE-POLICY-DOC", 0.90)],
    "NIST-IA": [("EVIDENCE-CONFIG-SCREENSHOT", 0.95), ("EVIDENCE-ACCESS-REVIEW-LOG", 0.90)],
    "NIST-IR": [("EVIDENCE-IR-TEST-RESULTS", 0.95), ("EVIDENCE-POLICY-DOC", 0.90)],
    "NIST-MA": [("EVIDENCE-CHANGE-RECORDS", 0.90), ("EVIDENCE-POLICY-DOC", 0.90)],
    "NIST-MP": [("EVIDENCE-POLICY-DOC", 0.90), ("EVIDENCE-CONFIG-SCREENSHOT", 0.85)],
    "NIST-PE": [("EVIDENCE-CONFIG-SCREENSHOT", 0.90), ("EVIDENCE-POLICY-DOC", 0.90)],
    "NIST-PL": [("EVIDENCE-POLICY-DOC", 0.95)],
    "NIST-PM": [("EVIDENCE-POLICY-DOC", 0.95), ("EVIDENCE-RISK-ASSESSMENT", 0.85)],
    "NIST-PS": [("EVIDENCE-BACKGROUND-CHECK", 0.95), ("EVIDENCE-POLICY-DOC", 0.90)],
    "NIST-PT": [("EVIDENCE-POLICY-DOC", 0.95), ("EVIDENCE-PROCEDURE-DOC", 0.90)],
    "NIST-RA": [("EVIDENCE-RISK-ASSESSMENT", 0.95), ("EVIDENCE-SCAN-REPORT", 0.90)],
    "NIST-SA": [("EVIDENCE-VENDOR-ASSESSMENT", 0.90), ("EVIDENCE-POLICY-DOC", 0.90)],
    "NIST-SC": [("EVIDENCE-NETWORK-DIAGRAM", 0.95), ("EVIDENCE-ENCRYPTION-CONFIG", 0.90), ("EVIDENCE-CONFIG-SCREENSHOT", 0.85)],
    "NIST-SI": [("EVIDENCE-SCAN-REPORT", 0.95), ("EVIDENCE-CONFIG-SCREENSHOT", 0.90)],
    "NIST-SR": [("EVIDENCE-VENDOR-ASSESSMENT", 0.90), ("EVIDENCE-POLICY-DOC", 0.90)],
}


def phase_requires_evidence(existing_node_ids: set[str]) -> tuple[list[dict], list[dict]]:
    """Generate REQUIRES_EVIDENCE edges based on family → evidence type mapping."""
    edges: list[dict] = []

    # Get all NIST controls
    nist_ctrls = sorted([nid for nid in existing_node_ids
                         if nid.startswith("NIST-") and any(c.isdigit() for c in nid.split("-")[-1])])

    for ctrl_id in nist_ctrls:
        family_id = infer_family_id(ctrl_id)
        if not family_id or family_id not in FAMILY_EVIDENCE_MAP:
            continue

        evidence_types = FAMILY_EVIDENCE_MAP[family_id]

        # -1 controls (policy controls) always get policy doc
        if ctrl_id.endswith("-1"):
            edges.append({
                "s": ctrl_id, "p": "REQUIRES_EVIDENCE",
                "o": "EVIDENCE-POLICY-DOC", "confidence": 0.95,
            })

        for ev_type, conf in evidence_types:
            edges.append({
                "s": ctrl_id, "p": "REQUIRES_EVIDENCE",
                "o": ev_type, "confidence": conf,
            })

    return [], edges


# ═══════════════════════════════════════════════════════════════════════════
# Phase 6 — RESPONSIBILITY_OF edges
# ═══════════════════════════════════════════════════════════════════════════

# Family → (service_model, responsibility_type) mappings
FAMILY_RESPONSIBILITY_MAP: dict[str, list[tuple[str, str]]] = {
    "NIST-PE": [("IAAS", "provider")],
    "NIST-MA": [("IAAS", "provider")],
    "NIST-MP": [("IAAS", "provider")],
    "NIST-SC": [("IAAS", "provider"), ("PAAS", "shared")],
    "NIST-CM": [("PAAS", "shared")],
    "NIST-SI": [("PAAS", "shared")],
    "NIST-AU": [("PAAS", "shared")],
    "NIST-CP": [("PAAS", "shared")],
    "NIST-IR": [("PAAS", "shared")],
    "NIST-AC": [("SAAS", "shared")],
    "NIST-IA": [("SAAS", "shared")],
    "NIST-AT": [("SAAS", "customer")],
    "NIST-PL": [("SAAS", "customer")],
    "NIST-PS": [("SAAS", "customer")],
    "NIST-PM": [("SAAS", "customer")],
    "NIST-RA": [("SAAS", "customer")],
    "NIST-PT": [("SAAS", "customer")],
    "NIST-CA": [("SAAS", "customer")],
    "NIST-SA": [("SAAS", "shared")],
    "NIST-SR": [("SAAS", "shared")],
}


def phase_responsibility_of(existing_node_ids: set[str]) -> tuple[list[dict], list[dict]]:
    """Generate RESPONSIBILITY_OF edges based on family → service model mapping."""
    edges: list[dict] = []

    nist_ctrls = sorted([nid for nid in existing_node_ids
                         if nid.startswith("NIST-") and any(c.isdigit() for c in nid.split("-")[-1])])

    for ctrl_id in nist_ctrls:
        family_id = infer_family_id(ctrl_id)
        if not family_id or family_id not in FAMILY_RESPONSIBILITY_MAP:
            continue

        for svc_model, resp_type in FAMILY_RESPONSIBILITY_MAP[family_id]:
            edges.append({
                "s": ctrl_id, "p": "RESPONSIBILITY_OF", "o": svc_model,
                "confidence": 0.90,
                "meta": {"responsibility_type": resp_type},
            })

    return [], edges


# ═══════════════════════════════════════════════════════════════════════════
# Phase 7 — DOCUMENTED_IN edges
# ═══════════════════════════════════════════════════════════════════════════

# Special family → document type overrides
FAMILY_DOCUMENT_OVERRIDES: dict[str, list[str]] = {
    "NIST-CA": ["DOC-SSP", "DOC-SAP", "DOC-SAR", "DOC-POAM"],
    "NIST-CP": ["DOC-SSP", "DOC-CP"],
    "NIST-IR": ["DOC-SSP", "DOC-IRP"],
    "NIST-CM": ["DOC-SSP", "DOC-CMP"],
    "NIST-PT": ["DOC-SSP", "DOC-PIA"],
    "NIST-SA": ["DOC-SSP", "DOC-ISA"],
}


def phase_documented_in(existing_node_ids: set[str]) -> tuple[list[dict], list[dict]]:
    """Generate DOCUMENTED_IN edges. Nearly all controls → DOC-SSP, plus family-specific docs."""
    edges: list[dict] = []

    nist_ctrls = sorted([nid for nid in existing_node_ids
                         if nid.startswith("NIST-") and any(c.isdigit() for c in nid.split("-")[-1])])

    for ctrl_id in nist_ctrls:
        family_id = infer_family_id(ctrl_id)
        if not family_id:
            continue

        if family_id in FAMILY_DOCUMENT_OVERRIDES:
            for doc_type in FAMILY_DOCUMENT_OVERRIDES[family_id]:
                edges.append({
                    "s": ctrl_id, "p": "DOCUMENTED_IN",
                    "o": doc_type, "confidence": 0.95,
                })
        else:
            edges.append({
                "s": ctrl_id, "p": "DOCUMENTED_IN",
                "o": "DOC-SSP", "confidence": 0.95,
            })

    return [], edges


# ═══════════════════════════════════════════════════════════════════════════
# Phase 8 — GDPR MAPS_TO edges (NIST → GDPR)
# ═══════════════════════════════════════════════════════════════════════════

# NIST → GDPR article mappings (NIST as subject for hub routing invariant)
NIST_TO_GDPR_MAPPINGS: list[tuple[str, str, float, str]] = [
    # AC → Art 25 (DPbD), Art 32 (Security)
    ("NIST-AC-1", "GDPR-ART32", 0.85, "Partial"),
    ("NIST-AC-2", "GDPR-ART32", 0.80, "Partial"),
    ("NIST-AC-3", "GDPR-ART32", 0.85, "Partial"),
    ("NIST-AC-4", "GDPR-ART32", 0.80, "Partial"),
    ("NIST-AC-5", "GDPR-ART25", 0.75, "Partial"),
    ("NIST-AC-6", "GDPR-ART25", 0.80, "Partial"),
    ("NIST-AC-6", "GDPR-ART32", 0.80, "Partial"),
    # AT → Art 39 (DPO tasks), Art 32 (Security)
    ("NIST-AT-2", "GDPR-ART39", 0.70, "Partial"),
    ("NIST-AT-2", "GDPR-ART32", 0.70, "Partial"),
    # AU → Art 5 (Accountability), Art 30 (Records)
    ("NIST-AU-2", "GDPR-ART5",  0.75, "Partial"),
    ("NIST-AU-2", "GDPR-ART30", 0.80, "Partial"),
    ("NIST-AU-6", "GDPR-ART5",  0.70, "Partial"),
    # CM → Art 25 (DPbD), Art 32 (Security)
    ("NIST-CM-2", "GDPR-ART25", 0.70, "Partial"),
    ("NIST-CM-6", "GDPR-ART32", 0.75, "Partial"),
    # CP → Art 32 (availability/resilience)
    ("NIST-CP-2", "GDPR-ART32", 0.85, "Partial"),
    ("NIST-CP-9", "GDPR-ART32", 0.80, "Partial"),
    # IA → Art 32 (Security)
    ("NIST-IA-2", "GDPR-ART32", 0.85, "Partial"),
    ("NIST-IA-5", "GDPR-ART32", 0.80, "Partial"),
    # IR → Art 33 (Breach notification), Art 34 (Communication to data subject)
    ("NIST-IR-4", "GDPR-ART33", 0.90, "Full"),
    ("NIST-IR-4", "GDPR-ART34", 0.80, "Partial"),
    ("NIST-IR-6", "GDPR-ART33", 0.90, "Full"),
    ("NIST-IR-8", "GDPR-ART33", 0.85, "Partial"),
    # MP → Art 32 (Security)
    ("NIST-MP-6", "GDPR-ART17", 0.70, "Partial"),
    # PE → Art 32 (Security)
    ("NIST-PE-3", "GDPR-ART32", 0.75, "Partial"),
    # PL → Art 24 (Responsibility of controller), Art 35 (DPIA)
    ("NIST-PL-2", "GDPR-ART24", 0.80, "Partial"),
    # PM → Art 37 (DPO), Art 38 (DPO position), Art 39 (DPO tasks)
    ("NIST-PM-1", "GDPR-ART24", 0.75, "Partial"),
    ("NIST-PM-9", "GDPR-ART35", 0.80, "Partial"),
    # PS → Art 32 (Security), Art 28 (Processor obligations)
    ("NIST-PS-3", "GDPR-ART32", 0.70, "Partial"),
    ("NIST-PS-6", "GDPR-ART28", 0.75, "Partial"),
    # PT → Art 5 (Principles), Art 6 (Lawfulness), Art 12-22 (Data subject rights)
    ("NIST-PT-1", "GDPR-ART5",  0.85, "Partial"),
    ("NIST-PT-2", "GDPR-ART6",  0.80, "Partial"),
    ("NIST-PT-3", "GDPR-ART7",  0.80, "Partial"),
    ("NIST-PT-4", "GDPR-ART12", 0.85, "Partial"),
    ("NIST-PT-4", "GDPR-ART13", 0.80, "Partial"),
    ("NIST-PT-5", "GDPR-ART15", 0.80, "Partial"),
    ("NIST-PT-5", "GDPR-ART20", 0.75, "Partial"),
    ("NIST-PT-6", "GDPR-ART35", 0.85, "Partial"),
    # RA → Art 35 (DPIA), Art 32 (Security)
    ("NIST-RA-3", "GDPR-ART35", 0.85, "Partial"),
    ("NIST-RA-5", "GDPR-ART32", 0.80, "Partial"),
    # SA → Art 28 (Processor), Art 32 (Security)
    ("NIST-SA-4", "GDPR-ART28", 0.85, "Partial"),
    ("NIST-SA-9", "GDPR-ART28", 0.80, "Partial"),
    ("NIST-SA-9", "GDPR-ART44", 0.70, "Partial"),
    # SC → Art 32 (Security — encryption, integrity)
    ("NIST-SC-7",  "GDPR-ART32", 0.85, "Partial"),
    ("NIST-SC-8",  "GDPR-ART32", 0.85, "Partial"),
    ("NIST-SC-12", "GDPR-ART32", 0.80, "Partial"),
    ("NIST-SC-13", "GDPR-ART32", 0.85, "Partial"),
    ("NIST-SC-28", "GDPR-ART32", 0.85, "Partial"),
    # SI → Art 32 (Security — integrity, monitoring)
    ("NIST-SI-2", "GDPR-ART32", 0.80, "Partial"),
    ("NIST-SI-3", "GDPR-ART32", 0.80, "Partial"),
    ("NIST-SI-4", "GDPR-ART32", 0.80, "Partial"),
    # SR → Art 28 (Processor), Art 32 (Security)
    ("NIST-SR-1", "GDPR-ART28", 0.75, "Partial"),
    ("NIST-SR-2", "GDPR-ART28", 0.70, "Partial"),
    # Art 25 (DPbD) — comprehensive mapping
    ("NIST-SA-8",  "GDPR-ART25", 0.85, "Partial"),
    ("NIST-PL-8",  "GDPR-ART25", 0.75, "Partial"),
    # Art 30 (Records of processing)
    ("NIST-PL-2",  "GDPR-ART30", 0.75, "Partial"),
    ("NIST-PM-5",  "GDPR-ART30", 0.70, "Partial"),
    # Art 37-39 (DPO)
    ("NIST-PM-2",  "GDPR-ART37", 0.70, "Partial"),
    # Art 46 (Appropriate safeguards for transfers)
    ("NIST-SA-9",  "GDPR-ART46", 0.65, "Implicit"),
    # Art 42 (Certification)
    ("NIST-CA-2",  "GDPR-ART42", 0.65, "Implicit"),
]


def phase_gdpr_mappings() -> tuple[list[dict], list[dict]]:
    """Generate MAPS_TO edges from NIST → GDPR articles."""
    edges: list[dict] = []

    for nist_id, gdpr_id, conf, coverage in NIST_TO_GDPR_MAPPINGS:
        edges.append({
            "s": nist_id, "p": "MAPS_TO", "o": gdpr_id,
            "confidence": conf,
            "meta": {"coverage": coverage, "source": "nist-to-gdpr"},
        })

    return [], edges


# ═══════════════════════════════════════════════════════════════════════════
# Merge & Write Logic
# ═══════════════════════════════════════════════════════════════════════════


def dedup_edges(existing: list[dict], new: list[dict]) -> list[dict]:
    """Deduplicate edges by (s, p, o) tuple. Existing edges take priority."""
    seen: set[tuple[str, str, str]] = set()
    for e in existing:
        seen.add((e["s"], e["p"], e["o"]))

    added: list[dict] = []
    for e in new:
        key = (e["s"], e["p"], e["o"])
        if key not in seen:
            seen.add(key)
            added.append(e)

    return added


def merge_and_write(
    nodes_data: dict,
    edges_data: dict,
    new_nodes: list[dict],
    new_edges: list[dict],
    preview: bool = True,
) -> dict:
    """Merge new nodes/edges into existing data, validate, optionally write."""

    # Collect existing node IDs for validation
    existing_ids = collect_all_node_ids(nodes_data)

    # ── Merge new nodes ──────────────────────────────────────────────────
    baselines_added = 0
    families_added = 0
    controls_added = 0

    for node in new_nodes:
        if node["id"] in existing_ids:
            continue
        ntype = node["type"]
        if ntype == "Baseline":
            nodes_data.setdefault("baselines", []).append(node)
            baselines_added += 1
        elif ntype == "ControlFamily":
            fw = node.get("framework_id", "unknown")
            section_key = {
                "GDPR": "gdpr",
                "NIST-800-171": "nist171",
            }.get(fw, fw.lower().replace("-", "_"))
            nodes_data.setdefault("control_families", {}).setdefault(section_key, []).append(node)
            families_added += 1
        elif ntype == "Control":
            fw = node.get("framework_id", "unknown")
            section_key = {
                "GDPR": "gdpr",
                "NIST-800-171": "nist171",
            }.get(fw, fw.lower().replace("-", "_"))
            nodes_data.setdefault("controls", {}).setdefault(section_key, []).append(node)
            controls_added += 1
        existing_ids.add(node["id"])

    # ── Collect + dedup new edges by type ────────────────────────────────
    existing_edges = collect_all_edges(edges_data)

    # Separate new edges by predicate and plane
    contains_fw_fam = []
    contains_fam_ctrl = []
    assigned_to = []
    maps_to_gdpr = []
    maps_to_n171 = []
    requires_evidence = []
    responsibility_of = []
    documented_in = []

    for e in new_edges:
        pred = e["p"]
        if pred == "CONTAINS":
            # Determine if framework→family or family→control
            obj_type = None
            for node in new_nodes:
                if node["id"] == e["o"]:
                    obj_type = node["type"]
                    break
            if obj_type == "ControlFamily":
                contains_fw_fam.append(e)
            else:
                contains_fam_ctrl.append(e)
        elif pred == "ASSIGNED_TO":
            assigned_to.append(e)
        elif pred == "MAPS_TO":
            source = e.get("meta", {}).get("source", "")
            if "gdpr" in source:
                maps_to_gdpr.append(e)
            elif "171" in source:
                maps_to_n171.append(e)
            else:
                maps_to_gdpr.append(e)
        elif pred == "REQUIRES_EVIDENCE":
            requires_evidence.append(e)
        elif pred == "RESPONSIBILITY_OF":
            responsibility_of.append(e)
        elif pred == "DOCUMENTED_IN":
            documented_in.append(e)

    # Dedup against existing edges
    existing_fw_fam = edges_data.get("plane_compliance", {}).get("framework_to_family", [])
    existing_fam_ctrl = edges_data.get("plane_compliance", {}).get("family_to_control", [])
    existing_assigned = edges_data.get("plane_compliance", {}).get("baseline_assignments", [])
    existing_evidence = edges_data.get("plane_evidence", {}).get("evidence_requirements", [])
    existing_responsibility = edges_data.get("plane_responsibility", {}).get("control_responsibility", [])
    existing_documentation = edges_data.get("plane_evidence", {}).get("documentation", [])

    new_fw_fam = dedup_edges(existing_fw_fam, contains_fw_fam)
    new_fam_ctrl = dedup_edges(existing_fam_ctrl, contains_fam_ctrl)
    new_assigned = dedup_edges(existing_assigned, assigned_to)
    new_evidence = dedup_edges(existing_evidence, requires_evidence)
    new_responsibility = dedup_edges(existing_responsibility, responsibility_of)
    new_documentation = dedup_edges(existing_documentation, documented_in)
    # MAPS_TO sections — collect all existing mapping edges for dedup
    all_existing_maps = []
    pm = edges_data.get("plane_mapping", {})
    for k, v in pm.items():
        if not k.startswith("_") and isinstance(v, list):
            all_existing_maps.extend(v)
    new_maps_gdpr = dedup_edges(all_existing_maps, maps_to_gdpr)
    new_maps_n171 = dedup_edges(all_existing_maps + new_maps_gdpr, maps_to_n171)

    # ── Print summary ────────────────────────────────────────────────────
    print(f"\n{'=' * 60}")
    print(f"  GRC Knowledge Graph Upgrade — {'PREVIEW' if preview else 'WRITE'}")
    print(f"{'=' * 60}")
    print(f"\n  New nodes:")
    print(f"    Baselines:        {baselines_added}")
    print(f"    Control Families: {families_added}")
    print(f"    Controls:         {controls_added}")
    print(f"    Total:            {baselines_added + families_added + controls_added}")
    print(f"\n  New edges (after dedup):")
    print(f"    CONTAINS (fw->fam):    {len(new_fw_fam)}")
    print(f"    CONTAINS (fam->ctrl):  {len(new_fam_ctrl)}")
    print(f"    ASSIGNED_TO:          {len(new_assigned)}")
    print(f"    MAPS_TO (GDPR):       {len(new_maps_gdpr)}")
    print(f"    MAPS_TO (N171):       {len(new_maps_n171)}")
    print(f"    REQUIRES_EVIDENCE:    {len(new_evidence)}")
    print(f"    RESPONSIBILITY_OF:    {len(new_responsibility)}")
    print(f"    DOCUMENTED_IN:        {len(new_documentation)}")
    total_new_edges = (len(new_fw_fam) + len(new_fam_ctrl) + len(new_assigned) +
                       len(new_maps_gdpr) + len(new_maps_n171) + len(new_evidence) +
                       len(new_responsibility) + len(new_documentation))
    print(f"    Total:                {total_new_edges}")

    total_nodes = len(existing_ids)
    total_edges = len(existing_edges) + total_new_edges
    print(f"\n  Final totals:")
    print(f"    Nodes: {total_nodes}")
    print(f"    Edges: {total_edges}")

    stats = {
        "nodes_added": baselines_added + families_added + controls_added,
        "edges_added": total_new_edges,
        "total_nodes": total_nodes,
        "total_edges": total_edges,
    }

    if preview:
        print(f"\n  Run with --write to persist changes.")
        return stats

    # ── Merge edges into data ────────────────────────────────────────────
    pc = edges_data.setdefault("plane_compliance", {})
    pc.setdefault("framework_to_family", []).extend(new_fw_fam)
    pc.setdefault("family_to_control", []).extend(new_fam_ctrl)
    pc.setdefault("baseline_assignments", []).extend(new_assigned)

    pmap = edges_data.setdefault("plane_mapping", {})
    if new_maps_gdpr:
        pmap.setdefault("nist_to_gdpr", []).extend(new_maps_gdpr)
    if new_maps_n171:
        pmap.setdefault("nist_to_nist171", []).extend(new_maps_n171)

    pr = edges_data.setdefault("plane_responsibility", {})
    pr.setdefault("control_responsibility", []).extend(new_responsibility)

    pe = edges_data.setdefault("plane_evidence", {})
    pe.setdefault("evidence_requirements", []).extend(new_evidence)
    pe.setdefault("documentation", []).extend(new_documentation)

    # ── Update metadata ──────────────────────────────────────────────────
    nodes_data["_meta"]["node_count"] = total_nodes
    nodes_data["_meta"]["revision_id"] = NEW_REVISION
    edges_data["_meta"]["edge_count"] = total_edges
    edges_data["_meta"]["revision_id"] = NEW_REVISION

    # ── Write files ──────────────────────────────────────────────────────
    print(f"\n  Writing nodes.json ...")
    with open(NODES_PATH, "w") as f:
        json.dump(nodes_data, f, indent=2)
        f.write("\n")

    print(f"  Writing edges.json ...")
    with open(EDGES_PATH, "w") as f:
        json.dump(edges_data, f, indent=2)
        f.write("\n")

    # ── Update schema.json revision ──────────────────────────────────────
    schema = load_json(SCHEMA_PATH)
    rev = schema.get("revision_layer", {}).get("current_revision", {})
    rev["revision_id"] = NEW_REVISION
    rev["created_at"] = "2026-02-20T00:00:00Z"
    rev["summary"] = (
        "Upgrade — GDPR + NIST 800-171 controls, full baseline/evidence/"
        "responsibility/documentation planes, ~3000 new edges"
    )
    print(f"  Writing schema.json ...")
    with open(SCHEMA_PATH, "w") as f:
        json.dump(schema, f, indent=2)
        f.write("\n")

    # ── Post-write validation ────────────────────────────────────────────
    print(f"\n  Running validation ...")
    node_count, edge_count, errors = validate_graph()
    if errors:
        print(f"\n  VALIDATION ERRORS ({len(errors)}):")
        for err in errors[:20]:
            print(f"    - {err}")
        if len(errors) > 20:
            print(f"    ... and {len(errors) - 20} more")
    else:
        print(f"  Validation passed: {node_count} nodes, {edge_count} edges, 0 errors")

    print(f"\n{'=' * 60}")
    return stats


# ═══════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════


def main() -> None:
    preview = "--write" not in sys.argv
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return

    # Load existing data
    nodes_data = load_json(NODES_PATH)
    edges_data = load_json(EDGES_PATH)

    # Collect existing node IDs (before adding new nodes)
    existing_ids = collect_all_node_ids(nodes_data)

    # Run phases — collect all new nodes and edges
    all_new_nodes: list[dict] = []
    all_new_edges: list[dict] = []

    phases = [
        ("Phase 1: NIST Baselines",       lambda: phase_nist_baselines()),
        ("Phase 2: GDPR Controls",        lambda: phase_gdpr_controls()),
        ("Phase 3: NIST 800-171 Controls", lambda: phase_nist171_controls()),
    ]

    for name, fn in phases:
        print(f"  {name} ...")
        nodes, edges = fn()
        all_new_nodes.extend(nodes)
        all_new_edges.extend(edges)

    # Add new node IDs to the set so subsequent phases can reference them
    for node in all_new_nodes:
        existing_ids.add(node["id"])

    dependent_phases = [
        ("Phase 4: ASSIGNED_TO",       lambda: phase_assigned_to(existing_ids)),
        ("Phase 5: REQUIRES_EVIDENCE", lambda: phase_requires_evidence(existing_ids)),
        ("Phase 6: RESPONSIBILITY_OF", lambda: phase_responsibility_of(existing_ids)),
        ("Phase 7: DOCUMENTED_IN",     lambda: phase_documented_in(existing_ids)),
        ("Phase 8: GDPR Mappings",     lambda: phase_gdpr_mappings()),
    ]

    for name, fn in dependent_phases:
        print(f"  {name} ...")
        nodes, edges = fn()
        all_new_nodes.extend(nodes)
        all_new_edges.extend(edges)

    # Merge and write
    stats = merge_and_write(nodes_data, edges_data, all_new_nodes, all_new_edges, preview=preview)

    if stats.get("edges_added", 0) == 0 and stats.get("nodes_added", 0) == 0:
        print("\n  No changes needed — graph is already up to date.")


if __name__ == "__main__":
    main()
