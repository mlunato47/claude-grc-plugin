import { useState, useMemo, useCallback, memo } from 'react'
import { ChevronDown, ChevronRight, RotateCcw } from 'lucide-react'
import type { GraphPayload } from '../types'
import {
  NODE_COLORS, PREDICATE_COLORS, PREDICATE_ORDER, LAYOUT_OPTIONS,
} from '../constants'

interface SidebarProps {
  graphData: GraphPayload
  activePredicates: Set<string>
  activeTypes: Set<string>
  focusedFramework: string
  layout: string
  showLabels: boolean
  showOrphans: boolean
  onTogglePredicate: (pred: string) => void
  onToggleType: (type: string) => void
  onSetAllPredicates: (enabled: boolean) => void
  onSetAllTypes: (enabled: boolean) => void
  onFocusFramework: (fw: string) => void
  onChangeLayout: (layout: string) => void
  onChangeLabels: (show: boolean) => void
  onChangeOrphans: (show: boolean) => void
  onResetFilters: () => void
  graphReady: boolean
}

function CollapsibleSection({ title, defaultOpen = true, actions, children }: {
  title: string; defaultOpen?: boolean; actions?: React.ReactNode; children: React.ReactNode
}) {
  const [open, setOpen] = useState(defaultOpen)
  const toggle = useCallback(() => setOpen(v => !v), [])

  return (
    <div className="sidebar-section">
      <div className="sidebar-section-header" onClick={toggle}>
        <span className="chevron">
          {open ? <ChevronDown size={14} /> : <ChevronRight size={14} />}
        </span>
        <h3>{title}</h3>
        {actions && (
          <span className="section-actions" onClick={e => e.stopPropagation()}>
            {actions}
          </span>
        )}
      </div>
      <div
        className={`sidebar-section-content${open ? '' : ' collapsed'}`}
        style={open ? { maxHeight: 600 } : undefined}
      >
        {children}
      </div>
    </div>
  )
}

export const Sidebar = memo(function Sidebar({
  graphData, activePredicates, activeTypes, focusedFramework,
  layout, showLabels, showOrphans,
  onTogglePredicate, onToggleType, onSetAllPredicates, onSetAllTypes,
  onFocusFramework, onChangeLayout, onChangeLabels, onChangeOrphans,
  onResetFilters, graphReady,
}: SidebarProps) {
  const frameworks = useMemo(() =>
    graphData.nodes
      .filter(n => n.type === 'Framework')
      .sort((a, b) => a.label.localeCompare(b.label)),
    [graphData],
  )

  const predCounts = graphData.stats.edge_predicates
  const usedPreds = useMemo(() =>
    PREDICATE_ORDER.filter(p => predCounts[p]),
    [predCounts],
  )

  const typeCounts = graphData.stats.node_types

  const allPredsOn = usedPreds.every(p => activePredicates.has(p))
  const allTypesOn = Object.keys(NODE_COLORS).every(t => activeTypes.has(t))

  return (
    <aside className={graphReady ? '' : 'disabled-overlay'}>
      <CollapsibleSection title="Focus Framework">
        <select
          value={focusedFramework}
          onChange={e => onFocusFramework(e.target.value)}
          disabled={!graphReady}
        >
          <option value="">All Frameworks</option>
          {frameworks.map(fw => (
            <option key={fw.id} value={fw.id}>{fw.label}</option>
          ))}
        </select>
      </CollapsibleSection>

      <CollapsibleSection
        title="Edge Predicates"
        actions={
          <button
            className="toggle-all-btn"
            onClick={() => onSetAllPredicates(!allPredsOn)}
            disabled={!graphReady}
          >
            {allPredsOn ? 'None' : 'All'}
          </button>
        }
      >
        <div>
          {usedPreds.map(pred => (
            <label key={pred} className={graphReady ? '' : 'disabled'}>
              <input
                type="checkbox"
                checked={activePredicates.has(pred)}
                onChange={() => onTogglePredicate(pred)}
                disabled={!graphReady}
              />
              <span
                className="color-dot"
                style={{ background: PREDICATE_COLORS[pred] || '#475569' }}
              />
              {` ${pred} `}
              <span className="filter-count">{predCounts[pred] || 0}</span>
            </label>
          ))}
        </div>
      </CollapsibleSection>

      <CollapsibleSection
        title="Node Types"
        actions={
          <button
            className="toggle-all-btn"
            onClick={() => onSetAllTypes(!allTypesOn)}
            disabled={!graphReady}
          >
            {allTypesOn ? 'None' : 'All'}
          </button>
        }
      >
        <div>
          {Object.keys(NODE_COLORS).map(type => (
            <label key={type} className={graphReady ? '' : 'disabled'}>
              <input
                type="checkbox"
                checked={activeTypes.has(type)}
                onChange={() => onToggleType(type)}
                disabled={!graphReady}
              />
              <span className="color-dot" style={{ background: NODE_COLORS[type] }} />
              {` ${type} `}
              <span className="filter-count">{typeCounts[type] || 0}</span>
            </label>
          ))}
        </div>
      </CollapsibleSection>

      <CollapsibleSection title="Layout">
        <select
          value={layout}
          onChange={e => onChangeLayout(e.target.value)}
          disabled={!graphReady}
        >
          {LAYOUT_OPTIONS.map(opt => (
            <option key={opt.value} value={opt.value}>{opt.label}</option>
          ))}
        </select>
      </CollapsibleSection>

      <CollapsibleSection title="Visibility">
        <label className={graphReady ? '' : 'disabled'}>
          <input
            type="checkbox"
            checked={showLabels}
            onChange={e => onChangeLabels(e.target.checked)}
            disabled={!graphReady}
          />
          Show labels
        </label>
        <label className={graphReady ? '' : 'disabled'}>
          <input
            type="checkbox"
            checked={showOrphans}
            onChange={e => onChangeOrphans(e.target.checked)}
            disabled={!graphReady}
          />
          Show orphaned nodes
        </label>
      </CollapsibleSection>

      <button
        className="reset-filters-btn"
        onClick={onResetFilters}
        disabled={!graphReady}
      >
        <RotateCcw size={13} />
        Reset Filters
      </button>
    </aside>
  )
})
