#!/usr/bin/python3
"""
3-my_safe_filter_states
Yes, it’s an SQL injection to delete all records of a table…

Once again, write a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where name
matches the argument. But this time, write one that is safe
from MySQL injections!
"""


from sys import argv
import MySQLdb


def main():
    username = argv[1]
    passwrd = argv[2]
    db_name = argv[3]
    st_nput = argv[4]

    db_connect = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=passwrd,
        db=db_name,
        charset='utf8'
    )

    cur = db_connect.cursor()

    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", {st_nput})
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db_connect.close()


if __name__ == "__main__":
    main()
