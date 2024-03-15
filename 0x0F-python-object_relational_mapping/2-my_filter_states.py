#!/usr/bin/python3
"""
script that takes an argument and displays all values in
the states table of the database where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # the four arguments taken
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    # connect to MySQL server
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=username, passwd=password, db=database)
    # create cursor to access
    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE states.name LIKE BINARY\
            '{}' ORDER BY id ASC".format(state)
    cursor.execute(query)
    rows = cursor.fetchall()
    # display results
    for row in rows:
        print(row)
    # don forget to close connection
    cursor.close()
    connection.close()
