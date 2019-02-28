import sqlite3

bank = sqlite3.connect('surfersDB.sdb')
bank.row_factory = sqlite3.Row
cursor = bank.cursor()
cursor.execute('select * from surfers where age > 25')
lines = cursor.fetchall()

for line in lines:
    print('Name    :', line['name'])
    print('Country :', line['country'])
    print('Average :', line['average'])
    print('Board   :', line['board'])
    print('Age     :', line['age'])
    print()
cursor.close()