import socket
import time
from datetime import datetime
from pathlib import Path
from threading import Thread

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from uvicorn import Config, Server

WEEKDAYS = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]


def getClockPayload():
    now = datetime.now()
    date_text = (
        f"{now.year}년 {now.month}월 {now.day}일 "
        f"{WEEKDAYS[now.weekday()]}"
    )
    return {
        "time": now.strftime("%H:%M:%S"),
        "date": date_text,
    }


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
        self.app = FastAPI()
        self._configure_routes()

        config = Config(
            app=self.app,
            host="127.0.0.1",
            port=self.port,
            log_level="warning",
        )
        self._server = Server(config)
        self._thread = Thread(target=self._server.run, daemon=True)

    def _configure_routes(self):
        self.app.add_api_route("/", self._serve_index, methods=["GET"])
        self.app.add_api_route(
            "/api/clock",
            self._serve_clock,
            methods=["GET"],
        )
        self.app.add_api_route(
            "/{file_path:path}",
            self._serve_asset,
            methods=["GET"],
        )

    def _serve_index(self):
        return FileResponse(self.index_file)

    def _serve_clock(self):
        return getClockPayload()

    def _serve_asset(self, file_path: str):
        asset_path = (self.frontend_dir / file_path).resolve()
        try:
            asset_path.relative_to(self.frontend_dir)
        except ValueError as error:
            raise HTTPException(status_code=404) from error

        if not asset_path.is_file():
            raise HTTPException(status_code=404)

        return FileResponse(asset_path)

    @property
    def base_url(self):
        return f"http://127.0.0.1:{self.port}"

    def start(self):
        self._thread.start()
        for _ in range(100):
            if self._server.started:
                return
            time.sleep(0.01)
        raise RuntimeError("FastAPI server did not start in time")

    def stop(self):
        self._server.should_exit = True
        self._thread.join(timeout=1)
