import sqlite3

with sqlite3.connect("new.db") as conn:
	curs = conn.cursor()
	try:

	    curs.execute("INSERT INTO population VALUES('New York City', \
		    'NY', 8200000)")
	    curs.execute("INSERT INTO population VALUES('San Francisco', \
		    'CA', 800000)")
	except sqlite3.OperationalError:
		print "Something went wrong. Try again..."