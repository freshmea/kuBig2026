import socket
from datetime import datetime
from pathlib import Path
from threading import Thread

from flask import Flask, send_from_directory
from werkzeug.serving import make_server

WEEKDAYS = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]


def getClockPayload():
    now = datetime.now()
    return {"time": now.strftime("%H:%M:%S"),
            "date": f"{now.year}년 {now.month}월 {now.day}일 {WEEKDAYS[now.weekday()]}"}


def getFreePort():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


class ClockApiServer:
    def __init__(self, frontend_dir):
        self.frontend_dir = Path(frontend_dir).resolve()
        self.index_file = self.frontend_dir / "index.html"
        if not self.index_file.is_file():
            raise FileNotFoundError(
                f"Frontend entry file not found: {self.index_file}"
            )

        self.port = getFreePort()
        self.app = Flask(
            __name__,
            static_folder=str(self.frontend_dir),
            static_url_path="",
        )
        self._server = make_server("127.0.0.1", self.port, self.app)
        self._thread = Thread(target=self._server.serve_forever, daemon=True)
        self.app.add_url_rule("/", "index", self._serve_index)
        self.app.add_url_rule("/api/clock", "clock", lambda: getClockPayload())

    def _serve_index(self):
        return send_from_directory(self.frontend_dir, self.index_file.name)

    @property
    def base_url(self):
        return f"http://127.0.0.1:{self.port}"

    def start(self):
        self._thread.start()
