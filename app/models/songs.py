from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Songs(db.Model):
    __tablename__ = "songs"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('albums.id')), nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('playlists.id')), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    lyrics = db.Column(db.String(5000), nullable=False)

    liker =

    def to_dict(self):
        return {
            "id": self.id,
            "album_id": self.album_id,
            "playlist_id": self.playlist_id,
            "title": self.title,
            "lyrics": self.lyrics
        }