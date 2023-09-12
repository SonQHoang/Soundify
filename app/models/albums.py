from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Albums(db.Model):
    __tablename__ = "albums"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    album_photo = db.Column(db.String)
    owner = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False, unique=True)
    album_description = db.Column(db.String)
    year = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    #Albums has a one to MANY relationship with album_likes, songs
    album_album_likes = db.relationship('AlbumLikes', back_populates='album_likes_albums', cascade='all, delete-orphan')
    album_songs = db.relationship('Songs', back_populates='song_albums', cascade='all, delete-orphan')
    
    #Albums has a MANY to one relationship with Users
    album_users = db.relationship('User', back_populates='albums')

    def to_dict(self):
        return {
            "id": self.id,
            "album_photo": self.album_photo,
            "title": self.title,
            "year": self.year,
            "album_description": self.album_description,
            "date_created": self.date_created,
            "album_users": self.album_users.to_dict()
        }