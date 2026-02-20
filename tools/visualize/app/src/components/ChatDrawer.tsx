import { useRef, useEffect, useCallback, useMemo } from 'react'
import { Bot, User, SendHorizontal, ChevronDown, ChevronUp, MessageCircle } from 'lucide-react'
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

    // Node link click
    if (target.classList.contains('node-link')) {
      e.preventDefault()
      const nodeId = target.getAttribute('data-node-id')
      if (nodeId) navigateToNode(nodeId)
      return
    }

    // Code copy button click
    if (target.closest('.code-copy-btn')) {
      const btn = target.closest('.code-copy-btn') as HTMLElement
      const pre = btn.closest('pre')
      if (pre) {
        const code = pre.querySelector('code')
        const text = code ? code.textContent || '' : pre.textContent || ''
        navigator.clipboard.writeText(text)
        btn.classList.add('copied')
        setTimeout(() => btn.classList.remove('copied'), 1500)
      }
      return
    }
  }, [navigateToNode])

  // Inject copy buttons into rendered HTML pre blocks
  const injectCopyButtons = useCallback((html: string, msgIdx: number): string => {
    let blockIdx = 0
    return html.replace(/<pre>/g, () => {
      const id = `${msgIdx}-${blockIdx++}`
      return `<pre><button class="code-copy-btn" data-copy-id="${id}" title="Copy code">` +
        `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">` +
        `<rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg></button>`
    })
  }, [])

  return (
    <div id="chat-drawer" className={isOpen ? '' : 'collapsed'}>
      <div id="chat-header" onClick={onToggle}>
        <Bot size={18} className="chat-header-icon" />
        <h3>Chat with Claude</h3>
        <span className="chat-status">
          {isStreaming && (
            <>
              <span className="streaming-dot" />
              Thinking...
            </>
          )}
        </span>
        <span className="chat-toggle">
          {isOpen ? <ChevronDown size={16} /> : <ChevronUp size={16} />}
        </span>
      </div>
      <div id="chat-messages" ref={messagesRef}>
        {messages.length === 0 && !streamingHtml && !error && (
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', flex: 1, gap: 8, color: 'var(--text-dim)' }}>
            <MessageCircle size={28} style={{ opacity: 0.4 }} />
            <span style={{ fontSize: 13 }}>Ask about the knowledge graph</span>
          </div>
        )}
        {messages.map((msg, i) => (
          <div key={i} className={`chat-msg-row ${msg.role}`}>
            <div className={`chat-avatar ${msg.role === 'user' ? 'user-avatar' : 'assistant-avatar'}`}>
              {msg.role === 'user' ? <User size={14} /> : <Bot size={14} />}
            </div>
            <div
              className={`chat-msg ${msg.role}`}
              onClick={msg.role === 'assistant' ? handleBubbleClick : undefined}
              dangerouslySetInnerHTML={
                msg.role === 'assistant'
                  ? { __html: injectCopyButtons(renderedMessages[i]!, i) }
                  : undefined
              }
            >
              {msg.role === 'user' ? msg.content : undefined}
            </div>
          </div>
        ))}
        {streamingHtml && (
          <div className="chat-msg-row assistant">
            <div className="chat-avatar assistant-avatar">
              <Bot size={14} />
            </div>
            <div
              className="chat-msg assistant"
              onClick={handleBubbleClick}
              dangerouslySetInnerHTML={{ __html: streamingHtml }}
            />
          </div>
        )}
        {isStreaming && !streamingHtml && (
          <div className="streaming-dots">
            <span /><span /><span />
          </div>
        )}
        {error && (
          <div className="chat-msg error">{error}</div>
        )}
      </div>
      <div id="chat-input-bar">
        <div className="chat-input-wrapper">
          <MessageCircle size={14} className="input-icon" />
          <textarea
            ref={inputRef}
            id="chat-input"
            rows={2}
            placeholder='Ask about the graph (e.g., "What controls are in FedRAMP Moderate?")'
            onKeyDown={handleKeyDown}
            onInput={handleInput}
          />
        </div>
        <button
          id="chat-send"
          onClick={handleSendClick}
          disabled={isStreaming}
          title="Send message"
        >
          <SendHorizontal size={18} />
        </button>
      </div>
    </div>
  )
}
