# Day 70

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'python',
    password = 'python',
    database = 'day070'
)

mycrusor = mydb.cursor()
#mycrusor.execute("CREATE TABLE customers (ID INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), address VARCHAR(255))")
mycrusor.execute('DESC customers')
for x in mycrusor:
    print(x)
mycrusor.execute('SELECT DATABASE()')
for x in mycrusor:
    print(x)
mycrusor.execute('SHOW DATABASES')
for x in mycrusor:
    print(x)

