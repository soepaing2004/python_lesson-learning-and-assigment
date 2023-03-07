class A:
    def method1(self):
        print("This is from A")

class B(A):
    def method2(self):
        print("This is from B")
class C(B):
    def method3(self):
        print("This is from C")
C().method1()
C().method2()
C().method3()