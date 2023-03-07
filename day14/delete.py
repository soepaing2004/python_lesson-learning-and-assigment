file=open('testFile.txt',"r")
lines=file.readlines()
file.close()
del lines[1]

new_file=open("testFile.txt","w")
for line in lines:
    new_file.write(line)
new_file.close()