#! env python

import sqlite3

db = sqlite3.connect('ru_alive.db')
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS persons(
                email TEXT PRIMARY KEY, 
                first_name TEXT, 
                last_name TEXT,  
                gender TEXT,
                birth_year INTEGER,
                location TEXT, 
                last_seen DATETIME,
                status TEXT
                )''')
