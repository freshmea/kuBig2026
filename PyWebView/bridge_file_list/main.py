from pathlib import Path

import webview

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"
DEMO_DIR = BASE_DIR / "demo_files"


class FileListApi:
    def __init__(self) -> None:
        DEMO_DIR.mkdir(exist_ok=True)
        for name, text in {
            "lesson.txt": "PyWebView API bridge demo",
            "students.csv": "name,score\nKim,95\nLee,88\n",
            "notes.md": "# Demo Notes\n\nPython returns this file list.\n",
        }.items():
            path = DEMO_DIR / name
            if not path.exists():
                path.write_text(text, encoding="utf-8")

    def list_files(self) -> list[dict[str, str | int]]:
        files = []
        for path in sorted(DEMO_DIR.iterdir()):
            if path.is_file():
                files.append({
                    "name": path.name,
                    "suffix": path.suffix or "(none)",
                    "size": path.stat().st_size,
                })
        return files


def main() -> None:
    webview.create_window(
        "03 API Bridge File List",
        url=(FRONTEND_DIR / "index.html").as_uri(),
        js_api=FileListApi(),
        width=520,
        height=420,
        resizable=True,
    )
    webview.start()


if __name__ == "__main__":
    main()
