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

  const toggleOpen = useCallback(() => setIsOpen(prev => !prev), [])

  const send = useCallback((text: string) => {
    if (!text.trim() || isStreaming) return

    const userMsg: ChatMessage = { role: 'user', content: text.trim() }
    setMessages(prev => [...prev, userMsg])
    setError(null)
    setIsStreaming(true)
    setStreamingText('')

    let accumulated = ''

    const allMessages = [...messages, userMsg]

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
          setMessages(prev => [...prev, { role: 'assistant', content: accumulated }])
        }
        setError(err.message)
      },
    })
  }, [messages, isStreaming, getSelectedNodeId])

  return {
    messages, streamingText, isStreaming, isOpen, error,
    toggleOpen, send, setIsOpen,
  }
}
