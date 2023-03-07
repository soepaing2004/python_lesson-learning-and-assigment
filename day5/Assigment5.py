def add(x,y):
    return x*5,y*5

result=add(3,2)
print(result)

def outerFun(a,b):
    def innerFun(c,d):
        return c+d

    return innerFun(a,b)
res=outerFun(5,10)
print(res)


def fun1(name,age):
    print(name,age)

fun1(name='Emma',age=23)

def shoe_info(item,quality,price):
    return quality * price
    print(price)
price=shoe_info("Cola",2,500)


def displayPerson(age,name):
    print(str(name)+"is"+str(age)+"yers old")
displayPerson("Kyaw Kyaw",28)


x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
print("Add")
print("sub")
print("muli")
print("div")
choice=input("Choice your operation:")
if choice=="add":
    print(x+y)
elif choice=="sub":
    print(x-y)
elif choice=="mul":
    print(x*y)
elif choice=="div":
    print(x/y)
else :
    print("Invalid input")



x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))

def Add(x,y):
    print(x+y)
def Sub(x,y):
    print(x-y)
def Muli(x,y):
    print(x*y)
def Divide(x,y):
    print(x/y)
print("add")
print("sub")
print("mul")
print("div")
choice=input("Choice your operation number:")
if choice=="add":
    print(Add(x,y))
elif choice=="sub":
    print(Sub(x,y))
elif choice=="mul":
    print(Muli(x,y))
elif choice=="div":
    print(Divide(x,y))
else :
    print("End of program")


x=input("Enter the name of your city:")
y=int(input("Enter the temperature of the "+x+"in Celsius is:"))
c=y*1.8+32

print("Temperature of the ",x,"in Fahrenheit is",c)











