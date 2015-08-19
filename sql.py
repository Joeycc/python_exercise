import sqlite3

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''
	CREATE TABLE food (
		id		TEXT PRIMARY KEY,
		desc 	TEXT,
		water 	FLOAT
	)
    ''')
query = 'INSERT INTO food VALUES ("hgo", "ett", 11.3)'

curs.execute(query)
conn.commit()
conn.close()