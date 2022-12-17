class User:
    def __init__(self,username,password):
        self.username=username
        self.__password=password

    def showDetails(self):
        print(f"username : {self.username}, password : {self.__password}")

    def getPassword(self):
        return(f"{self.__password}")

    def setPassword(self):
        password=input("Enter new password : ")
        self.__password=password
        print("Password Saved Successfully")

class Login(User):

    def __init__(self, username, password):
        super().__init__(username, password)
    
    def login(self):
        if(self.username=="ambarish"):
            if(self.getPassword()=="ambi@00"):
                print("Success")
            else:
                print("Forgot Password...?")
                self.setPassword()
                self.getPassword()
        else:
            print("Invalid username")

pwd=input("password : ")
object1=Login("ambarish",pwd)
object1.login()