from flask_app import app
from flask import render_template

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/new_item')
def create_one():
    return render_template('create_item.html')

@app.route('/edit_item')
def edit_one():
    return render_template('edit_item.html')

@app.route('/details/<int:id>')
def view_one(id):
    return render_template('item_info.html')