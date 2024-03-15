#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # the three arguments taken
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    #connect to MySQL server
    connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    # create cursor to access
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    #display results
    for row in rows:
        print(row)
    # don forget to close connection
    cursor.close()
    connection.close()
