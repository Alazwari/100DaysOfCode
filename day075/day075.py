# Day 75
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    port = '8889',
    user = 'python',
    password = 'python',
    database = 'MyEmoloyees'
)
mycursor = mydb.cursor()
###################################
# Create the table:
#table = 'CREATE TABLE Employee(ID INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(100), LastName VARCHAR(100), Age INT, Gender VARCHAR(20), Salary INT)'
#mycursor.execute(table)

# Insert Values:
# insert_data = 'INSERT INTO Employee(FirstName, LastName, Age, Gender, Salary)\
# Values\
#     ("Ahmed", "Ali", 30, "Male", 10000),\
#     ("Khalid", "Muhammed", 34, "Male", 7000),\
#     ("Norah", "Saleh", 29, "Female", 7000)'
# mycursor.execute(insert_data)
# mydb.commit()


mycursor.execute('SELECT * FROM Employee')
for x in mycursor:
    print(x)
print('-----------------------------------------------------')
mycursor.execute('SELECT FirstName, Gender, Salary FROM Employee')
for x in mycursor:
    print(x)
print('-----------------------------------------------------')
mycursor.execute('SELECT * FROM Employee ORDER BY FirstName DESC')
for x in mycursor:
    print(x)
delete_34 = 'DELETE FROM Employee WHERE Age = 34'
mycursor.execute(delete_34)
mydb.commit()
print('-----------------------------------------------------')
mycursor.execute('SELECT * FROM Employee')
for x in mycursor:
    print(x)