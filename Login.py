class Login:

    def __init__(self,email_phno,password):
        self.email_phno=email_phno
        self.password=password

    def getDetails(self):
        print(self.email_phno,self.password)

obj=Login("ambarish8653@gmail.com","ambi@00")
obj.getDetails()