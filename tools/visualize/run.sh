#!/usr/bin/env bash
# Start both the Python backend and Vite dev server for the KG viewer.
# Usage: bash tools/visualize/run.sh

set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$DIR/../.." && pwd)"

# Check for ANTHROPIC_API_KEY
if [ -z "$ANTHROPIC_API_KEY" ]; then
  # Try loading from .env at repo root
  if [ -f "$REPO/.env" ]; then
    export $(grep -v '^#' "$REPO/.env" | grep ANTHROPIC_API_KEY | xargs)
  fi
  if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "WARNING: ANTHROPIC_API_KEY not set — chat will not work"
  fi
fi

cleanup() {
  echo "Shutting down..."
  kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
  wait $BACKEND_PID $FRONTEND_PID 2>/dev/null
}
trap cleanup EXIT

# Find python
PYTHON=""
for cmd in python3 py python; do
  if command -v "$cmd" &>/dev/null; then PYTHON="$cmd"; break; fi
done
if [ -z "$PYTHON" ]; then
  echo "ERROR: No python found on PATH"; exit 1
fi

# Start backend
echo "Starting backend (serve.py) with $PYTHON..."
"$PYTHON" "$DIR/serve.py" &
BACKEND_PID=$!

# Start frontend
echo "Starting frontend (vite)..."
cd "$DIR/app" && npm run dev &
FRONTEND_PID=$!

echo "Backend PID: $BACKEND_PID | Frontend PID: $FRONTEND_PID"
echo "Press Ctrl+C to stop both."

wait
