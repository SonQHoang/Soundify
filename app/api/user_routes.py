from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import User
from app.models.db import db

user_routes = Blueprint('users', __name__, url_prefix="")


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/demo-user-profile', methods=["POST"])
@login_required
def populate_user_profile():

    # print('user======= backend', current_user)
    demo_user = User.query.filter_by(username='Demo').first()
    print('demo_user backend===>', demo_user)
    # if demo_user:
    #     current_user.playlists = demo_user.playlists
    #     current_user.albums = demo_user.albums
    #     db.session.commit()

    #     demo_data = {
    #         "message": "Demo data populated successfully",
    #         "user_playlists": [playlist.to_dict() for playlist in current_user.playlists],
    #         "user_albums": [album.to_dict() for album in current_user.albums],
    #     }

    #     return jsonify(demo_data), 200
