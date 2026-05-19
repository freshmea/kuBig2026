from pathlib import Path

import webview

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


class ScreenApi:
    def get_screen_data(self) -> dict[str, object]:
        return {
            "home": {"title": "홈", "body": "상태 기반 화면 전환 데모입니다."},
            "settings": {"title": "설정", "body": "라우터 없이 같은 HTML 안에서 화면만 교체합니다."},
            "detail": {"title": "상세", "body": "표시할 데이터는 Python에서 제공합니다."},
        }


def main() -> None:
    webview.create_window(
        "11 Screen Router",
        url=(FRONTEND_DIR / "index.html").as_uri(),
        js_api=ScreenApi(),
        width=560,
        height=420,
        resizable=True,
    )
    webview.start()


if __name__ == "__main__":
    main()
