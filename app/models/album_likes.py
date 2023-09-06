from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

class AlbumLikes(db.Model):
    __tablename__ = "album_likes"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('albums.id')), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    # AlbumLikes has a MANY to one relationship with albums
    album = db.Relationship("Albums", back_populates='likes')

    def to_dict(self):
        return {
            "id": self.id,
            "album_id": self.album_id,
            "date_created": self.date_created,
            "album": self.album.to_dict()
        }