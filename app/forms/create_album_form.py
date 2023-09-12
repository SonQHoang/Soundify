from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, SelectField, StringField, DateField, IntegerField
from wtforms.validators import DataRequired, Length
from ..routes.AWS_helpers import ALLOWED_EXTENSIONS

class CreateAlbumForm(FlaskForm):
    album_photo = FileField("Album Photo", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    title = StringField("Title", validators=[DataRequired()])
    year = IntegerField("Year", validators=[DataRequired()])
    date_created = DateField("Date Created", validators=[DataRequired()])
    album_description = StringField("Description")
    submit = SubmitField("Create Post") 