class Father:

    def method1(self):
        print("Method 1 working")

class Son(Father):

    def method2(self):
        print("Method 2 working")

obj=Father()
obj.method1()

obj2=Son()
obj2.method2()
