from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Playlists(db.Model):
    __tablename__ = "playlists"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        


    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    title = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    # Playlist has a MANY to one relationship with user
    playlist_user = db.relationship('User', back_populates='playlist')

    # Playlist has a one to MANY relationship with Songs
    playlist_songs = db.relationship('Songs', back_populates='song_playlists', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "date_created": self.date_created,
            "playlist_songs": self.playlist_songs.to_dict()
        }
