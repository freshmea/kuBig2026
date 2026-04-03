#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"

if [[ -s "$NVM_DIR/nvm.sh" ]]; then
    # Load the Linux Node.js runtime so Paperclip can start embedded PostgreSQL.
    . "$NVM_DIR/nvm.sh"
elif ! command -v npx >/dev/null 2>&1; then
    echo "npx is not available. Install Node.js or adjust NVM_DIR." >&2
    exit 1
fi

cd "$ROOT_DIR"
exec npx --yes paperclipai "$@"
