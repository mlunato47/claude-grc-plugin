export interface GraphNode {
  id: string
  type: string
  label: string
  props: Record<string, unknown>
}

export interface GraphEdge {
  source: string
  target: string
  predicate: string
  plane: string
  confidence: number
  meta: Record<string, string>
}

export interface GraphPayload {
  nodes: GraphNode[]
  edges: GraphEdge[]
  planes: Record<string, unknown>
  predicates: Record<string, unknown>
  scoring: Record<string, unknown>
  stats: {
    node_types: Record<string, number>
    edge_predicates: Record<string, number>
  }
}

export interface ChatMessage {
  role: 'user' | 'assistant'
  content: string
}
