import sys
from pathlib import Path

import webview

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


class PackagingApi:
    def get_environment(self) -> dict[str, str | bool]:
        return {
            "python": sys.version.split()[0],
            "executable": sys.executable,
            "baseDir": str(BASE_DIR),
            "isFrozen": bool(getattr(sys, "frozen", False)),
        }

    def get_pyinstaller_command(self) -> str:
        return "pyinstaller --noconfirm --windowed packaging_demo/main.py"


def main() -> None:
    webview.create_window(
        "12 Packaging Demo",
        url=(FRONTEND_DIR / "index.html").as_uri(),
        js_api=PackagingApi(),
        width=660,
        height=440,
        resizable=True,
    )
    webview.start()


if __name__ == "__main__":
    main()
