#!/usr/bin/python3
"""
2-my_filter_states - list searched state by user input
"""


from sys import argv
import MySQLdb


def main():
    username = argv[1]
    passwrd = argv[2]
    db_name = argv[3]
    state_input = argv[4]

    db_connect = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=passwrd,
        db=db_name,
        charset='utf8'
    )

    cur = db_connect.cursor()
    request = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
ORDER BY id ASC".format(state_input)

    cur.execute(request)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db_connect.close()


if __name__ == "__main__":
    main()
