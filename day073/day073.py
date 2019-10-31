# Day 73
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'python',
    password = 'python',
    database = 'test'
)
mycursor = mydb.cursor()
###################################

mycursor.execute('UPDATE customers SET name = "Rani" WHERE name = "Max"')
mydb.commit()
mycursor.execute('SELECT * FROM customers')
for x in mycursor:
    print(x)