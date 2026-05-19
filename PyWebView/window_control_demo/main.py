from pathlib import Path

import webview

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


class WindowApi:
    def __init__(self) -> None:
        self._window: webview.Window | None = None

    def set_window(self, window: webview.Window) -> None:
        self._window = window

    def resize_small(self) -> str:
        if self._window is not None:
            self._window.resize(480, 360)
        return "480 x 360"

    def resize_large(self) -> str:
        if self._window is not None:
            self._window.resize(760, 560)
        return "760 x 560"

    def toggle_fullscreen(self) -> str:
        if self._window is not None:
            self._window.toggle_fullscreen()
        return "fullscreen toggled"

    def confirm_close(self) -> str:
        if self._window is None:
            return "window not ready"
        ok = self._window.create_confirmation_dialog("확인", "창 제어 API 호출이 성공했습니다.")
        return "확인 선택" if ok else "취소 선택"

    def open_child_window(self) -> str:
        webview.create_window("Child Window", html="<h1>새 창</h1><p>Python에서 생성한 창입니다.</p>", width=320, height=220)
        return "새 창 생성"


def main() -> None:
    api = WindowApi()
    window = webview.create_window(
        "10 Window Control",
        url=(FRONTEND_DIR / "index.html").as_uri(),
        js_api=api,
        width=560,
        height=420,
        resizable=True,
    )
    api.set_window(window)
    webview.start()


if __name__ == "__main__":
    main()
