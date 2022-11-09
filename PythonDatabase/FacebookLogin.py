import sqlite3
import CheckUser

conn=sqlite3.connect('facebook.db')
cur=conn.cursor()

def signup():
    name=input("Enter your Name : ")
    email=input("Enter your email : ")
    password=input("Enter your password : ")
    cur.execute(f"insert into Users values('{name}','{email}','{password}')")
    conn.commit()
    print(f"Thank you for SignUp {name}")

print("WELCOME TO FACEBOOK")
print("Please select your choice...")
print("1 for SignUp")
print("2 for SignIn")
user_choice=input()
if(user_choice=="1"):
    signup()
elif(user_choice=="2"):
    CheckUser.signin()
conn.close()