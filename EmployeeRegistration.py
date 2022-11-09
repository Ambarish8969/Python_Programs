import sqlite3
conn=sqlite3.connect('test.db')
cur=conn.cursor()

# # cur.execute("drop table if exists Employees")
# # cur.execute('create table Employees(Name varchar(20),Phno number(10),id number(5),exp number(2))')
class EmployeeRegistration:

    def __init__(self,name,email_phno,eid,exp):
        self.name=name
        self.email_phno=email_phno
        self.eid=eid
        self.exp=exp

    def getDetails(self):
        print(self.name,self.email_phno,self.eid,self.exp)

for i in range(2):
    name=input("Enter employee name : ")
    phno=int(input("Enter employees phone-number : "))
    id=int(input("Enter employees id : "))
    exp=int(input("Enter experience : "))

    obj=EmployeeRegistration(name,phno,id,exp)
    # obj.getDetails()

    cur.execute(f"insert into Employees (Name,Phno,id,exp) values ('{name}','{phno}','{id}','{exp}')")
    conn.commit()
cur.execute('select * from Employees')
for row in cur:
    print(row)





conn.close()
