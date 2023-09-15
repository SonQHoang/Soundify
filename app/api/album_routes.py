from flask import Blueprint, request, jsonify, request
from flask_login import login_required, current_user
from app.models.db import db
from app.models import Albums, User
from datetime import datetime
from ..forms.create_album_form import CreateAlbumForm
from ..forms.update_album_form import UpdateAlbumForm
from ..routes.AWS_helpers import get_unique_filename, upload_file_to_s3, remove_file_from_s3

album_routes = Blueprint('album', __name__)
session = db.session

# def validation_errors_to_error_messages(validation_errors):

#     errorMessages = []
#     for field in validation_errors:
#         for error in validation_errors[field]:
#             errorMessages.append(f'A album {field} is required')
#     return errorMessages

@album_routes.route('/user_album', methods=["GET"])
def get_user_album():
    albums = Albums.query.filter_by(user_id = current_user.id).all()
    # print('albums=====>', albums)
    return [album.to_dict() for album in albums]

@album_routes.route("/all", methods=["GET"])
def get_all_albums():
    all_albums = Albums.query.all()
    # print('all_albums=======>', all_albums)
    return [album.to_dict() for album in all_albums]

@album_routes.route("/new", methods=["POST"])
def create_albums():
    user = User.query.get(current_user.id)
    form = CreateAlbumForm() 
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():

        image = form.data['image']
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        
        url = upload['url']

        new_album = Albums(
            user_id=user.id,
            title=form.data,
            owner = current_user.first_name,
            album_description=form.album_description.data,
            album_photo = form.album_photo.data,
            year = form.year.data,
            image = url,
            date_created=datetime.utcnow(),
        )

        # print('new_album========>', new_album)
        db.session.add(new_album)
        db.session.commit()
        # print('respost =======>', {new_album.to_dict()})
        return {"resPost": new_album.to_dict()}
        # return jsonify({"message": "Album created!"})
    else:
        print('Validation Errors:', form.errors)
        return jsonify({"error": "File upload failed."}), 400
    
    
@album_routes.route("/add", methods=["POST"])
def add_song_to_album():
    data = request.get_json()
    return jsonify(data)

@album_routes.route("/<int:albumId>")
def get_single_album_by_id(albumId):
    album = Albums.query.get(albumId)

    if album is None:
        return jsonify({"error": "Album not found"}), 404
    
    album_data = {
        "id": album.id,
        "title": album.title,
        "owner": album.owner,
        "album_description": album.album_description,
        "date_created": datetime.utcnow(),
    }

    if hasattr(album, "songs"):
        album_data["songs"] = [song.to_dict() for song in album.songs]
    return jsonify(album_data)

#1
# @album_routes.route("/update/<int:albumId>", methods=["PUT"])
# def update_albums(albumId):
#     current_album = Albums.query.get(albumId)
#     print('current_album===========>', current_album)

#     form = UpdateAlbumForm()
#     print('form==============>', form)
#     form['csrf_token'].data = request.cookies['csrf_token']

#     if form.validate_on_submit():
#         if current_user.id != current_album.user_id:
#             error = {"message": "You shouldn't be trying to adjust someone else's album..."}
#             return jsonify(error), 403
        
#         current_album.title = request.json['title']
#         print('current_album.title==============>', current_album)
#         current_album.album_photo = request.json['album_photo']
#         current_album.album_description = request.json['album_description']
        
#         updated_album = current_album
#         updated_album_dict = updated_album.to_dict()
#         db.session.commit()
#         return updated_album_dict
#     return jsonify(current_album.to_dict())

2
@album_routes.route('/update/<int:albumId>', methods=['PUT'])
def update_album(albumId):
    form = UpdateAlbumForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    print('form.data=======>', form.data)

    if form.validate_on_submit():
        current_album = Albums.query.get(albumId)
        current_album.title = form.title.data
        current_album.album_photo = form.album_photo.data
        current_album.year = form.year.data
        current_album.album_description = form.album_description.data

        db.session.commit()
        return current_album.to_dict()
    return jsonify({"errors": form.errors}), 400
    
    
@album_routes.route("/delete/<int:albumId>", methods=["DELETE"])
def delete_albums(albumId):
    album_to_delete = Albums.query.get(albumId)
    db.session.delete(album_to_delete)
    db.session.commit()
    return jsonify({"message": "Deletion successful"})