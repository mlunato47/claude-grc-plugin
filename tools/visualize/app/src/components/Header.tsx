import { useCallback } from 'react'
import type { Core } from 'cytoscape'

interface HeaderProps {
  cyRef: React.RefObject<Core | null>
  searchRef: React.RefObject<HTMLInputElement | null>
  totalNodes: number
  totalEdges: number
  visibleNodes: number
  visibleEdges: number
  chatOpen: boolean
  onToggleChat: () => void
  onReset: () => void
}

export function Header({
  cyRef, searchRef, totalNodes, totalEdges, visibleNodes, visibleEdges,
  chatOpen, onToggleChat, onReset,
}: HeaderProps) {
  const handleSearch = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    const cy = cyRef.current
    if (!cy) return
    const q = e.target.value.toLowerCase().trim()
    cy.nodes().removeClass('highlighted')
    cy.elements().removeClass('dimmed')

    if (q.length < 2) return

    const matches = cy.nodes().filter(n =>
      n.data('id').toLowerCase().includes(q) ||
      n.data('label').toLowerCase().includes(q)
    )
    matches.addClass('highlighted')

    if (matches.length > 0 && matches.length <= 30) {
      cy.elements().addClass('dimmed')
      matches.removeClass('dimmed')
      matches.connectedEdges().filter(e => e.visible()).removeClass('dimmed')
      matches.connectedEdges().filter(e => e.visible()).connectedNodes().removeClass('dimmed')
    }

    if (matches.length === 1) {
      cy.animate({ center: { eles: matches }, zoom: 2.5 }, { duration: 300 })
    } else if (matches.length > 1 && matches.length <= 30) {
      cy.animate({ fit: { eles: matches, padding: 60 } }, { duration: 300 })
    }
  }, [cyRef])

  const handleFit = useCallback(() => {
    cyRef.current?.fit(undefined, 40)
  }, [cyRef])

  const handleExport = useCallback(() => {
    const cy = cyRef.current
    if (!cy) return
    const png = cy.png({ bg: '#0f172a', full: true, scale: 2 })
    const a = document.createElement('a')
    a.href = png; a.download = 'grc-knowledge-graph.png'; a.click()
  }, [cyRef])

  return (
    <header>
      <h1>GRC Knowledge Graph</h1>
      <span className="stats">
        {totalNodes} nodes, {totalEdges} edges | Visible: {visibleNodes}n {visibleEdges}e
      </span>
      <input
        ref={searchRef}
        type="text"
        placeholder="Search nodes (e.g. AC-2, GDPR-ART32, N171-3.1)..."
        onChange={handleSearch}
      />
      <div className="actions">
        <button onClick={handleFit} title="Fit graph to view">Fit</button>
        <button onClick={onReset} title="Reset view and clear selection">Reset</button>
        <button onClick={handleExport} title="Export as PNG">PNG</button>
        <button
          onClick={onToggleChat}
          title="Toggle chat with Claude"
          className={chatOpen ? 'active' : ''}
        >
          Chat
        </button>
      </div>
    </header>
  )
}
