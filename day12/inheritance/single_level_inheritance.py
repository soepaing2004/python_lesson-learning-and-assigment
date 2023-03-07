class A:
    def __init__(self):
        print("This is A init method")
    def method1(self):
        print("This is method1")


class B(A):
    def __init__(self):
        super().__init__()
        print("This is B init")
    def method2(self):
        print("This is method2.")

B()
B().method1()
B().method2()
#a=A()
#b=B()
#a.method1()
#b.method2()


