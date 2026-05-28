from pathlib import Path

import webview
from backend.server_flask import ClockApiServer

BASE_DIR = Path(__file__).resolve().parent
FRONTED_DIR = BASE_DIR / "frontend"


def main():
    server = ClockApiServer(FRONTED_DIR)
    server.start()

    webview.create_window("탁상시계", url=server.base_url, width=460, height=320, resizable=True)
    webview.start()


if __name__ == "__main__":
    main()
