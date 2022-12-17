class A:

    def add(self,a,b):
        print(a+b)
    
class B(A):
    
    def add(self,a,b):
        super().add(a,b)
        print(a*b)
a=B()
a.add(1,2)