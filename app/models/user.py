from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    first_name = db.Column(db.String(40), nullable=False, unique=True)
    last_name = db.Column(db.String(40), nullable=False, unique=True)
    bio = db.Column(db.String(40), unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    ## User has a one to MANY relationship with playlists, albums, album_likes, songs, song_likes

    playlist = db.relationship('Playlists', back_populates='playlist_user', cascade='all, delete-orphan')
    songs = db.relationship('Songs', back_populates='song_users', cascade='all, delete-orphan')
    song_likes = db.relationship('SongLikes', back_populates='song_likes_users', cascade='all, delete-orphan')
    albums = db.relationship('Albums', back_populates='album_users', cascade='all, delete-orphan')
    album_likes = db.relationship('AlbumLikes', back_populates='album_likes_user', cascade='all, delete-orphan')


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'bio': self.bio,
            'email': self.email,
            'password': self.password
        }
