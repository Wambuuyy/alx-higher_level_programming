#!/usr/bin/python3
"""
script that takes an argument(name of state) and displays all cities in
the state  of the database where name matches the argument
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
    query = """
        SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        GROUP BY states.name
        """
    cursor.execute(query, (state,))
    result = cursor.fetchone()
    # display results
    if result:
        print(result[0])
    else:
        print("")
    # don forget to close connection
    cursor.close()
    connection.close()
