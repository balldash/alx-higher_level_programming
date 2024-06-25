#!/usr/bin/python3
'''
Lists all states from the database
'''
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,  user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = c.fetchall()
    for result in results::
        print(result)
    c.close()
    db.close()
