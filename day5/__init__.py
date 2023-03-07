#1.define the function
#2.call the function name
#3.Arguments
#4.Return

def greeting_customer():
    print("Hello ,Nice to meet you")

greeting_customer()

def show(x,y):#parameter
    print(x,y)
show("Helo","World")




x=input("Please,enteryour name;")
def greeting(x):
    print("Hello,"+x)

greeting(x)


def sum_sub(x,y):
    a=x+y
    b=x-y
    return a,b

z,j=sum_sub(5,3)
print(z,j)

#Argument
#1.position
#2.keyword
#3.default

def person(name,age):
    print(name,age)

person("Mgmg",age=32)
