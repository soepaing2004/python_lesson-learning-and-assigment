student_nmae=input("Enter a name:")
student_mark=input("Enter the student mark:")
fileAppend=open('testFile.txt','a')
fileAppend.write(student_nmae+":"+student_mark+"\n")
fileAppend.close()

f=open('testFile.txt','r')
x=input("Enter a name:")
data=f.readlines()

for line in data:
    if x in line:
        print(line)
    else:
        pass

