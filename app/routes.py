from flask import Blueprint, render_template, request, redirect, url_for
import csv
import pandas as pd
import matplotlib.pyplot as plt

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
    
    generate_bar_graph()
    return redirect(url_for('main.index'))

def generate_bar_graph():
    df = pd.read_csv('responses.csv', names=['name', 'email', 'notes', 'hotels', 'dates'])
    hotel_counts = df['hotels'].apply(eval).explode().value_counts()
    
    plt.figure(figsize=(10, 6))
    hotel_counts.plot(kind='bar', color='skyblue')
    plt.title('Hotel Popularity')
    plt.xlabel('Hotels')
    plt.ylabel('Number of Bookings')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('app/static/hotel_popularity.png')
    plt.close()
