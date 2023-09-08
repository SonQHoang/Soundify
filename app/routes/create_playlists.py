# from flask import Blueprint, request, jsonify, request
# from app.models.db import db
# from app.models import Playlists
# from datetime import date
# from ..forms.create_playlist_form import CreatePlaylistForm
# from .AWS_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3

# playlists = Blueprint("playlists", __name__)

# @playlists.route("/<int:id", methods=["GET"])
# def get_playlists():
#     pass

# @playlists.route("/new", methods="POST")
# def create_playlists():
#     form = CreatePlaylistForm
#     form['csrf_token'].data = request.cookies['csrf_token']

#     if form.validate_on_submit():
#         audio_file = form.data["audio"]
#         audio_file.filename = get_unique_filename(audio_file.filename)
#         upload = upload_file_to_s3(audio_file)

#         if "url" in upload:
#             new_playlist = Playlists(
#                 name= form.data["name"],
#                 audio_url = upload["url"]
#             )

#         db.session.add(new_playlist)
#         db.session.commit()

#         return jsonify({"message": "Playlist created!"})
#     else:
#         return jsonify({"error": "File upload failed."}), 400
    

# @playlists.route("/update", methods="PUT")
# def update_playlists():
#     return jsonify({"message": "Update successful"})

# @playlists.route("/delete", methods=["DELETE"])
# def delete_playlists():
#     return jsonify({"message": "Deletion successful"})