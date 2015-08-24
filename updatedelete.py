import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE population SET population = 90000000 WHERE city='New York City'")
    #c.execute("DELETE FROM population WHERE city='San Francisco'")

    print "\nNEW DATA:\n"

    c.execute("SELECT * FROM population")
    rows = c.fetchall()
    for r in rows:
        print r[0], r[1], r[2]