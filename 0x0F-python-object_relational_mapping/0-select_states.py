#!/usr/bin/python3
"""
A  script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

# Connect to the database
my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],db=argv[3], port=3306)
# Create cursor obj to interact with database
my_cursor = my_db.cursor()

# Execute a SELECT query to fetch data
my_cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

# fetch all the data returned by the query
my_data = my_cursor.fetchall()

# Iterate through the fetched data and print each row
for row in my_data:
print(row)

# Close all cursors
my_cursor.close()

# Close all databases
my_db.close()
