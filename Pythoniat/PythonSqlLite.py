import sqlite3
import sys

conn = sqlite3.connect("mydb.db")
conn.execute('CREATE TABLE students(num INTEGER PRIMARY KEY , name VARCHAR(10))')
conn.execute('INSERT into students values(1 , "yassine")')
conn.commit()