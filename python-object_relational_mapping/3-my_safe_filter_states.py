#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

try:
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    user_input = sys.argv[4]
    query0 = "SELECT id, name FROM states "
    query1 = "WHERE name COLLATE utf8mb4_bin LIKE %s"
    queryf = query0 + query1
    cur.execute(queryf, (user_input, ))
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
