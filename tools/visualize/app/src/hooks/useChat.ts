import { useState, useCallback, useRef, useEffect } from 'react'
import type { ChatMessage } from '../types'
import { streamChat } from '../api'

export interface Conversation {
  id: string
  title: string
  messages: ChatMessage[]
  updatedAt: number
}

const STORAGE_KEY = 'grc-kg-chat-conversations'
const ACTIVE_KEY = 'grc-kg-chat-active'

function generateId(): string {
  return Date.now().toString(36) + Math.random().toString(36).slice(2, 6)
}

function loadConversations(): Conversation[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    if (!raw) {
      // Migrate from old single-chat format
      const oldMessages = localStorage.getItem('grc-kg-chat-messages')
      if (oldMessages) {
        const msgs: ChatMessage[] = JSON.parse(oldMessages)
        if (msgs.length > 0) {
          const first = msgs.find(m => m.role === 'user')
          const conv: Conversation = {
            id: generateId(),
            title: first ? first.content.slice(0, 50) : 'Chat',
            messages: msgs,
            updatedAt: Date.now(),
          }
          localStorage.setItem(STORAGE_KEY, JSON.stringify([conv]))
          localStorage.setItem(ACTIVE_KEY, conv.id)
          localStorage.removeItem('grc-kg-chat-messages')
          return [conv]
        }
      }
    }
    return raw ? JSON.parse(raw) : []
  } catch {
    return []
  }
}

function loadActiveId(): string | null {
  return localStorage.getItem(ACTIVE_KEY)
}

function deriveTitle(messages: ChatMessage[]): string {
  const first = messages.find(m => m.role === 'user')
  if (!first) return 'New Chat'
  const text = first.content.trim()
  return text.length > 50 ? text.slice(0, 47) + '...' : text
}

export function useChat(getSelectedNodeId: () => string | null) {
  const initConvs = loadConversations
  const [conversations, setConversations] = useState<Conversation[]>(initConvs)
  const [activeId, setActiveId] = useState<string | null>(() => {
    const saved = loadActiveId()
    const convs = conversations   // use already-loaded state
    if (saved && convs.some(c => c.id === saved)) return saved
    return convs.length > 0 ? convs[0].id : null
  })

  const activeIdRef = useRef(activeId)
  activeIdRef.current = activeId

  const activeConv = conversations.find(c => c.id === activeId) ?? null
  const messages = activeConv?.messages ?? []

  const [streamingText, setStreamingText] = useState('')
  const [isStreaming, setIsStreaming] = useState(false)
  const [isOpen, setIsOpen] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const abortRef = useRef<AbortController | null>(null)
  const messagesRef = useRef<ChatMessage[]>([])
  messagesRef.current = messages

  // Persist conversations to localStorage
  useEffect(() => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(conversations))
  }, [conversations])

  useEffect(() => {
    if (activeId) localStorage.setItem(ACTIVE_KEY, activeId)
  }, [activeId])

  const toggleOpen = useCallback(() => setIsOpen(prev => !prev), [])

  // Use a stable helper that reads activeIdRef — no stale closure over activeId
  const updateConversationMessages = useCallback((convId: string, updater: (prev: ChatMessage[]) => ChatMessage[]) => {
    setConversations(prev => prev.map(c => {
      if (c.id !== convId) return c
      const newMsgs = updater(c.messages)
      return { ...c, messages: newMsgs, title: deriveTitle(newMsgs), updatedAt: Date.now() }
    }))
  }, [])

  const send = useCallback((text: string) => {
    if (!text.trim() || isStreaming) return

    const userMsg: ChatMessage = { role: 'user', content: text.trim() }

    // If no active conversation, create one
    let targetId = activeIdRef.current
    if (!targetId) {
      const newConv: Conversation = {
        id: generateId(),
        title: text.trim().slice(0, 50),
        messages: [],
        updatedAt: Date.now(),
      }
      targetId = newConv.id
      setConversations(prev => [newConv, ...prev])
      setActiveId(targetId)
      activeIdRef.current = targetId
    }

    // Capture targetId for all callbacks — immune to future activeId changes
    const sendTargetId = targetId

    updateConversationMessages(sendTargetId, prev => [...prev, userMsg])
    setError(null)
    setIsStreaming(true)
    setStreamingText('')

    let accumulated = ''
    const allMessages = [...messagesRef.current, userMsg]

    abortRef.current = streamChat(allMessages, getSelectedNodeId(), {
      onDelta(chunk) {
        accumulated += chunk
        setStreamingText(accumulated)
      },
      onDone() {
        updateConversationMessages(sendTargetId, prev => [...prev, { role: 'assistant', content: accumulated }])
        setStreamingText('')
        setIsStreaming(false)
      },
      onError(err) {
        setIsStreaming(false)
        setStreamingText('')
        if (accumulated) {
          updateConversationMessages(sendTargetId, prev => [...prev, { role: 'assistant', content: accumulated }])
        } else {
          updateConversationMessages(sendTargetId, prev => prev.slice(0, -1))
        }
        setError(err.message)
      },
    })
  }, [isStreaming, getSelectedNodeId, updateConversationMessages])

  const newChat = useCallback(() => {
    if (isStreaming && abortRef.current) abortRef.current.abort()
    const conv: Conversation = {
      id: generateId(),
      title: 'New Chat',
      messages: [],
      updatedAt: Date.now(),
    }
    setConversations(prev => [conv, ...prev])
    setActiveId(conv.id)
    setStreamingText('')
    setIsStreaming(false)
    setError(null)
  }, [isStreaming])

  const switchChat = useCallback((id: string) => {
    if (isStreaming && abortRef.current) abortRef.current.abort()
    setActiveId(id)
    setStreamingText('')
    setIsStreaming(false)
    setError(null)
  }, [isStreaming])

  const deleteChat = useCallback((id: string) => {
    setConversations(prev => {
      const next = prev.filter(c => c.id !== id)
      if (id === activeIdRef.current) {
        setActiveId(next.length > 0 ? next[0].id : null)
      }
      return next
    })
  }, [])

  const clear = useCallback(() => {
    if (isStreaming && abortRef.current) abortRef.current.abort()
    const id = activeIdRef.current
    if (id) updateConversationMessages(id, () => [])
    setStreamingText('')
    setIsStreaming(false)
    setError(null)
  }, [isStreaming, updateConversationMessages])

  return {
    messages, streamingText, isStreaming, isOpen, error,
    conversations, activeId,
    toggleOpen, send, setIsOpen, clear,
    newChat, switchChat, deleteChat,
  }
}
