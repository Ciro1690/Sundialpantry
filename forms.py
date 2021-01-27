from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import DateField


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    date = DateField("Date", validators=[InputRequired()], format='%Y-%m-%d')
    party_size = IntegerField("Party Size", validators=[InputRequired()])
    occasion = StringField("Occasion")
