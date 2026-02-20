import type { GraphPayload, ChatMessage } from './types'

export async function fetchGraph(): Promise<GraphPayload> {
  const res = await fetch('/api/graph')
  if (!res.ok) throw new Error(`Failed to load graph: HTTP ${res.status}`)
  return res.json()
}

export interface StreamCallbacks {
  onDelta: (text: string) => void
  onDone: () => void
  onError: (err: Error) => void
}

export function streamChat(
  messages: ChatMessage[],
  selectedNode: string | null,
  callbacks: StreamCallbacks,
): AbortController {
  const controller = new AbortController()

  ;(async () => {
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages, selectedNode }),
        signal: controller.signal,
      })

      if (!res.ok) {
        const err = await res.json().catch(() => ({ error: `HTTP ${res.status}` }))
        throw new Error(err.error || `HTTP ${res.status}`)
      }

      if (!res.body) {
        throw new Error('Response body is null — streaming not supported')
      }

      const reader = res.body.getReader()
      const decoder = new TextDecoder()
      let buffer = ''

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        buffer += decoder.decode(value, { stream: true })
        const lines = buffer.split('\n')
        buffer = lines.pop()!

        for (const line of lines) {
          if (!line.startsWith('data: ')) continue
          let data: { type: string; text?: string }
          try {
            data = JSON.parse(line.slice(6))
          } catch {
            continue // skip malformed SSE lines
          }

          if (data.type === 'delta') {
            callbacks.onDelta(data.text!)
          } else if (data.type === 'done') {
            // Server signals completion — stream reader will also end
          } else if (data.type === 'error') {
            throw new Error(data.text)
          }
        }
      }

      // Process any remaining buffer content
      if (buffer.trim().startsWith('data: ')) {
        try {
          const data = JSON.parse(buffer.trim().slice(6))
          if (data.type === 'delta') callbacks.onDelta(data.text!)
          else if (data.type === 'done') { /* ok */ }
          else if (data.type === 'error') throw new Error(data.text)
        } catch {
          // ignore trailing malformed data
        }
      }

      callbacks.onDone()
    } catch (err) {
      if ((err as Error).name !== 'AbortError') {
        callbacks.onError(err as Error)
      }
    }
  })()

  return controller
}
