#!/usr/bin/env bash

PAPERCLIP_URL="http://127.0.0.1:3100/api/health"

if pgrep -af "paperclipai run" >/dev/null && curl -fsS "$PAPERCLIP_URL" >/dev/null 2>&1; then
    echo "RUNNING"
    exit 0
else
    echo "NOT RUNNING"
    exit 1
fi