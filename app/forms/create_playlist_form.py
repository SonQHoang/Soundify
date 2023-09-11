from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, SelectField, StringField, DateField
from wtforms.validators import DataRequired, Length
from ..routes.AWS_helpers import ALLOWED_EXTENSIONS

class CreatePlaylistForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    # Add image url receiver later for playlist image
    image = FileField("Playlist Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    date_created = DateField("Date Created", validators=[DataRequired()])
    playlist_description = StringField("Description")
    submit = SubmitField("Create Post") 