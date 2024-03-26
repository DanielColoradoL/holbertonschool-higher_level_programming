#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """
import sys
import MySQLdb

try:
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    query = """
            SELECT a.id, a.name, b.name
            FROM cities a
            INNER JOIN states b
            ON a.state_id = b.id"""

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
except MySQLdb.Error as e:
    print("MySQL Error:", e)
except IndexError:
    print("Usage: ./script.py <username> <password> <table>")
except Exception as e:
    print("An error occurred:", e)
