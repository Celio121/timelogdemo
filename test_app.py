import pytest
import sqlite3
from app import db_create

# test database creation code
def test_db_create():
    connection = sqlite3.connect(":memory:")
    db_create(connection)

    # Checking to see if the table is created
    cursor = connection.cursor()
    cursor.execute("INSERT INTO timelogs(firstname, lastname, signing, time) VALUES ('testin', 'testin', 1, '2023-07-23 14:30:00')") # inputting signin data
    cursor.execute("INSERT INTO timelogs(firstname, lastname, signing, time) VALUES ('testout', 'testout', 0, '2023-07-23 15:30:00')") # inputting signout data
    cursor.execute("SELECT * FROM timelogs WHERE firstname = 'testin'") # fetching signin data
    result = cursor.fetchone()  # Use fetchone() to get the data from the cursor
    # testing table creation and signin
    assert result[1] == 'testin'  # firstname column
    assert result[2] == 'testin'  # lastname column
    assert result[3] == 1         # signing column (1 for True)
    assert result[4] == '2023-07-23 14:30:00'  # time column 

def test_time_out():
    connection = sqlite3.connect(":memory:")
    db_create(connection) # Call db_create to create the timelogs table
    
    cursor = connection.cursor()
    cursor.execute("INSERT INTO timelogs(firstname, lastname, signing, time) VALUES ('testin', 'testin', 1, '2023-07-23 14:30:00')")
    cursor.execute("INSERT INTO timelogs(firstname, lastname, signing, time) VALUES ('testout', 'testout', 0, '2023-07-23 15:30:00')")
    cursor.execute("SELECT * FROM timelogs WHERE firstname = 'testout'") # fetching signout data
    result_out = cursor.fetchone()  # Use fetchone() to get the data from the cursor
    # testing signout
    assert result_out[1] == 'testout'  # firstname column
    assert result_out[2] == 'testout'  # lastname column
    assert result_out[3] == 0          # signing column (0 for False)
    assert result_out[4] == '2023-07-23 15:30:00'  # time column