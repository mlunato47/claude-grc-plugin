import { useRef, useCallback, useEffect } from 'react'
import { useGraphData } from './hooks/useGraphData'
import { useCytoscape, type SelectedElement } from './hooks/useCytoscape'
import { useFilters } from './hooks/useFilters'
import { useChat } from './hooks/useChat'
import { Header } from './components/Header'
import { Sidebar } from './components/Sidebar'
import { GraphCanvas } from './components/GraphCanvas'
import { DetailPanel } from './components/DetailPanel'
import { ChatDrawer } from './components/ChatDrawer'
import { useState } from 'react'
import './App.css'

export default function App() {
  const containerRef = useRef<HTMLDivElement>(null)
  const [selected, setSelected] = useState<SelectedElement>(null)

  const { data: graphData, error: loadError } = useGraphData()

  const onSelect = useCallback((el: SelectedElement) => setSelected(el), [])

  const { cyRef, navigateToNode } = useCytoscape({
    containerRef, graphData, onSelect,
  })

  const filters = useFilters(cyRef, graphData)

  const getSelectedNodeId = useCallback((): string | null => {
    const cy = cyRef.current
    if (!cy) return null
    const sel = cy.elements('node:selected')
    return sel.length > 0 ? sel[0].id() : null
  }, [cyRef])

  const chat = useChat(getSelectedNodeId)

  // Keyboard: Escape to clear
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        setSelected(null)
        const cy = cyRef.current
        if (cy) {
          cy.elements().removeClass('dimmed').removeClass('highlighted').removeClass('neighbor')
        }
      }
    }
    document.addEventListener('keydown', handler)
    return () => document.removeEventListener('keydown', handler)
  }, [cyRef])

  if (loadError) {
    return <div style={{ color: '#ef4444', padding: 40, fontSize: 16 }}>Failed to load graph: {loadError}</div>
  }

  if (!graphData) {
    return <div style={{ color: '#94a3b8', padding: 40, fontSize: 16 }}>Loading graph...</div>
  }

  return (
    <>
      <Header
        cyRef={cyRef}
        totalNodes={graphData.nodes.length}
        totalEdges={graphData.edges.length}
        visibleNodes={filters.visibleNodes}
        visibleEdges={filters.visibleEdges}
        chatOpen={chat.isOpen}
        onToggleChat={chat.toggleOpen}
        onReset={filters.resetFilters}
      />
      <Sidebar
        graphData={graphData}
        activePredicates={filters.activePredicates}
        activeTypes={filters.activeTypes}
        focusedFramework={filters.focusedFramework}
        layout={filters.layout}
        showLabels={filters.showLabels}
        showOrphans={filters.showOrphans}
        onTogglePredicate={filters.togglePredicate}
        onToggleType={filters.toggleType}
        onFocusFramework={filters.setFocusedFramework}
        onChangeLayout={filters.changeLayout}
        onChangeLabels={filters.changeLabels}
        onChangeOrphans={filters.setShowOrphans}
      />
      <GraphCanvas containerRef={containerRef} />
      <DetailPanel
        cyRef={cyRef}
        selected={selected}
        navigateToNode={navigateToNode}
      />
      <ChatDrawer
        messages={chat.messages}
        streamingText={chat.streamingText}
        isStreaming={chat.isStreaming}
        isOpen={chat.isOpen}
        error={chat.error}
        graphData={graphData}
        onSend={chat.send}
        onToggle={chat.toggleOpen}
        navigateToNode={navigateToNode}
      />
    </>
  )
}
