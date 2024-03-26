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
    user_input = sys.argv[4]
    query0 = """
            SELECT a.name
            FROM cities a
            INNER JOIN states b
            ON a.state_id = b.id """
    query1 = "WHERE b.name = %s"
    queryf = query0 + query1
    cur.execute(queryf, (user_input,))
    rows = cur.fetchall()

    tmp = []
    for row in rows:
        tmp.append(row[0])
    print(*tmp, sep=", ")

    cur.close()
    db.close()
except MySQLdb.Error as e:
    print("MySQL Error:", e)
except IndexError:
    print("Usage: ./script.py <username> <password> <table> <state>")
except Exception as e:
    print("An error occurred:", e)
