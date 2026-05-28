import socket
from datetime import datetime
from pathlib import Path
from threading import Lock, Thread

from flask import Flask, send_from_directory
from werkzeug.serving import make_server


def getFreePort():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


class CounterApiServer:
    def __init__(self, frontend_dir):
        self.frontend_dir = Path(frontend_dir).resolve()
        self.port = getFreePort()
        self._count = 0
        self._lock = Lock()
        self._event_clients = []
        self.app = Flask(
            __name__,
            static_folder=str(self.frontend_dir),
            static_url_path="",
        )
        self._server = make_server("127.0.0.1", self.port, self.app)
        self._thread = Thread(target=self._server.serve_forever, daemon=True)
        self.app.add_url_rule("/", "index", self._serve_index)
        self.app.add_url_rule("/api/counter/increase", "increase", self._increase_payload, methods=["Post"])
        self.app.add_url_rule("/api/counter/decrease", "decrease", self._decrease_payload, methods=["Post"])

    def _serve_index(self):
        return send_from_directory(self.frontend_dir, "index.html")

    def _increase_payload(self):
        self._count += 1
        payload = {"count": self._count}
        return payload

    def _decrease_payload(self):
        self._count -= 1
        payload = {"count": self._count}
        return payload

    @property
    def base_url(self):
        return f"http://127.0.0.1:{self.port}"

    def start(self):
        self._thread.start()

    def stop(self):
        self._server.shutdown()
        self._thread.join(timeout=1)
