class A:
    def __init__(self):
        print("This is A init method")
    def method1(self):
        print("This is from A")

class B:
    def __init__(self):
        print("This is B init method")
    def method2(self):
        print("This is from B.")

class C(A,B):#super function run the left class method when there are two or more class is inheritance
    def __init__(self):
        super().__init__()
        print("This is C init method")
    def method3(self):
        print("This is from C.")

C()
#C().method2()
#C().method1()
#C().method3()