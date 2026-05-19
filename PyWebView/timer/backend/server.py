import json
import socket
from datetime import datetime
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.parse import urlparse

WEEKDAYS = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
type ClockPayload = dict[str, str]


class ClockApiServer:
    def __init__(self, frontend_dir: Path) -> None:
        self.frontend_dir = frontend_dir
        self.port = self._get_free_port()
        self._server = ThreadingHTTPServer(("127.0.0.1", self.port), self._make_handler())
        self._thread = Thread(target=self._server.serve_forever, daemon=True)

    @staticmethod
    def _get_free_port() -> int:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(("127.0.0.1", 0))
            return int(sock.getsockname()[1])

    @staticmethod
    def _clock_payload() -> ClockPayload:
        now = datetime.now()
        date_text = f"{now.year}년 {now.month}월 {now.day}일 {WEEKDAYS[now.weekday()]}"
        return {
            "time": now.strftime("%H:%M:%S"),
            "date": date_text,
        }

    def _make_handler(self) -> type[SimpleHTTPRequestHandler]:
        frontend_dir = self.frontend_dir

        class Handler(SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=str(frontend_dir), **kwargs)

            def _send_json(self, payload: ClockPayload) -> None:
                body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def do_GET(self) -> None:
                path = urlparse(self.path).path
                if path == "/api/clock":
                    self._send_json(ClockApiServer._clock_payload())
                    return

                if path == "/":
                    self.path = "/index.html"
                return super().do_GET()

            def log_message(self, format: str, *args: object) -> None:
                return

        return Handler

    @property
    def base_url(self) -> str:
        return f"http://127.0.0.1:{self.port}"

    def start(self) -> None:
        self._thread.start()

    def stop(self) -> None:
        self._server.shutdown()
        self._server.server_close()
        self._thread.join(timeout=1)
