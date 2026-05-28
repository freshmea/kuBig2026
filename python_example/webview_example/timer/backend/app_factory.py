from pathlib import Path

from backend.routes.api import api_bp
from backend.routes.frontend import frontend_bp
from flask import Flask


def create_app(frontend_dir):
    resolved_frontend_dir = Path(frontend_dir).resolve()
    index_file = resolved_frontend_dir / "index.html"
    if not index_file.is_file():
        raise FileNotFoundError(
            f"Frontend entry file not found: {index_file}"
        )

    app = Flask(__name__)
    app.config["FRONTEND_DIR"] = resolved_frontend_dir
    app.config["INDEX_FILE"] = index_file

    app.register_blueprint(api_bp)
    app.register_blueprint(frontend_bp)
    return app
