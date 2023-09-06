from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Albums(db.Model):
    __tablename__ = "albums"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    # Do users create the albums? Check your features list and see how I set it
    album_id = db.Column(db.Integer, db.ForeignKey(add_prefox_for_prod('users.id')), nullable=False)
    album_photo = db.Column(db.String)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullabe=False)

    #Albums has a one to MANY relationship with album_likes
    likes = db.Relationship('AlbumLikes', back_populates='album')


    def to_dict(self):
        return {
            "id": self.id,
            "album_photo": self.album_photo,
            "title": self.title,
            "year": self.year,
            "date_created": self.date_created
        }