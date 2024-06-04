from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

def read_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data

@app.route('/')
def index():
    dates = read_csv('dates.csv')[1:]  # Skip header
    hotels = read_csv('hotels.csv')[1:]  # Skip header
    hotel_popularity = calculate_popularity()
    return render_template('index.html', dates=dates, hotels=hotels, hotel_popularity=hotel_popularity)

def calculate_popularity():
    popularity = {}
    try:
        with open('responses.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                hotels = row['hotels'].split('|')
                for hotel in hotels:
                    if hotel in popularity:
                        popularity[hotel] += 1
                    else:
                        popularity[hotel] = 1
    except FileNotFoundError:
        pass
    return popularity

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    notes = request.form['notes']
    selected_hotels = request.form.getlist('hotels')
    selected_dates = request.form.getlist('dates')
    date_notes = request.form.getlist('date_notes')

    with open('responses.csv', 'a', newline='') as csvfile:
        fieldnames = ['name', 'email', 'notes', 'hotels', 'dates', 'date_notes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'name': name,
            'email': email,
            'notes': notes,
            'hotels': '|'.join(selected_hotels),
            'dates': '|'.join(selected_dates),
            'date_notes': '|'.join(date_notes)
        })

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000)
