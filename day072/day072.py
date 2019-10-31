# Day 72
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'python',
    password = 'python',
    database = 'day070'
)
mycursor = mydb.cursor()
###################################

sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
resulte = mycursor.fetchall()
for x in resulte:
    print(x)

sql = "DROP TABLE customers"
mycursor.execute(sql)

sql = "SHOW TABLES"
mycursor.execute(sql)
for x in mycursor:
    print(x)
