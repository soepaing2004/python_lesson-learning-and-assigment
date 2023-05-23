def add(a,b):
    return a+5,b+5

res=add(3,2)
print(res)

x=(1,2,3,4,5)
y=(6,7,8)
a=x+y
print(a)
l=[9,10,11]
p=l.index(9)
l[p]=90
t=tuple(l)
print(t)
i=a+t
print(i)

def fun1(num):
    return num+5
a=fun1(5)
print(a)

def outerfun(a,b):
    def innerfun(c,d):
        return c+d
    return innerfun(a,b)
res=outerfun(5,10)
print(res)

def fun1(name,age):
    print(name,age)
fun1('Emma',23)

x={False:"Hello"}
print(x)

tuple=(1,(1,2,3))
print(tuple[1])

x=0
for i in range(0,10+1):
    x=x+i
print(x)

x=0
y=1
while y<=10:
    x=y+x
    y=y+1
print(x)

a=[]
x=int(input("Enter the number of elements:"))
for x in range(0,x):
    y=int(input("Enter a number:"))
    if y%2==0:
        a.append(y)
print(a)
b=a.index(4)
a[b]=30
print(a)
a.pop(2)
a.insert(2,40)
print(a)


#recursion
def a(x):
    if x==1:
        return 1
    else :
        return (x+ a(x-1))
y=10
print(a(y))

x={1:"Cat",2:"Rabbit",3:"Dog",4:"Snake"}
x[4]="Goat"
print(x)
print(x.get(2))
del x[2]
print(x)
print(x.keys())
print(x.values())
print(sorted(x,reverse=True))
print(len(x))
x.clear()# clear function doesn't take arguments
print(x)


x=[1,4,3,7,5,9]
x.append(2)
print(set(x))
y=x.index(3)
x[y]=30
print(set(x))
i={1,2,3}
o={"TunTunn","KyawKyaw","MgMg"}
p=zip(i,o)
print(set(p))
s=(3,5,80,29,6)
print(set(s))
print(len(s))

