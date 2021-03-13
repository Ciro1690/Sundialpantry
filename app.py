from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message
from forms import ContactForm
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'abc123')

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sundialpantry@gmail.com'  # enter your email here
app.config['MAIL_PASSWORD'] = os.environ.get('SECRET_KEY', 'abc123') # enter your password here

mail = Mail(app)
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/photo-album")
def photo_album():
    return render_template("photos.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/farmers-market")
def farmers_market():
    return render_template("farmers-market.html")

@app.route("/special-orders")
def special_orders():
    return render_template("special-orders.html")
    
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/dinner-parties", methods=['GET', 'POST'])
def dinner_parties():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        date = form.date.data
        party_size = form.party_size.data
        occasion = form.occasion.data

        msg = Message(f"Message from {name}", sender=f"{email}", recipients=['sundialpantry@gmail.com'])
        msg.body = f"{date} for party request from {email}, Party size: {party_size}, Occasion - {occasion}"

        mail.send(msg)
        flash("Email sent", "success")
        return redirect('/')
    return render_template("dinner_parties.html", form=form)
