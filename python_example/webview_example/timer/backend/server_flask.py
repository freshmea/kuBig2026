import socket
from threading import Thread

from backend.app_factory import create_app
from werkzeug.serving import make_server


def getFreePort():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


class ClockApiServer:
    def __init__(self, frontend_dir):
        self.port = getFreePort()
        self.app = create_app(frontend_dir)
        self._server = make_server("127.0.0.1", self.port, self.app)
        self._thread = Thread(target=self._server.serve_forever, daemon=True)

    @property
    def base_url(self):
        return f"http://127.0.0.1:{self.port}"

    def start(self):
        self._thread.start()
