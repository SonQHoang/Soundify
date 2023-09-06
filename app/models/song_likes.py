from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

class SongLikes(db.Model):
    __tablename__ = "song_likes"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('songs.id')), nullable=False) 
    date_created = db.Column(db.DateTime, nullable=False)

    #SongLikes has a MANY to one relationship with users, and songs

    song_likes_songs = db.relationship('Songs', back_populates="song_song_likes")
    song_likes_users = db.relationship('Users', back_populates="song_likes")
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "song_id": self.song_id,
            "date_created": self.date_created,
            "song_likes_songs": self.song_likes_songs.to_dict(),
            "song_likes_users": self.song_likes_users.to_dict()
        }