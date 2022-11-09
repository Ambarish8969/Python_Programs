import sqlite3

email_list=[]
password_list=[]

conn=sqlite3.connect('facebook.db')
cur=conn.cursor()

cur.execute('select email from Users')
for row in cur:
    email_list.append(row[0])
cur.execute('select password from Users')
for row in cur:
    password_list.append(row[0])

def signin():
    # Email verification....
    email=input("Enter your email : ")
    if(email in email_list):
        # Password verification....
        password=input("Enter your password : ")
        if(password in password_list):
            print("Loggedin Succesfully")
        else:
            print("Invalid Password")
    else:
        print("Invalid emailid")

conn.close()