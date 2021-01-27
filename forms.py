from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import DateField
from wtforms.fields import html5 as h5fields
from wtforms.widgets import html5 as h5widgets

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    date = DateField("Date", validators=[InputRequired()], format='%Y-%m-%d')
    party_size = h5fields.IntegerField("Party Size", validators=[InputRequired()], widget=h5widgets.NumberInput(min=0, max=30))
    occasion = StringField("Occasion")
