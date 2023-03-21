x=input("Enter a word:")
number=0
for i in x:
    if (i.lower()== "a"):
        number+=1
    elif (i.lower()=="e"):
        number+=1
    elif (i.lower()=="i"):
        number+=1
    elif (i.lower()=="o"):
        number+=1
    elif (i.lower()=="u"):
        number+=1

print("There are",number,"vowel in this word.")