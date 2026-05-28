import socket
from threading import Thread

from flask import Flask
from werkzeug.serving import make_server


def getFreePort():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


class ClockApiServer:
    def __init__(self, frontend_dir):
        self.port = getFreePort()
        self.app = Flask(__name__, static_folder=str(frontend_dir), static_url_path="")
        self._server = make_server("127.0.0.1", self.port, self.app)
        self._thread = Thread(target=self._server.serve_forever, daemon=True)
        self.app.add_url_rule("/", "index", lambda: self.app.send_static_file("index.html"))

    def start(self):
        self._thread.start()