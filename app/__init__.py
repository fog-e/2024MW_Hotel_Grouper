from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        hotels = request.form.getlist('hotel')  # Get list of selected hotels
        dates = request.form.getlist('date')    # Get list of selected dates
        # Process additional fields similarly
        # Save data, send email, or process further as needed
        return redirect('/thank_you')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
