from flask_app import app
from flask import render_template, redirect, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

bcrypt = Bcrypt()

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/register', methods = ['POST'])
def register():
    # print(request.form)
    if request.form['password'] != request.form['confirm_password']:
        flash("Passwords do not match!")
        return redirect('/')

    hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hash
    }
    print(data)
    User.create(data)
    return redirect('/')

@app.route('/login', methods = ['POST'])
def login():
    # print(request.form)

    return redirect('/')