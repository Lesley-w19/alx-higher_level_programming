#!/usr/bin/python3
"""
5-filter_cities.py
 a script that takes in the name of a state as an
 argument and lists all cities of that state, using the
 database hbtn_0e_4_usa
"""


from sys import argv
import MySQLdb


def main():
    username = argv[1]
    passwrd = argv[2]
    db_name = argv[3]
    search_input = argv[4]

    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=passwrd,
        db=db_name,
        charset="utf8"
    )
    cur = db_connect.cursor()
    cur.execute("SELECT cty.name FROM cities cty\
        INNER JOIN states st ON cty.state_id = st.id\
        WHERE st.name = %s", (search_input,))
    
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db_connect.close()


if __name__ == '__main__':
    main()
