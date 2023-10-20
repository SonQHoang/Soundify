from flask import Blueprint, request, jsonify, request
from flask_login import login_required, current_user
from app.models.db import db
from app.models import Albums, User, Songs, Albums
from datetime import datetime
from ..forms.create_album_form import CreateAlbumForm
from ..forms.update_album_form import UpdateAlbumForm
from ..routes.AWS_helpers import get_unique_filename, upload_file_to_s3, remove_file_from_s3

album_routes = Blueprint('album', __name__)
session = db.session 

@album_routes.route('/user_album', methods=["GET"])
def get_user_album():
    albums = Albums.query.all()

    return [album.to_dict() for album in albums]

@album_routes.route("/all", methods=["GET"])
def get_all_albums():
    all_albums = Albums.query.all()
    return [album.to_dict() for album in all_albums]

@album_routes.route("/new", methods=["POST"])
def create_albums():
    user = User.query.get(current_user.id)
    form = CreateAlbumForm() 
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():

        album_photo = form.data['album_photo']
        album_photo.filename = get_unique_filename(album_photo.filename)
        upload = upload_file_to_s3(album_photo)
        
        url = upload['url']

        new_album = Albums(
            user_id=user.id,
            title=form.title.data,
            owner = current_user.first_name,
            album_description=form.album_description.data,
            album_photo = url,
            year = form.year.data,
            date_created=datetime.utcnow(),
        )

        db.session.add(new_album)
        db.session.commit()
        return {"resPost": new_album.to_dict()}
    else:
        print('Validation Errors:', form.errors)
        return jsonify({"error": "File upload failed."}), 400
    
     
@album_routes.route("/<int:albumId>/add", methods=["POST"])
def add_song_to_album(albumId):
    data = request.get_json()
    song_id = data['id']

    album = Albums.query.get(albumId)

    if not album:
        return jsonify({"error": "Album not found"}), 404
    
    new_songs = Songs.query.get(song_id)

    if not new_songs:
        return jsonify({"error": "Song not found"}), 404
    
    album.album_songs.append(new_songs)

    db.session.add(album)
    db.session.commit()

    return jsonify(new_songs.to_dict())

@album_routes.route("/<int:albumId>/songs", methods=["GET"])
def get_songs_for_album(albumId):

    album = Albums.query.get(albumId)
    album_songs = album.album_songs

    song_container = []

    for album_song in album_songs:
        song_to_dict = album_song.to_dict()
        song_container.append(song_to_dict)
    return song_container

@album_routes.route("/<int:albumId>")
def get_single_album_by_id(albumId):
    album = Albums.query.get(albumId)

    if album is None:
        return jsonify({"error": "Album not found"}), 404
    
    # album_data = {
    #     "id": album.id,
    #     "title": album.title,
    #     "owner": album.owner,
    #     "album_photo": album.album_photo,
    #     "songs": [song.to_dict() for song in album.album_songs],
    #     "year": album.year,
    #     "album_description": album.album_description,
    #     "date_created": datetime.utcnow(),
    # }

    # if hasattr(album, "songs"):
    #     album_data["songs"] = [song.to_dict() for song in album.songs]
    # return jsonify(album_data)
    return jsonify(album.to_dict())

@album_routes.route('/update/<int:albumId>', methods=['PUT'])
def update_album(albumId):
    form = UpdateAlbumForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        current_album = Albums.query.get(albumId)

        current_album.title = form.title.data
        current_album.year = form.year.data
        current_album.album_description = form.album_description.data

        if 'album_photo' in request.files:
            album_photo = request.files['album_photo']
            if album_photo.filename != '':
                album_photo.filename = get_unique_filename(album_photo.filename)
                upload = upload_file_to_s3(album_photo)
                current_album.album_photo = upload['url']

        db.session.commit()
        return current_album.to_dict()
    return jsonify({"errors": form.errors}), 400
    
    
@album_routes.route("/delete/<int:albumId>", methods=["DELETE"])
def delete_albums(albumId):
    album_to_delete = Albums.query.get(albumId)
    db.session.delete(album_to_delete)
    db.session.commit()
    return jsonify({"message": "Deletion successful"})