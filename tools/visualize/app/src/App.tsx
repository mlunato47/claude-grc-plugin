import { useRef, useCallback, useEffect, useState } from 'react'
import { useGraphData } from './hooks/useGraphData'
import { useCytoscape, type SelectedElement } from './hooks/useCytoscape'
import { useFilters } from './hooks/useFilters'
import { useChat } from './hooks/useChat'
import { Header } from './components/Header'
import { Sidebar } from './components/Sidebar'
import { GraphCanvas } from './components/GraphCanvas'
import { DetailPanel } from './components/DetailPanel'
import { ChatDrawer } from './components/ChatDrawer'
import './App.css'

export default function App() {
  const containerRef = useRef<HTMLDivElement>(null)
  const searchRef = useRef<HTMLInputElement>(null)
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

  // Clear selection and all visual artifacts
  const clearAll = useCallback(() => {
    setSelected(null)
    if (searchRef.current) searchRef.current.value = ''
    const cy = cyRef.current
    if (cy) {
      cy.elements().removeClass('dimmed').removeClass('highlighted').removeClass('neighbor')
    }
  }, [cyRef])

  // Reset: clear selection + dimming + search, then reset filters
  const handleReset = useCallback(() => {
    clearAll()
    filters.resetFilters()
  }, [clearAll, filters.resetFilters])

  // Keyboard: Escape to clear selection and search
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        clearAll()
      }
    }
    document.addEventListener('keydown', handler)
    return () => document.removeEventListener('keydown', handler)
  }, [clearAll])

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
        searchRef={searchRef}
        totalNodes={graphData.nodes.length}
        totalEdges={graphData.edges.length}
        visibleNodes={filters.visibleNodes}
        visibleEdges={filters.visibleEdges}
        chatOpen={chat.isOpen}
        onToggleChat={chat.toggleOpen}
        onReset={handleReset}
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
