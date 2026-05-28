from flask import Blueprint, current_app, send_from_directory

frontend_bp = Blueprint("frontend", __name__)


@frontend_bp.get("/")
def serve_index():
    frontend_dir = current_app.config["FRONTEND_DIR"]
    index_file = current_app.config["INDEX_FILE"]
    return send_from_directory(frontend_dir, index_file.name)


@frontend_bp.get("/<path:file_path>")
def serve_asset(file_path):
    frontend_dir = current_app.config["FRONTEND_DIR"]
    return send_from_directory(frontend_dir, file_path)
