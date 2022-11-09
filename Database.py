import sqlite3

conn=sqlite3.connect("test.db")

cur=conn.cursor()

cur.execute("drop table if exists Students")
cur.execute('create table Students(name varchar(11),phno number(10))')
cur.execute('insert into Students values ("ambarish",9900408969)')
conn.commit()

cur.execute('select phno from Students')
for row in cur:
    print(type(row[0]))
conn.close()