from . import app, db
from flask import render_template, request, redirect, url_for
from .models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    hotel_choice = request.form['hotel_choice']
    date = request.form['date']
    
    user = User(name=name, email=email, hotel_choice=hotel_choice, date=date)
    db.session.add(user)
    db.session.commit()
    
    return redirect(url_for('index'))
