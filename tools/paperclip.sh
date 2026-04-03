#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"

if [[ ! -s "$NVM_DIR/nvm.sh" ]]; then
    echo "nvm is not installed. Install it first or adjust NVM_DIR." >&2
    exit 1
fi

# Load the Linux Node.js runtime so Paperclip can start embedded PostgreSQL.
. "$NVM_DIR/nvm.sh"

cd "$ROOT_DIR"
exec npx --yes paperclipai "$@"