
x=2
print(x)# compiletime error

#Logical error
x=input("Enter a number:")
y=input("Enter a number:")
print(x+y)

#Runtime error
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print(a/b)

#try block
print("Open")
try:
    h=int(input("Enter a number:"))
    i=int(input("Enter a number:"))
    print(h/i)
#except Exception as e:
 #   print("Don't enter a character.")

except Exception as e:
    print("You can't divide by zero.")
#except ZeroDivisionError:
#    print("You can't divide by zero.")
#except Exception:
#    print("Invalid.")
else:
    print("End")# your choice
finally:
    print("Close.")

try:
    input1=int(input("Enter a number:"))
    input2=int(input("Enter a number:"))
    print(input2)
except ValueError:
    print("You can't put an error")
