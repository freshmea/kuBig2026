from pathlib import Path

import webview
from backend.server_flask import ClockApiServer

BASE_DIR = Path(__file__).resolve().parent
FRONTED_DIR = BASE_DIR / "frontend"


def main():
    server = ClockApiServer(FRONTEND_DIR)
    server.start()

    webview.create_window("Timer", html="<h1>Hello Webview</h1>")
    webview.start()


if __name__ == "__main__":
    main()
