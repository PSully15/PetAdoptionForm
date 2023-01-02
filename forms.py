from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[
        ("cat", 'Cat'),
        ("dog", 'Dog'),
        ("porkupine", 'Porkupine')
    ])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])


class EditPetForm(FlaskForm):
    """Form for editing a pet."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")
