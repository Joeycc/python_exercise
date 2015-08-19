import sqlite3
import sys

conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM FOOD'
curs.execute(query)

for row in curs.fetchall():
	print row