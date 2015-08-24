import sqlite3

with sqlite3.connect("cars.db") as connection:
	curs = connection.cursor()
	curs.execute("CREATE TABLE inventory(make TEXT, model TEXT, quantity INT)")
