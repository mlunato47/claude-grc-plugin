import { useState, useCallback, useRef } from 'react'
import type { ChatMessage } from '../types'
import { streamChat } from '../api'

export function useChat(getSelectedNodeId: () => string | null) {
  const [messages, setMessages] = useState<ChatMessage[]>([])
  const [streamingText, setStreamingText] = useState('')
  const [isStreaming, setIsStreaming] = useState(false)
  const [isOpen, setIsOpen] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const abortRef = useRef<AbortController | null>(null)
  // Ref to always have the latest messages without stale closures
  const messagesRef = useRef<ChatMessage[]>([])
  messagesRef.current = messages

  const toggleOpen = useCallback(() => setIsOpen(prev => !prev), [])

  const send = useCallback((text: string) => {
    if (!text.trim() || isStreaming) return

    const userMsg: ChatMessage = { role: 'user', content: text.trim() }
    setMessages(prev => [...prev, userMsg])
    setError(null)
    setIsStreaming(true)
    setStreamingText('')

    let accumulated = ''

    // Read from ref to avoid stale closure over messages state
    const allMessages = [...messagesRef.current, userMsg]

    abortRef.current = streamChat(allMessages, getSelectedNodeId(), {
      onDelta(chunk) {
        accumulated += chunk
        setStreamingText(accumulated)
      },
      onDone() {
        setMessages(prev => [...prev, { role: 'assistant', content: accumulated }])
        setStreamingText('')
        setIsStreaming(false)
      },
      onError(err) {
        setIsStreaming(false)
        setStreamingText('')
        if (accumulated) {
          // Partial response — keep it
          setMessages(prev => [...prev, { role: 'assistant', content: accumulated }])
        } else {
          // No response at all — remove the failed user message
          setMessages(prev => prev.slice(0, -1))
        }
        setError(err.message)
      },
    })
  }, [isStreaming, getSelectedNodeId])

  return {
    messages, streamingText, isStreaming, isOpen, error,
    toggleOpen, send, setIsOpen,
  }
}
