from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define a list to store trip details
ledger = []

@app.route('/')
def homepage():
    return render_template('portfolio.html')

@app.route('/education.html')
def page1():
    return render_template('education.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/skills.html')
def skills():
    return render_template('skills.html')

@app.route('/ledger_add.html', methods=['GET', 'POST'])
def ledger_add():
    if request.method == 'POST':
        trip = {
            'place': request.form['place'],
            'trip_start_date': request.form['trip_start_date'],
            'trip_end_date': request.form['trip_end_date'],
            'places_visited': request.form['places_visited'],
            'total_cost': request.form['total_cost'],
        }
        ledger.append(trip)  # Append to the "ledger" list
        # Redirect to ledger_view route after adding trip
        #return redirect(url_for('ledger_view'))
    return render_template('ledger_add.html')



@app.route('/ledger_view.html')
def ledger_view():
    return render_template('ledger_view.html', trips=ledger)  # Pass trips stored in the ledger list to the template

if __name__ == '__main__':
    app.run(debug=True)