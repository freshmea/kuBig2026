from pathlib import Path

import webview

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"
DATA_DIR = BASE_DIR / "data"
NOTE_PATH = DATA_DIR / "note.txt"


class MemoApi:
    def __init__(self) -> None:
        DATA_DIR.mkdir(exist_ok=True)
        if not NOTE_PATH.exists():
            NOTE_PATH.write_text("처음 메모를 입력해 보세요.", encoding="utf-8")

    def load_note(self) -> dict[str, str]:
        return {"text": NOTE_PATH.read_text(encoding="utf-8")}

    def save_note(self, text: str) -> dict[str, str]:
        NOTE_PATH.write_text(text, encoding="utf-8")
        return {"status": "saved", "path": str(NOTE_PATH)}


def main() -> None:
    webview.create_window(
        "04 Memo File IO",
        url=(FRONTEND_DIR / "index.html").as_uri(),
        js_api=MemoApi(),
        width=640,
        height=520,
        resizable=True,
    )
    webview.start()


if __name__ == "__main__":
    main()
