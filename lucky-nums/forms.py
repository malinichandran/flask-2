"""Form for lucky-nums"""

from flask_wtf import FlaskForm
from wtforms import StringField ,IntegerField, SelectField
from wtforms.validators import InputRequired, Email, NumberRange


class LuckyNumForm(FlaskForm):
    """Form for lucky-nums"""

    name = StringField(
        "User Name",
        validators=[InputRequired()])

    email = StringField(
        "Email Address",
        validators=[InputRequired(), Email()])

    birth_year = IntegerField(
        "Birth Year",
        validators=[NumberRange(
            min=1900,
            max=2001
        )])

    color = SelectField(
        "Favorite-Color",
        choices=['red','green','orange','blue'],
        validators=[InputRequired()])
    