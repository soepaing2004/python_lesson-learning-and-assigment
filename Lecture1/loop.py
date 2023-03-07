i=1
while i<6:
    print("Hello")
    i=i+1

i=1 #i=1
while i<6 :
    print(i)
    i=i+1 #incremental

x=5
while x>=1:
    print(x)
    x=x-1 #decremental
print("End of program")

#HElloHiHiHi
#HElloHiHiHi
#HElloHiHiHi
i=1
j=1
while i<=3:
    print("Hello",end='')
    while j<=4:
        print("Hi",end='')
        j=j+1
    i=i+1
    j=1
    print()


#for loop
x=["Hello",5,5.0] #list

for i in x :
    print(i)

#range

for i in range(1,31):
    if i%3==0:
        print(i)

for i in range(11):
    print(i)


x=int(input("Enter a number:"))
for x in range(1,x+1):
    print(x,'+',end='')


x=int(input("Enter a number:"))
m=0
for x in range(1,x+1):
    m=m+x
    print(m)


x=int(input("Enter a number:"))
s=0
while x>=1:
    s=s+x
    print(s)
    x=x-1


x=int(input("Enter a number:"))
for i in range(1,11):
    print(x*i)







