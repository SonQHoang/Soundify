from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Songs(db.Model):
    __tablename__ = "songs"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('albums.id')), nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('playlists.id')), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    lyrics = db.Column(db.String(5000), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    #Songs has a MANY to one relationship with albums, users, playlist

    song_users = db.relationship('Users', back_populates="songs")
    song_albums = db.relationship('Albums', back_populates='album_songs')
    song_playlists = db.relationship('Playlists', back_populates='playlist_songs')

    # Songs has a one to many relationship with song_likes
    song_song_likes = db.relationship('SongLikes', back_populates="song_likes_songs", cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "album_id": self.album_id,
            "playlist_id": self.playlist_id,
            "title": self.title,
            "lyrics": self.lyrics,
            "date_created": self.date_created,
            "song_song_likes": self.song_song_likes.to_dict()
        }