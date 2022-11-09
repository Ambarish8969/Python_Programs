import sqlite3

connect=sqlite3.connect('test.db')
cursor=connect.cursor()

cursor.execute('select Phno from Employees where Name="Namrata"')
for row in cursor:
    print(row[0])  # Index value is used for unpack the data from tuples.
cursor.execute('select * from Employees')
for row in cursor:
    print(row)  
connect.close()