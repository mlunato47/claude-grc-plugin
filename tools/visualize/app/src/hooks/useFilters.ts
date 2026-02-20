import { useState, useCallback, useRef, useEffect } from 'react'
import type { Core, LayoutOptions } from 'cytoscape'
import type { GraphPayload } from '../types'
import { DEFAULT_ON_PREDICATES, NODE_COLORS } from '../constants'

// Cytoscape types don't expose show/hide on singular elements; use collection methods
// eslint-disable-next-line @typescript-eslint/no-explicit-any
type CyAny = any

export interface FilterState {
  activePredicates: Set<string>
  activeTypes: Set<string>
  focusedFramework: string
  layout: string
  showLabels: boolean
  showOrphans: boolean
}

export function useFilters(cyRef: React.RefObject<Core | null>, graphData: GraphPayload | null) {
  const [activePredicates, setActivePredicates] = useState<Set<string>>(new Set(DEFAULT_ON_PREDICATES))
  const [activeTypes, setActiveTypes] = useState<Set<string>>(new Set(Object.keys(NODE_COLORS)))
  const [focusedFramework, setFocusedFramework] = useState('')
  const [layout, setLayout] = useState('cose')
  const [showLabels, setShowLabels] = useState(true)
  const [showOrphans, setShowOrphans] = useState(false)

  // Track visible counts for stats
  const [visibleNodes, setVisibleNodes] = useState(0)
  const [visibleEdges, setVisibleEdges] = useState(0)

  // Ref to avoid stale closure in applyFilters
  const stateRef = useRef({ activePredicates, activeTypes, focusedFramework, showOrphans })
  stateRef.current = { activePredicates, activeTypes, focusedFramework, showOrphans }

  const applyFilters = useCallback(() => {
    const cy = cyRef.current
    if (!cy) return
    const { activePredicates, activeTypes, focusedFramework, showOrphans } = stateRef.current

    // Edge predicates
    cy.edges().forEach((e: CyAny) => {
      if (activePredicates.has(e.data('predicate'))) e.show(); else e.hide()
    })

    // Node types
    cy.nodes().forEach((n: CyAny) => {
      if (activeTypes.has(n.data('type'))) n.show(); else n.hide()
    })

    // Framework focus
    cy.elements().removeClass('faded')
    if (focusedFramework) {
      const fwNode = cy.getElementById(focusedFramework)
      if (fwNode.length > 0) {
        const inScope = cy.collection()
        inScope.merge(fwNode)

        let frontier = fwNode
        for (let depth = 0; depth < 4; depth++) {
          const nextEdges = frontier.connectedEdges().filter(e =>
            e.data('predicate') === 'CONTAINS' && e.source().id() !== e.target().id()
          )
          const nextNodes = nextEdges.connectedNodes().difference(inScope)
          if (nextNodes.length === 0) break
          inScope.merge(nextEdges)
          inScope.merge(nextNodes)
          frontier = nextNodes
        }

        const controls = inScope.nodes().filter(n => n.data('type') === 'Control')
        const crossEdges = controls.connectedEdges().filter(e => e.visible())
        const crossNodes = crossEdges.connectedNodes()
        inScope.merge(crossEdges)
        inScope.merge(crossNodes)

        cy.elements().addClass('faded')
        inScope.removeClass('faded')
      }
    }

    // Hide orphans
    if (!showOrphans) {
      cy.nodes().forEach((n: CyAny) => {
        if (n.visible() && n.connectedEdges().filter((e: CyAny) => e.visible()).length === 0) n.hide()
      })
    }

    // Update visible counts
    const vn = cy.nodes().filter(n => n.visible() && !n.hasClass('faded')).length
    const ve = cy.edges().filter(e => e.visible() && !e.hasClass('faded')).length
    setVisibleNodes(vn)
    setVisibleEdges(ve)
  }, [cyRef])

  // Apply filters whenever state changes
  useEffect(() => {
    applyFilters()
  }, [activePredicates, activeTypes, focusedFramework, showOrphans, applyFilters])

  // Apply filters once graph is ready
  useEffect(() => {
    if (cyRef.current && graphData) {
      // Short delay to let cytoscape finish layout
      const t = setTimeout(applyFilters, 100)
      return () => clearTimeout(t)
    }
  }, [graphData, cyRef, applyFilters])

  const togglePredicate = useCallback((pred: string) => {
    setActivePredicates(prev => {
      const next = new Set(prev)
      if (next.has(pred)) next.delete(pred); else next.add(pred)
      return next
    })
  }, [])

  const toggleType = useCallback((type: string) => {
    setActiveTypes(prev => {
      const next = new Set(prev)
      if (next.has(type)) next.delete(type); else next.add(type)
      return next
    })
  }, [])

  const setAllPredicates = useCallback((enabled: boolean) => {
    if (enabled) {
      const all = Object.keys(
        graphData?.stats.edge_predicates ?? {},
      )
      setActivePredicates(new Set(all))
    } else {
      setActivePredicates(new Set())
    }
  }, [graphData])

  const setAllTypes = useCallback((enabled: boolean) => {
    if (enabled) {
      setActiveTypes(new Set(Object.keys(NODE_COLORS)))
    } else {
      setActiveTypes(new Set())
    }
  }, [])

  const changeLayout = useCallback((name: string) => {
    setLayout(name)
    const cy = cyRef.current
    if (!cy) return
    const opts: Record<string, unknown> = {
      name, animate: true, animationDuration: 500, nodeDimensionsIncludeLabels: true,
    }
    if (name === 'cose') {
      opts.animate = false; opts.nodeRepulsion = () => 20000
      opts.idealEdgeLength = () => 100; opts.gravity = 0.3; opts.numIter = 500
    }
    if (name === 'breadthfirst') { opts.directed = true; opts.spacingFactor = 0.8 }
    if (name === 'concentric') {
      opts.concentric = (n: { degree: () => number }) => n.degree()
      opts.levelWidth = () => 4
    }
    cy.layout(opts as unknown as LayoutOptions).run()
  }, [cyRef])

  const changeLabels = useCallback((show: boolean) => {
    setShowLabels(show)
    const cy = cyRef.current
    if (!cy) return
    cy.style().selector('node').style('label', show ? 'data(id)' : '').update()
  }, [cyRef])

  const resetFilters = useCallback(() => {
    setActivePredicates(new Set(DEFAULT_ON_PREDICATES))
    setActiveTypes(new Set(Object.keys(NODE_COLORS)))
    setFocusedFramework('')
    setShowOrphans(false)
    setShowLabels(true)
    const cy = cyRef.current
    if (!cy) return
    cy.elements().removeClass('faded').removeClass('dimmed').removeClass('highlighted').removeClass('neighbor')
    cy.style().selector('node').style('label', 'data(id)').update()
    setTimeout(() => cy.fit(undefined, 40), 50)
  }, [cyRef])

  return {
    activePredicates, activeTypes, focusedFramework, layout,
    showLabels, showOrphans, visibleNodes, visibleEdges,
    togglePredicate, toggleType, setAllPredicates, setAllTypes,
    setFocusedFramework, changeLayout, changeLabels, setShowOrphans,
    resetFilters, applyFilters,
  }
}
