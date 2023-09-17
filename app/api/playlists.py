from flask import Blueprint, request, jsonify, request
from flask_login import login_required, current_user
from app.models.db import db
from app.models import Playlists, User, Songs, Albums
from datetime import datetime
from ..forms.create_playlist_form import CreatePlaylistForm
from ..forms.update_playlist_form import UpdatePlaylistForm
from ..routes.AWS_helpers import get_unique_filename, upload_file_to_s3, remove_file_from_s3

playlist_routes = Blueprint('playlist', __name__)
session = db.session

@playlist_routes.route('/user_playlist', methods=["GET"])
def get_user_playlist():
    playlists = Playlists.query.filter_by(user_id = current_user.id).all()
    # print('playlists=====>', playlists)
    return [playlist.to_dict() for playlist in playlists]

@playlist_routes.route("/all", methods=["GET"])
def get_all_playlists():
    all_playlists = Playlists.query.all()
    # print('all_playlists=======>', all_playlists)
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
    
    
#1
# @playlist_routes.route("/add", methods=["POST"])
# def add_song_to_playlist():
#     data = request.get_json()
#     return jsonify(data)

#2
@playlist_routes.route("/<int:playlistId>/add", methods=["POST"])
def add_song_to_playlist(playlistId):

    data = request.json
    song_id = data['id']

    playlist = Playlists.query.get(playlistId)

    if not playlist:
        return jsonify({"error": "Playlist not found"}), 404

    new_songs = Songs.query.get(song_id)

    if not new_songs:
        return jsonify({"error": "Song not found"}), 404
    
    playlist.playlist_songs.append(new_songs)

    db.session.add(playlist)
    db.session.commit()

    return jsonify(new_songs.to_dict())

# #3 
@playlist_routes.route("/<int:playlistId>/songs", methods=["GET"])
def get_songs_for_playlist(playlistId):
    # print('playlist_id backend============>', playlistId)
    # Getting the plalyist in question with playlistId
    playlist = Playlists.query.get(playlistId)
    # print('current_playlist backend========>', playlist)

    # Getting access to the playlist_songs table
    playlist_songs = playlist.playlist_songs
    # print('playlist_songs backend==========>', playlist_songs)
    # return playlist_songs
    # return {playlist_songs: [playlist_song.to_dict() for playlist_song in playlist_songs]

    song_container = []

    for playlist_song in playlist_songs:
        # print(playlist_song)
        song_to_dict = playlist_song.to_dict()
        # print(playlist_song)
        song_container.append(song_to_dict)
        # print(playlist_song)
        
    # print('song_container_out of for loop----------->', song_container)
    return song_container

    # playlist_info = []

    # for playlist_song in playlist_songs:
    #     print('Playlist Song: ========>', playlist_song)
    #     song = playlist_song.song_playlists
    #     print('Song ===$$=====>:', song)
    #     print('Song ===$$=====>:', song.songs_album)

    #     album = song.song_albums
    #     print('album=============>', album)
    #     if album:
    #         song_info = {
    #             "song_id": song.id,
    #             "song_title": song.title,
    #             "album_id": album.id,
    #             "album_title": album.title  # Include album title if available
    #         }
    #         playlist_info.append(song_info)
    #     playlist_info.append(song_info)
    # print('playlist_info backend=======>', playlist_info)

    # return jsonify(playlist_info), 200


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
        "playlist_description": playlist.playlist_description,
        # "playlist_songs": [song.to_dict() for song in playlist.songs],
        "date_created": datetime.utcnow(),
    }

    if hasattr(playlist, "songs"):
        playlist_data["songs"] = [song.to_dict() for song in playlist.songs]
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
    playlist_to_delete = Playlists.query.get(playlistId)
    db.session.delete(playlist_to_delete)
    db.session.commit()
    return jsonify({"message": "Deletion successful"})