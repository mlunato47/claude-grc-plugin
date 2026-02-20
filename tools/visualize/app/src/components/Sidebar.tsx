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
  onFocusFramework: (fw: string) => void
  onChangeLayout: (layout: string) => void
  onChangeLabels: (show: boolean) => void
  onChangeOrphans: (show: boolean) => void
}

export function Sidebar({
  graphData, activePredicates, activeTypes, focusedFramework,
  layout, showLabels, showOrphans,
  onTogglePredicate, onToggleType, onFocusFramework,
  onChangeLayout, onChangeLabels, onChangeOrphans,
}: SidebarProps) {
  const frameworks = graphData.nodes
    .filter(n => n.type === 'Framework')
    .sort((a, b) => a.label.localeCompare(b.label))

  const predCounts = graphData.stats.edge_predicates
  const usedPreds = PREDICATE_ORDER.filter(p => predCounts[p])

  const typeCounts = graphData.stats.node_types

  return (
    <aside>
      <h3>Focus Framework</h3>
      <select value={focusedFramework} onChange={e => onFocusFramework(e.target.value)}>
        <option value="">All Frameworks</option>
        {frameworks.map(fw => (
          <option key={fw.id} value={fw.id}>{fw.label}</option>
        ))}
      </select>

      <h3>Edge Predicates</h3>
      <div>
        {usedPreds.map(pred => (
          <label key={pred}>
            <input
              type="checkbox"
              checked={activePredicates.has(pred)}
              onChange={() => onTogglePredicate(pred)}
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

      <h3>Node Types</h3>
      <div>
        {Object.keys(NODE_COLORS).map(type => (
          <label key={type}>
            <input
              type="checkbox"
              checked={activeTypes.has(type)}
              onChange={() => onToggleType(type)}
            />
            <span className="color-dot" style={{ background: NODE_COLORS[type] }} />
            {` ${type} `}
            <span className="filter-count">{typeCounts[type] || 0}</span>
          </label>
        ))}
      </div>

      <h3>Layout</h3>
      <select value={layout} onChange={e => onChangeLayout(e.target.value)}>
        {LAYOUT_OPTIONS.map(opt => (
          <option key={opt.value} value={opt.value}>{opt.label}</option>
        ))}
      </select>

      <h3>Visibility</h3>
      <label>
        <input
          type="checkbox"
          checked={showLabels}
          onChange={e => onChangeLabels(e.target.checked)}
        />
        Show labels
      </label>
      <label>
        <input
          type="checkbox"
          checked={showOrphans}
          onChange={e => onChangeOrphans(e.target.checked)}
        />
        Show orphaned nodes
      </label>
    </aside>
  )
}
