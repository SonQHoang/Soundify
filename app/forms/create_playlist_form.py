from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, SelectField, StringField, DateField
from wtforms.validators import DataRequired, Length
from ..routes.AWS_helpers import ALLOWED_EXTENSIONS

class CreatePlaylistForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    # Add image url receiver later for playlist image
    date_created = DateField("Date Created", validators=[DataRequired()])
    # audio = FileField("Audio", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    submit = SubmitField("Create Post")