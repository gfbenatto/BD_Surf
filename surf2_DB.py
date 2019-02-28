import sqlite3

bank = sqlite3.connect('surfersDB.sdb')
bank.row_factory = sqlite3.Row
cursor = bank.cursor()
cursor.execute('select name, average from surfers where age > 20 order by average desc')

lines = cursor.fetchall()
for line in lines:
    print('Name    :', line['name'])
    print('Average :', line['average'])
    print()
cursor.close()