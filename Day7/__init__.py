#Tuple
#Tuple can not  be changed the value

x=(1,2,3,4,5)
y=(6,7)
a=x+y
print(a)

x=(1,2,3,4)
y=(5,6,7)
a=x+y
print(a)
l=[8,9,10]
t=tuple(l)
print(t)
s=a+t
print(s)

#Set{}
#Set also can not be changed
#Set cann't index
x={1,2,3}
print(type(x))
print(x)


#Dicdionary (Eg. is in phone contact)
#Key value pair
x={1:"Hello",2:"World"}
print(type(x))
print(x[1]) #x[1] is key and dic cann't print value directly
print(x.get(2))
x[3]="Rabbit"
print(x)
del x[3]
print(x)

x={(1,2,3,4,5):"Hello","Cat":"World"}# list cann't be used in key position

print(x.values())
print(x.keys())

keys=(1,2,3)
values=["Dog","Cat","Bird"]

x=zip(keys,values)
print((dict(x)))


