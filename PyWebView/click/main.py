from pathlib import Path

import webview

from backend.server import CounterApiServer

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


def main() -> None:
    server = CounterApiServer(FRONTEND_DIR)
    server.start()

    try:
        window = webview.create_window(
            "Click Counter Demo",
            url=server.base_url,
            width=420,
            height=360,
            resizable=True,
        )
        if window is None:
            raise RuntimeError("PyWebView window could not be created.")

        webview.start()
    finally:
        server.stop()


if __name__ == "__main__":
    main()
