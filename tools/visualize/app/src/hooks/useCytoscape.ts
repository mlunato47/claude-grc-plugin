import { useRef, useEffect, useCallback } from 'react'
import cytoscape, { type Core, type EventObject } from 'cytoscape'
import type { GraphPayload } from '../types'
import {
  NODE_COLORS, NODE_SHAPES, NODE_SIZES,
  PREDICATE_COLORS, PREDICATE_STYLES,
} from '../constants'

export interface SelectedNode {
  kind: 'node'
  id: string
}

export interface SelectedEdge {
  kind: 'edge'
  id: string
}

export type SelectedElement = SelectedNode | SelectedEdge | null

interface UseCytoscapeArgs {
  containerRef: React.RefObject<HTMLDivElement | null>
  graphData: GraphPayload | null
  onSelect: (el: SelectedElement) => void
  onReady?: () => void
}

export function useCytoscape({ containerRef, graphData, onSelect, onReady }: UseCytoscapeArgs) {
  const cyRef = useRef<Core | null>(null)

  // Create cytoscape instance when data arrives
  useEffect(() => {
    if (!graphData || !containerRef.current) return
    if (cyRef.current) { cyRef.current.destroy(); cyRef.current = null }

    const elements: cytoscape.ElementDefinition[] = []

    graphData.nodes.forEach(n => {
      elements.push({
        group: 'nodes',
        data: { id: n.id, label: n.label, type: n.type, ...n.props },
        classes: n.type,
      })
    })

    graphData.edges.forEach((e, i) => {
      elements.push({
        group: 'edges',
        data: {
          id: `e${i}`, source: e.source, target: e.target,
          predicate: e.predicate, plane: e.plane,
          confidence: e.confidence, meta: e.meta,
        },
        classes: `${e.plane} pred-${e.predicate}`,
      })
    })

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const style: any[] = [
      { selector: 'node', style: {
        'label': 'data(id)', 'font-size': 7, 'color': '#cbd5e1',
        'text-valign': 'bottom', 'text-margin-y': 3,
        'min-zoomed-font-size': 5,
        'text-max-width': 80, 'text-wrap': 'ellipsis',
      } as unknown as cytoscape.Css.Node },
      { selector: 'edge', style: {
        'width': 1, 'curve-style': 'bezier',
        'target-arrow-shape': 'triangle', 'arrow-scale': 0.5,
        'opacity': 0.5,
      } as unknown as cytoscape.Css.Edge },
      { selector: 'node.highlighted', style: {
        'border-width': 3, 'border-color': '#fbbf24', 'z-index': 100,
      } as unknown as cytoscape.Css.Node },
      { selector: 'node:selected', style: {
        'border-width': 3, 'border-color': '#f472b6',
      } as unknown as cytoscape.Css.Node },
      { selector: 'edge:selected', style: {
        'width': 3, 'opacity': 1, 'z-index': 100,
      } as unknown as cytoscape.Css.Edge },
      { selector: 'node.neighbor', style: {
        'border-width': 2, 'border-color': '#fbbf24', 'opacity': 1,
      } as unknown as cytoscape.Css.Node },
      { selector: 'node.dimmed', style: { 'opacity': 0.12 } as unknown as cytoscape.Css.Node },
      { selector: 'edge.dimmed', style: { 'opacity': 0.03 } as unknown as cytoscape.Css.Edge },
      { selector: 'node.faded', style: { 'opacity': 0.08 } as unknown as cytoscape.Css.Node },
      { selector: 'edge.faded', style: { 'opacity': 0.02 } as unknown as cytoscape.Css.Edge },
    ]

    Object.entries(NODE_COLORS).forEach(([type, color]) => {
      style.push({ selector: `node.${type}`, style: {
        'background-color': color,
        'shape': NODE_SHAPES[type] || 'ellipse',
        'width': NODE_SIZES[type] || 20,
        'height': NODE_SIZES[type] || 20,
      } as unknown as cytoscape.Css.Node })
    })

    Object.entries(PREDICATE_COLORS).forEach(([pred, color]) => {
      style.push({ selector: `edge.pred-${pred}`, style: {
        'line-color': color,
        'target-arrow-color': color,
        'line-style': PREDICATE_STYLES[pred] || 'solid',
      } as unknown as cytoscape.Css.Edge })
    })

    const cy = cytoscape({
      container: containerRef.current,
      elements,
      style,
      layout: {
        name: 'cose', animate: false,
        nodeRepulsion: () => 20000,
        idealEdgeLength: () => 100,
        nodeOverlap: 20,
        nodeDimensionsIncludeLabels: true,
        gravity: 0.3,
        numIter: 500,
      } as unknown as cytoscape.LayoutOptions,
      minZoom: 0.05, maxZoom: 6,
      wheelSensitivity: 0.25,
      pixelRatio: 1,
      textureOnViewport: true,
    })

    cy.on('tap', 'node', (evt: EventObject) => {
      const node = evt.target
      clearDimming(cy)
      const neighborhood = node.neighborhood()
      cy.elements().addClass('dimmed')
      node.removeClass('dimmed')
      neighborhood.removeClass('dimmed')
      neighborhood.nodes().addClass('neighbor')
      onSelect({ kind: 'node', id: node.id() })
    })

    cy.on('tap', 'edge', (evt: EventObject) => {
      onSelect({ kind: 'edge', id: evt.target.id() })
    })

    cy.on('tap', (evt: EventObject) => {
      if (evt.target === cy) {
        clearDimming(cy)
        onSelect(null)
      }
    })

    cyRef.current = cy
    onReady?.()

    return () => {
      cy.destroy()
      cyRef.current = null
    }
    // onSelect and onReady are stable via useCallback in App
  }, [graphData, containerRef, onSelect, onReady])

  const navigateToNode = useCallback((nodeId: string) => {
    const cy = cyRef.current
    if (!cy) return
    const target = cy.getElementById(nodeId)
    if (target.length > 0) {
      cy.animate({ center: { eles: target }, zoom: 2.5 }, { duration: 300 })
      target.emit('tap')
    }
  }, [])

  return { cyRef, navigateToNode }
}

function clearDimming(cy: Core) {
  cy.elements().removeClass('dimmed').removeClass('highlighted').removeClass('neighbor')
}
