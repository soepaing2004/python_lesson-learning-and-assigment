class Operation:
    def factorial(self):
        factorial_number=int(input("Enter a number that you want his factorial series number:"))
        a=1
        for b in range(2,factorial_number+1):
            c=a*b
            a=c
            print(c)
    def fibonacci(self):
        fibonacci_number=int(input("Enter a number that you his fibonacci series:"))
        x=0
        y=1
        for z in range(0,fibonacci_number):
            print(x)
            z=x+y
            x=y
            y=z
    def sum(self):
        sum_number=int(input("Enter a number that you want his sum of all number from 0:"))
        x=0
        for y in range(1,sum_number+1):
            x=x+y
            print(x)
    def prime(self):
        prime_number=int(input("Enter a number to check taht is a prime number or not:"))
        x=0
        if (prime_number==1):
            print(prime_number," is not a prime number.")
        else :
            for y in range(2,prime_number):
                if (prime_number%y==0):
                    x+=1
                    break
            if (x==1):
                print(prime_number," is not a prime number.")
            else :
                print(prime_number," is a prime number.")

class Option(Operation):
    print("This is a program that's calculate about the factorial number,"+"\n"+"fibonacci number,"+"\n"+"the sum of all the that you enter from 0 "+"\n"+"and prime number.")
user_input=input("Enter an option that you want to do:")
if (user_input.lower() == "factorial"):
    Option().factorial()
elif (user_input.lower() == "fibonacci"):
    Option().fibonacci()
elif (user_input.lower() == "sum"):
    Option().sum()
elif (user_input.lower() == "prime"):
    Option().prime()
