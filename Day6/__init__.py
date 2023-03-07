#List is used to stored multiple values in a single vriable

x=["Hello","Hi","MgMg",2,2.5]
print(type(x))


x=[1,3,5,7,9]   #empty list

#index start from 0
#- index start from back

print(x[-1])

#slice

x=[1,2,3,4,5,6,7]

print(x[1:3])

#nested list
x=[[1,2,3,4,5],[33,4,455,6,66]]
print(x)


x=[2,3,4,5,6]

x.append(3)
print(x)

x.insert(3,"Hello") #insert function must have two arguments,1st is index and 2nd place is value
print(x)

x.remove(3) #remove function directly remove the value not index
print(x)

x.pop(2)  #pop function remove automatically the last value if you don't put any index in function
print(x)

del x[2:]
print(x)

x.extend([3,4,5]) #extend function join two element
print(x)

print(min(x)) #min function find the minimum value
print(max(x))  #max function find the maximum value

x.sort() #sort function does min to max
print(x)


x.reverse() #reverse function print value from last to start
print(x)

print(len(x)) #len function find the quantity of element



List=[]
n=int(input("Enter number of element:"))

for i in range(0,n):

    x=int(input("Enter number:"))

    List.append(x)

print(List)

