from flask import Blueprint, request
from app.models import Playlists
from datetime import datetime

playlist_routes = Blueprint('playlists', __name__)

@playlist_routes.route('/all', methods=["GET"])
def get_playlist():
    pass

