# 29 Write a program to accept a filename from the user and display all the lines from the file which contain # symbol
filename=input("Enter filename:")
myfile=open(filename,"r")
text=myfile.read()
count=0
for i in text:
    if i=='#':
        count=count+1
print(count)