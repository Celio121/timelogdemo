# pytesting app.py

from app import time_in, time_out # importing from app to test functions
import sqlite3

# Testing time_in function
def test_time_in():
    firstname = "testin"
    lastname = "testin"

    # Running the time_in function
    time_in(firstname, lastname)

    # Assert that the data that was added to the database correctly without any issues
    with sqlite3.connect("timelogged.db") as connection:
        cursor = connection.commit()
        cursor.execute("SELECT fitsname, lastname, signins FROM timelogs WHERE firstname=? AND lastname=?", (firstname, lastname))
        result = cursor.fetchone()

    assert result is not None
    assert result[0] == firstname
    assert result[1] == lastname
    assert result[2] == 1 # Signing should be set to True (1) for signing-in

    # testing time_out finction
def test_time_out():
    firstname = "testout"
    lastname = "testout"

    # Run the time_out function
    time_out(firstname, lastname)

    # Assert that the data that was added to the database correctly without any issues
    with sqlite3.connect("timelogged.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT firstname, lastname, signing FROM timelogs WHERE firstname=? AND lastname=?", (firstname, lastname))
        result = cursor.fetchone()

    assert result is not None
    assert result[0] == firstname
    assert result[1] == lastname
    assert result[2] == 0 # Signing should be set to False (0) for signing-out