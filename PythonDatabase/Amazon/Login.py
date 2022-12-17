import sqlite3
import Dbcode

conn=sqlite3.connect("Amazon.db")
cur=conn.cursor()
class Amazon:
    pass

    # def __init__(self,username,password):
    #     self.username=username
    #     self.password=password

    

class CustomerLogin(Amazon):

    # def __init__(self,username,password):
    #     self.username=username
    #     self.password=password

    def addCustomer(self):
        # cur.execute("drop table if exists Customers")
        # cur.execute('create table Customers(Username varchar(50),Phno number(10),Password varchar(20))')
        username=input("Enter username : ")
        password=input("Enter password : ")
        phno=int(input("Enter phno : "))
        cur.execute(f"insert into Customers values('{username}','{phno}','{password}')")
        conn.commit()
        
    def showDetails(self):
        phno1=int(input("Enter phno : "))
        if(phno1 in Dbcode.phno_list):
            cur.execute(f"select * from Customers where Phno={phno1}")
            for i in cur:
                print(i)

    def login(self):
        if(self.username=="ambarish"):
            if(self.password=="ambi@00"):
                print("Successfully LoggedIn")
            else:
                print("Invalid Password")
        else:
            print("Invalid Username")


obj1=CustomerLogin()
#obj1.addCustomer()
obj1.showDetails()