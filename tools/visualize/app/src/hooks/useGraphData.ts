import { useState, useEffect } from 'react'
import type { GraphPayload } from '../types'
import { fetchGraph } from '../api'

export function useGraphData() {
  const [data, setData] = useState<GraphPayload | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchGraph().then(setData).catch(e => setError(e.message))
  }, [])

  return { data, error }
}
