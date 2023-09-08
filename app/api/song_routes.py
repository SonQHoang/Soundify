from flask import Blueprint, request, jsonify, request
from flask_login import login_required, current_user
from app.models.db import db
from app.models import Songs, User
from datetime import datetime
from ..routes.AWS_helpers import get_unique_filename, upload_file_to_s3, remove_file_from_s3

song_routes = Blueprint('song', __name__)
session = db.session

@song_routes.route("/all", methods=["GET"])
def get_all_songs():
    all_songs = Songs.query.all()
    print('all_songs============>', all_songs)
    return [songs.to_dict() for songs in all_songs]

@song_routes.route("/new", methods=["POST"])
def create_song():
    pass

@song_routes.route("/update", methods=["PUT"])
def update_songs():
    pass

@song_routes.route("/delete", methods=["DELETE"])
def delete_songs():
    pass