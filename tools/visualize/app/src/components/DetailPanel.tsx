import type { Core } from 'cytoscape'
import type { SelectedElement } from '../hooks/useCytoscape'
import { NODE_COLORS, PREDICATE_COLORS, PREDICATE_ORDER } from '../constants'

interface DetailPanelProps {
  cyRef: React.RefObject<Core | null>
  selected: SelectedElement
  navigateToNode: (nodeId: string) => void
}

export function DetailPanel({ cyRef, selected, navigateToNode }: DetailPanelProps) {
  const cy = cyRef.current

  if (!selected || !cy) {
    return (
      <div id="detail" className="empty">
        <span>Click a node or edge to inspect</span>
      </div>
    )
  }

  if (selected.kind === 'node') {
    return <NodeDetail cy={cy} nodeId={selected.id} navigateToNode={navigateToNode} />
  }

  return <EdgeDetail cy={cy} edgeId={selected.id} navigateToNode={navigateToNode} />
}

function NodeDetail({ cy, nodeId, navigateToNode }: {
  cy: Core; nodeId: string; navigateToNode: (id: string) => void
}) {
  const node = cy.getElementById(nodeId)
  if (node.length === 0) return <div id="detail" className="empty"><span>Node not found</span></div>

  const type = node.data('type') as string
  const badgeColor = NODE_COLORS[type] || '#475569'
  const data = node.data()
  const skip = new Set(['id', 'label', 'type'])

  // Connected edges grouped by predicate
  const connected = node.connectedEdges().filter(e => e.visible())
  const byPredicate: Record<string, Array<{
    otherId: string; direction: string; confidence: number; meta: Record<string, string>
  }>> = {}

  connected.forEach(e => {
    const pred = e.data('predicate') as string
    if (!byPredicate[pred]) byPredicate[pred] = []
    const other = e.source().id() === nodeId ? e.target() : e.source()
    byPredicate[pred].push({
      otherId: other.id(),
      direction: e.source().id() === nodeId ? 'out' : 'in',
      confidence: e.data('confidence') as number,
      meta: e.data('meta') as Record<string, string>,
    })
  })

  const sortedPreds = Object.keys(byPredicate).sort((a, b) => {
    const ai = PREDICATE_ORDER.indexOf(a)
    const bi = PREDICATE_ORDER.indexOf(b)
    return (ai === -1 ? 99 : ai) - (bi === -1 ? 99 : bi)
  })

  return (
    <div id="detail">
      <h2>{nodeId}</h2>
      <span className="badge" style={{ background: `${badgeColor}33`, color: badgeColor }}>
        {type}
      </span>
      <table>
        <tbody>
          <tr><td>Label</td><td>{node.data('label')}</td></tr>
          {Object.entries(data).map(([k, v]) => {
            if (skip.has(k) || v === undefined || v === null) return null
            const display = typeof v === 'object' ? JSON.stringify(v) : String(v)
            return <tr key={k}><td>{k}</td><td>{display}</td></tr>
          })}
        </tbody>
      </table>

      {sortedPreds.map(pred => {
        const edges = byPredicate[pred]
        const predColor = PREDICATE_COLORS[pred] || '#475569'
        return (
          <div key={pred}>
            <div className="section-label">
              <span className="pred-dot" style={{ background: predColor }} />
              {pred} ({edges.length})
            </div>
            <ul>
              {edges.map((e, i) => {
                const arrow = e.direction === 'out' ? '\u2192' : '\u2190'
                const pct = e.confidence ? (e.confidence * 100).toFixed(0) : null
                const coverage = e.meta?.coverage
                const respType = e.meta?.responsibility_type
                return (
                  <li key={i} onClick={() => navigateToNode(e.otherId)}>
                    {arrow} {e.otherId}
                    {pct && (
                      <span className="confidence-bar">
                        <span className="fill" style={{ width: `${pct}%` }} />
                      </span>
                    )}
                    {coverage && (
                      <span style={{ color: '#64748b', fontSize: 11, marginLeft: 4 }}>[{coverage}]</span>
                    )}
                    {respType && (
                      <span style={{ color: '#64748b', fontSize: 11, marginLeft: 4 }}>[{respType}]</span>
                    )}
                  </li>
                )
              })}
            </ul>
          </div>
        )
      })}
    </div>
  )
}

function EdgeDetail({ cy, edgeId, navigateToNode }: {
  cy: Core; edgeId: string; navigateToNode: (id: string) => void
}) {
  const edge = cy.getElementById(edgeId)
  if (edge.length === 0) return <div id="detail" className="empty"><span>Edge not found</span></div>

  const pred = edge.data('predicate') as string
  const predColor = PREDICATE_COLORS[pred] || '#475569'
  const meta = edge.data('meta') as Record<string, string> | undefined
  const source = edge.data('source') as string
  const target = edge.data('target') as string

  return (
    <div id="detail">
      <h2>{source} &rarr; {target}</h2>
      <span className="badge" style={{ background: `${predColor}33`, color: predColor }}>
        {pred}
      </span>
      <table>
        <tbody>
          <tr><td>Plane</td><td>{edge.data('plane')}</td></tr>
          <tr><td>Confidence</td><td>{((edge.data('confidence') as number) * 100).toFixed(0)}%</td></tr>
          {meta && Object.entries(meta).map(([k, v]) => (
            <tr key={k}><td>{k}</td><td>{v}</td></tr>
          ))}
        </tbody>
      </table>

      <div className="section-label">Endpoints</div>
      <ul>
        <li onClick={() => navigateToNode(source)}>{source}</li>
        <li onClick={() => navigateToNode(target)}>{target}</li>
      </ul>
    </div>
  )
}
