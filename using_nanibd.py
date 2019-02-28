import sqlite3

con = sqlite3.connect('nani.bd')
cur = con.cursor()

cur.execute('insert into name values("Giovani", 36)')
cur.execute('insert into name values("Ledesma", 27)')
cur.execute('select * from name')

for x in cur.fetchall():
    print(x)

cur.close()
con.commit()
con.close()
