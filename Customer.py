class Customer:

    def __init__(self,name,id,password):
        self.name=name
        self.id=id
        self.password=password
    
    def displayDetails(self):
        print(self.name,self.id,self.password)

obj=Customer("Ambarish",4658,"ambarish@00")
obj.displayDetails() 