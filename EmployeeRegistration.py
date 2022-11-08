class EmployeeRegistration:

    def __init__(self,name,email_phno,eid,exp):
        self.name=name
        self.email_phno=email_phno
        self.eid=eid
        self.exp=exp

    def getDetails(self):
        print(self.name,self.email_phno,self.eid,self.exp)

obj=EmployeeRegistration("Ambarish",9900408969,4564334,10)
obj.getDetails()