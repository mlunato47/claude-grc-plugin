interface GraphCanvasProps {
  containerRef: React.RefObject<HTMLDivElement | null>
}

export function GraphCanvas({ containerRef }: GraphCanvasProps) {
  return <div ref={containerRef} id="cy" />
}
