import json
from pathlib import Path

import webview

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"
DATA_DIR = BASE_DIR / "data"
SETTINGS_PATH = DATA_DIR / "settings.json"
DEFAULT_SETTINGS = {"theme": "light", "fontSize": 18, "lastCount": 0}


class SettingsApi:
    def __init__(self) -> None:
        DATA_DIR.mkdir(exist_ok=True)

    def load_settings(self) -> dict[str, str | int]:
        if not SETTINGS_PATH.exists():
            return DEFAULT_SETTINGS.copy()
        try:
            saved = json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return DEFAULT_SETTINGS.copy()
        return DEFAULT_SETTINGS | saved

    def save_settings(self, settings: dict[str, str | int]) -> dict[str, str]:
        next_settings = DEFAULT_SETTINGS | settings
        SETTINGS_PATH.write_text(
            json.dumps(next_settings, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return {"status": "saved", "path": str(SETTINGS_PATH)}


def main() -> None:
    webview.create_window(
        "05 Settings Store",
        url=(FRONTEND_DIR / "index.html").as_uri(),
        js_api=SettingsApi(),
        width=520,
        height=460,
        resizable=True,
    )
    webview.start()


if __name__ == "__main__":
    main()
