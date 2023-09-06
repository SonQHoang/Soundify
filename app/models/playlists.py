from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Playlists(db.Model):
    __tablename__ = "playlists"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('')), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('')), nullable=False)
    title = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    user = db.Relationship('User', back_populates='playlist')
    song = db.Relationship('Song', back_populates='')
    likes = db.Relationship('SongLikes', back_populates="")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "song_id": self.song_id,
            "title": self.title,
            "date_created": self.date_created
        }
