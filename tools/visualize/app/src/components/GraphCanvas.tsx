import { useRef, useEffect } from 'react'

interface GraphCanvasProps {
  containerRef: React.RefObject<HTMLDivElement | null>
}

export function GraphCanvas({ containerRef }: GraphCanvasProps) {
  // We need to forward the ref to the parent, but the parent already owns it.
  // This component just renders the container div.
  const localRef = useRef<HTMLDivElement>(null)

  // Sync the parent ref to point to our div
  useEffect(() => {
    if (containerRef && 'current' in containerRef) {
      (containerRef as React.MutableRefObject<HTMLDivElement | null>).current = localRef.current
    }
  })

  return <div ref={localRef} id="cy" />
}
