from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, SelectField, StringField, DateField
from wtforms.validators import DataRequired
from ..routes.AWS_helpers import ALLOWED_EXTENSIONS

class CreatePlaylistForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    image = FileField("Playlist Image", validators=[FileAllowed(ALLOWED_EXTENSIONS)])
    date_created = DateField("Date Created", validators=[DataRequired()])
    playlist_description = StringField("Description")
    submit = SubmitField("Create Post") 