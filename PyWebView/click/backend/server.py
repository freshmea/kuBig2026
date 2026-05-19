import json
import queue
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock, Thread
from urllib import error, request
from urllib.parse import urlparse

COUNTER_PORT = 49321
type CounterPayload = dict[str, int]
type CounterEventQueue = queue.Queue[CounterPayload]


class CounterHttpServer(ThreadingHTTPServer):
    daemon_threads = True


class CounterApiServer:
    def __init__(self, frontend_dir: Path) -> None:
        self.frontend_dir = frontend_dir
        self.port = COUNTER_PORT
        self._count = 0
        self._lock = Lock()
        self._event_clients: list[CounterEventQueue] = []
        self._server: ThreadingHTTPServer | None = None
        self._thread: Thread | None = None
        self._owns_server = False

    def _counter_payload(self) -> CounterPayload:
        with self._lock:
            return {"count": self._count}

    def _increase_payload(self) -> CounterPayload:
        with self._lock:
            self._count += 1
            payload = {"count": self._count}
            self._broadcast_counter(payload)
            return payload

    def _decrease_payload(self) -> CounterPayload:
        with self._lock:
            self._count -= 1
            payload = {"count": self._count}
            self._broadcast_counter(payload)
            return payload

    def _add_event_client(self) -> CounterEventQueue:
        client_queue: CounterEventQueue = queue.Queue()
        with self._lock:
            self._event_clients.append(client_queue)
            client_queue.put({"count": self._count})
        return client_queue

    def _remove_event_client(self, client_queue: CounterEventQueue) -> None:
        with self._lock:
            if client_queue in self._event_clients:
                self._event_clients.remove(client_queue)

    def _broadcast_counter(self, payload: CounterPayload) -> None:
        for client_queue in list(self._event_clients):
            client_queue.put(payload)

    def _make_handler(self) -> type[SimpleHTTPRequestHandler]:
        frontend_dir = self.frontend_dir
        app_server = self

        class Handler(SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=str(frontend_dir), **kwargs)

            def _send_json(self, payload: CounterPayload) -> None:
                body = json.dumps(payload).encode("utf-8")
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def _send_event(self, payload: CounterPayload) -> None:
                body = f"data: {json.dumps(payload)}\n\n".encode("utf-8")
                self.wfile.write(body)
                self.wfile.flush()

            def _stream_counter_events(self) -> None:
                client_queue = app_server._add_event_client()
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Connection", "keep-alive")
                self.end_headers()

                try:
                    while True:
                        payload = client_queue.get()
                        self._send_event(payload)
                except (ConnectionError, BrokenPipeError, OSError):
                    return
                finally:
                    app_server._remove_event_client(client_queue)

            def do_GET(self) -> None:
                path = urlparse(self.path).path
                if path == "/api/counter/events":
                    self._stream_counter_events()
                    return

                if path == "/api/counter":
                    self._send_json(app_server._counter_payload())
                    return

                if path == "/":
                    self.path = "/index.html"
                return super().do_GET()

            def do_POST(self) -> None:
                path = urlparse(self.path).path
                if path == "/api/counter/increase":
                    self._send_json(app_server._increase_payload())
                    return

                if path == "/api/counter/decrease":
                    self._send_json(app_server._decrease_payload())
                    return

                self.send_error(HTTPStatus.NOT_FOUND)

            def log_message(self, format: str, *args: object) -> None:
                return

        return Handler

    @property
    def base_url(self) -> str:
        return f"http://127.0.0.1:{self.port}"

    def _existing_server_is_ready(self) -> bool:
        try:
            with request.urlopen(f"{self.base_url}/api/counter", timeout=1) as response:
                return response.status == HTTPStatus.OK
        except (OSError, error.URLError):
            return False

    def start(self) -> None:
        if self._existing_server_is_ready():
            return

        try:
            self._server = CounterHttpServer(("127.0.0.1", self.port), self._make_handler())
        except OSError as exc:
            if exc.errno in {10048, 98} and self._existing_server_is_ready():
                return
            raise

        self._thread = Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()
        self._owns_server = True

    def stop(self) -> None:
        if not self._owns_server or self._server is None or self._thread is None:
            return

        self._server.shutdown()
        self._server.server_close()
        self._thread.join(timeout=1)
