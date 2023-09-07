# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileAllowed, FileRequired
# from wtforms import SubmitField, SelectField, StringField
# from wtforms.validators import DataRequired, Length
# from ..routes.AWS_helpers import ALLOWED_EXTENSIONS

# class PostForm(FlaskForm):
#     caption = StringField('Caption', validators=[DataRequired(), Length()])
#     audio = FileField("Audio File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
#     author = SelectField("Post Author", choices=[])
#     submit = SubmitField("Create Post")