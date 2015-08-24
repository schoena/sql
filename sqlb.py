import sqlite3

with sqlite3.connect("new.db") as conn:
	curs = conn.cursor()
	curs.execute("INSERT INTO population VALUES('New York City', \
		'NY', 8200000)")
	curs.execute("INSERT INTO population VALUES('San Francisco', \
		'CA', 800000)")