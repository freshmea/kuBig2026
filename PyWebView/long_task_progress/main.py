from pathlib import Path
from threading import Lock, Thread
from time import sleep

import webview

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


class LongTaskApi:
    def __init__(self) -> None:
        self._lock = Lock()
        self._running = False
        self._progress = 0
        self._message = "대기 중"

    def start_task(self) -> dict[str, object]:
        with self._lock:
            if self._running:
                return self.get_progress()
            self._running = True
            self._progress = 0
            self._message = "작업 시작"

        Thread(target=self._run_task, daemon=True).start()
        return self.get_progress()

    def get_progress(self) -> dict[str, object]:
        with self._lock:
            return {
                "running": self._running,
                "progress": self._progress,
                "message": self._message,
            }

    def _run_task(self) -> None:
        for step in range(1, 11):
            sleep(0.35)
            with self._lock:
                self._progress = step * 10
                self._message = f"{step}/10 단계 처리 중"

        with self._lock:
            self._running = False
            self._message = "작업 완료"


def main() -> None:
    webview.create_window(
        "09 Long Task Progress",
        url=(FRONTEND_DIR / "index.html").as_uri(),
        js_api=LongTaskApi(),
        width=520,
        height=360,
        resizable=True,
    )
    webview.start()


if __name__ == "__main__":
    main()
