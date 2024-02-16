from flask import Blueprint, request, jsonify, request
from flask_login import login_required, current_user
from app.models.db import db
import traceback
from app.models import Playlists, User, Songs, Albums
from datetime import datetime
from ..forms.create_playlist_form import CreatePlaylistForm
from ..forms.update_playlist_form import UpdatePlaylistForm
from ..routes.AWS_helpers import get_unique_filename, upload_file_to_s3, remove_file_from_s3

playlist_routes = Blueprint('playlist', __name__)
session = db.session

@playlist_routes.route('/user_playlist', methods=["GET"])
def get_user_playlist():
    playlists = Playlists.query.all()
    return [playlist.to_dict() for playlist in playlists]

@playlist_routes.route("/all", methods=["GET"])
def get_all_playlists():
    all_playlists = Playlists.query.all()
    return [playlist.to_dict() for playlist in all_playlists]

@playlist_routes.route("/new", methods=["POST"])
def create_playlists():
    user = User.query.get(current_user.id)
    form = CreatePlaylistForm() 
    form['csrf_token'].data = request.cookies['csrf_token']


    if form.validate_on_submit():

        image = form.data['image']
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)

        url = upload['url']

        new_playlist = Playlists(
            user_id=user.id,
            title=form.data['title'],
            owner = current_user.first_name,
            playlist_description=form.data['playlist_description'],
            image = url,
            date_created=datetime.utcnow(),
        )

        db.session.add(new_playlist)
        db.session.commit()
        return {"resPost": new_playlist.to_dict()}
    else:
        print('Validation Errors:', form.errors)
        return jsonify({"error": "File upload failed."}), 400
    
@playlist_routes.route("/<int:playlistId>/add", methods=["POST"])
def add_song_to_playlist(playlistId): 
    #Capturing playlistId

    data = request.json
    song_id = data['id']

    playlist = Playlists.query.get(playlistId)

    if not playlist: 
        return jsonify({"error": "Playlist not found"}), 404

    new_songs = Songs.query.get(song_id) #searching for song being added based on song_id

    if not new_songs:
        return jsonify({"error": "Song not found"}), 404
    
    playlist.playlist_songs.append(new_songs) #Add to playlist

    db.session.add(playlist) #Stage
    db.session.commit() #Commit

    return jsonify(new_songs.to_dict()) 
        # returns songs in JSON format for JS to read

@playlist_routes.route("/<int:playlistId>/songs", methods=["GET"])
def get_songs_for_playlist(playlistId):
    playlist = Playlists.query.get(playlistId)
    playlist_songs = playlist.playlist_songs

    song_container = []

    for playlist_song in playlist_songs:
        song_to_dict = playlist_song.to_dict()
        song_container.append(song_to_dict)
        
    return song_container

@playlist_routes.route("/<int:playlistId>")
def get_single_playlist_by_id(playlistId):
    playlist = Playlists.query.get(playlistId)

    if playlist is None:
        return jsonify({"error": "Playlist not found"}), 404
    
    playlist_data = {
        "id": playlist.id,
        "song_id": playlist.song_id,
        "title": playlist.title,
        "image": playlist.image,
        "owner": playlist.owner,
        "songs": [song.to_dict() for song in playlist.playlist_songs],
        "playlist_description": playlist.playlist_description,
        "date_created": datetime.utcnow(),
    }

    if hasattr(playlist, "playlist_songs"): 
        playlist_data["songs"] = [song.to_dict() for song in playlist.playlist_songs]

    return jsonify(playlist_data)

@playlist_routes.route("/update/<int:playlistId>", methods=["PUT"])
def update_playlists(playlistId):
    current_playlist = Playlists.query.get(playlistId)

    form = UpdatePlaylistForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        if current_user.id != current_playlist.user_id:
            error = {}
            error.message = "You shouldn't be trying to adjust someone else's playlist..."
            return jsonify(error), 403
            
        current_playlist.title = request.json['title']
        current_playlist.image = request.json['image']
        current_playlist.playlist_description = request.json['playlist_description']
        updated_playlist = current_playlist
        updated_playlist_dict = updated_playlist.to_dict()
        db.session.commit()
        return updated_playlist_dict
    return jsonify(current_playlist.to_dict())

@playlist_routes.route("/delete/<int:playlistId>", methods=["DELETE"])
def delete_playlists(playlistId):
    # print('We have hit the backend route for delete playlist============+>')
    playlist_to_delete = Playlists.query.get(playlistId)
    # print('playlist_to_delete======>', playlist_to_delete)

    try:
        # print("Deleting songs associated with playlist ID:", playlistId)
        # playlist_to_delete.playlist_songs.delete()
        # print('playlist_to_delete INSIDE TRY======>', playlist_to_delete)
        db.session.delete(playlist_to_delete)
        db.session.commit()
        return jsonify({"message": "Playlist and associated songs deleted successfully"})
    except Exception as e:
        print("Error:", e)
        print("Traceback:", traceback.format_exc())
        db.session.rollback()
        return jsonify({"error": "An error occurred while deleting the playlist"}), 500
