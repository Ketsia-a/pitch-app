from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import  Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Hobbies','Hobbies'),('Experiences','Experiences'),('Skills','Skills')],validators=[Required()])
    pitch = TextAreaField('Your Pitch...', validators=[Required()])
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment here',validators=[Required()])
    submit = SubmitField('Comment')
