import sqlite3
conn=sqlite3.connect("Amazon.db")
cur=conn.cursor()

username_list=[]
phno_list=[]
password_list=[]

cur.execute('select Username from Customers')
for row in cur:
    username_list.append(row[0])
cur.execute('select Phno from Customers')
for row in cur:
    phno_list.append(row[0])
cur.execute('select Password from Customers')
for row in cur:
    password_list.append(row[0])
