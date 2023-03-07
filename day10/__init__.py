#OOP

class Mammals:
    legs=2

    def feeding(self):
        print("It feeds milk.")

Mammals()
Mammals.legs=4
print(Mammals.legs)
Mammals.feeding

a='Hello'
print(a.upper())

class Car():
    def __init__(self,name,wheels):
        self.name=name
        self.wheel=wheels

    def kind(self):
        print("The name of car is {},It has {} wheels.".format(self.name,self.wheel))

Car(input(),4)
Car.kind

bugatti=Car("Bugatti",4)
bugatti.kind()

class Temp():
    def __init__(self,name_of_the_city,temperature_in_celsius):
        self.name=name_of_the_city
        self.temperature=temperature_in_celsius

    def farenheit(self):
        a=y*1.8+32
        print("Temperature of "+x+" city in fahrenheit is ",a)

x=input("Enter the nameof the city:")
y=int(input("Enter the "+x+" temperature in celsius:"))
result=Temp(x,y)
result.farenheit()

class Operation():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def operation(self):
        if a.lower()=='add':
            print(x+y)
        elif a.lower()=='sub':
            print(x-y)
        elif a.lower()=='mul':
            print(x*y)
        elif a.lower()=='div':
            print(x/y)
        elif a.lower()=='mod':
            print(x%y)
        else:
            print("Enter a valid option")

x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number"))
print("add"+"\n"+"sub"+"\n"+"div"+"\n"+"mul"+"\n"+"mod")
a=input("Choice the option:")
result=Operation(x,y)
result.operation()
