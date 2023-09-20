"""Creating tables

Revision ID: b13fdd8569c5
Revises:
Create Date: 2023-09-11 22:24:36.056196
"""
from alembic import op
import sqlalchemy as sa
import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")
# revision identifiers, used by Alembic.
revision = 'b13fdd8569c5'

down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('audio_url', sa.String(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('lyrics', sa.String(length=5000), nullable=True),
    sa.Column('duration', sa.String(length=5000), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=True),
    sa.Column('album_photo', sa.String(), nullable=True),
    sa.Column('owner', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('album_description', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('playlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=True),
    sa.Column('owner', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('playlist_description', sa.String(length=255), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('song_likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('album_likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('album_songs',
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.Column('song_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], )
    )
    op.create_table('playlist_songs',
    sa.Column('playlist_id', sa.Integer(), nullable=True),
    sa.Column('song_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlists.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], )
    )
    # ### end Alembic commands ###

    if environment == "production":
        op.execute(f"ALTER TABLE  users SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE  albums SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE  album_likes SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE  songs SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE  album_songs SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE  playlists SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE  song_likes SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE  playlist_songs SET SCHEMA {SCHEMA};")

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('playlist_songs')
    op.drop_table('album_songs')
    op.drop_table('album_likes')
    op.drop_table('song_likes')
    op.drop_table('playlists')
    op.drop_table('albums')
    op.drop_table('songs')
    op.drop_table('users')
    # ### end Alembic commands ###
