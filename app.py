from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3

app = Flask(__name__, template_folder='templates')

# creation of the database
def db_create(connection=None):
    if connection is None:
        connection = sqlite3.connect("timelogged.db")
    with connection:
        cursor = connection.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS timelogs(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           firstname VARCHAR(20) NOT NULL,
                           lastname VARCHAR(20) NOT NULL,
                           signing BOOLEAN NOT NULL,
                           time DATETIME NOT NULL)""")
        except Exception as e:
            print(f"Error creating table: {e}")

# Time in function
def time_in(data):
    with sqlite3.connect("timelogged.db") as connection:
        cursor = connection.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("""INSERT INTO timelogs(
                       firstname,
                       lastname,
                       signing,
                       time
                    ) VALUES (?, ?, ?, ?)""", (*data, True, current_time,))
        connection.commit()  # Committing data into database

# time out function
def time_out(data):
    with sqlite3.connect("timelogged.db") as connection:
        cursor = connection.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("""INSERT INTO timelogs(
                       firstname,
                       lastname,
                       signing,
                       time
                    ) VALUES (?, ?, ?, ?)""", (*data, False, current_time,))
        connection.commit() # Committing data into database

# Route definitions
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']

        time_in((firstname, lastname))

        return redirect(url_for('dashboard'))

    return render_template('signin.html')

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    if request.method == 'POST':
        try:
            firstname = request.form['firstname']
            lastname = request.form['lastname']

            time_out((firstname, lastname))

            return redirect(url_for('home'))
        except Exception as e:
            print(f"Error processing sign-out form: {e}")
            # Add any additional error handling or logging as needed

    return render_template('signout.html')

@app.route('/home')
def dashboard():
    return render_template('home.html')
