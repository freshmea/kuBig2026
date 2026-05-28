from backend.services.clock_service import get_clock_payload
from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.get("/clock")
def get_clock():
    return jsonify(get_clock_payload())
