"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from NadavS_sPhotoAlbum import app
# from flask_wtf import FlaskForm
# from wtfform import StringField, SubmitField
# from wtform.validators import DataRequired 

app.config['SECRET_KEY'] = 'The first argument to the field'

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/Photos')
def Photos():
    """Renders the photos page."""
    return render_template(
        'Photos.html',
        title='Photos',
        year=datetime.now().year,
        message='This is my photo album'

    )
@app.route('/Query')
def Query():
    """Renders the photos page."""
    return render_template(
        'Query.html',
        title='Query',
        year=datetime.now().year,
        message='This is my photo album'
        )

# class ShootingsForm(FlaskForm):
   # Name: 
