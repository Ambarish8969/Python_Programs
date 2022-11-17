class Account:
    def __init__(self,accno,bal,owner,bankname):
        self.accno=accno
        self.bal=bal
        self.owner=owner
        self.bankname=bankname

    def showDetails(self):
        print(self.accno)
        print(self.bal)
        print(self.owner)
        print(self.bankname)

    def deposit(self,amt):
        self.bal=self.bal+amt
        print(f"Current bal : {self.bal} , Deposit ammount : {amt}")

    def withdraw(self,amt):
        self.bal=self.bal-amt
        print(f"Current bal : {self.bal} , Withdraw ammount : {amt}")

class Savings(Account):
    roi=0.005
    def calculateroi(self):
        self.bal=self.bal+self.bal*self.roi
        print(self.bal)

class Current(Account):
    minimumBalance=50000.0
    def showMinimumBal(self):
        print(self.minimumBalance)

obj1=Savings(14378411789,20000.0,"Namrata","ICICI")
obj1.showDetails()
obj1.deposit(10000)

obj2=Current(4567841164,10000.0,"Ambarish","ICIC908")
obj2.showMinimumBal()