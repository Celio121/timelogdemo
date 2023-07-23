import pytest
import sqlite3
from app import app, db_create

connection = sqlite3.connect('timelogged.db')
db_create(connection)

# Checking to see if the table is created
cursor = connection.cursor()
cursor.execute("INSERT INTO timelogs(firstname, lastname, signing, time) VALUES ('testin', 'testin', 1, '2023-07-23 14:30:00')") # inputting signin data
connection.commit()

# testing the routes in the flask app
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Home page testing
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Home Page" in response.data
    assert b"Go to sign-in" in response.data
    assert b"Go to sign-out" in response.data

# Sign in page testing
def test_signin_page(client):
    response = client.get('/signin')
    assert response.status_code == 200
    assert b"Sign In" in response.data
    assert b"First Name:" in response.data
    assert b"Last Name:" in response.data
    assert b"type=\"submit\" value=\"Sign In\"" in response.data


# Signout page testing
def test_signout_page(client):
    response = client.get('/signout')
    assert response.status_code == 200
    assert b"Sign Out" in response.data  # Corrected the button text here
    assert b"First Name:" in response.data
    assert b"Last Name:" in response.data
    assert b"type=\"submit\" value=\"Sign Out\"" in response.data

# return to dashboard testing
def test_dashboard_page(client):
    response = client.get('/home')
    assert response.status_code == 200
    assert b"Welcome to the Home Page" in response.data
    assert b"Go to sign-in" in response.data
    assert b"Go to sign-out" in response.data

# checked signin redirect routing
def test_signin_post(client):
    data = {'firstname': 'testin', 'lastname': 'testin'}
    response = client.post('/signin', data=data, follow_redirects=True)
    assert response.status_code == 200  # Check if the redirect was successful
    assert b"Welcome to the Home Page" in response.data

# checked signout redirect routing
def test_signout_post(client):
    data = {'firstname': 'testout', 'lastname': 'testout'}
    response = client.post('/signout', data=data, follow_redirects=True)
    assert response.status_code == 200  # Check if the redirect was successful
    assert b"Welcome to the Home Page" in response.data
