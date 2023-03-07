aList=['a','b','c','d']
newList=list(aList)
print(newList)


listOne=['a','b','c','d']
listTwo=['e','f','g']

newList=listOne.extend(listTwo)
print(newList)

sampleList=[10,20,30,40]
del sampleList[0:6]
print(sampleList)


sampleList=[10,20,30,40,50]
sampleList.pop()
print(sampleList)
sampleList.pop(2)
print(sampleList)


aList=[10,20,30,40,50,60,70,80]
print(aList[2:5])
print(aList[:4])
print(aList[3:])

sampleList=[10,20,30,40,50]
print(sampleList[-2])
print(sampleList[-4:-1])

sampleList=[10,20,30,40,50]
sampleList.append(60)
print(sampleList)

sampleList.append(60)
print(sampleList)

n=[1,2,3,4,5,6,7]
for s in n:
    print(s**2)

list=[1,2,3]
v=[v**2 for v in list]
print(v)


x=int(input("Enter a number:"))
while 1<=x:
    print(x**2,end='')
    x=x-1

x=int(input("Enter a number:"))
for x in range(1,x+1):
    print(x**2)


x=[10,20,30,40,60,20,40]
print(x[3])
x.remove(40)
print(x)
x.insert(3,200)
print(x)


x=[10,20,30,40,40,50,50]
s=x.index(40)
x[s]=200
print(x)

x=["Hla Hla","Mg Mg","Emma","Kyaw Kyaw"]
x.pop(1)
print(x)

y=[]
x=int(input("Enter number of element:"))
for x in range(0,x):
    i=int(input("Enter a number:"))
    y.append(i)
print(y)
j=y[0] if y else None
for f in y:
    if f<j:
        f=j
print(j)


y=[]
x=int(input("Enter the number of element:"))
for x in range(0,x):
    i=int(input("Enter a number:"))
    if i%2!=0:
        y.append(i)
print(y)

a=["M","na","i","Soe"]
b=["y","me","s","Paing"]
c=[]
for i in range(4):
    c.append(a[i]+b[i])
print(c)

x=["Dear","take"]
y=["Sir","care"]
a=[]
for i in range(2):
        a.append(x[i]+y[i])
print(a)









