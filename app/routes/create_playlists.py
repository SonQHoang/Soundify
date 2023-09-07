from flask import Blueprint, request, jsonify, request
from app.models.db import db
from datetime import date

playlists = Blueprint("playlists", __name__)

@playlists.route("/<int:id", methods=["GET"])
def get_playlists():
    pass

@playlists.route("/new", methods="POST")
def create_playlists():
    return jsonify({"message": "Playlist created!"})

@playlists.route("/update", methods="PUT")
def update_playlists():
    return jsonify({"message": "Update successful"})

@playlists.route("/delete", methods=["DELETE"])
def delete_playlists():
    return jsonify({"message": "Deletion successful"})