import { useRef, useEffect, useCallback, useMemo } from 'react'
import { marked } from 'marked'
import DOMPurify from 'dompurify'
import type { ChatMessage, GraphPayload } from '../types'

interface ChatDrawerProps {
  messages: ChatMessage[]
  streamingText: string
  isStreaming: boolean
  isOpen: boolean
  error: string | null
  graphData: GraphPayload | null
  onSend: (text: string) => void
  onToggle: () => void
  navigateToNode: (nodeId: string) => void
}

// Build a Set of node IDs for O(1) lookup instead of linear scan
function useNodeIdSet(graphData: GraphPayload | null): Set<string> {
  return useMemo(() => {
    if (!graphData) return new Set<string>()
    return new Set(graphData.nodes.map(n => n.id))
  }, [graphData])
}

function renderMarkdown(text: string, nodeIds: Set<string>): string {
  let html = marked.parse(text) as string
  // Make node IDs clickable
  html = html.replace(/\b([A-Z][A-Z0-9]*(?:-[A-Za-z0-9.]+)+)\b/g, (match) => {
    if (nodeIds.has(match)) {
      return `<a class="node-link" data-node-id="${match}">${match}</a>`
    }
    return match
  })
  return DOMPurify.sanitize(html, {
    ADD_ATTR: ['data-node-id'],
  })
}

export function ChatDrawer({
  messages, streamingText, isStreaming, isOpen, error,
  graphData, onSend, onToggle, navigateToNode,
}: ChatDrawerProps) {
  const messagesRef = useRef<HTMLDivElement>(null)
  const inputRef = useRef<HTMLTextAreaElement>(null)
  const nodeIds = useNodeIdSet(graphData)

  // Memoize rendered HTML per message to avoid re-rendering all messages on each update
  const renderedMessages = useMemo(() =>
    messages.map(msg =>
      msg.role === 'assistant' ? renderMarkdown(msg.content, nodeIds) : null
    ),
    [messages, nodeIds],
  )

  // Streaming text is rendered live (not memoized — changes every delta)
  const streamingHtml = streamingText ? renderMarkdown(streamingText, nodeIds) : ''

  // Auto-scroll on new content
  useEffect(() => {
    if (messagesRef.current) {
      messagesRef.current.scrollTop = messagesRef.current.scrollHeight
    }
  }, [messages, streamingText])

  // Focus input when opened
  useEffect(() => {
    if (isOpen && inputRef.current) inputRef.current.focus()
  }, [isOpen])

  const handleKeyDown = useCallback((e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      const input = inputRef.current
      if (input) {
        onSend(input.value)
        input.value = ''
        input.style.height = 'auto'
      }
    }
  }, [onSend])

  const handleSendClick = useCallback(() => {
    const input = inputRef.current
    if (input) {
      onSend(input.value)
      input.value = ''
      input.style.height = 'auto'
    }
  }, [onSend])

  const handleInput = useCallback(() => {
    const input = inputRef.current
    if (input) {
      input.style.height = 'auto'
      input.style.height = Math.min(input.scrollHeight, 120) + 'px'
    }
  }, [])

  const handleBubbleClick = useCallback((e: React.MouseEvent) => {
    const target = e.target as HTMLElement
    if (target.classList.contains('node-link')) {
      e.preventDefault()
      const nodeId = target.getAttribute('data-node-id')
      if (nodeId) navigateToNode(nodeId)
    }
  }, [navigateToNode])

  return (
    <div id="chat-drawer" className={isOpen ? '' : 'collapsed'}>
      <div id="chat-header" onClick={onToggle}>
        <h3>Chat with Claude</h3>
        <span className="chat-status">
          {isStreaming ? 'Thinking...' : ''}
        </span>
        <span className="chat-toggle">
          {isOpen ? '\u25BC' : '\u25B2'}
        </span>
      </div>
      <div id="chat-messages" ref={messagesRef}>
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`chat-msg ${msg.role}`}
            onClick={msg.role === 'assistant' ? handleBubbleClick : undefined}
            dangerouslySetInnerHTML={
              msg.role === 'assistant'
                ? { __html: renderedMessages[i]! }
                : undefined
            }
          >
            {msg.role === 'user' ? msg.content : undefined}
          </div>
        ))}
        {streamingHtml && (
          <div
            className="chat-msg assistant"
            onClick={handleBubbleClick}
            dangerouslySetInnerHTML={{ __html: streamingHtml }}
          />
        )}
        {error && (
          <div className="chat-msg error">{error}</div>
        )}
      </div>
      <div id="chat-input-bar">
        <textarea
          ref={inputRef}
          id="chat-input"
          rows={2}
          placeholder='Ask about the graph (e.g., "What controls are in FedRAMP Moderate?")'
          onKeyDown={handleKeyDown}
          onInput={handleInput}
        />
        <button
          id="chat-send"
          onClick={handleSendClick}
          disabled={isStreaming}
        >
          Send
        </button>
      </div>
    </div>
  )
}
