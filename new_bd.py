import sqlite3

con = sqlite3.connect('nani.bd')
cur = con.cursor()
cur.execute('''create table name(login varchar(8), num integer)''')

cur.close()
con.close()
