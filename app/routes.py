from flask import Blueprint, render_template, request, redirect, url_for
import csv

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    notes = request.form.get('notes')
    hotels = request.form.getlist('hotels')
    dates = request.form.getlist('dates')

    with open('responses.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email, notes, hotels, dates])
    
    return redirect(url_for('main.index'))
