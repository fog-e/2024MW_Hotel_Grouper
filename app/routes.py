from flask import Blueprint, render_template, request, redirect, url_for
import csv
import pandas as pd

main = Blueprint('main', __name__)

@main.route('/')
def index():
    hotel_popularity = calculate_hotel_popularity()
    return render_template('index.html', hotel_popularity=hotel_popularity)

@main.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    notes = request.form.get('notes')
    hotels = request.form.getlist('hotels')
    other_hotels = request.form.getlist('other_hotels[]')
    dates = request.form.getlist('dates')
    date_notes = request.form.getlist('date_notes[]')

    # Combine hotels and other_hotels
    hotels.extend(other_hotels)

    with open('responses.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email, notes, hotels, dates, date_notes])
    
    return redirect(url_for('main.index'))

def calculate_hotel_popularity():
    try:
        df = pd.read_csv('responses.csv', names=['name', 'email', 'notes', 'hotels', 'dates', 'date_notes'])
        hotel_counts = df['hotels'].apply(eval).explode().value_counts().to_dict()
        return hotel_counts
    except FileNotFoundError:
        return {}

