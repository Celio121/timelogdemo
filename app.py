from datetime import datetime
import sqlite3

def db_create():
    with sqlite3.connect("timelogged.db") as connection:
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

def time_in(firstname, lastname):
    with sqlite3.connect("timelogged.db") as connection:
        cursor = connection.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("""INSERT INTO timelogs(
                       firstname,
                       lastname,
                       signing,
                       time
                    ) VALUES (?, ?, ?, ?)""", (firstname, lastname, True, current_time,))
        connection.commit()

def time_out(firstname, lastname):
    with sqlite3.connect("timelogged.db") as connection:
        cursor = connection.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("""INSERT INTO timelogs(
                       firstname,
                       lastname,
                       signing,
                       time
                    ) VALUES (?, ?, ?, ?)""", (firstname, lastname, False, current_time,))
        connection.commit()

if __name__ == '__main__':
    db_create()

    while True:
        choice = input("Enter '1' for Sign-In, '2' for Sign-Out, or 'q' to quit: ")

        if choice == '1':
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")
            time_in(firstname, lastname)
            print("Sign-In recorded.")

        elif choice == '2':
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")
            time_out(firstname, lastname)
            print("Sign-Out recorded.")

        elif choice.lower() == 'q':
            break

        else:
            print("Invalid choice. Please try again.")
