
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
a=['add','minus','mul','divide']
print(a)
i=input("Enter a choice")
if i.lower()=='add':
    print(x+y)
elif i.lower()=='minus':
    print(x-y)
elif i.lower()=='mul':
    print(x*y)
elif i.lower()=='divide':
    print(x/y)
else:
    print("Enter a valid option.")
