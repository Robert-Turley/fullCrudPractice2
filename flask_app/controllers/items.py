from flask_app import app
from flask import render_template

@app.route('/')
def login():
    return render_template('login.html')