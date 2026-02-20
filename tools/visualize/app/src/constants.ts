export const NODE_COLORS: Record<string, string> = {
  Framework:     '#3b82f6',
  ControlFamily: '#8b5cf6',
  Control:       '#10b981',
  Baseline:      '#f59e0b',
  ServiceModel:  '#ef4444',
  EvidenceType:  '#06b6d4',
  DocumentType:  '#6b7280',
}

export const NODE_SHAPES: Record<string, string> = {
  Framework:     'diamond',
  ControlFamily: 'round-rectangle',
  Control:       'ellipse',
  Baseline:      'pentagon',
  ServiceModel:  'hexagon',
  EvidenceType:  'rectangle',
  DocumentType:  'rectangle',
}

export const NODE_SIZES: Record<string, number> = {
  Framework: 40, ControlFamily: 28, Control: 16,
  Baseline: 26, ServiceModel: 28, EvidenceType: 22, DocumentType: 22,
}

export const PREDICATE_COLORS: Record<string, string> = {
  CONTAINS:          '#6b7280',
  ASSIGNED_TO:       '#f59e0b',
  MAPS_TO:           '#3b82f6',
  REQUIRES_EVIDENCE: '#06b6d4',
  RESPONSIBILITY_OF: '#ef4444',
  DOCUMENTED_IN:     '#a78bfa',
  INHERITS_FROM:     '#f97316',
  PART_OF:           '#6b7280',
  SUPERSEDES:        '#64748b',
}

export const PREDICATE_STYLES: Record<string, string> = {
  CONTAINS:          'solid',
  ASSIGNED_TO:       'solid',
  MAPS_TO:           'dashed',
  REQUIRES_EVIDENCE: 'dotted',
  RESPONSIBILITY_OF: 'solid',
  DOCUMENTED_IN:     'dotted',
  INHERITS_FROM:     'solid',
  PART_OF:           'solid',
  SUPERSEDES:        'dashed',
}

export const DEFAULT_ON_PREDICATES = new Set(['CONTAINS', 'MAPS_TO'])

export const PREDICATE_ORDER = [
  'CONTAINS', 'MAPS_TO', 'ASSIGNED_TO', 'REQUIRES_EVIDENCE',
  'RESPONSIBILITY_OF', 'DOCUMENTED_IN', 'INHERITS_FROM', 'PART_OF', 'SUPERSEDES',
]

export const LAYOUT_OPTIONS: { value: string; label: string }[] = [
  { value: 'cose', label: 'Force-Directed (cose)' },
  { value: 'breadthfirst', label: 'Hierarchy (breadthfirst)' },
  { value: 'concentric', label: 'Concentric' },
  { value: 'circle', label: 'Circle' },
]
