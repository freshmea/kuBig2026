from pathlib import Path

import webview

from backend.server import ClockApiServer

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


def main() -> None:
    server = ClockApiServer(FRONTEND_DIR)
    server.start()

    try:
        window = webview.create_window(
            "탁상 시계",
            url=server.base_url,
            width=460,
            height=320,
            resizable=True,
        )
        if window is None:
            raise RuntimeError("PyWebView 창을 생성하지 못했습니다.")

        webview.start()
    finally:
        server.stop()


if __name__ == "__main__":
    main()
