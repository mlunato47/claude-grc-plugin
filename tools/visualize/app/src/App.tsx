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
  const [graphOpen, setGraphOpen] = useState(false)
  const [graphReady, setGraphReady] = useState(false)

  const { data: graphData, error: loadError } = useGraphData()

  const onSelect = useCallback((el: SelectedElement) => setSelected(el), [])
  const onGraphReady = useCallback(() => setGraphReady(true), [])

  const { cyRef, navigateToNode } = useCytoscape({
    containerRef, graphData: graphOpen ? graphData : null, onSelect,
    onReady: onGraphReady,
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

  // Keyboard shortcuts
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      // Escape — clear selection and search
      if (e.key === 'Escape') {
        clearAll()
        return
      }
      // Ctrl+K / Cmd+K — focus search
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault()
        searchRef.current?.focus()
        return
      }
      // Ctrl+/ — toggle chat
      if ((e.ctrlKey || e.metaKey) && e.key === '/') {
        e.preventDefault()
        chat.toggleOpen()
        return
      }
    }
    document.addEventListener('keydown', handler)
    return () => document.removeEventListener('keydown', handler)
  }, [clearAll, chat.toggleOpen])

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
        graphReady={graphReady}
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
        onSetAllPredicates={filters.setAllPredicates}
        onSetAllTypes={filters.setAllTypes}
        onFocusFramework={filters.setFocusedFramework}
        onChangeLayout={filters.changeLayout}
        onChangeLabels={filters.changeLabels}
        onChangeOrphans={filters.setShowOrphans}
        onResetFilters={handleReset}
        graphReady={graphReady}
      />
      {graphOpen ? (
        <div className="graph-area">
          <GraphCanvas containerRef={containerRef} />
          {!graphReady && (
            <div className="graph-loading-overlay">
              <div className="graph-loading-spinner" />
              <span>Rendering graph...</span>
            </div>
          )}
        </div>
      ) : (
        <div id="cy" className="graph-placeholder">
          <button className="render-graph-btn" onClick={() => setGraphOpen(true)}>
            Render Graph
          </button>
          <span className="graph-placeholder-hint">
            {graphData.nodes.length} nodes, {graphData.edges.length} edges
          </span>
        </div>
      )}
      <DetailPanel
        cyRef={cyRef}
        selected={selected}
        navigateToNode={navigateToNode}
        graphReady={graphReady}
      />
      <ChatDrawer
        messages={chat.messages}
        streamingText={chat.streamingText}
        isStreaming={chat.isStreaming}
        isOpen={chat.isOpen}
        error={chat.error}
        graphData={graphData}
        conversations={chat.conversations}
        activeId={chat.activeId}
        onSend={chat.send}
        onToggle={chat.toggleOpen}
        onNewChat={chat.newChat}
        onSwitchChat={chat.switchChat}
        onDeleteChat={chat.deleteChat}
        navigateToNode={navigateToNode}
        graphReady={graphReady}
      />
    </>
  )
}
