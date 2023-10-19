from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

songs_playlist_association = db.Table('playlist_songs',
    db.Column('playlist_id', db.Integer, db.ForeignKey(add_prefix_for_prod('playlists.id'))),
    db.Column('song_id', db.Integer, db.ForeignKey(add_prefix_for_prod('songs.id'))),
)



class Playlists(db.Model):  
    __tablename__ = "playlists"

    if environment == "production":
        songs_playlist_association.schema = SCHEMA

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('songs.id')), nullable=True)
    owner = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    playlist_description = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, nullable=False)

    # Playlist has a MANY to MANY relationship with Songs
    playlist_songs = db.relationship('Songs', secondary=songs_playlist_association, back_populates='song_playlists')

    # Playlist has a MANY to one relationship with user
    playlist_user = db.relationship('User', back_populates='playlist')

    def to_dict(self): 
        return {
            "id": self.id,
            "user_id": self.user_id,
            "song_id": self.song_id,
            "owner": self.owner,
            "playlist_description": self.playlist_description,
            "image": self.image,
            "title": self.title,
            "date_created": self.date_created,
            "songs": [playlist_song.to_dict() for playlist_song in self.playlist_songs]
        }