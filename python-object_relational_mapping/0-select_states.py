#!/usr/bin/python3
"""
Get all states
Creates a connection to a given db
then executes a query and print the respective rows
"""
import sys
import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3],
                     port=3306)
cur = db.cursor()
cur.execute("SELECT id, name FROM states")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
db.close()
