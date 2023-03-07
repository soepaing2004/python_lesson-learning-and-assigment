#File mode"'x','r','w','a'")
file=open('testFile.txt','a')
#print(file.read())# read all file

#print(file.readline())# read first line from file

#print(file.readlines())# read all file and print as a list

file.write("Mg Mg"+"\n")# overwrite the new data delete the older  ---- append also use the write function

file.close()