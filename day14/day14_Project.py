def Calculator():

    try:
        file = open('day14project.txt', 'a')
        first_number = int(input("Enter 1st number:"))
        second_number = int(input("Enter 2nd number:"))
        print(
            "Enter a option that you want to do with two numbers that you enter and the results will be store to a file" + "\n" +
            "Enter '+' to add two numbers" + "\n" + "Enter '-' to subtract two numbers" + "\n" + "Enter '*' to multiple the two numbers" + "\n" +
            "Enter '/' two divide two numbers.")
        user_option = input("Enter an option:")

        if user_option == "+":
            print(first_number+second_number)
            print("The result will be stored to the file.")
            add=str(first_number+second_number)
            file.write(str(first_number)+"+"+str(second_number)+"="+add+"\n")
            file.close()

        elif user_option == "-":
            print(first_number - second_number)
            print("The result will be stored to the file.")
            subtract=str(first_number-second_number)
            file.write(str(first_number)+"-"+str(second_number)+"="+subtract+"\n")
            file.close()

        elif user_option == "*":
            print(first_number * second_number)
            print("The result will be stored to the file.")
            multiplication=str(first_number * second_number)
            file.write(str(first_number)+"*"+str(second_number)+"="+multiplication+"\n")
            file.close()


        elif user_option == "/":
            print(first_number / second_number)
            print("The result will be stored to the file.")
            division=str (first_number/second_number)
            file.write(str(first_number)+"/"+str(second_number)+"="+division+"\n")
            file.close()

    except ValueError:
        print("You can't put a character.Put the numbers again.")
        Calculator()

    except ZeroDivisionError:
        print("You can't divide by zero.Choose again the numbers.")
        Calculator()

    except Exception:
        print("There are something is wrong.Please,put again the input and also choose the operation.")
        Calculator()


Calculator()
