# Day 71
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'python',
    password = 'python',
    database = 'day070'
)
mycursor = mydb.cursor()
sql = 'INSERT INTO customers (name, address) VALUES(%s, %s)'
val = [
    ('John', 'Highway 21'),
    ('Jack', 'Red 321'),
    ('Rani', 'NewWay 651'),
    ('Elx', 'Center 42')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount)


######################3333
mycursor.execute('SELECT * FROM customers')
result = mycursor.fetchall()
for x in result:
    print(x)