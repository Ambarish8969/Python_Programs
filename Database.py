import sqlite3

conn=sqlite3.connect("test.db")

cur=conn.cursor()

# cur.execute("drop table if exists Students")
# cur.execute('create table Students(usn varchar(11),name varchar(50))')
# cur.execute('insert into Students values ("2kd18ec004","ambarish")')
# conn.commit()

cur.execute('select * from Students')
for row in cur:
    print(row)
conn.close()