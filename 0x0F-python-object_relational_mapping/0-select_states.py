#!/usr/bin/python3
"""
0-select_states
"""


from sys import argv
import MySQLdb


def main():
    user = argv[1]
    passwrd = argv[2]
    db_name = argv[3]

    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        password=passwrd,
        db=db_name,
        charset="utf8"
    )
    cur = db_connect.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db_connect.close()


if __name__ == '__main__':
    main()
