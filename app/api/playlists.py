from flask import Blueprint, request, jsonify, request
from flask_login import login_required, current_user
from app.models.db import db
from app.models import Playlists, User
from datetime import datetime
from ..forms.create_playlist_form import CreatePlaylistForm
from ..routes.AWS_helpers import get_unique_filename, upload_file_to_s3, remove_file_from_s3

playlist_routes = Blueprint('playlist', __name__)

@playlist_routes.route("/new", methods=["POST"])
def create_playlists():
    user = User.query.get(current_user.id)
    print('user======>', user)
    form = CreatePlaylistForm() 
    # print('form=======>', form)
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        # Commenting out audio-related code
        # audio = form.audio.data
        # print('audio=========>', audio)
        # audio.filename = get_unique_filename(audio.filename)

        # upload = upload_file_to_s3(audio)
        # print('upload=========>', upload)
        # if "url" in upload:
        new_playlist = Playlists(
            user_id=user.id,
            title=form.title.data,
            # audio_url=upload["url"],
            date_created=datetime.utcnow(),
        )
        print('new_playlist========>', new_playlist)
        db.session.add(new_playlist)
        db.session.commit()
        # print('respost =======>', {new_playlist.to_dict()})
        return {"resPost": new_playlist.to_dict()}
        # return jsonify({"message": "Playlist created!"})
    else:
        print('Validation Errors:', form.errors)
        return jsonify({"error": "File upload failed."}), 400
    

@playlist_routes.route("/update", methods=["PUT"])
def update_playlists():
    return jsonify({"message": "Update successful"})

@playlist_routes.route("/delete", methods=["DELETE"])
def delete_playlists():
    return jsonify({"message": "Deletion successful"})