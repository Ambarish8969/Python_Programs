class Account:
    def __init__(self,username,password):
        self.username=username
        self.__password=password

    def showDetails(self):
        print(self.username+" "+ self.__password)

    def setPassword(self,password):
        if(password[0] in [1,2,3,4,5,6,7,8,9,0]):
            print("Enter valid password")
        else:
            self.__password=password
            print("Password Saved in Database")

    def getPassword(self):
        print(self.__password)

class Account2(Account):
    def printName(self):
        print(self.username,self.getPassword())

    

obj=Account2("ambarish","1233456")
obj.showDetails()
obj.setPassword("1233456")