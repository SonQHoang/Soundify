from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, SelectField, StringField, DateField
from wtforms.validators import DataRequired, Length
from ..routes.AWS_helpers import ALLOWED_EXTENSIONS

class AddSongToPlaylist (FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    image = FileField("Adjust Your Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    playlist_description = StringField("Description")