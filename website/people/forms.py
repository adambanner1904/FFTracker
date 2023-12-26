from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


class NewPlayerForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")
