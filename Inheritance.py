class Father:

    def method1(self):
        print("Method 1 working")

class Son(Father):  # Father is inherited by Son
    
    def method2(self):
        print("Method 2 working")

obj=Father()
obj.method1()

obj2=Son()  # Son can use both method1 and method2 because of Inheritance.
obj2.method2()
