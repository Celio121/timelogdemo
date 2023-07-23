import csv
import sqlite3

# Function to export database data to csv file
def export_csv():
    with sqlite3.connect("timelogged.db") as connection:
        cursor = connection.cursor()

        # Retrieve all the data from timelogs table
        cursor.execute("SELECT * FROM timelogs")
        data = cursor.fetchall()

    # Specifying the csv file name
    csv_file = "timelogs_export.csv"

    # Write data to the file
    with open(csv_file, "w", newline="") as f:
        csv_writer = csv.writer(f)

        # Write header row
        csv_writer.writerow(["ID", "First Name", "Last Name", "Signing", "Time"])

        # Write data rows
        csv_writer.writerows(data)

if __name__ == "__main__":
    export_csv()