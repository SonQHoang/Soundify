from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod
from .playlists import songs_playlist_association

class Songs(db.Model):
    __tablename__ = "songs"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('albums.id')), nullable=False)
    audio_url = db.Column(db.String, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    lyrics = db.Column(db.String(5000), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    #Songs has a MANY to MANY relationship with playlist
    song_playlists = db.relationship('Playlists', secondary=songs_playlist_association, back_populates='playlist_songs')

    #Songs has a MANY to one relationship with albums, users, playlist

    song_users = db.relationship('User', back_populates="songs")
    song_albums = db.relationship('Albums', back_populates='album_songs')

    # Songs has a one to many relationship with song_likes
    song_song_likes = db.relationship('SongLikes', back_populates="song_likes_songs", cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "album_id": self.album_id,
            "audio_url": self.audio_url,
            "title": self.title,
            "lyrics": self.lyrics,
            "date_created": self.date_created,
            # "song_song_likes": [like.to_dict() for like in self.song_song_likes],

            # This will return an array of all of the lists of the different playlists where this song is attached
            # "song_playlists": [song.to_dict() for song in self.song_playlists]
        }
    
# Playlist 1
## song 1 id 

# Playlist 2
## song 1 id

## song1 is associated with Playlist 1 and 2