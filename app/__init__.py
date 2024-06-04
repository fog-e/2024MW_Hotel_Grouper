from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Handle form data here
    name = request.form.get('name')
    email = request.form.get('email')
    # Extract other form data like hotel choices and dates

    # Logic to save data to CSV or display it can be added here

    return redirect(url_for('index'))  # Redirect to home or to a confirmation page

if __name__ == "__main__":
    app.run(debug=True)
