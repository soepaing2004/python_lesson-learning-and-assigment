#passed by value
#passed by reference
#scope #local variable #global variable
def update(x):
    print(id(x))
    x=15
    print(id(x))
    print(x)

a=1
print(id(a))
update(a)

def something():
    global a #if you want to change the local to global use global keyword;
    a=14
    print(a)

a=1
something()
print(a)