"""creating playlist_songs_table_productions

Revision ID: 10a58a93b7cc
Revises: e073d26357e6
Create Date: 2023-09-14 22:11:08.749248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10a58a93b7cc'
down_revision = 'e073d26357e6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('playlist_songs',
        sa.Column('playlist_id', sa.Integer(), nullable=False),
        sa.Column('song_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['playlist_id'], ['playlists.id']),
        sa.ForeignKeyConstraint(['song_id'], ['songs.id']),
    )


def downgrade():
    op.drop_table('playlist_songs')
